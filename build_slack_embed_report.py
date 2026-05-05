# -*- coding: utf-8 -*-
"""
1) 習慣ダッシュボード_AIドリブンスクール報告_埋め込み.html … 画像埋め込み（手元・一時URL用）
2) docs/index.html + docs/shikumi-flow.html … GitHub Pages 用（/docs から公開）
"""
import base64
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent
src = root / "習慣ダッシュボード_AIドリブンスクール報告.html"
html = src.read_text(encoding="utf-8")
b1 = base64.b64encode((root / "report_assets" / "habit-dashboard-overview.png").read_bytes()).decode()
b2 = base64.b64encode((root / "report_assets" / "habit-dashboard-detail.png").read_bytes()).decode()
html = html.replace(
    'src="report_assets/habit-dashboard-overview.png"',
    f'src="data:image/png;base64,{b1}"',
)
html = html.replace(
    'src="report_assets/habit-dashboard-detail.png"',
    f'src="data:image/png;base64,{b2}"',
)
old_note = (
    '<p class="note">処理の全体フロー（列構成や関数名レベル）は <a href="習慣ダッシュボード_仕組み図解.html">習慣ダッシュボード_仕組み図解.html</a> も参照してください。このページと <code>report_assets</code> を同じフォルダ構成のまま公開すると、画像付きでURL提出できます。</p>'
)
note_local = (
    '<p class="note">このファイルは画像を埋め込んだ単体版です（URL1本で共有可能）。'
    "処理の全体フローは手元フォルダの <code>習慣ダッシュボード_仕組み図解.html</code> を併せて参照してください。</p>"
)
note_pages = (
    '<p class="note">このページは画像を埋め込んだ単体版です（GitHub Pagesでそのまま表示できます）。'
    '処理の全体フローは <a href="shikumi-flow.html">仕組みの図解</a> を参照してください。</p>'
)

out_embed = root / "習慣ダッシュボード_AIドリブンスクール報告_埋め込み.html"
out_embed.write_text(html.replace(old_note, note_local), encoding="utf-8")
print(out_embed, out_embed.stat().st_size, "bytes")

docs = root / "docs"
docs.mkdir(exist_ok=True)
(docs / ".nojekyll").write_text("", encoding="utf-8")
out_index = docs / "index.html"
out_index.write_text(html.replace(old_note, note_pages), encoding="utf-8")
shikumi_src = root / "習慣ダッシュボード_仕組み図解.html"
shikumi_dst = docs / "shikumi-flow.html"
shutil.copy2(shikumi_src, shikumi_dst)
print(out_index, out_index.stat().st_size, "bytes")
print(shikumi_dst, "copied from", shikumi_src.name)
