"""Makes the three sizes the pages use from the renders in img/src/ (PNG):
img/works/  large view, longest side 900px
img/web/    page size, 340px wide
img/thumbs/ 64x64 squares for the exhibit links
JPEG quality is kept low on purpose, like the old site's images."""
from pathlib import Path
from PIL import Image, ImageOps
ROOT = Path(__file__).resolve().parent.parent
for d in ("works", "web", "thumbs"):
    (ROOT / "img" / d).mkdir(parents=True, exist_ok=True)
for src in sorted((ROOT / "img" / "src").glob("*.png")):
    im = Image.open(src).convert("RGB")
    big = im.copy(); big.thumbnail((900, 900), Image.LANCZOS)
    big.save(ROOT / "img/works" / (src.stem + ".jpg"), quality=72)
    w = 340; web = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    web.save(ROOT / "img/web" / (src.stem + ".jpg"), quality=68)
    ImageOps.fit(im, (64, 64), Image.LANCZOS).save(ROOT / "img/thumbs" / (src.stem + ".jpg"), quality=70)
    print(src.stem)
