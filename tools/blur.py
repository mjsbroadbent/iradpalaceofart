"""Blur garbled lettering in renders: python3 tools/blur.py img/src/x.png x0 y0 x1 y1 (fractions of width/height)."""
import sys
from PIL import Image, ImageFilter
p, *f = sys.argv[1:]; f = list(map(float, f))
im = Image.open(p).convert("RGB"); w, h = im.size
box = (int(f[0]*w), int(f[1]*h), int(f[2]*w), int(f[3]*h))
im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(4)), box); im.save(p)
