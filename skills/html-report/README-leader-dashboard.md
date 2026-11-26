# AD&C Leader Dashboard (reversible experiment)

This CLI converts an authorized local JSON extract into an offline HTML snapshot, a normalized JSON file, and a short TXT summary. It never fetches sources, publishes, sends, or updates a service. Keep real inputs and outputs in a private approved folder; only synthetic fixtures belong in public source control.

## Run

```sh
python leader_dashboard.py example_leader_dashboard.synthetic.json /tmp/leader-view
```

Outputs: `/tmp/leader-view.html`, `.json`, and `.txt`. Add `--pdf` to create a Japanese PDF using ReportLab's built-in CID font. This avoids a local Chromium dependency. The PDF contains the summary, category totals, items, and source links; interactive HTML filters and copy buttons are HTML-only. The HTML is a snapshot: source acquisition, freshness, and correctness remain the caller's responsibility.

## Input contract

See `example_leader_dashboard.synthetic.json`. Required metadata are organization, project/work, responsibility, scope, and retrieval time; use `未確認` instead of guessing. Categories keep independent denominators for Issue #13 parents, Work60, KB review_due, ORCH children, and patrol outcomes. A null denominator renders as `未集計`; categories are never added together. Work60 item IDs are deduplicated; historical UNKNOWN records are excluded from current counts; SENT is distinct from DONE. Achievement keys (`checked`, `repaired`, `improved`, `resolved`, `recorded`) are separate.

## Checks

```sh
python -m unittest -v test_leader_dashboard.py
```

The synthetic boundary checks cover duplicates, missing counts, historical UNKNOWN, SENT-only, unknown/missing detail, and escaping/HTTPS link handling. They do not prove real-source acquisition, PDF rendering, phone display, or live organizational counts.
