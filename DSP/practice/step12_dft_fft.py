# DSP STEP 12  -  DFT, IDFT, circular convolution, FFT cost      (TT2 Q1 + Q3, past final paper Q3c, Q4h, Q6c)
#
#   X[k] = sum_n x[n] exp(-j 2 pi k n / N)              k = 0 .. N-1            (DFT)
#   x[n] = (1/N) sum_k X[k] exp(+j 2 pi k n / N)                               (IDFT: 1/N and the + sign!)
#   The DFT is the z-transform sampled on the unit circle:  X[k] = X(z) at z = exp(j 2 pi k / N)
#
#   Circular convolution:  y[n] = sum_k x[k] * h[(n-k) mod N]        (cyclic shift = wrap-around)
#        the N-point DFT turns it into a product:  y = IDFT( DFT(x) * DFT(h) )
#        circular convolution == LINEAR convolution only when N >= len(x) + len(h) - 1
#        (that single condition is past final paper Q4h and the whole point of TT2 Q3)
#
#   Cost (TT2 Q1): direct DFT = N^2 complex multiplications, N(N-1) complex additions        -> O(N^2)
#                  radix-2 FFT (DIT/DIF) = (N/2) log2(N) complex multiplications             -> O(N log2 N)
#                  speed-up = N^2 / ((N/2) log2 N) = 2N / log2(N)
#
#   Matrix view of the DFT: X = W @ x with W[k, n] = exp(-j 2 pi k n / N)  (this is the naive version below)
#
# Run:  python DSP/practice/step12_dft_fft.py

import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([1, 1, 2, 1.0])     # past final paper Q6c / Q3c
x2 = np.array([1, 2, 2, 1.0])     # TT2 Q3
h1 = np.array([1, 2, 1.0])        # past final paper Q6c
h2 = np.array([1, 2, 1, 1.0])     # past final paper Q3c
h3 = np.array([1, 2, 3.0])        # TT2 Q3


def dft_naive(x):
    """N-point DFT straight from the definition."""
    x = np.asarray(x, dtype=float)
    N = len(x)
    # TODO: for each k: X[k] = sum_n x[n] * exp(-2j*pi*k*n/N)
    return None


def idft_naive(X):
    """N-point IDFT straight from the definition (remember the 1/N and the + sign)."""
    X = np.asarray(X, dtype=complex)
    N = len(X)
    # TODO: for each n: x[n] = (1/N) * sum_k X[k] * exp(+2j*pi*k*n/N)
    return None


def circ_conv(x, h, N):
    """N-point circular convolution; both sequences are zero-padded to length N (N >= max(len(x), len(h)))."""
    x = np.asarray(x, dtype=float)
    h = np.asarray(h, dtype=float)
    xp = np.zeros(N); xp[:len(x)] = x
    hp = np.zeros(N); hp[:len(h)] = h
    # TODO: y[n] = sum_k xp[k] * hp[(n - k) % N]
    return None


def fft_mults(N):
    """Complex multiplications of a radix-2 FFT of length N = 2^m."""
    # TODO: (N/2) * log2(N)
    return None


# ---------------- checker: don't edit below ----------------
L   = lambda a: None if a is None else np.round(np.asarray(a).real, 6).tolist()   # for printing
ERR = lambda a, b: None if a is None else float(np.abs(np.asarray(a) - np.asarray(b)).max())

X1, Xh = dft_naive(x1), dft_naive(h1)
x_rt = None if X1 is None else idft_naive(X1)
dft_err = ERR(X1, np.fft.fft(x1))
tt2_err = ERR(Xh, [4, np.exp(-2j*np.pi/3), np.exp(2j*np.pi/3)])     # exact DFT of {1,2,1}
rt_err  = ERR(x_rt, x1)

y_tt2  = circ_conv(x2, h3, 4)
y_tt2f = np.fft.ifft(np.fft.fft(x2, 4) * np.fft.fft(h3, 4)).real
y_tt2_6 = circ_conv(x2, h3, 6)                 # N = 4+3-1 = 6 -> must equal the linear convolution
y_lin   = np.convolve(x2, h3)
y_past  = circ_conv(x1, h2, 4)

checks = [
    ("DFT of {1,1,2,1}",               L(X1),       [5, -1, 1, -1],       0),
    ("DFT vs np.fft (max error)",      dft_err,     0.0,                  1e-9),
    ("DFT of {1,2,1} (exact values)",  tt2_err,     0.0,                  1e-9),
    ("IDFT(DFT(x)) = x (max error)",   rt_err,      0.0,                  1e-9),
    ("TT2 Q3 {1,2,2,1} (*4) {1,2,3}",  L(y_tt2),    [9, 7, 9, 11],        0),
    ("   the same via a DFT product",  L(y_tt2f),   [9, 7, 9, 11],        1e-9),
    ("N=6 circular == linear",         L(y_tt2_6),  L(y_lin),             0),
    ("Q3c {1,1,2,1} (*4) {1,2,1,1}",   L(y_past),   [6, 6, 6, 7],         0),
]
ok = True
for name, got, want, tol in checks:
    good = got is not None and np.abs(np.asarray(got) - np.asarray(want)).max() <= tol
    ok &= good
    print(f"{name:33s} {got}   {'ok' if good else f'expected {want}'}")

print("\n   N          direct DFT N^2      radix-2 FFT (N/2)log2 N      speed-up")
cost_ok = True
for N in (8, 64, 1024, 4096):
    f = fft_mults(N)
    good = f is not None and f < N ** 2
    cost_ok &= good
    print(f"{N:6d} {N**2:22d} {str(None if f is None else int(f)):>22} "
          f"{('--' if not good else f'{N**2/f:.1f} x'):>17}   {'ok' if good else 'expected (N/2)log2 N'}")
ok &= cost_ok
print("PASS  ->  open step13_fir_window.py" if ok else
      "FAIL  (X[k] = sum x[n] e^(-j 2pi k n/N);  IDFT carries 1/N and +j;  circular conv wraps with % N)")

if ok:
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.6))
    ax[0].stem(np.arange(len(x2)), x2, basefmt=" "); ax[0].set_title("x[n] = {1,2,2,1}")
    ax[1].stem(np.arange(4), y_tt2, basefmt=" ")
    ax[1].set_title("4-point circular: {9,7,9,11}")
    ax[2].stem(np.arange(len(y_lin)), y_lin, basefmt=" ")
    ax[2].axvspan(3.5, 5.5, color="C3", alpha=.15)
    ax[2].set_title("N=6: linear {1,4,9,11,8,3}   (pink = what wraps at N=4)")
    for t in ax:
        t.set_xlabel("n"); t.grid(alpha=.3)
    plt.tight_layout(); plt.show()
