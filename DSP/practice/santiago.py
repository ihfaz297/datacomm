import numpy as np, matplotlib.pyplot as plt
Fs = 10000; t = np.arange(0, 0.5, 1/Fs)          # sample instants for 0.5 s at 10 kHz
f=4800

sine     = np.sin(2*np.pi*f*t)
square   = np.sign(np.sin(2*np.pi*f*t))
triangle = (2/np.pi)*np.arcsin(np.sin(2*np.pi*f*t))


per = int(3*Fs/f); plt.plot(t[:per], square[:per]); plt.show()