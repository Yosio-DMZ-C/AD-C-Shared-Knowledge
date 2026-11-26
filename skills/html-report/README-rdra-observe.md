# Evidence-first relation/event review

Small, optional local helper for review candidates in an explicitly collected snapshot. It does not fetch records, edit source systems, or decide whether a finding is semantically true. Missing observations are labeled `unconfirmed`.

## Input and run

Use `adnc-rdra-observe/v1` JSON with optional `relations` (`id`, `expected`, `observed`, `evidence`) and `events` (`id`, `state`, `completed`, `evidence`, `next_action`, `work_type`, `purpose_contribution`).

```sh
python rdra_observe.py example_rdra_observe.synthetic.json -o /tmp/rdra-findings.json
```

The tool reports relation mismatches, unobserved relations, completion/state or evidence mismatches, missing recovery paths for nonterminal events, and management work explicitly marked as not contributing to purpose. Inspect every candidate against its evidence before taking action. Keep private source snapshots and outputs outside public Git.

## Check

```sh
python -m unittest -v test_rdra_observe.py
```

Synthetic boundary fixtures cover a normal match, a mismatch, missing observation, false completion, missing evidence, and a nonterminal event without a next action. This is a focused string/field check, not a semantic RDRA validator or independent-agent comparison.
