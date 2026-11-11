# Playbook作成・更新テンプレート｜Designer’s Note

> この文書は2026-11-11 Q7で、対応する実行Playbookから原文のまま局所分離した設計ノートです。本文の採用済み実行規則と未採用の仮説は区別してください。通常利用では読込不要、改訂・障害調査時に取得します。出典となる旧本文はGit版履歴に残ります。 **本文中の旧「同一ファイル末尾HTMLコメントへ置く」等の記述は移設前の履歴として保存したもので、現行の配置仕様は[開発プラクティス v0.1.15](../docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)または各対象の現行標準が優先します。**

通常の実行ではこの末尾コメントを読む必要はない。障害・改訂・意図の解釈で必要なら参照できる。ここに置く内容は対象Playbookの歴史・設計理由であり、新しい実行命令や承認条件ではない。
このテンプレートの既存のDesigner’s Note本文と着想例を削らず、移動して保持する。実案件へコピーするときは対象固有の設計判断へ差し替え、他案件の仮説を実行条件にしない。

## DESIGNER'S NOTE（デザイナーズノート／自由記述・保存ルール正式採用）

**目的**：通常の【背景】2〜3行や変更履歴に圧縮すると消える、設計者の原文・直感・パッション・違和感・意外な失敗・採用しなかった案・変更したくなった理由を、将来の改訂・反証の手がかりとして残す。合理的に説明できない着想も記録してよい。**この保存・参照ルールは正式仕様（2026-11-04 本人指示）**。ノート内の設計思想・未採用の仮説は、確定仕様・実証結果と区別する。記録だけでは命令・採用・実証・変更許可にならない。全Playbookへの一斉追加・Active化を意味しない。

- **記録する時**：創作や設計の転機、失敗から得た着想、判断が割れた時など、後の変更で意味を持つ場合。原文の引用を優先し、可能な範囲で観測事実／仮説／本人の確定判断を区別する。不要な固定フォーム、文字数、全案件への記入義務を設けない。既存Playbook内の短い自由記述で足りるなら新しい別ファイル・台帳を作らない。
- **普段の実行時**：採用済みの目的・背景・素材・禁止事項・完成条件を使う。ノート全文を毎回読み込ませず、制作AIへのプロンプトへ自動注入しない。創作担当の発想を過去の議論で過度に固定しない。
- **参照する時**：**Playbookを作成・改訂するときは、対象に既存のDESIGNER'S NOTEがあれば毎回変更前に必読**。重要な設計変更・デグレ・失敗原因調査・意図の再解釈では、必要な関連ノートも参照する。本文と現行正本・実成果を照合し、採用済み／未採用を区別する。通常の実務実行にはノートの毎回参照を求めない。
- **優先順位と境界**：本人が確定した文字・構図・素材・段階的な承認、現行の専門Playbook・安全条件を上書きしない。確定作品の変更は本人が指定した差分だけ。仮説の採用には隔離試験・実物評価・必要な承認を別に要する。非公開の経緯、人物情報、個人KBのURL・IDは公開テンプレートへ転載せず、利用者の非公開正本側に置く。

### 最初の記録例：創作を助ける「思考断絶」（2026-11-04／仮説・未検証）

着想の原文（要約へ置換せず保持）：

> 「うまく思考を断絶」
>
> 「枠の作成(オブジェクト配置)→タイトル文の『創造(創造力！)』」
>
> 「論理ではなくて、いろんなパターンを作ってみて動くかどうかをエンジニアリング的に『調整』するしかない」

**仮説**：シナリオ・PPT完成で論理の役割を終えたら、創作担当には不要な試行錯誤を引き渡さず、必要な目的・素材・禁止条件は維持する。次にオブジェクト配置の「枠」を試し、未確定のタイトル文を創造し、合成・検収する。**文脈の継承能力と、意図的な文脈の切断による創造性は両立し得る**、という探索対象である。既に確定したタイトルや素材を創造段階で書き直す許可ではない。

**実験の候補**：一度に一条件だけ変更し、(1)新チャット・別担当への引渡し量、(2)枠とタイトルを考える順序、(3)創作指示の言い方、(4)構図と文の往復調整を順次検討。実際の文脈切断と「同一チャットの役割宣言」は分けて記録する。**制作品質（人間の評価）／実行手順遵守／文脈断絶の効果**を混同しない。前回の参考画像は正式な断絶比較実験の成功証拠ではない。

**現在地**：設計仮説のみ。画像生成・Workによる再実験・CASE A改変・本人評価は本節の追加では実施していない。既存MUSE採用CASE Aは凍結し、模倣・強制採用・機械的一括書換えを行わない。

Python領域を設けるPlaybookでは、この人間側コメントをPython領域の直前に置き、Pythonの末尾に次の形式で**コード内コメント**を付す（Pythonなしの場合は不要）。
`# ADNC:DESIGNER_NOTE:PYTHON:BEGIN`
`# 通常実行では読込不要。入出力・AUTO範囲・人間本文保護・復旧の設計理由を書く。`
`# ADNC:DESIGNER_NOTE:PYTHON:END`

【設計原文の局所移設｜2026-11-11】
ADNC:NOTE_MIGRATION:20261111:PLAYBOOK_AUTHOR
出典：[移設前LEADER_WORKSHEET.md](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/5ba3a955b150d5443153dfee06ff94196e1cb54d/docs/templates/LEADER_WORKSHEET.md)。当時の採用済み判断／設計仮説／失敗の経緯を省略せず保持。通常動作時は読込不要で、改訂・障害時のみ必要な節を読む。下記は実行命令としての追加ではない。

### DESIGNER'S NOTE 追補｜「作り込みは濃く、運用は軽く」（2026-11-08）

> 「作りこみ重視、ワークシートなどのツールで品質を担保、過剰品質・検査は避ける」

**ワークシートはAIを規則で縛る審査票ではなく、必要なときに素早く正しい作業・画面・判断へ辿るための小型KB／実行ツール。** ボタンの意味、視覚的な見落とし防止、操作の流れ、分岐、機械化できる作業は、道具側に具体的に作り込む。使わない案件にその検査やフォームを課さない。作り込みの濃さと、利用者・担当AIの運用負担の軽さを**両立**させる。

新しい改善を採用するときの設計軸は、**「次のAIはこれで実務をやりやすくなるか、それとも全員の義務が増えるだけか」**。局所改善にはまず局所適用を選ぶ。本人が一案件について「はい」と答えても、全担当への汎用必須ルールの承認と見なさない。共通化するなら便利な機能・検索入口・失敗回避の知見を先に共有し、一律の事前チェック・重複承認・詳細報告は増やさない。必要な重大安全・機密・権限・不可逆操作と本人が特に指定した条件は守る。

この判断の**作成・更新側の正本**は[共有KB開発プラクティスのPlaybook・ワークシート作成更新節](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)。本ノートはUIと道具の「なぜ」を残し、下記の具体的なボタン設計契約は維持する。別の審査Playbookや新しい管理表を作らない。

### DESIGNER'S NOTE 追補｜説明書から使える道具へ（2026-11-10）

**設計意図／理念（開発プラクティス本文から移設）**：品質を担当AIの毎回の高度推論・大量の検査・承認儀式に頼らず、既存Playbook・ワークシート・実行ツールに作り込んで、普通の依頼を簡単に完走できるようにする。**ツールの機能が増えても、全員の遵守義務が増えるとは限らない。** これは新しい事前ゲートではなく、既存手順を作成・更新する際の設計判断である。

**設計判断の原文（開発プラクティス本文から移設）**：「次のAIが仕事をしやすくなるか／新たな管理負担が増えるだけか」で比較し、完成度・実用性・作業時間・重複と混乱・手戻りをまとめて考える。機能が便利でも、全件の開始条件にはしない。例外は重大な安全・機密・権限・不可逆操作または本人の明示的な完成条件に必要な場合。

**今回の発想（本人発言）**：
> 「単なる手順ではなく、便利なワークブックにするのがAD&Cの思想でしょ？」
>
> 「プレイブックワークシートはテキストでよくない？」
>
> 「理念の部分はデザイナーズノートに避難させて、プレイブック自体はツールにしていこう。」

**理由**：AIが説明書を読んで毎回素材・手順を組み立て直すのではなく、目的からテキストで探して候補を見つけ、必要なときだけ画像で比較し、実ファイルを取得して使えるようにする。道具の側を作り込み、現場の利用・制作の自由を軽くする。PPTアイコン集はこの設計の具体例であり、全作品へのアイコン使用命令や新しい審査・OCR義務ではない。

**実行境界**：このノートはWHYと設計の来歴を記録する場所。実際の作成・改訂手順は[開発プラクティスの当該節](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)、素材の発見・選択・取得は[既存アイコン探索ワークシート表D](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/skills/video-production-setup/PRODUCTION_ASSETS_GENERAL_SPEC_v0.1.md)を参照する。ノート自体から普段の制作を開始・停止・再承認させない。

### DESIGNER'S NOTE 追補｜AIと人間の二重インターフェース、進歩の土台（2026-11-10）

**着想・出典**：[2026-11-09公開の本人構想記事「玄人の『当たり前』を、次の人たちの進歩の土台に」](https://campsite7.jp/2026/11/09/adnc-progress-foundation-concept/) および2026-11-10のPlaybook／アイコン素材集の設計対話。記事は**目的と思想を説明する本人の構想**であり、教育効果や制作効率の実証ではない。

**目指す姿**：専門家には当たり前でも初めての人には難しい知識・道具・判断を、既存AIと人間が読めるPlaybookでつなぎ、最初の検索・解釈・AIへの再説明という摩擦を減らす。「便利に使って終わる」人も、「使いながら仕組みを理解して次へ進む」人も同じ入口から参加できる。**理解・改良・共有は可能性として開き、学習・GitHubへの投稿・公開は義務にしない**。AD&Cが独占することより、実現が早まり、誰かの経験が次の人の足場になることを重視する。

**二つの利用者を同時に想定する**：
- **AI向けインターフェース**：自然言語の目的から既存の知識／素材／ツールを発見し、選択、実体取得、実行、必要な確認・復旧へ進める。曖昧な暗黙知を検索語・使いどころ・原本リンク・境界条件として道具側に作り込む。
- **人間向けインターフェース**：日本語で「何をしようとしているか・どう進んでいるか・何を自分で判断できるか」を読み取れる。AI専用の不透明なコードだけを唯一の説明にせず、必要なら根拠・手順・結果・失敗から学び、提案・修正に進める余地を残す。全工程の読解を通常作業の条件にはしない。
- **共有KBとの接続**：実用上の発見・反例・失敗や修復のうち、一般化できる部分を、個人情報や私的Contextから分けて再利用可能な形で育てる。AIが次の利用者へ案内するのに必要な入口を持たせるが、利用者自身への知識提供・投稿要求はしない。

**設計上の緊張**：AIの実行だけを最適化すると、人間には意味が見えないブラックボックスになりやすい。説明を厚くしすぎると、便利に使いたい人や制作AIを妨げる。よって**実行本文は最短の道具、学びたい人には日本語の見通し、設計意図はDesigner’s Note**に分ける。定型操作は機械化し、表現・創造・最終判断の自由を残す。人が「中級者への入口」に進めたかどうかは未測定であり、成果を保証しない。

**実行への橋渡し**：Playbook／ワークシートの作成規則は[共有KB開発プラクティス](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)が正本。実例は[テキスト主体のPPTアイコン探索ワークシート](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/skills/video-production-setup/PRODUCTION_ASSETS_GENERAL_SPEC_v0.1.md)を参照。このノートを制作時の全文必読・追加審査・公開義務に変えない。


【Q3逐次分離・原文保全｜Q3-LOCAL-TEMPLATE-20261111】
出典：docs/templates/LEADER_WORKSHEET.md の2026-11-11変更前Git版。以下は移設前本文の原文保全であり、通常実行では既存の専門Playbook実行節と本人最新指示を優先する。歴史的な選択肢・古い制約を新たな承認・自動実行命令にしない。

## Entry-first creation and acceptance
Before creating or substantially revising a playbook or worksheet, check existing shared/personal KB procedures and Skills for equivalent purpose; distinguish Active, Draft, superseded, and withdrawn. Define a natural-language request that should lead to the procedure, its directly fetchable canonical source, version and applicability. Treat `request → discover → fetch → execute in specified order → inspect required output → present useful result` as one deliverable. A README link alone is not automatic discovery. When a task actually calls for independent discovery or behavior verification, reuse existing Q1 (entry and document), Q2 (independent cold-start interpretation), Q3 (actual sequence and relevant safety boundaries), and Q4 (user-facing result). Do not require all four as a routine preflight for every minor change; mark untested stages as untested rather than stopping unrelated safe work. **Design for easy execution first, not more compulsory verification.** Avoid creating another registry or gate. Preserve private identifiers outside public KB.


## Human-first Playbook customization and upstream proposal (2026-11-03; user-approved design, pilot only)

Keep **human-readable natural-language instructions first**, followed by an explicitly labeled **AI execution / Python reference part** within the same Markdown file when applying the single-Playbook structural pilot. The natural-language part is the local authority for purpose, steps, decisions and stop conditions. Do not silently replace a human edit with generated content.

When a human changes the natural-language part: (1) compare it against a verified previous revision and record the changed region/hash; (2) infer the intended behavioral change from the diff and surrounding context, and ask one focused question **only when the intent materially remains ambiguous**; (3) honor the local human edit within existing safety/authorization boundaries, update dependent Python/checks and local Playbook **as an authorized reversible customization**; (4) test consistency, idempotence, recovery and actual readback, marking blocked stages NOT_RUN; (5) distinguish local customization from a proposed general improvement. Do not presume a mere text diff proves the author's intent. If the edit conflicts with a mandatory security, legal, authorization or upstream contract, preserve the human edit and report the conflict instead of silently overriding either rule.

**Upstream opt-in:** After the local change is accepted, explain any reusable generalization briefly and ask whether to submit a proposal to the AD&C main repository. No upstream Issue/PR or publication without the user's explicit opt-in for that proposal; no automatic upstream merge. If clearly local-only, do not pester the user. Do not copy private IDs, data or environment-specific settings to a public proposal. Use the existing central Issue or standard contribution route; do not create duplicate tracking systems.

**Scope:** This is a **single-Playbook design/pilot**, not a mass rewrite of existing Playbooks. The separate runner and SHA gate remain bounded tools; a Python file's existence does not mean the Markdown executes it automatically. Structural migration, local human-edit detection, semantic alignment and independent cold-start behavior must each be separately tested before claiming production PASS.


