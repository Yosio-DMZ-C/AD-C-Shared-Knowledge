#!/usr/bin/env python3
"""Generate an offline AD&C leader snapshot from authorized local JSON.

This tool never fetches source records or sends/publishes data. Keep real inputs
and generated outputs in an approved private location; public examples are fake.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit


KINDS = {"issue13", "work60", "kb_review_due", "orch", "patrol"}
ACHIEVEMENTS = ("checked", "repaired", "improved", "resolved", "recorded")

# In the source checkout this module sits beside the established renderer.
# The fallback path only supports running this scratch copy during development.
try:
    from render_report import render as render_base
except ModuleNotFoundError:
    sibling = Path(__file__).parent / "work" / "skills" / "html-report"
    if sibling.is_dir():
        sys.path.insert(0, str(sibling))
    from render_report import render as render_base


def safe_url(value):
    if not isinstance(value, str) or not value:
        return ""
    try:
        p = urlsplit(value)
        if p.scheme != "https" or not p.hostname or p.username or p.password:
            return ""
        if any(ord(c) < 32 or ord(c) == 127 for c in value):
            return ""
        return value
    except ValueError:
        return ""


def _count(value, name):
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer or null")
    return value


def _unique_ids(values, label):
    if not isinstance(values, list):
        raise ValueError(f"{label} must be an array")
    result = []
    seen = set()
    seen_status = {}
    for value in values:
        if not isinstance(value, dict):
            raise ValueError(f"{label} entries must be objects")
        key = str(value.get("id", "")).strip()
        if not key:
            raise ValueError(f"{label} entry id is required")
        identity = (str(value.get("parent_id", "")).strip() + "|" + key
                    if value.get("parent_id") else key)
        status = str(value.get("status", "未確認")).strip().upper()
        if identity in seen_status and seen_status[identity] != status:
            raise ValueError(f"{label} has conflicting duplicate state for {identity}")
        seen_status[identity] = status
        if identity not in seen:
            seen.add(identity)
            result.append(value)
    return result


def normalize(data):
    if not isinstance(data, dict) or data.get("schema") != "adnc-leader-dashboard/v1":
        raise ValueError("schema must be adnc-leader-dashboard/v1")
    meta = data.get("meta")
    if not isinstance(meta, dict):
        raise ValueError("meta object required")
    for key in ("organization", "project_or_work", "responsibility", "scope", "retrieved_at"):
        if not isinstance(meta.get(key), str) or not meta[key].strip():
            raise ValueError(f"meta.{key} must be non-empty; use '未確認' when absent")
    cats = data.get("categories")
    if not isinstance(cats, list):
        raise ValueError("categories array required")
    output = []
    seen_cat = set()
    for idx, raw in enumerate(cats):
        if not isinstance(raw, dict):
            raise ValueError(f"categories[{idx}] must be object")
        cid = raw.get("id")
        if cid not in KINDS or cid in seen_cat:
            raise ValueError(f"categories[{idx}].id must be a unique supported category")
        seen_cat.add(cid)
        rows = _unique_ids(raw.get("items", []), f"categories[{idx}].items")
        denominator = _count(raw.get("denominator"), f"{cid}.denominator")
        achievement = raw.get("achievement", {})
        if not isinstance(achievement, dict):
            raise ValueError(f"{cid}.achievement must be an object")
        counts = {k: _count(achievement.get(k), f"{cid}.{k}") for k in ACHIEVEMENTS}
        # Work60 uses independent mutually non-additive status views. Deduplicate
        # by parent/job identity, exclude historical UNKNOWN and never total columns.
        if cid == "work60":
            active = []
            for row in rows:
                status = str(row.get("status", "")).upper()
                if row.get("historical") or status in {"UNKNOWN", "UNKNOWN_NO_EVIDENCE", "HISTORY"}:
                    continue
                active.append(row)
            rows = active
            states = {}
            for state in ("READY", "SENT", "DONE"):
                states[state.lower()] = len({str(r.get("parent_id", "")) + "|" + str(r.get("id", ""))
                                             for r in rows if str(r.get("status", "")).upper() == state})
            if any(str(r.get("status", "")).upper() in {"READY", "SENT", "DONE"} for r in rows):
                denominator = states["ready"] + states["sent"]
        else:
            states = {}
        output.append({"id": cid, "label": str(raw.get("label") or cid),
                       "denominator": denominator, "achievement": counts,
                       "states": states, "items": rows})
    return {"schema": data["schema"], "meta": meta, "source": data.get("source", {}),
            "summary": str(data.get("summary") or ""), "next_action": str(data.get("next_action") or "未確認"),
            "categories": output}


def _e(value):
    return html.escape("" if value is None else str(value), quote=True)


def _denominator(value):
    return "未集計" if value is None else f"{value}件"


def render(data):
    d = normalize(data)
    m = d["meta"]
    cards = []
    summary_lines = [d["summary"], "カテゴリは独立分母です。縦合計・進捗率の推測はありません。"]
    for c in d["categories"]:
        ach = "　".join(f"{k}={_denominator(v)}" for k, v in c["achievement"].items())
        states = "　".join(f"{k.upper()}={v}件" for k, v in c["states"].items())
        summary_lines.append(f'{c["label"]}: 未解決分母={_denominator(c["denominator"])}; 実績={ach}' +
                             (f"; 状態内訳={states}" if states else ""))
        cards.append({"id": f'CATEGORY-{c["id"]}', "title": c["label"], "priority": "OTHER",
                      "status": "未集計" if c["denominator"] is None else f'分母 {c["denominator"]}件',
                      "owner": "未確認", "next_action": d["next_action"], "evidence": f'今回実績: {ach}' +
                      (f"; {states}" if states else "")})
        rows = []
        for r in c["items"]:
            href = safe_url(r.get("source_url"))
            priority = str(r.get("priority") or "OTHER").upper()
            cards.append({"id": r.get("id"), "title": r.get("title", "未確認"), "priority": priority,
                          "status": r.get("status", "未確認"), "owner": r.get("owner", "未確認"),
                          "next_action": r.get("next_action", "未確認"), "evidence": r.get("evidence", "未確認"),
                          "source_url": href})
    sources = d["source"] if isinstance(d["source"], dict) else {}
    source_label, source_url = next(iter(sources.items()), ("未確認", ""))
    html_out = render_base({"kind": "project", "title": f'{m["project_or_work"]}｜リーダーダッシュボード',
                            "snapshot_date": m["retrieved_at"][:10], "source_checked_at": m["retrieved_at"],
                            "source_label": source_label, "source_url": safe_url(source_url),
                            "summary": "\n".join(summary_lines),
                            "handoff": f'次の1操作: {d["next_action"]}', "items": cards})
    meta_html = (f'<section class="panel" aria-label="管理範囲"><b>組織:</b> {_e(m["organization"])}　'
                 f'<b>責任:</b> {_e(m["responsibility"])}　<b>管理範囲:</b> {_e(m["scope"])}　'
                 f'<b>取得時点:</b> {_e(m["retrieved_at"])}</section>')
    return html_out.replace("<main>", "<main>" + meta_html, 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_stem", type=Path, help="write .html, .json and .txt beside this path")
    parser.add_argument("--pdf", action="store_true", help="also use sibling html_to_pdf.py when available")
    args = parser.parse_args()
    data = normalize(json.loads(args.input_json.read_text(encoding="utf-8")))
    stem = args.output_stem
    stem.parent.mkdir(parents=True, exist_ok=True)
    out_html = stem.with_suffix(".html")
    out_json = stem.with_suffix(".json")
    out_txt = stem.with_suffix(".txt")
    out_html.write_text(render(data), encoding="utf-8")
    out_json.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    text_lines = [f'{data["meta"]["organization"]}｜{data["meta"]["project_or_work"]}',
                  f'責任: {data["meta"]["responsibility"]}', f'管理範囲: {data["meta"]["scope"]}',
                  f'取得時点: {data["meta"]["retrieved_at"]}', data["summary"],
                  f'次の1操作: {data["next_action"]}', "カテゴリ別の分母・実績"]
    for category in data["categories"]:
        achievement = ", ".join(f'{key}={_denominator(value)}' for key, value in category["achievement"].items())
        states = ", ".join(f'{key.upper()}={value}' for key, value in category["states"].items())
        text_lines.append(f'{category["label"]}: 分母={_denominator(category["denominator"])}; 実績={achievement}' +
                          (f'; 状態内訳={states}' if states else ""))
    out_txt.write_text("\n".join(text_lines) + "\n", encoding="utf-8")
    if args.pdf:
        converter = Path(__file__).with_name("html_to_pdf.py")
        if not converter.exists():
            raise SystemExit("PDF NOT_RUN: sibling html_to_pdf.py is absent")
        import subprocess
        try:
            result = subprocess.run(["python", str(converter), str(out_html), "--output", str(stem.with_suffix(".pdf")), "--no-web-logo"],
                                    check=False, capture_output=True, text=True)
            if result.returncode:
                detail = result.stdout.strip() or result.stderr.strip() or f"exit={result.returncode}"
                print(f"PDF=FAIL ({detail[:300]}); HTML/JSON/TXT remain available")
            else:
                print(f"PDF={stem.with_suffix('.pdf')}")
        except OSError as exc:
            print(f"PDF=NOT_RUN ({exc}); HTML/JSON/TXT remain available")
    print(f"HTML={out_html} JSON={out_json} TXT={out_txt}")


if __name__ == "__main__":
    main()
