import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io, contextlib, sys, os
plt.show = lambda *a, **k: None
D = r"C:\Users\ADIB\OneDrive\Desktop\datacomm\DSP\practice"
# step4 quantizes a picture that only exists on the author's machine -> skip when the file is absent
DATA_FILES = {"step4_quantization_image.py": [r"C:\Users\adib\Pictures\Saved Pictures\niche_stuff.jpg"]}

SOL = {
"step1_ct_signals.py": [
    ("t = None", "t = np.linspace(0, periods / f, N)"),
    ("sine     = None", "sine     = np.sin(2*np.pi*f*t)"),
    ("square   = None", "square   = np.sign(np.sin(2*np.pi*f*t))"),
    ("triangle = None", "triangle = (2/np.pi)*np.arcsin(np.sin(2*np.pi*f*t))"),
],
# steps 2, 3, 5, 5b and 9 already carry their solutions inside the drill file itself, so they need no
# replacements here.  step4 loads a private picture and is skipped unless that file exists (see below).
"step4_quantization_image.py": [],
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
# ---- steps 10-13: the transforms / discrete-time-systems topic (lab exam 2 topic 4, TT2) ----
"step10_dtft.py": [
    ("    # TODO: return exp(-1j * outer(w, n)) @ x\n    return None",
     "    return np.exp(-1j*np.outer(w, n)) @ x"),
    ("    # TODO: 1 / (1 - a * exp(-1j*w))\n    return None",
     "    return 1 / (1 - a*np.exp(-1j*w))"),
    ("    # TODO: sin(w*M/2) / (M*sin(w/2)) * exp(-1j*w*(M-1)/2);  the w = 0 sample must come out as 1\n    #       (sin(w/2) = 0 there -> evaluate the quotient inside np.errstate(divide=\"ignore\", invalid=\"ignore\"))\n    return None",
     "    w = np.asarray(w, dtype=float)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        H = np.sin(w*M/2) / (M*np.sin(w/2)) * np.exp(-1j*w*(M-1)/2)\n    return np.where(w == 0, 1.0 + 0j, H)"),
],
"step11_ztransform.py": [
    ('    """Closed form X(z) of x[n] = a^n u[n] + b^n u[-n-1]   (past final paper Q6a)."""\n    # TODO: 1/(1 - a_/z_) - 1/(1 - b_/z_)\n    return None',
     "    return 1/(1 - a_/z_) - 1/(1 - b_/z_)"),
    ('    """True when z_ lies inside the ROC annulus |a| < |z| < |b| of that two-sided sequence."""\n    # TODO\n    return None',
     "    return abs(a_) < abs(z_) < abs(b_)"),
    ("    # TODO: num = [1, 0 ... 0, -a_**M_]   (degree M, i.e. z^M - a^M)\n    #       den = [1, -a_, 0 ... 0]      (degree M, i.e. z^(M-1) (z - a))\n    #       zp, zr = np.roots(den), np.roots(num);  drop the shared root z = a_ from both\n    return None, None",
     "    num = np.concatenate(([1.0], np.zeros(M_-1), [-a_**M_]))\n    den = np.concatenate(([1.0, -a_], np.zeros(M_-1)))\n    zp, zr = np.roots(den), np.roots(num)\n    keep = lambda r: r[np.abs(r - a_) > 1e-6]\n    return keep(zp), keep(zr)"),
],
"step12_dft_fft.py": [
    ("    # TODO: for each k: X[k] = sum_n x[n] * exp(-2j*pi*k*n/N)\n    return None",
     "    k = np.arange(N)\n    return np.exp(-2j*np.pi*np.outer(k, np.arange(N))/N) @ x"),
    ("    # TODO: for each n: x[n] = (1/N) * sum_k X[k] * exp(+2j*pi*k*n/N)\n    return None",
     "    k = np.arange(N)\n    return (np.exp(+2j*np.pi*np.outer(k, np.arange(N))/N) @ X) / N"),
    ("    # TODO: y[n] = sum_k xp[k] * hp[(n - k) % N]\n    return None",
     "    return np.array([sum(xp[k]*hp[(n - k) % N] for k in range(N)) for n in range(N)])"),
    ("    # TODO: (N/2) * log2(N)\n    return None",
     "    return (N/2) * np.log2(N)"),
],
"step13_fir_window.py": [
    ("    # TODO: return sin(wc*k)/(pi*k) and set the k = 0 sample to wc/pi\n    return None",
     "    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        h = np.sin(wc*k)/(np.pi*k)\n    h[k == 0] = wc/np.pi\n    return h"),
    ("    # TODO: 'rect' 1 ; 'hann' 0.5 - 0.5cos(2pi n/M) ; 'hamming' 0.54 - 0.46cos(2pi n/M) ;\n    #       'blackman' 0.42 - 0.5cos(2pi n/M) + 0.08cos(4pi n/M)\n    return None",
     "    if kind == \"rect\":     return np.ones(M+1)\n    if kind == \"hann\":     return 0.5 - 0.5*np.cos(2*np.pi*n/M)\n    "
     "if kind == \"hamming\":  return 0.54 - 0.46*np.cos(2*np.pi*n/M)\n    "
     "if kind == \"blackman\": return 0.42 - 0.5*np.cos(2*np.pi*n/M) + 0.08*np.cos(4*np.pi*n/M)"),
    ("    # TODO: exp(-1j*outer(w, arange(len(h)))) @ h\n    return None",
     "    return np.exp(-1j*np.outer(w, np.arange(len(h)))) @ h"),
],
}

allok = True
for fname, reps in SOL.items():
    src = open(os.path.join(D, fname), encoding="utf-8").read()
    if any(not os.path.exists(p) for p in DATA_FILES.get(fname, [])):
        print(f"SKIP  {fname}   (needs a local input file)")
        plt.close("all")
        continue
    missing = []
    for old, new in reps:
        if old not in src:          # already solved in the file itself
            missing.append(" ".join(old.strip().splitlines()[0].split())[:58])
            continue
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
    note = f"   [{len(missing)} pattern(s) already in place]" if missing else ""
    print(f"{'PASS' if passed else 'FAIL'}  {fname}{note}")
    for m in missing:
        print(f"        stale SOL entry -> {m}")
    if not passed:
        print(out[-1500:])
    elif fname.startswith("step1"):        # steps 10-13 print their measurement tables
        print(out)
    plt.close("all")
print("\nALL CHECKERS OK" if allok else "\nSOME FAILED")
