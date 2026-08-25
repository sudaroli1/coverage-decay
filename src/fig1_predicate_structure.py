r"""
Figure 1 — how an exclusion is added, and what each form does to rule structure.

Deterministic: no data input, no randomness. Drawn from the certutil rule shown in
Listing 1 so the figure and the listing are continuous.

The point the figure has to carry, because §4.2 and §5.2 both depend on it:
a list-valued field is ONE predicate holding many literals, so appending a literal
narrows the matched set while leaving structure — predicate count, condition line —
exactly as it was. That is the 31% a structural diff cannot see.

Writes results/fig1_predicate_structure.{svg,pdf,png}

Run:  python src/fig1_predicate_structure.py
"""

import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
R = ROOT / "results"
NAME = "fig1_predicate_structure"

W, H = 720, 470
MONO = "DejaVu Sans Mono, Consolas, monospace"
SANS = "Arial, Helvetica, DejaVu Sans, sans-serif"

INK = "#1a1a1a"
MUTED = "#6b6b6b"
FAINT = "#9a9a9a"
BAND = "#e9e9e9"      # diff highlight
BOX = "#c9c9c9"       # box border
KEEP = "#4a4a4a"      # retained matched set


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def mono(x, y, s, fill=INK, size=9.3, weight="normal"):
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" xml:space="preserve">{esc(s)}</text>')


def sans(x, y, s, fill=INK, size=9, weight="normal", anchor="start", style="normal"):
    return (f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" '
            f'font-style="{style}">{esc(s)}</text>')


def rect(x, y, w, h, fill="none", stroke="none", sw=0.8, dash=None, rx=2):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


# ── panel geometry ────────────────────────────────────────────────────────────
BX, BW = 46, 424                 # rule-text box
GX, GW = 502, 186                # matched-set glyph
LH = 15.5                        # mono line height

PANELS = [
    dict(tag="v1", top=44, lines=[
        ("  ", "detection:"),
        ("  ", "  selection_img:"),
        ("  ", "    - Image|endswith: '\\certutil.exe'", "P1"),
        ("  ", "    - OriginalFileName: 'CertUtil.exe'", "P2"),
        ("  ", "  selection_cli:"),
        ("  ", "    CommandLine|contains: '-encode'", "P3"),
        ("  ", "  condition: all of selection_*"),
    ], note="3 predicates · 3 literals",
        verdict=None,
        glyph=dict(keep=186, new=0, old=0,
                   above="M₁ — records that raise an alert",
                   below=None)),

    dict(tag="v2", top=210, lines=[
        ("+ ", "  filter_installer:", None, True),
        ("+ ", "    ParentImage|endswith: '\\ccmexec.exe'", "P4", True),
        ("− ", "  condition: all of selection_*", None, True),
        ("+ ", "  condition: all of selection_* and not filter_installer", None, True),
    ], note="4 predicates · 4 literals — the condition line changes",
        verdict="visible to structural diffing",
        glyph=dict(keep=150, new=36, old=0,
                   above="M₂ — strictly narrower than M₁",
                   below="a new predicate removes a slice")),

    dict(tag="v3", top=318, lines=[
        ("  ", "  filter_installer:"),
        ("  ", "    ParentImage|endswith:"),
        ("  ", "      - '\\ccmexec.exe'"),
        ("+ ", "      - '\\SenseIR.exe'", None, True),
        ("  ", "  condition: all of selection_* and not filter_installer"),
    ], note="4 predicates · 5 literals — nothing structural moves",
        verdict="invisible to structural diffing",
        glyph=dict(keep=122, new=28, old=36,
                   above="M₃ — strictly narrower than M₂",
                   below="the slice grew; the structure did not")),
]


def build():
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" font-family="{SANS}">')
    o.append(f'<rect width="{W}" height="{H}" fill="white"/>')
    o.append('<defs>'
             '<pattern id="hatch" width="5" height="5" patternUnits="userSpaceOnUse" '
             'patternTransform="rotate(45)">'
             '<rect width="5" height="5" fill="white"/>'
             '<line x1="0" y1="0" x2="0" y2="5" stroke="#b0b0b0" stroke-width="1.1"/>'
             '</pattern></defs>')

    # column headers
    o.append(sans(BX, 24, "rule text and predicate structure", MUTED, 8.6))
    o.append(sans(GX, 24, "records the rule matches", MUTED, 8.6))
    o.append(f'<line x1="{BX}" y1="30" x2="{W-32}" y2="30" '
             f'stroke="{BOX}" stroke-width="0.8"/>')

    for i, p in enumerate(PANELS):
        top = p["top"]
        n = len(p["lines"])
        bh = n * LH + 14
        o.append(rect(BX, top, BW, bh, "none", BOX, 0.8))

        # version tag in the left margin
        o.append(sans(BX - 8, top + 14, p["tag"], INK, 9.5, "bold", "end"))

        # arrow from the panel above
        if i:
            prev = PANELS[i - 1]
            py = prev["top"] + len(prev["lines"]) * LH + 14
            o.append(f'<line x1="{BX+18}" y1="{py+16}" x2="{BX+18}" y2="{top-4}" '
                     f'stroke="{FAINT}" stroke-width="0.9"/>')
            o.append(f'<path d="M {BX+18} {top-1} l -3 -5 l 6 0 z" fill="{FAINT}"/>')

        y = top + 16
        for ln in p["lines"]:
            gut, txt = ln[0], ln[1]
            tag = ln[2] if len(ln) > 2 else None
            hl = ln[3] if len(ln) > 3 else False
            if hl:
                o.append(rect(BX + 3, y - 11, BW - 6, LH - 1.5, BAND, "none", rx=1))
            o.append(mono(BX + 8, y, gut, INK if gut.strip() else MUTED,
                          9.3, "bold" if gut.strip() else "normal"))
            o.append(mono(BX + 22, y, txt))
            if tag:
                o.append(sans(BX + BW - 10, y, tag, MUTED, 8.2, "bold", "end"))
            y += LH

        o.append(sans(BX, top + bh + 15, p["note"], MUTED, 8.6))

        # ── matched-set glyph ────────────────────────────────────────────────
        g = p["glyph"]
        cy = top + bh / 2
        by, bhh = cy - 11, 22
        o.append(sans(GX, by - 8, g["above"], INK, 8.6, "bold"))

        x = GX
        o.append(rect(x, by, g["keep"], bhh, KEEP, "none", rx=1.5))
        x += g["keep"]
        if g["old"]:
            o.append(rect(x, by, g["old"], bhh, "url(#hatch)", FAINT, 0.7,
                          dash="2.5,2", rx=1.5))
            x += g["old"]
        if g["new"]:
            o.append(rect(x, by, g["new"], bhh, "url(#hatch)", INK, 1.0, rx=1.5))
            x += g["new"]

        if g["below"]:
            o.append(sans(GX, by + bhh + 13, g["below"], MUTED, 8.2))
        if p["verdict"]:
            bold = "bold" if "invisible" in p["verdict"] else "normal"
            o.append(sans(GX, by + bhh + 26, p["verdict"], INK, 8.6, bold))

    # footer rule, then key and takeaway on one baseline
    fy = H - 26
    o.append(f'<line x1="{BX}" y1="{fy-12}" x2="{W-32}" y2="{fy-12}" '
             f'stroke="{BOX}" stroke-width="0.8"/>')

    o.append(rect(GX, fy - 8, 11, 10, KEEP, "none", rx=1))
    o.append(sans(GX + 16, fy, "still alerts", MUTED, 8))
    o.append(rect(GX + 78, fy - 8, 11, 10, "url(#hatch)", FAINT, 0.7, rx=1))
    o.append(sans(GX + 94, fy, "suppressed", MUTED, 8))

    o.append(sans(BX, fy,
                  "one predicate, many literals: appending to a list narrows the "
                  "matched set without changing the structure",
                  FAINT, 8, style="italic"))
    o.append("</svg>")
    return "\n".join(o)


def main():
    R.mkdir(exist_ok=True)
    svg = R / f"{NAME}.svg"
    svg.write_text(build(), encoding="utf-8")
    print(f"  wrote {svg.name}")
    try:
        import cairosvg
        cairosvg.svg2pdf(url=str(svg), write_to=str(R / f"{NAME}.pdf"))
        cairosvg.svg2png(url=str(svg), write_to=str(R / f"{NAME}.png"), scale=4.17)
        print(f"  wrote {NAME}.pdf, {NAME}.png")
    except ImportError:
        for fmt in ("pdf", "png"):
            subprocess.run(["rsvg-convert", "-f", fmt, "-o",
                            str(R / f"{NAME}.{fmt}"), str(svg)], check=False)


if __name__ == "__main__":
    main()
