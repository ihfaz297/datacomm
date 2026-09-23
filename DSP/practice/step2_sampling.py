# DSP STEP 2 / 9  -  Sampling in the time domain   (syllabus 2a, Assignment 3 Task 3)
#
# Sampling = evaluate the SAME formula on a coarse axis instead of a dense one.
#   Ts = 1 / Fs                              sampling interval
#   n_t = np.arange(0, duration, Ts)         sample instants  (0, Ts, 2Ts, ... < duration)
#   x_s = np.sin(2 * np.pi * F * n_t)        sample values
#   number of samples = len(n_t) = Fs * duration
#
# Plot: dense curve with plt.plot, samples on top with plt.stem.
#
# Assignment 3 Task 3 asks the same thing five times with different F / Fs / duration.
# Write ONE function and call it five times.

import numpy as np
import matplotlib.pyplot as plt


# def sample(F, Fs, duration):
#     """Return (n_t, x_s): sample instants and sample values of sin(2*pi*F*t)."""
#     # TODO: Ts, n_t, x_s
#     n_t = np.arange(0, duration, 1 / Fs)
#     x_s = np.sin(2*np.pi*F*n_t)
#     return n_t, x_s

def sampler(F, Fs, d):
    n_t = np.arange(0, d, 1 / Fs)
    x_s = np.sin(2 * np.pi * F * n_t)
    return n_t, x_s

cases = [  # (F, Fs, duration)   a..e from the assignment
    (5, 10, 1),
    (5, 10, 2),
    (5, 20, 1),
    (10, 10, 1),
    (10, 40, 1),
]

# ---------------- checker: don't edit below ----------------
expected_counts = [10, 20, 20, 10, 40]
counts = []
for F, Fs, d in cases:
    n_t, x_s = sampler(F, Fs, d)
    counts.append(None if n_t is None else len(n_t))
    print(f"F = {F:>2} Hz  Fs = {Fs:>2} Hz  t = {d} s  ->  samples: {counts[-1]}")
ok = counts == expected_counts
print("PASS  ->  open step3_aliasing.py" if ok else f"FAIL  (expected counts {expected_counts})")



if ok:
    fig, ax = plt.subplots(len(cases), 1, figsize=(10,7))
    for a, (F, Fs, d) in zip(ax, cases):
        t = np.linspace(0, d, 2000)
        sine = np.sin(2 * np.pi * F * t)
        n_t, x_s = sampler(F, Fs, d)
        a.plot(t, sine, label="CT Signal")
        a.stem(n_t, x_s, linefmt="C1-", markerfmt="C1o", basefmt=" ", label="DT Signal")
        a.legend()
        a.set_title(f"Sampling Freq.: {Fs} Hz, Signal Freq.: {F} Hz, Duration: {d}s")
        a.set_ylabel("Amplitude")
        a.grid(alpha=0.3)
    ax[-1].set_xlabel("Time(s)")
    plt.tight_layout()
    plt.show()

















# if ok:
#     fig, axes = plt.subplots(len(cases), 1, figsize=(10, 12))
#     for ax, (F, Fs, d) in zip(axes, cases):
#         t = np.linspace(0, d, 2000)
#         n_t, x_s = sample(F, Fs, d)
#         ax.plot(t, np.sin(2 * np.pi * F * t), alpha=.5, label="CT signal")
#         ax.stem(n_t, x_s, linefmt="C1-", markerfmt="C1o", basefmt=" ", label=f"{len(n_t)} samples")
#         ax.set_title(f"F = {F} Hz sampled at Fs = {Fs} Hz for {d} s")
#         ax.legend()
#         ax.grid(alpha=.3)
#     axes[-1].set_xlabel("time (s)")
#     plt.tight_layout()
#     plt.show()
