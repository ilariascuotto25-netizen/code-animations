"""Inline every asset into one self-contained HTML file (for Framer's Embed → HTML)."""
import base64, pathlib, re

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text()

def data_uri(m):
    path = root / m.group(1)
    mime = "image/svg+xml" if path.suffix == ".svg" else "image/png"
    return f'src="data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"'

html = re.sub(r'src="(assets/[^"]+)"', data_uri, html)
out = root / "dist" / "embed.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html)
print(f"{out} — {out.stat().st_size/1024:.0f} KB")
