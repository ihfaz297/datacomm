"""Draws the pole-zero and stability figures used in 21-T2-ztransform.md into figs/*.svg.

Colours are the phone page's CSS variables with light-theme fallbacks, so the same file
works as an <img> in the VS Code preview and inlined (theme-aware) in mid2-notes.html.
Run:  python DSP/study/_make_pz_figs.py
"""
import cmath
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figs")

INK = "var(--ink, #18212e)"
SOFT = "var(--ink-soft, #505b6b)"
RULE = "var(--rule, #c9d1db)"
TRACE = "var(--trace, #17698a)"
NOTE = "var(--note, #8a5800)"
SHEET = "var(--sheet, #ffffff)"
OK = "var(--ok, #1d7a4a)"
BAD = "var(--bad, #b3261e)"
FONT = "font-family:var(--f-ui, 'IBM Plex Sans', 'Segoe UI', sans-serif)"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=12, fill=INK, anchor="start", weight=400):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" style="fill:{fill}">{s}</text>')


def label_box(x, y, s, size=12):
    w = len(s) * size * 0.56 + 12
    return (f'<rect x="{x:.1f}" y="{y - size - 4:.1f}" width="{w:.1f}" height="{size + 9:.1f}" rx="4" '
            f'style="fill:{SHEET};fill-opacity:0.92;stroke:{RULE}"/>' + text(x + 6, y, esc(s), size))


def svg(name, w, h, body, label):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
           f'role="img" aria-label="{esc(label)}" style="{FONT}">\n'
           f'<rect width="{w}" height="{h}" rx="8" style="fill:{SHEET}"/>\n{body}\n</svg>\n')
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(doc)


class Plane:
    def __init__(self, uid, cx, cy, half_px, half_units):
        self.uid, self.cx, self.cy, self.h = uid, cx, cy, half_px
        self.s = half_px / half_units

    def xy(self, z):
        return self.cx + z.real * self.s, self.cy - z.imag * self.s

    def circle_path(self, r):
        R, cx, cy = r * self.s, self.cx, self.cy
        return (f"M{cx + R:.2f} {cy:.2f}A{R:.2f} {R:.2f} 0 1 0 {cx - R:.2f} {cy:.2f}"
                f"A{R:.2f} {R:.2f} 0 1 0 {cx + R:.2f} {cy:.2f}Z")

    def clip(self):
        x0, y0, w = self.cx - self.h, self.cy - self.h, 2 * self.h
        return f'<clipPath id="{self.uid}"><rect x="{x0}" y="{y0}" width="{w}" height="{w}"/></clipPath>'

    def roc(self, kind, r1=0.0, r2=0.0):
        x0, y0, w = self.cx - self.h, self.cy - self.h, 2 * self.h
        rect = f"M{x0} {y0}h{w}v{w}h{-w}Z"
        d = {"outside": rect + self.circle_path(r1),
             "inside": self.circle_path(r1),
             "ring": self.circle_path(r2) + self.circle_path(r1),
             "all": rect}[kind]
        return (f'<path d="{d}" fill-rule="evenodd" clip-path="url(#{self.uid})" '
                f'style="fill:{TRACE};fill-opacity:0.17"/>')

    def edge(self, r):
        return (f'<path d="{self.circle_path(r)}" clip-path="url(#{self.uid})" '
                f'style="fill:none;stroke:{TRACE};stroke-width:1.3"/>')

    def guide(self, r):
        return (f'<path d="{self.circle_path(r)}" style="fill:none;stroke:{SOFT};stroke-width:0.8;'
                f'stroke-dasharray:1.5 3"/>')

    def axes(self, labels=True):
        x0, x1, y0, y1 = self.cx - self.h, self.cx + self.h, self.cy - self.h, self.cy + self.h
        out = (f'<line x1="{x0}" y1="{self.cy}" x2="{x1}" y2="{self.cy}" style="stroke:{SOFT};stroke-width:0.8"/>'
               f'<line x1="{self.cx}" y1="{y0}" x2="{self.cx}" y2="{y1}" style="stroke:{SOFT};stroke-width:0.8"/>')
        if labels:
            out += text(x1 - 3, self.cy - 6, "Re", 11, SOFT, "end") + text(self.cx + 6, y0 + 13, "Im", 11, SOFT)
        return out

    def unit_circle(self, label_deg=None):
        out = (f'<path d="{self.circle_path(1)}" clip-path="url(#{self.uid})" style="fill:none;stroke:{INK};'
               f'stroke-width:1.1;stroke-dasharray:5 3.5;opacity:0.75"/>')
        if label_deg is not None:
            a = math.radians(label_deg)
            x, y = self.xy(cmath.rect(1.0, a))
            out += text(x + 5, y + 14, "|z| = 1", 11, SOFT)
        return out

    def pole(self, z, size=5.5):
        x, y = self.xy(z)
        return (f'<path d="M{x - size:.1f} {y - size:.1f}L{x + size:.1f} {y + size:.1f}M{x + size:.1f} {y - size:.1f}'
                f'L{x - size:.1f} {y + size:.1f}" style="stroke:{INK};stroke-width:2.2;stroke-linecap:round"/>')

    def zero(self, z, r=5.0, faded=False):
        x, y = self.xy(z)
        extra = ";stroke-dasharray:2 2;opacity:0.6" if faded else ""
        return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{SHEET};stroke:{NOTE};'
                f'stroke-width:2{extra}"/>')

    def at(self, z, dx, dy, s, size=11, anchor="middle", fill=INK):
        x, y = self.xy(z)
        return text(x + dx, y + dy, esc(s), size, fill, anchor)


def fig_single(name, kind, a, label, alt, b=None):
    p = Plane(name, 140, 140, 122, 1.8 if b else 1.5)
    parts = [p.clip()]
    if kind == "ring":
        parts += [p.roc("ring", a, b), p.edge(a), p.edge(b)]
    else:
        parts += [p.roc(kind, a), p.edge(a)]
    parts += [p.axes(), p.unit_circle(-48 if kind != "inside" else -40), p.zero(0), p.pole(a), p.at(a, 0, 20, "a")]
    if b:
        parts += [p.pole(b), p.at(b, 0, 20, "b")]
    parts.append(label_box(14, 32, label))
    svg(name, 280, 280, "\n".join(parts), alt)


def fig_note32():
    p = Plane("pz-note32", 140, 140, 122, 1.3)
    r = abs(0.25 + 0.75j)
    parts = [p.clip(), p.roc("outside", r), p.edge(r), p.axes(), p.unit_circle(-40)]
    for z in (0, 0.5 + 0.5j, 0.5 - 0.5j):
        parts.append(p.zero(z))
    for z in (-0.5, 0.25 + 0.75j, 0.25 - 0.75j):
        parts.append(p.pole(z))
    parts += [p.at(-0.5, 0, 20, "−0.5"),
              p.at(0.25 + 0.75j, 9, -6, "0.25 ± 0.75j", anchor="start"),
              p.at(0.5 + 0.5j, 9, 4, "0.5 ± 0.5j", anchor="start", fill=NOTE),
              label_box(14, 32, "causal ROC: |z| > 0.79")]
    svg("pz-note32", 280, 280, "\n".join(parts),
        "Pole-zero plot: zeros at 0 and 0.5 plus or minus 0.5j, poles at minus 0.5 and 0.25 plus or minus 0.75j, ROC outside radius 0.79")


def fig_finite8():
    a, M = 0.8, 8
    p = Plane("pz-finite8", 140, 140, 122, 1.3)
    parts = [p.clip(), p.roc("all"), p.axes(), p.unit_circle(-62), p.guide(a)]
    for k in range(1, M):
        parts.append(p.zero(cmath.rect(a, 2 * math.pi * k / M)))
    parts += [p.zero(a, faded=True), p.at(a, 0, 20, "cancelled", 10, fill=SOFT),
              p.pole(0), p.at(0, 13, -9, "(7)", 12, "start"),
              label_box(14, 32, "ROC: |z| > 0")]
    svg("pz-finite8", 280, 280, "\n".join(parts),
        "Pole-zero plot for a to the n, n from 0 to 7: seven zeros on a circle of radius a, the eighth cancelled, seven poles at the origin")


def stems(x0, x1, top, bottom, vmin, vmax, values, n0=0):
    """Stem plot of values[i] at n = n0 + i, clipped to [vmin, vmax] with arrow heads."""
    out = []
    span = vmax - vmin
    ymap = lambda v: top + (vmax - v) / span * (bottom - top)
    yb = ymap(0)
    out.append(f'<line x1="{x0 - 6}" y1="{yb:.1f}" x2="{x1 + 6}" y2="{yb:.1f}" style="stroke:{SOFT};stroke-width:0.8"/>')
    dx = (x1 - x0) / (len(values) - 1)
    for i, v in enumerate(values):
        x = x0 + i * dx
        clipped = v > vmax or v < vmin
        vd = min(max(v, vmin), vmax)
        y = ymap(vd)
        if abs(v) > 1e-9:
            out.append(f'<line x1="{x:.1f}" y1="{yb:.1f}" x2="{x:.1f}" y2="{y:.1f}" style="stroke:{TRACE};stroke-width:1.4"/>')
        if clipped:
            s = 1 if v > 0 else -1  # arrow points up when the value runs off the top
            out.append(f'<path d="M{x - 3.8:.1f} {y + s * 5:.1f}L{x + 3.8:.1f} {y + s * 5:.1f}L{x:.1f} {y - s * 1.5:.1f}Z" '
                       f'style="fill:{BAD}"/>')
        else:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" style="fill:{TRACE}"/>')
    return "".join(out)


def fig_poles_hn():
    W, rowh, pad = 420, 112, 8
    rows = [
        ("Pole at 0.5", "stable: dies out", OK, [0.5], lambda n: 0.5 ** n),
        ("Pole at −0.5", "stable: dies out, flipping sign", OK, [-0.5], lambda n: (-0.5) ** n),
        ("Pole at 0.9", "stable: dies out slowly", OK, [0.9], lambda n: 0.9 ** n),
        ("Pole at 1", "not stable: never dies", BAD, [1.0], lambda n: 1.0),
        ("Pole at 1.15", "unstable: grows", BAD, [1.15], lambda n: 1.15 ** n),
        ("Poles 0.85e^±jπ/4", "stable: rings, dies out", OK,
         [cmath.rect(0.85, math.pi / 4), cmath.rect(0.85, -math.pi / 4)],
         lambda n: 0.85 ** n * math.cos(math.pi * n / 4)),
    ]
    parts = []
    for i, (title, verdict, colour, poles, h) in enumerate(rows):
        y0 = pad + i * rowh
        p = Plane(f"poles-hn-{i}", 56, y0 + 56, 44, 1.35)
        parts += [f'<rect x="{p.cx - p.h}" y="{p.cy - p.h}" width="{2 * p.h}" height="{2 * p.h}" rx="4" '
                  f'style="fill:none;stroke:{RULE}"/>', p.clip(), p.axes(False), p.unit_circle()]
        parts += [p.pole(z, 4.5) for z in poles]
        if "^" in title:
            head, sup = title.split("^")
            t = f'<tspan font-weight="600">{esc(head)}<tspan dy="-5" font-size="9.5">{esc(sup)}</tspan></tspan>'
            v = f'<tspan dy="5" style="fill:{colour}">  {esc(verdict)}</tspan>'
        else:
            t = f'<tspan font-weight="600">{esc(title)}</tspan>'
            v = f'<tspan style="fill:{colour}">  {esc(verdict)}</tspan>'
        parts.append(f'<text x="118" y="{y0 + 20}" font-size="12.5" style="fill:{INK}">{t}{v}</text>')
        parts.append(stems(126, 404, y0 + 32, y0 + 104, -1.2, 1.6, [h(n) for n in range(16)]))
        if i == 0:
            parts.append(text(404, y0 + 76, "n", 10.5, SOFT, "end"))
        if i < len(rows) - 1:
            parts.append(f'<line x1="12" y1="{y0 + rowh - 2}" x2="{W - 12}" y2="{y0 + rowh - 2}" style="stroke:{RULE}"/>')
    svg("poles-hn", W, pad * 2 + rowh * len(rows) - 4, "\n".join(parts),
        "Six pole positions and the impulse responses they produce: inside the unit circle the response dies out, on it it never dies, outside it grows")


def fig_three_roc():
    W, rowh, pad = 420, 176, 8
    rows = [
        ("outside", "ROC |z| > 2", "causal (right-sided)", "misses the unit circle: unstable", BAD),
        ("ring", "ROC 0.5 < |z| < 2", "two-sided", "contains the unit circle: stable", OK),
        ("inside", "ROC |z| < 0.5", "anti-causal (left-sided)", "misses the unit circle: unstable", BAD),
    ]
    parts = []
    for i, (kind, roc, side, verdict, colour) in enumerate(rows):
        y0 = pad + i * rowh
        p = Plane(f"three-roc-{i}", 92, y0 + 84, 78, 2.5)
        parts.append(p.clip())
        if kind == "outside":
            parts.append(p.roc("outside", 2))
        elif kind == "ring":
            parts.append(p.roc("ring", 0.5, 2))
        else:
            parts.append(p.roc("inside", 0.5))
        parts += [p.edge(0.5), p.edge(2), p.axes(False), p.unit_circle(), p.zero(0, 4.5),
                  p.at(0, -9, -8, "(2)", 10, "end", NOTE),
                  p.pole(0.5, 4.5), p.pole(2, 4.5), p.at(2, 0, 18, "2", 10.5), p.at(0.5, 2, 18, "0.5", 10.5)]
        parts += [text(196, y0 + 62, esc(roc), 14, INK, weight=600),
                  text(196, y0 + 84, esc(side), 13, SOFT),
                  text(196, y0 + 110, esc(verdict), 13, colour, weight=600)]
        if i < len(rows) - 1:
            parts.append(f'<line x1="12" y1="{y0 + rowh - 2}" x2="{W - 12}" y2="{y0 + rowh - 2}" style="stroke:{RULE}"/>')
    svg("stab-three-roc", W, pad * 2 + rowh * len(rows) - 4, "\n".join(parts),
        "The same H(z) with poles at 0.5 and 2 and three possible ROCs; only the ring contains the unit circle and is stable")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    fig_single("pz-causal", "outside", 0.6, "ROC: |z| > |a|", "Pole-zero plot of a to the n u of n: zero at the origin, pole at a, ROC outside the circle through a")
    fig_single("pz-anticausal", "inside", 0.6, "ROC: |z| < |a|", "Same poles and zeros, ROC inside the circle through a")
    fig_single("pz-twosided", "ring", 0.5, "ROC: |a| < |z| < |b|", "Poles at a and b, zero at the origin, ROC the ring between them", b=1.5)
    fig_note32()
    fig_finite8()
    fig_poles_hn()
    fig_three_roc()
    print("wrote", sorted(os.listdir(OUT)))
