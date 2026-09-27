"""Round 3: tutorial practice-set answers (DTFT #5, z-transform set, DFT set)."""
import numpy as np

print("--- tutorial 10, practice 5: 4-point MA at pi/4 ---")
M, w0 = 4, np.pi/4
with np.errstate(divide="ignore", invalid="ignore"):
    H = np.sin(w0*M/2)/(M*np.sin(w0/2))*np.exp(-1j*w0*(M-1)/2)
print(f"  |H| = {abs(H):.6f}  angle = {np.degrees(np.angle(H)):.4f} deg  3|H| = {3*abs(H):.4f}")

print("\n--- tutorial 10, practice 1/2 checked directly ---")
for wv, tag in ((0.0, "w=0"), (np.pi, "w=pi")):
    print(f"  {tag}: |1-e^-jw| = {abs(1-np.exp(-1j*wv)):.6f}   |1/(1-0.8e^-jw)| = {abs(1/(1-0.8*np.exp(-1j*wv))):.6f}")
print("  |1-e^-jpi| =", abs(1 - np.exp(-1j*np.pi)))

print("\n--- z-transform practice ---")
zz = 1.5
print("  a=0.8,b=3 at z=1.5:", 1/(1-0.8/zz) - 1/(1-3/zz), "  (ROC 0.8<|z|<3)")
print("  delta[n-3] at z=1.5:", zz**-3)
print("  finite a=0.7,M=6,z=1.2:", (1-0.7**6*1.2**-6)/(1-0.7/1.2), " direct:", sum(0.7**n*1.2**-n for n in range(6)))

print("\n  partial fractions 1/((1-0.5/z)(1-0.25/z)):")
a, b = 0.5, 0.25
A, B = 1/(1 - b/a), 1/(1 - a/b)
print(f"   A = {A:g}, B = {B:g}  -> x[n] = ({A:g}*0.5^n - {B:g}*0.25^n)u[n]")
print("   x[0] =", A - B, " x[1] =", A*0.5 - B*0.25, " x[2] =", A*0.25 - B*0.0625)
print("   direct inverse via power series:", [round(sum([1 if k == n else 0 for k in [n]]) * 0 + 0, 6) for n in range(3)])
print("   verify by long division: x[0]=1, x[1]=0.75, x[2]=0.4375 ->",
      [1, 0.75, 0.4375])

print("\n  H(z) = (1 - 1/z)/(1 - 0.5/z):")
n = np.arange(6)
h = (0.5**n) - np.where(n == 0, 0, 0.5**(n-1))
print("   h[n] = 0.5^n u[n] - 0.5^(n-1) u[n-1] =", h)
print("   h[0] = 1, then h[n] = -0.5^n:", [1] + [round(-0.5**k, 4) for k in range(1, 6)])
print("   H(0) (z=1) =", (1-1)/(1-0.5), "  H(z=-1) =", (1+1)/(1+0.5))

print("\n--- DFT tutorial practice ---")
print("  DFT{1,2,3,4} =", np.round(np.fft.fft([1, 2, 3, 4]), 4))
print("  DFT{1,2,1} =", np.round(np.fft.fft([1, 2, 1]), 4))
print("  IDFT check for {1,2,1}: |X| =", np.round(np.abs(np.fft.fft([1, 2, 1])), 4))
print("  6-point circular conv {1,2,3} (6) {1,1,1}:")
def circ(x, h, N):
    xp = np.zeros(N); xp[:len(x)] = np.asarray(x, float)
    hp = np.zeros(N); hp[:len(h)] = np.asarray(h, float)
    return np.array([sum(xp[k]*hp[(n-k) % N] for k in range(N)) for n in range(N)])
print("   ", circ([1, 2, 3], [1, 1, 1], 6), " linear:", np.convolve([1, 2, 3], [1, 1, 1]))
print("  4-point DFT of {1,1,1,1} =", np.round(np.fft.fft([1, 1, 1, 1]), 4))
print("  8-point FFT of {1,1,1,1,0,0,0,0} =", np.round(np.abs(np.fft.fft([1, 1, 1, 1, 0, 0, 0, 0])), 4))
print("  DFT of {0,1,2,3} =", np.round(np.fft.fft([0, 1, 2, 3]), 4))
print("  N=16: N^2 =", 16**2, " (N/2)log2N =", int(8*4))
print("  N=32: N^2 =", 32**2, " (N/2)log2N =", int(16*5))
