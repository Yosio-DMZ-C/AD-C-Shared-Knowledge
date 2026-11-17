#!/usr/bin/env python3
"""Synchronize reviewed Japanese shared sections without replacing Playbook prose.

Run from a repository checkout:
  python scripts/sync_playbook_shared.py --check
  python scripts/sync_playbook_shared.py --apply

The script never commits or pushes. Review git diff before committing.
"""
import argparse
import hashlib
import os
from pathlib import Path
import re
import sys
import tempfile

SOURCE = "docs/DEVELOPMENT_WORKFLOW_PRACTICES.md"
TARGETS = {
    "OUTPUT_5W2H": (
        "skills/document-authoring/SKILL.md",
        "skills/video-production-setup/SKILL.md",
        "skills/style-bootstrap/SKILL.md",
    ),
}
HASH_RE = re.compile(r"^<!-- ADNC:SYNC_SHA256:([0-9a-f]{64}) -->\n")


def section(content: str, key: str, require_hash: bool):
    start = f"<!-- ADNC:SHARED:{key}:BEGIN -->\n"
    end = f"<!-- ADNC:SHARED:{key}:END -->"
    if content.count(start) != 1 or content.count(end) != 1:
        raise ValueError(f"{key}: missing or duplicate section markers")
    left = content.index(start) + len(start)
    right = content.index(end, left)
    raw = content[left:right]
    match = HASH_RE.match(raw)
    if require_hash and not match:
        raise ValueError(f"{key}: missing integrity hash")
    body = raw[match.end():] if match else raw
    if not body.endswith("\n"):
        raise ValueError(f"{key}: block must end with newline")
    if match and hashlib.sha256(body.encode("utf-8")).hexdigest() != match.group(1):
        raise ValueError(f"{key}: common block changed manually; review before syncing")
    return left, right, body


def sync(root: Path, apply: bool):
    src = (root / SOURCE).read_text(encoding="utf-8")
    changes = []
    for key, target_paths in TARGETS.items():
        _, _, canonical = section(src, key, require_hash=False)
        stamp = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        replacement = f"<!-- ADNC:SYNC_SHA256:{stamp} -->\n" + canonical
        for relative in target_paths:
            path = root / relative
            before = path.read_bytes()
            text = before.decode("utf-8")
            left, right, current = section(text, key, require_hash=True)
            if current == canonical:
                print(f"OK      {relative} [{key}]")
                continue
            print(f"STALE   {relative} [{key}]")
            changes.append((path, before, text[:left] + replacement + text[right:]))
    if not apply:
        return 1 if changes else 0
    for path, before, after in changes:
        # Refuse replacement if another process edited the file since inspection.
        if path.read_bytes() != before:
            raise RuntimeError(f"concurrent edit detected: {path}")
        fd, temp = tempfile.mkstemp(prefix=".adnc-sync-", dir=str(path.parent))
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(after.encode("utf-8"))
            os.chmod(temp, path.stat().st_mode)
            if path.read_bytes() != before:
                raise RuntimeError(f"concurrent edit detected: {path}")
            os.replace(temp, path)
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
        print(f"UPDATED {path.relative_to(root)}")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="read-only drift check")
    group.add_argument("--apply", action="store_true", help="replace verified common blocks")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    try:
        return sync(args.root.resolve(), args.apply)
    except (OSError, UnicodeError, ValueError, RuntimeError) as exc:
        print(f"CONFLICT: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
