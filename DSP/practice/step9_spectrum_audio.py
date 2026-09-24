# DSP STEP 9 / 9  -  Spectrum with numpy FFT, aliased harmonics, and listening   (Assignments 1 & 2, no ThinkDSP)
#
#   X     = np.fft.rfft(x)                      complex spectrum, positive frequencies only
#   freqs = np.fft.rfftfreq(len(x), 1 / Fs)     the Hz axis for X   (0 .. Fs/2)
#   plot abs(X) against freqs
#
# Square wave  -> odd harmonics f, 3f, 5f ...  falling like 1/k
# Triangle     -> odd harmonics falling like 1/k^2  (so only the first few are visible)
# Any harmonic above Fs/2 ALIASES down to  apparent = |k*f - round(k*f/Fs)*Fs|   (same formula as step 3)
#   1100 Hz square at Fs = 10 kHz:  3300 ok, 5500 -> 4500, 7700 -> 2300, 9900 -> 100 ...  the spectrum fills with junk
# Assignment 1 Q5: cosines at 4500 and 5500 Hz sampled at 10 kHz give the SAME spectrum peak at 4500.
# Assignment 2 Q1b: setting X[0] (the DC bin) to a big number then inverse-FFT shifts the whole waveform UP by a constant.
#
# Listening is optional (sounddevice is installed here, not in the exam): sd.play(x / abs(x).max(), Fs); sd.wait()

import numpy as np
import matplotlib.pyplot as plt

Fs, duration = 10000, 0.5
t = np.arange(0, duration, 1 / Fs)

def square(f):   return np.sign(np.sin(2 * np.pi * f * t))
def triangle(f): return (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * f * t))

def spectrum(x, Fs):
    """Return (freqs, magnitude) of x sampled at Fs."""
    # TODO: rfft and rfftfreq, magnitude = np.abs(X)
    X = np.fft.rfft(x)
    fs = np.fft.rfftfreq(len(x), 1/Fs)
    return fs, np.abs(X)

def peak_freq(x, Fs):
    """Frequency (Hz) of the largest spectral peak, ignoring DC."""
    # TODO: 
    f, mag = spectrum(x, Fs); return f[np.argmax(mag[1:]) + 1]

# Assignment 2 Q1b: add DC by editing bin 0 and inverse transforming
tri440 = triangle(440)
# TODO: 
X = np.fft.rfft(tri440); X[0] = 100 * len(t); tri_shifted = np.fft.irfft(X, n=len(t))
# tri_shifted = None

# ---------------- checker: don't edit below ----------------
ok = True
for name, x, want in [("square 100 Hz", square(100), 100), ("triangle 200 Hz", triangle(200), 200),
                      ("cos 4500 Hz", np.cos(2*np.pi*4500*t), 4500), ("cos 5500 Hz (aliased!)", np.cos(2*np.pi*5500*t), 4500)]:
    p = peak_freq(x, Fs)
    good = p is not None and abs(p - want) < 3
    ok &= good
    print(f"{name:26s} peak at {p} Hz   {'ok' if good else f'expected {want}'}")
f, mag = spectrum(square(100), Fs)
if f is not None:
    top3 = sorted(f[np.argsort(mag)[-3:]]); print("square 100 Hz, three strongest bins:", top3, " (want 100, 300, 500)")
    ok &= all(abs(a - b) < 3 for a, b in zip(top3, [100, 300, 500]))
good = tri_shifted is not None and abs(tri_shifted.mean() - 100) < 1 and abs(tri440.mean()) < 0.05
ok &= good
print("DC shift: triangle mean", None if tri_shifted is None else round(float(tri_shifted.mean()), 2), "(want ~100)", "ok" if good else "FAIL")
print("PASS  ->  DSP drills done." if ok else "FAIL")

if ok:
    fig, ax = plt.subplots(3, 2, figsize=(13, 9))
    for row, (name, x) in enumerate([("square 100 Hz", square(100)), ("square 1100 Hz (harmonics alias)", square(1100)), ("triangle 200 Hz", triangle(200))]):
        f, mag = spectrum(x, Fs)
        ax[row,0].plot(t[:300], x[:300]); ax[row,0].set_title(name + "  (first 30 ms)"); ax[row,0].set_xlabel("t (s)")
        ax[row,1].plot(f, mag); ax[row,1].set_title("spectrum"); ax[row,1].set_xlabel("Hz"); ax[row,1].set_xlim(0, Fs/2)
    plt.tight_layout(); plt.show()
