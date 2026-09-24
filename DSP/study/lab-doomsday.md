# DSP lab doomsday sheet

Allowed libraries in the exam: **numpy, matplotlib, SymPy**. Nothing else. No ThinkDSP, no librosa, no scipy.
Official syllabus is three items (CT signals, sampling/aliasing/quantization, DT sequences). Convolution and
spectrum are **not** on it. They are here because the assignments had them and sir might paste one.

Every block below was run and checked on 24 Sep 2026. Type it, change the numbers, done.

---

## 0. The two lines everything starts with

```python
import numpy as np, matplotlib.pyplot as plt
Fs = 10000; t = np.arange(0, 0.5, 1/Fs)          # sample instants for 0.5 s at 10 kHz
```

Three waveforms, one line each:

```python
sine     = np.sin(2*np.pi*f*t)
square   = np.sign(np.sin(2*np.pi*f*t))
triangle = (2/np.pi)*np.arcsin(np.sin(2*np.pi*f*t))
```

Plot "3 periods" means slice the first `int(3*Fs/f)` samples:

```python
per = int(3*Fs/f); plt.plot(t[:per], x[:per]); plt.show()
```

---

## 1. Convolution, step by step  (Assignment 4 Q2)

The formula is `y[n] = sum_k x[k] * h[n-k]`. Two loops: outer over output n, inner over k.
The only condition is that `n-k` must be a real index of h.

```python
x = np.array([1, 2, 3, 1]); h = np.array([1, 1, 1])
y = np.zeros(len(x) + len(h) - 1)               # output length rule
for n in range(len(y)):
    terms = []
    for k in range(len(x)):
        if 0 <= n-k < len(h):                    # does h[n-k] exist?
            y[n] += x[k] * h[n-k]
            terms.append(f"x[{k}]h[{n-k}]={x[k]*h[n-k]}")
    print(f"y[{n}] = " + " + ".join(terms) + f" = {y[n]:g}")
print(y, np.convolve(x, h))                      # proof line, they match
```

Output it prints, so you know it worked:

```
y[0] = x[0]h[0]=1 = 1
y[1] = x[0]h[1]=1 + x[1]h[0]=2 = 3
y[2] = x[0]h[2]=1 + x[1]h[1]=2 + x[2]h[0]=3 = 6
y[3] = x[1]h[2]=2 + x[2]h[1]=3 + x[3]h[0]=1 = 6
y[4] = x[2]h[2]=3 + x[3]h[1]=1 = 4
y[5] = x[3]h[2]=1 = 1
```

If the arrow is not under the first sample: output starts at `start_x + start_h`. Axis is
`np.arange(start, start + len(y))`. Plot with `plt.stem(n_axis, y)`.

**Absolute doomsday:** `y = np.convolve(x, h); plt.stem(y); plt.show()`. Marks for the answer, none for "step by step".

---

## 2. Correlation  (Assignment 4 Q3)

Correlation is convolution with the second one **flipped**. That is the whole trick.

```python
a = np.array([1, 2, 3, 4]); b = np.array([1, 1, 2])
r    = np.convolve(a, b[::-1])                   # cross-correlation r_ab
lags = np.arange(-(len(b)-1), len(a))            # lag axis, same length as r
plt.stem(lags, r); plt.show()
print(np.correlate(a, b, "full"))                # proof line, matches r
```

Autocorrelation is the same with `a` twice: `np.convolve(a, a[::-1])`, lags `np.arange(-(len(a)-1), len(a))`.
Its peak is at lag 0 and equals `sum(a**2)`. Say that in the report, it is a free mark.

---

## 3. Moving average / noise removal  (Assignment 4 Q4)

```python
n = np.arange(50); s = 2*n*0.9**n                # clean signal
d = np.random.rand(50) - 0.5                     # noise, zero mean
x = s + d                                        # corrupted
X1 = np.zeros(50)
for _ in range(50):                              # 50 fresh noisy copies, summed
    X1 += s + (np.random.rand(50) - 0.5)
X1 /= 50                                         # ensemble average, noise cancels
```

Plot s, d, x, X1 as four `plt.stem` (or `plt.plot`) calls. If he says "moving average filter" and means
the M-point one from the slides, it is one line on the single noisy x:

```python
M = 5; y = np.convolve(x, np.ones(M)/M, mode="same")
```

---

## 4. Spectrum with numpy only  (Assignments 1 and 2, no ThinkDSP)

ThinkDSP's `make_spectrum()` is banned. This is the replacement. Two lines.

```python
X = np.abs(np.fft.rfft(x))                       # magnitude of each frequency
f = np.fft.rfftfreq(len(x), 1/Fs)                # the Hz axis, 0 .. Fs/2
plt.plot(f, X); plt.xlabel("Hz"); plt.show()
```

Strongest peak, skipping DC: `f[np.argmax(X[1:]) + 1]`.

What to write next to the plot:

- Square wave: odd harmonics f, 3f, 5f, ... falling like 1/k. Checked: 100 Hz square gives peaks at 100, 300, 500.
- Triangle: odd harmonics falling like 1/k², so only the first few show.
- Any harmonic above Fs/2 aliases to `|k*f - round(k*f/Fs)*Fs|`. 1100 Hz square at 10 kHz: 5500 lands on 4500, 7700 on 2300, 9900 on 100. The spectrum fills with junk, and yes you can hear it.
- A1 Q5: cos at 4500 and cos at 5500, both at Fs = 10 kHz, give the **same** peak at 4500. That is the problem. 5500 is above Fs/2 = 5000.

**A2 Q1b, "set hs[0] = 100":** bin 0 is DC, the mean. Editing it and inverse transforming lifts the whole waveform up by a constant.

```python
X = np.fft.rfft(tri440); X[0] = 100*len(t); x2 = np.fft.irfft(X, n=len(t))
plt.plot(t, tri440); plt.plot(t, x2); plt.show()   # x2 is tri440 shifted up by 100
```

(`100*len(t)` because numpy's bin 0 is the sum, not the mean, and ThinkDSP's hs[0] is scaled differently. The effect is what he marks.)

"Listen to the wave": in Colab, `from IPython.display import Audio; Audio(x, rate=Fs)`. That is IPython, which Colab always has. If he objects, skip it, the plot is the marks.

---

## 5. Audio file, if one appears

The syllabus says an **image** file will be provided, not audio. If a WAV appears anyway, `wave` is standard library, not a third-party import:

```python
import wave
with wave.open("file.wav", "rb") as w:
    Fs = w.getframerate(); N = w.getnframes(); raw = w.readframes(N)   # read INSIDE the with
x = np.frombuffer(raw, dtype=np.int16)
```

mp3 cannot be read with the allowed libraries. Say so, ask for WAV.

---

## Mistakes already made once, so not again

- Reading `readframes` after the `with` block closes the file. Keep it indented.
- Adding two sequences with different start indices by plain `+`. Put both on a common axis first (step5b `on_axis`).
- `librosa.load` without `sr=None` silently resamples to 22050 Hz. Irrelevant now, librosa is banned.
- `Fs / M` is a float. Use `Fs // M` when a checker compares to an int.
