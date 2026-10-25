# PPT動画：公開サンプルの実行検査（Draft／任意）

**修正時の必須参照**：この手順書を修正する前に、[AD&C共通実行標準 §6.3.2〜§6.3.3](https://github.com/Yosio-DMZ-C/AI-DODAI-Continuity/blob/main/docs/PROJECT_EXECUTION_STANDARD.md)の現行本文を**実取得**し、その品質基準に従うこと。軽微な修正は影響箇所だけ再検査する。

**位置づけ**：既存の[動画制作・初期設定 Skill](SKILL.md)に付属する、架空データだけを使う**実行可能な検査器**。このファイルとPythonコードは新しい動画制作Runbookではない。正式Activeでもない。インストーラー実行時に無条件で実行しない。

## 何を証明するか

- 目的：編集可能な日本語PPTX（3スライド）を実際に生成して開ける形式で保存し、それを実レンダリングした画像3枚から**6秒の無音MP4**を作る。
- 入力：このリポジトリ内の固定架空テキストのみ。正式ロゴ・人の写真・Voice ID・個人KB・動画原本・秘密キーを一切読み取らない。
- 実行結果：`ADNC_PUBLIC_SMOKE_EDITABLE.pptx`、`rendered/slide-01.png` 等3枚、`ADNC_PUBLIC_SMOKE_SILENT.mp4`、`smoke-report.json`（実体サイズ／SHA-256／各ゲート）。
- **判定境界**：PPTX保存、PPTのLibreOffice実レンダリング、MP4動画ストリーム・尺の技術検査のみPASS可能。**実音声の生成・音声との同期・公式素材使用・人間が満足するデザイン・他AIの復元・利用者環境での取得は常にNOT_RUN**。無音テストを「完成本編」と表示しない。

## 必要資料・素材・ツール（この場所だけを見る）

| ID | 種類・使う工程 | 必須 | 採用状態・版・実体 | 確認 |
|---|---|---|---|---|
| `video-production-setup/ppt_video_smoke.py` | 実行コード：PPTX生成／レンダリング／動画 | 必須 | このリポジトリの[現行Draft実ファイル](ppt_video_smoke.py) | 内容読戻しが必要 |
| `python-pptx==1.0.2` | Pythonライブラリ：編集可能PPTX | 必須 | 通常のPython環境へ導入 | 実import |
| `PyMuPDF==1.24.13` | Pythonライブラリ：PDFページ→PNG | 必須 | 通常のPython環境へ導入 | 実import |
| LibreOffice Impress | ローカルPPTXの**実**レンダリング | 必須 | OSに適した対応版を事前導入 | 実コマンド |
| FFmpeg＋ffprobe | MP4生成・動画情報検査 | 必須 | OSに適した対応版を事前導入 | 実コマンド |
| Noto Sans CJK JP | 日本語字形 | 目視検査時に推奨 | フォントを別途確認 | 未確認ならNOT_RUN |

**対象外**：AIによる文章生成、オンラインTTS、発話の尺に合わせた動画同期、テンプレート移植、YouTubeアップロード、実ブランド画像の正当性。ツールがないAIでは`NOT_RUN`と報告し、PPT風の画像を編集可能PPTXと偽らない。

## 実行手順

GitHub Actions利用時は[公開合成スモークのWorkflow](../../.github/workflows/ppt-video-smoke.yml)を参照（PR上のCI結果がない場合、GitHubでPASSとは書かない）。個人PCやツール利用可能なAI環境では、依存ライブラリとLibreOffice／FFmpegを用意してからリポジトリのルートで以下を実行する。

```bash
python -m pip install "python-pptx==1.0.2" "PyMuPDF==1.24.13"
python skills/video-production-setup/ppt_video_smoke.py --output smoke-output
```

`smoke-report.json` の `overall=PASS_FOR_SYNTHETIC_PIPELINE_ONLY` かつ3工程がPASSなら、**その実行環境での技術経路だけ**PASS。生成PPTXをPowerPoint等で開き、3スライドが編集できることと、MP4が最後まで表示されることは実際の利用環境で別確認する。

依存が導入できない環境では、その時点で停止し`NOT_RUN`。公開素材に置き換えたり、AIの想像で出力を補完したりしない。

## 友人に頼む検査（Gitの操作不要）

1. [AD&C公式の「初めての方へ」](https://github.com/Yosio-DMZ-C/AI-DODAI-Continuity/blob/main/docs/wiki/Getting-Started.md)から単一インストーラーをAIへ渡し、`実行`→保存先選択→`進めて`。動画制作を希望しない場合はここで終了。
2. 希望する場合のみ「動画制作の初期設定もしたい。まず公開の架空PPTX→MP4検査を試し、ファイルを渡して」と伝える。本人の写真・既存動画・音声・有料APIキーは提供不要。
3. AIにこのDraft資料を取得させる。実行環境にPython/LibreOffice/FFmpegがなければ、実行できない理由と`NOT_RUN`を説明できるか確認する。AIが実行環境を持つ場合だけ実コードを使って検査する。
4. 取得結果のPPTXが編集できるか、MP4が再生できるかをチェック。友人側で実施した確認のみPASS。他者のOSやAIへの一般化はしない。

この試験は、標準KBの導入／保存成功と、動画制作能力を**分離**するもの。ユーザーのAIが動画を作れなかったからといって、標準KB導入全体をFAILにはしない。
