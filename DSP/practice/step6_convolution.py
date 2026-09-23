# DSP STEP 6 / 9  -  Convolution sum, simulated step by step   (Assignment 4 Q2)
#
#   y[n] = sum over k of  x[k] * h[n - k]
#   length of y = len(x) + len(h) - 1
#   if x starts at index x0 and h at index h0, y starts at x0 + h0   (arrow bookkeeping)
#
# Step-by-step means: for each output n, list the products x[k]*h[n-k] that exist, then sum them.
# Two nested loops. Then compare with np.convolve(x, h) to prove it.

import numpy as np
import matplotlib.pyplot as plt

x  = np.array([1, 2, 3, 1])      # x[n], starts at n = 0
h  = np.array([1, 1, 1])         # h[n], starts at n = 0
x0, h0 = 0, 0                    # start indices (change these if the arrow isn't under the first element)


def conv_steps(x, h):
    """Return y (numpy array) and a list of text lines showing each step."""
    N, M = len(x), len(h)
    y = np.zeros(N + M - 1)
    lines = []
    for n in range(N + M - 1):
        terms = []
        for k in range(N):
            # TODO: the index into h is n - k. If it is inside 0 .. M-1, add x[k]*h[n-k] to y[n]
            #       and append a string like f"x[{k}]*h[{n-k}]={x[k]*h[n-k]}" to terms
            pass
        lines.append(f"y[{n}] = " + " + ".join(terms) + f" = {y[n]:g}")
    return y, lines


y, lines = conv_steps(x, h)
print("x =", x, " h =", h)
for line in lines: print("  " + line)
print("y =", y, "   starts at n =", x0 + h0)

# ---------------- checker: don't edit below ----------------
ref = np.convolve(x, h)
ok = np.allclose(y, ref) and len(lines) == len(ref) and all("x[" in l for l in lines)
print("np.convolve says:", ref)
print("PASS  ->  open step7_correlation.py" if ok else "FAIL  (y must equal np.convolve(x, h); every line must list its products)")

if ok:
    ny = np.arange(x0 + h0, x0 + h0 + len(y))
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.5))
    ax[0].stem(np.arange(x0, x0 + len(x)), x, basefmt=" "); ax[0].set_title("x[n]")
    ax[1].stem(np.arange(h0, h0 + len(h)), h, basefmt=" "); ax[1].set_title("h[n]")
    ax[2].stem(ny, y, basefmt=" "); ax[2].set_title("y[n] = x[n] * h[n]")
    for a in ax: a.set_xlabel("n"); a.grid(alpha=.3)
    plt.tight_layout(); plt.show()
