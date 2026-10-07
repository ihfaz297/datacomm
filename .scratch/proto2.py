import numpy as np
np.set_printoptions(precision=4, suppress=True)

# ---------- 3. FIR window design ----------
M = 30; wc = 0.4*np.pi; nn = np.arange(M+1)
kk = nn - M/2
with np.errstate(invalid="ignore"):
    hd = np.sin(wc*kk)/(np.pi*kk)
hd[kk == 0] = wc/np.pi
wins = {"rect": np.ones(M+1),
        "hann": 0.5 - 0.5*np.cos(2*np.pi*nn/M),
        "hamming": 0.54 - 0.46*np.cos(2*np.pi*nn/M),
        "blackman": 0.42 - 0.5*np.cos(2*np.pi*nn/M) + 0.08*np.cos(4*np.pi*nn/M)}
wg = np.linspace(0, np.pi, 20001)
tab = {"rect": (21, 1.8, 4), "hann": (44, 6.2, 8), "hamming": (53, 6.6, 8), "blackman": (74, 11.0, 12)}
locmin = lambda a: [i for i in range(1, len(a)-1) if a[i] < a[i-1] and a[i] <= a[i+1]]
locmax = lambda a: [i for i in range(1, len(a)-1) if a[i] > a[i-1] and a[i] >= a[i+1]]
print(f"M = {M} order, taps = {M+1}, wc = {wc/np.pi:.2f}pi")
for kind, wf in wins.items():
    h = hd*wf
    H = np.exp(-1j*np.outer(wg, nn)) @ h; mag, db = np.abs(H), 20*np.log10(np.abs(H)+1e-300)
    W = np.exp(-1j*np.outer(wg, nn)) @ wf; wm = np.abs(W)
    wn = locmin(wm); win_ml = wg[wn[0]]*2                      # window mainlobe, null to null
    ip = int(np.argmax(mag)); inull = min(i for i in locmin(mag) if i > ip)
    att = -db[inull:].max()                                    # worst stopband ripple
    pm = [i for i in locmax(mag) if i < ip]; sm = [i for i in locmax(mag) if i > inull]
    trans = wg[sm[0]] - wg[pm[-1]]
    pr = db[:inull].max() - db[inull-1]
    lin = np.abs(np.imag(H*np.exp(1j*wg*M/2))).max()
    print(f"{kind:9s} win ML {win_ml/np.pi:.4f}pi (th {tab[kind][2]/(M+1):.4f}) | 1st null {wg[inull]/np.pi:.4f}pi"
          f" | stop att {att:6.2f} dB (th {tab[kind][0]}) | trans {trans/np.pi:.4f}pi (th {tab[kind][1]/M:.4f})"
          f" | pass ripple {pr:.4f} dB | lin-phase err {lin:.2e}")

# ---------- 4. moving average ----------
Mw = 5; w = np.linspace(0, np.pi, 1001)
H = np.sin(w*Mw/2)/(Mw*np.sin(w/2))*np.exp(-1j*w*(Mw-1)/2)
H = np.where(w == 0, 1.0, H)
Hn = np.exp(-1j*np.outer(w, np.arange(Mw))) @ (np.ones(Mw)/Mw)
print("\nMA err vs definition:", np.abs(H-Hn).max(), "|H(0)| =", abs(H[0]))
print("MA first null:", w[1:][np.argmin(abs(H[1:]))], " 2pi/M =", 2*np.pi/Mw)
lin = np.abs(np.imag(H*np.exp(1j*w*(Mw-1)/2))).max()
print("MA linear-phase err:", lin)

# ---------- 5. z-transform checks ----------
A, B = 0.5, 2.0
z0 = 1.2
s = sum(A**k * z0**-k for k in range(0, 400)) + sum(B**k * z0**-k for k in range(-400, 0))
print("\ntwo-sided numeric:", s, " closed form:", 1/(1-A/z0) - 1/(1-B/z0))
Mf = 8; Af = 0.5
num_poly = [1] + [0]*(Mf-1) + [-Af**Mf]
den_poly = [1, -Af] + [0]*(Mf-1)
zr = np.roots(num_poly); zp = np.roots(den_poly)
print("finite-length zero angles/pi:", np.sort(np.angle(zr))/np.pi)
print("theory  a*exp(j2pi k/M) k=1..M-1:", np.sort(np.angle(Af*np.exp(1j*2*np.pi*np.arange(1, Mf)/Mf)))/np.pi)
print("zero mags:", np.abs(zr).round(6), "poles:", zp.round(6))
