"""Every number that goes into the DSP/study markdown files gets checked here first."""
import numpy as np

def df(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    return np.array([sum(x[n]*np.exp(-2j*np.pi*k*n/N) for n in range(N)) for k in range(N)])

def show(tag, a, places=4):
    a = np.asarray(a)
    if np.iscomplexobj(a):
        print(f"{tag:52s} " + " ".join(f"{v.real:.{places}f}{v.imag:+.{places}f}j" for v in a))
    else:
        print(f"{tag:52s} " + " ".join(f"{v:.{places}f}" for v in np.atleast_1d(a)))

# ---------------- TT2 Q3: 4-point DFT of {1,2,2,1} and {1,2,3} ----------------
x = np.array([1, 2, 2, 1.0]); h = np.array([1, 2, 3.0])
X, H = df(x), df([1, 2, 3, 0])   # h zero-padded to N = 4
show("DFT{1,2,2,1}", X)
show("DFT{1,2,3,0}", H)
show("X*H", X*H)
show("idft(X*H)  -> TT2 Q3 answer", np.rint(np.fft.ifft(X*H).real))

def circ(x, h, N):
    xp = np.zeros(N); xp[:len(x)] = np.asarray(x, dtype=float)
    hp = np.zeros(N); hp[:len(h)] = np.asarray(h, dtype=float)
    return np.array([sum(xp[k]*hp[(n-k) % N] for k in range(N)) for n in range(N)])

print("\n--- TT2 Q3 wrap table, term by term (h padded to 4 = {1,2,3,0}) ---")
hp = np.array([1, 2, 3, 0.0])
for n in range(4):
    terms = [(k, (n-k) % 4, x[k], hp[(n-k) % 4]) for k in range(4)]
    s = " + ".join(f"x[{k}]h[{m}]={xk:g}*{hm:g}" for k, m, xk, hm in terms)
    print(f"  y[{n}] = {s} = {sum(xk*hm for *_, xk, hm in terms):g}")
print("  circ N=4 =", circ(x, h, 4), "  linear =", np.convolve(x, h), "  circ N=6 =", circ(x, h, 6))

# ---------------- final Q3c / Q6c ----------------
a1 = np.array([1, 1, 2, 1.0]); h2 = np.array([1, 2, 1, 1.0])
print("\n--- final Q3c ---")
show("  DFT{1,1,2,1}", df(a1), 6); show("  DFT{1,2,1,1}", df(h2), 6)
print("  idft product =", np.rint(np.fft.ifft(df(a1)*df(h2)).real), " wrap method =", circ(a1, h2, 4))
h3 = np.array([1, 2, 1.0])
show("  DFT{1,2,1}", df(h3), 6)
print("  e^{-j2pi/3} =", np.round(np.exp(-2j*np.pi/3), 6), " e^{+j2pi/3} =", np.round(np.exp(2j*np.pi/3), 6))

# ---------------- final Q1h: convolution with negative index axis ----------------
xs = {-2: -1, -1: 3, 0: 2, 1: 0, 2: 1}
hs = {-1: -3, 0: 5, 1: 0, 2: 1}
ns = range(-3, 5)
y = {n: sum(xs.get(k, 0)*hs.get(n-k, 0) for k in xs) for n in ns}
print("\n--- final Q1h convolution ---")
print("  y[n] for n=-3..4:", [y[n] for n in ns])
print("  np.convolve =", np.convolve([-1, 3, 2, 0, 1], [-3, 5, 0, 1]))

# ---------------- final Q1b, Q1d, Q5e ----------------
print("\n--- final small parts ---")
print("  (-1)^n power =", [((-1.0)**n)**2 for n in range(4)], "-> avg power 1, energy infinite")
print("  sin(5pi n) =", np.round(np.sin(5*np.pi*np.arange(4)), 12))
print("  cos(5pi n) =", np.round(np.cos(5*np.pi*np.arange(6)), 6), "(= (-1)^n, period 2)")
print("  autocorr [1,0,1,2] =", np.correlate([1, 0, 1, 2], [1, 0, 1, 2], "full"), "lags", list(range(-3, 4)))

# ---------------- final Q2f: Parseval ----------------
al = 0.6
tt = np.linspace(0, 60, 400001)
print("\n  Q2f energy = 1/(2a) =", 1/(2*al), " time trapz =", np.trapezoid(np.exp(-2*al*tt), tt))
Om = np.linspace(-4000, 4000, 800001)
print("  Q2f parseval =", np.trapezoid(1/(al**2 + Om**2), Om)/(2*np.pi))



# ---------------- DTFT: causal exponential, finite length, 5-point MA ----------------
print("\n--- DTFT ---")
w = np.array([0.0, np.pi/4, np.pi/2, np.pi])
al = 0.5
show("  causal exp a=0.5: X(e^jw)", 1/(1 - al*np.exp(-1j*w)))
show("  |X| vs 1/sqrt(1-2a cos w + a^2)", 1/np.sqrt(1 - 2*al*np.cos(w) + al**2))
M = 5
with np.errstate(divide="ignore", invalid="ignore"):
    Hma = np.sin(w*M/2)/(M*np.sin(w/2))*np.exp(-1j*w*(M-1)/2)
Hma[0] = 1.0 + 0j
show(f"  {M}-pt moving average H", Hma)
show(f"  |H| of {M}-pt MA", np.abs(Hma))
print("  first null at 2pi/M =", round(2*np.pi/M, 6), "=", round(2*np.pi/M/np.pi, 3), "pi")
Mf, alf = 5, 0.5
show("  y[n]=a^n,0..M-1 : Y(e^jw)", (1 - alf**Mf*np.exp(-1j*w*Mf))/(1 - alf*np.exp(-1j*w)), 6)
show("  direct DTFT same", np.array([sum(alf**n*np.exp(-1j*wi*n) for n in range(Mf)) for wi in w]), 6)

# ---------------- final Q5c: h = {-3,6,-5,4}, x = A cos(w0 n) ----------------
print("\n--- final Q5c: h = {-3,6,-5,4} ---")
hh = np.array([-3, 6, -5, 4.0])
for w0, tag in ((np.pi/2, "pi/2"), (np.pi/4, "pi/4"), (np.pi, "pi")):
    Hv = sum(hh[n]*np.exp(-1j*w0*n) for n in range(4))
    print(f"  w0={tag:5s}: H = {Hv.real:+.4f}{Hv.imag:+.4f}j  |H| = {abs(Hv):.4f}"
          f"  angle = {np.degrees(np.angle(Hv)):+.2f} deg")

# ---------------- final Q5a ----------------
print("\n--- final Q5a ---")
print("  h[n] = 2(0.5)^n u[n] =", [2*0.5**n for n in range(5)], " |H(0)| = 2/(1-0.5) =", 2/(1-0.5))

# ---------------- window design worked examples ----------------
print("\n--- FIR window worked numbers ---")
def hd(M, wc):
    k = np.arange(M+1) - M/2
    with np.errstate(divide="ignore", invalid="ignore"):
        v = np.sin(wc*k)/(np.pi*k)
    v[np.isclose(k, 0)] = wc/np.pi
    return v
print("  M=4 wc=pi/2 ideal h_d =", np.round(hd(4, np.pi/2), 6), " sum =", round(hd(4, np.pi/2).sum(), 6))
n5 = np.arange(5)
han4 = 0.5 - 0.5*np.cos(2*np.pi*n5/4)
print("  hann M=4 w =", np.round(han4, 6), " h =", np.round(hd(4, np.pi/2)*han4, 6),
      " H(0) =", round((hd(4, np.pi/2)*han4).sum(), 6))
print("  1/pi =", round(1/np.pi, 6))
print("  M=8 wc=0.3pi ideal =", np.round(hd(8, 0.3*np.pi), 6))
ham8 = 0.54 - 0.46*np.cos(2*np.pi*np.arange(9)/8)
print("  hamming M=8 taps =", np.round(hd(8, 0.3*np.pi)*ham8, 6),
      " H(0) =", round((hd(8, 0.3*np.pi)*ham8).sum(), 6))
print("  N=4096: N^2 =", 4096**2, " (N/2)log2N =", int(4096/2*np.log2(4096)))
