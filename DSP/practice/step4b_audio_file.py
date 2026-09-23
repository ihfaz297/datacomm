# DSP STEP 4b  -  If he drops an audio file: read a WAV with only the standard library + numpy
#
# WAV = header + raw PCM samples. Python's built-in `wave` module (no install, always allowed) reads the header;
# numpy turns the raw bytes into numbers.
#   with wave.open("file.wav", "rb") as w:
#       Fs       = w.getframerate()            samples per second
#       channels = w.getnchannels()            1 mono, 2 stereo
#       width    = w.getsampwidth()            bytes per sample: 2 -> int16
#       N        = w.getnframes()              number of samples
#       raw      = w.readframes(N)             bytes
#   x = np.frombuffer(raw, dtype=np.int16)     the samples   (if stereo: x = x[::2] keeps the left channel)
#   duration = N / Fs
#   t = np.arange(N) / Fs                      time axis
#
# Then every syllabus item applies to x:
#   sampling / aliasing : downsample by M -> x[::M] at Fs/M  (no anti-alias filter, so high notes fold down)
#   quantization        : q = np.round(x / step) * step  with step = 65536 / L
# mp3 cannot be read this way (compressed). If he gives mp3, say so and ask for wav.

import wave
import numpy as np
import matplotlib.pyplot as plt

# ---- make a test file so there is something to read (in the exam this part doesn't exist) ----
Fs0 = 8000
t0 = np.arange(0, 1.0, 1 / Fs0)
tone = (0.6 * np.sin(2 * np.pi * 440 * t0) + 0.3 * np.sin(2 * np.pi * 3000 * t0))
with wave.open("DSP/practice/test_tone.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(Fs0)
    w.writeframes((tone * 32767).astype(np.int16).tobytes())

# ---- the part you'd type in the exam ----
path = "DSP/practice/test_tone.wav"        # in the exam: whatever he gives you

# TODO: open with wave, read Fs, channels, width, N, raw
Fs = channels = width = N = None
raw = None
# TODO: x from raw (int16), duration, t
x = None
duration = None
t = None

# TODO: downsample by 4 (keep every 4th sample) -> x_ds at Fs_ds
M = 4
x_ds  = None
Fs_ds = None

# TODO: quantize x to L = 16 levels (4 bits) using step = 65536 / L
L = 16
step = None
x_q  = None

# ---------------- checker: don't edit below ----------------
ok = Fs == 8000 and channels == 1 and width == 2 and N == 8000
ok = ok and x is not None and len(x) == 8000 and x.dtype == np.int16 and abs(duration - 1.0) < 1e-9 and t is not None and abs(t[-1] - (N - 1) / Fs) < 1e-9
ok = ok and x_ds is not None and len(x_ds) == 2000 and Fs_ds == 2000
ok = ok and x_q is not None and len(np.unique(x_q)) <= L + 1
print(f"Fs = {Fs} Hz, channels = {channels}, {width * 8 if width else None}-bit, N = {N} samples, duration = {duration} s")
print(f"downsampled by {M}: {None if x_ds is None else len(x_ds)} samples at {Fs_ds} Hz   (3000 Hz tone now aliases: apparent {abs(3000 - round(3000/2000)*2000)} Hz)")
print(f"quantized to {L} levels: {None if x_q is None else len(np.unique(x_q))} distinct values")
print("PASS  ->  audio covered." if ok else "FAIL")

if ok:
    fig, ax = plt.subplots(3, 1, figsize=(11, 8))
    ax[0].plot(t[:200], x[:200]); ax[0].set_title(f"first 200 samples of the WAV (Fs = {Fs} Hz)")
    ax[1].stem(np.arange(50) / Fs_ds, x_ds[:50], basefmt=" "); ax[1].set_title(f"downsampled by {M}: Fs = {Fs_ds} Hz")
    ax[2].plot(t[:200], x[:200], alpha=.4, label="original"); ax[2].step(t[:200], x_q[:200], where="mid", label=f"{L} levels"); ax[2].legend(); ax[2].set_title("quantized")
    for a in ax: a.set_xlabel("time (s)"); a.grid(alpha=.3)
    plt.tight_layout(); plt.show()
