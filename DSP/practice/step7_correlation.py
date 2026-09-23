# DSP STEP 7 / 9  -  Cross-correlation and autocorrelation   (Assignment 4 Q3)
#
#   r_xy[l] = sum over n of  x[n] * y[n - l]        l = lag
#   Trick: correlation is convolution with the second sequence FOLDED:
#       r_xy = conv(x, y[::-1])
#   Lags run from -(len(y)-1) to +(len(x)-1).
#   Autocorrelation: r_xx = correlation of x with itself. Peak is at lag 0 and equals the energy sum(x**2).
#   numpy reference: np.correlate(x, y, mode="full")

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([1, 1, 2])


def xcorr(x, y):
    """Return (lags, r) with r[l] = sum_n x[n] * y[n - l]."""
    # TODO: r = np.convolve(x, y[::-1]);  lags = np.arange(-(len(y) - 1), len(x))
    return None, None

def autocorr(x):
    # TODO: xcorr of x with itself
    return None, None


# ---------------- checker: don't edit below ----------------
lags, r = xcorr(x, y)
al, ra  = autocorr(x)
ref  = np.correlate(x, y, mode="full")
refa = np.correlate(x, x, mode="full")
print("cross-corr lags :", lags); print("cross-corr r    :", r); print("np.correlate    :", ref)
print("autocorr r      :", ra, " energy sum(x^2) =", int(np.sum(x**2)))
ok = (r is not None and np.array_equal(r, ref) and lags is not None and list(lags) == list(range(-(len(y)-1), len(x)))
      and ra is not None and np.array_equal(ra, refa) and ra[len(x) - 1] == np.sum(x**2))
print("PASS  ->  open step8_moving_average.py" if ok else "FAIL  (match np.correlate(x, y, 'full'); autocorr peak at lag 0 must equal sum(x**2))")

if ok:
    fig, ax = plt.subplots(1, 2, figsize=(11, 3.5))
    ax[0].stem(lags, r, basefmt=" "); ax[0].set_title("cross-correlation r_xy[l]"); ax[0].set_xlabel("lag l")
    ax[1].stem(al, ra, basefmt=" ");  ax[1].set_title("autocorrelation r_xx[l]  (even, peak at 0)"); ax[1].set_xlabel("lag l")
    for a in ax: a.grid(alpha=.3)
    plt.tight_layout(); plt.show()
