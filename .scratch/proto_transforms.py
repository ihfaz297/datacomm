import numpy as np
np.set_printoptions(precision=4, suppress=True)

# ---------- 1. DFT / circular convolution / linear convolution ----------
def dft(x):
    x = np.asarray(x, float); N = len(x)
    return np.array([sum(x[n]*np.exp(-2j*np.pi*k*n/N) for n in range(N)) for k in range(N)])

def circ(x, h, N):
    x = np.asarray(x, float); h = np.asarray(h, float)
    xp = np.zeros(N); hp = np.zeros(N)
    xp[:len(x)] = x; hp[:len(h)] = h
    return np.array([sum(xp[k]*hp[(nn-k) % N] for k in range(N)) for nn in range(N)])

print("== DFT of {1,1,2,1} ==", dft([1,1,2,1]).round(4))
print("== DFT of {1,2,1} ==", dft([1,2,1]).round(4))
print("== TT2 Q3: 4-pt circ of {1,2,2,1}*{1,2,3} ==", circ([1,2,2,1], [1,2,3], 4).round(6))
print("   via fft:", np.fft.ifft(np.fft.fft([1,2,2,1],4)*np.fft.fft([1,2,3,0],4)).real.round(6))
print("   N=6 (should equal linear):", circ([1,2,2,1], [1,2,3], 6).round(6))
print("   linear np.convolve:", np.convolve([1,2,2,1], [1,2,3]))
print("== final Q3c: 4-pt circ {1,1,2,1}*{1,2,1,1} ==", circ([1,1,2,1], [1,2,1,1], 4).round(6))
print("   linear:", np.convolve([1,1,2,1], [1,2,1,1]))
print("== final Q5e autocorr of {1,0,1,2} ==", np.correlate([1,0,1,2], [1,0,1,2], "full"))

# ---------- 2. causal exponential DTFT ----------
a = 0.5; w = np.linspace(0, np.pi, 1001); n1 = np.arange(0, 40)
num = np.exp(-1j*np.outer(w, n1)) @ (a**n1)
clo = 1/(1 - a*np.exp(-1j*w))
print("DTFT err:", np.abs(num-clo).max())

# ---------- 3. FIR window design ----------
M = 30; wc = 0.4*np.pi; nn = np.arange(M+1)
kk = nn - M/2
hd = np.sin(wc*kk)/(np.pi*kk); hd[kk == 0] = wc/np.pi
wins = {"rect": np.ones(M+1),
        "hann": 0.5 - 0.5*np.cos(2*np.pi*nn/M),
        "hamming": 0.54 - 0.46*np.cos(2*np.pi*nn/M),
        "blackman": 0.42 - 0.5*np.cos(2*np.pi*nn/M) + 0.08*np.cos(4*np.pi*nn/M)}
wg = np.linspace(0, np.pi, 20001)
tab = {"rect": (21, 1.8), "hann": (44, 6.2), "hamming": (53, 6.6), "blackman": (74, 11.0)}
print(f"\nM = {M} taps = {M+1}, wc = {wc/np.pi:.2f}pi   (table: att dB, dw/pi = k/M)")
for kind, wf in wins.items():
    h = hd*wf
    H = np.exp(-1j*np.outer(wg, nn)) @ h; mag = np.abs(H)
    db = 20*np.log10(np.maximum(mag, 1e-300))
    # local minima near the cutoff -> mainlobe nulls
    lo, hi = np.argmin(np.abs(wg-(wc-0.35*np.pi))), np.argmin(np.abs(wg-(wc+0.35*np.pi)))
    seg = mag[lo:hi]
    mins = [lo+i for i in range(1, len(seg)-1) if seg[i] < seg[i-1] and seg[i] <= seg[i+1]]
    pk = np.argmax(mag[lo:hi]) + lo
    left = [m for m in mins if m < pk]; right = [m for m in mins if m > pk]
    ml = wg[right[0]] - wg[left[-1]] if left and right else float("nan")
    att = -db[wg >= wc + 0.5*ml].max()
    pb_max = db[wg <= wc - 0.5*ml].max(); pb_min = db[wg <= wc - 0.5*ml].min()
    print(f"{kind:9s} mainlobe {ml/np.pi:.4f}pi (theory {[4,8,8,12][list(wins).index(kind)]/(M+1):.4f}pi)  "
          f"att {att:6.2f} dB (table {tab[kind][0]})  passband ripple {pb_max-pb_min:.4f} dB  delay {np.angle(H[np.argmin(abs(wg-0.3*np.pi))])/-0.3: .4f}")

# ---------- 4. moving average ----------
Mw = 5; H = np.sin(w*Mw/2)/(Mw*np.sin(w/2))*np.exp(-1j*w*(Mw-1)/2)
H[0] = 1.0
print("\nMA |H(0)| =", abs(H[0]), " first null =", w[1:][np.argmin(abs(H[1:]))], "2pi/M =", 2*np.pi/M)
print("MA delay from phase at w=0.1,0.3:", -(np.angle(H[np.argmin(abs(w-0.3))])-np.angle(H[np.argmin(abs(w-0.1))]))/0.2)

# ---------- 5. z-transform checks ----------
A, B = 0.5, 2.0
z0 = 1.2
s = sum(A**k * z0**-k for k in range(0, 400)) + sum(B**k * z0**-k for k in range(-400, 0))
print("\ntwo-sided numeric:", s, " closed form:", 1/(1-A/z0) - 1/(1-B/z0))
Mf = 8; Af = 0.5
num_poly = [1] + [0]*(Mf-1) + [-Af**Mf]
den_poly = [1, -Af] + [0]*(Mf-1)
zr = np.roots(num_poly); zp = np.roots(den_poly)
print("finite-length zeros (deg):", np.sort(np.angle(zr))/np.pi, "mags:", np.abs(zr).round(6))
print("expected zeros at a*exp(j2pi k/M), k=1..M-1:", np.sort(np.angle(Af*np.exp(1j*2*np.pi*np.arange(1, Mf)/Mf)))/np.pi)
print("poles:", zp.round(6))
