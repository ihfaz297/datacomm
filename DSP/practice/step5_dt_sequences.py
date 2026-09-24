# DSP STEP 5 / 9  -  Generating and operating on discrete-time sequences   (syllabus item 3, Assignment 4 Q1)
#
# A DT sequence in numpy = an index axis n plus the values at each n.
#   n = np.arange(-5, 6)                  n from -5 to 5
#   impulse delta[n - k] : 1 where n == k, else 0          k > 0 delay, k < 0 advance
#   step    u[n - k]     : 1 where n >= k, else 0
# numpy trick: (n == k) is a True/False array; .astype(int) turns it into 1/0.
#
# Operations (slides "Elementary Operations"):
#   shift x[n - k]  : np.roll is WRONG (it wraps). Recompute on the shifted index instead, or use np.interp on n.
#   fold  x[-n]     : x[::-1]  when n is symmetric about 0
#   scale, add, multiply : plain numpy arithmetic, sequences must share the same n axis.
# Plot with plt.stem(n, x). Mark n = 0.

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 6)          # -5 .. 5


def impulse(n, k=0):
    """delta[n - k] on index axis n."""
    impulse = (n == k) * 1
    # TODO
<<<<<<< HEAD
    return impulse
=======
    imp = (n == k) * 1
    return imp
>>>>>>> ef1da11e463049280418d6d91a236737edf5d842

def step(n, k=0):
    """u[n - k] on index axis n."""
    step = (n >= k) * 1
<<<<<<< HEAD
    # TODO
=======
>>>>>>> ef1da11e463049280418d6d91a236737edf5d842
    return step


# a rectangular pulse from n = -2 to n = 2 is  u[n + 2] - u[n - 3]
# TODO: build it from your step() function
rect = step(n, -2) - step(n, 3)

# a triangle-ish combo:  2*delta[n + 1] + delta[n - 1] + u[n - 3]
# TODO
combo = 2 * impulse(n, -1) + impulse(n, 1) + step(n, 3)

# fold rect -> rect[-n]  (should equal rect here because rect is symmetric)
# TODO
rect_folded = rect[::-1]

# ---------------- checker: don't edit below ----------------
def arr(x): return None if x is None else list(map(int, x))
checks = [
    ("impulse(n)",      arr(impulse(n)),      [0,0,0,0,0,1,0,0,0,0,0]),
    ("impulse(n, 2)",   arr(impulse(n, 2)),   [0,0,0,0,0,0,0,1,0,0,0]),
    ("impulse(n, -3)",  arr(impulse(n, -3)),  [0,0,1,0,0,0,0,0,0,0,0]),
    ("step(n)",         arr(step(n)),         [0,0,0,0,0,1,1,1,1,1,1]),
    ("step(n, -2)",     arr(step(n, -2)),     [0,0,0,1,1,1,1,1,1,1,1]),
    ("rect",            arr(rect),            [0,0,0,1,1,1,1,1,0,0,0]),
    ("combo",           arr(combo),           [0,0,0,0,2,0,1,0,1,1,1]),
    ("rect_folded",     arr(rect_folded),     [0,0,0,1,1,1,1,1,0,0,0]),
]
ok = True
for name, got, want in checks:
    good = got == want
    ok &= good
    print(f"{name:14s} {got}   {'ok' if good else f'expected {want}'}")
print("PASS  ->  open step5b_dt_operations.py" if ok else "FAIL")

if ok:
    fig, axes = plt.subplots(2, 3, figsize=(13, 6))
    dt_sig = [("delta[n]", impulse(n)), 
              ("delta[n-2] (delay)", impulse(n, 2)), 
              ("delta[n+3] (advance)", impulse(n, -3)),
              ("u[n]", step(n)), 
              ("u[n+2] - u[n-3]", rect), 
              ("2d[n+1] + d[n-1] + u[n-3]", combo)]
    for ax, (name, x) in zip(axes.flat, dt_sig):
        ax.stem(n, x, basefmt=" ")
        ax.set_title(name)
        ax.set_xticks(n)
        ax.axvline(0, color="gray", alpha=.3)
        ax.set_xlabel("n")
    plt.tight_layout()
    plt.show()
