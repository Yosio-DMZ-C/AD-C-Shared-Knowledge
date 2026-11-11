# AD&C｜単一Playbook Markdown AUTO生成・人間編集差分の局所説明

このファイルは[既存runner.py](runner.py)・[汎用読取専用差分検出](check_playbook_diff.py)の近くにある参照メモ。実行仕様・使用範囲は現在のコードと[開発プラクティス](../../docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)を優先する。リーダーワークシートに蓄積した以下の専門説明を**原文のまま移設・保全**したもの。通常業務の全件検査や自動Python実行を義務化せず、旧試験での合格判定を現在の全Playbook実証と読み替えない。

原文の出典：`docs/templates/LEADER_WORKSHEET.md`（2026-11-11 Q3移設前のGit履歴）。**既存runner.pyの実行コード・AUTO領域・保護境界・前版SHA検査は変更しない**。

## 移設原文（歴史的判断・検証条件）

## Markdown-embedded Python pilot (bounded single-Playbook use adopted; broader rollout not adopted)

Human-editable purpose, authorization, stop conditions, and recovery rules remain authoritative prose. A trusted runner MAY extract the fenced block labeled `python adnc-generated-steps`, execute it only in an isolated no-network test environment, and replace only text between the two AUTO markers. Never execute arbitrary downloaded Markdown code or silently overwrite human prose. For production use, require approved runtime, exact pre-write SHA, conflict check, backup and restore test, and readback. Thumbnail/image composition remains excluded pending separate specialist review.

The executable/checkable AUTO region and literal Python STEPS source are located together in the final AI appendix. Human instructions above remain authoritative.



Pilot acceptance: preserve all text outside AUTO markers byte-for-byte, compare expected SHA before write, verify idempotence, and restore from a verified backup. A successful isolated pilot does not prove a Drive write, an AI cold start, or production execution.



## Markdown-embedded Python: single-Playbook operational acceptance gate (2026-11-02)

**Decision ①: test only this leader Playbook first. Do not roll out to all Playbooks.**

**Historical pilot decision (already answered; do not re-ask):** The user selected single-Playbook testing. The earlier comparison was ① single pilot (selected), ② risky all-Playbook rollout (not authorized), ③ explain, ④ hold. This is a historical record, **not** an exception to the current general one-question option contract. Never present a past choice as pending or treat showing an option as approval. The human-readable instructions above remain authoritative. Python is limited to bounded, mechanical regeneration of an explicitly marked AUTO section, not policy decisions, external writes, status promotion, or silent repairs.

Acceptance procedure: (1) fetch the current main file and record Git blob SHA and original bytes; (2) create an isolated candidate, retaining all human-authored text and markers; (3) run the embedded or accompanying Python on that candidate twice and verify byte-for-byte idempotence; (4) verify unchanged human regions, correct AUTO boundaries, valid UTF-8, and no duplicated sections; (5) test malformed/missing markers, stale input SHA, and recovery from an immutable backup; (6) compare candidate to intended requirements and write only after all gates pass; (7) re-fetch the same canonical file and compare content, then verify any required registry/links. **A local pilot is not an operational PASS** until the actual current source, execution log, failures and post-write readback are recorded. Never invoke arbitrary Python from untrusted documents without inspection.

If a required runtime or safe write interface is unavailable, record the precise blocked step, evidence, attempted safe remedy and unblocking condition in the existing issue/review, mark operational test NOT_RUN, and continue with the next independent review item. Do not use the user's selection ① to authorize mass rollout.


### Human-edit detection: executable bounded gate (2026-11-03)

The [single-Playbook runner](../../skills/markdown-auto-pilot/runner.py) accepts `--baseline PATH` in addition to the required current `--expected-sha256`. The baseline must be the verified previous complete worksheet. It computes **separate human-section SHA-256** values using the unique `## AI execution appendix` boundary, emits a unified human diff, and blocks writes on any human change with `REVIEW_REQUIRED`. Never automatically regenerate over a changed human section; AI must infer the intent, clarify only material ambiguity, update the machine section accordingly, and then rerun tests against an explicitly reviewed baseline. This gate detects **text changes**, not semantic intent or authorization. It does not automatically read Git history or automatically invoke Python in chat.

**Acceptance:** current and baseline same → no human change; changed human wording → REVIEW_REQUIRED and no write; changed machine appendix only → human UNCHANGED; missing/duplicated appendix → error; stale full-file SHA → refuse. These behavior cases require execution evidence before marking operational PASS. The upstream opt-in rule above still applies; no automatic proposal or acceptance.

