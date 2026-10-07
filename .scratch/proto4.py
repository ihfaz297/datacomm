import numpy as np
np.set_printoptions(precision=4, suppress=True)
locmin = lambda a: [i for i in range(1, len(a)-1) if a[i] < a[i-1] and a[i] <= a[i+1]]
locmax = lambda a: [i for i in range(1, len(a)-1) if a[i] > a[i-1] and a[i] >= a[i+1]]
wg = np.linspace(0, np.pi, 40001)

def win(kind, M):
    n = np.arange(M+1)
    if kind == "rect":     return np.ones(M+1)
    if kind == "hann":     return 0.5 - 0.5*np.cos(2*np.pi*n/M)
    if kind == "hamming":  return 0.54 - 0.46*np.cos(2*np.pi*n/M)
    if kind == "blackman": return 0.42 - 0.5*np.cos(2*np.pi*n/M) + 0.08*np.cos(4*np.pi*n/M)

def ideal_lpf(M, wc):
    k = np.arange(M+1) - M/2
    with np.errstate(invalid="ignore", divide="ignore"):
        h = np.sin(wc*k)/(np.pi*k)
    h[k == 0] = wc/np.pi
    return h

def respond(h, w=wg):
    return np.exp(-1j*np.outer(w, np.arange(len(h)))) @ h

def metrics(kind, M, wc=0.4*np.pi, w=wg):
    h = ideal_lpf(M, wc)*win(kind, M)
    mag = np.abs(respond(h, w)); db = 20*np.log10(mag+1e-300)
    ih = int(np.argmax(mag <= 0.5))                    # half-power crossing = middle of transition band
    inull = min(i for i in locmin(mag) if i > ih)      # first real null after the transition
    att = -db[inull:].max()
    ripple = db[:ih].max() - db[:ih].min()
    dp = 10**(-ripple/20); ds = 10**(-att/20)
    wp = max(i for i in range(ih+1) if mag[i] >= 1-dp)
    ws = min(i for i in range(ih, len(w)) if mag[i] <= ds)
    trans = w[ws]-w[wp]
    lin = np.abs(np.imag(respond(h, w)*np.exp(1j*w*M/2))).max()
    return dict(taps=M+1, att=att, ripple=ripple, trans=trans, wp=w[wp], ws=w[ws],
                null=w[inull], lin=lin)

print("M=30, wc=0.4pi   (table: att dB | transition /pi = k/M)")
for kind in ("rect", "hann", "hamming", "blackman"):
    m = metrics(kind, 30)
    print(f"{kind:9s} taps {m['taps']:3d} | att {m['att']:6.2f} dB | ripple {m['ripple']:.4f} dB |"
          f" transition {m['trans']/np.pi:.4f}pi  [wp {m['wp']/np.pi:.3f}pi ws {m['ws']/np.pi:.3f}pi] |"
          f" 1st null {m['null']/np.pi:.4f}pi | lin {m['lin']:.1e}")
print("\nscaling of the transition band with the order M (hamming):")
for M in (15, 30, 60, 120):
    m = metrics("hamming", M)
    print(f"  M={M:3d} taps={M+1:3d} transition {m['trans']/np.pi:.4f}pi | M*trans = {M*m['trans']/np.pi:.4f} | att {m['att']:.2f} dB | ripple {m['ripple']:.4f}")
print("scaling for rect:")
for M in (15, 30, 60, 120):
    m = metrics("rect", M)
    print(f"  M={M:3d} transition {m['trans']/np.pi:.4f}pi | M*trans = {M*m['trans']/np.pi:.4f} | att {m['att']:.2f}")

print("\nwindow spectrum, first 4 sidelobe peaks (fine grid, M=30 and M=100):")
for kind in ("rect", "hann", "hamming", "blackman"):
    for M in (30, 100):
        W = np.abs(respond(win(kind, M))) ; W = W/W[0]
        lm = locmax(W)
        print(f"  {kind:9s} M={M:3d}: " + "  ".join(f"{20*np.log10(W[i]):7.2f} dB @ {wg[i]/np.pi:.3f}pi" for i in lm[:3]))
