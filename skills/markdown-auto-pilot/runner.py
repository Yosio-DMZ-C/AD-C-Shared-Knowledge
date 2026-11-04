#!/usr/bin/env python3
"""Single-Playbook AUTO block updater; never executes embedded Python."""
import argparse
import ast
import hashlib
import os
from pathlib import Path
import tempfile
import json
import difflib

BEGIN = '<!-- ADNC:AUTO:BEGIN -->'
END = '<!-- ADNC:AUTO:END -->'
FENCE = '```python adnc-generated-steps'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def render(data):
    raw = data.decode('utf-8')
    if raw.count(BEGIN) != 1 or raw.count(END) != 1 or raw.index(BEGIN) >= raw.index(END):
        raise ValueError('AUTO markers missing, duplicated or reversed')
    if raw.count(FENCE) != 1:
        raise ValueError('Python block missing or duplicated')
    code = raw.split(FENCE, 1)[1].split('```', 1)[0]
    tree = ast.parse(code)
    assignments = [n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0], ast.Name) and n.targets[0].id=='STEPS']
    if len(assignments)!=1:
        raise ValueError('STEPS literal not found exactly once')
    steps = ast.literal_eval(assignments[0].value)
    if not isinstance(steps,list) or not steps or any(not isinstance(x,str) or not x.strip() or '\n' in x or '\r' in x for x in steps):
        raise ValueError('STEPS must be nonempty one-line strings')
    newline = '\r\n' if b'\r\n' in data else '\n'
    replacement = newline + newline.join(f'{i}. {step}' for i,step in enumerate(steps,1)) + newline
    start = raw.index(BEGIN)+len(BEGIN)
    finish = raw.index(END)
    return (raw[:start]+replacement+raw[finish:]).encode('utf-8')

def split_human_machine(data):
    """Return stable, separate hashes; appendix is machine-only."""
    raw = data.decode('utf-8')
    boundary = '## AI execution appendix'
    if raw.count(boundary) != 1:
        raise ValueError('AI appendix boundary missing or duplicated')
    human, machine = raw.split(boundary, 1)
    return human, boundary + machine


def human_digest(data):
    human, _ = split_human_machine(data)
    return sha(human.encode('utf-8'))


def inspect_human_change(current, baseline):
    old_human, _ = split_human_machine(baseline)
    new_human, _ = split_human_machine(current)
    changed = old_human != new_human
    diff = list(difflib.unified_diff(
        old_human.splitlines(), new_human.splitlines(),
        fromfile='baseline/human', tofile='current/human', lineterm=''
    ))
    return {
        'status': 'REVIEW_REQUIRED' if changed else 'UNCHANGED',
        'human_sha256_before': sha(old_human.encode('utf-8')),
        'human_sha256_after': sha(new_human.encode('utf-8')),
        'diff': diff,
        'machine_alignment': 'NOT_RUN' if changed else 'NOT_REQUIRED',
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('file',type=Path)
    p.add_argument('--expected-sha256',required=True)
    p.add_argument('--write',action='store_true')
    p.add_argument('--baseline',type=Path,help='Verified previous complete Playbook; detect human edits before any generation')
    a=p.parse_args()
    if a.file.is_symlink() or not a.file.is_file():
        raise ValueError('Refuse symlink or missing file')
    old=a.file.read_bytes()
    if sha(old)!=a.expected_sha256:
        raise ValueError('Stale input SHA; refusing update')
    if a.baseline is not None:
        if a.baseline.is_symlink() or not a.baseline.is_file():
            raise ValueError('Invalid baseline')
        report=inspect_human_change(old,a.baseline.read_bytes())
        print(json.dumps(report,ensure_ascii=False,indent=2))
        if report['status']=='REVIEW_REQUIRED':
            raise ValueError('Human edit detected: review intent and align STEPS before write')
    new=render(old)
    if render(new)!=new:
        raise ValueError('Idempotence failure')
    if not a.write:
        print('CHECK PASS',sha(old),'changed=',new!=old)
        return
    backup=a.file.with_name(a.file.name+'.adnc-backup')
    if backup.exists():
        raise ValueError('Backup already exists; refuse overwrite')
    backup.write_bytes(old)
    if backup.read_bytes()!=old:
        raise ValueError('Backup mismatch')
    fd,tmp=tempfile.mkstemp(dir=a.file.parent,prefix='.adnc-')
    try:
        with os.fdopen(fd,'wb') as f:
            f.write(new)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp,a.file)
        if a.file.read_bytes()!=new:
            raise ValueError('Post-write mismatch')
        print('WRITE PASS',sha(new),'backup=',backup)
    except Exception:
        if backup.read_bytes()==old:
            a.file.write_bytes(old)
        raise
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)

if __name__=='__main__':
    try:
        main()
    except ValueError as exc:
        raise SystemExit(f'ABORT: {exc}') from None
