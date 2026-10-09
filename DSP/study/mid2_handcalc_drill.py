"""Mid-2 hand-calculation drill.

Work each one ON PAPER first (calculator allowed, like the exam), then type your number
after the = and run:   python DSP/study/mid2_handcalc_drill.py

Leave a TODO as None to skip it. Complex numbers: write 2-2j. Angles in DEGREES.
Section numbers point at the tutorial that teaches it.
"""

# ---------------- Q1: frequency response (20-T1-frequency-response.md) ----------------

# T1 §3b  Mitra 4.68: h[n] = (0.4)^n u[n].  H(e^{j pi/4}) = ?
q1_H_pi4 = None            # TODO complex, e.g. 1.2-0.5j
q1_H_pi4_mag = None        # TODO |H|
q1_H_pi4_phase_deg = None  # TODO angle in degrees

# T1 §3a  h = {-3, 6, -5, 4}. H(e^{j pi/2}) = ?   (e^{-j pi/2} = -j)
q1_H_fir_pi2 = None        # TODO complex

# T1 §5   5-point moving average: |H| at w = pi/5, and the first zero (in units of pi)
q1_ma_mag_pi5 = None       # TODO
q1_ma_first_zero_over_pi = None   # TODO  e.g. 0.4 means 0.4*pi

# T1 §6a  h = {4, -5, 6, -3}, input u[n]: y[0], y[1], y[2], and steady state
q1_step = None             # TODO list [y0, y1, y2, y_ss]

# T1 §8a  3-tap HPF that kills w=0.1 and passes w=0.4 with gain 1: alpha0, alpha1
q1_hpf = None              # TODO [alpha0, alpha1]

# ---------------- Q2: z-transform (21-T2-ztransform.md) ----------------

# T2 §8b  y = 2^n u[n] * 0.5^n u[n]  ->  y[n] = A*2^n + B*0.5^n.  A, B = ?
q2_AB = None               # TODO [A, B]

# T2 §8c  X(z) = 1/((1+2z^-1)(1-z^-1)^2), causal. x[n] = A*(p)^n + B + C*n.  A, p, B, C = ?
q2_double = None           # TODO [A, p, B, C]

# T2 §7a  y(n) = 0.5 y(n-1) + 2 x(n):  h[0], h[1], h[2]
q2_h = None                # TODO [h0, h1, h2]

# T2 §3c  x = 0.5^n u[n] + 2^n u[-n-1]: inner and outer ROC radius
q2_roc = None              # TODO [inner, outer]

# T2 §6a  poles of X(z) = z(2z^2-2z+1)/(16z^3+6z+5): the largest |pole|  (2 decimals)
q2_max_pole = None         # TODO

# ---------------- Q3: frequency analysis (22-T3-frequency-analysis.md) ----------------

# T3 §1b  square wave +-1: c_1 and c_3
q3_square = None           # TODO [c1, c3]

# T3 §3a  DTFS of the period-4 sequence {1,1,0,0}: c0, c1, c2, c3
q3_dtfs = None             # TODO [c0, c1, c2, c3]  (complex allowed)

# T3 §4d  energy of e^{-0.6 t} u(t)
q3_energy = None           # TODO

# T3 §4a  energy density S_xx(w) of 0.5^n u[n] at w = 0 and w = pi
q3_sxx = None              # TODO [S(0), S(pi)]

# T3 §3b  DTFS of the period-10 pulse train, 5 ones (n = -2..2): c0 and c1
q3_pulse = None            # TODO [c0, c1]


# ---------------- Convolution by EXPANSION (23-convolution-revise.md) ----------------
# Write y(n) = sum x(k)h(n-k) out on paper, expand per n, then type the sequence here.

# A1 (TT1 Q4)  h = {1, 2↑, 1, -1}, x = {1↑, 2, 3, 1}.  First n of y, then the values
conv_tt1_start = None      # TODO the n where y begins
conv_tt1 = None            # TODO list of 7 values

# A2 (final Q1h)  x = {-1,3,2,0,1} on -2..2,  h = {-3,5,0,1} on -1..2.  y(0) = ?
conv_final_y0 = None       # TODO

# A3  u(n) * (0.5)^n u(n): y(3) = ?
conv_step_y3 = None        # TODO


# =================== checker (don't edit below) ===================
import cmath, math

def _close(a, b, tol=2e-3):
    if isinstance(b, (list, tuple)):
        return isinstance(a, (list, tuple)) and len(a) == len(b) and all(_close(x, y, tol) for x, y in zip(a, b))
    return abs(complex(a) - complex(b)) <= tol * max(1, abs(complex(b)))

def _H(h, w):
    return sum(c * cmath.exp(-1j * w * n) for n, c in enumerate(h))

H4 = 1 / (1 - 0.4 * cmath.exp(-1j * math.pi / 4))
a0 = 1 / (2 * (math.cos(0.4) - math.cos(0.1)))
expected = {
    "q1_H_pi4": H4,
    "q1_H_pi4_mag": abs(H4),
    "q1_H_pi4_phase_deg": math.degrees(cmath.phase(H4)),
    "q1_H_fir_pi2": _H([-3, 6, -5, 4], math.pi / 2),
    "q1_ma_mag_pi5": abs(_H([0.2] * 5, math.pi / 5)),
    "q1_ma_first_zero_over_pi": 0.4,
    "q1_step": [4, -1, 5, 2],
    "q1_hpf": [a0, -2 * a0 * math.cos(0.1)],
    "q2_AB": [4 / 3, -1 / 3],
    "q2_double": [4 / 9, -2, 5 / 9, 1 / 3],
    "q2_h": [2, 1, 0.5],
    "q2_roc": [0.5, 2],
    "q2_max_pole": abs(0.25 + 0.75j),
    "q3_square": [2 / math.pi, -2 / (3 * math.pi)],
    "q3_dtfs": [0.5, 0.25 - 0.25j, 0, 0.25 + 0.25j],
    "q3_energy": 1 / 1.2,
    "q3_sxx": [4, 1 / 2.25],
    "q3_pulse": [0.5, math.sin(2 * math.pi * 2.5 / 10) / (10 * math.sin(math.pi / 10))],
    "conv_tt1_start": -1,
    "conv_tt1": [1, 4, 8, 8, 3, -2, -1],
    "conv_final_y0": 9,
    "conv_step_y3": 1.875,
}

def _fmt(v):
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(_fmt(x) for x in v) + "]"
    if isinstance(v, complex):
        return f"{v.real:.4f}{v.imag:+.4f}j"
    return f"{v:.4f}" if isinstance(v, float) else str(v)

passed = skipped = 0
for name, exp in expected.items():
    got = globals()[name]
    if got is None:
        skipped += 1
        print(f"  SKIP {name}")
    elif _close(got, exp, tol=1e-2 if name == "q2_max_pole" else 2e-3):
        passed += 1
        print(f"  PASS {name}")
    else:
        print(f"  FAIL {name}: you wrote {_fmt(got)}, expected {_fmt(exp)}")
print(f"\n{passed}/{len(expected)} PASS, {skipped} skipped")
