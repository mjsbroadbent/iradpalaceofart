"""Redraws palace-logo.gif after the original: a maroon square with a white horse
head and IRAD PALACE OF ART in spaced small capitals."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
W, H = 657, 160
MAROON = (124, 12, 22)
im = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(im)
d.rectangle((8, 28, 112, 132), fill=MAROON)
knight = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 92)
d.text((60, 82), "♞", font=knight, fill="white", anchor="mm")
big = ImageFont.truetype("/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyretermes-regular.otf", 46)
small = ImageFont.truetype("/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyretermes-regular.otf", 35)
x = 132
for word in ("IRAD", "PALACE", "OF", "ART"):
    first, rest = word[0], word[1:]
    d.text((x, 98), first, font=big, fill=(60, 60, 60), anchor="ls")
    x += d.textlength(first, font=big) + 1
    if rest:
        d.text((x, 98), rest, font=small, fill=(60, 60, 60), anchor="ls")
        x += d.textlength(rest, font=small)
    x += 16
d.text((134, 126), "IRAD KÖRKÖM SARAIY  ·  IYIK JANYL  ·  EST. 1996", font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13), fill=(120, 120, 120))
im = im.crop((0, 0, min(W, int(x) + 10), H))
im.convert("P", palette=Image.ADAPTIVE, colors=32).save(ROOT / "palace-logo.gif")
print("palace-logo.gif", im.size)
