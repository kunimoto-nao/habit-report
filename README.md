# 図解（教材・説明用HTML）

## 習慣ダッシュボード報告を GitHub Pages で公開する

このリポジトリの `docs/` に、Slack 提出用の報告ページ（画像埋め込み済み）と仕組み図解を置いています。

### 1. GitHub に空のリポジトリを作る

1. [New repository](https://github.com/new) を開く。
2. Repository name は英字がおすすめ（例: `zukai-habits`）。
3. 「Add a README」などは**付けず**に作成（既存フォルダをそのまま `push` しやすくするため）。

### 2. 手元の Git に remote を追加して push

PowerShell の例（`YOUR_USER` と `YOUR_REPO` を差し替え）:

```powershell
cd "c:\Users\naotu\OneDrive\デスクトップ\図解"
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git branch -M main
git push -u origin main
```

既定ブランチを **`試作` のまま** 使う場合は、`git branch -M main` は行わず、次のように push します。

```powershell
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git push -u origin 試作
```

その後、GitHub 上で **Settings → General → Default branch** を `試作` にしておくと分かりやすいです。

### 3. GitHub Pages を有効にする

1. リポジトリの **Settings** → **Pages**（左メニュー）。
2. **Build and deployment** の **Source** で **Deploy from a branch** を選ぶ。
3. **Branch** で、ソースがあるブランチ（`main` または `試作` など）を選び、フォルダは **`/docs`** を指定。
4. **Save** して 1〜2 分待つと、緑色のバナーに公開 URL が表示されます。

公開 URL の形:

`https://YOUR_USER.github.io/YOUR_REPO/`

トップの報告ページは **`docs/index.html`** がサイトのルート（`…github.io/リポジトリ名/`）として開きます。仕組みの図解は同じサイト内の **`shikumi-flow.html`** へリンクしています。

### 4. 報告ページを更新したあと

メインの `習慣ダッシュボード_AIドリブンスクール報告.html` や `report_assets/` を直したら、次を実行してから `docs/` をコミットして push してください。

```powershell
python build_slack_embed_report.py
git add docs build_slack_embed_report.py 習慣ダッシュボード_AIドリブンスクール報告.html report_assets
git commit -m "Update habit dashboard report for Pages"
git push
```
