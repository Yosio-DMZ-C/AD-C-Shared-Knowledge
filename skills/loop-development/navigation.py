#!/usr/bin/env python3
"""One-layer loop-mode decision aid. Does not schedule jobs or create UI buttons."""
import argparse
import json


def decide(layer, feedback, metric="", revision="", limit=0,
           trigger="", authorized=False):
    if layer not in ("internal", "external"):
        raise ValueError("layer must be internal or external")
    if feedback not in ("record_only", "adapt"):
        raise ValueError("feedback must be record_only or adapt")
    if limit < 0:
        raise ValueError("limit must not be negative")

    missing = []
    if feedback == "adapt":
        if not metric.strip():
            missing.append("evaluation_metric")
        if not revision.strip():
            missing.append("revision_path")
        if limit < 1:
            missing.append("positive_iteration_limit")
    if layer == "external":
        if not trigger.strip():
            missing.append("confirmed_external_trigger")
        if not authorized:
            missing.append("execution_authorization")

    loop_type = "open" if feedback == "record_only" else (
        "closed" if not any(x in missing for x in
                          ("evaluation_metric", "revision_path",
                           "positive_iteration_limit")) else "closed_unverified"
    )
    ready = not missing
    return {
        "layer": layer, "feedback": loop_type,
        "mode": ("内" if layer == "internal" else "外") + "×" + (
            "開" if loop_type == "open" else
            "閉" if loop_type == "closed" else "閉（条件未確認）"),
        "status": "DESIGN_ONLY" if layer == "external" and not ready
                  else "LOGIC_READY" if ready else "NEEDS_EVIDENCE",
        "missing_conditions": missing,
        "next_action": "不足条件を案件正本で確認" if missing
                       else "既存専門Playbook・本人指定・実権限を照合",
        "actual_execution": "NOT_RUN",
        "ui_buttons": "NOT_GENERATED",
        "note": "Single-layer advisory only; never creates automations, sends messages, or judges creative quality.",
    }


def self_test():
    cases = [
        (dict(layer="internal", feedback="record_only"), "内×開", "LOGIC_READY"),
        (dict(layer="internal", feedback="adapt", metric="Pester",
              revision="code fix", limit=3), "内×閉", "LOGIC_READY"),
        (dict(layer="internal", feedback="adapt", limit=3),
         "内×閉（条件未確認）", "NEEDS_EVIDENCE"),
        (dict(layer="external", feedback="record_only", trigger="weekly"),
         "外×開", "DESIGN_ONLY"),
        (dict(layer="external", feedback="adapt", metric="quality",
              revision="revise plan", limit=2, trigger="weekly",
              authorized=True), "外×閉", "LOGIC_READY"),
    ]
    for inputs, mode, status in cases:
        result = decide(**inputs)
        assert result["mode"] == mode and result["status"] == status, result
        assert result["actual_execution"] == "NOT_RUN"
    return len(cases)


def main():
    parser = argparse.ArgumentParser(description="AD&C loop mode single-layer advisory")
    parser.add_argument("--layer", choices=["internal", "external"])
    parser.add_argument("--feedback", choices=["record_only", "adapt"])
    parser.add_argument("--metric", default="")
    parser.add_argument("--revision-path", default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--trigger", default="")
    parser.add_argument("--external-authorized", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps({"self_test": "PASS", "cases": self_test()}))
        return
    if args.layer is None or args.feedback is None:
        parser.error("--layer and --feedback are required except with --self-test")
    try:
        result = decide(args.layer, args.feedback, args.metric, args.revision_path,
                        args.limit, args.trigger, args.external_authorized)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

# ADNC:DESIGNER_NOTE:PYTHON:BEGIN
# 通常利用時には読込不要。内/外と開/閉の単層の定義を、明示入力からのみ判定する。
# 自然文解釈・入れ子・外部実行許可・実送信を自動推定しない。実行時の権限は別。
# JSONのmodeは相談用の機械結果。日本語SKILL.mdと専門の採用仕様が正本。
# ADNC:DESIGNER_NOTE:PYTHON:END
