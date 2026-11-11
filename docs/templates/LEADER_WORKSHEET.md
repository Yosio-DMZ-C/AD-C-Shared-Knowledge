# Leader worksheet v0.1

Use this worksheet for leader-only decisions, patrol, evidence and reports, not as a central storage dump for all specialist Designer’s Notes. Specialist reasons and tools belong next to their own Playbooks; keep a short link here when needed. This is a format, not a decision procedure. Refer to the existing registry and operating rules for authoritative facts and approvals.

**正本の役割分離（2026-11-09）**：AD&C全体の理念（WHY）の公開正本は[共有KB READMEの宣言・理念](../../README.md)。このワークシートのGrand Design・DESIGNER'S NOTEは設計背景と採用理由（WHY / design history）であり、普段の担当AIの着手可否や停止を判断させる実行契約ではない。共通の機械的な操作（HOW）は[標準コミュニケーションPlaybook](../../skills/communication-navigation/SKILL.md)、Playbook作成・改訂の手順は[共有KB開発プラクティス](../../docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)、専門固有の秘訣・安全・制作順序は各専門Playbookを正本とする。**Playbookの改訂担当は対象に存在するDesigner’s Noteを変更前に必読**。普通の実務担当にはノート全文の毎回取得を強制しない。

**リーダーの本人向け応答における実動ボタン（2026-11-10・既存共通規則の適用）**：通常の相談・進捗回答では、[標準コミュニケーションPlaybook](../../skills/communication-navigation/SKILL.md)の**推奨アクション0〜2件＋補助「もう一声」1件**を既定にする。結論・実装結果を先に返し、実行可能な次の一手があれば対象と動作を一致させてボタンに結ぶ。承認済みの可逆作業をボタン待ちで止めず、未送信を送信済みとしない。**定時巡回の定型報告、Work60の1行配送文・固定入力、独立試験の結果待ち、専門UI／ボタン0件の指定には汎用ボタンを足さない。** 既存の［見直す／保留］等の具体的な本人判断UIと安全・新承認境界を優先する。実ボタン非対応なら実際に使える短い返信またはコピー文にする。これは既存共通HOWへの参照であって、Work60固定契約や各担当への配送権限を変えない。

## 別チャットへの調査委任カード｜リーダーのコピーUI（2026-11-10）

**使い所**：規約・外部仕様・異分野の反例・独立検証など、別担当の調査結果をリーダーが集約すると早い案件では、リーダー自身の長い説明や本人への調査結果の転記依頼より、**「新しいチャットで○○を調査」＋「結果は既存リーダー報告先へ直接保存」**の委任カードを主操作の優先候補にする。本人が直接処理を依頼した可逆な仕事まで委任待ちで止めない。既存Work60・ORCH80の配送契約や専門Playbookの専用UIを置き換えない。

**組立入力（このワークシートの道具欄。毎回人間に入力させない）**：リーダーが既存正本から `親ID／調査名／完成条件／確認済み事実と正本URL／禁止・権限境界／既存リーダー報告先の実URLと報告ラベル` を充填。報告先は対象の既存Project／80_reviews／運行票等から具体的なアクセス可能先を選ぶ。リーダー個人の生チャット宛に勝手にメッセージが届く仕組みは仮定しない。非公開情報を公開Issueに書かない。適切な書込先が未確認なら未確認と明示して架空の直送を約束しない。

**完成指示文を機械的に組み立てる**（実案件の値を差し込む。下記は新規管理票ではない）：

```text
【AD&C｜{調査名}｜既存親{親ID}】新規チャットの独立調査担当です。
目的／完成条件：{完成条件}
確認済みの事実・現行参照：{事実と正本URL}
今回の作業：必要な一次資料・反例を調べ、事実／推論／未確認と出典・検証結果を区別して結論を出す。
禁止・境界：{禁止・権限境界}。既存親・採用済み決定を変更しない。別試験の自動連鎖をしない。
【リーダー報告先】{既存非公開保存先URL} の既存親{親ID}に【LEADER_REPORT｜{調査名}｜{親ID}】として「結論・根拠URL・PASS/FAIL/NOT_RUN・残件・次の1操作」を直接保存し読戻す。リーダーは既存巡回／同一案件から回収・判断する。本人に結果の再転記を頼まず、公開Issueへの私的情報投稿もしない。
保存・直送の権限がない場合は「DIRECT_REPORT_NOT_EXECUTED／理由／得られた結果」を明記し、受領済みと偽らず終了する。既存の安全な別経路だけ利用し、権限拒否を迂回しない。
```

**画面は2行＋実動ボタンが基本**：件名・一言の目的・「コピーして新規チャットに貼り付けてください」を表示し、**［調査指示文をコピー］**を押すと上記の値を埋めた**全文**をクリップボードへコピーする。全文を通常回答に垂れ流さない。対応するUIなら実コピー操作（例：`GenUI.copy(完成指示文)`）をボタンに結び、押すだけで新規チャットを作成・送信したと表示しない。同じ完成原文を開ける**［全文を確認］**も並べ、通常は折りたたみ、押すと改行・見出し・URLを保持した全文を読み上げ可能なテキストとして展開する。長文は表示領域内のスクロールを優先し、プレビューとコピーの内容を別々に生成しない。UI非対応時は全文を単一のコピー可能なブロックに収め、必要なら長文原本を既存の保存先へ置き、短い起動文を提示する。共通の表示・代替仕様は[標準コミュニケーション](../../skills/communication-navigation/SKILL.md#長文の指示文引継ぎ文を渡すときの共通ui)を参照する。アクセシビリティ・入力待ち・専門UIには従う。

**状態**：`指示文準備`・`コピー`・`新チャット送信`・`担当受領`・`既存先へ結果保存`・`リーダーによる回収`を混同しない。**報告の直接書込・読戻しが確認された時だけ「保存PASS」**、リーダーが読んだ証拠がある時だけ「受領PASS」。本人を報告の中継役にせず、最終採否はリーダーが担う。[既存チャット引継ぎPlaybook](../../skills/chat-handoff/SKILL.md#独立試験から集約担当への一方向引継ぎ2026-11-09-本人決定)の一方向終了規則と、[標準コミュニケーション](../../skills/communication-navigation/SKILL.md)の実動UIをそのまま使う。新しいタスク・ゲート・追跡DBを作らない。

**Execution model (2026-10-29 β):** Team members complete their authorized reversible changes through canonical writes, reference/Git integration and readback; the leader audits across changes and repairs scoped inconsistencies. Follow the actual enabled patrol schedule; this worksheet does not set its cadence or add preflight gates. Audit significant dependencies and actual restorability, not just reported completion. Avoid new trackers and duplicate approval prompts.

1. New changes: record only new facts, or 'no new changes'.
2. Reconciliation: note sources checked, discrepancies, and unverified claims.
3. Implementation: record actual writes, commits, readback, and PASS / FAIL / NOT_RUN.
4. Recovery: identify prior version and whether rollback was actually tested.
5. Next action: one priority and, if needed, one approval question.

Keep routine reports brief. Mark irrelevant checks N/A with a reason. Never report a draft or unverified change as DONE.

## 本人最終決定（2026-11-08）｜担当は実装、問題はリーダーが解消

**Q5に伴う開発・運営トラブルの担当分離（2026-11-11・本人指定）**：AD&Cの利用者向け標準（理念／KBナビ／基本ふるまい／秘書／専門Playbookの利用）そのものではない、**開発・運営設備側の問題**（例：Work60の送信経路障害、巡回の実行環境・オーケストレーション不調、関連ツールの接続障害）は、既存**サブリーダーを一次切分け・修復・再試験担当**とする。リーダーは既存案件ID・実物・直近証拠を渡して結果を同じ報告先から回収し、設計全体への影響・本人の採否だけを判断する。AD&C製品の一般的な利用・KB内部の局所修復を、開発設備の障害に巻き込んで止めない。

**実行と委任は別**：本役割分担を記載しただけではサブリーダーへのメッセージ送信・受領・修復は完了していない。既存の認可された配送経路が使えるときに既存親IDへ依頼し、送信状態UNKNOWNを未送信へ変更しない。送信できない場合でも、他の許可済み工程を進め、問題と次の一手を既存記録へ保全する。既存の巡回・Work60運行票、スケジュール、runner、安全/権限境界は変更しない。

**AD&C独自のSTOP・HOLD・全PASS・事前承認待ちは撤廃する。** このワークシートは停止審査票ではなく、実施した結果と問題を短く受け渡す道具とする。既存のGit・Drive版履歴を復旧に使い、旧判定や古いHOLDを現在の停止命令として再適用しない。

担当は既存正本に実装→可能なら実物を読戻し→「実施／現物リンク／問題と影響／次の一手」を既存案件に残す。問題があっても成功部分を保全する。`DONE`・`DONE_WITH_ISSUES`・`NOT_EXECUTED` を区別し、未検証をPASSと称さない。原因の解明・全件形式・SHA連鎖・第三者レビューは実装開始の前提としない。

**リーダー定時巡回**は新着の `DONE_WITH_ISSUES`・修復待ち・実環境制約を優先し、毎回可能な具体修正を1件以上実施して、同じ案件の実物へ保存・読戻しする。解決不能な問題のみ `本人判断事項＝何を判断してほしいか／選択肢・影響／推奨案` として本人に上げる。巡回のための新しいDB・管理Issue・承認ループは作らない。

`STOP` は外部の実制限・本人個別指示によって実行できなかったという事実表示のみ。`REQUIRED` は完成品の条件であって部分実装・試作の停止条件ではない。`OPTIONAL` は任意の品質・UX・監査補助。競合や欠落も問題を記録し、独立した作業は進める。AI／サービス規約・実権限・法令の条件は別途適用する。

**オンデマンドの実行補助**：DESIGNER'S NOTE／T007／専門Playbookは実際にボタン・GUI・制作物で必要な場合にだけ参照する。新しい形式審査を増やさず、採用済み部分は勝手に作り直さない。

## 定時巡回の報告ワークシート｜実績と記録を分けて見せる（2026-11-08）

**既存案件の実行基盤・復旧を引き継ぐとき（T014/T015/T005の2026-11-10実証から）**：巡回は新しい仕組みを作らず、対象の既存IDにある「最終成果・入力・実行基盤・最後の成功した実物／版・保存先・受領先・未実行の次の一手」を必要な箇所だけ再取得する。報告未回収・重複・権限失敗が疑われた場合、送信や実行を繰り返す前に同じIDの出力と既存履歴を照合し、本人の指示内で直せる一枝だけ修復・読戻しする。実行・成果保存・読戻し・リーダーの実取得・外部利用者の受領・次回巡回の効果を別判定し、未確認を成功扱いしない。**この一文は巡回の既存差分確認への組込みであり、毎回の全件検査・新規Runbook/Task・Work60一般標準化を命じるものではない。**


**最初の問い：「あなたが今回解消した問題は？」** 既存案件ID・元の問題・実際に変更した原本または動く機能・確認結果を短く答える。解消がなければ「実績0件」と書いてよい。数を埋めるための新規タスク・過剰な再検査・未確認の成功宣言はしない。

| 報告区分 | 記載すること（簡潔に） |
| --- | --- |
| **実績（問題の解消・実務の前進）** | 元の不具合への修正、原本の実変更、必要な実行・読戻し。案件ID／現物リンク／何が改善したか。例：誤っているregistry原本の修正は実績。 |
| **報告・報告修正** | 調査、事実確認、証拠回収、状態訂正、既存レビューへの追記。例：既に終了した実行のrun_idを確認し、報告を訂正しただけならこちら。 |
| **未解決・次の一手** | 元の問題として残ったことと、次に可能な修復を一言。確認・記録をしただけで元の不具合をDONEにしない。 |

**集計は「実績 N 件／報告・報告修正 M 件」。** 同じ作業を両方に重複加算しない。対象そのものが誤った案内・記録であった場合、その**正本の修正**は実績だが、別文書での報告追記は報告。実績0件でも罰則・再承認・作業停止はない。調査・確認が実務の前提として必要な巡回なら、それも価値のある報告として残す。

仕事選びに迷ったら、**既に原因・対象が判明し、その場で安全に直せる未解決事項**を、同じ件の再調査や報告だけの更新より先に試す。直せない枝は理由を短く残し、可能な別の実務へ進む。新しい毎回必須のフォーム・ゲート・管理DBは作らない。

## 独立試験の集約フラグと次工程（2026-11-09 本人決定）

**既存親案件のワークシート内だけで扱う。** 元の独立試験依頼文の「対象名＋独立試験」という名前を識別の入口とし、元試験計画の各ステップを基準に結果を集める。試験ごとの新規親・並行台帳・全件PASS承認ゲート・追加定時タスクは作らない。試験数が未確定なら `実施2件／計画総数?` のように不明のまま記す。件数を推測したり埋めるために試験を発行しない。

**同一親IDでの最小記録例：** `親ID | 元の試験名・計画/依頼文URL | 計画ステップ（判明分） | 各ステップのPASS/FAIL/NOT_RUNと証拠・担当/受領 | 集約フラグ | 集約担当の判断・次の1操作`。既存Issue・KB・レビュー欄のうち、その案件がすでに使う記録先へ必要部分だけ残す。独立試験の報告そのものと、正本実装・読戻し・最終成果完成は別の実績とする。

- `TESTING`：元の計画に沿って独立試験を進行中。結果受領前の状態を含む。
- `REVIEW_PENDING`：独立試験の結果が届き、既存リーダーまたは最終成果担当の横断判断待ち。未実施・失敗・残る計画ステップがあってもよく、全件PASSや作業停止を意味しない。
- `DECIDED`：集約担当が証拠と元計画を照合し、**修正して対象試験を再実行／必要な追加検証／最終成果へ実装**のどれを進めるか、対象と担当・次の操作を同じ親IDへ記録済み。これは最終成果の `DONE` を意味しない。

**試験担当の終了規則：** 指定された試験範囲を実行し、証拠と未確認点を既存報告先へ返す。直接返せない場合は、親ID・元の試験名/計画URL・対象ステップ・PASS/FAIL/NOT_RUN・証拠・残件・報告先を含む、**リーダー／最終成果担当への完成済み1通の指示文**を渡して終了する。試験担当自身が次の独立試験を自動生成したり、コピー操作の確認を理由に同じ試験を再配布したりしない。コピーや表示は相手の受領ではない。

**集約担当の判断：** 元の計画と受領済み結果を照合し、欠けた試験数を勝手に確定せず、必要なら影響するステップだけ修正・再試験を依頼する。試験結果が十分なら別の最終成果担当へ実装を委任、または許可済みの実装を自ら進める。元の完成条件を変える必要があるときだけ本人判断へ上げる。これは次工程の道案内であり、既存の承認・安全条件を変更しない。

## Work60｜指示書ファイルの保存から1行配送まで（リーダー用）

**役割を分離する**：リーダー・定期巡回が案件を選び、担当A/B/C向けの**詳細指示書をストレージに保存**する。**Workに渡すのは各担当への1行配送文だけ**で、Work自身には案件の詳細を読ませず、判断・調査・制作・成果回収をさせない。詳しい判断・安全境界・完成条件は受け手の担当チャットが指示書を実取得して扱う。これは既存Work60の「配達係」という設計を具体化する道具で、新規承認ゲート・並列台帳・新しい定期タスクではない。

**2026-11-09 本人決定・現行数量規則：** Work60のA戦略＋B実務は**合計最大100件**を一つの候補キューとして扱い、**A単独・B単独の件数上限は設けない**。Cブログのみ**最大1件（任意）**。したがってA+B 100件とC 1件は別枠。100は上限であって不足分の架空起票・無意味な再送を求めるノルマではない。各案件のJOB_ID＋個別IDを維持し、既送信・実施済み・配送UNKNOWNを分ける。ORCH80/ORCH20は別JOBであり、共通候補を重複計上・再配送しない。Workは選定や実務を行わず、正規GUIで配送のみ行う。

**未完了の取りこぼし防止（2026-11-09本人補足）：** 最大100件は配送可能な候補キューの容量であり最低件数や目標件数ではない。日々の実務で実数が0件、3件、10件になってよく、ゼロでも未完了が消えたと扱わない。リーダー／既存定期巡回は現行Issue #13の未完了親、既存子作業・80_reviews／非公開KB、Work60／ORCH80／ORCH20の既存JOB_ID＋個別IDと送信控え、担当の実受領・成果・未完了1工程を対象限定で差分照合し、**埋もれた未着手・途中停止・報告未回収・担当未確定・期限超過**を発見する。重要なのは件数の増減でなく「未完了を既存IDで保持し、担当・最後の証拠・次の実行可能な一手を残す」こと。既済・実送信済・担当が作業中・他レーン予約済みは二重配送しない。配送UNKNOWNは未配送と決めつけず、既存配送控え・担当報告を確認する仕事として追跡する。新しい実務が独立して必要なときだけ既存親の子作業として指示書を保存・読戻し、A/Bの配分を固定せず1行配送候補にする。すぐ配送できない滞留は既存親・既存レビューへ「理由／現在の担当／次の一手」を残し、次の巡回で差分を拾う。**停滞があっても他の作業を止めず、追加台帳・承認ゲート・親Issue・Automationsは作らない。**

**定期巡回の実行責務と終了判断（2026-11-09 修復）：** 巡回の終点は「実修復1件の報告」や「現在保存済みの指示書を再確認」ではない。本人の最終成果から逆算し、既存Issue親／子、KBレビュー、Work60・ORCH80・ORCH20の個別ID、担当報告の**未完了かつ次の一手が未実行の候補**を差分で拾う。未完了親12件・ORCH80候補80件・KB期限超過37件は同一実務の重なりがあり、足し算を配送数にしない。ただし「担当がいる」「他JOBの候補表にある」「送信UNKNOWN」「実機待ち」は、その親・子を検討対象から消す理由にはならない。**成果物単位**で「既済・他担当が実行中（進行証拠）／配送済・受領済／未着手で実行可能／実機・本人・外部条件待ち／配送UNKNOWNで控え照合要／陳腐化」を対象限定で区別する。

巡回は、自分で安全に修復できるものを修復しながら、**別担当へ渡す実行可能な未着手分を実際の完全指示書＋各1行配送文まで準備**する。「1件修復した」「準備済みA1+B1を確認した」だけで候補抽出を完了と判定しない。最初に既存の実行可能候補を横断してから、未処理の高価値な候補について次の指示書化を続ける。広い一覧を一巡で検査しきれない場合は**今回どの範囲まで評価したか／未評価範囲と次回着手対象**を既存運行票・レビューへ残し、未評価を「適格0件」へ変換しない。巡回の時間・ツール制限や新証拠不足で切り上げる場合も、処理済み件数／未評価／準備済み／送信・受領UNKNOWNを分けて報告する。これは100件のノルマ・全80件の毎回監査・新しい承認ゲートではない。

**出口は2本立て**：①今回安全に直した現物・読戻しと未解消問題、②Workに渡せる完全指示書URL・送信文（準備済み件数、未評価範囲、配送証拠）。WorkのGUI送信・担当実受領・実務完成は別事実。新JOBや未配達と確定できない枝を捏造・再送しないが、**UNKNOWNはその枝の配送判断だけに作用し、他の案件選定・指示書作成・Work用文面の提示を止めない。** 同一JOBの状態不明時でもWork側へ渡す「送信前に現GUI控えを確認し、未配送確定分のみ送信する」指示文は準備できる（Work自身も状態UNKNOWNなら送らない）。必要条件に当たらない場合は空リストと未評価範囲を正直に示して終える。

**生成側（リーダー／定期巡回）の手順：**

1. 現行Issue、既存Work60契約・運行票・最新成果から、**A戦略＋B実務は合計最大100件、Cブログは最大1件**を、既存親IDに紐づく未完了候補として整理する。A/Bの割合は固定しない。既済・重複・配送UNKNOWNを無確認で未配達扱いにせず、準備済みの仕事を優先し追加件数を水増ししない。Cを省略してもA/Bを止めない。旧JOBや既送信を再起動しない。
2. **Workとは別の実行環境**で、各担当向け指示書を既存の適切なDrive/KB格納先に作成・更新する。既存A/B/Cの指示書を利用できれば同一IDを優先し、必要時だけJOB固有のファイルを作る。指示書本文には「JOB_ID／親ID・担当ロール／目的／今回する実作業／既存正本・対象URL／既済除外／権限と禁止範囲／完成・読戻しの目安／既存報告先／残問題の扱い」を揃え、判断・実装・検収は担当AIに依頼する。非公開情報は適正な権限・共有範囲のまま保持する。
3. 保存できた各ファイルを**生成側自身が実取得**し、JOB_ID、対象、本文、直接URLが意図した新規・現行の内容かを対象限定で確かめる。未保存・URL未確認の文書について「保存済みの1行指示」と偽らない。全KBや全SHAの一律事前監査は行わない。
4. 保存済みの**各ファイルに対応する1行配送文を生成**する。**受取先で新規作成されるチャットのタイトルが先頭だけ表示されても判別できるよう、1行の先頭を必ず `A-人間に理解できる短い題名`／`B-人間に理解できる短い題名`／`C-人間に理解できる短い題名` とし、その後ろに `｜AD&C｜JOB_ID=...｜担当：指示書URL...` を置く。** 題名は今回の実作業を具体的に示す短い日本語（目安10〜18文字）とし、単なる「戦略担当」「実務担当」「ブログ担当」だけにしない。例：`A-次の開発優先順位｜AD&C｜JOB_ID=<実ID>｜A戦略担当：<検証済み指示書URL> を実取得し、本文の指示だけを実行・検収し、本文指定の既存先へ報告してください。`（B/Cも同型）。**`AD&C`／JOB_ID／URLを先頭に置かない。** 先頭題名以外は配送用の最低限だけで、長い仕様・調査結果・成果条件・原文をこの1行へ展開しない。実URLは生成側が取得・読戻し済みのものに限る。タイトルの自動生成結果そのものは保証しない（必要なら実チャットURLと表示名を記録する）。
5. Workを起動する人には**短い配送指示＋今回確定した未配送案件ごとの1行配送文だけ**を渡す。**新規チャットへの配送を標準**とし、WorkはChatGPT画面で各案件の新規チャットを作成→対応する1行を1回送信→作成後の実チャットURL・送信成否だけ返して終了。A/B合計100件を一度のWork起動で完走させる義務はなく、実際に配送できた件数と未配送の次回繰越を個別IDで区別する。**送信前に存在しない新規チャットURL、既存担当チャットの特定を要求しない。** 既存チャット送信を本人が明示指定した場合だけその実URLを先に確認する。Workは指示書URLを開かず、Drive/GitHubを開かず、説明文の内容を読まない。ブラウザ実送信不可の枝だけNOT_EXECUTEDとして他を続け、送信したふりをしない。
6. 担当チャットが自分の1行を受領した後、**担当が**ストレージの詳細指示書を取得し、実務・修復・読戻し・既存IDへの結果保存を行う。後続リーダー巡回は「保存／Work送信／担当受領／実行／検収」を別事実として扱い、実績と報告・報告修正を分ける。**Workの配送成功を担当の実務完了と数えない**。

**Workに見せるメッセージの最小形：** 「ChatGPTで今回選定済みの各未配送案件について新しいチャットを1件ずつ作成し、各送信メッセージの冒頭を `A-短い具体的な題名`／`B-短い具体的な題名`／`C-短い具体的な題名` のまま、一行全部を原文どおり1回送信。作成後の実URLと送信可否だけ返して終了。既存担当チャットは探さず、作成前のURLは要求しない。リンクは開かず、案件の実行・調査・確認・保存は一切しない。」＋検証済みの各1行のみ。元ファイルの本文はWorkの起動メッセージに貼らない。

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

> **設計理念の解説・採用理由（実行手順ではない）**。AD&Cの公開理念は[README](../../README.md)が正本。本節の示唆を理由に、既に承認された作業を停止、専門Playbookの固定工程を変更、追加の承認や検査を要求しない。通常の実行条件は共通・専門Playbookの具体的操作欄に置く。

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

## One-shot worker handoff: execute, do not paraphrase (β)

For a handoff through a scheduled one-time task, record a concrete **parent task ID, origin request timestamp (with timezone), origin chat reference if accessible, canonical KB task/Context reference, already-approved scope, completion evidence, and the existing KB result destination** in the worker's actual prompt. The worker must **attempt to read the origin conversation around that instruction timestamp when supported**, reconcile it with the canonical KB handoff, then **perform the authorized work** and read back the saved result. Merely summarizing the chat, creating a Draft, or handing the instruction back to the user is NOT execution. If chat access is unavailable, mark origin-chat NOT_RUN (do not invent the dialogue) and continue independently safe tasks when the KB contains sufficient instructions and authorization. If essential details are missing, stop only the affected step and record its exact blocker. Verify child execution, KB write/readback, parent reception, and worker self-disable separately; never claim a disabled task was deleted or that a new child chat is automatically attached to its parent. Preserve approval, recovery, conflict and privacy boundaries; do not create a second tracker.

## Entry-first creation and acceptance

**Q3局所移管済み**：[専門正本](../../templates/PLAYBOOK_TEMPLATE.md) の末尾Designer’s Noteに当時の原文を保全。自然文から実体発見・実行までの作成設計はテンプレート／開発プラクティスへ移管。リーダーは案件採否と進行の検収に専念する。

## Human-first Playbook customization and upstream proposal (2026-11-03; user-approved design, pilot only)

**Q3局所移管済み**：[専門正本](../../templates/PLAYBOOK_TEMPLATE.md) の末尾Designer’s Noteに当時の原文を保全。人間編集と機械定義の整合・上流への提案分離はテンプレートと開発プラクティスが担当。リーダーの本人による採否・公開判断は変えない。

## Markdown-embedded Python pilot (bounded single-Playbook use adopted; broader rollout not adopted)

**Q3局所移管済み**：[専門正本](../../skills/markdown-auto-pilot/README.md) の末尾Designer’s Noteに当時の原文を保全。単一Playbook AUTO試験・人間本文保護・バックアップ/復旧の説明は既存runner付近へ原文保全。現行ワークシート末尾のAUTO/Python固定入力は維持する。

## Completion-through-repair rule (2026-11-02, user-approved)

When asked to **修正・検証する**, do not stop at inspecting, proposing, drafting, opening a PR, or recording NOT_RUN. Attempt every remaining in-scope, authorized, safe step **in this execution**: resolve the correct canonical document and registry entry, obtain pre-edit bytes/ID/version and recovery copy, diagnose write-interface and conflict failures, modify the original canonical file (same ID when required), update dependent links/indexes and required Git/main, then re-fetch each destination and compare intended content. A failed first attempt is a reason for targeted diagnosis and one safe retry after checking whether the first write took effect, not an automatic end of work. Seek an equivalent supported write mechanism when the initially selected connector cannot complete the operation; avoid duplicate or replacement files presented as original changes.

**Exit decision is based on the user's outcome, not on the amount of work performed.** Only report completed when every required canonical and downstream acceptance check is PASS. A file being fetched, a draft being made, or a blocker being described is not the requested completion. If—and only if—a concrete permission, safety, irreversibility, exhausted technical route, or verified external-dependency boundary actually prevents completion, record the exact parent/step, observed cause, attempted recovery, and specific unblock action in the existing tracker, plus FAIL/NOT_RUN; do not conceal, downgrade, or forget the unfinished parent. Routine Git changes/merge are within the user-approved scope when needed for the intended result, but this does not authorize leaking private KB into public GitHub, deletion, privilege changes or unreviewed production effects.

## One-question lead-in requirement (2026-11-05; minimal clarification)

**Q3局所移管済み**：[専門正本](../../skills/communication-navigation/SKILL.md) の末尾Designer’s Noteに当時の原文を保全。本人判断が実際に必要な未決1件だけ提示。専門UIの原文・検収条件はリンク先の局所Designer’s Noteと現行実行本文を参照する。

## DESIGNER'S NOTE — 人間が迷わず選べる一問一答UI

本文の設計原文は[標準コミュニケーションPlaybookの末尾Designer’s Note](../../skills/communication-navigation/SKILL.md)へ移設（通常実行では読込不要）。リーダー固有の一問一答の実行仕様は下記T007節を正本として保持。

### DESIGNER'S NOTE 追補｜「作り込みは濃く、運用は軽く」

設計原文は[Playbook作成・更新テンプレート末尾Designer’s Note](../../templates/PLAYBOOK_TEMPLATE.md)へ移設。通常の巡回や実行では全文参照不要。

### DESIGNER'S NOTE 追補｜AIと人間の二重インターフェース、進歩の土台

AIと人間の二重インターフェースの原文・採用理由は[Playbook作成・更新テンプレート末尾Designer’s Note](../../templates/PLAYBOOK_TEMPLATE.md)へ移設。理念の短い入口は[README](../../README.md)。

### DESIGNER'S NOTE 追補｜基本動作の検索ナビと次の一手

次の一手・情報取得・ボタンに関する設計原文は[標準コミュニケーションPlaybook末尾Designer’s Note](../../skills/communication-navigation/SKILL.md)へ移設。通常の動作契約は同Playbook本文、リーダー固有の補助UIはT007節を使う。

## T007 — actionable one-question UI contract (2026-11-05; approved local implementation)

**Q3局所移管済み**：[専門正本](../../skills/communication-navigation/SKILL.md) の末尾Designer’s Noteに当時の原文を保全。実ボタンの具体操作・番号付き代替・状態区別の専門正本は標準コミュニケーション。リーダーは本人判断の対象・実権限・報告先のみ確定する。

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

**Q3局所移管済み**：[専門正本](../../skills/communication-navigation/SKILL.md) の末尾Designer’s Noteに当時の原文を保全。コピー可能な指示文・独立試験名の共通表示規則はリンク先を参照。リーダーは元案件のID・成果物・報告先を維持する。

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

**Q3局所移管済み**：[専門正本](../../skills/markdown-auto-pilot/README.md) の末尾Designer’s Noteに当時の原文を保全。限定的なrunner検証の手順・過去採否はtool近傍へ原文保全。全Playbook一括適用と異なり、runner本体/元のAUTOマーカー・復旧条件は変更しない。

## Chat handoff / context compression (shared user-adopted trial; 2026-11-03)

**Q3局所移管済み**：[チャット引継ぎPlaybook](../../skills/chat-handoff/SKILL.md) に引継ぎ手順原文、[runner説明](../../skills/markdown-auto-pilot/README.md) に人間編集検出原文を保全。リーダーは案件の受領・再開・正本照合を引き続き担当する。

<!-- ADNC:DESIGNER_NOTE:HUMAN:BEGIN
このリーダーワークシート固有の設計メモ。**通常の巡回・実務では読込不要**。仕様改訂・判断の衝突・不具合調査で必要なら参照する。内容はWHY／経緯であり実行命令・承認・停止ゲートではない。
- 理由：作り込みは濃く運用は軽く。人間に伝わる本文を正本とし、AIに必要な固定動作は既存ツールへ移す。全欄検査や3巡・全SHA同期・毎回のDesigner’s Note取得を要求しない。
- 設計原文の現在地：次の一手・UIは[標準コミュニケーション](../../skills/communication-navigation/SKILL.md)の末尾、道具化・二重インターフェースは[Playbookテンプレート](../../templates/PLAYBOOK_TEMPLATE.md)の末尾コメントへ局所移設。歴史的な原本はGit版履歴で保持。必要な対象だけ開き、未採用仮説と確定判断を区別する。
- 固定境界：人間が変更した自然言語の目的・手順を機械生成で戻さない。末尾のAUTOは限定的な定型工程で、別AIの自動実行・全Playbook展開・動画／サムネイルの機械的一括変更を意味しない。
- Python側の詳細は直後のAI appendix末尾にある # ADNC:DESIGNER_NOTE:PYTHON コメントを参照。非公開情報を公開側へ出さない。
ADNC:DESIGNER_NOTE:HUMAN:END -->

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

# ADNC:DESIGNER_NOTE:PYTHON:BEGIN
# 通常の実務では読込不要。改訂・不具合調査のときだけ参照。
# このSTEPSはrunner.pyがast.literal_evalで読んでAUTO:BEGIN/END間だけ再生成する固定入力。
# Markdown内のPythonを自由実行せず、Pythonコメントは生成対象外。人間本文は優先正本。
# 人間本文の変更は意味をレビューしてからSTEPSと整合する。自動推測で本文・既存採用仕様を上書きしない。
# ADNC:DESIGNER_NOTE:PYTHON:END
```
