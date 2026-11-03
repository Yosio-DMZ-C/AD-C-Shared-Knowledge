#!/usr/bin/env python3
"""Read-only GitHub common-rule version gate. Python 3.9+, standard library only.

Usage:
  python check.py --state .adnc-common-rule-state.json
  python check.py --state .adnc-common-rule-state.json --acknowledge
  python check.py --self-test

Exit: 0 SAME; 10 CHANGED or FIRST_USE (fetch and read full rule before continuing);
      20 UNKNOWN (network/parse error, fail closed); 30 invalid local state.
--acknowledge is permitted ONLY AFTER the caller has fetched and reviewed the
full content at the returned blob SHA; it records the fetched SHA in local state.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import urllib.error
import urllib.request

SOURCES = {
    "shared": ("Yosio-DMZ-C", "AD-C-Shared-Knowledge", "README.md"),
    "execution": ("Yosio-DMZ-C", "AI-DODAI-Continuity", "docs/PROJECT_EXECUTION_STANDARD.md"),
}
STATE_VERSION = 1


def blob_sha(content):
    data = content.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\\0" + data).hexdigest()


def fetch(owner, repo, path, timeout=12):
    url = "https://api.github.com/repos/{}/{}/contents/{}?ref=main".format(owner, repo, path)
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.raw+json", "User-Agent": "ADNC-common-rule-gate/1"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        content = response.read().decode("utf-8")
    return {"url": url, "sha": blob_sha(content), "content": content}


def read_state(path):
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("version") != STATE_VERSION or not isinstance(data.get("reviewed"), dict):
        raise ValueError("invalid state schema")
    if any(k not in SOURCES or not isinstance(v, str) or len(v) != 40 for k, v in data["reviewed"].items()):
        raise ValueError("invalid reviewed SHA")
    return data["reviewed"]


def save_state(path, reviewed):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".adnc-rule-", dir=str(path.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump({"version": STATE_VERSION, "reviewed": reviewed}, f, ensure_ascii=False, indent=2)
            f.write("\\n")
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def self_test():
    assert blob_sha("test content\\n") == hashlib.sha1(b"blob 13\\0test content\\n").hexdigest()
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "state.json"
        assert read_state(path) == {}
        save_state(path, {"shared": "a" * 40})
        assert read_state(path) == {"shared": "a" * 40}
        path.write_text('{"version": 2, "reviewed": {}}', encoding="utf-8")
        try:
            read_state(path)
            raise AssertionError("invalid state accepted")
        except ValueError:
            pass
    print("SELF_TEST_PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=Path(".adnc-common-rule-state.json"))
    parser.add_argument("--acknowledge", action="store_true", help="ONLY after reviewing full content of all changed sources")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    try:
        reviewed = read_state(args.state)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "INVALID_STATE", "reason": str(exc)}, ensure_ascii=False))
        return 30
    fetched = {}
    try:
        for key, (owner, repo, path) in SOURCES.items():
            fetched[key] = fetch(owner, repo, path)
    except (urllib.error.URLError, OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"status": "UNKNOWN", "reason": str(exc)}, ensure_ascii=False))
        return 20
    changes = [key for key in SOURCES if reviewed.get(key) != fetched[key]["sha"]]
    result = {"status": "CHANGED" if changes else "SAME",
              "sources": {key: {"sha": value["sha"], "url": value["url"], "changed": key in changes}
                          for key, value in fetched.items()}}
    if args.acknowledge:
        if changes:
            print(json.dumps({"status": "REVIEW_REQUIRED", "reason": "Fetch and read complete changed source before acknowledgment; no automatic approval"}, ensure_ascii=False))
            return 10
        result["acknowledged"] = True
    print(json.dumps(result, ensure_ascii=False))
    return 10 if changes else 0


if __name__ == "__main__":
    sys.exit(main())
