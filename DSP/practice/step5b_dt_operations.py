# DSP STEP 5b  -  Operations on discrete-time sequences   (syllabus item 3, Chapter 2 slides "Elementary Operations")
#
# Keep the sequence as TWO arrays: the index axis n and the values x. Every operation is then honest.
#
#   shift  y[n] = x[n - k]     : values unchanged, index axis moves:  n + k          (k > 0 delay = move right)
#   fold   y[n] = x[-n]        : values reversed, index axis negated and reversed:  -n[::-1], x[::-1]
#   scale  y[n] = a * x[n]     : a * x
#   add / multiply two sequences: they must be on the SAME axis first. Build a common axis from
#       min(start) to max(end), place each sequence on it with zeros elsewhere, then add / multiply.
#   up-sample by L  : insert L-1 zeros between samples          np.zeros(L*len(x)); y[::L] = x
#   down-sample by M: keep every M-th sample                     x[::M]
#
# Example sequence from the slides, arrow under the 4th value:
#   x = {2, -2, 2, 1, 1, 2, 3, 4}   with n = -3 .. 4

import numpy as np
import matplotlib.pyplot as plt

x  = np.array([2, -2, 2, 1, 1, 2, 3, 4])
nx = np.arange(-3, 5)                    # -3 .. 4, so x[0] = 1 (the 4th entry)


def shift(n, x, k):
    """y[n] = x[n - k].  Returns (n_new, y)."""
    # TODO
    return (n+k), x

def fold(n, x):
    """y[n] = x[-n].  Returns (n_new, y)."""
    # TODO
    return -n[::-1], x[::-1]

def on_axis(n, x, n_common):
    """Place (n, x) onto the axis n_common, zeros where x is not defined."""
    # TODO: y = np.zeros(len(n_common)); for each i, v in zip(n, x): y[np.where(n_common == i)] = v
    y = np.zeros(len(n_common))
    for i, v in zip(n, x):
        y[np.where(n_common == i)] = v
    return y

def add(n1, x1, n2, x2):
    """Sum of two sequences on a common axis. Returns (n_common, y)."""
    # TODO: n_common = np.arange(min(n1[0], n2[0]), max(n1[-1], n2[-1]) + 1); then on_axis both and add
    n_common = np.arange(min(n1[0], n2[0]), max(n1[-1], n2[-1]) + 1)
    y1 = on_axis(n1, x1, n_common)
    y2 = on_axis(n2, x2, n_common)
    return n_common, (y1+y2)

def upsample(x, L):
    # TODO
    y = np.zeros(L*len(x))
    y[::L]=x
    return y

def downsample(x, M):
    # TODO
    return x[::M]


# ---------------- checker: don't edit below ----------------
def L(a): return None if a is None else list(np.asarray(a).tolist())
n2, y2 = shift(nx, x, 2)
nf, yf = fold(nx, x)
na, ya = add(nx, x, *shift(nx, x, 2)) if n2 is not None else (None, None)
checks = [
    ("shift k=2 axis",  L(n2), list(range(-1, 7))),
    ("shift k=2 vals",  L(y2), [2, -2, 2, 1, 1, 2, 3, 4]),
    ("fold axis",       L(nf), list(range(-4, 4))),
    ("fold vals",       L(yf), [4, 3, 2, 1, 1, 2, -2, 2]),
    ("x + x[n-2] axis", L(na), list(range(-3, 7))),
    ("x + x[n-2] vals", L(ya), [2, -2, 4, -1, 3, 3, 4, 6, 3, 4]),
    ("upsample L=2",    L(upsample(np.array([1, 2, 3]), 2)),   [1, 0, 2, 0, 3, 0]),
    ("downsample M=2",  L(downsample(np.array([1, 2, 3, 4, 5]), 2)), [1, 3, 5]),
]
ok = True
for name, got, want in checks:
    good = got == want
    ok &= good
    print(f"{name:18s} {got}   {'ok' if good else f'expected {want}'}")
print("PASS  ->  syllabus items 1-3 done. steps 6-9 are bonus (Assignment 4 / 1 material)." if ok else "FAIL")

if ok:
    fig, ax = plt.subplots(2, 2, figsize=(11, 6))
    for a, (title, nn, xx) in zip(ax.flat, [("x[n]", nx, x), ("x[n-2]  (delay by 2)", n2, y2), ("x[-n]  (fold)", nf, yf), ("x[n] + x[n-2]", na, ya)]):
        a.stem(nn, xx, basefmt=" "); a.set_title(title); a.set_xticks(nn); a.axvline(0, color="gray", alpha=.3); a.grid(alpha=.3)
    plt.tight_layout(); plt.show()
