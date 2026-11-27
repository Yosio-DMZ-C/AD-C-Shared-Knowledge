#!/usr/bin/env python3
"""AD&C Playbook creation/update worksheet helper (experimental, read-only).

Usage: python3 templates/playbook_workshop.py {design|decompose|retro} input.json
       python3 templates/playbook_workshop.py --self-test

AI/human supplies actual facts. This tool checks structure and preserves claims;
it never decides adoption, changes any original, or contacts a service.
"""
import argparse
import json
import sys
from pathlib import Path

MODES = ("design", "decompose", "retro")


def text_value(value):
    return value.strip() if isinstance(value, str) else ""


def seq(value, field):
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError(f"{field} must be a list")
    return value


def design(data):
    goal = text_value(data.get("goal"))
    if not goal:
        raise ValueError("design requires goal")
    existing = data.get("existing")
    if not isinstance(existing, bool):
        raise ValueError("design requires boolean existing")
    preserve = seq(data.get("preserve"), "preserve")
    change = seq(data.get("change"), "change")
    questions = seq(data.get("questions"), "questions")
    if any(not text_value(v) for v in preserve + change + questions):
        raise ValueError("preserve, change and questions must contain text")
    satisfied = data.get("satisfied") is True
    needs_reuse = data.get("reuse_intent") is True
    route = ("revision_with_preservation" if existing else
             "initial_playbook_candidate" if satisfied and needs_reuse else "first_result_iteration")
    warnings = []
    if existing and not preserve:
        warnings.append("既存成果の保持条件が未記録。変更前の実動／原本を確認する")
    if existing and not text_value(data.get("source_ref")):
        warnings.append("既存正本の取得根拠が未指定。推測で削除・置換しない")
    if questions:
        warnings.append("未解決の疑問は削除・採用を決めず、対象部分を保持する")
    return {
        "mode": "design", "route": route, "goal": goal,
        "source_ref": text_value(data.get("source_ref")) or None,
        "keep_unchanged": preserve, "requested_changes": change,
        "unresolved_questions": questions, "warnings": warnings,
        "next": ("既存内容を保持した影響・依存の分解を行う" if existing else
                 "既存KBに再利用条件と満足した点を残し、新設時検収へ進む" if route == "initial_playbook_candidate" else
                 "最小の成果物を作り、本人の反応を得る"),
        "automatic_adoption": False,
    }


def decompose(data):
    goal = text_value(data.get("goal"))
    items = seq(data.get("items"), "items")
    if not goal or not items:
        raise ValueError("decompose requires goal and at least one item")
    by_id = {}
    for i in items:
        if not isinstance(i, dict):
            raise ValueError("each item must be an object")
        ident = text_value(i.get("id"))
        if not ident or ident in by_id:
            raise ValueError("item id must be nonempty and unique")
        if not text_value(i.get("deliverable")) or not text_value(i.get("acceptance")):
            raise ValueError(f"{ident} must have deliverable and acceptance")
        blockers = seq(i.get("blocked_by"), f"{ident}.blocked_by")
        if any(not text_value(b) for b in blockers):
            raise ValueError("blockers must be identifiers")
        by_id[ident] = i
    for ident, i in by_id.items():
        unknown = set(i.get("blocked_by") or []) - set(by_id)
        if unknown:
            raise ValueError(f"{ident} unknown blocker(s): {sorted(unknown)}")
    # Kahn's algorithm: detect cycles and return ready frontier without inventing tickets.
    pending = set(by_id)
    layers = []
    while pending:
        ready = [ident for ident in by_id if ident in pending and
                 not (set(by_id[ident].get("blocked_by") or []) & pending)]
        if not ready:
            raise ValueError("cyclic blocker graph: cannot execute")
        layers.append(ready)
        pending.difference_update(ready)
    budget = data.get("context_budget")
    if budget is not None and (isinstance(budget, bool) or not isinstance(budget, int) or budget <= 0):
        raise ValueError("context_budget must be a positive, case-specific integer")
    cautions = []
    for ident, i in by_id.items():
        estimate = i.get("estimated_tokens")
        branches = i.get("branches", 1)
        if isinstance(branches, bool) or not isinstance(branches, int) or branches < 1:
            raise ValueError(f"{ident}.branches must be a positive integer")
        if estimate is not None:
            if isinstance(estimate, bool) or not isinstance(estimate, int) or estimate < 0:
                raise ValueError(f"{ident}.estimated_tokens must be a nonnegative integer")
            if budget and estimate > budget:
                cautions.append({"id": ident, "reason": "文脈予算を超える仮置き。分割か引継ぎを検討"})
        if branches > 1:
            cautions.append({"id": ident, "reason": "複雑な条件分岐。分岐のみ別工程にできるか検討"})
    return {
        "mode": "decompose", "goal": goal,
        "units": [{"id": ident, "deliverable": i["deliverable"],
                   "acceptance": i["acceptance"],
                   "blocked_by": i.get("blocked_by") or []} for ident, i in by_id.items()],
        "ready_frontier": layers[0], "execution_layers": layers,
        "split_cautions": cautions,
        "one_worker_possible": len(items) == 1 and not cautions,
        "automatic_dispatch": False,
    }


def retro(data):
    stage = text_value(data.get("stage"))
    if stage not in ("first", "revision"):
        raise ValueError("retro stage must be first or revision")
    successes = seq(data.get("valued_results"), "valued_results")
    events = seq(data.get("failures"), "failures")
    if any(not text_value(v) for v in successes):
        raise ValueError("valued_results must contain text")
    recurrent = any(isinstance(e, dict) and isinstance(e.get("count"), int) and
                    not isinstance(e.get("count"), bool) and e["count"] >= 2 for e in events)
    satisfied = data.get("satisfied") is True
    triggered = satisfied or recurrent
    candidates = []
    if triggered:
        for e in events:
            if not isinstance(e, dict):
                raise ValueError("failures must contain objects")
            count = e.get("count", 1)
            if isinstance(count, bool) or not isinstance(count, int) or count < 1:
                raise ValueError("failure count must be a positive integer")
            if count >= 2 or satisfied:
                candidates.append({
                    "observed": text_value(e.get("observed")) or "未記録",
                    "evidence_ref": text_value(e.get("evidence_ref")) or None,
                    "suggestion": text_value(e.get("candidate")) or "原因確認が必要",
                    "evidence_status": "RECORDED" if text_value(e.get("evidence_ref")) else "NOT_VERIFIED",
                    "decision": "HUMAN_REVIEW_REQUIRED",
                })
    return {
        "mode": "retro", "triggered": triggered,
        "reason": "利用者が満足" if satisfied else "反復失敗" if recurrent else "未発火",
        "valued_results": successes,
        "improvement_candidates": candidates,
        "next": "改善候補を選別し、採用分だけ既存KBへ継承" if triggered else "まず成果物の完成または失敗の実測を続行",
        "automatic_changes": False,
    }


ROUTES = {"design": design, "decompose": decompose, "retro": retro}


def self_test():
    # Case 1: first artifact, positive response, candidate for initial Playbook.
    first = design({"goal": "ガイドを作る", "existing": False, "satisfied": True,
                    "reuse_intent": True, "preserve": ["利用者に好評だった短い手順"],
                    "change": [], "questions": []})
    assert first["route"] == "initial_playbook_candidate"
    assert first["keep_unchanged"] == ["利用者に好評だった短い手順"]
    first_retro = retro({"stage": "first", "satisfied": True,
                         "valued_results": ["利用者に好評だった短い手順"], "failures": []})
    assert first_retro["triggered"] and not first_retro["automatic_changes"]
    # Case 2: revise legacy Playbook and preserve an unclear but important rule.
    old = design({"goal": "既存配送手順を改善", "existing": True,
                  "source_ref": "case2/original", "preserve": ["UNKNOWNを消さない", "理由不明の例外を保持"],
                  "change": ["既知の誤記を直す"], "questions": ["例外は何のため？"]})
    parts = decompose({"goal": "変更を限定して検証", "context_budget": 2000,
                       "items": [
                           {"id": "A", "deliverable": "旧挙動記録", "acceptance": "現行実例と一致"},
                           {"id": "B", "deliverable": "局所修正", "acceptance": "旧規則維持・差分検収",
                            "blocked_by": ["A"], "estimated_tokens": 2800, "branches": 2},
                           {"id": "C", "deliverable": "結果読戻し", "acceptance": "元正本照合",
                            "blocked_by": ["B"]}]})
    assert old["keep_unchanged"] == ["UNKNOWNを消さない", "理由不明の例外を保持"]
    assert old["unresolved_questions"] == ["例外は何のため？"]
    assert parts["execution_layers"] == [["A"], ["B"], ["C"]]
    assert len(parts["split_cautions"]) == 2
    # Case 3: repeated failure triggers Retro; no autonomous fix or adoption.
    repeated = retro({"stage": "revision", "satisfied": False,
                      "valued_results": ["既存作業は完成"],
                      "failures": [{"observed": "同じ誤配送が2回", "count": 2,
                                    "evidence_ref": "case3/log", "candidate": "実際の起動器を独立検査"}]})
    assert repeated["triggered"] and not repeated["automatic_changes"]
    assert repeated["improvement_candidates"][0]["decision"] == "HUMAN_REVIEW_REQUIRED"
    assert not retro({"stage": "first", "satisfied": False, "failures": []})["triggered"]
    # Fail closed for bad dependency graph.
    try:
        decompose({"goal": "壊れた依存", "items": [{"id": "A", "deliverable": "A",
                    "acceptance": "A", "blocked_by": ["B"]},
                    {"id": "B", "deliverable": "B", "acceptance": "B", "blocked_by": ["A"]}]})
    except ValueError as exc:
        assert "cyclic" in str(exc)
    else:
        raise AssertionError("cycle not detected")
    return {"test": "PASS", "cases": [
        {"case": "initial_success", "route": first["route"], "retro_after_satisfaction": first_retro["triggered"]},
        {"case": "legacy_revision", "route": old["route"], "preserved": len(old["keep_unchanged"]),
         "questions": len(old["unresolved_questions"]), "layers": parts["execution_layers"],
         "split_cautions": len(parts["split_cautions"])},
        {"case": "repeated_failure", "triggered": repeated["triggered"],
         "candidate_count": len(repeated["improvement_candidates"]), "automatic_changes": False}],
        "negative_tests": ["nontrigger_first", "cyclic_dependency"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", choices=MODES)
    parser.add_argument("input", nargs="?", help="UTF-8 JSON file (read only)")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.self_test:
            result = self_test()
        elif args.mode and args.input:
            data = json.loads(Path(args.input).read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("input must be a JSON object")
            result = ROUTES[args.mode](data)
        else:
            parser.error("provide MODE input.json or --self-test")
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())