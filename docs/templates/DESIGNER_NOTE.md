# AD&C 開発リーダー｜Designer’s Note（局所設計原文）

> 2026-11-11のリーダーワークシート軽量化で、グランドデザインの長文と既存局所Noteを移設。以下の2つの【原文】ブロックは移設前の本文を**一字一句変更せず保全**。配置・実行契約は[現行リーダーワークシート](LEADER_WORKSHEET.md)と[共有KB開発プラクティス](../../docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)が優先。通常のリーダー巡回には全文読込不要。重要な設計変更・衝突検討時だけ参照。

旧版全体（実行契約等の長い議論を含む）：[整理前ワークシート・Git履歴](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/824565f201dad52dc9509d128308823d127fb509/docs/templates/LEADER_WORKSHEET.md)。

## 移設前グランドデザイン原文

## AD&C grand-design engineering principle (approved 2026-11-04)

> **設計理念の解説・採用理由（実行手順ではない）**。AD&Cの公開理念は[README](../../README.md)が正本。本節の示唆を理由に、既に承認された作業を停止、専門Playbookの固定工程を変更、追加の承認や検査を要求しない。通常の実行条件は共通・専門Playbookの具体的操作欄に置く。

AD&C is a practical navigation system for imperfect humans and imperfect AI, not an attempt to attain 100% theoretical completeness. Select the context-appropriate scale of knowledge, show the next actionable turn, recalculate when reality changes, and preserve human control. Prefer small reversible implementations with measured user benefit over short-term logical elegance alone; use observed failures to revise hypotheses and procedures. Combine explicit rules with the empirically observed flexibility and behavior of each AI interface. Do not confuse an attractive theory with verified implementation, operation, effect, or independent test. Keep free/manual routes, bounded recovery, and evidence-based corrections. This principle guides design tradeoffs but never overrides existing permissions, private-KB write gates, or publication approvals.

**Project mission / public-facing charter (2026-11-04, editorial clarification):** 「完成形のない仕組みで、完成する仕事を増やす。」 AD&C has no final perfected architecture; each user-requested deliverable still has a concrete acceptance and readback gate. Balance the useful features and limitations of an imperfect AI with safety, human understanding, time and continued user control. Aim for social benefit through actual usable outcomes, not through an unsupported claim of guaranteed success or measured QOL gains. Do not treat permanent evolution as permission to leave requested work unfinished.

**Anti-local-optimization cue (use at the existing decision point; no new audit loop):** When you are about to add another abstract layer, reopen a settled decision, repeat a local check without progress, or delay an approved reversible implementation for theoretical elegance, ask: *“Which specific user outcome or required safety condition will this next step improve?”* If a concrete benefit is absent, stop optimizing that part and proceed with the smallest already-authorized, verifiable action through actual output and readback. If a safety, rights, accuracy, or approval constraint is real, meet it rather than bypassing it. Separate `implementation`, `operation`, and `effect` as PASS / FAIL / NOT_RUN; do not count a plausible theory or documentation alone as proof of user benefit. This is a **decision reminder**, not an additional checklist, process or deadline.



## 移設前のリーダー固有Designer’s Note原文

このリーダーワークシート固有の設計メモ。**通常の巡回・実務では読込不要**。仕様改訂・判断の衝突・不具合調査で必要なら参照する。内容はWHY／経緯であり実行命令・承認・停止ゲートではない。
- 理由：作り込みは濃く運用は軽く。人間に伝わる本文を正本とし、AIに必要な固定動作は既存ツールへ移す。全欄検査や3巡・全SHA同期・毎回のDesigner’s Note取得を要求しない。
- 設計原文の現在地：次の一手・UIは[標準コミュニケーション](../../skills/communication-navigation/SKILL.md)の末尾、道具化・二重インターフェースは[Playbookテンプレート](../../templates/PLAYBOOK_TEMPLATE.md)の末尾コメントへ局所移設。歴史的な原本はGit版履歴で保持。必要な対象だけ開き、未採用仮説と確定判断を区別する。
- 固定境界：人間が変更した自然言語の目的・手順を機械生成で戻さない。末尾のAUTOは限定的な定型工程で、別AIの自動実行・全Playbook展開・動画／サムネイルの機械的一括変更を意味しない。
- Python側の詳細は直後のAI appendix末尾にある # ADNC:DESIGNER_NOTE:PYTHON コメントを参照。非公開情報を公開側へ出さない。
