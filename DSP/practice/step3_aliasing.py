# DSP STEP 3 / 9  -  Aliasing in the time domain   (syllabus 2b, Assignment 3 Tasks 1, 4, post-lab)
#
# Two CT sinusoids whose frequencies differ by a multiple of Fs give IDENTICAL samples.
#   10 Hz and 110 Hz sampled at 100 Hz  ->  110 = 10 + 1*100  ->  same samples.
#
# Digital frequency  fd = F / Fs   (cycles per sample).  Only the range -0.5 .. 0.5 is unique.
# Apparent (aliased) frequency:
#   fd_wrapped = fd - round(fd)              brings fd into -0.5 .. 0.5
#   F_apparent = abs(fd_wrapped) * Fs        what you hear / see
# Nyquist: no aliasing if F <= Fs / 2.

import numpy as np
import matplotlib.pyplot as plt
# ---- Part A: Assignment 3 Task 1 ----
Fs, duration = 100, 0.2
n_t = np.arange(0, duration, 1 / Fs)
# TODO: samples of the 10 Hz and 110 Hz sinusoids at these instants
x10  = np.sin(2 * np.pi * 10 * n_t)
x110 = np.sin(2 * np.pi * 110 * n_t)

# ---- Part B: the alias formula ----
def apparent_freq(F, Fs):
    """Frequency (Hz) that a sinusoid of F Hz appears to have after sampling at Fs Hz."""
    # TODO: fd, wrap it, return abs(...) * Fs
    fd = F / Fs
    f_w = fd - round(fd)
    F_real = abs(f_w) * Fs

    return F_real

# ---------------- checker: don't edit below ----------------
okA = x10 is not None and x110 is not None and np.allclose(x10, x110)
print("Part A 10 Hz vs 110 Hz at Fs=100:", "identical samples  ok" if okA else "FAIL (samples should be identical)")

# Assignment 3 post-lab table: F in kHz at Fs = 8 kHz -> what you hear
table = {1: 1, 2: 2, 3: 3, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0, 9: 1, -1: 1, -2: 2, 25: 1}
okB = True
for F, want in table.items():
    got = apparent_freq(F, 8)
    good = got is not None and abs(got - want) < 1e-9
    okB &= good
    print(f"F = {F:>3} kHz  Fs = 8 kHz  ->  sounds like {got} kHz   {'ok' if good else f'expected {want}'}   {'no aliasing' if abs(F) <= 4 else 'ALIASING'}")
# Assignment 3 Task 4: 40 Hz cosine at 30 samples/s
fd = 40 / 30
print(f"Task 4: fd = 40/30 = {fd:.4f}  ->  wrapped = {fd - round(fd):+.4f}  ->  apparent {apparent_freq(40, 30)} Hz")
ok = okA and okB
print("PASS  ->  open step4_quantization_image.py" if ok else "FAIL")

if ok:
    t = np.linspace(0, duration, 2000)
    plt.subplots(1, 1, figsize=(10, 4))
    plt.plot(t, np.sin(2 * np.pi * 10 * t), label="10 Hz")
    plt.plot(t, np.sin(2 * np.pi * 110 * t), alpha=.4, label="110 Hz")
    plt.stem(n_t, x10, linefmt="k-", markerfmt="ko", basefmt=" ", label="samples at Fs = 100 Hz (both!)")
    plt.title("Aliasing: 110 Hz sampled at 100 Hz looks exactly like 10 Hz")
    plt.xlabel("time (s)"); plt.legend(); plt.grid(alpha=.3)
    plt.tight_layout(); plt.show()
