# 開発現場の「ハマりどころ」日英記事調査（2026-10-13）

- 状態：Draft / 調査記録（正式Activeではない）
- 目的：仕様書だけでは気づきにくい実務上の予防策を抽出し、開発調査KBの候補にする。
- 調査方法：日本語のQiita/Zenn、英語のDEV Community/AWS Builders' Library、Microsoft Learnをキーワード検索。網羅調査ではなく初回探索。
- 留意：個人記事の失敗談は著者環境での事例。一般性・因果関係・現行版への適用を無条件に保証しない。

## 検索語

- 日本語：「開発 ハマりどころ 実体験」「プログラミング やらかし集」「環境依存 罠 原因 対策」「本番障害 振り返り」「自動化 失敗談」「文字化け バッチ PowerShell」
- 英語：「software engineering gotchas」「lessons learned the hard way」「production incident postmortem」「environment-specific pitfalls」「automation failure lessons learned」「subtle bugs root cause analysis」

## 有用記事と抽出事項

| 記事 | 記事が扱う問題 | KB化する予防策 | 根拠区分 |
|---|---|---|---|
| [Windows + AIコーディングエージェントで踏んだ罠](https://zenn.dev/mukuil_blog/articles/9a048ea2e8dec4) | PowerShell 5.1のBOMなしUTF-8誤読など | OS/シェル/エディタ/実行環境ごとに文字コードを確認 | 個人実例 |
| [Claude CodeでShift_JIS環境と格闘](https://qiita.com/DIKE_zozo/items/ca9eca9af506d5c09381) | 既存Shift_JIS資産とUTF-8前提ツールの不一致 | 既存ファイルの文字コードを維持し、差分と日本語を検査 | 個人実例 |
| [Claude Code 総まとめ：ハマりどころ](https://zenn.dev/mika_and_coco/articles/claude-code-diary-15-summary) | PATHの反映やセッション開始時設定 | 設定後は反映タイミング・再起動/再ログイン条件を確認 | 個人実例 |
| [macOS入力ソース自動切替](https://zenn.dev/deepzz/articles/fa0a2392493254) | イベント多重発火、手動操作との競合 | デバウンス、現在状態の照会、手動操作の優先 | 個人実例 |
| [AIエージェントを無人で働かせたら最後の1行で止まった](https://zenn.dev/hullspark/articles/570e42ead0c0c1) | 無人自動化の終了段階での停止 | 最終確認、認証/人間承認が必要な箇所の事前分離 | 個人実例 |
| [Most Production Bugs Don’t Live in Your Code](https://dev.to/xcodedadx0/most-production-bugs-dont-live-in-your-code-they-live-between-systems-2ei2) | システム境界で状態が食い違う | 各境界の入力/出力/保存結果を照合 | 技術者の経験談 |
| [The Hardest Bugs I've Worked On Were Rarely Syntax Problems](https://dev.to/hakeem/the-hardest-bugs-ive-worked-on-were-rarely-syntax-problems-h9o) | 正常な部品同士の処理順序による不具合 | 単体テストに加え、順序・非同期・再送を検査 | 技術者の経験談 |
| [10 Software Spec Mistakes That Cause Production Incidents](https://dev.to/speccoding/10-software-spec-mistakes-that-cause-production-incidents-with-fixes-34lk) | 検証できない受入条件 | 成功条件を観測可能な結果で記述 | 技術者の経験談 |
| [AWS Builders' Library: Timeouts, Retries, and Backoff With Jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) | リトライによる負荷増幅 | 有限リトライ、バックオフ、ジッター、再試行予算 | 企業技術資料 |
| [AWS Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) | 再送による重複作成 | 冪等性キー・実保存状態照会 | 企業技術資料 |
| [Microsoft Learn: about_Character_Encoding](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-5.1) | Windows PowerShell 5.1と7系で異なるエンコーディング | 実行バージョン、BOM、出力コマンド別既定値を確認 | 公式仕様 |

## 優先採用候補（重複を統合）

1. **文字コードの暗黙変換**：.bat/PowerShell 5.1/PowerShell 7/既存Shift_JISを区別。日本語入りの最小テストを必須化。
2. **設定反映のタイミング**：PATH・サービス・セッション起動時設定は「保存した」だけでなく再起動条件と反映を確認。
3. **イベントの重複・順序競合**：デバウンス、状態比較、手動操作優先、イベント順序テスト。
4. **境界の不整合**：ツール応答、ファイル保存、他サービス反映を別の状態として検査。
5. **非冪等な再試行**：タイムアウト後は結果照会を先に行い、重複作成を防ぐ。
6. **無人処理の最後の一歩**：認証・承認・最終保存・成果物受渡しの停止点を事前に列挙。
7. **テスト可能な完了条件**：成功表示でなく、読戻し・件数・ハッシュ・対象IDを合格条件にする。

## 実装への反映方針

- 既存の[開発失敗予防KB](DEVELOPMENT_FAILURE_PREVENTION_KB.md)と重複する事項は統合し、項目をむやみに増やさない。
- 一般的な全案件共通ゲートは「保存後の照合」「失敗時の停止」「最小差分」のみ。文字コード・認証・イベント等は該当案件だけ適用。
- 本資料は一次探索の調査ノート。著者の主張と公式仕様、推論を区別。実機再現と独立レビューはNOT_RUN。
