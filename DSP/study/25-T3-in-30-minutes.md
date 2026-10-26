# Frequency Analysis in 30 Minutes

*Topic 3 · Proakis Ch 4 · only what a 5-mark question needs*

Read each block once, then cover it and say the boxed line out loud. The minutes are a guide.

---

## 1. The four transforms (3 min)

Two questions decide which tool you use: is time continuous or discrete, and is the signal periodic or not?

| | Periodic signal | Aperiodic signal |
|---|---|---|
| **Continuous time** | CTFS: $c_k = \frac{1}{T_0}\int_{T_0} x(t)e^{-j2\pi kF_0t}dt$ | CTFT: $X(F) = \int x(t)e^{-j2\pi Ft}dt$ |
| **Discrete time** | DTFS: $c_k = \frac1N\sum_{n=0}^{N-1} x[n]e^{-j2\pi kn/N}$ | DTFT: $X(\omega) = \sum_n x[n]e^{-j\omega n}$ |

> **The duality:** periodic in time means a discrete (line) spectrum, and discrete time means a periodic spectrum. That is why the DTFT always repeats every $2\pi$.

---

## 2. Square wave, CTFS (5 min)

An even $\pm1$ square wave with period $T_0$: $+1$ for $|t| < T_0/4$, $-1$ for the rest of the period.

Because $x(t)$ is even, only the cosine part survives:

$$
c_k = \frac{2}{T_0}\left[\int_0^{T_0/4}\cos(k\Omega_0t)\,dt - \int_{T_0/4}^{T_0/2}\cos(k\Omega_0t)\,dt\right] = \frac{4\sin(k\pi/2)}{k\Omega_0T_0}.
$$

With $\Omega_0T_0 = 2\pi$:

$$
\boxed{c_k = \frac{2}{k\pi}\sin\frac{k\pi}{2}}
$$

Then say what it means: $c_0 = 0$ (no DC, equal time at $+1$ and $-1$); even harmonics are zero; odd harmonics fall off like $1/k$, with $c_1 = 0.637$, $c_3 = -0.212$, $c_5 = 0.127$.

---

## 3. Rectangular pulse, CTFT (4 min)

$x(t) = A$ for $|t| < \tau/2$, zero otherwise.

$$
X(F) = \int_{-\tau/2}^{\tau/2} A\,e^{-j2\pi Ft}\,dt = \boxed{A\tau\,\frac{\sin(\pi F\tau)}{\pi F\tau} = A\tau\operatorname{sinc}(F\tau)}
$$

Three facts to write: $X(0) = A\tau$, the area of the pulse; zeros at $F = \pm1/\tau, \pm2/\tau, \ldots$; and **a wider pulse gives a narrower spectrum** (the time–bandwidth trade-off).

---

## 4. Discrete-time periodicity and the DTFS (4 min)

> **The test:** $\cos(\omega_0 n)$ is periodic only if $f_0 = \dfrac{\omega_0}{2\pi}$ is a ratio of integers $k/N$. The period is the smallest such $N$.

- $\cos(\pi n/3)$: $f_0 = 1/6$, so $N = 6$.
- $\cos(\sqrt2\,\pi n)$: $f_0 = 1/\sqrt2$ is irrational, so it is **not periodic**.
- $\cos(n/6)$: $f_0 = 1/(12\pi)$ is irrational, so it is **not periodic** either (a favourite trick).

**DTFS of $\cos(\pi n/3)$:** write it with Euler and match terms with $\sum_k c_k e^{j2\pi kn/6}$:

$$
\cos\frac{2\pi n}{6} = \tfrac12 e^{j2\pi n/6} + \tfrac12 e^{-j2\pi n/6} = \tfrac12 e^{j2\pi(1)n/6} + \tfrac12 e^{j2\pi(5)n/6}.
$$

So $\boxed{c_1 = c_5 = \tfrac12}$, and all the other $c_k$ are zero. Only $N$ coefficients exist because $c_{k+N} = c_k$.

---

## 5. DTFT of $a^n u[n]$ (3 min)

A geometric series, convergent because $|a| < 1$:

$$
X(\omega) = \sum_{n=0}^{\infty}\big(ae^{-j\omega}\big)^n = \boxed{\frac{1}{1 - ae^{-j\omega}}},
\qquad
|X(\omega)|^2 = \frac{1}{1 - 2a\cos\omega + a^2}.
$$

$|X(\omega)|^2$ is the **energy density spectrum**. With $a = 0.5$ it is $4$ at $\omega = 0$ and $0.444$ at $\omega = \pi$: the energy sits at low frequencies, a low-pass signal.

**The DTFT exists only if $\sum|x[n]| < \infty$.** $2^n u[n]$ and $u[n]$ have no DTFT. If asked, say: "not absolutely summable; the ROC does not contain the unit circle".

---

## 6. Energy, power and Parseval (4 min)

$$
\boxed{E = \sum_n |x[n]|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi}|X(\omega)|^2\,d\omega}
\qquad\qquad
\boxed{P = \frac1N\sum_{n=0}^{N-1}|x[n]|^2 = \sum_{k=0}^{N-1}|c_k|^2}
$$

The left one is for aperiodic signals, the right one for periodic signals. In words: the energy (or power) is the same whether you add it up over time or over frequency.

Worked examples sir has used:

- **$x(t) = e^{-0.6t}u(t)$:** $E = \int_0^\infty e^{-1.2t}dt = \dfrac{1}{1.2} = 0.8333$ J.
- **$x[n] = (-1)^n$:** every $|x[n]|^2 = 1$, so $E = \infty$ but $P = 1$. It is a **power signal**, and all of it sits at $\omega = \pi$.
- **$u[n]$:** $E = \infty$ and $P = \tfrac12$, because it is on for only half of the window from $-N$ to $N$.

---

## 7. Properties (4 min)

| Property | $x[n]$ | $X(\omega)$ |
|---|---|---|
| Time shift | $x[n-k]$ | $e^{-j\omega k}X(\omega)$: only the phase changes |
| Frequency shift | $e^{j\omega_0n}x[n]$ | $X(\omega - \omega_0)$ |
| Modulation | $x[n]\cos\omega_0n$ | $\tfrac12[X(\omega - \omega_0) + X(\omega + \omega_0)]$ |
| Convolution | $x_1[n] * x_2[n]$ | $X_1(\omega)X_2(\omega)$ |
| Time reversal | $x[-n]$ | $X(-\omega)$ |
| Real $x[n]$ | | $X(-\omega) = X^*(\omega)$: $\lvert X\rvert$ even, phase odd |

**Proof of the time shift** (the one most likely to be asked). Substitute $m = n - k$:

$$
\sum_n x[n-k]\,e^{-j\omega n} = e^{-j\omega k}\sum_m x[m]\,e^{-j\omega m} = e^{-j\omega k}X(\omega).
$$

The frequency shift is the same idea: $\sum_n e^{j\omega_0n}x[n]e^{-j\omega n} = \sum_n x[n]e^{-j(\omega-\omega_0)n} = X(\omega - \omega_0)$.

---

## 8. Two one-liners (2 min)

**DTFT and z-transform.** The DTFT is the z-transform on the unit circle:

$$
X(\omega) = X(z)\big|_{z = e^{j\omega}} \qquad \text{(only if the ROC contains } |z| = 1\text{)}.
$$

**Dirichlet conditions** (when the Fourier series or transform converges): finitely many finite discontinuities; finitely many maxima and minima; and $x(t)$ absolutely integrable, $\int|x(t)|\,dt < \infty$. At a jump, the series converges to the midpoint.

---

## If you blank in the exam

Write the definition of the transform that fits (Section 1), substitute the signal, and simplify with a geometric series ($\sum r^n = \frac{1}{1-r}$ or $\frac{1-r^N}{1-r}$) or Euler's formula. That method alone earns part marks on almost any Topic 3 question.
