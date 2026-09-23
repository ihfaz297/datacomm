# PCM DRILL  -  Sample -> Quantize -> Encode   (three TODO blocks, checker after each)
#
# Run:  python CE/practice/pcm_drill.py

import math
import numpy as np

# =====================================================================
# STAGE 1: SAMPLING.  Read the analog signal every Ts = 1/fs seconds.
#   Nyquist: fs must be >= 2 * f_max, or you alias.
# =====================================================================
f_signal = 5          # Hz
fs       = 40         # samples per second
duration = 0.2        # seconds  ->  fs * duration = 8 samples

# TODO: sample instants  t = [0, 1/fs, 2/fs, ...]   (int(fs * duration) of them)
t = []
t.extend([(i / fs) for i in range (int(fs * duration))])
# TODO: sample values    x = sin(2*pi*f_signal*t)  for each t
x = []
x.extend([math.sin(2 * math.pi * f_signal * n) for n in t])

# ---------------- checker 1 ----------------
ok1 = len(t) == 8 and abs(t[3] - 0.075) < 1e-9 and len(x) == 8 and abs(x[2] - 1.0) < 1e-9 and abs(x[6] + 1.0) < 1e-9
print("STAGE 1 sampling  :", "PASS" if ok1 else f"FAIL  (want 8 samples, t[3]=0.075, x[2]=1.0, x[6]=-1.0; got len={len(t)})")


# =====================================================================
# STAGE 2: QUANTIZATION.  Chop the amplitude range into L = 2**n zones.
#   delta   = (Vmax - Vmin) / L                 zone height
#   zone    = int((sample - Vmin) / delta)      which zone, 0 .. L-1  (clamp L -> L-1)
#   quant   = Vmin + (zone + 0.5) * delta       middle of that zone
#   error   = sample - quant                    always within +-delta/2
# This is the textbook Fig 4.26 setup: range -20..+20 V, 3 bits.
# =====================================================================
Vmin, Vmax = -20, 20
n_bits     = 3
samples    = [-6.1, 7.5, 16.2, -11.3, 19.7, -19.9]

# TODO: L and delta
L     = 2**3
delta = (Vmax - Vmin) / L
# TODO: zone list, quantized list, error list (one entry per sample)
zone  = []
zone.extend([int((s - Vmin) / delta) for s in samples])
quant = []
quant.extend([Vmin + (z + 0.5) * delta for z in zone])
error = []
error.extend([samples[i] - zone[i] for i in range(0, len(samples))]) 

# ---------------- checker 2 ----------------
ok2 = (L == 8 and delta == 5
       and zone  == [2, 5, 7, 1, 7, 0]
       and quant == [-7.5, 7.5, 17.5, -12.5, 17.5, -17.5])
print("STAGE 2 quantize  :", "PASS" if ok2 else f"FAIL  (want L=8 delta=5 zone=[2,5,7,1,7,0] quant=[-7.5,7.5,17.5,-12.5,17.5,-17.5]; got L={L} delta={delta} zone={zone} quant={quant})")


# =====================================================================
# STAGE 3: ENCODING.  Zone number -> n-bit binary string.
#   format(zone, '03b')  gives '010' for zone 2 when n_bits = 3
#   bit rate = n_bits * fs          SNR_dB = 6.02 * n_bits + 1.76
# =====================================================================
# TODO: codes list, one binary string per zone
codes     = []
codes.extend([format(z, '03b') for z in zone])
# TODO: join the codes into one bit stream string
bitstream = "".join(codes)
# TODO: the two formulas
bit_rate  = 3 * fs
snr_db    = 6.02 * 3 + 1.76

# ---------------- checker 3 ----------------
ok3 = (codes == ['010', '101', '111', '001', '111', '000']
       and bitstream == '010101111001111000'
       and bit_rate == 120 and snr_db is not None and abs(snr_db - 19.82) < 1e-6)
print("STAGE 3 encode    :", "PASS" if ok3 else f"FAIL  (want codes=['010','101','111','001','111','000'], bit_rate=120, snr=19.82; got {codes} {bit_rate} {snr_db})")

print(f"{'samples':>8} {'zone':>4} {'quant':>6} {'error':>6} code")
for s, z, q,e,c in zip(samples,zone,quant,error,codes):
    print(f"{s:>8} {z:>4} {q:>6} {e:>6} {c}")