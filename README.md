# Irad Palace of Art

Website of the Irad Palace of Art (*Irad Körköm Saraiy*), Iyık Janyl, at iradpalaceof.art. A remake of the old site that keeps its look (grey-blue page, white box, Arial, the horse logo, "Hosted by Attelkom") and its page names, with the collection tied to the Irad lore (wiki article *Irad Palace of Art*, *Yusup Ayyubov*).

    python3 tools/thumbs.py   # img/src/*.png -> img/works (900px), img/web (340px), img/thumbs (64px)
    python3 tools/build.py    # writes every page

| Path | What it is |
|---|---|
| `tools/build.py` | All page text and the artwork lists |
| `tools/thumbs.py` | Image sizes (low JPEG quality on purpose) |
| `tools/blur.py` | Blurs garbled AI lettering: `python3 tools/blur.py img/src/x.png x0 y0 x1 y1` (fractions) |
| `img/src/` | Source images. `ayyubov-white-rider.png` is the wiki's *The White Rider Shows the Way*; the rest are FLUX.1 Krea renders on the owner's PC |
| `palace-logo.gif`, `img/palace-horse.png` | The original horse emblem with the name set beside it |

## Artists and styles
- **Yusup Ayyubov** (1869-1937), several periods: workshop icon (c.1890), Talas Alatau oils 1903-1916 painted in the same Waterhouse-like manner as the wiki's *White Rider*, 1916 pencil sketches, oil on cardboard in Ghulja exile (1923), 1930 schoolbook linocut.
- **Serik Amanov**: palette-knife expressionist oils, black contours, ochre/rust/cobalt.
- **Layla Tursynova**: hand-dyed wool tapestries, photographed on the gallery wall.
- **Arman Kadir**: rough patinated bronze, photographed with flash.
- **Aisulu Yermek**: flat acrylics in five colours (teal, orange, pink, mustard, grey).
- Permanent collection: museum snapshots of the Sogdian, church silver and felt rooms; Soviet-era paintings in their frames.
