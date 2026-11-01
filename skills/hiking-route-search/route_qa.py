#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AD&C 山歩きワークシート検収（Python標準ライブラリのみ／β試用）

使い所：
  YAMAP等で実在ルートを1件採用した後、集めた事実をワークシートへ
  入れてから回答する。欠落・経由地点の逆転・標高計算・服装選択を照合する。
  AIはこの検査結果を読んで「不足ならその項目だけ調査 → 1回だけ再検査」する。
  このスクリプト自身はネット検索せず、出典の真偽・通行安全を保証しない。

使い方（SKILL.md と同じフォルダで実行）：
  python route_qa.py --template > route_input.json
  （AIが route_input.json の null 欄へ根拠付き情報を入力）
  python route_qa.py --check route_input.json
  python route_qa.py --self-test

JSONはYAML 1.2のサブセット。PlaybookのYAML結果欄をAIがJSONに書き出す。
PyYAML・APIキー・追加の依存ライブラリは不要。コード実行できないAIは
SKILL.mdの同じ検査を手動実施し、Python検査は NOT_RUN と記録する。

終了コード：0=検査PASS、2=不足・不整合・安全停止、3=入力/ツール異常。
検査不能はPASSにしない。個人名・非公開ID・秘密情報は入力しない。
"""
import argparse
import json
from pathlib import Path
import re
import sys


def template():
    return {
        "route": {
            "source_url": None,
            "route_name": None,
            "start": None,
            "end": None,
            "distance_km": None,
            "walk_minutes": None,
            "ascent_m": None,
            "max_elevation_m": None,
            "start_elevation_m": None,
            "checkpoints": [
                {"id": None, "name": None, "elapsed_min": None}
            ]
        },
        "plan": {
            "date": None,
            "shown_distance_km": None,
            "shown_walk_minutes": None,
            "checkpoints": [
                {"id": None, "elapsed_min": None}
            ]
        },
        "safety": {
            "status": "UNKNOWN",
            "evidence_url": None,
            "checked_at": None
        }
    }


def issue(issues, code, field, action, blocking=True):
    issues.append({
        "code": code, "field": field, "blocking": blocking,
        "next_action": action
    })


def is_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def minutes_for(month_range):
    match = re.fullmatch(r"(\d{1,2})〜(\d{1,2})月", month_range)
    if match:
        first, last = map(int, match.groups())
        return {n for n in range(1, 13) if
                (first <= n <= last if first <= last
                 else n >= first or n <= last)}
    match = re.fullmatch(r"(\d{1,2})月", month_range)
    return {int(match.group(1))} if match else set()


def clothes_from_playbook(text, month, altitude):
    """服装ルールはSKILL.md表だけが正本。Pythonへ同内容を二重登録しない。"""
    matched = []
    for raw in text.splitlines():
        if not re.match(r"^\|\s*[LMH]\d+\s*\|", raw):
            continue
        values = [v.strip().replace("**", "") for v in raw.strip("|").split("|")]
        if len(values) != 5:
            raise ValueError("SKILL.mdの服装表が5列ではありません")
        key, band, mo, label, phrase = values
        if band == "999m以下":
            lo, hi = 0, 999
        elif band == "1,000〜1,999m":
            lo, hi = 1000, 1999
        elif band == "2,000m以上":
            lo, hi = 2000, float("inf")
        else:
            raise ValueError("未対応の標高帯: " + band)
        if lo <= altitude <= hi and month in minutes_for(mo):
            matched.append({
                "row_id": key, "label": label, "clothing": phrase
            })
    if len(matched) != 1:
        raise ValueError("月×標高に該当する服装表の行数が" +
                         str(len(matched)) + "件です")
    return matched[0]


def verify_checkpoints(route_points, plan_points, issues):
    if not isinstance(route_points, list) or not route_points or any(
            not isinstance(p, dict) or not p.get("id")
            or not p.get("name") or not is_number(p.get("elapsed_min"))
            for p in route_points):
        issue(issues, "MISSING", "route.checkpoints",
              "採用ルート原典の経由地点ID・名前・経過分を順に取得する")
        return
    if not isinstance(plan_points, list) or not plan_points or any(
            not isinstance(p, dict) or not p.get("id")
            or not is_number(p.get("elapsed_min")) for p in plan_points):
        issue(issues, "MISSING", "plan.checkpoints",
              "作成する行程表の地点IDと経過分を転記する")
        return
    ids = [p["id"] for p in route_points]
    if len(ids) != len(set(ids)):
        issue(issues, "CONFLICT", "route.checkpoints",
              "起点と終点を含め、各通過地点に一意のIDを付ける")
        return
    original_elapsed = [p["elapsed_min"] for p in route_points]
    if original_elapsed != sorted(original_elapsed):
        issue(issues, "CONFLICT", "route.checkpoints",
              "原典の通過順序と累積経過分を再取得する")
    indexes = {p["id"]: i for i, p in enumerate(route_points)}
    seen = [p["id"] for p in plan_points]
    extras = [i for i in seen if i not in indexes]
    if extras:
        issue(issues, "UNVERIFIED", "plan.checkpoints",
              "原典にない地点の経路と所要時間を別途確認: " +
              " / ".join(extras))
    common = [p for p in plan_points if p["id"] in indexes]
    order = [indexes[p["id"]] for p in common]
    if order != sorted(order) or len(order) != len(set(order)):
        issue(issues, "CONFLICT", "plan.checkpoints",
              "採用ルート原典の地点順に並べ直し、時間を再計算する")
    planned_elapsed = [p["elapsed_min"] for p in plan_points]
    if planned_elapsed != sorted(planned_elapsed):
        issue(issues, "CONFLICT", "plan.checkpoints.elapsed_min",
              "行程表の経過時間が逆戻りしないか確認する")


def verify(data, skill_text):
    issues = []
    route = data.get("route") or {}
    plan = data.get("plan") or {}
    safety = data.get("safety") or {}
    if not all(isinstance(p, dict) for p in (route, plan, safety)):
        raise ValueError("route/plan/safety はオブジェクトにしてください")
    required = {
        "route.source_url": "採用した実在ルートの直接URLを確認",
        "route.route_name": "採用したルート名を原典から確認",
        "route.start": "採用経路の起点を原典で確認",
        "route.end": "採用経路の終点を原典で確認",
        "route.distance_km": "原典の同じ経路の距離を確認",
        "route.walk_minutes": "原典の歩行時間を分単位で確認",
        "route.ascent_m": "原典の累積上り標高を確認（最高点との差では代用しない）",
        "route.max_elevation_m": "コース通過最高標高を確認（山頂標高と混同しない）",
        "plan.date": "計画日を YYYY-MM-DD で決める",
        "plan.shown_distance_km": "回答に表示する歩行距離を入れる",
        "plan.shown_walk_minutes": "回答に表示する歩行時間を分単位で入れる"
    }
    for key, action in required.items():
        group, name = key.split(".")
        v = (route if group == "route" else plan).get(name)
        if v is None or v == "":
            issue(issues, "MISSING", key, action)
    if route.get("start_elevation_m") is None:
        issue(issues, "MISSING", "route.start_elevation_m",
              "起点標高を確認して最高点との標高差を照合。原典で得られない場合は未確認を明記",
              blocking=False)

    for field in ("distance_km", "walk_minutes", "ascent_m",
                  "max_elevation_m", "start_elevation_m"):
        value = route.get(field)
        if value is not None and (not is_number(value) or value < 0):
            issue(issues, "INVALID", "route." + field, "非負の数値で入力する")
    for field in ("shown_distance_km", "shown_walk_minutes"):
        value = plan.get(field)
        if value is not None and (not is_number(value) or value < 0):
            issue(issues, "INVALID", "plan." + field, "非負の数値で入力する")

    if is_number(route.get("distance_km")) and is_number(plan.get("shown_distance_km")):
        if abs(route["distance_km"] - plan["shown_distance_km"]) > 0.01:
            issue(issues, "CONFLICT", "plan.shown_distance_km",
                  "採用した経路から変更していないか確認。別経路なら原典数値を流用しない")
    if is_number(route.get("walk_minutes")) and is_number(plan.get("shown_walk_minutes")):
        if route["walk_minutes"] != plan["shown_walk_minutes"]:
            issue(issues, "CONFLICT", "plan.shown_walk_minutes",
                  "原典の歩行時間と、見学・休憩・余裕の追加時間を分ける")
    if route.get("source_url") and not str(route["source_url"]).startswith(("https://", "http://")):
        issue(issues, "INVALID", "route.source_url", "URLを根拠のある直接リンクにする")
    gap = None
    max_m, start_m, ascent = (
        route.get("max_elevation_m"), route.get("start_elevation_m"),
        route.get("ascent_m"))
    if is_number(max_m) and is_number(start_m):
        gap = max_m - start_m
        if gap < 0:
            issue(issues, "CONFLICT", "route.max_elevation_m",
                  "最高標高が起点より低い。参照値や単位を確認する")
        if is_number(ascent) and ascent + 1 < gap:
            issue(issues, "CONFLICT", "route.ascent_m",
                  "累積上りが起点から最高点の標高差より小さい。経路・単位を再確認する")
    verify_checkpoints(route.get("checkpoints"), plan.get("checkpoints"), issues)

    clothing = None
    try:
        d = plan.get("date")
        if d:
            from datetime import date
            month = date.fromisoformat(str(d)).month
            if is_number(max_m) and max_m >= 0:
                clothing = clothes_from_playbook(skill_text, month, max_m)
    except (ValueError, TypeError) as exc:
        issue(issues, "INVALID", "plan.date / clothing_table",
              "日付またはSKILL.mdの服装表を確認: " + str(exc))

    status = safety.get("status")
    if status not in ("YES", "NO", "UNKNOWN"):
        issue(issues, "INVALID", "safety.status", "YES／NO／UNKNOWN のいずれかを入力する")
    if status == "NO":
        for field in ("evidence_url", "checked_at"):
            if not safety.get(field):
                issue(issues, "MISSING", "safety." + field,
                      "通常実施を勧める根拠と確認時点を調べる")
    if status in ("YES", "UNKNOWN"):
        issue(issues, "SAFETY_STOP", "safety.status",
              "通常の登山推奨は停止し、未確認事項・代替案と参考服装を伝える")

    blocking = [x for x in issues if x["blocking"]]
    if any(x["code"] == "SAFETY_STOP" for x in blocking):
        state = "SAFETY_STOP"
    elif blocking:
        state = "NEEDS_INFO"
    elif issues:
        state = "PASS_WITH_GAPS"
    else:
        state = "PASS"
    return {
        "status": state,
        "route_altitude_gap_m": gap,
        "clothing_from_skill_table": clothing,
        "issues": issues,
        "instruction": (
            "MISSING/UNVERIFIEDの関連事項だけ追加調査し、ワークシート更新後に1回再実行。"
            "CONFLICTは経路・順序を訂正。SAFETY_STOPなら実施可能と案内しない。"
            "Pythonは出典を取得・検証しないため、原典照合はAIの責任。"
        )
    }


def self_test(skill_text):
    base = template()
    base["route"].update({
        "source_url": "https://yamap.com/model-courses/example",
        "route_name": "検査専用の架空周回",
        "start": "起点", "end": "起点",
        "distance_km": 5.3, "walk_minutes": 169,
        "ascent_m": 477, "max_elevation_m": 517,
        "start_elevation_m": 150,
        "checkpoints": [
            {"id": "start", "name": "起点", "elapsed_min": 0},
            {"id": "peak", "name": "山頂", "elapsed_min": 90},
            {"id": "temple", "name": "寺院", "elapsed_min": 150},
            {"id": "end", "name": "帰着", "elapsed_min": 169}
        ]})
    base["plan"].update({
        "date": "2026-11-28",
        "shown_distance_km": 5.3, "shown_walk_minutes": 169,
        "checkpoints": [
            {"id": "start", "elapsed_min": 0},
            {"id": "peak", "elapsed_min": 90},
            {"id": "temple", "elapsed_min": 150},
            {"id": "end", "elapsed_min": 169}
        ]})
    base["safety"].update({
        "status": "NO", "evidence_url": "https://example.org/safety",
        "checked_at": "2026-11-01"
    })
    good = verify(base, skill_text)
    assert good["status"] == "PASS", good
    assert good["clothing_from_skill_table"]["row_id"] == "L4", good
    assert good["route_altitude_gap_m"] == 367, good
    base["route"]["max_elevation_m"] = None
    missing = verify(base, skill_text)
    assert any(i["field"] == "route.max_elevation_m" and i["code"] == "MISSING"
               for i in missing["issues"]), missing
    base["route"]["max_elevation_m"] = 517
    base["plan"]["checkpoints"][1], base["plan"]["checkpoints"][2] = (
        {"id": "temple", "elapsed_min": 40},
        {"id": "peak", "elapsed_min": 90})
    inverted = verify(base, skill_text)
    assert any(i["field"] == "plan.checkpoints" and i["code"] == "CONFLICT"
               for i in inverted["issues"]), inverted
    base["plan"]["checkpoints"] = [
        {"id": "start", "elapsed_min": 0},
        {"id": "peak", "elapsed_min": 90},
        {"id": "temple", "elapsed_min": 150},
        {"id": "end", "elapsed_min": 169}
    ]
    base["route"]["ascent_m"] = 100
    assert any(i["field"] == "route.ascent_m" and i["code"] == "CONFLICT"
               for i in verify(base, skill_text)["issues"])
    base["route"]["ascent_m"] = 477
    base["safety"]["status"] = "UNKNOWN"
    assert verify(base, skill_text)["status"] == "SAFETY_STOP"
    for altitude in (0, 517, 999, 1000, 1999, 2000, 3000):
        for month in range(1, 13):
            assert clothes_from_playbook(skill_text, month, altitude)["row_id"]
    return {"result": "PASS", "scenarios": 5, "clothing_conditions": 84}


def main():
    ap = argparse.ArgumentParser(description="AD&C hiking worksheet checker")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--template", action="store_true")
    mode.add_argument("--check", metavar="JSON")
    mode.add_argument("--self-test", action="store_true")
    ap.add_argument("--skill", default=str(Path(__file__).with_name("SKILL.md")))
    args = ap.parse_args()
    try:
        if args.template:
            print(json.dumps(template(), ensure_ascii=False, indent=2))
            return 0
        skill_text = Path(args.skill).read_text(encoding="utf-8")
        if args.self_test:
            print(json.dumps(self_test(skill_text), ensure_ascii=False, indent=2))
            return 0
        data = json.loads(Path(args.check).read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("JSONの最上位はオブジェクトにしてください")
        result = verify(data, skill_text)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["status"] in ("PASS", "PASS_WITH_GAPS") else 2
    except (OSError, ValueError, AssertionError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "TOOL_ERROR", "detail": str(exc)},
                         ensure_ascii=False), file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
