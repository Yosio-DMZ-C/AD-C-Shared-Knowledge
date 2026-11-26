#!/usr/bin/env python3
"""Evidence-first relation/event review for small AD&C work snapshots.

This helper raises review candidates only; it never decides semantic correctness.
Input is an explicitly collected JSON file and all output stays local.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

SCHEMA = "adnc-rdra-observe/v1"

def analyze(data):
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")
    findings = []
    for rel in data.get("relations", []):
        rid = str(rel.get("id", "relation"))
        expected, observed = rel.get("expected"), rel.get("observed")
        if expected is not None and observed is not None and expected != observed:
            findings.append({"id": rid, "kind": "relation_mismatch", "certainty": "candidate",
                "detail": "observed value differs from stated contract", "expected": expected,
                "observed": observed, "evidence": rel.get("evidence") or []})
        elif observed is None:
            findings.append({"id": rid, "kind": "unconfirmed", "certainty": "unconfirmed",
                "detail": "relation was not observed; absence is not treated as failure",
                "expected": expected, "observed": None, "evidence": rel.get("evidence") or []})
    for ev in data.get("events", []):
        eid = str(ev.get("id", "event")); state = str(ev.get("state", "unknown")).lower()
        evidence = ev.get("evidence") or []
        if ev.get("completed") is True and state not in {"success", "done", "resolved"}:
            findings.append({"id": eid, "kind": "completion_state_mismatch", "certainty": "candidate",
                "detail": "completion is claimed while outcome state is not successful", "evidence": evidence})
        if ev.get("completed") is True and not evidence:
            findings.append({"id": eid, "kind": "completion_without_evidence", "certainty": "candidate",
                "detail": "completion is claimed without an evidence reference", "evidence": []})
        if state in {"failed", "waiting", "hold", "unknown", "not_run"} and not ev.get("next_action"):
            findings.append({"id": eid, "kind": "recovery_path_missing", "certainty": "candidate",
                "detail": "nonterminal event has no recorded next action", "evidence": evidence})
        if ev.get("purpose_contribution") is False and ev.get("work_type") == "management":
            findings.append({"id": eid, "kind": "management_value_unclear", "certainty": "candidate",
                "detail": "management step is explicitly marked as not contributing to purpose", "evidence": evidence})
    return {"schema": SCHEMA, "source_as_of": data.get("source_as_of", "未確認"),
            "findings": findings, "finding_count": len(findings),
            "interpretation": "候補抽出のみ。意味判断・原因確定・修正判断は人が行う。未観測は未確認。"}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path); ap.add_argument("-o", "--output", type=Path)
    ns=ap.parse_args(); data=json.loads(ns.input.read_text(encoding="utf-8")); out=analyze(data)
    text=json.dumps(out, ensure_ascii=False, indent=2)+"\n"
    if ns.output: ns.output.write_text(text, encoding="utf-8")
    else: print(text, end="")
if __name__ == "__main__": main()
