# DSP STEP 10  -  DTFT and the frequency response of an LTI system
#   (TT2 topic 1: frequency-domain representation  /  lab exam 2 topic 4 "Transforms and DT systems")
#
# DTFT by definition:     X(e^jw) = sum over all n of  x[n] * exp(-j w n)
#   a whole frequency grid at once:   X = exp(-1j * outer(w, n)) @ x
# The frequency response H(e^jw) of an LTI system IS the DTFT of its impulse response h[n].
#
# Causal exponential (past final paper Q2c):   x[n] = a^n u[n]  ->  X(e^jw) = 1/(1 - a e^-jw),  |a| < 1
#       |X| = 1/sqrt(1 - 2 a cos w + a^2)          phase = -arctan( a sin w / (1 - a cos w) )
# M-point moving average (past final paper Q5b):  h[n] = 1/M, 0 <= n <= M-1
#       H(e^jw) = sin(w M/2) / (M sin(w/2)) * exp(-j w (M-1)/2)
#       |H| = 1 at w = 0,  first null at w = 2 pi / M,  linear phase = pure delay of (M-1)/2 samples
#       (that is why the moving average is a poor lowpass: 13 dB sidelobes, wide transition band)
#
# Run:  python DSP/practice/step10_dtft.py

import numpy as np
import matplotlib.pyplot as plt

a = 0.5          # pole radius of the causal exponential, |a| < 1
M = 5            # moving average length
w = np.linspace(0, np.pi, 1001)      # rad/sample.  The DTFT is 2*pi periodic, so 0..pi says everything


def dtft(x, w, n=None):
    """DTFT of the sequence x (values) sitting on the index axis n (default 0 .. len(x)-1)."""
    x = np.asarray(x, dtype=float)
    n = np.arange(len(x)) if n is None else np.asarray(n)
    # TODO: return exp(-1j * outer(w, n)) @ x
    return None


def causal_exp_dtft(a, w):
    """Closed form DTFT of x[n] = a^n u[n]."""
    # TODO: 1 / (1 - a * exp(-1j*w))
    return None


def moving_average_H(M, w):
    """Closed form frequency response of the M-point moving average filter."""
    # TODO: sin(w*M/2) / (M*sin(w/2)) * exp(-1j*w*(M-1)/2);  the w = 0 sample must come out as 1
    #       (sin(w/2) = 0 there -> evaluate the quotient inside np.errstate(divide="ignore", invalid="ignore"))
    return None


# ---------------- checker: don't edit below ----------------
n_exp = np.arange(0, 40)                       # 40 terms: a^40 is already 1e-12, so this is the DTFT
num = dtft(a ** n_exp, w, n_exp)
clo = causal_exp_dtft(a, w)
err   = None if num is None or clo is None else float(np.abs(num - clo).max())
mag   = None if clo is None else np.abs(clo)
err_m = None if mag is None else float(np.abs(mag - 1 / np.sqrt(1 - 2*a*np.cos(w) + a**2)).max())

H  = moving_average_H(M, w)
Hn = dtft(np.ones(M) / M, w)
errH = None if H is None or Hn is None else float(np.abs(H - Hn).max())
k = np.arange(1, len(w))                       # skip w = 0 when hunting for the null
null = None if H is None else float(w[k][np.argmin(np.abs(H[k]))])
if H is None:
    delay = None
else:
    ph = np.angle(moving_average_H(M, np.array([0.1, 0.3])))
    delay = float(-(ph[1] - ph[0]) / 0.2)

checks = [
    ("DTFT vs closed form (max err)",   err,   0.0,         1e-9),
    ("|X| vs 1/sqrt(1-2a cos w + a^2)", err_m, 0.0,         1e-9),
    ("H(e^jw) vs DTFT of h[n]",         errH,  0.0,         1e-9),
    ("|H(0)|  (must be 1)",             None if H is None else float(abs(H[0])), 1.0, 1e-9),
    ("first null of |H|  (2 pi / M)",   null,  2*np.pi/M,   5e-3),
    ("phase slope -> delay (M-1)/2",    delay, (M-1)/2,     1e-9),
]
ok = True
for name, got, want, tol in checks:
    good = got is not None and abs(got - want) <= tol
    ok &= good
    print(f"{name:34s} {got if got is None else round(got, 6)}   {'ok' if good else f'expected {want}'}")
print("PASS  ->  open step11_ztransform.py" if ok else
      "FAIL  (X = exp(-j w n) @ x ; h[n] = 1/M -> H is the Dirichlet kernel sin(wM/2)/(M sin(w/2)))")

if ok:
    fig, ax = plt.subplots(1, 3, figsize=(14, 3.8))
    ax[0].plot(w / np.pi, np.abs(num)); ax[0].set_title(f"|X(e^jw)| of {a}^n u[n]")
    ax[1].plot(w / np.pi, 20*np.log10(np.abs(H)))
    ax[1].axvline(2*np.pi/M/np.pi, color="r", ls="--", label="first null  2pi/M")
    ax[1].set_title(f"|H| of the {M}-point moving average (dB)"); ax[1].legend()
    ax[2].plot(w / np.pi, np.angle(H)); ax[2].set_title("phase of H: straight line = linear phase")
    for t in ax:
        t.set_xlabel("w / pi"); t.grid(alpha=.3)
    plt.tight_layout(); plt.show()
