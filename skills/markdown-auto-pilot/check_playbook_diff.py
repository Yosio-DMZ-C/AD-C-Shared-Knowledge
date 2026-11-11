#!/usr/bin/env python3
"""Read-only baseline comparison for Playbook editing; no semantic auto-sync."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path

APPENDIX_HEADER = '## AI execution appendix'


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def human_scope(content: str) -> tuple[str, bool]:
    """Exclude the known machine appendix, when exactly one boundary exists."""
    lines = content.splitlines(keepends=True)
    positions = [i for i, line in enumerate(lines) if line.rstrip('\r\n') == APPENDIX_HEADER]
    if len(positions) == 1:
        return ''.join(lines[:positions[0]]), True
    return content, False


def compare(baseline: bytes, current: bytes) -> dict:
    before = baseline.decode('utf-8')
    after = current.decode('utf-8')
    old_human, old_split = human_scope(before)
    new_human, new_split = human_scope(after)
    same_scope = old_split == new_split
    # If appendix boundaries were added/removed, compare the whole files.
    if not same_scope:
        old_human, new_human = before, after
    changed = old_human != new_human
    return {
        'status': 'CHANGE_DETECTED' if changed else 'UNCHANGED',
        'file_changed': baseline != current,
        'human_text_changed': changed,
        'human_scope': 'before_appendix' if old_split and new_split else 'whole_document',
        'baseline_sha256': sha256(baseline),
        'current_sha256': sha256(current),
        'human_sha256_before': sha256(old_human.encode('utf-8')),
        'human_sha256_after': sha256(new_human.encode('utf-8')),
        'diff': list(difflib.unified_diff(
            old_human.splitlines(), new_human.splitlines(),
            fromfile='baseline/human', tofile='current/human', lineterm='')),
        'nav_alignment': 'REVIEW_NEEDED' if changed else 'NOT_REQUIRED',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Read-only Playbook baseline diff')
    parser.add_argument('--baseline', required=True, type=Path,
                        help='The verified previous revision (e.g. git show)')
    parser.add_argument('current', type=Path, help='The current Playbook')
    args = parser.parse_args()
    for path in (args.baseline, args.current):
        if path.is_symlink() or not path.is_file():
            parser.error(f'Missing, invalid or symlink path: {path}')
    try:
        result = compare(args.baseline.read_bytes(), args.current.read_bytes())
    except UnicodeDecodeError:
        parser.error('Both Playbooks must be UTF-8 text')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
