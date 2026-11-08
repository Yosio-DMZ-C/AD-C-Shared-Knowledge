# Leader worksheet v0.1

Use this worksheet during the work, then reuse it as the final report. This is a format, not a decision procedure. Refer to the existing registry and operating rules for authoritative facts and approvals.

**Execution model (2026-10-29 β):** Team members complete their authorized reversible changes through canonical writes, reference/Git integration and readback; the leader audits across changes and repairs scoped inconsistencies. Follow the actual enabled patrol schedule; this worksheet does not set its cadence or add preflight gates. Audit significant dependencies and actual restorability, not just reported completion. Avoid new trackers and duplicate approval prompts.

1. New changes: record only new facts, or 'no new changes'.
2. Reconciliation: note sources checked, discrepancies, and unverified claims.
3. Implementation: record actual writes, commits, readback, and PASS / FAIL / NOT_RUN.
4. Recovery: identify prior version and whether rollback was actually tested.
5. Next action: one priority and, if needed, one approval question.

Keep routine reports brief. Mark irrelevant checks N/A with a reason. Never report a draft or unverified change as DONE.

## 本人最終決定（2026-11-08）｜担当は実装、問題はリーダーが解消

**AD&C独自のSTOP・HOLD・全PASS・事前承認待ちは撤廃する。** このワークシートは停止審査票ではなく、実施した結果と問題を短く受け渡す道具とする。既存のGit・Drive版履歴を復旧に使い、旧判定や古いHOLDを現在の停止命令として再適用しない。

担当は既存正本に実装→可能なら実物を読戻し→「実施／現物リンク／問題と影響／次の一手」を既存案件に残す。問題があっても成功部分を保全する。`DONE`・`DONE_WITH_ISSUES`・`NOT_EXECUTED` を区別し、未検証をPASSと称さない。原因の解明・全件形式・SHA連鎖・第三者レビューは実装開始の前提としない。

**リーダー定時巡回**は新着の `DONE_WITH_ISSUES`・修復待ち・実環境制約を優先し、毎回可能な具体修正を1件以上実施して、同じ案件の実物へ保存・読戻しする。解決不能な問題のみ `本人判断事項＝何を判断してほしいか／選択肢・影響／推奨案` として本人に上げる。巡回のための新しいDB・管理Issue・承認ループは作らない。

`STOP` は外部の実制限・本人個別指示によって実行できなかったという事実表示のみ。`REQUIRED` は完成品の条件であって部分実装・試作の停止条件ではない。`OPTIONAL` は任意の品質・UX・監査補助。競合や欠落も問題を記録し、独立した作業は進める。AI／サービス規約・実権限・法令の条件は別途適用する。

**オンデマンドの実行補助**：DESIGNER'S NOTE／T007／専門Playbookは実際にボタン・GUI・制作物で必要な場合にだけ参照する。新しい形式審査を増やさず、採用済み部分は勝手に作り直さない。

## 定時巡回の報告ワークシート｜実績と記録を分けて見せる（2026-11-08）

**最初の問い：「あなたが今回解消した問題は？」** 既存案件ID・元の問題・実際に変更した原本または動く機能・確認結果を短く答える。解消がなければ「実績0件」と書いてよい。数を埋めるための新規タスク・過剰な再検査・未確認の成功宣言はしない。

| 報告区分 | 記載すること（簡潔に） |
| --- | --- |
| **実績（問題の解消・実務の前進）** | 元の不具合への修正、原本の実変更、必要な実行・読戻し。案件ID／現物リンク／何が改善したか。例：誤っているregistry原本の修正は実績。 |
| **報告・報告修正** | 調査、事実確認、証拠回収、状態訂正、既存レビューへの追記。例：既に終了した実行のrun_idを確認し、報告を訂正しただけならこちら。 |
| **未解決・次の一手** | 元の問題として残ったことと、次に可能な修復を一言。確認・記録をしただけで元の不具合をDONEにしない。 |

**集計は「実績 N 件／報告・報告修正 M 件」。** 同じ作業を両方に重複加算しない。対象そのものが誤った案内・記録であった場合、その**正本の修正**は実績だが、別文書での報告追記は報告。実績0件でも罰則・再承認・作業停止はない。調査・確認が実務の前提として必要な巡回なら、それも価値のある報告として残す。

仕事選びに迷ったら、**既に原因・対象が判明し、その場で安全に直せる未解決事項**を、同じ件の再調査や報告だけの更新より先に試す。直せない枝は理由を短く残し、可能な別の実務へ進む。新しい毎回必須のフォーム・ゲート・管理DBは作らない。

## Work60｜指示書ファイルの保存から1行配送まで（リーダー用）

**役割を分離する**：リーダー・定期巡回が案件を選び、担当A/B/C向けの**詳細指示書をストレージに保存**する。**Workに渡すのは各担当への1行配送文だけ**で、Work自身には案件の詳細を読ませず、判断・調査・制作・成果回収をさせない。詳しい判断・安全境界・完成条件は受け手の担当チャットが指示書を実取得して扱う。これは既存Work60の「配達係」という設計を具体化する道具で、新規承認ゲート・並列台帳・新しい定期タスクではない。

**生成側（リーダー／定期巡回）の手順：**

1. 現行Issue、既存Work60契約・運行票・最新成果から、**A戦略／B実務／Cブログ**をそれぞれ0〜1件選ぶ。Bの実務、Cの実例は既済・重複・配送UNKNOWNを避ける。Cを省略してもA/Bを止めない。旧JOBや既送信を再起動せず、既存親IDと今回の識別子を紐づける。
2. **Workとは別の実行環境**で、各担当向け指示書を既存の適切なDrive/KB格納先に作成・更新する。既存A/B/Cの指示書を利用できれば同一IDを優先し、必要時だけJOB固有のファイルを作る。指示書本文には「JOB_ID／親ID・担当ロール／目的／今回する実作業／既存正本・対象URL／既済除外／権限と禁止範囲／完成・読戻しの目安／既存報告先／残問題の扱い」を揃え、判断・実装・検収は担当AIに依頼する。非公開情報は適正な権限・共有範囲のまま保持する。
3. 保存できた各ファイルを**生成側自身が実取得**し、JOB_ID、対象、本文、直接URLが意図した新規・現行の内容かを対象限定で確かめる。未保存・URL未確認の文書について「保存済みの1行指示」と偽らない。全KBや全SHAの一律事前監査は行わない。
4. 保存済みの**各ファイルに対応する1行配送文を生成**する。例：`AD&C｜JOB_ID=<実ID>｜A戦略担当：<検証済み指示書URL> を実取得し、本文の指示だけを実行・検収し、本文指定の既存先へ報告してください。`（B実務・Cブログも同型）。**実URLは生成側で取得したものに限定**し、長い仕様・調査結果・成果条件・原文をこの1行へ展開しない。
5. Workを起動する人には**短い配送指示＋A/B/Cの1行配送文だけ**を渡す。**新規チャットへの配送を標準**とし、WorkはChatGPT画面でA/B/Cそれぞれ別の新規チャットを作成→対応する1行を1回送信→作成後の実チャットURL・送信成否だけ返して終了。**送信前に存在しない新規チャットURL、既存担当チャットの特定を要求しない。** 既存チャット送信を本人が明示指定した場合だけその実URLを先に確認する。Workは指示書URLを開かず、Drive/GitHubを開かず、説明文の内容を読まない。ブラウザ実送信不可の枝だけNOT_EXECUTEDとして他を続け、送信したふりをしない。
6. 担当チャットが自分の1行を受領した後、**担当が**ストレージの詳細指示書を取得し、実務・修復・読戻し・既存IDへの結果保存を行う。後続リーダー巡回は「保存／Work送信／担当受領／実行／検収」を別事実として扱い、実績と報告・報告修正を分ける。**Workの配送成功を担当の実務完了と数えない**。

**Workに見せるメッセージの最小形：** 「ChatGPTでA/B/Cそれぞれ新しいチャットを1件ずつ作成し、対応する各1行を原文どおり1回送信。作成後の実URLと送信可否だけ返して終了。既存担当チャットは探さず、作成前のURLは要求しない。リンクは開かず、案件の実行・調査・確認・保存は一切しない。」＋検証済みの各1行のみ。元ファイルの本文はWorkの起動メッセージに貼らない。

**注意：** URLの共有は閲覧権限の代替にならない。本人が許可していない相手・外部AIへ機密リンクを配送しない。実行前の形式不備だけでA/B/C全体を止めず、対象の修正・未実施を記録する。既存のWork60契約と本人の明示条件を優先し、新しい正本・タスク管理制度を増やさない。

## 半月次の運用ふり返り｜見える化は軽く、評価より人間の判断を助ける（2026-11-08）

既存の1日・15日の半月次レビューで、**既存の実行記録から短い表を作り、リーダーの所見を1〜2行添えるだけ**。全件採点、点数化、変化率の提出義務、新DB、新たな毎日点検は設けない。秘書の日次／半月次の一問一答や専用ボタンは変更しない。

| 見るもの | 現状（観測できたこと） | 前回からの変化・気になること |
|---|---|---|
| 依頼した仕事 | 完了／進行中／止まっている具体例 | 以前は実行されていた依頼が止まっていないか |
| 使える機能 | Workの配送、操作ボタン、コピー、次へ等の実動例 | 機能喪失・再依頼・訂正の増減など |
| 人間に求めること | 必要な最終承認や判断が残っているか | 不要な確認・再入力が増えていないか |

数値・前後の変化率は**同じ定義で比較できる実測が既にある時だけ任意に添える**。数字がなくても具体例と所見で十分。測るための作業・母数調整・余分な報告を担当に課さない。本人の明示保留や実サービスの実行不可は、AD&C内製の停止判定とは分けて事実記録する。

**原則は「問題があっても実施済み成果を保全して継続」**。観測範囲で特段の問題がなければ「現状継続を推奨」と短く伝え、原則ボタンや回答要求は不要。実行されなくなった依頼、失われた機能、本人に繰返し訂正させる問題など、**見直す価値がある論点だけ**を提示し、必要なら実動する **［見直す］［保留］** の2択を示す。

- **［見直す］**：その具体的な問題（案件ID・現象・最終ゴール）に限定して、既存リーダーが原因確認→許可済みの小修正→結果確認まで進める依頼を次ターンへ送る。公開・権限・費用・不可逆など新しい承認が必要なら、最終操作を明示して改めて承認を求める。「見直す」を危険な操作の一括承認にしない。
- **［保留］**：今回の**提案を採用しない／今はルールを変えない**。通常業務と既存の安全な復旧・定時巡回は継続。明示HOLDの解除、既存タスク停止、問題のDONE化を意味しない。同じ論点を毎回問い直さない。
- ボタンが機能しなければ、同じ2択を短い返信文で示す。最終操作の新承認を求める場合のコードブロック回避策は[標準コミュニケーションPlaybook](../../skills/communication-navigation/SKILL.md)に従う。

**発見した故障は半月次を待たず通常巡回で対処**する。半月次はその結果を人間が見えるようにする場であり、修復の先送り理由にはしない。所見と対象の既存記録だけを残し、今回のふり返りを新たな受入れゲートにしない。

## 人間に見える承認・最終ゴール到達（2026-11-08）

全業務は最終的に人間が何を利用できれば完了かから考える。承認済み・可逆な工程は途中で止めない。必要な新承認だけが残ったら、**「最終ゴール／ここまで実行済み／これを実行すれば何が完了するか／何を承認するか」**を一画面にまとめ、UI対応なら具体的な操作名を持つ**押せる承認ボタンを必ず提示**する。UI非対応なら「最終ゴールへの承認指示文」を`text`コードブロックで示し、「これをチャットに投入いただければ実施します。」と案内する。「止まっています」だけで報告を終えない。クリックしただけで実操作・他AI受領・Git main反映が完了したことにはしない。特にDraft PRをDONEと呼ばず、main統合が最終ゴールなら「READY_FOR_APPROVAL：あとmainマージ」と示す。通常の可逆作業への再承認ボタンは出さない。

テストは危険を増やさない限り最終形の一気通貫を先に1回試し、失敗時に原因に対応して安全に戻す。未承認の公開・本番不可逆操作は試験名目で行わない。詳しい共通定義は[標準コミュニケーション・ゴール到達ナビ Playbook](../../skills/communication-navigation/SKILL.md)。DESIGNER'S NOTE と T007 は具体的なボタン設計の道具であり、全件のUX審査義務にはしない。

## Work estimates and approvals: optional UI helper (2026-11-08)
Use this **only when the human requests stepwise progress, bulk execution choices, or explicit control over execution**. Do not require it in ordinary authorized work. A user's existing explicit request authorizes in-scope reversible implementation, without routine reapproval.

When needed, estimate total steps N (or a range), already completed, remaining, and real stopping conditions. Offer these established *working UI choices* with unchanged meaning:
1. **全てのステップを確認** — pause for the user's decision before each executable step.
2. **推奨5工程ずつ** — authorize up to five listed, reversible, non-decision steps, report actual results/readback, then request the next batch.
3. **全部一括承認** — authorize the currently displayed reversible, non-decision steps together; not a blanket authorization of new tasks.

Use actual interactive buttons when supported, passing the selected mode and known task scope into the next action. Otherwise show clearly numbered alternatives for a typed choice. Never render decorative inert controls. Public release, payment, deletion, permissions, merge and other separately gated actions are excluded. Do not repeat already completed steps to use a quota. Stop the affected high-risk or conflicted operation only, and continue independent safe work.

## KB write integration: issue-first and leader post-audit (2026-11-08)
Agents use the current canonical target and valid write permissions and avoid overwriting other people's changes. They should execute approved reversible updates, read back the changed target when feasible, and report any incomplete index/registry/hash propagation to the existing parent ID. A missing pre-write backup, full-source fetch, or complete SHA graph is an issue for the affected verification, not a reason for a new AD&C stop gate. Use existing history for recovery. The leader's existing scheduled review checks and repairs cross-reference, version, registry, and recovery issues afterwards. Never mark unverified propagation PASS. Never disclose private file IDs, registry data, or credentials in this public repository.

**On-demand technical repair recipe, not a mandatory preflight:** When a real KB discrepancy or corruption risk is discovered, use the existing canonical IDs and relevant private procedure to check *only the affected chain*: current target and SHA/modified version → competing changes and recoverable history → authorized same-ID patch → raw readback → compare registry, INDEX, Context/reverse links → repair mismatches locally → read back again. Record what passed and what remains unknown. This recipe is available to the leader and specialist, not forced on every chat before useful work begins. A linked file or successful upload alone does not establish propagation or another AI's receipt.

## AD&C grand-design engineering principle (approved 2026-11-04)
AD&C is a practical navigation system for imperfect humans and imperfect AI, not an attempt to attain 100% theoretical completeness. Select the context-appropriate scale of knowledge, show the next actionable turn, recalculate when reality changes, and preserve human control. Prefer small reversible implementations with measured user benefit over short-term logical elegance alone; use observed failures to revise hypotheses and procedures. Combine explicit rules with the empirically observed flexibility and behavior of each AI interface. Do not confuse an attractive theory with verified implementation, operation, effect, or independent test. Keep free/manual routes, bounded recovery, and evidence-based corrections. This principle guides design tradeoffs but never overrides existing permissions, private-KB write gates, or publication approvals.

**Project mission / public-facing charter (2026-11-04, editorial clarification):** 「完成形のない仕組みで、完成する仕事を増やす。」 AD&C has no final perfected architecture; each user-requested deliverable still has a concrete acceptance and readback gate. Balance the useful features and limitations of an imperfect AI with safety, human understanding, time and continued user control. Aim for social benefit through actual usable outcomes, not through an unsupported claim of guaranteed success or measured QOL gains. Do not treat permanent evolution as permission to leave requested work unfinished.

**Anti-local-optimization cue (use at the existing decision point; no new audit loop):** When you are about to add another abstract layer, reopen a settled decision, repeat a local check without progress, or delay an approved reversible implementation for theoretical elegance, ask: *“Which specific user outcome or required safety condition will this next step improve?”* If a concrete benefit is absent, stop optimizing that part and proceed with the smallest already-authorized, verifiable action through actual output and readback. If a safety, rights, accuracy, or approval constraint is real, meet it rather than bypassing it. Separate `implementation`, `operation`, and `effect` as PASS / FAIL / NOT_RUN; do not count a plausible theory or documentation alone as proof of user benefit. This is a **decision reminder**, not an additional checklist, process or deadline.


## Implementation-first policy (updated 2026-11-08)
Do the work first within the authorized, reversible scope. Report real changes and remaining work in existing records. Never stop at a proposal or a long procedural explanation when an executable safe action is available. If an isolated operation is blocked, perform another independent step instead.

## Exit gate: brief result check (2026-11-08)
Before reporting, identify the actual deliverable or change, the target readback when available, and any unresolved work. Do not demand all ancillary checks before producing partial but usable results. Distinguish a completed subtask from the entire project's verification.

## β is a release stage, not a completion status (2026-10-29)

At the exit gate, **never use “β”, “experimental”, “research”, “PR prepared”, or “next phase” to close or downgrade an originally requested implementation**. Check three independent facts only where they are part of the original acceptance criteria: **(1) implementation** = required canonical source, Git/main (if required), dependent references/settings, and readback actually match; **(2) operation** = requested working path or independent recipient actually ran; **(3) effect** = the requested outcome or comparative evidence was actually measured. Mark each `PASS / FAIL / NOT_RUN / N/A (reason)`, and keep the *original parent task OPEN* for missing required parts. A committed **instruction** is implementation PASS for that instruction, **not** proof that other AI agents obeyed it. If only the effect study remains, report “rule implemented; effect NOT_RUN” without relabeling the implementation as unfinished or inventing an open-ended new project. Fix an authorized safe missing step now; stop only at a real blocker. In routine no-change reviews, one concise status line suffices; do not create another ledger or audit pass.

## No 'separate process' escape
A requested outcome remains one tracked item across its substeps. Never close or defer an unfinished substep merely by labeling it 'separate process', 'next time', 'handoff', or 'PR prepared'. Before reporting, enumerate every remaining substep and attempt each authorized, safe action now. For each unexecuted substep, name the exact blocker (specific missing approval, permission, unavailable tool, conflict, or failed recovery check), evidence, and the single action that would unblock it. A different workflow or repository is not itself a blocker. Keep the parent item OPEN until the requested canonical end state and readback are verified. Do not treat a general implementation request as approval for public-main merges or other restricted actions.

## Human-time principle (experimental)

**Short rationale cue at a decision boundary (β, not evidence of effectiveness):** “Human time is limited; repeating approvals and deferring already authorized, reversible work create costs. After verifying actual authorization, pre-change state, conflicts and recovery path, finish safe steps through readback. Pause only for a new approval or unsafe/unrecoverable condition.” The cue never authorizes a write and never overrides a required approval or safety stop. Evaluate on existing T005 scenarios: A = safety baseline, B = exit check only, C = cue plus exit check; compare completion, extra questions, delays and safety violations. Do not add a third routine audit loop or a new checklist. Report all behavioral effects as NOT_RUN until observed.

Human time is finite and nonrenewable: five minutes now matter as much as five minutes near the end of life. Unnecessary repeated approval requests, forgotten unfinished work, and vague deferrals waste that time. AD&C already defines safeguards for backups, recovery, conflict checks, and authorization; verify those safeguards rather than assuming either safety or danger. Once they pass, complete authorized reversible work without asking again. Never use this principle to override an actual safety boundary. If several genuine decisions remain, present only the highest-priority actionable decision, then continue after it is resolved. Record the others in the existing tracker, not a new list. Treat this wording as an interface hypothesis, not a validated behavioral effect.

## Pending-item provenance
For every unfinished action, report: `NOT_RUN (origin: original parent request; action: exact remaining step; blocker: verified reason or unverified; unblock: next concrete action)`. Keep the parent OPEN until its intended end state is verified. A different workflow or repository is not a blocker. Distinguish not attempted from failed execution; never ask for blanket approval.

## Unfinished work and retry
Every action not performed must be labeled `未実施（元工程：...／理由：...）`. Keep its parent task OPEN. A different workflow is not a reason to omit this label. For a transient tool failure, retry once after checking whether the first attempt succeeded, to avoid duplicate writes. Do not retry authorization denials, irreversible actions, or safety blocks automatically. Record the outcome of both attempts.

## Entry-first creation and acceptance
Before creating or substantially revising a playbook or worksheet, check existing shared/personal KB procedures and Skills for equivalent purpose; distinguish Active, Draft, superseded, and withdrawn. Define a natural-language request that should lead to the procedure, its directly fetchable canonical source, version and applicability. Treat `request → discover → fetch → execute in specified order → inspect required output → present useful result` as one deliverable. A README link alone is not automatic discovery. When a task actually calls for independent discovery or behavior verification, reuse existing Q1 (entry and document), Q2 (independent cold-start interpretation), Q3 (actual sequence and relevant safety boundaries), and Q4 (user-facing result). Do not require all four as a routine preflight for every minor change; mark untested stages as untested rather than stopping unrelated safe work. **Design for easy execution first, not more compulsory verification.** Avoid creating another registry or gate. Preserve private identifiers outside public KB.

## Human-first Playbook customization and upstream proposal (2026-11-03; user-approved design, pilot only)

Keep **human-readable natural-language instructions first**, followed by an explicitly labeled **AI execution / Python reference part** within the same Markdown file when applying the single-Playbook structural pilot. The natural-language part is the local authority for purpose, steps, decisions and stop conditions. Do not silently replace a human edit with generated content.

When a human changes the natural-language part: (1) compare it against a verified previous revision and record the changed region/hash; (2) infer the intended behavioral change from the diff and surrounding context, and ask one focused question **only when the intent materially remains ambiguous**; (3) honor the local human edit within existing safety/authorization boundaries, update dependent Python/checks and local Playbook **as an authorized reversible customization**; (4) test consistency, idempotence, recovery and actual readback, marking blocked stages NOT_RUN; (5) distinguish local customization from a proposed general improvement. Do not presume a mere text diff proves the author's intent. If the edit conflicts with a mandatory security, legal, authorization or upstream contract, preserve the human edit and report the conflict instead of silently overriding either rule.

**Upstream opt-in:** After the local change is accepted, explain any reusable generalization briefly and ask whether to submit a proposal to the AD&C main repository. No upstream Issue/PR or publication without the user's explicit opt-in for that proposal; no automatic upstream merge. If clearly local-only, do not pester the user. Do not copy private IDs, data or environment-specific settings to a public proposal. Use the existing central Issue or standard contribution route; do not create duplicate tracking systems.

**Scope:** This is a **single-Playbook design/pilot**, not a mass rewrite of existing Playbooks. The separate runner and SHA gate remain bounded tools; a Python file's existence does not mean the Markdown executes it automatically. Structural migration, local human-edit detection, semantic alignment and independent cold-start behavior must each be separately tested before claiming production PASS.

## Markdown-embedded Python pilot (bounded single-Playbook use adopted; broader rollout not adopted)

Human-editable purpose, authorization, stop conditions, and recovery rules remain authoritative prose. A trusted runner MAY extract the fenced block labeled `python adnc-generated-steps`, execute it only in an isolated no-network test environment, and replace only text between the two AUTO markers. Never execute arbitrary downloaded Markdown code or silently overwrite human prose. For production use, require approved runtime, exact pre-write SHA, conflict check, backup and restore test, and readback. Thumbnail/image composition remains excluded pending separate specialist review.

The executable/checkable AUTO region and literal Python STEPS source are located together in the final AI appendix. Human instructions above remain authoritative.



Pilot acceptance: preserve all text outside AUTO markers byte-for-byte, compare expected SHA before write, verify idempotence, and restore from a verified backup. A successful isolated pilot does not prove a Drive write, an AI cold start, or production execution.


## Completion-through-repair rule (2026-11-02, user-approved)

When asked to **修正・検証する**, do not stop at inspecting, proposing, drafting, opening a PR, or recording NOT_RUN. Attempt every remaining in-scope, authorized, safe step **in this execution**: resolve the correct canonical document and registry entry, obtain pre-edit bytes/ID/version and recovery copy, diagnose write-interface and conflict failures, modify the original canonical file (same ID when required), update dependent links/indexes and required Git/main, then re-fetch each destination and compare intended content. A failed first attempt is a reason for targeted diagnosis and one safe retry after checking whether the first write took effect, not an automatic end of work. Seek an equivalent supported write mechanism when the initially selected connector cannot complete the operation; avoid duplicate or replacement files presented as original changes.

**Exit decision is based on the user's outcome, not on the amount of work performed.** Only report completed when every required canonical and downstream acceptance check is PASS. A file being fetched, a draft being made, or a blocker being described is not the requested completion. If—and only if—a concrete permission, safety, irreversibility, exhausted technical route, or verified external-dependency boundary actually prevents completion, record the exact parent/step, observed cause, attempted recovery, and specific unblock action in the existing tracker, plus FAIL/NOT_RUN; do not conceal, downgrade, or forget the unfinished parent. Routine Git changes/merge are within the user-approved scope when needed for the intended result, but this does not authorize leaking private KB into public GitHub, deletion, privilege changes or unreviewed production effects.

## One-question lead-in requirement (2026-11-05; minimal clarification)

After checking the current unresolved state and carrying out available safe work, ask only about an unresolved item requiring a real human decision. **Never display bare numbered options without a leading question.** Present, in this order: (1) the parent ID and latest verified unresolved fact, (2) why authorized automatic resolution cannot finish it, (3) a concise recommended route with its reason, and (4) an explicit natural-language question immediately before the selectable options, such as 「この未解決案件を、どの方法で進めますか？」. Make the question specific to the decision; do not imply that choosing an option itself completes implementation.

Use the latest user-corrected choice semantics: ① delegate to a verified active responsible leader **only if such a leader exists**, ② prepare a standalone new-chat delegation instruction, ③ explain in more detail, ④ hold. Automatic secretary/leader repairs belong **before** the question and are not an option. Show one question at a time, at most ten, and do not re-ask settled approvals. If no genuine human decision remains, report 「本人判断が必要な質問：0件」 and show no inert controls. Keep recipient acceptance, actual execution and readback as separate statuses. This is a presentation requirement, not authorization to alter private KB or bypass any existing gate.

## DESIGNER'S NOTE — 人間が迷わず選べる一問一答UI（2026-11-05、利用者の設計知見）

> 「ユーザーを事前にリードして、迷わせないためにボタンを表示するところの整理には特に時間をかけました」

これは装飾の話ではない。AIにとっては複数行の文字列・分岐条件・状態遷移として表現しやすいが、人間は画面を視覚的に走査し、位置・形・強調・色・アイコン・押せることを手掛かりに判断する。**文章として正しいだけでは、使いやすいUIとは限らない。** 一問一答では①最新の状況、②今なぜ本人判断が必要か、③推奨案と理由、④明示的な質問文、⑤実際に押せる選択肢を、この順に配置する。AIの説明量より、人間が迷わず次の操作を選べることを優先する。

### DESIGNER'S NOTE 追補｜「作り込みは濃く、運用は軽く」（2026-11-08）

> 「作りこみ重視、ワークシートなどのツールで品質を担保、過剰品質・検査は避ける」

**ワークシートはAIを規則で縛る審査票ではなく、必要なときに素早く正しい作業・画面・判断へ辿るための小型KB／実行ツール。** ボタンの意味、視覚的な見落とし防止、操作の流れ、分岐、機械化できる作業は、道具側に具体的に作り込む。使わない案件にその検査やフォームを課さない。作り込みの濃さと、利用者・担当AIの運用負担の軽さを**両立**させる。

新しい改善を採用するときの設計軸は、**「次のAIはこれで実務をやりやすくなるか、それとも全員の義務が増えるだけか」**。局所改善にはまず局所適用を選ぶ。本人が一案件について「はい」と答えても、全担当への汎用必須ルールの承認と見なさない。共通化するなら便利な機能・検索入口・失敗回避の知見を先に共有し、一律の事前チェック・重複承認・詳細報告は増やさない。必要な重大安全・機密・権限・不可逆操作と本人が特に指定した条件は守る。

この判断の**作成・更新側の正本**は[共有KB開発プラクティスのPlaybook・ワークシート作成更新節](../../docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)。本ノートはUIと道具の「なぜ」を残し、下記の具体的なボタン設計契約は維持する。別の審査Playbookや新しい管理表を作らない。

設計・検収観点：
- ボタンは文章中の番号の飾りではなく、対象親IDと選択意味を次のターンへ渡す**実際の動作**を持つ。操作できない環境では番号付きテキスト入力へ切替える。①稼働確認済み担当へ委任（いるときのみ）、②新チャット委任、③詳説、④保留の意味を保持し、選択だけで実行・受領・検収が済んだと誤表示しない。
- 赤字などの警告色は危険・未解決・失敗等の**意味がある場合だけ**に使う。色だけに依存せず文字ラベルやアイコンも併用する。アイコンは意味の一貫性を保ち、飾りを増やさない。通常の見出し・情報は落ち着いた階層で示す。
- 主操作の視認性、選択肢の間隔と押しやすさ、長文の折返し、画面サイズ、コントラスト、キーボード/読み上げ代替、誤操作の戻し方、操作後の状態表示を確認する。確定済みの選択を勝手に変更しない。
- 新チャット委任の詳細はKBへ保存・読戻しし、画面の最終まとめには短い1行だけを案件別に集約する。押す前に何が起きるかを明確にし、押した後の委任・受領・実行・検収を別状態で表示する。
- **研究メモ（未検証の仮説）**：文章だけの選択肢と、質問による事前誘導＋明確なラベルの操作ボタンを比較し、選択までの時間、誤選択、質問し直し、完了率、主観的な迷いを評価する。色・アイコン・位置・文面を一度に変えず、アクセシビリティ条件も含めて比較する。利用者の実体験を設計要件として記録するが、定量的な効果を実証済みとは扱わない。

このノートは定例の表示・UXに関する知見であり、Work60第0工程、固定枠、KB書込ゲート、既存の権限・承認を変更しない。

## T017 — three-character asset entry and independent Q2/Q3 acceptance (2026-11-05; approved local implementation)

**Scope:** existing approved characters 私／ワタシ／専門家, records `VID-CHAR-01/02/03`. The 2026-11-03 human approval remains PASS; this checklist never asks for approval again and does not modify image masters, Drive permissions or published materials.

1. **Q1 / inventory (leader):** for each of the three IDs, resolve the current canonical A-VIDEO record, the master asset file identity and revision, the index/manifest entry, the actual consumption URL or file path, and the Runbook instruction that points to it. Record source URLs privately when necessary; never invent a path or expose a private KB link in a public Issue. A missing source is `NOT_RUN`, not PASS.
2. **Q2 / readback (separate reader):** independently fetch each permitted master and index entry; compare exact ID, file identity, revision, bytes/SHA-256 where supplied, and the Runbook link target. Distinguish `PASS` (all resolved and matching), `FAIL` (demonstrable mismatch), `NOT_RUN` (access or evidence missing). Do not regenerate an approved character to make a mismatch disappear.
3. **Q3 / cold-start consumption (different chat/AI):** using only the published/authorized entry and Runbook, locate each of the three approved assets without a leader-supplied hidden path. Verify the target is retrievable and remains recognizable at intended thumbnail/video reduction. Log per-ID `PASS/FAIL/NOT_RUN`, consumer chat/AI and timestamp; mere acknowledgement is not a successful retrieval.
4. **Receipt gate:** independently record owner assignment, actual receipt, Q2 result, Q3 result, and remaining blocker. A sent instruction is not an accepted handoff. Do not mark T017 or T016 DONE on Q1 alone, and do not infer Q2/Q3 PASS from existing adoption status.
5. **Repair boundary:** if an index/Runbook pointer is stale, propose the smallest reversible pointer-only correction with before/after evidence and readback. Do not alter approved image masters, identifiers, wording or layout without an explicit change request. Preserve all previous approval and audit history.

**Minimal evidence row:** `asset_id | approved=PASS | canonical_source | master_identity/revision | index_entry | runbook_entry | Q2 + evidence | Q3 + evidence | receiver + receipt | next_blocker`. Complete three rows, one per ID. Until independent fetches are performed, record Q2/Q3 as `NOT_RUN`; this written contract itself is only a local implementation PASS.

## T007 — actionable one-question UI contract (2026-11-05; approved local implementation)

**Purpose:** convert the already-approved one-question decision semantics into a functional UI, not a decorative row of option labels. This section is a rendering and action contract; it does not approve new delegated work, change Work60, or override the private KB write gate.

- **Precondition:** check the latest unresolved state and carry out any immediately safe authorized work first (there is no mandatory three-pass research loop). Select exactly one genuinely unresolved parent requiring human judgment. Show its verified ID, present blocker, recommended route and reason, and an explicit question **before** any controls. If there is no such parent, state `本人判断が必要な質問：0件` and show no fictitious ①–④ choices.
- **① 担当リーダーへ委任:** render only after verifying a currently available recipient and a working delivery route. A click records `parent_id + choice=active_leader` and requests/initiates a verifiable delivery; do not mark recipient acceptance or execution PASS until separately evidenced.
- **② 新チャットへ委任:** click carries `parent_id + choice=new_chat` into the next turn. Queue only that selected parent, then prepare and validate its detailed KB handoff under the existing authorized record. Do **not** claim the new chat has been launched or received it. At the final summary, show a short one-line prompt only after the direct KB entry and readback are verified; otherwise show the blocker and NOT_RUN.
- **③ 詳しく説明:** click carries `parent_id + choice=explain`; explain the specific blocker, evidence, risks and recommendation, then return to the same unanswered decision without changing its state.
- **④ 保留:** click carries `parent_id + choice=hold`; record a deliberate hold, reason if given, and next review point. Hold is not DONE or DROPPED.
- **Buttons must be real controls:** bind each to a supported click/submit action with the parent ID, option meaning and required next turn. If functional controls are unavailable, fall back to the same numbered choices in plain text and accept a typed reply. Never present inert controls as though they work. Keep labels and ordering stable across sessions.
- **Visual and accessibility checks:** keep the question immediately above controls; use a clearly distinguishable primary action only when there is a justified recommendation. Warning colors indicate genuine warnings and are accompanied by words, not color alone. Icons have consistent meaning; provide readable labels, sufficient tap spacing, narrow-screen wrapping, contrast and text/keyboard alternatives. Display what happened after each click, including failures.
- **End-of-review controls:** `まとめて下さい` requests an actual consolidated decision/status view and deduplicated KB-backed one-line prompts for selected ② cases; `依頼が終わったら教えて下さい` requests a receipt/status check and must not itself assert that any external agent completed work. Do not show a redundant summary button after a summary is already complete.
- **Acceptance:** inspect a real parent question and click routing for each available option, confirm the parent ID is preserved, and verify summary and fallback behavior. Until interaction is actually tested in a client, classify the **written contract** as PASS and **end-to-end button behavior** as NOT_RUN.

## KB-backed short delegation and end-of-review summary (2026-11-05; user-approved)

Adopt the useful **display and handoff pattern** of the existing private secretary half-monthly review Playbook; do not modify that secretary document or supersede private KB write contracts. First carry out available authorized work; no mandatory three-loop pre-review. When the user actually selects new-chat delegation ②, save the **detailed, task-specific handoff inside the authorized private KB** under the original parent/review or its existing linked handoff location. Record the parent ID, latest verified facts and source links, decisions and approval limits, exact remaining work, blocker/cause status, acceptance/readback criteria and report destination. Preserve existing IDs and avoid parallel canonical Playbooks or duplicated trackers. Complete the full private KB gate (START_HERE → registry → SK-20261007-001 → backup/conflict → same-ID write → raw/SHA/INDEX/Context readback); if this cannot be completed, mark KB registration/entry as NOT_RUN with a specific unblock step. A newly stored file with no working entry is **not** a validated KB handoff.

For the user's screen, **do not paste the detailed procedure into the answer or each one-question exchange**. During questions record the selection and queue only the original parent ID. When all genuine questions are finished, display a concise decision/status table (decided / handed off / executed / verified / held / unconfirmed), then collect all deduplicated new-chat instructions **together at the end**, below 「以下の内容は新チャットに投げて下さい。」. Each item is **one short copyable line** like 「T014/T015：KB引継ぎ〔検証済みの直接URL〕を読んで実行・検収して。」, in its own plain text fenced code block. The KB, **not the one-liner**, holds the long evidence and test plan. For an existing active leader, consolidate separately under 「以下の担当（チャット）に伝えて下さい。」 and show only verified recipients; do not manufacture acceptance. If the private KB handoff or its direct link could not be saved and read back, do **not** issue a misleading short link; list the blocked handoff in the final NOT_RUN queue with its cause/unblock and provide an explicit fallback only if it is independently executable.

After the final question, allow feedback with 「なにかご指摘あればお願いします。」 and a working 「まとめて下さい」 action when controls are available; after summary, allow 「依頼が終わったら教えて下さい」 to check *requests sent* separately from recipients' execution and verification. Never claim that displaying a one-liner or the user's report proves another chat received it. Keep existing option meanings: ① active responsible leader only if verified; ② new chat; ③ detailed explanation; ④ hold. No human decision → no artificial question or delegation prompt. This refines UI and KB-backed handoff only; **scheduled Work-priority/Work60 step 0, its fixed frame, work-launch automations, task cadence and safety boundaries are out of scope**.

## Latest-result and delegation closure gate (2026-11-03)

Before a question or status report, resolve **the newest verified evidence for the same parent ID**. A historical report remains preserved but cannot override a later canonical readback. Distinguish reported / leader-received / independently reconciled; the mere existence of a report is not receipt. For each delegated item record responsible role and evidence of availability, accepted scope, receipt evidence, execution and readback as separate fields. When no active recipient can be confirmed, do not offer a fictitious leader; queue a standalone new-chat instruction for the final summary. Never mark the whole batch DONE from delegation or from a count match.

## Three-stage human approval protocol (2026-11-03; user-directed)

Only when the user specifically requests the **formal approval interaction** for an object ID, revision and approval scope, record the required affirmative evidence and offer a working final confirmation control labeled **正式承認にします**. Routine authorized reversible requests do not require two affirmations or this special UI. Ambiguous acknowledgements, AI replies and approval of another version do not count. The user's direct unambiguous **正式承認** instruction bypasses the two-utterance prerequisite; do not demand the same approval again. When a final control is required, merely rendering it is not approval: only an actual user action confirms. Record approval evidence and scope separately from recipient acceptance and technical verification. After approval, complete authorized canonical/reference/Git changes with pre-write preservation, conflict checks and post-write readback. A write failure leaves technical acceptance OPEN but **never revokes valid user approval**. Verify that a fresh AI can retrieve the approval state from the canonical entry; do not claim cross-AI behavior PASS from a documentation edit alone. Public release, permissions, deletion, payments and irreversible changes retain their own explicit approval gates.

## KB-persistent context dispatch for the recommended agent team (2026-11-04)

When assigning tasks to ChatGPT, Muse, Grok, research, implementer, librarian, creative specialists or a Work traffic coordinator, use the existing [chat-handoff Playbook](../../skills/chat-handoff/SKILL.md) **KB-continuity mode**. Each authorized role reads its own current Project/Area Context and the current parent issue, rather than regenerating and copying an ever-growing handoff transcript. Keep the *role's original mission, verified decisions and their reasons, user's explicitly expressed expectations, latest evidence and next one step*. At significant turning points (including a surprising or interesting discovery), swap lower-value middle detail for important material without monotonically expanding the summary (approximately 4,000 Japanese characters is a starting budget, not a reason to omit mandatory facts). Do not automatically update at every chat/run.

The **secretary** keeps role-specific context for daily and semi-monthly work and must validate real task scheduling, answered questions and unfinished requests in their own canonical sources. The **development leader** preserves vision and conversation continuity; scheduled patrols do not replace that ongoing relationship. **Specialized team members** preserve the task-specific test intent, boundaries, accepted/withdrawn conclusions, artifact versions, blockers and handoff conditions, not private secretary or user biography. **Work** only routes browser sessions, prompts and verbatim replies; it does not spend premium Work capacity repeatedly composing context. Permission barriers and private URL boundaries remain in force. A newly stored private role Context or a copied link is not proof of a registered KB entry, another AI's retrieval, or successful continuation. Report each gate separately, and never publish non-public KB links or personal context into this GitHub worksheet.

## Separate scheduled patrol and leader conversation (2026-11-04; user-approved)

Scheduled patrols are separate execution conversations, not replacements for the long-running development leader's conversational context. The leader retains grand design, synthesis and relationship/decision continuity; the patrol performs evidence retrieval, reconciliation, authorized reversible repairs and readback, then returns a concise handoff through existing records. A newly created task chat is expected and must not be treated as the user's pinned leader conversation. Distinguish the scheduled **task title** from the dynamically generated **run report heading**; naming a task alone cannot guarantee the application renames or pins an execution chat.

For UI clarity, name the active patrol task using the local MMDD prefix and `定期点検【最新】`, and mark redundant paused predecessors `【旧・停止】`. Begin *every* report with the actual JST run time: `MMDD定期点検【最新】｜HH:mm JST`. The static task title's date records its naming point, not the last run; freshness must be established from run timestamps and the latest canonical evidence. Before asking the user, reconcile older findings with newer completed/verified work; do not require the user to process an older chat first. Keep open parent IDs and unresolved work in the canonical record, rather than relying on the chat being read.

Do not auto-delete/archive a chat still associated with an active scheduled task: it may pause execution, and deleting a chat is not equivalent to closing or resolving its recorded issues. Do not create chat-cleanup schedules without verified capability and a separate retention/recovery check. Pinning is a user's UI affordance, not the task state or knowledge source of truth.

## Scheduled leader execution contract (2026-11-02)

This section is the external operational contract for the existing three-times-daily leader automation; the worksheet above remains its report template. Follow private START_HERE → registry → current leader Playbook → 80_reviews, Context, BUILD_PLAN and OPERATING_RULES before relying on this public summary. Never copy private KB content or identifiers into public GitHub. If a required source cannot be fetched, label that branch NOT_RUN rather than inventing its state.

1. **Two independent passes, difference-first.** Fetch recent team reports, canonical artifacts, registry, entry links, GitHub main/PR/Issue #13, and prior run. Pass one reconciles reports against actual files and acceptance evidence; pass two re-fetches changed or contested facts, checks reverse dependencies, parallel writes and overlooked items. Check one rotating older entry-to-Skill-to-Q1–Q4 path. Do not re-audit unchanged DONE or intentionally held Draft in full.
2. **Draft and hidden work.** Search new/changed records for Draft, OPEN, Blocked, NOT_RUN and contextually relevant TODO/FIXME/WIP/pending/暫定/保留/未接続/引継ぎ待ち. Distinguish historical citations and deliberately retained Draft. Group by existing OPEN parent ID, not by file or PR. For each Draft verify artifact, remaining substeps, approval, canonical/main gap, recovery source, next action; classify approved/implementable, approval-needed, technical Blocked, or intentional Draft. Do not promote unapproved proposals.
3. **Integration checks.** Trace natural request → entry/README → INDEX/registry → canonical Skill and dependencies → Q1–Q4 → real output/distribution/recipient readback, and reverse links. Distinguish CI file present vs wired/executed, PR vs main/release, commit vs push, save vs recipient receipt. An untested cold-start or external AI chat is NOT_RUN, not PASS. Preserve specialist gates (e.g. thumbnail).
4. **N-item implementation loop.** Deduplicate all OPEN parents, including Draft overlap, and inspect each once: verify current source and approval, pre-write file ID/version/hash/timestamp or Git base/head/blob, parallel-write conflicts, and a tested or verifiable rollback. Finish authorized low-risk reversible canonical and reference writes with actual readback; use safe Git branches when main merge is not authorized. A transient failure permits one retry only after checking first-write effects; never retry safety/permission denials. A blocked branch does not stop independent safe work. No unapproved publication, public main merge, deletion, permission change, billing, private-data export, or irreversible production operation. A separate workflow is not a reason to defer an authorized substep.
5. **Exit gate and record.** Start by answering the worksheet's 「あなたが今回解消した問題は？」 and separate substantive fixes from report/evidence edits. Compare requested outcome to canonical source, Git/main/release if required, references, operation and readback. Close only verified DONE. For every remainder record exactly: 未実施（元工程：親ID／対象工程：具体的操作／停止理由：確認済み障害または未検証／解除条件：次の1手）. Write status only to existing private KB parent rows or Issue #13, preserving confidentiality. Report new changes, pass-1/pass-2 findings, actual saves/commits/readback/recovery PASS/FAIL/NOT_RUN, OPEN parent N, Draft count and overlap, Draft promotions, integration/commit gaps, top blocker and at most one user decision. Do not alter other scheduled tasks.
6. **One-question review UI (2026-11-03 latest user decision).** The secretary/leader first performs the three-loop pre-processing below; automatic investigation, repair and readback are **not** a choice to ask the user. Only unresolved matters requiring a human decision become questions. Fixed choices: ① delegate to a **verified existing and active responsible leader** (omit ① when none exists); ② delegate to a new chat, saving evidence and acceptance criteria in the verified private KB handoff first, then accumulating only a short one-line KB-reference instruction for the final summary; ③ 詳しく説明する; ④ 保留. Do not renumber ②③④ when ① is omitted. Delegation offered, recipient receipt, actual execution and acceptance are distinct states; never invent a recipient, receipt or a user's selection. For a leader performing its own assigned work, finish authorized work rather than offering delegation as a substitute. At exit reconcile decision / executed-and-read-back / unexecuted-or-held / recipient receipt / next action. Do not present historical resolved findings as new questions.
**Scheduled leader review decision queue (2026-11-03):** After each scheduled leader review, complete authorized investigation, deduplication, repair and readback first. Group remaining unresolved items by common root cause, dependency and single human approval decision, retaining all original parent IDs and evidence. Rank grouped decisions by impact, urgency, dependency-unblocking value and whether a human decision is genuinely necessary. Prepare at most ten highest-priority questions for the human, not ten mandatory questions; zero is valid. Present one question at a time with a recommended actionable choice and 「なにかご指摘あればお願いします。」; preserve the existing secretary/leader fixed choices where that review contract applies. Keep lower-ranked items in existing tracking records with owner, priority and next review; never silently close or discard them. This queue is a navigation aid to bring beginners toward intermediate capability, not an autonomous expert decision-maker or an instruction to solicit approval for already authorized work. Do not change scheduled task timing or send unsolicited messages; use the existing review report and user interaction surface. A written rule is not evidence of a scheduled run or cross-AI behavior.
7. **Evidence and cause.** Separate observed failure, inferred cause and proven cause. A missing verified cause fails any cause-required gate. Run the three-loop pre-question review: (1) obtain original and newest evidence, deduplicate and clear superseded findings without deleting history; (2) repair all authorized safe items, write and read back; (3) for each remainder record observation, confirmed cause / hypothesis / unknown, why unknown, next diagnostic step, blocker, unblock, responsible party and acceptance criteria. A machine check must reject empty cause, paraphrases of the symptom as cause, or unknown cause without reason and next test. Stop after three loops without infinite retries, leaving FAIL/NOT_RUN. Human-authored decisions and stop rules stay in natural-language Markdown; trusted Python adapters may generate only marked sections and must pass idempotence, SHA, conflict, backup and restoration checks. Do not treat the embedded-Python pilot as proven production automation.

Historical anchors are not live facts: recheck merged PR #50/#38, installer v1.5.6, PR #32, KB version choices and Muse receipt before reporting current state. Keep the existing T005 safety-comparison experiment separate; its effectiveness remains unproven until measured.

## Copy-ready instruction formatting (2026-11-03; user-directed)

When presenting a prompt or instruction that the user should paste into another chat, AI, or tool, put the **complete copyable instruction inside a fenced Markdown code block** (triple backticks). **Exception:** for user-selected new-chat delegation with a verified KB-backed handoff, the complete *instruction to fetch and act on the KB handoff* is deliberately a short one-line KB reference; all task detail belongs in the private KB, not in the code block. Keep the explanation, evidence, caveats, and PASS/FAIL/NOT_RUN status **outside** that block. Preserve exact wording, URLs, parent IDs, test criteria, and report destination within the block; do not split one instruction across multiple fragments. Use a plain `text` fence or no language tag, not a programming-language fence that implies executable code. Apply to independent-test handoffs, new-chat delegation, leader/secretary handoff and other copy/paste instructions; this is presentation only, not approval or authorization. If the interface supplies a genuinely copyable writing artifact instead, that may be used, but never bury the actionable instruction in surrounding prose.

**Independent-test chat naming (2026-11-03; user-directed):** Never start a copy/paste independent-test instruction with the generic label `独立試験`. Start its first line with the specific subject, project, or Playbook being tested and put `独立試験` at the **end of that title**, e.g. `AD&C 開発リーダーPlaybook 独立試験`, `AD&C 山歩きPlaybook 独立試験`. This applies to the first line of the copyable prompt and any proposed chat title so distinct tests are distinguishable in conversation lists. Do not use a generic `独立試験｜...` prefix. Preserve existing test content and acceptance criteria.

## Development execution budget and approval cadence (2026-11-03; user-approved)

Before a multi-step development or repair task, estimate the **number of verification/repair loops remaining** and state the estimate, scope, acceptance criteria and uncertainty in plain language. For short-loop work, offer two interaction modes **only when no valid mode authorization already covers the work**: (A) step-by-step, pause for a user decision after each loop; (B) phase-completion batch, request **one explicit approval** for up to N loops and proceed autonomously through testing, diagnosis, safe repair, canonical integration and readback. The third mode, bounded end-to-end delegation, is offered only under the verified persistent-executor contract specified below. A user may choose a different cap. Default recommendation: batch for routine reversible work; step-by-step for exploratory or high-impact choices. Do not ask again when the user has already authorized the same scope and loop budget; the current instruction to perform approximately three loops is such authorization.

At each loop: (1) obtain newest canonical state and identify the smallest failure; (2) run the actual check and safe correction; (3) read back the changed state and log PASS/FAIL/NOT_RUN with the cause and next action. Count attempts explicitly (e.g. 1/3, 2/3, 3/3). A loop is not an unconditional retry of a failed write: inspect whether a previous attempt took effect first. If the estimate changes materially, report remaining loops and request additional authorization **only if the agreed budget or scope would be exceeded**. Do not silently expand from one Playbook to all Playbooks.

Batch permission never bypasses separate explicit gates for new scope, irreversible changes, external publication, access/permission changes, payments, disclosure of private data, or required release approval. At the budget limit, deliver observed results and unresolved causes; never invent completion. A user selecting step-by-step must receive a real pause between loops. Keep this decision in natural-language Markdown; do not generate policy or approval decisions through Python.

**Pilot promotion gate:** isolated test PASS may authorize a *single-Playbook trial*, but production adoption requires a trusted installed runner, real-current-source write/readback, recovery proof, and independent operation evidence. Creative video/thumbnail Playbooks remain outside mechanical batch modification.

### Development conversation modes and bounded autonomy (2026-11-03)

**Entry forecast:** For every development request, infer an end-to-end plan: outcome and Definition of Done → canonical discovery → design → implementation → test/diagnose/repair → Git/reference integration and readback → independent operational verification when needed. Show current phase, remaining estimated loops (a range), evidence needed, dependencies, and recommended next action. Skip irrelevant phases, preserve the original parent ID, and update forecasts when evidence changes.

**Three interaction modes:** **逐次確認** executes one meaningful step, reports evidence, and waits for user input. **フェイズ完走** (default for reversible ordinary development) iterates diagnosis, safe correction and readback until the current phase exit criteria are satisfied or an enforceable cap/stop is reached, without repeated approvals. **完成まで委任** continues across phases only under a preauthorized, enforceable execution contract, with checkpoint and recovery records. Never imply that a normal chat runs unattended for 24 hours.

**Execution contract:** record parent ID, exact scope and allowed write targets, acceptance criteria, mode, estimated loop count, hard limit on attempts/time and optionally measurable cost, checkpoint cadence, recovery path, reporting destination, and hard stops. 'Unlimited loops' requires an independent finite time or cost cap that the runtime can actually enforce. If a requested cap is not measurable, disclose that limitation and use an enforceable alternative or ask once. Stop at expiration; never auto-renew.

**Recommended action controls:** When only one next meaningful action exists, show **one** action, such as 「独立検証を実行」. For a genuine iterative phase, offer **two primary choices**: 「このフェイズをクリアするまで進める」 (recommended for safe reversible work) and 「各ステップを確認しながら進める」. Add 「完成まで任せる（上限付き）」 only when relevant and a real persistent executor and enforceable limits are available. Use clickable controls only when supported; otherwise show concise numbered choices. A control must trigger its described action. Do not ask again after valid same-scope approval. After presenting an actionable recommendation, add 「なにかご指摘あればお願いします。」 so the user may either select the control or type a correction or alternative. Never show an inert button or require a button when valid authorization already permits execution. This is a shared display principle, not a replacement for the secretary's one-question review choices or the development phase's two modes.

**Safety and quality:** Mode selection never overrides existing approval gates, including the three-stage human approval protocol. Stop for new scope, unapproved public/production release, irreversible effects, deletion, permission changes, payments, disclosure of private data, missing rollback, conflict, or exceeded limits. Report observed facts, cause (proven/hypothesized/unknown), smallest safe fix and readback on each loop; no fabricated PASS or recipient behavior. At a limit, checkpoint and report remaining work. A phase completes only when its exit tests PASS.

**Creative exception:** creative video, thumbnails, image generation, subjective design decisions and exact approved assets are excluded from bulk mechanical modification and autonomous approval. Specialist Playbooks govern those decisions; only separately scoped mechanical support work may be automated.

**Independent acceptance cases:** one-action path, two-choice loop, bounded persistent delegation, no duplicate approvals, safety stops, creative exclusion, cause/readback reporting. Cross-AI behavior remains NOT_RUN until a separate recipient executes and reports evidence.

### Development ambition interview, tripwires and external test handoff (2026-11-03)

**Independent-test handoff at the start:** If the executing assistant cannot create a genuinely independent fresh conversation or another AI recipient, immediately provide a complete copy/paste test instruction with canonical URL, scope, test cases, expected evidence, PASS/FAIL/NOT_RUN rules and report destination. Label recipient execution NOT_RUN until actual recipient evidence returns. Never defer this handoff until after claiming independent verification. Do not claim the user's plan permits tools or runtime features without checking.

**Capability interview tripwires:** At development kickoff and every half-month review, ask *only when not already answered or when conditions materially changed*: (1) desired autonomy: stepwise / phase completion / bounded end-to-end; (2) available execution environment and verified plan/runtime limits, not guessed from subscription tier; (3) enforceable time, usage or monetary budget; (4) permission for reversible code changes and separate release gates; (5) whether a fresh independent recipient is available; (6) the ambitious outcome the creator would like even if it currently seems impractical. The last question should be conversational: 「実現できたらうれしい、今は無理そうだと思う開発目標を一つ教えてください」. If user has already given an objective, do not interrupt progress with another interview. Log answers as user preferences, not global policy.

**Three-hour proof-of-progress offer:** For suitable uncertain development, recommend a bounded *up to three-hour* experiment: choose the smallest demonstrable vertical slice, run safe test/repair loops, then report (a) actual working artifact or measured result, (b) objective PASS/FAIL/NOT_RUN evidence, (c) elapsed execution time, (d) **measured** usage/cost or clearly marked unavailable/not measurable, (e) remaining blockers and next decision. Never promise a deliverable for every idea or infer a monetary price from elapsed time. Do not claim a three-hour unattended run is possible unless an actual persistent executor and enforceable limits are verified. Offer a shorter trial when runtime limits require it.

**Additional tripwires (event-triggered, not nagging):** scope or Definition-of-Done change; repeated same-cause failure (e.g. twice) or no measurable progress by checkpoint; projected time/cost overrun; approaching context/window or task quota limit; irreversible/public/private-data or access boundary; new dependency or unverified external claim; drift between canonical and working artifact; missing recovery or checkpoint; independent test disagreement; creative approval boundary. At each tripwire, report what changed, current evidence, recommended safe action and whether an explicit user decision is actually required. If reversible and within prior authorization, correct and continue without needless questioning.

**Review rhythm:** kickoff selects initial mode and a modest budget; the half-month review compares promised versus observed outcomes and costs, then proposes increasing, reducing or retaining autonomy based on real evidence. Never silently upgrade to long-running or paid execution. Keep user-visible prose concise; show the next recommended action as one actionable choice if only one path exists.


### Single-Playbook runner implementation (2026-11-03)

The bounded pilot runner is [skills/markdown-auto-pilot/runner.py](../../skills/markdown-auto-pilot/runner.py). It **does not execute** Markdown-embedded code; it parses the literal `STEPS` list, generates only the AUTO region, requires the exact input SHA-256, checks repeat rendering, and preserves a byte-identical backup on write. In a trusted checkout, compute the SHA-256 of the current local worksheet, then invoke `python skills/markdown-auto-pilot/runner.py docs/templates/LEADER_WORKSHEET.md --expected-sha256 <sha256>` for a read-only check. Add `--write` only after scope, recovery and conflict checks. A preexisting backup blocks overwrites; retain the backup until recovery has been checked.

**Evidence status (2026-11-03): single-Playbook pilot ADOPTED for bounded mechanical use only.** The [GitHub Actions isolated full-source test](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/actions/runs/41602672021) completed SUCCESS on main commit `3612ed73164a0562f680b3b230c949b5b7ed6f73`, Python 3.13.17. The runner executed against a disposable copy of the **actual current worksheet**: pre-write SHA check PASS, write/readback PASS, repeat/idempotence PASS, unchanged human regions PASS, original-byte backup PASS, restore PASS. The AUTO region was already up-to-date (`changed=False`), so no production worksheet mutation was needed or performed. The trusted CI test workflow is `.github/workflows/adnc-markdown-pilot.yml` and remains scoped to this worksheet. Separate AI cold-start/recipient behavior remains NOT_RUN, and automatic production edits/rollout to other Playbooks are NOT authorized. Thumbnail/video/creative Playbooks remain excluded.

## Markdown-embedded Python: single-Playbook operational acceptance gate (2026-11-02)

**Decision ①: test only this leader Playbook first. Do not roll out to all Playbooks.**

**Historical pilot decision (already answered; do not re-ask):** The user selected single-Playbook testing. The earlier comparison was ① single pilot (selected), ② risky all-Playbook rollout (not authorized), ③ explain, ④ hold. This is a historical record, **not** an exception to the current general one-question option contract. Never present a past choice as pending or treat showing an option as approval. The human-readable instructions above remain authoritative. Python is limited to bounded, mechanical regeneration of an explicitly marked AUTO section, not policy decisions, external writes, status promotion, or silent repairs.

Acceptance procedure: (1) fetch the current main file and record Git blob SHA and original bytes; (2) create an isolated candidate, retaining all human-authored text and markers; (3) run the embedded or accompanying Python on that candidate twice and verify byte-for-byte idempotence; (4) verify unchanged human regions, correct AUTO boundaries, valid UTF-8, and no duplicated sections; (5) test malformed/missing markers, stale input SHA, and recovery from an immutable backup; (6) compare candidate to intended requirements and write only after all gates pass; (7) re-fetch the same canonical file and compare content, then verify any required registry/links. **A local pilot is not an operational PASS** until the actual current source, execution log, failures and post-write readback are recorded. Never invoke arbitrary Python from untrusted documents without inspection.

If a required runtime or safe write interface is unavailable, record the precise blocked step, evidence, attempted safe remedy and unblocking condition in the existing issue/review, mark operational test NOT_RUN, and continue with the next independent review item. Do not use the user's selection ① to authorize mass rollout.

## Chat handoff / context compression (shared user-adopted trial; 2026-11-03)

When an explicit leader-chat or cross-AI handoff is requested, refer to [the U-shaped context handoff Playbook](../../skills/chat-handoff/SKILL.md): retain the old role/contract and newest status, heavily trim routine middle dialogue, but preserve any middle decisions, approvals, safety constraints, evidence, and unresolved original-parent steps regardless of position. This creates a handoff *packet*, not a replacement for the current leader worksheet, private START_HERE/registry/write contract, or actual canonical evidence. Check source retrieval and real recipient restart separately; do not report receipt or execution PASS without observing it. Creative/video/thumbnail content and exact approved assets are not subject to mechanical bulk compression. This shared handoff procedure is user-adopted for manual trial by all roles, including secretary and scheduled-review handoffs, but formal distribution and independently verified recipient restart remain NOT_RUN. Do not change any recurring schedule merely by preparing a packet.

---

### Human-edit detection: executable bounded gate (2026-11-03)

The [single-Playbook runner](../../skills/markdown-auto-pilot/runner.py) accepts `--baseline PATH` in addition to the required current `--expected-sha256`. The baseline must be the verified previous complete worksheet. It computes **separate human-section SHA-256** values using the unique `## AI execution appendix` boundary, emits a unified human diff, and blocks writes on any human change with `REVIEW_REQUIRED`. Never automatically regenerate over a changed human section; AI must infer the intent, clarify only material ambiguity, update the machine section accordingly, and then rerun tests against an explicitly reviewed baseline. This gate detects **text changes**, not semantic intent or authorization. It does not automatically read Git history or automatically invoke Python in chat.

**Acceptance:** current and baseline same → no human change; changed human wording → REVIEW_REQUIRED and no write; changed machine appendix only → human UNCHANGED; missing/duplicated appendix → error; stale full-file SHA → refuse. These behavior cases require execution evidence before marking operational PASS. The upstream opt-in rule above still applies; no automatic proposal or acceptance.

## AI execution appendix — machine-checkable STEPS (human instructions above take precedence)

This appendix is for bounded mechanical validation. If a human changes the natural-language procedure, review that diff first, update this appendix to match the intended local customization, and test before reporting PASS. The runner never executes downloaded Python from Markdown and never rewrites human prose. No automatic upstream proposal or publication.

<!-- ADNC:AUTO:BEGIN -->
1. Read current canonical source and record its revision.
2. Check authorization, conflict and recovery evidence.
3. Execute only authorized reversible actions; read back and report.
<!-- ADNC:AUTO:END -->

```python adnc-generated-steps
STEPS = [
    "Read current canonical source and record its revision.",
    "Check authorization, conflict and recovery evidence.",
    "Execute only authorized reversible actions; read back and report.",
]
def render_steps():
    return "\n".join(f"{i}. {step}" for i, step in enumerate(STEPS, 1))
```
