"""Round 2: numbers used in the tutorial files and their practice sets."""
import numpy as np

def df(x, N=None):
    x = np.asarray(x, dtype=complex)
    N = len(x) if N is None else N
    xp = np.zeros(N, dtype=complex); xp[:len(x)] = x
    return np.array([sum(xp[n]*np.exp(-2j*np.pi*k*n/N) for n in range(N)) for k in range(N)])

def circ(x, h, N):
    xp = np.zeros(N); xp[:len(x)] = np.asarray(x, float)
    hp = np.zeros(N); hp[:len(h)] = np.asarray(h, float)
    return np.array([sum(xp[k]*hp[(n-k) % N] for k in range(N)) for n in range(N)])

print("--- DTFT of {1,2,3} ---")
w = np.array([0.0, np.pi/2, np.pi])
X = np.array([sum(v*np.exp(-1j*wi*n) for n, v in enumerate([1, 2, 3])) for wi in w])
print("  X =", np.round(X, 6), " |X| =", np.round(np.abs(X), 6), " phase deg =", np.round(np.degrees(np.angle(X)), 2))

print("\n--- 5-point MA ---")
for wi, tag in ((np.pi/5, "pi/5"), (2*np.pi/5, "2pi/5"), (np.pi/2, "pi/2"), (np.pi, "pi")):
    with np.errstate(divide="ignore", invalid="ignore"):
        v = np.sin(5*wi/2)/(5*np.sin(wi/2))*np.exp(-1j*wi*2)
    print(f"  w={tag:6s} H = {v.real:+.6f}{v.imag:+.6f}j  |H| = {abs(v):.6f}  phase = {np.degrees(np.angle(v)):+.2f} deg")

print("\n--- recursive y(n)=0.5y(n-1)+2x(n) steady state at w0=pi/2 ---")
H = 2/(1 - 0.5*np.exp(-1j*np.pi/2))
print(f"  H = {H.real:.6f}{H.imag:+.6f}j  |H| = {abs(H):.6f}  angle = {np.degrees(np.angle(H)):.3f} deg")
print("  h[n] =", [2*0.5**n for n in range(6)], " sum =", sum(2*0.5**n for n in range(60)), "= H(0)")

print("\n--- z-transform practice numbers ---")
a, b, zz = 0.8, 3.0, 1.5
print("  two-sided a=0.8,b=3 at z=1.5:", 1/(1-a/zz) - 1/(1-b/zz), " (ROC 0.8<|z|<3, 1.5 inside)")
Md, ad, zf = 6, 0.7, 1.2
print(f"  finite a=0.7, M=6 at z=1.2:", (1-ad**Md*zf**-Md)/(1-ad/zf), " direct =", sum(ad**n*zf**-n for n in range(Md)))
print("  closed form 1/(1-a/z) at z=1.2:", 1/(1-ad/zf))
print("  zeros of 0.7^n, n=0..5 (M=6):", np.round([ad*np.exp(2j*np.pi*k/6) for k in range(1, 6)], 4))

print("\n--- practice: 4-pt circ conv {2,1,1} and {1,2} ---")
print("  circ =", circ([2, 1, 1], [1, 2], 4), " linear =", np.convolve([2, 1, 1], [1, 2]))
print("  via DFT product =", np.rint(np.fft.ifft(df([2, 1, 1], 4)*df([1, 2], 4)).real))

print("\n--- practice: 8-point circular conv of {1,1,1,1} and {1,2,3,4} ---")
print("  circ N=8 =", circ([1, 1, 1, 1], [1, 2, 3, 4], 8), " linear =", np.convolve([1, 1, 1, 1], [1, 2, 3, 4]))
print("  circ N=4 =", circ([1, 1, 1, 1], [1, 2, 3, 4], 4))

print("\n--- practice: DFT of {1,0,1,0} and {1,2,3,4} ---")
print("  DFT{1,0,1,0} =", np.round(df([1, 0, 1, 0]), 6))
print("  DFT{1,2,3,4} =", np.round(df([1, 2, 3, 4]), 6))

print("\n--- practice: window design M=8, wc=0.3pi, hamming (already in round 1) ---")
print("  hamming attenuation theory 53 dB; taps 9")
print("  transition ~ 6.6pi/8 =", round(6.6/8, 4), "pi")

print("\n--- practice: cascade 8-point MA + 5-point MA nulls ---")
print("  MA8 first null 2pi/8 =", round(2/8, 3), "pi   MA5 first null 2pi/5 =", round(2/5, 3), "pi")
print("  h[n] = 1/8 sum: at w=0 ->", 1.0)
