import numpy as np
import matplotlib.pyplot as plt

f = 200
periods = 3
N = 2000

t=np.linspace(0, periods / f, N)
x=np.sin(2*np.pi*f*t)

square = np.sign(x)
triangle=(2/np.pi)*(np.arcsin(x))

fig, ax = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
signal = (x, square, triangle)
names = ("sine", "square", "triangle")
for a, sig, name in zip(ax, signal, names):
    a.plot(t, sig)
    a.grid(alpha=0.3)
    a.set_title(f"{name} signal")
    a.set_ylabel("Amplitude")
ax[-1].set_xlabel("Time(s)")
plt.tight_layout()
plt.show()