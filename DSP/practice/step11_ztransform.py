# DSP STEP 11  -  z-transform, ROC, poles and zeros        (TT2 topic 2 / past final paper Q6, Q4b, Q5a)
#
#   X(z) = sum over all n of x[n] z^-n       (two-sided; the one-sided version starts at n = 0)
#   The ROC is part of the answer: a z-transform WITHOUT its ROC is meaningless.
#
#        a^n u[n]              ->  1/(1 - a z^-1)      ROC |z| > |a|    (right sided, causal)
#       -a^n u[-n-1]           ->  1/(1 - a z^-1)      ROC |z| < |a|    (left sided)
#        a^n u[n] + b^n u[-n-1] ->  1/(1-a/z) - 1/(1-b/z)  =  (a-b) z^-1 / ((1-a/z)(1-b/z))
#                                   ROC  |a| < |z| < |b|   -- an annulus, EMPTY if |b| <= |a|
#
#   Finite length (past final paper Q6b): x[n] = a^n, 0 <= n <= M-1
#        X(z) = (1 - a^M z^-M)/(1 - a z^-1) = (z^M - a^M) / (z^(M-1) (z - a))
#        -> z = a is a pole-zero CANCELLATION, so really
#           zeros at z = a e^(j 2 pi k / M), k = 1 .. M-1  and  (M-1) poles at z = 0, ROC |z| > 0
#
#   SymPy is allowed in the lab exam and does the series / partial fractions for you:
#        sp.summation((a/z)**n, (n, 0, sp.oo))      -> the sum AND its ROC condition
#        sp.apart(X/z, z)                           -> partial fractions for the inverse z-transform
#
# Run:  python DSP/practice/step11_ztransform.py

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

a, b, z, n = sp.symbols("a b z n")
Ms = sp.symbols("M", integer=True, positive=True)
M_num = 8                    # length used for the numeric pole-zero part
a_num, b_num = 0.5, 2.0      # the two-sided example has poles at 0.5 and 2 -> ROC 0.5 < |z| < 2
z0 = 1.2                     # a test point inside that annulus


def two_sided(a_, b_, z_):
    """Closed form X(z) of x[n] = a^n u[n] + b^n u[-n-1]   (past final paper Q6a)."""
    # TODO: 1/(1 - a_/z_) - 1/(1 - b_/z_)
    return None


def in_roc(z_, a_, b_):
    """True when z_ lies inside the ROC annulus |a| < |z| < |b| of that two-sided sequence."""
    # TODO
    return None


def zeros_poles(M_, a_):
    """Poles and zeros of x[n] = a^n, 0 <= n <= M-1   (past final paper Q6b).
    X(z) = (z^M - a^M) / (z^(M-1) (z - a));  the root z = a cancels, so return it in neither list."""
    # TODO: num = [1, 0 ... 0, -a_**M_]   (degree M, i.e. z^M - a^M)
    #       den = [1, -a_, 0 ... 0]      (degree M, i.e. z^(M-1) (z - a))
    #       zp, zr = np.roots(den), np.roots(num);  drop the shared root z = a_ from both
    return None, None
# ---------------- checker: don't edit below ----------------
F = lambda v: None if v is None else float(v)

geo    = sp.summation((a/z)**n, (n, 0, sp.oo))       # SymPy even reports the ROC condition |a/z| < 1
finite = sp.summation((a/z)**n, (n, 0, Ms - 1))
geo_num    = F(geo.subs({a: a_num, z: z0}))          # |a/z| = 0.42 < 1, so this branch is the answer
finite_num = F(finite.subs({a: a_num, z: z0, Ms: M_num}))
ref_geo    = 1 / (1 - a_num/z0)
ref_finite = sum((a_num/z0)**k for k in range(M_num))

num_sum = sum(a_num**k * z0**-k for k in range(0, 400)) + sum(b_num**k * z0**-k for k in range(-400, 0))
X = two_sided(a_num, b_num, z0)

zp, zr = zeros_poles(M_num, a_num)
if zr is None or zp is None:
    zero_ok = pole_ok = False
else:
    want = 2*np.pi*np.arange(1, M_num)/M_num            # k = 1 .. M-1, i.e. every other M-th root cancelled
    got_ang = np.sort(np.mod(np.angle(zr), 2*np.pi))    # np.angle gives (-pi, pi]; wrap before comparing
    zero_ok = (len(zr) == M_num-1 and np.allclose(np.abs(zr), a_num, atol=1e-9)
               and np.allclose(got_ang, want, atol=1e-9))
    pole_ok = len(zp) == M_num-1 and np.allclose(zp, 0, atol=1e-9)

checks = [
    ("SymPy sum, |a/z|<1 branch",     geo_num,                      ref_geo,    1e-9),
    ("SymPy finite geometric sum",    finite_num,                   ref_finite, 1e-9),
    (f"two-sided X(z) at z = {z0}",   F(X),                         num_sum,    1e-6),
    ("ROC: point 1.2 inside (0.5,2)", F(in_roc(1.2, a_num, b_num)), True,       0),
    ("ROC: point 0.3 rejected",       F(in_roc(0.3, a_num, b_num)), False,      0),
    ("ROC: point 3.0 rejected",       F(in_roc(3.0, a_num, b_num)), False,      0),
    ("ROC empty when |b| <= |a|",     F(in_roc(1.2, 2.0, 0.5)),     False,      0),
]
ok = True
for name, got, want, tol in checks:
    good = got is not None and abs(got - float(want)) <= tol
    ok &= good
    print(f"{name:30s} {got if got is None else round(got, 6)}   {'ok' if good else f'expected {want}'}")
for name, good in (("zeros = a e^(j2pi k/M), k=1..M-1", zero_ok), ("poles = M-1 at z = 0", pole_ok)):
    ok &= good
    print(f"{name:30s} {'ok' if good else f'expected {M_num-1} of them'}")
print("PASS  ->  open step12_dft_fft.py" if ok else
      "FAIL  (a^n u[n] ~ 1/(1-a/z) with |z|>|a|;  -a^n u[-n-1] flips the ROC to |z|<|a|)")

print("\nSymPy says:")
print("  sum (a/z)^n, 0..oo   :", geo)
print("  sum (a/z)^n, 0..M-1  :", finite)
print(f"  two-sided X(z) at z = {z0}: numeric {num_sum:.10f}   closed form {X}")
if zr is not None:
    print("  zeros of a^n, 0<=n<=M-1:", np.round(zr, 4))

if ok:
    th = np.linspace(0, 2*np.pi, 400)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.6))
    for t, title in zip(ax, ["ROC of the two-sided sequence = annulus", "zeros / poles of a^n, 0<=n<=M-1"]):
        t.plot(np.cos(th), np.sin(th), "k--", lw=.8, label="unit circle")
        t.set_aspect("equal"); t.set_title(title); t.legend(); t.grid(alpha=.3)
        t.set_xlabel("Re z"); t.set_ylabel("Im z")
    ax[0].fill_between(b_num*np.cos(th), b_num*np.sin(th), a_num*np.sin(th), color="C0", alpha=.15)
    ax[0].plot(a_num*np.cos(th), a_num*np.sin(th), "r--", lw=.8, label="|z| = a = 0.5")
    ax[0].plot(b_num*np.cos(th), b_num*np.sin(th), "r:", lw=.8, label="|z| = b = 2")
    ax[0].plot(0.5, 0.9, "x", color="C3"); ax[0].plot(2*np.cos(.6), 2*np.sin(.6), "x", color="C3")
    ax[0].set_xlim(-2.6, 2.6); ax[0].set_ylim(-2.6, 2.6); ax[0].legend(loc="upper right", fontsize=8)
    if zr is not None and zp is not None:
        ax[1].plot(zr.real, zr.imag, "o", mfc="none", ms=7, label="zeros")
        ax[1].plot(zp.real, zp.imag, "x", ms=8, label="poles (7 at the origin)")
        ax[1].set_xlim(-1.3, 1.3); ax[1].set_ylim(-1.3, 1.3)
    plt.tight_layout(); plt.show()

