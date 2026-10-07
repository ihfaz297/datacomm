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
    n = np.arange(M+1); k = n - M/2
    with np.errstate(invalid="ignore", divide="ignore"):
        h = np.sin(wc*k)/(np.pi*k)
    h[k == 0] = wc/np.pi
    return h

def respond(h, w=wg):
    return np.exp(-1j*np.outer(w, np.arange(len(h)))) @ h

def metrics(kind, M, wc=0.4*np.pi):
    h = ideal_lpf(M, wc)*win(kind, M)
    H = respond(h); mag = np.abs(H); db = 20*np.log10(mag+1e-300)
    ip = int(np.argmax(mag)); inull = min(i for i in locmin(mag) if i > ip)
    att = -db[inull:].max()
    pm = [i for i in locmax(mag) if i < ip]
    reg = db[:pm[-1]+1] if pm else db[:ip]
    ripple = reg.max()-reg.min()
    i6 = int(np.argmax(mag <= 0.5))
    offset = wg[i6] - wc
    W = respond(win(kind, M)); wm = np.abs(W)
    wml = 2*wg[locmin(wm)[0]]
    lin = np.abs(np.imag(H*np.exp(1j*wg*M/2))).max()
    return dict(hlen=M+1, win_ml=wml/np.pi, null=wg[inull]/np.pi, att=att, ripple=ripple, off6=offset/np.pi, lin=lin)

for kind in ("rect", "hann", "hamming", "blackman"):
    m = metrics(kind, 30)
    print(f"{kind:9s} taps {m['hlen']} | win ML {m['win_ml']:.4f}pi | 1st null {m['null']:.4f}pi | att {m['att']:6.2f} dB"
          f" | pass ripple {m['ripple']:.4f} dB | -6dB offset {m['off6']:.4f}pi | lin {m['lin']:.1e}")
print()
for M in (15, 30, 60, 120):
    r = metrics("hamming", M); q = metrics("rect", M)
    print(f"M={M:3d} taps={M+1:3d} hamming: -6dB offset {r['off6']:.4f}pi att {r['att']:.2f} | rect: offset {q['off6']:.4f}pi att {q['att']:.2f}")
print()
print("ratio of hamming offset 30/60:", metrics("hamming",30)['off6']/metrics("hamming",60)['off6'])
print("sidelobe peaks of each window's own spectrum (dB):")
for kind in ("rect", "hann", "hamming", "blackman"):
    W = np.abs(respond(win(kind, 30))); W = W/W[0]
    lm = locmax(W)
    print(f"  {kind:9s} first sidelobe {20*np.log10(W[lm[0]]):7.2f} dB")
