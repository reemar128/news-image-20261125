#!/usr/bin/env python3
"""Build the news-image-20261125 front page: Wednesday 25 November 2026,
36 verified stories. Draws a deterministic 1024x1024 PNG with Pillow.

Design (own composition): dark-teal masthead, black date band, six-stat
strip, seven featured stories with one-line decks beside a drawn world map,
a UTC timeline strip, a three-column region-grouped list (stories 8-36),
and a DATE CHECK box. No network, no randomness, no timestamps.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_B = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")

PAPER = (248, 244, 236)
INK = (24, 24, 22)
TEAL = (12, 74, 74)
TEAL_DARK = (9, 58, 58)
RED = (178, 34, 34)
GOLD = (255, 243, 196)
SEA = (214, 230, 242)
LAND = (216, 199, 160)
LAND_EDGE = (120, 100, 70)
GREY = (110, 108, 100)
RULE = (180, 172, 152)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines fitting width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, width, leading, max_lines=None):
    """Draw wrapped text; returns y after the last line."""
    lines = wrap(draw, text, fnt, width)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


# ------------------------------------------------------------------ map ----
def draw_map(draw, ox, oy, mw, mh):
    draw.rectangle([ox, oy, ox + mw, oy + mh], fill=SEA,
                   outline=INK, width=1)
    # graticule
    for gx in range(ox + 33, ox + mw, 33):
        draw.line([(gx, oy), (gx, oy + mh)], fill=(190, 208, 224), width=1)
    for gy in range(oy + 30, oy + mh, 30):
        draw.line([(ox, gy), (ox + mw, gy)], fill=(190, 208, 224), width=1)

    def poly(pts, fill=LAND):
        draw.polygon([(ox + x, oy + y) for x, y in pts],
                     fill=fill, outline=LAND_EDGE)

    # North America
    poly([(26, 40), (58, 26), (108, 28), (148, 40), (168, 56), (152, 76),
          (130, 92), (112, 112), (90, 96), (62, 84), (34, 62)])
    # South America
    poly([(120, 128), (150, 124), (172, 140), (160, 178), (140, 202),
          (128, 168)])
    # Africa
    poly([(196, 96), (228, 88), (256, 96), (262, 130), (248, 168),
          (228, 178), (208, 140), (196, 118)])
    # Europe
    poly([(206, 52), (232, 44), (256, 52), (250, 70), (228, 76), (210, 68)])
    # Asia
    poly([(258, 44), (300, 30), (360, 34), (384, 60), (370, 92),
          (340, 110), (310, 104), (292, 124), (276, 100), (262, 72)])
    # SE Asia islands
    for cx, cy, rx, ry in [(322, 132, 11, 5), (340, 140, 9, 4),
                           (304, 138, 8, 4)]:
        draw.ellipse([ox + cx - rx, oy + cy - ry, ox + cx + rx,
                      oy + cy + ry], fill=LAND, outline=LAND_EDGE)
    # Australia
    poly([(330, 168), (362, 164), (374, 180), (352, 196), (332, 188)])
    # UK dot
    draw.ellipse([ox + 198, oy + 56, ox + 204, oy + 62],
                 fill=LAND, outline=LAND_EDGE)

    markers = [
        (1, 322, 78),    # China — Shenzhou-24
        (2, 328, 136),   # Indonesia — West Java mine
        (3, 128, 132),   # Colombia — Cartagena rescue
        (4, 308, 100),   # Bangladesh — garment wage
        (5, 300, 48),    # Russia — Samara refineries
        (6, 380, 158),   # Solomon Islands — security treaty
        (7, 228, 60),    # Europe — Shein sales
    ]
    f = font(SANS_B, 11)
    for num, mx, my in markers:
        draw.ellipse([ox + mx - 10, oy + my - 10, ox + mx + 10, oy + my + 10],
                     fill=RED, outline=(255, 255, 255), width=2)
        tw = draw.textlength(str(num), font=f)
        draw.text((ox + mx - tw / 2, oy + my - 8), str(num),
                  font=f, fill=(255, 255, 255))


# ------------------------------------------------------------- featured ----
# (region tag, headline, one-line deck) — decks kept under ~110 chars.
FEATURED = [
    ("ASIA", "Shenzhou-24 launches, Pakistan's first astronaut",
     "Tang Hongbo and Wu Yi fly with Pakistan's Zeeshan Ali — the first "
     "foreign astronaut to visit China's station."),
    ("ASIA", "Three bodies found in flooded West Java gold mine",
     "Three bodies are recovered and 26 miners remain trapped in a flooded "
     "unauthorised gold mine."),
    ("LATIN AMERICA", "Cartagena hostage siege ends with all freed",
     "Security forces storm a supermarket after a day-long siege, freeing "
     "every hostage and killing one captor."),
    ("ASIA", "Bangladesh garment wage rises 36%",
     "Garment workers win a rise to 17,000 taka a month after weeks of "
     "violent protests over pay."),
    ("EUROPE", "Ukrainian drones strike Samara refineries",
     "Fires burn at Syzran and Kuibyshev, about 800 km inside Russia, as "
     "Kyiv hits the plants funding Moscow's war."),
    ("OCEANIA", "Australia signs Solomons security treaty",
     "The pact bars any foreign military base from Solomon Islands, backed "
     "by A$740m over ten years."),
    ("EUROPE", "Shein Europe sales sink 27.6%",
     "European revenue falls 27.6% to $2.98bn as the EU's €3 parcel fee "
     "bites the fast-fashion giant."),
]

# List items 8-36: (number, headline) grouped by region per column.
COLUMNS = [
    [("NORTH AMERICA", [
        (8, "Dow 50,183 (+0.33%); Nasdaq −0.62% at the close"),
        (16, "US PCE inflation +3.8%, core +3.3% YoY"),
        (17, "US Q3 GDP +4.3%, revised up from 3.4%"),
        (18, "Jobless claims 189,000; durable goods +0.2%"),
        (19, "Trump readies new tariffs — China 20%, maybe 40%"),
        (20, "Deere misses; FY2027 guidance $4.5–5.25bn"),
        (21, "Dell beats hugely, shares still fall 5–7%"),
    ]),
     ("EUROPE", [
        (12, "Germany Q3 GDP +0.1%, revised down"),
        (22, "Eurostar strike cancels London–Paris trains"),
        (23, "Merz defends Ukraine aid in Bundestag"),
     ])],
    [("EUROPE", [
        (25, "UK energy bills +26% from January, cap £2,166"),
        (26, "Two charged over Anmer Hall break-in"),
        (14, "Estonia FM Tsahkna arrives in Kyiv"),
     ]),
     ("ASIA-PACIFIC", [
        (9, "North Korea expels Swiss office head, 48h to leave"),
        (13, "Australia October CPI +4.9% y/y"),
        (15, "China pledges Mekong pollution help"),
        (27, "Malaysia Airlines orders 10 Boeing 787-10s"),
        (28, "Australia passes Digital Duty of Care Act"),
     ]),
     ("MIDDLE EAST", [
        (10, "Saudi coalition hits Hodeidah; Houthis threaten Jeddah"),
        (11, "Gaza strike kills a family of four in al-Shati"),
     ])],
    [("MIDDLE EAST", [
        (29, "Two tankers hit mines in Hormuz"),
        (35, "Iraq court: Baghdad may send troops to Kurdistan border"),
     ]),
     ("AFRICA", [
        (24, "Ramaphosa wins Phala Phala court battle"),
        (33, "Africa CDC + WHO launch $1.576bn Ebola plan"),
        (34, "Nollywood actor Pete Edochie dies at 79"),
     ]),
     ("LATIN AMERICA & SPACE", [
        (30, "Hera finds stadium-sized crater on Dimorphos"),
        (31, "Brazil raids R$2bn illegal iron-ore scheme"),
        (32, "Puerto Rico court voids LUMA grid contract 5–4"),
        (36, "NBA Cup: 76ers 111–104 Heat, LeBron triple-double"),
     ])],
]

STATS = [
    ("+3.8%", "US PCE inflation"),
    ("+4.3%", "US Q3 GDP"),
    ("50,183", "Dow close"),
    ("−0.62%", "Nasdaq"),
    ("+36%", "Garment wage"),
    ("+4.9%", "Australia CPI"),
]

TIMELINE = [
    ("00:18", "Shenzhou-24 launches from Jiuquan, carrying Pakistan's "
              "first astronaut"),
    ("02:00", "Bangladesh approves garment wage rise of 36% to 17,000 taka"),
    ("13:30", "US data: PCE +3.8%, core +3.3%; Q3 GDP +4.3%"),
    ("21:00", "Dow closes at 50,183 after erasing a ~1,100-point plunge"),
]


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 84], fill=TEAL)
    d.rectangle([0, 84, W, 86], fill=TEAL_DARK)
    f_mast = font(SERIF, 58)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_mast)
    d.text(((W - tw) / 2, 10), title, font=f_mast, fill=(255, 255, 255))

    # Date band
    d.rectangle([0, 86, W, 118], fill=(0, 0, 0))
    f_date = font(SANS_B, 19)
    date_line = "WEDNESDAY  25  NOVEMBER  2026      •      36 STORIES      •      7 REGIONS"
    tw = d.textlength(date_line, font=f_date)
    d.text(((W - tw) / 2, 92), date_line, font=f_date, fill=(255, 255, 255))

    # Stats strip
    y0, y1 = 124, 188
    box_w = (W - 32 - 5 * 8) / 6
    f_num = font(SANS_B, 25)
    f_lab = font(SANS, 10)
    for i, (num, lab) in enumerate(STATS):
        x0 = 16 + i * (box_w + 8)
        d.rectangle([x0, y0, x0 + box_w, y1], outline=INK, width=1,
                    fill=(255, 255, 255))
        nw = d.textlength(num, font=f_num)
        d.text((x0 + (box_w - nw) / 2, y0 + 6), num, font=f_num, fill=RED)
        lw = d.textlength(lab, font=f_lab)
        d.text((x0 + (box_w - lw) / 2, y0 + 40), lab, font=f_lab, fill=INK)

    # Featured + map section
    sec_y = 198
    f_sec = font(SANS_B, 13)
    d.text((16, sec_y), "TOP OF THE DAY", font=f_sec, fill=TEAL)
    d.line([(16, sec_y + 20), (600, sec_y + 20)], fill=INK, width=2)

    f_tag = font(SANS_B, 9)
    f_head = font(SERIF, 14)
    f_deck = font(SANS, 10)
    fy = sec_y + 30
    for i, (region, head, deck) in enumerate(FEATURED, start=1):
        tag_w = d.textlength(region, font=f_tag)
        d.text((16, fy + 3), region, font=f_tag, fill=TEAL)
        num_txt = f"{i}. "
        nx = 16 + tag_w + 8
        nw = d.textlength(num_txt, font=f_head)
        d.text((nx, fy), num_txt, font=f_head, fill=RED)
        d.text((nx + nw, fy), head, font=f_head, fill=INK)
        text_block(d, 16, fy + 19, deck, f_deck, (60, 58, 52), 584, 13,
                   max_lines=1)
        fy += 39
        if i < len(FEATURED):
            d.line([(16, fy - 3), (600, fy - 3)], fill=RULE, width=1)

    # Map panel
    mx = 612
    d.text((mx, sec_y), "WHERE IT HAPPENED", font=f_sec, fill=TEAL)
    d.text((mx + 250, sec_y + 2), "1–7 = top stories",
           font=font(SANS, 10), fill=GREY)
    d.line([(mx, sec_y + 20), (1008, sec_y + 20)], fill=INK, width=2)
    draw_map(d, mx, sec_y + 28, 396, 224)
    d.text((mx, sec_y + 258),
           "Markers match the seven top stories at left.",
           font=font(SANS, 10), fill=GREY)

    # Timeline strip
    ty = 508
    d.rectangle([16, ty, 1008, ty + 76], outline=INK, width=1,
                fill=(255, 255, 255))
    d.text((28, ty + 8), "WEDNESDAY IN UTC — when the news broke",
           font=f_sec, fill=TEAL)
    col_w = (1008 - 16 - 24) / 4
    f_time = font(SANS_B, 13)
    f_tl = font(SANS, 10)
    for i, (t, txt) in enumerate(TIMELINE):
        x0 = 28 + i * col_w
        d.text((x0, ty + 30), t, font=f_time, fill=RED)
        text_block(d, x0, ty + 48, txt, f_tl, INK, col_w - 16, 12,
                   max_lines=2)
        if i:
            d.line([(x0 - 8, ty + 30), (x0 - 8, ty + 68)], fill=RULE,
                   width=1)

    # List section
    ly = 594
    d.text((16, ly), "MORE FROM WEDNESDAY — STORIES 8 TO 36",
           font=f_sec, fill=TEAL)
    d.line([(16, ly + 20), (1008, ly + 20)], fill=INK, width=2)
    col_xs = [16, 360, 704]
    col_ws = [328, 328, 304]
    f_rh = font(SANS_B, 10)
    f_item = font(SANS, 11)
    f_num2 = font(SANS_B, 11)
    for ci, groups in enumerate(COLUMNS):
        x0 = col_xs[ci]
        cw = col_ws[ci]
        y = ly + 30
        for region, items in groups:
            d.text((x0, y), region, font=f_rh, fill=TEAL)
            y += 17
            for num, head in items:
                num_txt = f"{num}. "
                nw = d.textlength(num_txt, font=f_num2)
                d.text((x0, y), num_txt, font=f_num2, fill=RED)
                lines = wrap(d, head, f_item, cw - nw)
                yy = y
                for line in lines[:2]:
                    d.text((x0 + nw, yy), line, font=f_item, fill=INK)
                    yy += 14
                y = yy + 6
            y += 5

    # Bottom note line
    ny = 946
    d.text((16, ny),
           "Thursday: US markets shut for Thanksgiving; the Fed's next "
           "decision is due 9 December.",
           font=font(SANS, 10), fill=GREY)

    # Footer
    fy = 964
    d.rectangle([16, fy, 620, fy + 44], fill=GOLD, outline=INK, width=1)
    f_dc = font(SANS_B, 11)
    d.text((26, fy + 4), "DATE CHECK", font=f_dc, fill=INK)
    text_block(d, 26, fy + 19,
               "Every story on this page was verified as Wednesday 25 "
               "November 2026. Stories from Tuesday 24 November or earlier "
               "were checked and left out.",
               font(SANS, 10), INK, 580, 11, max_lines=2)
    f_cr = font(SANS, 10)
    d.text((636, fy + 4), "Compiled from verified reports", font=f_cr,
           fill=GREY)
    d.text((636, fy + 19), "Wednesday 25 November 2026", font=f_cr,
           fill=GREY)
    d.text((636, fy + 34), "make.fun bounty news-image-20261125",
           font=f_cr, fill=GREY)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG")
    print("wrote", out)


if __name__ == "__main__":
    build()
