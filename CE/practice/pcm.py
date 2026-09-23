# PCM in three stages: SAMPLE -> QUANTIZE -> ENCODE   (Forouzan 4.2.1)
# Run:  python practice/pcm.py

import numpy as np
import matplotlib.pyplot as plt

# ---------- inputs (the question will give some of these) ----------
f_signal = 5          # Hz, analog signal frequency  (fmax)
fs       = 40         # Hz, sampling rate  (Nyquist says fs >= 2 * fmax)
n_bits   = 3          # bits per sample
Vmax, Vmin = 1, -1    # amplitude range of the signal
duration = 0.2        # seconds to show (1 period of a 5 Hz wave)

# ---------- stage 0: the "analog" signal (dense time axis, just for drawing) ----------
t_analog = np.linspace(0, duration, 1000)
x_analog = np.sin(2 * np.pi * f_signal * t_analog)

# ---------- stage 1: SAMPLING (PAM) ----------
Ts = 1 / fs                                   # sampling interval
t_s = np.arange(0, duration, Ts)              # sample instants
x_s = np.sin(2 * np.pi * f_signal * t_s)      # sample values

# ---------- stage 2: QUANTIZATION ----------
L     = 2 ** n_bits                           # number of levels
delta = (Vmax - Vmin) / L                     # step size (height of one zone)
zone  = np.floor((x_s - Vmin) / delta).astype(int)   # which zone each sample falls in: 0 .. L-1
zone  = np.clip(zone, 0, L - 1)               # a sample exactly at Vmax would give L, clamp it
x_q   = Vmin + (zone + 0.5) * delta           # quantized value = middle of the zone
error = x_s - x_q                             # quantization error, always within +-delta/2

# ---------- stage 3: ENCODING ----------
codes = [format(z, f"0{n_bits}b") for z in zone]      # zone number -> n-bit binary string
bitstream = "".join(codes)

# ---------- numbers the question usually asks for ----------
bit_rate = n_bits * fs                        # bps
snr_db   = 6.02 * n_bits + 1.76               # quantization SNR for a full-scale sine

print(f"Signal frequency      : {f_signal} Hz  -> Nyquist rate = {2*f_signal} Hz")
print(f"Sampling rate fs      : {fs} Hz  (Ts = {Ts:.4f} s)  -> {len(t_s)} samples in {duration} s")
print(f"Bits per sample n     : {n_bits}  -> L = {L} levels, step delta = {delta:.4f} V")
print(f"Bit rate              : {bit_rate} bps")
print(f"SNR(dB) = 6.02n+1.76  : {snr_db:.2f} dB")
print()
print(f"{'i':>2} {'t(s)':>7} {'sample':>8} {'zone':>4} {'quantized':>9} {'error':>7}  code")
for i in range(len(t_s)):
    print(f"{i:>2} {t_s[i]:>7.4f} {x_s[i]:>8.4f} {zone[i]:>4} {x_q[i]:>9.4f} {error[i]:>7.4f}  {codes[i]}")
print("\nEncoded bit stream:", bitstream)

# ---------- plot: analog + samples + quantized levels ----------
plt.figure(figsize=(11, 5))
plt.plot(t_analog, x_analog, label="analog signal", alpha=0.6)
plt.stem(t_s, x_s, linefmt="C1-", markerfmt="C1o", basefmt=" ", label="samples (PAM)")
plt.step(t_s, x_q, where="post", color="C2", linewidth=2, label="quantized (PCM)")
for lvl in range(L + 1):                                     # zone boundaries
    plt.axhline(Vmin + lvl * delta, color="gray", linestyle="--", alpha=0.3)
for i in range(len(t_s)):                                    # code word above each sample
    plt.text(t_s[i], Vmax + 0.08, codes[i], ha="center", fontsize=8, rotation=90)
plt.ylim(Vmin - 0.1, Vmax + 0.45)
plt.xlabel("Time (s)"); plt.ylabel("Amplitude (V)")
plt.title(f"PCM: fs = {fs} Hz, n = {n_bits} bits, L = {L} levels")
plt.legend(loc="lower left"); plt.tight_layout()
plt.show()
