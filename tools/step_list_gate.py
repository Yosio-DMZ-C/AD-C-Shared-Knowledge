#!/usr/bin/env python3
"""Read-only gate for the leader Playbook's generated list; never executes steps."""
import argparse
import ast
import hashlib
from pathlib import Path
import re
import sys

BEGIN = "<!-- ADNC:AUTO:BEGIN -->"
END = "<!-- ADNC:AUTO:END -->"
FENCE = re.compile(r"^```python adnc-generated-steps[ \t]*\r?\n(.*?)^```[ \t]*$", re.M | re.S)

def verify(raw: bytes, expected_sha256: str) -> int:
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError("stale input SHA")
    text = raw.decode("utf-8", errors="strict")
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError("AUTO marker count invalid")
    start = text.index(BEGIN) + len(BEGIN)
    end = text.index(END)
    if start >= end:
        raise ValueError("AUTO marker order invalid")
    matches = list(FENCE.finditer(text))
    if len(matches) != 1:
        raise ValueError("Python fence count invalid")
    tree = ast.parse(matches[0].group(1))
    assigns = [node for node in tree.body if isinstance(node, ast.Assign)
               and any(isinstance(t, ast.Name) and t.id == "STEPS" for t in node.targets)]
    if len(assigns) != 1:
        raise ValueError("STEPS assignment count invalid")
    steps = ast.literal_eval(assigns[0].value)
    if not isinstance(steps, list) or not steps or not all(isinstance(s, str) and s.strip() for s in steps):
        raise ValueError("STEPS invalid")
    newline = "\r\n" if b"\r\n" in raw else "\n"
    expected = newline + newline.join(f"{i}. {step}" for i, step in enumerate(steps, 1)) + newline
    if text[start:end] != expected:
        raise ValueError("AUTO list differs from STEPS")
    return len(steps)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("playbook")
    p.add_argument("--sha256", required=True, help="exact expected SHA256 of the raw input")
    args = p.parse_args()
    raw = Path(args.playbook).read_bytes()
    count = verify(raw, args.sha256)
    print(f"PASS: {count} generated steps match; no steps executed and no files written")

if __name__ == "__main__":
    try:
        main()
    except (ValueError, UnicodeError, SyntaxError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
