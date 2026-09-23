# DSP STEP 1 / 9  -  Generating "continuous-time" signals with numpy   (syllabus item 1)
#
# A CT signal on a computer = a very dense time axis + the formula evaluated on it.
#   t = np.linspace(start, stop, many_points)      dense axis, e.g. 1000 points
#   x = np.sin(2 * np.pi * f * t)                   sine of frequency f Hz
# "Plot 3 periods" means stop = 3 / f  (one period T = 1/f).
#
# Square and triangle WITHOUT scipy (only numpy is allowed in the exam):
#   square   = np.sign(np.sin(2*np.pi*f*t))                    +1 / -1
#   triangle = (2/np.pi) * np.arcsin(np.sin(2*np.pi*f*t))      -1 .. +1, straight edges
#
# Run:  python DSP/practice/step1_ct_signals.py

import numpy as np
import matplotlib.pyplot as plt

f = 200            # Hz
periods = 3
N = 1000           # points on the dense axis

# TODO: dense time axis covering `periods` periods
# t = None
t = np.linspace(0, periods/f, 1000)
# TODO: the three signals
# sine     = None
sine = np.sin(2*np.pi*f*t)

# square   = None
square = np.sign(sine)
# triangle = None
triangle = (2 / np.pi)*np.arcsin(sine)

# ---------------- checker: don't edit below ----------------
ok = t is not None and len(t) == N and abs(t[-1] - periods / f) < 1e-12
ok = ok and sine is not None and abs(sine[0]) < 1e-9 and abs(sine.max() - 1) < 1e-3
ok = ok and square is not None and set(np.unique(np.sign(square))) <= {-1.0, 0.0, 1.0} and abs(square).max() == 1
ok = ok and triangle is not None and abs(triangle.max() - 1) < 1e-2 and abs(triangle.min() + 1) < 1e-2
print("PASS  ->  open step2_sampling.py" if ok else "FAIL  (t must run 0 .. 3/f with 1000 points; sine starts at 0, peaks at 1; square is +-1; triangle spans -1..+1)")

if ok:
    fig , ax = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    signal = (sine, square, triangle)
    names = ("sine", "square", "triangle")
    for a, sig, name in zip(ax, signal, names):
        a.plot(t, sig)
        a.set_title(f"{name} wave, {f} Hz, {periods} cycles")
        a.set_ylabel("Amplitude")
        a.grid(alpha=0.3)
        plt.tight_layout()

    ax[-1].set_xlabel("Time(s)")
    plt.show()

    # fig, ax = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
    #     signal = (sine, square, triangle)
    #     names = ("sine", "square", "triangle")
    #     for a, sig, name in zip(ax, signal, names):
    #         a.plot(t, sig)
    #         a.set_title(f"{name} wave, f = {f} Hz, {periods} periods")
    #         a.set_ylabel("amplitude")
    #         a.grid(alpha=.3)
    #     ax[-1].set_xlabel("time (s)")
    #     plt.tight_layout()
    #     plt.show()
