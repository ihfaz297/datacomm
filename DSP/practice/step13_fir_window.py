# DSP STEP 13  -  FIR lowpass design by the window method        (TT2 Q2 + Q4, past final paper Q2b, Q3a)
#
# The 4 lines to write in the exam:
#   1) ideal (brick wall) impulse response, CENTRED at M/2 so the FIR comes out causal:
#         h_d[n] = sin(wc (n - M/2)) / (pi (n - M/2)),   n = 0 .. M        (M even -> M+1 taps)
#         h_d[M/2] = wc / pi                                               (the 0/0 point)
#   2) choose a window w[n] of the same length
#   3) h[n] = h_d[n] * w[n]                        (truncate + taper = design done)
#   4) H(e^jw) = DTFT of h, then check |H| against the spec
#
# Textbook table (order M, window length M+1):
#   window        transition dW      min stopband attenuation     in-band ripple
#   rectangular   1.8 pi / M         21 dB                        ~0.74 dB  (Gibbs ringing)
#   Hann          6.2 pi / M         44 dB                        ~0.05 dB
#   Hamming       6.6 pi / M         53 dB                        ~0.02 dB
#   Blackman      11  pi / M         74 dB                        ~0.001 dB
#
# The exam answer in one sentence: the WINDOW SHAPE decides the stopband attenuation and the
# ripple, the ORDER M decides the transition width (transition ~ 1/M, attenuation does not move).
# Sharper transition or deeper stopband  ->  bigger M  ->  longer filter, more delay, more maths.
#
# Run:  python DSP/practice/step13_fir_window.py

import numpy as np
import matplotlib.pyplot as plt


def ideal_lpf(M, wc):
    """Ideal lowpass h_d[n] for n = 0 .. M, centred at M/2 (M must be even)."""
    k = np.arange(M + 1) - M / 2
    # TODO: return sin(wc*k)/(pi*k) and set the k = 0 sample to wc/pi
    return None


def window(kind, M):
    """Window of length M+1: 'rect', 'hann', 'hamming', 'blackman'."""
    n = np.arange(M + 1)
    # TODO: 'rect' 1 ; 'hann' 0.5 - 0.5cos(2pi n/M) ; 'hamming' 0.54 - 0.46cos(2pi n/M) ;
    #       'blackman' 0.42 - 0.5cos(2pi n/M) + 0.08cos(4pi n/M)
    return None


def response(h, w):
    """H(e^jw) on the frequency grid w: the DTFT one-liner of step 10."""
    # TODO: exp(-1j*outer(w, arange(len(h)))) @ h
    return None


# ---------------- checker: don't edit below ----------------
M, wc = 30, 0.4*np.pi                      # order 30 -> 31 taps, cutoff 0.4 pi rad/sample
w = np.linspace(0, np.pi, 4001)
table = {"rect": (21, 4/(M+1)), "hann": (44, 8/M), "hamming": (53, 8/M), "blackman": (74, 12/M)}
# att_theory in dB, window mainlobe width (null to null) in pi: rect 4pi/(M+1), cos-sum windows k*pi/M
locmin = lambda a: [i for i in range(1, len(a)-1) if a[i] < a[i-1] and a[i] <= a[i+1]]


def metrics(kind, M_=None, wc_=None):
    """Measure the four numbers the exam asks about, from |H| on a dense grid."""
    M_, wc_ = (M if M_ is None else M_), (wc if wc_ is None else wc_)
    hd, wf = ideal_lpf(M_, wc_), window(kind, M_)
    if hd is None or wf is None:
        return None
    h = hd * wf
    H = response(h, w)
    if H is None:
        return None
    mag, db = np.abs(H), 20*np.log10(np.abs(H) + 1e-300)
    ih = int(np.argmax(mag <= 0.5))                     # -6 dB point = middle of the transition band
    inull = min(i for i in locmin(mag) if i > ih)       # first true null after the transition
    att = -db[inull:].max()                             # worst stopband ripple
    wp = max(i for i in range(ih+1) if mag[i] >= 0.9)   # passband edge (-0.92 dB)
    ws = min(i for i in range(ih, len(w)) if mag[i] <= 0.1)   # stopband edge (-20 dB)
    W = np.abs(response(window(kind, M_), w))
    band = db[w <= wc_/2]                               # safely inside the passband
    return dict(h=h, taps=h.size, att=att, trans=(w[ws]-w[wp])/np.pi,
                ml=2*w[locmin(W)[0]]/np.pi, ripple=band.max()-band.min(),
                lin=np.abs(np.imag(H*np.exp(1j*w*M_/2))).max())


print("window      taps   stopband attenuation      transition    window mainlobe      in-band ripple   linear phase")
res, ok = {}, True
for kind, (att_th, ml_th) in table.items():
    r = metrics(kind)
    res[kind] = r
    if r is None:
        print(f"{kind:10s}  not implemented")
        ok = False
        continue
    good = abs(r["att"] - att_th) < 3 and abs(r["ml"] - ml_th) < 0.02 and r["lin"] < 1e-9
    ok &= good
    print(f"{kind:10s} {r['taps']:4d}   {r['att']:6.2f} dB  ({att_th:2d} dB)   {r['trans']:.4f}pi"
          f"   {r['ml']:.4f}pi ({ml_th:.4f}pi)   {r['ripple']:.4f} dB    {r['lin']:.1e}  {'ok' if good else 'FAIL'}")

# the order M drives the transition width; the window shape drives the attenuation:
m30, m60 = metrics("hamming"), metrics("hamming", 60)
if m30 is None or m60 is None:
    scale_ok = False
    print("\n1/M law   (hamming not implemented yet)")
else:
    t30, t60, a30, a60 = m30["trans"], m60["trans"], m30["att"], m60["att"]
    scale_ok = abs(t60 - t30/2) / (t30/2) < 0.05 and abs(a60 - a30) < 0.5
    print(f"\n1/M law   hamming M=30: transition {t30:.4f}pi   M=60: {t60:.4f}pi (halved),  "
          f"attenuation {a30:.2f} -> {a60:.2f} dB (did not move)   {'ok' if scale_ok else 'FAIL'}")
ok &= scale_ok

rip = {k: res[k]["ripple"] for k in table if res[k] is not None}
nan = float("nan")
rip_ok = (len(rip) == len(table) and rip["rect"] > 0.5                       # Gibbs ringing, by far the worst
          and max(rip["hann"], rip["hamming"]) < 0.1                          # both cos-sum windows are smooth
          and rip["blackman"] < rip["rect"])
ok &= rip_ok
print(f"in-band ripple: rect {rip.get('rect', nan):.4f} dB (Gibbs)   hann {rip.get('hann', nan):.4f}"
      f"   hamming {rip.get('hamming', nan):.4f}   blackman {rip.get('blackman', nan):.4f} dB (smoothest)"
      f"   {'ok' if rip_ok else 'FAIL'}")

print("PASS  ->  transforms drills done: TT2 topics 1-2 + lab exam 2 topic 4." if ok else
      "FAIL  (h_d = sin(wc(n-M/2))/(pi(n-M/2)) with the M/2 sample = wc/pi; windows are the cos sums)")

if ok:
    fig, ax = plt.subplots(1, 2, figsize=(12.5, 4.4))
    for kind, r in res.items():
        ax[0].plot(w/np.pi, 20*np.log10(np.abs(response(r["h"], w)) + 1e-300),
                   label=f"{kind}: {r['att']:.0f} dB stopband")
    ax[0].axvspan(wc/np.pi, (wc + 0.2)/np.pi, color="gold", alpha=.25)
    ax[0].plot([wc/np.pi, wc/np.pi], [-100, 5], "k:")
    ax[0].set_ylim(-100, 5); ax[0].set_xlabel("w / pi"); ax[0].set_ylabel("|H| dB")
    ax[0].set_title("same cutoff 0.4pi, 31 taps, four windows"); ax[0].legend(fontsize=8); ax[0].grid(alpha=.3)
    ax[1].stem(np.arange(M+1), res["hamming"]["h"], basefmt=" ")
    ax[1].set_title("hamming h[n] = h_d[n] w[n], even symmetry about M/2"); ax[1].set_xlabel("n")
    ax[1].grid(alpha=.3)
    plt.tight_layout(); plt.show()
