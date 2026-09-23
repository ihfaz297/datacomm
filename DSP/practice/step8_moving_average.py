# DSP STEP 8 / 9  -  Noise removal by averaging   (Assignment 4 Q4)
#
# Clean signal  s[n] = 2 * n * 0.9**n            n = 0 .. 49
# Noise         d[n] = rand(50) - 0.5           uniform in -0.5 .. 0.5, zero mean
# Corrupted     x[n] = s[n] + d[n]
#
# Ensemble averaging (what the assignment does): make 50 different noisy copies, add them up, divide by 50.
# Noise averages toward zero, signal stays.
#
# M-point moving-average FILTER (the slides' version, one noisy copy, average neighbours):
#   y[n] = (1/M) * (x[n] + x[n-1] + ... + x[n-M+1])   ->   np.convolve(x, np.ones(M)/M, mode="same")

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n = np.arange(50)
# TODO: s, one noise d, one corrupted x
s = None
d = None
x = None

# TODO: ensemble average over 50 trials.  Loop 50 times: fresh noise, add s + noise into an accumulator; divide by 50 at the end.
X1 = None

# TODO: 5-point moving-average filter applied to the single corrupted x
M = 5
y_ma = None

# ---------------- checker: don't edit below ----------------
def err(a): return None if a is None else float(np.mean((a - s) ** 2))
ok = s is not None and abs(s[1] - 1.8) < 1e-9 and abs(s.max() - s[9]) < 1e-9
ok = ok and d is not None and -0.5 <= d.min() and d.max() < 0.5 and x is not None and np.allclose(x, s + d)
e_x, e_X1, e_ma = err(x), err(X1), err(y_ma)
print(f"mean squared error vs clean s:   single noisy x = {e_x}   ensemble avg X1 = {e_X1}   5-pt MA = {e_ma}")
ok = ok and e_X1 is not None and e_X1 < e_x / 10 and e_ma is not None and e_ma < e_x
print("PASS  ->  open step9_spectrum_audio.py" if ok else "FAIL  (s[1] must be 1.8, s peaks at n=9; X1 error must be far below x's; MA error below x's)")

if ok:
    fig, ax = plt.subplots(2, 2, figsize=(12, 7))
    ax[0,0].stem(n, s, basefmt=" "); ax[0,0].set_title("clean s[n] = 2 n 0.9^n")
    ax[0,1].stem(n, d, basefmt=" "); ax[0,1].set_title("noise d[n] = rand - 0.5")
    ax[1,0].stem(n, x, basefmt=" "); ax[1,0].set_title("corrupted x[n] = s + d")
    ax[1,1].plot(n, s, "k--", label="clean"); ax[1,1].plot(n, X1, label="ensemble avg of 50"); ax[1,1].plot(n, y_ma, label=f"{M}-pt moving avg")
    ax[1,1].set_title("noise removed"); ax[1,1].legend()
    for a in ax.flat: a.grid(alpha=.3); a.set_xlabel("n")
    plt.tight_layout(); plt.show()
