# AD&C｜秘書・PJ・定例のHTMLレポート制作Playbook v0.1.0

<!-- ADNC-HTML-REPORT-20261120 -->
**適用状態**：本人正式採用（単一HTMLの人間向けVIEW/SNAPSHOTと共通オフラインPython生成ツール）。**公開されている手順・ツールの採用**と、組織内での受入・配備・利用承認は別。組織が定めた利用権限と保存先が優先。既存の秘書専用UI／PJの正本／定例の実行結果は変更しない。

> AD&Cは「完成形のない仕組みで、完成する仕事を増やす」。HTMLを新しい正本にせず、読みやすく、戻れる形で渡す。

改訂担当だけの参照（通常利用では追加読込み不要）：

```text
EDIT_REF_PHILOSOPHY=https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/README.md
EDIT_REF_DESIGNER_NOTE=https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/templates/DESIGNER_NOTE.md
EDIT_REF_UPDATE_PLAYBOOK=https://github.com/Yosio-DMZ-C/AD-C-Shared-Knowledge/blob/main/docs/DEVELOPMENT_WORKFLOW_PRACTICES.md
```

- **カスタム優先**：社内では当該組織の正式情報分類・表示・保存・承認・配布規則、個人秘書では本人の採用済み秘書Playbookを先に適用。取得不能な非公開ルールを推測しない。
- `AI_NAV_PY_PATH=NONE`（このPythonはナビではなく**レポート生成器**）。`REPORT_RENDER_PY_PATH=./render_report.py`。
- **発動条件**：「秘書の今日の報告をHTMLで」「このPJをカード化」「定例業務の週報・巡回状況をHTMLで」。専門固定出力やユーザー明示の別媒体がある場合はそちらを優先する。
- **生成対象**：`kind=secretary`（予定・判断待ち・引継ぎ）、`kind=project`（既存PJ_ID/TASK_ID・優先度・実績）、`kind=routine`（既存ROUTINE_ID/EXECUTION_ID・対象期間・例外）。PJと定例はそれぞれの管理正本・分母を保ち、単純に混ぜない。

## 1. 観測と入力

1. 今回の権限で閲覧できる**既存の正本**から、対象期間・ID・現行状態・根拠・次の一手だけを取得。秘書は当日の日次記録と採用済み秘書Playbook、PJは採用された1つのWBSと既存タスク管理先、定例は既存の定義正本と**各回の実行記録**を使う。チャット内の未検証要約から最新状態を補完しない。
2. 個人・社内のURL、職員名、進捗などを**公開GitHubや第三者プレビュー、外部AIへ自動転送しない**。社内情報は社内承認済みのツールと保存先だけで処理する。外部公開用サンプルには架空データだけを使う。
3. 入力はUTF-8 JSON。必須：`kind`、`title`、`snapshot_date`、`source_checked_at`、`source_label`。任意：`source_url`（HTTPSのみ）、`visibility`（既定private）、`summary`、`handoff`、`items`（配列）。各itemは`title`必須、`id / priority(P0,P1,P2,OTHER) / period（定例の対象期間） / due（PJの期限） / status / owner / next_action / evidence / source_url`を任意指定。既存の元IDを入れ、新IDを採番しない。欠落は未確認と記す。
4. **分母の区別**：PJ＝対象のTASK_ID、定例＝予定された実行回ID。欠損・遅延・UNKNOWNとDONEを混同しない。進捗率を資料が提供していなければ推測計算しない。

## 2. 作成（Pythonが使える場合）

```shell
python render_report.py example_synthetic.json report.html
```

- `render_report.py`はPython標準ライブラリのみ。**外部CDN／外部フォント／外部画像／通信API不要**で、HTML・CSSとフィルタ・全文コピー用JavaScriptを一つのファイルに生成する。外部の正本の取得、ログイン、権限付与、送信、共有、実行スケジュール、本人や職員への査定、帳票の編集は行わない。
- 入力JSONは会社の許可された作業環境・フォルダに置く。元情報や実URLを**この公開リポジトリに書き戻さない**。出力HTMLも非公開の既存保存場所へ保存。出力先のアクセス権は保存先システム側で保証する（HTML内のPRIVATE表示はアクセス制御ではない）。
- Pythonが禁止／利用不能なら、同じデータ項目と表示条件で権限内のHTML制作を行い、未検証機能をPASSにしない。会社にPython導入やマクロ実行を強制しない。

## 3. 人間へ渡す閲覧リンク

- **人間が読む入口＝実際にレンダリングされるURL**。Google Driveの`/file/d/.../view`やGitHub `blob/raw`はまず**ファイル保存・コード閲覧リンク**であり、描画済みHTMLの直リンクとみなさない。
- 公開許可されたものは公式静的サイト、**非公開**は既存の認証付き閲覧環境（許可された社内Webサーバー／SharePointアプリ等、または個人のChatGPT非公開PageにHTML可視化として埋込み）を選ぶ。ChatGPT専用の可視化リンクは**社内CopilotやSharePointが同じ方式を提供する証拠ではない**。権限のない第三者や会社外サービスでのプレビューをしない。
- ブラウザーで描画・フィルター・コピーが実際に動くかは利用画面で別々に実測。レンダリング確認未実施なら `NOT_RUN` と記し、**HTMLファイル＋ローカルで開く手順**を代替として渡す。閲覧リンク、原本URL、版日付を分けて提示する。
- HTMLは**閲覧専用のスナップショット**。外部リンクをクリックした先で編集できても、HTML自身の保存や組織KBの更新を意味しない。コピー＝送信でもない。

## 4. 最小検収と再開

1. 元のID・件数・優先度・状態・時点・出典をHTMLソースと比較。日本語・リンク・HTMLエスケープ・不正URL除外を確認。
2. 使用できるブラウザーでPC／スマホ幅のカード表示、P0〜P2フィルター、全文確認と全文コピー／代替を操作確認。ツール構文テストと本人が実際に開いた操作を同一PASSにしない。
3. 保存先からバイト一致・読戻し。元正本は不変、閲覧権限は変更なし。非公開Pageへ埋込む場合もHTMLの原本取得と公開範囲を別に確認する。
4. 結果を既存の案件KB・日次記録・定例結果へ `生成PASS / 保存読戻しPASS / 描画PASS|NOT_RUN / 操作PASS|NOT_RUN / 採用状態 / 次の一手` として短く返す。独立の新規台帳は作らない。

## 5. 配布・社内移植時の固定境界

- 公開の**汎用Playbookとコード**は、社内の`99_inbox/`等に取り込む**候補**。組織の承認なく`approved`へ昇格させず、社内の4列List／registry／playbooks.tsvを壊さない。法人・個人の実データを付属せず、サンプルは架空データのみ。
- 社内のPJ定例管理は[組織業務計画Playbook](../project-management/SKILL.md)を優先。「正式採用」の対象は**人間用表示・制作道具**であり、組織の会議設計・監督・人事評価を勝手に変更する権限ではない。
- 運用でPython禁止、Content Security Policy（CSP）やSharePointスクリプト制限がある場合は当該枝だけ`NOT_RUN`。**セキュリティ制限を回避しない**。内容静的閲覧は継続可能なら継続する。

**検収の初期実績（2026-11-20）**：架空入力を使ったPython生成・HTMLエスケープ・HTTPS判定・3種のkind出力はローカル試験PASS。実社内環境の受入・SharePointでのHTML直接表示・ブラウザーの本人押下・別AI利用はNOT_RUN。秘書/PJの既存11月20日版HTMLは**デザイン参考の現物**であり、本Pythonで元現物が生成された証拠ではない。