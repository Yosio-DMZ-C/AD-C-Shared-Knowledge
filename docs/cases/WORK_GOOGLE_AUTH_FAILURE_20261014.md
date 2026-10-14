# 事例：WorkクラウドブラウザからGoogle認証へ進めなかった

- 案件ID：`external-op-googleauth-20261014`
- 日付：2026-10-14
- 状態：Draft／調査記録。原因未確定、再現検証NOT_RUN。
- 由来：利用者が提出した開発調査レポート。以下の実施結果は**提供記録**であり、本ファイル作成時に再試験していない。
- 公開用要約のため対象ファイルID、個別実行ID、認証情報は掲載しない。

## 目的・結果

Google Driveの対象ファイルを「リンクを知っている全員・閲覧者」に変更し、外部AIからURL取得可能にする。**共有変更は未完了**。

## 観測（提供記録）

- 接続済みDriveツールではメタデータ読取に成功し、共有操作可能フラグがあったが、当時の利用可能な共有アクションでは`type=anyone`相当の共有先を指定できなかった。
- WorkクラウドブラウザはGoogleログインへの遷移後、HTTP 502と`[Errno 111] Connection refused`を表示。2実行・合計3ブラウザアクセス／再読込で同様の結果。
- ブラウザから共有設定画面に到達せず、提供記録では権限は未変更。
- 障害を生成したホスト、ポート、コンポーネント、Work消費量は不明。

## 判断と代替

- **事実と推論を分離**：502の発行元やConnection refusedの宛先は未特定。「GoogleがAIを拒否した」「OpenAIの障害」とは断定できない。
- **能力≠権限**：ファイルの共有権限があっても、接続ツールに指定した公開先を扱う引数があるとは限らない。
- **認証経路を分離**：コネクタの認可成功はWorkブラウザのログイン成功を保証しない。
- **停止**：同じ条件で追加試行しても新しい観測が見込めないため、Work再実行を止める。
- **代替**：単発の共有変更は本人の通常Google Drive UIで、対象・公開範囲を確認して実施。変更後は未認証での閲覧を検証する。繰返し必要な場合だけ適切なOAuth権限を持つ独立API実装を検討する。

## 予防策を突破した失敗か

**適用不明**。当時の標準予防策の適用ログがないため「最低限の予防策を実施したが突破された件数」に算入しない。1事象からの2実行・3アクセスを3独立インシデントとして数えない。

## 候補と採否（リーダーレビュー案）

- 採用：ツールの機能と利用者の権限を別確認／コネクタとブラウザの認証分離／Work→人間切替／症状ベース索引。
- 既存へ統合：層別診断、費用対効果、変更前後照合、使用量記録。
- 修正採用：同一条件の安全な自動再試行は原則最大1回。追加は情報利得が見込める別試験に限る。「累計3アクセス」を普遍閾値にはしない。
- 条件付き：Private原本と公開用コピーの分離は公開作業に適用。

## 参考一次資料（調査報告に記載されたURL）

- [OpenAI Cloud browser](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
- [OpenAI Google Drive app](https://help.openai.com/en/articles/10929079-google-drive-app-and-setup-in-chatgpt)
- [Google Drive API permissions.create](https://developers.google.com/workspace/drive/api/reference/rest/v3/permissions/create)
- [Google Drive共有](https://developers.google.com/workspace/drive/api/guides/manage-sharing)
- [RFC 9110 502](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.6.3)
- [Google Drive APIエラー](https://developers.google.com/workspace/drive/api/guides/handle-errors)

## 品質ゲート

- PASS：提出レポートと本要約の整合、事実／推論／未検証の区別、公開向け個別ファイルIDの省略。
- NOT_RUN：Work再実行、Google Drive実際の権限変更、原因の実機確定、独立レビュー、外部AIからの取得確認。
- 【未検証】出典ページの本日付での再照合は未実施。提出レポートの調査結果を要約した。
- 【人間判断】正式Active化・共通ルール昇格は別途審査。
