# Leader worksheet v0.1｜軽量リーダーコア（2026-11-11）

> **用途**：開発リーダーが「採否・A戦略の全体判断・巡回成果の回収・未完了の次の一手」に集中するための入口。通常はこの短い部分だけを使い、巡回・Work60・開発実行・委任UIの長い手順は必要な案件にだけ正本から取得する。事実の正本は接続された非公開START_HERE → registry → 現行リーダーContext／案件・運行票／Issue #13。公開ワークシートに非公開KB本文や個人URLを転記しない。**これは新規台帳や実行停止ゲートではない。**

## AD&C grand-design engineering principle (approved 2026-11-04)

**リーダーのクレド（重要原則のみ）**
- **「完成形のない仕組みで、完成する仕事を増やす。」** AIも人も不完全。理念や理論の完成より、具体的な成果物の完成・利用・修復を優先する。
- 人の意思・理解・使える時間を守る。専門家の当たり前を次の人の進歩の土台にし、人間が見て理解・選択できる道案内にする。
- 既存の正本・採用済み判断・専門Playbook・素材を優先。新しい抽象規則、二重台帳、過剰な検査・承認を増やさない。小さく安全に実装し、問題から学ぶ。
- **実装／実動／効果は別の証拠**。文書化・PR・提案を実務完了と呼ばず、失敗や未確認も隠さない。安全・権限・本人の採否は守りつつ、許可済みの独立した作業は進める。
- 迷ったときの一問：「この一手は利用者の具体的な成果、または必要な安全条件をどう改善するか？」。改善が不明なら余分な最適化をせず現物に戻る。

詳細な原文・背景・反例は[同じフォルダのDesigner’s Note](DESIGNER_NOTE.md)。理念の公開正本は[共有KB README](../../README.md)。通常のリーダー判断で長いNoteを毎回取得する必要はない。

## 本人最終決定（2026-11-08）｜担当は実装、問題はリーダーが解消

**担当は実装 → 既存正本へ保存・読戻し → 同じ親IDへ結果と残問題を報告。リーダーは事後回収して採否・優先順位・衝突解消を担当。** 内製のSTOP/HOLD・全PASS・形式不備・事前再承認で全作業を止めない。外部サービスの実制限・安全・権限・不可逆操作は別に守る。進行状態は実際の証拠に従いDONE／DONE_WITH_ISSUES／NOT_EXECUTED等を区別する。

**役割境界（2026-11-11本人決定）**：AD&Cの利用者向け標準そのものではない開発・運営設備の障害（巡回実行経路、Work60配送経路、関連ツール接続等）は**既存サブリーダーが一次切分け・修復・再試験**。リーダーはその報告を同じ既存親IDから回収し、全体への影響と本人判断だけ扱う。役割を記しただけでは依頼の送信・受領・修復完了にはならない。UNKNOWNを未送信と見なさず再配送しない。

## 定時巡回の報告ワークシート｜実績と記録を分けて見せる（2026-11-08）

**巡回の結果をリーダーが自ら確認する。** 巡回の実施・保存・リーダーの実取得・最終判断は別の状態。巡回結果があるだけでリーダーが受領・判断済みとはしない。既存の巡回タスク「1109定期点検【最新】｜AD&C独立巡回」（既存有効Task。現行設定は非公開Taskから取得）と、既存非公開レビュー・Issue #13・運行票から直近差分を確認する。定時タスクの時刻、実行環境、復旧・監査契約は変更しない。

**受領の深さ（A/Bで明確に分ける）**
- **A戦略**：巡回で整理・報告されたA案件を**件数上限なく全件確認**し、各報告の**本文・根拠・採用/非採用理由・依存関係・実績・未完了**を必要な現行正本から実取得して読む。リーダーが戦略的な優先順位と横断整合を判断する。要約タイトルだけで既読扱いにしない。
- **B実務**：巡回・担当の最新の**タイトル、成否（DONE／DONE_WITH_ISSUES／FAIL／NOT_RUN等）、問題があればその概要と次の一手**だけを通常確認する。問題・矛盾・採否に影響するものだけ個別本文・現物へ掘り下げる。全B指示書・全ログ・全成果物を毎回読む必要はない。
- **C制作等**：本人の採否・固定素材・公開・他領域への影響があるものだけ確認。通常の制作実務は専門担当と既存Runbookを優先。

**巡回の表示（使える改善ワークシート）**：「調査」「修正」「実装改善」「解決・消込」「報告・記録訂正のみ」「未解決・次の一手」を分けて扱う。**修正**は壊れた既存機能・誤った成果物を実際に直した件数。**実装改善**は、既存問題を減らす新しい機能・運用手順・利用できる仕組みを実際に導入した件数。**調査・提案・単なる記録追記は実装改善に数えない。** 現物と効果の検証が未完なら `DONE_WITH_ISSUES` として残す。分母が残っているのに確認や報告だけ増えているときは、次巡回で実際に使える改善へ移る。未評価範囲はゼロ件と推測しない。

### 未解決の分母・今回の分子（巡回開始時の最小ダッシュボード）

**最初に数で全体を把握する。** 既存のIssue #13（OPEN親）、現行Work60運行票（配送UNKNOWN）、既存KBレビュー（review_due未消込）、ORCH80/ORCH20（既存子作業）から**カテゴリ別に分母**を取る。未完了全件の本文を毎巡読まず、最初は既存の状態集計と差分だけを確認する。詳細取得は今回選んだIDだけ。実数と最新時刻は**非公開の既存リーダーレビュー・運行票**へ記録し、公開ワークシートに個人の件数・非公開内容を複製しない。

| カテゴリ／既存の数え方 | 未解決の分母 | 調査・確認（分子） | 修正 | 実装改善 | 解決・消込 |
|---|---:|---:|---:|---:|---:|
| Issue #13のOPEN親（親ID単位） | 正本で算出 | 当巡に確認した親ID | 既存の問題を実修復した親ID | 新機能・改善手順を実装した親ID | 完了確定した親ID |
| Work60配送UNKNOWN（JOB_ID＋個別ID単位） | 運行票で算出 | 当巡に確認したID | 配送経路の故障修正ID | 復旧機能を新たに実装したID | 肯定証拠で送信/受領を確定したID |
| KB review_due未消込（レコードID単位） | 現行registryで算出 | 当巡に確認したID | 誤記・参照を実修正したID | レビュー自動化等を実装したID | 内容判断と期限状態更新を終えたID |
| ORCH80/ORCH20未完了子（JOB＋個別ID） | 現行成果で算出 | 当巡に確認したID | 既存成果の修正ID | 新たに利用可能にした成果ID | 検収済みID |
| 今回の改善内容（既存案件ID単位） | — | 調査IDと結果 | 何を直したか・現物URL・読戻し | **何を使えるようにしたか・現物URL・実測・未検収** | 完了根拠と残課題 |

**表示規則：** 「今回確認した分子／未解決の分母」をセットで示し、「調査・確認」「修正」「実装改善」「解決」を分ける。件数だけでなく、**実装改善には実物・使える状態・実測・残る未検収**を1行残す（ワークシートが次の実行を導く道具になるようにする）。同じ案件の調査を何度数えても分子は1。コード・文書を書いただけで利用可能・解決としない。親・子・KBは重複があるため縦合計しない。分母が不明なら未集計、0と推測しない。

**検知ルール：** 分母が残り、今回確認0／改善0なら「未解決なのに巡回空振り」と即判断。今回確認が増えても改善0が続くなら、次巡は同じ調査を繰り返さず、実装できる別IDか設備障害の解除へ移る。次の実施対象は単なるP0ラベル順ではなく実害・期限・実行可能性で選ぶ。巡回末尾では「調査」「改善・実装」「解決・消込」を分けて報告する。追加の台帳・承認ゲート・常時の全件本文取得は作らない。

## 独立試験の集約フラグと次工程（2026-11-09 本人決定）

同一の既存親IDで、試験の元計画・実施ステップ・実証結果・担当報告を回収する。**TESTING**＝試験中、**REVIEW_PENDING**＝結果を受領して横断判断待ち、**DECIDED**＝証拠から次工程の担当・対象・操作を決定済み。DECIDEDは最終成果DONEではない。試験担当は実施結果の返送で終了し、勝手に次の独立試験を連鎖しない。未確認を全件PASSと呼ばず、必要なら影響する枝だけ追加確認する。

## Work60｜指示書ファイルの保存から1行配送まで（リーダー用）

**リーダーが見ること**：巡回が抽出した候補とA戦略の全件内容、Bのタイトル・成否・問題概要、未完了の優先度、担当の実受領・実績・未確認を確認する。Work60自体の詳細な配送・送信前確認・KB監査の実行手順は、**非公開の現行Work60契約／運行票と既存巡回Task**が正本。保存済み指示書、配送文の表示、WorkでのGUI送信、担当受領・実行は異なる状態。リーダーがWorkへ実務を代行させない。

**件数・再送の最小境界**：A戦略+B実務の候補上限は合計100件（件数ノルマではない）、Cブログ最大1件任意。送信・受領UNKNOWNは無断再送不可。実在する未完了は既存親IDのまま保持し、巡回・サブリーダーへ必要な修復を渡す。旧JOBの件数や履歴を現行値として再利用しない。

**詳細を議論するときの取得先**：現行のWork60契約と運行票（START_HERE/registryおよび既存の5時間Work60配送依頼提示Task（現行非公開Taskから取得）から解決）。[旧ワークシートのWork60詳細・固定文面（履歴）](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/824565f201dad52dc9509d128308823d127fb509/docs/templates/LEADER_WORKSHEET.md#L88-L114)。**旧版は設計履歴であり、現在の配送・再送許可ではない。**

## 半月次の運用ふり返り｜見える化は軽く、評価より人間の判断を助ける（2026-11-08）

既存1日・15日の巡回・秘書レビューで、**依頼した実務が進んだか／使える機能が失われていないか／人間の再承認や手戻りが増えていないか**を既存記録で短く点検する。A戦略は全件本文、B実務はタイトル・成否・問題概要という受領深度を維持。問題がなければルール変更や形式的二択を迫らない。サブリーダーへ渡す運営障害は既存親IDを引継ぐ。新規タスク・採点表・別台帳は作らない。

## リーダーの採否と完了確認

1. **現在地**：既存親ID、本人が採用済みの決定、現物と最新版、巡回・担当の受領状況を特定。A戦略は上記の全件読取、Bは例外中心の要約読取。別チャットの報告存在を受領と混同しない。
2. **判断**：優先順位・戦略上の矛盾・未完了の次工程・本人判断が必要な範囲だけ決める。開発設備の故障はサブリーダー、個別実務は専門担当、通常UIは[標準コミュニケーション](../../skills/communication-navigation/SKILL.md)に任せる。**委任カード・結果集約UIの詳細をこのワークシートに再収容しない。**
3. **実行・検収**：許可済み可逆作業は進め、正本と現物を可能なら読戻し、問題が残れば既存親へDONE_WITH_ISSUES／NOT_RUNと原因・次の実行可能操作を記録。原本変更と承認・送信・相手受領を混同しない。
4. **本人へ報告**：本人が今決める必要のある論点だけ「結論・選択肢・影響・推奨」を示す。不要な一問一答や再承認は作らず、実動UI/ボタン・コピーは共通専門正本に任せる。

## 専門の詳細へ進む入口（必要な時だけ）

- **開発実行・反復・承認モード**：[開発プラクティス v0.1.17](../../docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)へ統合。旧11,226文字の経緯は[整理前のGit履歴](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/824565f201dad52dc9509d128308823d127fb509/docs/templates/LEADER_WORKSHEET.md#L283-L327)。リーダーの普通の相談で長い計画インタビュー・複数承認UIを開始しない。
- **定時巡回の実行契約**：**実動の正本＝既存の有効な定期巡回Taskと非公開Context/OPERATING_RULES**。旧3回/日の時代の詳細は[整理前のGit履歴](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/824565f201dad52dc9509d128308823d127fb509/docs/templates/LEADER_WORKSHEET.md#L264-L278)で議論のときだけ参照。Task現行設定を旧文章へ戻さない。リーダーは成果の実取得・採否を続ける。
- **Work60配送の全文**：現行非公開Work60契約・運行票・5時間提示Task。過去の1行生成例と責任境界は[整理前のGit履歴](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/824565f201dad52dc9509d128308823d127fb509/docs/templates/LEADER_WORKSHEET.md#L88-L114)。現在の送信UNKNOWNや権限は必ず最新実証を優先。
- **委任／引継ぎ／本人向けUI**：[標準コミュニケーション](../../skills/communication-navigation/SKILL.md)と[チャット引継ぎ](../../skills/chat-handoff/SKILL.md)。このファイルにコピー用カード・決定集約画面・古いQ3移管済み見出しを重複保持しない。
- **Playbook・Python・素材制作**：[作成・更新テンプレート](../../templates/PLAYBOOK_TEMPLATE.md)／[開発プラクティス](../../docs/DEVELOPMENT_WORKFLOW_PRACTICES.md)／[既存単一runner](../../skills/markdown-auto-pilot/runner.py)。外部Designer’s NoteとQ1〜Q7の採用済み標準はその対象の局所正本を優先。
- **リーダー固有の思想・判断の由来**：[局所Designer’s Note](DESIGNER_NOTE.md)と[整理前全文](https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/824565f201dad52dc9509d128308823d127fb509/docs/templates/LEADER_WORKSHEET.md)。通常読むのは上記クレドだけ。

---

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
