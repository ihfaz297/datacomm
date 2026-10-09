import numpy as np
np.set_printoptions(precision=5, suppress=True)
j = 1j
def H(h, w, n0=0):
    n = np.arange(len(h)) + n0
    return np.sum(np.array(h) * np.exp(-j * w * n))

print("--- 4.68: h=0.4^n u[n], w=pi/4")
Hw = 1 / (1 - 0.4 * np.exp(-j * np.pi / 4))
print(Hw, abs(Hw), np.angle(Hw), np.degrees(np.angle(Hw)))

print("--- h={4,-5,6,-3} step response, H(0)")
h = [4, -5, 6, -3]
print(np.cumsum(h), H(h, 0))

print("--- h={-3,6,-5,4} at w=pi/2 and pi/4")
h2 = [-3, 6, -5, 4]
for w in [np.pi / 2, np.pi / 4, 0, np.pi]:
    v = H(h2, w); print(w, v, abs(v), np.degrees(np.angle(v)))

print("--- HPF design 0.1 stop, 0.4 pass")
a0 = 1 / (2 * (np.cos(0.4) - np.cos(0.1))); a1 = -2 * a0 * np.cos(0.1)
print(a0, a1, abs(H([a0, a1, a0], 0.1)), abs(H([a0, a1, a0], 0.4)))

print("--- 5-pt MA")
for w in [0, np.pi / 5, 2 * np.pi / 5, np.pi / 2, 4 * np.pi / 5, np.pi]:
    v = H([0.2] * 5, w); print(round(w / np.pi, 3), "pi", round(abs(v), 5), round(np.degrees(np.angle(v)), 2))

print("--- 2^n * 0.5^n conv")
n = np.arange(8)
y = np.convolve(2.0 ** n, 0.5 ** n)[:8]
print(y, 4 / 3 * 2.0 ** n - 1 / 3 * 0.5 ** n)

print("--- double pole partial fraction: 1/((1+2z^-1)(1-z^-1)^2)")
from numpy.polynomial import polynomial as P
den = P.polymul([1, 2], P.polymul([1, -1], [1, -1]))  # in z^-1
x = np.zeros(8); d = np.zeros(8); d[0] = 1
for k in range(8):
    x[k] = d[k] - sum(den[i] * x[k - i] for i in range(1, len(den)) if k - i >= 0)
print(x, 4 / 9 * (-2.0) ** n + 5 / 9 + n / 3)

print("--- y=0.5y(n-1)+2x(n) impulse")
hh = np.zeros(6);
for k in range(6): hh[k] = 0.5 * (hh[k - 1] if k else 0) + (2 if k == 0 else 0)
print(hh, 2 * 0.5 ** np.arange(6))

print("--- two-sided a=0.5,b=2 at z=1.2")
a, b, z = 0.5, 2, 1.2
cf = 1 / (1 - a / z) - 1 / (1 - b / z)
s = sum((a / z) ** k for k in range(400)) + sum((z / b) ** l for l in range(1, 400))
print(cf, s, (a - b) / z / ((1 - a / z) * (1 - b / z)))

print("--- 16z^3+6z+5 roots, 2z^2-2z+1 roots")
print(np.roots([16, 0, 6, 5]), np.roots([2, -2, 1]), abs(np.roots([16, 0, 6, 5])))

print("--- DTFS {1,1,0,0}")
print(np.fft.fft([1, 1, 0, 0]) / 4)
print("--- DTFS cos(pi n/3), N=6")
print(np.round(np.fft.fft(np.cos(np.pi * np.arange(6) / 3)) / 6, 5))
print("--- DTFS square N=10, N1=2 (n=-2..2)")
xs = np.array([1, 1, 1, 0, 0, 0, 0, 0, 1, 1.0])
ck = np.fft.fft(xs) / 10
form = [0.5] + [np.sin(2 * np.pi * k * 2.5 / 10) / (10 * np.sin(np.pi * k / 10)) for k in range(1, 10)]
print(np.round(ck.real, 5), np.round(form, 5), "power", np.mean(xs ** 2), np.sum(abs(ck) ** 2))

print("--- CTFS square +-1: c1, c3")
print(2 / np.pi, -2 / (3 * np.pi))

print("--- Parseval e^-0.6t")
t = np.linspace(0, 80, 2_000_001); print(np.trapezoid(np.exp(-1.2 * t), t), 1 / 1.2)

print("--- energy density a^n u[n] a=0.5 at w=0, pi")
for w in [0, np.pi]: print(1 / (1 - 2 * 0.5 * np.cos(w) + 0.25))

print("--- 4.57 DC: alpha=0.5 M=4")
print(sum(0.5 ** k for k in range(4)), (1 - 0.5 ** 4) / (1 - 0.5))

print("--- 4.76 allpass check random d")
d1, d2, d3 = 0.3, -0.2, 0.1
for w in [0.3, 1.1, 2.5]:
    e = np.exp(-j * w)
    print(abs((d3 + d2 * e + d1 * e ** 2 + e ** 3) / (1 + d1 * e + d2 * e ** 2 + d3 * e ** 3)))

print("--- 4.64 alpha=-beta: |(a+e^-jw)/(1-b e^-jw)|, b=0.6, a=-0.6")
for w in [0.2, 1.5, 3.0]:
    e = np.exp(-j * w); print(abs((-0.6 + e) / (1 - 0.6 * e)))

print("--- steady state, h=0.4^n, x = sin(pi n/4)u[n], y[50] vs ss")
N = 60; nn = np.arange(N)
yy = np.convolve(np.sin(np.pi * nn / 4), 0.4 ** nn)[:N]
print(yy[50], abs(Hw) * np.sin(np.pi * 50 / 4 + np.angle(Hw)))
print("y[0..3]", yy[:4], "ss[0..3]", abs(Hw) * np.sin(np.pi * nn[:4] / 4 + np.angle(Hw)))

print("--- (-1)^n power")
print(np.mean(((-1.0) ** np.arange(1000)) ** 2))
