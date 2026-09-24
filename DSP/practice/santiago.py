import wave
import numpy as np
import matplotlib.pyplot as plt

path = "DSP/practice/test_tone.wav" 

with wave.open(path, "rb") as w:
    Fs = w.getframerate()
    N= w.getnframes()
    raw = w.readframes(N)
x = np.frombuffer(raw, dtype=np.int16)
duration = N / Fs
t = np.arange(N) / Fs

x_down = x[::4]
fs = Fs/4

L = 16
step = 65536 / L
q_new = step * np.floor(x / step)

plt.plot(t[:200], x_down[:200])
plt.step(t, q_new)
plt.show()