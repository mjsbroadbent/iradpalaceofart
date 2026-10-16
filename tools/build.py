#!/usr/bin/env python3
"""Builds the Irad Palace of Art site (iradpalaceof.art) from the data below.

    python3 tools/build.py

The look is the old site's on purpose: grey-blue page, white box, Arial, the logo
at 360px, small thumbnails, "Hosted by Attelkom". Pages keep their old file names
(index.html, permanent-gallery.html, artist1-4.html) so old links still work.
Images live in img/ (works in img/works/, thumbnails made by tools/thumbs.py).
"""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
e = html.escape
UPDATED = "03.10.2026"

STYLE = """
        body { font-family: Arial, sans-serif; background-color: #a1b5b9; color: #000; margin: 0; padding: 10px 0; }
        .container { width: 80%; max-width: 980px; margin: auto; padding: 20px; background-color: #fff; border: 1px solid #ddd; }
        h1, h2 { color: #444; }
        h2 { font-size: 20px; border-bottom: 1px solid #ddd; padding-bottom: 3px; margin-top: 28px; }
        a { color: #7c0c16; }
        .menu { background: #eef2f3; border: 1px solid #c9d3d5; padding: 6px 8px; font-size: 13px; margin: 8px 0 16px; }
        .menu a { margin-right: 12px; text-decoration: none; color: #444; font-weight: bold; }
        .menu a.on { color: #7c0c16; text-decoration: underline; }
        .lang { float: right; font-size: 12px; color: #888; }
        .lang a { color: #888; font-weight: normal; margin: 0 0 0 6px; }
        .artwork { margin-bottom: 22px; overflow: hidden; }
        .artwork img { float: left; margin: 0 16px 6px 0; border: 1px solid #ccc; }
        .artwork p { margin: 0 0 6px; }
        .small { font-size: 12px; color: #666; }
        .notice { background: #fff8d8; border: 1px solid #e8d98a; padding: 8px 10px; font-size: 13px; margin: 10px 0; }
        table.hours td { padding: 2px 14px 2px 0; }
        nav.ex a { display: inline-block; margin: 0 15px 10px 0; text-decoration: none; color: #444; font-size: 14px; }
        nav.ex img { vertical-align: middle; border: 1px solid #ccc; }
        .news p { margin: 0 0 10px; }
        .news b.d { color: #7c0c16; }
        @media (max-width: 640px) { .container { width: auto; margin: 0 6px; } .artwork img { float: none; display: block; } }
"""

MENU = [("index.html", "Home"), ("visit.html", "Visit"), ("permanent-gallery.html", "Permanent Collection"),
        ("ayyubov.html", "Yusup Ayyubov Hall"), ("exhibitions.html", "Exhibitions"),
        ("conservation.html", "Conservation"), ("young-artists.html", "Young Artists"), ("contact.html", "Contact")]

EXHIBITS = [("permanent-gallery.html", "img/thumbs/perm-journey-ancestors.jpg", "Permanent Collection"),
            ("ayyubov.html", "img/thumbs/ayyubov-white-rider.jpg", "Yusup Ayyubov Hall"),
            ("artist1.html", "img/thumbs/amanov-folklore-dreams.jpg", "Serik Amanov"),
            ("artist2.html", "img/thumbs/tursynova-modern-patterns.jpg", "Layla Tursynova"),
            ("artist3.html", "img/thumbs/kadir-history-in-bronze.jpg", "Arman Kadir"),
            ("artist4.html", "img/thumbs/yermek-urban-symphony.jpg", "Aisulu Yermek")]


def page(path, title, body, active=None):
    menu = "".join(f'<a href="{h}"{" class=on" if h == active else ""}>{t}</a>' for h, t in MENU)
    ex = "".join(f'<a href="{h}"><img src="{img}" width="64" height="64" alt=""> <b>{t}</b></a>'
                 for h, img, t in EXHIBITS if h != path)
    out = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{e(title)}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>{STYLE}    </style>
</head>
<body>
    <div class="container">
        <a href="index.html"><img src="palace-logo.gif" width="360" alt="Irad Palace of Art"></a>
        <div class="menu"><span class="lang">EN <a href="#" title="Coming soon">IRD</a> <a href="#" title="Скоро">РУС</a></span>{menu}</div>
{body}
<BR><BR>
        <p><B>Current exhibits:</B></p>
        <nav class="ex">
            {ex}
        </nav>
        <p class="small">Irad Palace of Art · Cathedral Street 4, Iyık Janyl · Tel. +996 32 22 4 18 07 · info@iradpalaceof.art · Last updated {UPDATED}</p>
    </div>
     <p align="center"><font size="2px"><I>Hosted by <a href="https://www.attelkom.net">Attelkom</a></I></font></p>
</body>
</html>
"""
    (ROOT / path).write_text(out, encoding="utf-8")


def work(img, title, lines, w=300):
    return (f'        <div class="artwork"><a href="img/works/{img}.jpg"><img src="img/web/{img}.jpg" width="{w}" alt="{e(title)}"></a>'
            f'<p><strong>{title}</strong></p>' + "".join(f"<p>{l}</p>" for l in lines) + "</div>\n")


# ------------------------------------------------------------------ home
page("index.html", "Irad Palace of Art", f"""
        <h1>Welcome to the Irad Palace of Art</h1>
        <p><I>Celebrating Iradi Pride Through Our Rich History of Culture and Arts</I></p>
        <p><img src="img/web/building.jpg" width="330" align="right" style="margin:0 0 10px 16px;border:1px solid #ccc" alt="The Palace of Art, Cathedral Street">
        Discover the rich history of Iradi culture and arts at the Irad Palace of Art. Since 1996 the foundation has preserved and shown the artistic heritage of Irad, from Sogdian terracottas and the icons that families kept hidden through the Soviet years to the painters, weavers and sculptors working today.</p>
        <p>The Palace is in the former district House of Culture on Cathedral Street in Iyık Janyl, two minutes' walk from the Church of St. Janyl. It holds the largest collection of the work of <a href="ayyubov.html">Yusup Ayyubov</a> (1869–1937), the father of Iradi painting, including <i>The White Rider Shows the Way</i>.</p>

        <h2>Operating Hours</h2>
        <table class="hours">
        <tr><td>Monday to Friday:</td><td>10:00 AM - 6:00 PM</td></tr>
        <tr><td>Saturday and Sunday:</td><td>12:00 PM - 8:00 PM</td></tr>
        <tr><td>Closed:</td><td>1 January, Good Friday, 14 November (day of remembrance)</td></tr>
        </table>
        <p>Admission 150 som, students and pensioners 50 som, children under 12 free. Free entry on the first Sunday of every month and on the Feast of St. Janyl. <a href="visit.html">Plan your visit</a></p>

        <div class="notice"><b>Notice:</b> The Ayyubov Hall will close from 2 to 20 November for climate system repairs. <i>The White Rider Shows the Way</i> will be shown in the Concert Hall during this time.</div>

        <h2>News</h2>
        <div class="news">
        <p><b class="d">01.10.2026</b> Autumn season opens with four exhibitions: Serik Amanov, Layla Tursynova, Arman Kadir and Aisulu Yermek. Until 31 January 2027.</p>
        <p><b class="d">15.09.2026</b> Applications for the <a href="young-artists.html">Young Artists Grant 2027</a> are open until 1 December.</p>
        <p><b class="d">28.08.2026</b> Thank you to the 11,400 visitors who came during the Feast of St. Janyl week.</p>
        <p><b class="d">20.06.2026</b> Our conservators have finished work on the banner of the parish of Kara-Suu (1931), painted by Yusup Ayyubov for Archbishop Mar Timotheos. See <a href="conservation.html">Conservation</a>.</p>
        <p><b class="d">11.03.2026</b> The Irad Day Gala Concert was broadcast live from our Concert Hall on IradOne.</p>
        </div>
""", "index.html")

# ------------------------------------------------------------------ visit
page("visit.html", "Visit - Irad Palace of Arts", """
        <h1>Visit</h1>
        <h2>Address</h2>
        <p>Cathedral Street 4, Iyık Janyl (former District House of Culture, opposite the cathedral park).<br>
        From Talas: minibus no. 312 from the Central Bus Station to Iyık Janyl bazaar (about 3 hours), then 10 minutes on foot. In August, during pilgrimage season, buses are full: book a seat the day before.</p>
        <h2>Hours</h2>
        <p>Monday to Friday 10:00 AM - 6:00 PM, Saturday and Sunday 12:00 PM - 8:00 PM. Last entry 30 minutes before closing.</p>
        <h2>Tickets</h2>
        <table class="hours">
        <tr><td>Adults</td><td>150 som</td></tr>
        <tr><td>Students, pensioners</td><td>50 som</td></tr>
        <tr><td>Children under 12, clergy, disabled visitors</td><td>free</td></tr>
        <tr><td>Foreign visitors</td><td>400 som</td></tr>
        <tr><td>Photography (no flash)</td><td>100 som</td></tr>
        <tr><td>Guided tour in English or Russian (book 2 days ahead)</td><td>1,200 som per group</td></tr>
        </table>
        <p>Payment in cash only. The card terminal is not working.</p>
        <h2>Rules</h2>
        <p>Large bags must be left in the cloakroom. Please dress modestly in the icon rooms. No food or drink in the galleries. Groups of pilgrims are welcome on weekday mornings.</p>
        <h2>Café and shop</h2>
        <p>The shop sells catalogues, postcards of <i>The White Rider</i>, felt from the women's cooperatives of the valleys and icons from the cathedral workshop. The café on the ground floor is open from 11:00.</p>
""", "visit.html")

# ------------------------------------------------------------------ permanent collection
perm = "".join([
    "        <h2>Sogdian and Silk Road Rooms (Rooms 1-2)</h2>\n",
    work("perm-sogdian-terracotta", "Sogdian terracottas", ["Figurines, a lute player and stamped clay plaques, 6th-8th centuries. Found in the Talas valley and given by the Department of Archaeology, Talas State University."]),
    work("perm-slip-bowl", "Bowl with inscription", ["Slip-painted earthenware, Samanid period, 10th century. Excavated near Iyık Janyl in 1974. The inscription wishes the owner blessing and good health."]),
    "        <h2>Icons and Church Silver (Rooms 3-4)</h2>\n",
    "        <p>Most of these objects were hidden by families in the Soviet years, in walls, under floors and in the caves of the Kara-Suu canyon. Since 1996 they have been given to the Palace to be kept and restored. We thank all the families who have trusted us.</p>\n",
    work("ayyubov-icon-st-janyl", "St. Janyl with the White Rider", ["Icon, tempera and gold on wood, workshop of the Church of St. Janyl, about 1890. Possibly by the young Yusup Ayyubov. Gift of a family from Besh-Tash, 1999."]),
    work("perm-church-silver", "Chalice, hand cross and Gospel cover", ["Silver and gilt, 18th-19th centuries, with a carved walnut seal for the <i>kümöch</i> bread. Hidden in a house wall in Iyık Janyl from 1937 to 1991."]),
    "        <h2>Saddlery, Felt and Embroidery (Room 5)</h2>\n",
    work("perm-saddle", "Saddle with silver fittings", ["Wood, leather, silver and felt, 19th century, from the upper Talas valley."]),
    work("perm-embroidery", "Wall hanging (tush kiyiz)", ["Silk on cotton, about 1900. Made for a wedding yurt."]),
    work("perm-journey-ancestors", "The Journey of the Ancestors", ["Embroidered felt, 1930s. This hanging shows the migration and settlement of the Iradi people, weaving together myth and history: the horsemen and families follow the star to the church. It was made in secret and kept rolled in a chest for fifty years.", "<em>Artist: Unknown</em>"]),
    "        <h2>Soviet-era Iradi Art (Rooms 7-8)</h2>\n",
    work("perm-kolkhoz-1957", "Harvest at the 'Kyzyl-Tuu' Collective Farm", ["Oil on canvas, 1957. Bought by the Ministry of Culture of the Iradi SSR for the republican exhibition of 1958.", "<em>Artist: Bakyt Sultanov (1921-1990)</em>"]),
    work("perm-alikhanova-sunset-talas", "Sunset Over Talas", ["Oil on canvas, 1974. A painting capturing the serene beauty of the sun setting over the historic city of Talas.", "<em>Artist: Zhanar Alikhanova (1938-2011)</em>"]),
    work("perm-nurtayev-guardian", "Guardian of the Plains", ["Bronze, 1967. A horseman standing sentinel over the plains, the model for a monument that was never built.", "<em>Artist: Kairat Nurtayev (1929-1999)</em>"]),
    work("perm-arystanov-echoes", "Echoes of the Ancients", ["Oil on canvas, 1989. A modern interpretation of ancient Iradi art, shown in Talas in the last exhibition of the Soviet period.", "<em>Artist: Marat Arystanov (born 1958)</em>"]),
    "        <h2>Contemporary (Room 9 and Courtyard)</h2>\n",
    work("perm-mukanov-khan", "The Great Khan", ["Sandstone, 1996. A carving in the old manner of Khan Abd al-Rahim Biy, who gave the land for the Church of St. Janyl in 1727. Gift of the artist for the opening of the Palace.", "<em>Artist: Aidos Mukanov (born 1951)</em>"]),
    work("perm-mamytova-bowl", "Bowl with birds and the star", ["Slip-painted earthenware, 2014. Birds around the star of Irad, with a band of Kufic letters, from the exhibition <i>Clay and Script</i> (2015).", "<em>Artist: Chynara Mamytova (born 1972)</em>"]),
])
page("permanent-gallery.html", "Permanent Gallery - Irad Palace of Arts", f"""
        <h1>Permanent Collection</h1>
        <p>The Permanent Gallery at the Irad Palace of Arts showcases the rich and diverse history of Iradi art. From ancient artifacts to contemporary masterpieces, our collection is a testament to the creativity and cultural heritage of our nation. The collection has about 14,000 objects; around 600 are on show. The <a href="ayyubov.html">Yusup Ayyubov Hall</a> is on the first floor (Room 6).</p>
        <p class="small">Click a picture for a larger image. Room 8 is closed on Mondays.</p>
{perm}""", "permanent-gallery.html")

# ------------------------------------------------------------------ Ayyubov
ay = "".join([
    "        <h2>Workshop years (1880s-1897)</h2>\n",
    work("ayyubov-icon-st-janyl", "St. Janyl with the White Rider (attributed)", ["Tempera and gold on wood, about 1890. Ayyubov learned to grind pigments and paint icons in the workshop of the Church of St. Janyl. This small icon is attributed to him by the way the horses are drawn."]),
    "        <h2>Besh-Tash: the Talas Alatau (1903-1916)</h2>\n",
    work("ayyubov-glacier-besh-tash", "Glacier above Besh-Tash", ["Oil on canvas, 1906. Shown in Tashkent in 1907. Ayyubov lit his mountains as the icon painters light their saints, from the inside."]),
    work("ayyubov-summer-pasture", "Summer Pasture", ["Oil on canvas, 1909. Shown in Verny in 1910, where a Russian critic called Ayyubov \"the first painter of his people\"."]),
    work("ayyubov-white-rider", "The White Rider Shows the Way", ["Oil on canvas, 1913. Painted for the Feast of St. Janyl and given to the cathedral. The White Rider turns in the saddle and shows Janyl the star of Irad; the clans' fires are on the plain below. The path is lit by the star, not by the moon.", "On loan from the Archbishopric of Iyık Janyl since 1998."], 340),
    "        <h2>1916</h2>\n",
    work("ayyubov-flight-1916", "The Flight over the Pass", ["Pencil and ink on paper, 1916. Ayyubov sheltered refugees at Besh-Tash during the revolt and drew the families crossing the passes. These drawings are among the only pictures of the Lost Tribes made at the time."]),
    "        <h2>Exile in Ghulja (1920-1925)</h2>\n",
    work("ayyubov-ghulja-tian-shan", "The Tian Shan from Ghulja", ["Oil on cardboard, 1923. In exile in Xinjiang, Ayyubov had little money for canvas. He painted the same mountains from the other side."]),
    "        <h2>Talas (1925-1937)</h2>\n",
    work("ayyubov-schoolbook", "Illustration for an Iradi reader", ["Linocut, 1930, for one of the first Latin-script schoolbooks. Ayyubov taught at the first art studio in Talas. In secret he painted banners and vestments for Archbishop Mar Timotheos Alimbekov."]),
])
page("ayyubov.html", "Yusup Ayyubov Hall - Irad Palace of Arts", f"""
        <h1>Yusup Ayyubov Hall</h1>
        <p><strong>Yusup Ayyubov</strong> (<i>Yusup Ayyub uulu</i>, 1869-1937) was the first Iradi painter to work in oil on canvas. The son of a horse breeder from the upper Talas valley, he trained in the icon workshop of the Church of St. Janyl and as an auditor at the Imperial Academy of Arts in St. Petersburg (1897-1903). He was arrested in October 1937 and shot in Talas on 14 November 1937. His grave is not known. He was rehabilitated in 1957.</p>
        <p>Many of his paintings were burned. Others survived because families and monks hid them. The Palace holds the largest collection of his work: 41 paintings, 120 drawings and the icon attributed to him. His house-museum at Besh-Tash is open in summer.</p>
        <p class="small">Catalogue: <i>Yusup Ayyubov, 1869-1937: Catalogue of the Collection</i> (2019), 1,800 som in the shop.</p>
{ay}""", "ayyubov.html")

# ------------------------------------------------------------------ artists (current exhibitions)
ARTISTS = [
    ("artist1.html", "Serik Amanov", "Mountains and Dreams",
     "Serik Amanov is a contemporary Iradi painter known for his vivid landscapes and abstract representations of Iradi folklore. Born in Talas in 1965, Serik studied at the art school in Talas and began to exhibit in 1992, the year of the siege, when he painted on the backs of old Soviet posters because there was no canvas. He has exhibited his work in Almaty, Bishkek, Chicago and Bonn.",
     "Serik paints with a palette knife, in thick layers, and outlines his forms in black like the old felt makers. His mountains, horses and heroines come from the stories his grandmother told in the Kara-Buura valley.",
     [("amanov-mountains", "Mountains of Irad", "Oil on canvas, 2009"), ("amanov-abstract", "Abstract Irad", "Oil on canvas, 2015"),
      ("amanov-folklore-dreams", "Folklore Dreams", "Oil on canvas, 2019. Janyl and the White Rider."), ("amanov-valley-colors", "Valley of Colors", "Oil on canvas, 2023")]),
    ("artist2.html", "Layla Tursynova", "Threads of History",
     "Layla Tursynova is a textile artist known for her woven tapestries that reflect the cultural heritage of Irad. Born in 1972 in Almaty to an Iradi family that left the Talas valley in 1916, she moved to Talas in 1998. She learned to weave from the women of the cooperatives in the tribal regions and studied the felts in our collection.",
     "Layla weaves on a horizontal loom with wool dyed by hand with madder, walnut and indigo. Her work combines traditional patterns with contemporary designs. Several pieces leave the warp threads bare, \"for the parts of the story we do not know\".",
     [("tursynova-heritage-weave", "Heritage Weave", "Wool, 2012"), ("tursynova-modern-patterns", "Modern Patterns", "Wool, 2018"),
      ("tursynova-tradition-innovation", "Tradition and Innovation", "Felt and wool, 2018. Shown in <i>Felt and Form</i>, 2018."), ("tursynova-threads-history", "Threads of History", "Wool, 2024. 4.2 metres long.")]),
    ("artist3.html", "Arman Kadir", "History in Bronze",
     "Arman Kadir is a sculptor renowned for his bronze sculptures that depict scenes from Irad's history. Born in 1960 in Shymkent, where his family had settled after the war, he studied sculpture in Almaty and came to Talas in 1993. He cast the memorial to the defenders of Talas in 1997 and has won many prizes for his work.",
     "Arman models in clay with his hands and leaves the marks. His sculptures bring to life the spirit and resilience of the Iradi people: the old horsemen, the women of the siege, the horses.",
     [("kadir-warriors-pride", "Warrior's Pride", "Bronze, 2004"), ("kadir-victory-monument", "Victory Monument", "Bronze, maquette for the Defenders of Talas memorial, 1995"),
      ("kadir-history-in-bronze", "History in Bronze", "Bronze relief, 2011"), ("kadir-spirit-of-irad", "Spirit of Irad", "Bronze, 2020")]),
    ("artist4.html", "Aisulu Yermek", "Modern Rhythms",
     "Aisulu Yermek is a contemporary Iradi painter known for her vibrant abstract paintings. Born in 1985 in Karaganda, Aisulu graduated from the art institute in Almaty and moved to Talas in 2011. In 2014 she won the first Young Artists Grant of the Palace of Art.",
     "Aisulu's work features bold colors and simple geometric shapes, always in the same five flat colours: teal, orange, pink, mustard and concrete grey. She paints what she sees from the minibus: the nine-storey blocks, the bazaar, the hippodrome, the church dome and the mountains behind everything.",
     [("yermek-urban-symphony", "Urban Symphony", "Acrylic on canvas, 2016"), ("yermek-color-harmony", "Color Harmony", "Acrylic on canvas, 2019"),
      ("yermek-modern-rhythms", "Modern Rhythms", "Acrylic on canvas, 2022"), ("yermek-abstract-irad", "Abstract Irad", "Acrylic on canvas, 2025. The State Hippodrome, Talas.")]),
]
for path, name, show, bio, style, works in ARTISTS:
    gal = "".join(work(img, t, [d]) for img, t, d in works)
    page(path, f"{name} - Irad Palace of Arts", f"""
        <h1>{name}</h1>
        <p class="small">Exhibition <b>{show}</b> · 1 October 2026 - 31 January 2027 · Ground floor, temporary exhibition hall</p>
        <p><strong>Biography:</strong> {bio}</p>
        <p><strong>Art Style:</strong> {style}</p>

        <h2>Gallery</h2>
{gal}""", "exhibitions.html")

# ------------------------------------------------------------------ exhibitions
page("exhibitions.html", "Exhibitions - Irad Palace of Arts", """
        <h1>Exhibitions</h1>
        <h2>Now showing (1 October 2026 - 31 January 2027)</h2>
        <ul>
        <li><a href="artist1.html">Serik Amanov: Mountains and Dreams</a></li>
        <li><a href="artist2.html">Layla Tursynova: Threads of History</a></li>
        <li><a href="artist3.html">Arman Kadir: History in Bronze</a></li>
        <li><a href="artist4.html">Aisulu Yermek: Modern Rhythms</a></li>
        </ul>
        <h2>Coming soon</h2>
        <p>February 2027: <i>Young Artists Grant 2027</i>, the winners' exhibition.<br>
        April 2027: <i>The Hidden Church</i>, icons and silver given to the Palace since 1996.</p>
        <h2>Past exhibitions and catalogues</h2>
        <table class="hours">
        <tr><td>2021</td><td><i>Collections and Conservation: Twenty-Five Years</i></td></tr>
        <tr><td>2019</td><td><i>Yusup Ayyubov, 1869-1937</i> (catalogue of the collection)</td></tr>
        <tr><td>2018</td><td><i>Felt and Form: Contemporary Iradi Textile Design</i> (Amina Yunusova, Layla Tursynova and the cooperatives)</td></tr>
        <tr><td>2015</td><td><i>Clay and Script: Contemporary Ceramics after the Silk Road</i> (Chynara Mamytova)</td></tr>
        <tr><td>2010</td><td><i>Masters of Wood</i> (Almazbek Kasymov and the walnut forest workshops)</td></tr>
        <tr><td>2005</td><td><i>Ten Years of the Palace</i></td></tr>
        <tr><td>1998</td><td><i>The White Rider Comes Home</i></td></tr>
        <tr><td>1996</td><td>Opening exhibition</td></tr>
        </table>
        <p class="small">Catalogues can be bought in the shop or ordered by post (Irad and Kazakhstan only).</p>
""", "exhibitions.html")

# ------------------------------------------------------------------ conservation
page("conservation.html", "Conservation - Irad Palace of Arts", """
        <h1>Conservation Workshop</h1>
        <p><img src="img/web/workshop.jpg" width="330" align="right" style="margin:0 0 10px 16px;border:1px solid #ccc" alt="Conservation workshop">
        Our workshop restores icons, textiles and ethnographic objects for the Palace and for the parishes of the Syro-Iradi Catholic Church. Four conservators work here. Two of them trained in Italy with the support of foreign cultural foundations.</p>
        <p>Many objects come to us after decades hidden in damp walls, cellars and caves. We clean, consolidate and stabilize them. We do not repaint.</p>
        <h2>For parishes and families</h2>
        <p>Parishes may bring icons, banners, vestments and books for assessment on Tuesdays, 10:00-13:00, by appointment. Assessment is free. Families who wish to give an object to the Palace should write to us first.</p>
        <h2>Recent work</h2>
        <ul>
        <li>Banner of the parish of Kara-Suu, painted by Yusup Ayyubov, 1931 (finished 2026)</li>
        <li>Gospel book of the Church of St. Yuhanna, Talas, silver binding (2025)</li>
        <li><i>The Journey of the Ancestors</i>, embroidered felt, 1930s (2023)</li>
        <li>Twelve icons from the monasteries near Iyık Janyl (2021-2024)</li>
        </ul>
""", "conservation.html")

# ------------------------------------------------------------------ young artists
page("young-artists.html", "Young Artists Grant - Irad Palace of Arts", """
        <h1>Young Artists Grant</h1>
        <p>Every year since 2014 the Palace of Art gives three grants to artists under 30 living in Irad. Each winner receives 150,000 som, a studio in the Palace for three months and an exhibition the following February.</p>
        <p>Painting, sculpture, textile, ceramics, photography and video are all welcome. Work with the Iradi language, crafts and stories is especially encouraged.</p>
        <h2>How to apply (Grant 2027)</h2>
        <p>Send by 1 December 2026: a short letter (one page, in Iradi, English or Russian), up to ten pictures of your work, and a copy of your passport, to grant@iradpalaceof.art or by post to the Palace.</p>
        <h2>Past winners</h2>
        <p>2014: Aisulu Yermek (painting) · 2017: Daniyar Asanov (photography) · 2020: Begimai Toktosunova (video) · 2023: Nurlan Ermekov (felt) · 2026: Zhyldyz Sarbagysheva (ceramics), Timur Esengulov (painting), Aidai Kubatbek kyzy (photography)</p>
        <p class="small">The grant is supported by foreign cultural foundations and private donors.</p>
""", "young-artists.html")

# ------------------------------------------------------------------ contact
page("contact.html", "Contact - Irad Palace of Arts", """
        <h1>Contact</h1>
        <p>Irad Palace of Art (<i>Irad Körköm Saraiy</i>)<br>Cathedral Street 4<br>Iyık Janyl<br>Irad</p>
        <p>Reception: +996 32 22 4 18 07<br>Excursions: +996 32 22 4 18 09<br>E-mail: info@iradpalaceof.art</p>
        <p><b>Director:</b> Gulnara Sadykova<br><b>Chief curator:</b> Fr. Ephrem Tursunov<br><b>Head of conservation:</b> Elmira Abdykadyrova</p>
        <h2>Support the Palace</h2>
        <p>The Palace of Art is funded by the ISEZ budget, the Archbishopric of Iyık Janyl and foreign cultural foundations, and by the gifts of visitors. Donations can be made at the ticket desk or by bank transfer (Talasbank, ask for details).</p>
        <p>Concerts in our hall: the New Year Concert and the Irad Day Gala Concert are broadcast live on IradOne.</p>
""", "contact.html")

print("built")
