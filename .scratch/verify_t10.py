"""Every numeric claim in DSP/study/10-dtft-worked-tutorial.md, re-derived from scratch.

Run:  python .scratch/verify_t10.py
Prints one PASS/FAIL line per claim.  Anything that FAILs is a real error in the markdown.
"""
import os

import numpy as np

FAILS = []


def chk(tag, got, want, tol=5e-5):
    got, want = complex(got), complex(want)
    err = max(abs(got.real - want.real), abs(got.imag - want.imag))
    ok = err <= tol
    if not ok:
        FAILS.append(tag)
    print(f"{'PASS' if ok else 'FAIL'}  {tag:52s} got {got.real:+.5f}{got.imag:+.5f}j  "
          f"want {want.real:+.5f}{want.imag:+.5f}j  err {err:.1e}")


def chka(tag, got, want, tol=0.01):
    """Angle comparison: +180 and -180 are the same angle, so wrap the difference."""
    d = (float(got) - float(want) + 180.0) % 360.0 - 180.0
    ok = abs(d) <= tol
    if not ok:
        FAILS.append(tag)
    print(f"{'PASS' if ok else 'FAIL'}  {tag:52s} got {float(got):+9.4f} deg  "
          f"want {float(want):+9.4f} deg  diff {d:+.2e}")


def sdtft(x, w, n=None):
    x = np.asarray(x, dtype=float)
    n = np.arange(len(x)) if n is None else np.asarray(n)
    return np.exp(-1j * np.outer(w, n)) @ x


def ma_H(M, ww):
    ww = np.atleast_1d(np.asarray(ww, dtype=float))
    with np.errstate(divide="ignore", invalid="ignore"):
        h = np.sin(ww * M / 2) / (M * np.sin(ww / 2)) * np.exp(-1j * ww * (M - 1) / 2)
    h[np.isclose(ww % (2 * np.pi), 0.0)] = 1.0 + 0j
    return h


print("=== S1 the DTFT one-liner (definition, all-n sum) ===")
x123 = np.array([1, 2, 3.0])
for wi in (0.0, np.pi / 2, np.pi, 1.234):
    brute = sum(x123[n] * np.exp(-1j * wi * n) for n in range(3))
    chk(f"S1 outer-product DTFT at w={wi:.3f}", sdtft(x123, [wi])[0], brute, 1e-12)

print("\n=== S2 x[n] = {1,2,3}: X at 0, pi/2, pi ===")
chk("S2 X(0)", sdtft(x123, [0.0])[0], 6)
chk("S2 X(pi/2)", sdtft(x123, [np.pi / 2])[0], -2 - 2j)
chk("S2 X(pi)", sdtft(x123, [np.pi])[0], 2)
for tag, wi, want in (("S2 |X(0)|", 0.0, 6), ("S2 |X(pi/2)|", np.pi / 2, 2.828),
                      ("S2 |X(pi)|", np.pi, 2)):
    chk(tag, abs(sdtft(x123, [wi])[0]), want, 5e-4)
chk("S2 angle X(pi/2) deg", np.degrees(np.angle(sdtft(x123, [np.pi / 2])[0])), -135, 5e-3)

print("\n=== S3 (a) causal geometric pair, a = 0.5 ===")
a = 0.5
w = np.array([0.0, np.pi / 4, np.pi / 2, np.pi])
n_exp = np.arange(0, 400)
clo = 1 / (1 - a * np.exp(-1j * w))
chk("S3a max |direct sum - 1/(1-a e^-jw)|", np.abs(sdtft(a ** n_exp, w, n_exp) - clo).max(), 0, 1e-9)
chk("S3 magnitude formula max err",
    np.abs(np.abs(clo) - 1 / np.sqrt(1 - 2 * a * np.cos(w) + a ** 2)).max(), 0, 1e-12)

print("\n=== S3 (b) finite geometric series ===")
for M in (5, 7):
    for av in (0.5, 1.0, -0.3):
        ws = w if av != 1.0 else w[w > 0]          # a = 1 at w = 0 is 0/0; checked separately below
        closed = (1 - av ** M * np.exp(-1j * ws * M)) / (1 - av * np.exp(-1j * ws))
        chk(f"S3b a={av}, M={M} max err", np.abs(closed - sdtft(av ** np.arange(M), ws)).max(), 0, 1e-12)
    wtiny = np.array([1e-9])
    chk(f"S3b a=1, M={M}: 0/0 at w=0 has limit M",
        ((1 - np.exp(-1j * wtiny * M)) / (1 - np.exp(-1j * wtiny)))[0], M, 1e-2)

print("\n=== S4 a = 0.5: X, |X|, angle at 0, pi/4, pi/2, pi ===")
X4 = 1 / (1 - 0.5 * np.exp(-1j * w))
for tag, v, want in (("S4 X(0)", X4[0], 2.0000), ("S4 X(pi/4)", X4[1], 1.1907 - 0.6512j),
                     ("S4 X(pi/2)", X4[2], 0.8000 - 0.4000j), ("S4 X(pi)", X4[3], 0.6667)):
    chk(tag, v, want, 5e-5)
for tag, v, want in (("S4 |X(0)|", X4[0], 2.0000), ("S4 |X(pi/4)|", X4[1], 1.3572),
                     ("S4 |X(pi/2)|", X4[2], 0.8944), ("S4 |X(pi)|", X4[3], 0.6667)):
    chk(tag, abs(v), want, 5e-5)
for tag, v, want in (("S4 ang X(0) deg", X4[0], 0), ("S4 ang X(pi/4) deg", X4[1], -28.7),
                     ("S4 ang X(pi/2) deg", X4[2], -26.6), ("S4 ang X(pi) deg", X4[3], 0)):
    chk(tag, np.degrees(np.angle(v)), want, 5e-2)
chk("S4 phase formula -atan(a sin w/(1-a cos w))",
    np.degrees(-np.arctan(0.5 * np.sin(np.pi / 4) / (1 - 0.5 * np.cos(np.pi / 4)))),
    np.degrees(np.angle(X4[1])), 1e-9)

print("\n=== S5 finite length a=0.5, M=5 ===")
M5, a5 = 5, 0.5
Y5 = (1 - a5 ** M5 * np.exp(-1j * w * M5)) / (1 - a5 * np.exp(-1j * w))
chk("S5 Y(0) = 1.9375", Y5[0], 1.9375)
chk("S5 Y(0) = plain sample sum", Y5[0], sum(a5 ** k for k in range(5)), 1e-12)
grid = np.linspace(0, np.pi, 2000001)
Yg = np.abs((1 - a5 ** M5 * np.exp(-1j * grid * M5)) / (1 - a5 * np.exp(-1j * grid)))
chk("S5 fix guard: min |Y| MUST be > 0 for a = 0.5", 1.0 if Yg.min() > 1e-6 else 0.0, 1, 1e-12)
print(f"      -> the OLD wording ('|Y| now has nulls ... w = 2pi k/M') was wrong: min |Y| = "
      f"{Yg.min():.6f}, numerator floor 1-a^M = {1 - a5 ** M5:.6f}")
print(f"      -> TRUE: min |Y| for a=0.5 is {Yg.min():.6f}; numerator floor is 1-a^M = "
      f"{1 - a5 ** M5:.6f}, so it NEVER reaches zero")
print(f"      -> flat a=1 case: min |Y| = {np.abs(sdtft(np.ones(5), grid)).min():.2e}, "
      f"nulls at k*2pi/5 = {2 * np.pi / 5:.6f}")


print("\n=== S6 5-point moving average ===")
w6 = np.array([0.0, np.pi / 5, 2 * np.pi / 5, np.pi / 2, np.pi])
H6 = ma_H(5, w6)
chk("S6 H(0)", H6[0], 1)
chk("S6 H(pi/5)", H6[1], 0.200 - 0.616j, 1e-3)
chk("S6 H(2pi/5) = 0", H6[2], 0, 1e-12)
chk("S6 H(pi/2)", H6[3], +0.2, 1e-9)
chk("S6 H(pi)", H6[4], +0.2, 1e-9)
chk("S6 |H(pi/5)|", abs(H6[1]), 0.6472, 1e-4)
chk("S6 |H(pi/2)|", abs(H6[3]), 0.2, 1e-9)
chk("S6 |H(pi)|", abs(H6[4]), 0.2, 1e-9)
chk("S6 ang H(pi/5) deg", np.degrees(np.angle(H6[1])), -72, 5e-3)
chk("S6 ang H(pi/2) deg", np.degrees(np.angle(H6[3])), 0, 1e-9)
chk("S6 ang H(pi) deg", np.degrees(np.angle(H6[4])), 0, 1e-9)
wfine = np.linspace(0.01, np.pi, 999)
chk("S6 MA closed form == DTFT of h[n]=1/5",
    np.abs(ma_H(5, wfine) - sdtft(np.ones(5) / 5, wfine)).max(), 0, 1e-12)
wg = np.linspace(0, np.pi, 200001)
chk("S6 first null = 2pi/5 = 0.4pi", wg[np.argmin(np.abs(ma_H(5, wg))[1:]) + 1], 2 * np.pi / 5, 2e-3)
mask = wg > 2 * np.pi / 5 + 1e-3
sl = 20 * np.log10(np.abs(ma_H(5, wg[mask])).max())
print(f"      -> 5-pt MA highest sidelobe = {sl:.2f} dB (doc says 'about 13 dB down'; "
      f"asymptotic rect window = -13.26 dB)")
ph = np.angle(ma_H(5, np.array([0.1, 0.3])))
chk("S6 delay = -(dphi/dw) = (M-1)/2 = 2", -(ph[1] - ph[0]) / 0.2, 2, 1e-9)

print("\n=== S7 h = {-3,6,-5,4}, x = A cos(w0 n) ===")
hh = np.array([-3, 6, -5, 4.0])
for tag, w0, want, amag, adeg in (("S7 w0=pi/2 H", np.pi / 2, 2 - 2j, 2.828, -45.0),
                                  ("S7 w0=pi/4 H", np.pi / 4, -1.5858 - 2.0711j, 2.6085, -127.44),
                                  ("S7 w0=pi H", np.pi, -18, 18, 180.0)):
    Hv = sum(hh[n] * np.exp(-1j * w0 * n) for n in range(4))
    chk(tag, Hv, want, 5e-5)
    chk(tag + " |H|", abs(Hv), amag, 1e-3)
    chka(tag + " angle deg", np.degrees(np.angle(Hv)), adeg, 1e-2)

print("\n=== S8 y(n) = 0.5 y(n-1) + 2 x(n), x = cos(pi n/2) u[n] ===")
H8 = 2 / (1 - 0.5 * np.exp(-1j * np.pi / 2))
chk("S8 H(pi/2) = 1.6-0.8j", H8, 1.6 - 0.8j)
chk("S8 |H(pi/2)| = 1.7889", abs(H8), 1.7889, 5e-5)
chk("S8 angle = -26.565 deg", np.degrees(np.angle(H8)), -26.565, 5e-3)
chk("S8 DC gain H(0) = 4", 2 / (1 - 0.5), 4)
chk("S8 0.5^10 ~ 0.001", 0.5 ** 10, 0.001, 1e-4)
chk("S8 analytic h[n] DTFT == closed form",
    abs(sdtft(np.array([2 * 0.5 ** n for n in range(60)]), [np.pi / 2])[0] - H8), 0, 1e-12)
Ns = 80
yy = np.zeros(Ns)
xx = np.cos(np.pi * np.arange(Ns) / 2)
for n in range(1, Ns):
    yy[n] = 0.5 * yy[n - 1] + 2 * xx[n]
ss = abs(H8) * np.cos(np.pi * np.arange(Ns) / 2 + np.angle(H8))
print(f"      -> recursion vs quoted steady state: max err first 10 = "
      f"{np.abs(yy[:10] - ss[:10]).max():.4f}, last 10 = {np.abs(yy[-10:] - ss[-10:]).max():.5f}")

print("\n=== S9 Parseval ===")
al = 0.6
tt = np.linspace(0, 60, 600001)
chk("S9 CT time energy 1/(2a)", np.trapezoid(np.exp(-2 * al * tt), tt), 1 / (2 * al), 1e-4)
chk("S9 1/(2a) = 0.8333", 1 / (2 * al), 0.8333, 5e-5)
Om = np.linspace(-4000, 4000, 1600001)
chk("S9 CT frequency-grid Parseval = 0.83325",
    np.trapezoid(1 / (al ** 2 + Om ** 2), Om) / (2 * np.pi), 0.83325, 5e-4)
wgrid = np.linspace(-np.pi, np.pi, 400001)
chk("S9 DT Parseval (1/2pi)int|X|^2dw = 1.3333",
    np.trapezoid(np.abs(1 / (1 - 0.5 * np.exp(-1j * wgrid))) ** 2, wgrid) / (2 * np.pi), 1.3333, 1e-4)

print("\n=== S5b + S6b: the CORRECTED claims (post-fix regression guard) ===")
wprof = np.linspace(0, np.pi, 2000001)
Yprof = np.abs((1 - 0.5 ** 5 * np.exp(-1j * wprof * 5)) / (1 - 0.5 * np.exp(-1j * wprof)))
chk("S5b numerator floor 1-a^M = 0.96875", 1 - 0.5 ** 5, 0.96875, 1e-12)
chk("S5b min |Y| = 0.6685 (NEVER zero for a=0.5)", Yprof.min(), 0.6685, 1e-4)
chk("S5b that minimum sits near 0.85pi", wprof[Yprof.argmin()] / np.pi, 0.846, 3e-3)
for frac, want in ((0.0, 1.9375), (0.3, 1.2295), (0.4, 0.9987), (0.5, 0.8949), (1.0, 0.6875)):
    chk(f"S5b |Y| at w = {frac}pi",
        np.abs((1 - 0.5 ** 5 * np.exp(-1j * frac * np.pi * 5)) / (1 - 0.5 * np.exp(-1j * frac * np.pi))), want)
chk("S5b a=-1, M=5 gives a null at w = pi/5",
    np.abs((1 - (-1.0) ** 5 * np.exp(-1j * np.pi / 5 * 5)) / (1 + np.exp(-1j * np.pi / 5))), 0, 1e-12)
wsl = np.linspace(2 * np.pi / 5 + 1e-6, np.pi, 400001)
Hsl = np.abs(np.sin(wsl * 5 / 2) / (5 * np.sin(wsl / 2)))
chk("S6b 5-pt MA peak sidelobe = 0.25 at 0.5804pi", wsl[Hsl.argmax()] / np.pi, 0.5804, 5e-5)
chk("S6b that is -12.04 dB (not 13 dB)", 20 * np.log10(Hsl.max()), -12.041, 5e-3)
chk("S6b long-window (M=201) limit is -13.26 dB",
    20 * np.log10(np.abs(np.sin(np.linspace(2 * np.pi / 201 + 1e-6, np.pi, 200001) * 201 / 2) /
                         (201 * np.sin(np.linspace(2 * np.pi / 201 + 1e-6, np.pi, 200001) / 2))).max()),
    -13.26, 5e-2)


print("\n=== S11 practice-set answers ===")
chk("P1 X(0) of {1,-1}", sdtft([1, -1], [0.0])[0], 0, 1e-12)
chk("P1 X(pi) of {1,-1}", sdtft([1, -1], [np.pi])[0], 2, 1e-12)
chk("P1 |X| = 2|sin(w/2)| at w=1.1", abs(sdtft([1, -1], [1.1])[0]), 2 * abs(np.sin(1.1 / 2)), 1e-12)
chk("P2 |X(0)| = 1/(1-0.8) = 5", abs(1 / (1 - 0.8)), 5)
chk("P2 |X(pi)| = 1/(1+0.8) = 0.5556", abs(1 / (1 - 0.8 * np.exp(-1j * np.pi))), 0.5556, 5e-5)
chk("P3 8-pt MA |H(0)| = 1", abs(ma_H(8, 0.0))[0], 1)
chk("P3 8-pt MA first null = 0.25pi", 2 * np.pi / 8 / np.pi, 0.25, 1e-12)
chk("P3 8-pt MA closed form == DTFT of h",
    np.abs(ma_H(8, np.linspace(0.01, np.pi, 500)) -
           sdtft(np.ones(8) / 8, np.linspace(0.01, np.pi, 500))).max(), 0, 1e-12)
chk("P4 h={1,-1} |H(0)| = 0", abs(sdtft([1, -1], [0.0])[0]), 0, 1e-12)
chk("P4 h={1,-1} |H(pi)| = 2", abs(sdtft([1, -1], [np.pi])[0]), 2, 1e-12)
chk("P5 4-pt MA |H(pi/4)| = 0.6533", abs(ma_H(4, np.pi / 4))[0], 0.6533, 5e-5)
chk("P5 4-pt MA angle at pi/4 = -67.5 deg", np.degrees(np.angle(ma_H(4, np.pi / 4)[0])), -67.5, 5e-3)
chk("P5 output amplitude 1.960", 3 * abs(ma_H(4, np.pi / 4))[0], 1.960, 5e-4)
chk("P6 h[1] = 2(0.5) = 1", 2 * 0.5, 1)
chk("P6 H(0) = 4", 2 / (1 - 0.5), 4)
chk("P7 DT energy = 1.3333", 1 / (1 - 0.25), 1.3333, 1e-4)
chk("P8 H(pi) = -18", sum(hh[n] * np.exp(-1j * np.pi * n) for n in range(4)), -18)
chk("P8 angle H(pi) = 180 deg (== -180 deg)",
    np.degrees(np.angle(sum(hh[n] * np.exp(-1j * np.pi * n) for n in range(4)))), -180, 1e-6)
chk("P9 10 ones: X(0) = 10", sdtft(np.ones(10), [0.0])[0], 10, 1e-12)
chk("P9 |X| = |sin(5w)/sin(w/2)| at w=1.3", abs(sdtft(np.ones(10), [1.3])[0]),
    abs(np.sin(5 * 1.3) / np.sin(1.3 / 2)), 1e-12)
chk("P9 first null at pi/5", np.abs(sdtft(np.ones(10), [np.pi / 5])[0]), 0, 1e-12)

print("\n=== drill step10_dtft.py claims ===")
wdr = np.linspace(0, np.pi, 1001)
chk("drill: DTFT vs closed form max err = 0.0",
    np.abs(sdtft(0.5 ** np.arange(40), wdr, np.arange(40)) -
           1 / (1 - 0.5 * np.exp(-1j * wdr))).max(), 0, 1e-9)
chk("drill: |H(0)| = 1 (M=5)", abs(ma_H(5, 0.0))[0], 1, 1e-9)
chk("drill: first null = 2pi/M = 1.256637 (M=5)", 2 * np.pi / 5, 1.256637, 1e-6)
chk("drill: delay = (M-1)/2 = 2",
    -(np.angle(ma_H(5, np.array([0.3])))[0] - np.angle(ma_H(5, np.array([0.1])))[0]) / 0.2, 2, 1e-9)

print("\n=== TEXT GUARDS: the wrong sentences must be gone from the markdown ===")
doc = open(os.path.join("DSP", "study", "10-dtft-worked-tutorial.md"), encoding="utf-8").read()
base = open(os.path.join("DSP", "study", "00-tt2-battle-plan.md"), encoding="utf-8").read()
drill = open(os.path.join("DSP", "practice", "step10_dtft.py"), encoding="utf-8").read()
for tag, needle, want_present in (
        ("10: old 'now has **nulls**' removed", "now has **nulls**", False),
        ("10: new 'there are NO nulls' present", "there are NO nulls", True),
        ("10: old 'only about 13 dB down' removed", "only about 13 dB down", False),
        ("10: new '-12.04 dB' present", "\u221212.04 dB", True),
        ("10: 0/0 note added", "the quotient is 0/0", True),
        ("battle plan: old '~13 dB down, so it is' removed", "only ~13 dB down, so it is", False),
        ("battle plan: new '~12 dB down for M = 5' present", "~12 dB down for M = 5", True),
        ("drill: old '13 dB sidelobes' removed", "13 dB sidelobes", False),
        ("drill: new '~12 dB down for M = 5' present", "~12 dB down for M = 5", True)) + ():
    present = needle in (doc if tag.startswith("10") else base if tag.startswith("battle") else drill)
    chk(tag, 1 if present == want_present else 0, 1, 0)

print("\n" + "=" * 96)
print("ALL CHECKS PASS" if not FAILS else f"{len(FAILS)} FAILURES:\n  - " + "\n  - ".join(FAILS))

