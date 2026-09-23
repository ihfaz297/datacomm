import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io, contextlib, sys, os
plt.show = lambda *a, **k: None
D = r"C:\Users\ADIB\OneDrive\Desktop\datacomm\DSP\practice"

SOL = {
"step1_ct_signals.py": [
    ("t = None", "t = np.linspace(0, periods / f, N)"),
    ("sine     = None", "sine     = np.sin(2*np.pi*f*t)"),
    ("square   = None", "square   = np.sign(np.sin(2*np.pi*f*t))"),
    ("triangle = None", "triangle = (2/np.pi)*np.arcsin(np.sin(2*np.pi*f*t))"),
],
"step2_sampling.py": [
    ("    n_t = None\n    x_s = None", "    Ts = 1/Fs\n    n_t = np.arange(0, duration, Ts)\n    x_s = np.sin(2*np.pi*F*n_t)"),
],
"step3_aliasing.py": [
    ("x10  = None", "x10  = np.sin(2*np.pi*10*n_t)"),
    ("x110 = None", "x110 = np.sin(2*np.pi*110*n_t)"),
    ("    # TODO: fd, wrap it, return abs(...) * Fs\n    return None", "    fd = F/Fs\n    return abs(fd - round(fd))*Fs"),
],
"step4_quantization_image.py": [
    ("gray = None", "gray = img.mean(axis=2)"),
    ("    # TODO: step, zone, return zone * step\n    return None", "    step = 256/L\n    zone = np.floor(image/step)\n    return zone*step"),
],
"step5_dt_sequences.py": [
    ('    """delta[n - k] on index axis n."""\n    # TODO\n    return None', '    return (n == k).astype(int)'),
    ('    """u[n - k] on index axis n."""\n    # TODO\n    return None', '    return (n >= k).astype(int)'),
    ("rect = None", "rect = step(n, -2) - step(n, 3)"),
    ("combo = None", "combo = 2*impulse(n, -1) + impulse(n, 1) + step(n, 3)"),
    ("rect_folded = None", "rect_folded = rect[::-1]"),
],
"step5b_dt_operations.py": [
    ('    """y[n] = x[n - k].  Returns (n_new, y)."""\n    # TODO\n    return None, None', '    return n + k, x.copy()'),
    ('    """y[n] = x[-n].  Returns (n_new, y)."""\n    # TODO\n    return None, None', '    return -n[::-1], x[::-1]'),
    ('    # TODO: y = np.zeros(len(n_common)); for each i, v in zip(n, x): y[np.where(n_common == i)] = v\n    return None', '    y = np.zeros(len(n_common), dtype=int)\n    for i, v in zip(n, x): y[np.where(n_common == i)] = v\n    return y'),
    ('    # TODO: n_common = np.arange(min(n1[0], n2[0]), max(n1[-1], n2[-1]) + 1); then on_axis both and add\n    return None, None', '    n_common = np.arange(min(n1[0], n2[0]), max(n1[-1], n2[-1]) + 1)\n    return n_common, on_axis(n1, x1, n_common) + on_axis(n2, x2, n_common)'),
    ('def upsample(x, L):\n    # TODO\n    return None', 'def upsample(x, L):\n    y = np.zeros(L*len(x), dtype=int); y[::L] = x; return y'),
    ('def downsample(x, M):\n    # TODO\n    return None', 'def downsample(x, M):\n    return x[::M]'),
],
"step6_convolution.py": [
    ("            pass\n", "            j = n - k\n            if 0 <= j < M:\n                y[n] += x[k]*h[j]\n                terms.append(f\"x[{k}]*h[{j}]={x[k]*h[j]}\")\n"),
],
"step7_correlation.py": [
    ('    # TODO: r = np.convolve(x, y[::-1]);  lags = np.arange(-(len(y) - 1), len(x))\n    return None, None', '    return np.arange(-(len(y)-1), len(x)), np.convolve(x, y[::-1])'),
    ('    # TODO: xcorr of x with itself\n    return None, None', '    return xcorr(x, x)'),
],
"step8_moving_average.py": [
    ("s = None", "s = 2*n*0.9**n"),
    ("d = None", "d = np.random.rand(50) - 0.5"),
    ("x = None", "x = s + d"),
    ("X1 = None", "X1 = np.zeros(50)\nfor _ in range(50):\n    X1 += s + (np.random.rand(50) - 0.5)\nX1 /= 50"),
    ("y_ma = None", "y_ma = np.convolve(x, np.ones(M)/M, mode='same')"),
],
"step9_spectrum_audio.py": [
    ("    # TODO: rfft and rfftfreq, magnitude = np.abs(X)\n    return None, None", "    X = np.fft.rfft(x)\n    return np.fft.rfftfreq(len(x), 1/Fs), np.abs(X)"),
    ("    # TODO: f, mag = spectrum(x, Fs); return f[np.argmax(mag[1:]) + 1]\n    return None", "    f, mag = spectrum(x, Fs)\n    return f[np.argmax(mag[1:]) + 1]"),
    ("tri_shifted = None", "X = np.fft.rfft(tri440); X[0] = 100*len(t); tri_shifted = np.fft.irfft(X, n=len(t))"),
],
}

allok = True
for fname, reps in SOL.items():
    src = open(os.path.join(D, fname), encoding="utf-8").read()
    for old, new in reps:
        assert old in src, f"{fname}: pattern not found: {old[:50]!r}"
        src = src.replace(old, new, 1)
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(src, fname, "exec"), {"__name__": "__main__", "__file__": os.path.join(D, fname)})
        out = buf.getvalue()
    except Exception as e:
        out = buf.getvalue() + f"\nEXCEPTION: {type(e).__name__}: {e}"
    passed = "PASS" in out and "EXCEPTION" not in out
    allok &= passed
    print(f"{'PASS' if passed else 'FAIL'}  {fname}")
    if not passed:
        print(out[-1500:])
    plt.close("all")
print("\nALL CHECKERS OK" if allok else "\nSOME FAILED")
