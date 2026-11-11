# 標準コミュニケーションPlaybook｜Designer’s Note

> この文書は2026-11-11 Q7で、対応する実行Playbookから原文のまま局所分離した設計ノートです。本文の採用済み実行規則と未採用の仮説は区別してください。通常利用では読込不要、改訂・障害調査時に取得します。出典となる旧本文はGit版履歴に残ります。

AD&C標準コミュニケーション固有の設計理由。通常の質問・回答では読込不要。改訂・UIの不具合・仕様の衝突のときだけ必要な範囲で参照し、採用済み実行仕様と未検証の設計仮説を区別する。
- 目的：AIが手順を理解していても人間には次に押す場所が見えない、実際に送っていないのに「渡した」とする等の摩擦を減らす。本文のUIと状態区別は実動のための具体化であって、新しい承認儀式ではない。
- 採用済みの判断：結論・実行結果を先に示す。未完了工程を捏造しない範囲で推奨操作0〜2件＋「もう一声」1件。専門UI／入力待ち／ボタン0件が常に優先し、コピー・表示・送信・受領・検収を混同しない。ボタンは実動させる。
- 変更時の注意：これらを全Playbookの生成プロンプトや専門の固定文面へ無断挿入しない。デザイン・サムネイルの創作工程には専門側の固定仕様と裁量を残す。
- 検証の限界：別クライアントでの実ボタン動作・効果は実測のある場合のみPASS。全体のWHYや設計履歴は必要時にリーダーGrand Design／DESIGNER'S NOTEを参照する。
- Python領域はこのPlaybookには無い。Python化のためだけにコードや空の機械コメントを追加しない。

【設計原文の局所移設｜2026-11-11】
ADNC:NOTE_MIGRATION:20261111:COMM
出典：[移設前LEADER_WORKSHEET.md](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/5ba3a955b150d5443153dfee06ff94196e1cb54d/docs/templates/LEADER_WORKSHEET.md)。当時の採用済み判断／設計仮説／失敗の経緯を省略せず保持。通常動作時は読込不要で、改訂・障害時のみ必要な節を読む。下記は実行命令としての追加ではない。

## DESIGNER'S NOTE — 人間が迷わず選べる一問一答UI（2026-11-05、利用者の設計知見）

**参照境界**：このノートは設計の原文・理由・失敗からの着想を保持する。**Playbook作成・改訂担当は対象に既存のDesigner’s Noteがあれば変更前に必ず読み、採用済み仕様と非採用の仮説を分ける**。本ノートを読むこと自体は実行・採用・承認ではない。一般利用時の実際のボタン、コピー、状態分岐は[標準コミュニケーションPlaybook](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/skills/communication-navigation/SKILL.md)の操作条件を用い、専門Playbookにより定められたUIと固定素材を優先する。通常の回答・業務にこのノートの全読取や追加の審査を課さない。


> 「ユーザーを事前にリードして、迷わせないためにボタンを表示するところの整理には特に時間をかけました」

これは装飾の話ではない。AIにとっては複数行の文字列・分岐条件・状態遷移として表現しやすいが、人間は画面を視覚的に走査し、位置・形・強調・色・アイコン・押せることを手掛かりに判断する。**文章として正しいだけでは、使いやすいUIとは限らない。** 一問一答では①最新の状況、②今なぜ本人判断が必要か、③推奨案と理由、④明示的な質問文、⑤実際に押せる選択肢を、この順に配置する。AIの説明量より、人間が迷わず次の操作を選べることを優先する。

### DESIGNER'S NOTE 追補｜基本動作の検索ナビと次の一手（2026-11-09、本人の設計意図）

**狙いは規則による過剰品質ではなく、AIと人間の判断・再指示を減らし、最終成果へ早く到達すること。** 毎回「ボタンは必要か」「次の操作をどう提示するか」をゼロから考えるより、一般応答の既定として**意味のある実動ボタンを原則1つ表示する**方が、AIの迷いと人間の導線探しを減らせる、という本人の設計仮説を採用する。ボタンを出すために次工程を考えることは無駄ではない。**依頼の最終成果から逆算し、まだ必要な次の一手を考える**こと自体が、利用者とAIの期待する仕事である。毎回別の承認や新規案件を作ることではない。

- **操作の既定**：一般の回答では、最終成果に向けた具体的な次の1操作を、実際に押せるボタンで示す方向とする。ラベルは対象と結果が分かる短い日本語にし、選択すれば対応する次ターン／実操作が起きるよう結び付ける。表示や選択だけで外部送信・実行完了・検収を宣言しない。新承認が必要な操作は通常の「次へ」と分ける。
- **考える場所を減らす**：「ボタンを表示するか」は原則として機械的に定め、AIの判断は**最終成果／今の到達点／実現可能な次の一手**へ向ける。作業が完了していれば未完了工程を捏造しない。追加工程を作らずに役立つコピー・再利用等の実動操作を選べる場合だけ使う。
- **専門Playbook優先**：必要な表示・入力欄・選択肢が既に専門Playbookで定義されているならその通りにし、共通ボタンを重ねない。例：ユーザーがログや自由入力を貼る段階では、定型ボタンが入力を妨げるなら表示しない。UIが実ボタン非対応なら短い入力文で代替し、操作不能な飾りボタンは出さない。
- **設計と実装の区別**：この追補は「なぜその既定を選ぶか」の設計意図であり、これをGitへ書いただけで各AIに自動適用された、実ボタンが動いた、既存の個別Playbookが改訂された、とは言わない。既存の[標準コミュニケーションPlaybook](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/skills/communication-navigation/SKILL.md)では承認ボタンを主目的としているため、一般の「次の一手」導線とは目的と適用範囲を分けて扱う。

**情報取得の既定ナビ（文脈が該当するときの探索順）**：まず**①チャット（今の会話、取得可能な過去会話の原文）→②KB（START_HERE／registry／現行Playbook・採用済み決定）→③WEB（公開一次情報、最新仕様や外部反例）→④操作検証**を考える。この順は「本人との文脈や正本に先に届く」ための既定であって、4段階すべての検索を毎回義務化するものではない。初めから最新の公開情報が目的ならWEBを優先し、既存正本が明示されていればそこへ直接進む。対象の原文・現在の版・実物が判断の根拠である場合、その取得前に内容固有の評価を確定しない。検索順の最適性は未測定であり、運用上の初期仮説として扱う。

- **検索結果を四つに分ける**：「未検索」＝検索していない、「検索したが未発見」＝検索範囲内で見つからなかった、「取得不能」＝接続・権限・形式などで本文を読めない、「取得済み」＝現行本文を実際に読んだ。存在しないという断定は、未発見や取得不能から導かない。「検索した」と実行していない操作を報告しない。
- **原文が必要なら原文を待つ**：特定チャットの指示文や文書の品質評価では、タイトル・記憶・断片から当該原文を読んだふりをしない。未取得なら、その事実と試した範囲を短く示す。一般論の提示は原文評価と明確に区別し、無理に内容を補完して結論を出さない。取得可能な別経路があるか先に探し、人間による再提示は最後の補助手段とする。
- **④操作検証は「無理」と言う前の短い再確認**：ツール操作の入力・パス・引数・APIの呼び方を誤ったために「できる操作をできない」と誤報告することを抑える工程。Playbookの「必要資料・素材・ツール」にある**実体へのパスとAI向け自然言語の使い方入口**（[開発プラクティス「ツールの1入口・発見可能性」](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)、必要なら開発調査Skillの道具棚）を参照し、実在・現在の権限・操作仕様を確認する。初回がツールの使い方の間違いと疑われる場合、同一目的の正しい小さな操作を**原則1回**試してから不能を報告する。サービス・権限・安全上できない枝は無理に再試行しない。操作を試せなかった場合は「未検証」、試した結果の拒否は「実際の制限」として区別する。
- **運用を重くしない**：既存の専門Playbook・KB入口の資料を再度全文複写せず、該当する道具への短いリンクを使う。これは事前チェック表、全件検索ゲート、全ツール操作の再試験、長い検索報告の追加ではない。通常は得られた答え・成果と必要な未確認点を簡潔に返す。

設計・検収観点：
- ボタンは文章中の番号の飾りではなく、対象親IDと選択意味を次のターンへ渡す**実際の動作**を持つ。操作できない環境では番号付きテキスト入力へ切替える。①稼働確認済み担当へ委任（いるときのみ）、②新チャット委任、③詳説、④保留の意味を保持し、選択だけで実行・受領・検収が済んだと誤表示しない。
- 赤字などの警告色は危険・未解決・失敗等の**意味がある場合だけ**に使う。色だけに依存せず文字ラベルやアイコンも併用する。アイコンは意味の一貫性を保ち、飾りを増やさない。通常の見出し・情報は落ち着いた階層で示す。
- 主操作の視認性、選択肢の間隔と押しやすさ、長文の折返し、画面サイズ、コントラスト、キーボード/読み上げ代替、誤操作の戻し方、操作後の状態表示を確認する。確定済みの選択を勝手に変更しない。
- 新チャット委任の詳細はKBへ保存・読戻しし、画面の最終まとめには短い1行だけを案件別に集約する。押す前に何が起きるかを明確にし、押した後の委任・受領・実行・検収を別状態で表示する。
- **研究メモ（未検証の仮説）**：文章だけの選択肢と、質問による事前誘導＋明確なラベルの操作ボタンを比較し、選択までの時間、誤選択、質問し直し、完了率、主観的な迷いを評価する。色・アイコン・位置・文面を一度に変えず、アクセシビリティ条件も含めて比較する。利用者の実体験を設計要件として記録するが、定量的な効果を実証済みとは扱わない。

このノートは定例の表示・UXに関する知見であり、Work60第0工程、固定枠、KB書込ゲート、既存の権限・承認を変更しない。

### DESIGNER'S NOTE 追補｜通常対話の推奨0〜2件＋もう一声（2026-11-09、本人の設計決定）

通常のAI対話では人間の満足地点をAIが推測する必要はない。AIは現在の根拠で結論と実行可能な推奨を0〜2件示し、その最後に**方向を変えて検討し直したいという人間の明示コマンド「もう一声」**を控えめな補助操作として原則1件出す（合計最大3件）。推奨がない場合も結論＋「もう一声」。人間が満足なら何も押さずに終了し、細かい希望があるなら通常のチャットで伝える。**押されない限りAIは勝手に別方向へ探し直さない。** 2件を埋めるための案の水増し・新たな満足推定・追加ゲートを作らない。

本追補は上記2026-11-09「原則主ボタン1件」という先行設計の**通常対話における表示件数を更新**する。専門Playbookの操作UI（秘書の既存4択、結果提出・自由入力待ち、ボタン0件）はそのまま優先し、「もう一声」を重ねない。正式な機械的実行条件は[標準コミュニケーションPlaybook](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/skills/communication-navigation/SKILL.md)に置き、設計意図を通常実務の停止条件に変えない。

**2026-11-10の出口処理の着想（設計理由・原因は仮説）**：本人の観察「結論が終わったらボタンを出せばいいだけ」「ボタン入力には次もボタンを出せとの指示を埋め込めるが、人間が書き込むと欠ける」。Work60の配送UNKNOWNを巡る対話で、AIが次の操作を文章で提案したのにボタンを表示しなかった事例が発端。**ボタン規則そのものの欠落ではなく、自由入力・長い調査や障害解析後に出口規則の適用が抜ける**可能性を扱う。ただし原因がコンテクスト長・AIの内部処理・UI制約のどれかは未検証。理念は「人間の再指示負担を減らす」ことであり、ボタンを表示するために作業を止めたり架空の仕事を作ることではない。製品側の将来改善で不要になり得る補助設計として、通常回答の最後に既存表示契約を適用するだけに留める。実装のHOWは[標準コミュニケーションPlaybookの共通出口](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/skills/communication-navigation/SKILL.md)に限定し、専門の固定UIやWork60の配送認可・UNKNOWNの重複防止条件は変えない。


【Q3逐次分離・原文保全｜Q3-LOCAL-COMM-20261111】
出典：docs/templates/LEADER_WORKSHEET.md の2026-11-11変更前Git版。以下は移設前本文の原文保全であり、通常実行では既存の専門Playbook実行節と本人最新指示を優先する。歴史的な選択肢・古い制約を新たな承認・自動実行命令にしない。

## One-question lead-in requirement (2026-11-05; minimal clarification)

After checking the current unresolved state and carrying out available safe work, ask only about an unresolved item requiring a real human decision. **Never display bare numbered options without a leading question.** Present, in this order: (1) the parent ID and latest verified unresolved fact, (2) why authorized automatic resolution cannot finish it, (3) a concise recommended route with its reason, and (4) an explicit natural-language question immediately before the selectable options, such as 「この未解決案件を、どの方法で進めますか？」. Make the question specific to the decision; do not imply that choosing an option itself completes implementation.

Use the latest user-corrected choice semantics: ① delegate to a verified active responsible leader **only if such a leader exists**, ② prepare a standalone new-chat delegation instruction, ③ explain in more detail, ④ hold. Automatic secretary/leader repairs belong **before** the question and are not an option. Show one question at a time, at most ten, and do not re-ask settled approvals. If no genuine human decision remains, report 「本人判断が必要な質問：0件」 and show no inert controls. Keep recipient acceptance, actual execution and readback as separate statuses. This is a presentation requirement, not authorization to alter private KB or bypass any existing gate.


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


## Copy-ready instruction formatting (2026-11-03; user-directed)

When presenting a prompt or instruction that the user should paste into another chat, AI, or tool, put the **complete copyable instruction inside a fenced Markdown code block** (triple backticks). **Exception:** for user-selected new-chat delegation with a verified KB-backed handoff, the complete *instruction to fetch and act on the KB handoff* is deliberately a short one-line KB reference; all task detail belongs in the private KB, not in the code block. Keep the explanation, evidence, caveats, and PASS/FAIL/NOT_RUN status **outside** that block. Preserve exact wording, URLs, parent IDs, test criteria, and report destination within the block; do not split one instruction across multiple fragments. Use a plain `text` fence or no language tag, not a programming-language fence that implies executable code. Apply to independent-test handoffs, new-chat delegation, leader/secretary handoff and other copy/paste instructions; this is presentation only, not approval or authorization. If the interface supplies a genuinely copyable writing artifact instead, that may be used, but never bury the actionable instruction in surrounding prose.

**Independent-test chat naming (2026-11-03; user-directed):** Never start a copy/paste independent-test instruction with the generic label `独立試験`. Start its first line with the specific subject, project, or Playbook being tested and put `独立試験` at the **end of that title**, e.g. `AD&C 開発リーダーPlaybook 独立試験`, `AD&C 山歩きPlaybook 独立試験`. This applies to the first line of the copyable prompt and any proposed chat title so distinct tests are distinguishable in conversation lists. Do not use a generic `独立試験｜...` prefix. Preserve existing test content and acceptance criteria.


