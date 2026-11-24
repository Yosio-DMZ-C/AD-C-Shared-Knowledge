#!/usr/bin/env python3
"""Synchronize reviewed Japanese shared sections without replacing Playbook prose.

Run from a repository checkout:
  python scripts/sync_playbook_shared.py --check
  python scripts/sync_playbook_shared.py --apply
  python scripts/sync_playbook_shared.py --check --target skills/document-authoring/SKILL.md
  python scripts/sync_playbook_shared.py --apply --target skills/document-authoring/SKILL.md

Default mode covers existing registered targets. --target selects an existing file
by its ADNC:SHARED markers; empty marker pairs can be initialized explicitly.
No unmarked prose is changed. The script never commits or pushes. Review git diff.
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
    "COMMON_EXIT": (
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
    if body and not body.endswith("\n"):
        raise ValueError(f"{key}: block must end with newline")
    if match and hashlib.sha256(body.encode("utf-8")).hexdigest() != match.group(1):
        raise ValueError(f"{key}: common block changed manually; review before syncing")
    return left, right, body


MARKER_RE = re.compile(r"<!-- ADNC:SHARED:([A-Z][A-Z0-9_]*):(BEGIN|END) -->")


def selected_targets(root: Path, source: str, names: list[str]):
    """Use explicit paths and existing markers; never search/alter unmarked prose."""
    source_keys = {key for key, boundary in MARKER_RE.findall(source) if boundary == "BEGIN"}
    jobs = {}
    for name in names:
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or relative.suffix != ".md":
            raise ValueError(f"unsafe target path: {name}")
        path = root / relative
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
            raise ValueError(f"missing, symlinked or outside-root target: {name}")
        content = path.read_text(encoding="utf-8")
        markers = MARKER_RE.findall(content)
        target_keys = [key for key, boundary in markers if boundary == "BEGIN"]
        expected_markers = [(key, boundary) for key in target_keys for boundary in ("BEGIN", "END")]
        if not target_keys or len(target_keys) != len(set(target_keys)) or markers != expected_markers:
            raise ValueError(f"missing, duplicate or overlapping shared markers: {name}")
        unknown = set(target_keys) - source_keys
        if unknown:
            raise ValueError(f"no canonical source for {sorted(unknown)} in {name}")
        for key in target_keys:
            jobs.setdefault(key, []).append(relative.as_posix())
    return jobs


def sync(root: Path, apply: bool, targets: list[str] | None = None):
    src = (root / SOURCE).read_text(encoding="utf-8")
    jobs = selected_targets(root, src, targets) if targets else TARGETS
    plans = {}  # path -> (original bytes, accumulated edited text)
    for key, target_paths in jobs.items():
        _, _, canonical = section(src, key, require_hash=False)
        stamp = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        replacement = f"<!-- ADNC:SYNC_SHA256:{stamp} -->\n" + canonical
        for relative in target_paths:
            path = root / relative
            if path not in plans:
                before = path.read_bytes()
                plans[path] = (before, before.decode("utf-8"))
            before, text = plans[path]
            # Explicit targets may bootstrap an EMPTY marker pair. Existing
            # stamped blocks keep their tamper-detection contract.
            explicit = targets is not None
            left, right, current = section(text, key, require_hash=not explicit)
            stamped = HASH_RE.match(text[left:right]) is not None
            if explicit and not stamped and current.strip() and current != canonical:
                raise ValueError(f"{relative} [{key}]: unstamped content must be empty or match source")
            if current == canonical and stamped:
                print(f"OK      {relative} [{key}]")
                continue
            print(f"STALE   {relative} [{key}]")
            plans[path] = (before, text[:left] + replacement + text[right:])
    changes = [(path, before, after) for path, (before, after) in plans.items()
               if after.encode("utf-8") != before]
    if not apply:
        return 1 if changes else 0
    # Preflight all files before any write; never overwrite a different version.
    for path, before, _ in changes:
        if path.read_bytes() != before:
            raise RuntimeError(f"concurrent edit detected: {path}")
    for path, before, after in changes:
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
    parser.add_argument("--target", action="append", metavar="RELATIVE_MD",
                        help="sync only this marked Playbook (repeatable; no registry edit)")
    args = parser.parse_args()
    try:
        return sync(args.root.resolve(), args.apply, args.target)
    except (OSError, UnicodeError, ValueError, RuntimeError) as exc:
        print(f"CONFLICT: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
