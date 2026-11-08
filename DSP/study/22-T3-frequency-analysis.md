# Topic 3 · Frequency Analysis of Signals

*Proakis Chapter 4 · the other **Term Test 2** question (5 marks)*

This follows your class note (`Note/Mid-2 note.pdf`, pages 34–53: Proakis 4.1–4.4, Examples 4.1.2 and 4.2.1) and the 2021–22 final (Q1b, 1c, 2c, 2e, 2f). Your note says the last few slides were missing, so Section 8 fills that gap from Proakis §4.4. Every number was checked in Python.

---

## 0. The whole topic in one table

*Draw this first in any "explain" answer.*

There are four Fourier tools, one for each combination of continuous or discrete time with a periodic or aperiodic signal.

| | **Periodic signal** (discrete spectrum) | **Aperiodic signal** (continuous spectrum) |
|---|---|---|
| **Continuous time** (aperiodic spectrum) | **CTFS**: $c_k = \frac{1}{T_p}\int_{T_p} x(t)\,e^{-j2\pi kF_0t}\,dt$ | **CTFT**: $X(F) = \int_{-\infty}^{\infty} x(t)\,e^{-j2\pi Ft}\,dt$ |
| **Discrete time** (periodic spectrum) | **DTFS**: $c_k = \frac{1}{N}\sum_{n=0}^{N-1} x[n]\,e^{-j2\pi kn/N}$ | **DTFT**: $X(\omega) = \sum_{n=-\infty}^{\infty} x[n]\,e^{-j\omega n}$ |

The matching synthesis (inverse) formulas are

$$
\begin{aligned}
\text{CTFS:}\quad & x(t) = \sum_{k=-\infty}^{\infty} c_k\,e^{j2\pi kF_0t} \\
\text{CTFT:}\quad & x(t) = \int_{-\infty}^{\infty} X(F)\,e^{j2\pi Ft}\,dF \\
\text{DTFS:}\quad & x[n] = \sum_{k=0}^{N-1} c_k\,e^{j2\pi kn/N} \\
\text{DTFT:}\quad & x[n] = \frac{1}{2\pi}\int_{2\pi} X(\omega)\,e^{j\omega n}\,d\omega
\end{aligned}
$$

The pattern to remember is a duality: **periodic in one domain means discrete in the other, and discrete in one domain means periodic in the other.**

**Vocabulary** (note p.34):

- **Frequency analysis:** breaking a signal down into its frequency components.
- **Harmonics:** the frequencies $kF_0$, the integer multiples of the fundamental $F_0$.
- **Bandwidth:** the range of frequencies where the signal's energy or power is concentrated.
- **Resonance:** a system's tendency to respond with a much larger amplitude at certain frequencies.

Examples: a sinusoidal carrier is periodic, an ECG is aperiodic, speech is aperiodic, and machine vibration is periodic.

---

## 1. The continuous-time Fourier series

Any periodic signal $x(t)$ with period $T_0$, so fundamental $\Omega_0 = 2\pi/T_0$, can be written as a weighted sum of complex exponentials at the harmonic frequencies $k\Omega_0$:

$$
x(t) = \sum_{k=-\infty}^{\infty} c_k\,e^{jk\Omega_0 t},
\qquad
c_k = \frac{1}{T_0}\int_{T_0} x(t)\,e^{-jk\Omega_0 t}\,dt.
$$

The coefficient $c_k$ tells you how much of harmonic $k$ the signal contains.

### 1a. Spectra you can read off by inspection (note p.35)

If the signal is already a sum of sinusoids, Euler's formula gives the coefficients without any integration:

$$
\cos\Omega_0 t = \tfrac12 e^{j\Omega_0 t} + \tfrac12 e^{-j\Omega_0 t}
\quad\Longrightarrow\quad
c_1 = c_{-1} = \tfrac12, \ \text{all others } 0.
$$

In particular $c_0 = 0$: a pure cosine has no DC part. With an amplitude and a phase,

$$
A\cos(\Omega_0 t + \phi)
\quad\Longrightarrow\quad
c_1 = \tfrac{A}{2}e^{j\phi}, \qquad c_{-1} = \tfrac{A}{2}e^{-j\phi} = c_1^*.
$$

That relation $c_{-k} = c_k^*$ is the conjugate symmetry every real signal has. The magnitude plot is two lines of height $A/2$ at $\pm\Omega_0$; the phase plot is $+\phi$ at $+\Omega_0$ and $-\phi$ at $-\Omega_0$.

### 1b. The $\pm 1$ square wave: full derivation

*An even square wave with period $T_0$: $x(t) = +1$ for $|t| < T_0/4$ and $-1$ for $T_0/4 < |t| < T_0/2$.*

Integrate over one period centred on zero. Because $x(t)$ is even and sine is odd, the sine part of $e^{-jk\Omega_0 t}$ integrates to zero and the cosine part doubles over the half-period:

$$
\begin{aligned}
c_k &= \frac{1}{T_0}\int_{-T_0/2}^{T_0/2} x(t)\,e^{-jk\Omega_0 t}\,dt
     = \frac{2}{T_0}\int_0^{T_0/2} x(t)\cos(k\Omega_0 t)\,dt \\[6pt]
    &= \frac{2}{T_0}\left[\int_0^{T_0/4}\cos(k\Omega_0 t)\,dt - \int_{T_0/4}^{T_0/2}\cos(k\Omega_0 t)\,dt\right] \\[6pt]
    &= \frac{2}{T_0}\cdot\frac{1}{k\Omega_0}\Big[\sin\tfrac{k\pi}{2} - 0 - \big(\sin k\pi - \sin\tfrac{k\pi}{2}\big)\Big]
     = \frac{4\sin(k\pi/2)}{k\Omega_0 T_0}.
\end{aligned}
$$

Since $\Omega_0 T_0 = 2\pi$,

$$
\boxed{c_k = \frac{2}{k\pi}\,\sin\frac{k\pi}{2}}
$$

Now read off what it says:

- For $k = 0$: $c_0 = 0$. The wave spends equal time at $+1$ and $-1$, so its average is zero.
- For even $k$: $\sin(k\pi/2) = 0$, so $c_k = 0$.
- For odd $k$: $c_k = \pm\frac{2}{k\pi}$, so $|c_k| = \frac{2}{\pi|k|}$. That gives $c_1 = 0.637$, $c_3 = -0.212$, $c_5 = 0.127$, and so on.

**Only the odd harmonics survive, and they shrink like $1/k$.**

A common variant is the $0/1$ square wave with the same timing (50% duty cycle). It equals $\tfrac12\big(x(t) + 1\big)$, so it has $c_0 = \tfrac12$ and $c_k = \frac{1}{k\pi}\sin\frac{k\pi}{2}$ for $k \ne 0$.

---

## 2. The continuous-time Fourier transform

For an aperiodic signal, imagine a periodic one whose period $T_p$ grows without limit. The harmonics crowd closer and closer together until the lines merge into a continuous spectrum. In angular frequency $\Omega$:

$$
X(\Omega) = \int_{-\infty}^{\infty} x(t)\,e^{-j\Omega t}\,dt,
\qquad
x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X(\Omega)\,e^{j\Omega t}\,d\Omega.
$$

In hertz, with $\Omega = 2\pi F$, the $2\pi$ disappears from the inverse:

$$
X(F) = \int_{-\infty}^{\infty} x(t)\,e^{-j2\pi Ft}\,dt,
\qquad
x(t) = \int_{-\infty}^{\infty} X(F)\,e^{j2\pi Ft}\,dF.
$$

**The Dirichlet conditions** (final 1c, "briefly demonstrate"). The series or the transform converges if:

1. $x(t)$ has a finite number of finite discontinuities in any finite interval (in one period, for the series);
2. $x(t)$ has a finite number of maxima and minima in that interval;
3. $x(t)$ is absolutely integrable, $\int |x(t)|\,dt < \infty$ (over one period, for the series).

These conditions are sufficient, not necessary. When they hold, the series or transform converges to $x(t)$ wherever $x$ is continuous, and to the midpoint of the jump at a discontinuity.

### 2a. A rectangular pulse gives a sinc (Ex 4.1.2)

Let $x(t) = A$ for $|t| < \tau/2$ and $0$ otherwise. It is aperiodic and satisfies the Dirichlet conditions.

$$
X(\Omega) = \int_{-\tau/2}^{\tau/2} A\,e^{-j\Omega t}\,dt
= \frac{A}{-j\Omega}\Big[e^{-j\Omega\tau/2} - e^{j\Omega\tau/2}\Big]
= \frac{2A\sin(\Omega\tau/2)}{\Omega}.
$$

In hertz this becomes the famous sinc:

$$
\boxed{X(F) = A\tau\,\frac{\sin(\pi F\tau)}{\pi F\tau} = A\tau\,\operatorname{sinc}(F\tau)}
$$

Three things to say about it:

- $X(0) = A\tau$, which is the area of the pulse.
- The zeros are at $F = \pm 1/\tau, \pm 2/\tau, \ldots$, that is, at $\Omega = \pm 2\pi/\tau, \pm 4\pi/\tau, \ldots$
- **A wider pulse gives a narrower spectrum, and a narrower pulse a wider one.** This is the time–bandwidth trade-off.

### 2b. What the transform means (note p.38–39)

**$X(\Omega)$ is a recipe.** The inverse formula builds $x(t)$ by adding up exponentials, and $X(\Omega)$ says how much of each frequency goes in. If $|X|$ has one tall peak, $x(t)$ looks almost like a clean sinusoid at that frequency. If $|X|$ is spread out, there is no single tone.

**Duality.** The forward and inverse formulas are nearly identical with $t$ and $\Omega$ swapped. So a rect transforms to a sinc and a sinc transforms to a rect, and convolution in one domain is multiplication in the other.

**Phase carries most of the information.** The magnitude says *how much* of each frequency there is. The phase says *when* each component peaks relative to the others. Keep the magnitude but scramble the phase, and every recognisable feature of the signal is gone. That is why a good filter tries to preserve phase relationships, and why **linear-phase filters** are popular: they delay every frequency by the same amount, so the shape survives.

---

## 3. The discrete-time Fourier series (periodic sequences)

A periodic sequence satisfies $x[n] = x[n + N]$, and it is built from just $N$ harmonics:

$$
x[n] = \sum_{k=0}^{N-1} c_k\,e^{j2\pi kn/N},
\qquad
c_k = \frac{1}{N}\sum_{n=0}^{N-1} x[n]\,e^{-j2\pi kn/N}.
$$

The coefficients repeat, $c_{k+N} = c_k$, so only $N$ of them are distinct. With sampling rate $F_s$, the index $k = 0, \ldots, N-1$ covers the frequencies $F_k = kF_s/N$, from $0$ up to (but not including) $F_s$.

### 3a. Ex 4.2.1: determine the spectra

**(a) $x[n] = \cos(\sqrt2\,\pi n)$.** Here $\omega_0 = \sqrt2\,\pi$, so $f_0 = \omega_0/2\pi = 1/\sqrt2$, which is **irrational**. A discrete-time sinusoid is periodic only when $f_0 = k/N$ is a ratio of integers, so **this signal is not periodic** and has no DTFS. Its spectrum is a single frequency component at $\omega = \pm\sqrt2\,\pi$, which, brought back into $[-\pi, \pi]$, sits at $\pm(2 - \sqrt2)\pi$.

**(b) $x[n] = \cos(\pi n/3)$.** Now $f_0 = 1/6$, which is rational, so the period is $N = 6$. Expand with Euler's formula and match the terms with the DTFS sum:

$$
\cos\frac{\pi n}{3} = \cos\frac{2\pi n}{6} = \tfrac12 e^{j2\pi n/6} + \tfrac12 e^{-j2\pi n/6},
\qquad\text{and}\qquad
e^{-j2\pi n/6} = e^{j2\pi(5)n/6}.
$$

So $c_1 = c_5 = \tfrac12$ and $c_0 = c_2 = c_3 = c_4 = 0$.

**(c) $x[n] = \{1, 1, 0, 0\}$, repeated with $N = 4$.** Only $n = 0$ and $n = 1$ contribute to the sum:

$$
c_k = \tfrac14\big(1 + e^{-j\pi k/2}\big)
\quad\Longrightarrow\quad
c_0 = \tfrac12, \quad c_1 = \tfrac14(1 - j), \quad c_2 = 0, \quad c_3 = \tfrac14(1 + j).
$$

### 3b. A periodic train of rectangular pulses (note p.43)

One period is $x[n] = 1$ for $-N_1 \le n \le N_1$ (that is $2N_1 + 1$ ones) and $0$ for the rest of the period. Then

$$
c_k = \frac{1}{N}\sum_{n=-N_1}^{N_1} e^{-j2\pi kn/N}.
$$

**When $k = 0, \pm N, \pm 2N, \ldots$,** every term is 1, so $c_0 = (2N_1 + 1)/N$. That is the average value, the DC level.

**For every other $k$,** it is a geometric sum. Write $\alpha = 2\pi k/N$ and multiply the top and bottom by $e^{j\alpha/2}$; the result is a ratio of sines:

$$
c_k = \frac{1}{N}\,\frac{\sin\big(\alpha(N_1 + \tfrac12)\big)}{\sin(\alpha/2)}
    = \frac{1}{N}\,\frac{\sin\big(2\pi k(N_1 + \tfrac12)/N\big)}{\sin(\pi k/N)}.
$$

With $N = 10$ and $N_1 = 2$: $c_0 = 0.5$, $c_1 = 0.3236$, $c_2 = 0$, $c_3 = -0.1236$ and $c_5 = 0.1$, and an FFT agrees. This is the discrete cousin of the sinc.

### 3c. The power density spectrum of a periodic signal

The average power over one period can be computed from the coefficients. Substitute the synthesis formula for $x^*[n]$ and swap the order of the two sums:

$$
\begin{aligned}
P_x &= \frac{1}{N}\sum_{n=0}^{N-1}|x[n]|^2
     = \frac{1}{N}\sum_{n=0}^{N-1} x[n]\,x^*[n]
     = \frac{1}{N}\sum_{n=0}^{N-1} x[n]\sum_{k=0}^{N-1} c_k^*\,e^{-j2\pi kn/N} \\[6pt]
    &= \sum_{k=0}^{N-1} c_k^*\left[\frac{1}{N}\sum_{n=0}^{N-1} x[n]\,e^{-j2\pi kn/N}\right]
     = \sum_{k=0}^{N-1} c_k^*\,c_k.
\end{aligned}
$$

$$
\boxed{P_x = \sum_{k=0}^{N-1}|c_k|^2}
$$

The total power is the sum of the powers in the individual harmonics. A plot of $|c_k|^2$ against $k$ is the **power density spectrum**. For a real $x[n]$, $c_k^* = c_{-k} = c_{N-k}$, so $|c_k|$ is symmetric and you only need $k = 0, \ldots, N/2$.

Check: the $N = 10$ pulse train has $P_x = 5/10 = 0.5$, and $\sum_k |c_k|^2 = 0.5$ as well.

---

## 4. The discrete-time Fourier transform (aperiodic sequences)

$$
X(\omega) = \sum_{n=-\infty}^{\infty} x[n]\,e^{-j\omega n},
\qquad
x[n] = \frac{1}{2\pi}\int_{2\pi} X(\omega)\,e^{j\omega n}\,d\omega.
$$

Two facts to state whenever you use it:

- **It is always periodic with period $2\pi$:** $X(\omega + 2\pi) = X(\omega)$, because $e^{-j2\pi n} = 1$ for every integer $n$.
- **It converges if $x[n]$ is absolutely summable,** $\sum_n |x[n]| < \infty$. The spectrum is then a continuous function of $\omega$.

### 4a. Final 2c: the DTFT of $x[n] = a^n u[n]$ with $|a| < 1$

$$
X(\omega) = \sum_{n=0}^{\infty}\big(ae^{-j\omega}\big)^n = \frac{1}{1 - ae^{-j\omega}},
$$

which converges because $|ae^{-j\omega}| = |a| < 1$. Its squared magnitude is the energy density spectrum:

$$
S_{xx}(\omega) = |X(\omega)|^2 = \frac{1}{(1 - ae^{-j\omega})(1 - ae^{j\omega})} = \frac{1}{1 - 2a\cos\omega + a^2}.
$$

With $a = 0.5$, $S_{xx}(0) = 4$ and $S_{xx}(\pi) = 0.444$. The energy sits at low frequencies, so this is a **low-pass signal**. With $a < 0$ it flips and becomes high-pass.

### 4b. Final 2e: $x[n] = a^n$ for $0 \le n \le M-1$

*The paper hints: use the time-shift property $g[n - n_0] \leftrightarrow e^{-j\omega n_0}G(\omega)$.*

**Directly,** it is a finite geometric series:

$$
X(\omega) = \sum_{n=0}^{M-1}\big(ae^{-j\omega}\big)^n = \frac{1 - a^M e^{-j\omega M}}{1 - ae^{-j\omega}}.
$$

**The way the hint wants:** write the finite sequence as an infinite one minus a shifted copy of itself,

$$
x[n] = a^n u[n] - a^M\cdot a^{n-M}u[n-M],
$$

and transform each piece, using the time-shift property on the second:

$$
X(\omega) = \frac{1}{1 - ae^{-j\omega}} - a^M e^{-j\omega M}\,\frac{1}{1 - ae^{-j\omega}} = \frac{1 - a^M e^{-j\omega M}}{1 - ae^{-j\omega}}.
$$

Same answer, and this route shows the examiner you used the property he asked for.

### 4c. A rectangular sequence (Proakis Ex 4.2.3): $x[n] = A$ for $0 \le n \le L-1$

Use the same factoring trick as for the moving average (Topic 1, Section 5):

$$
X(\omega) = A\,\frac{1 - e^{-j\omega L}}{1 - e^{-j\omega}} = A\,e^{-j\omega(L-1)/2}\,\frac{\sin(\omega L/2)}{\sin(\omega/2)}.
$$

Here $|X(0)| = AL$ and the zeros are at $\omega = 2\pi k/L$. This is the discrete version of the sinc.

### 4d. The energy density spectrum and Parseval's relation

Write $|x[n]|^2 = x[n]\,x^*[n]$, replace $x^*[n]$ by its inverse-DTFT integral, and swap the sum and the integral:

$$
\begin{aligned}
E_x &= \sum_{n=-\infty}^{\infty}|x[n]|^2 = \sum_n x[n]\,x^*[n]
     = \sum_n x[n]\left[\frac{1}{2\pi}\int_{-\pi}^{\pi} X^*(\omega)\,e^{-j\omega n}\,d\omega\right] \\[6pt]
    &= \frac{1}{2\pi}\int_{-\pi}^{\pi} X^*(\omega)\left[\sum_n x[n]\,e^{-j\omega n}\right]d\omega
     = \frac{1}{2\pi}\int_{-\pi}^{\pi}|X(\omega)|^2\,d\omega.
\end{aligned}
$$

$$
\boxed{E_x = \sum_{n=-\infty}^{\infty}|x[n]|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi}|X(\omega)|^2\,d\omega}
$$

The function $S_{xx}(\omega) = |X(\omega)|^2$ is the **energy density spectrum**: it tells you how much of the energy sits in each small slice of frequency.

**Final 2f (continuous-time Parseval).** Find the energy of $x_a(t) = e^{-\alpha t}u(t)$ with $\alpha = 0.6$.

In the time domain the integral is easy:

$$
E = \int_0^{\infty} e^{-2\alpha t}\,dt = \frac{1}{2\alpha} = \frac{1}{1.2} = 0.8333 \text{ J}.
$$

In the frequency domain, $X(F) = \dfrac{1}{\alpha + j2\pi F}$, so $|X(F)|^2 = \dfrac{1}{\alpha^2 + 4\pi^2F^2}$. Parseval says $\int_{-\infty}^{\infty}|X(F)|^2\,dF$ gives the same $0.8333$, and numerical integration agrees.

**Final 1b.** Find the energy and the power of $x[n] = (-1)^n$.

Every sample has $|x[n]|^2 = 1$, so the energy is $E = \sum 1 = \infty$ and this is **not** an energy signal. The power is

$$
P = \lim_{N\to\infty}\frac{1}{2N+1}\sum_{n=-N}^{N} 1 = 1,
$$

so it is a **power signal**. Its spectrum sits entirely at $\omega = \pi$, the highest discrete-time frequency, because $(-1)^n = \cos\pi n$.

### 4e. Symmetry for real signals (note p.48, 51)

Split $e^{-j\omega n} = \cos\omega n - j\sin\omega n$ to separate the real and imaginary parts:

$$
X(\omega) = X_R(\omega) + jX_I(\omega),
\qquad
X_R(\omega) = \sum_n x[n]\cos\omega n,
\qquad
X_I(\omega) = -\sum_n x[n]\sin\omega n.
$$

Cosine is even and sine is odd, so for a real $x[n]$

$$
X_R(-\omega) = X_R(\omega)\ \ (\text{even}),
\qquad
X_I(-\omega) = -X_I(\omega)\ \ (\text{odd}),
\qquad\text{hence}\qquad
X(-\omega) = X^*(\omega).
$$

This is called Hermitian symmetry. It means $|X(\omega)|$ is even, $\angle X(\omega)$ is odd, and $S_{xx}(\omega)$ is even. So for a real signal you only need $0 \le \omega \le \pi$ (or $0 \le F \le F_s/2$), which halves the work.

---

## 5. The Fourier transform and the z-transform (note p.49)

Take $X(z) = \sum_n x[n]\,z^{-n}$ with ROC $r_2 < |z| < r_1$, and put $z = re^{j\omega}$:

$$
X(z)\Big|_{z = re^{j\omega}} = \sum_n\big[x[n]\,r^{-n}\big]\,e^{-j\omega n}.
$$

That is the DTFT of the weighted sequence $x[n]\,r^{-n}$. If the ROC contains the unit circle, set $r = 1$:

$$
\boxed{X(\omega) = X(z)\Big|_{z = e^{j\omega}}}
$$

**The Fourier transform is the z-transform evaluated on the unit circle.** If the ROC does not include the unit circle, as for $2^n u[n]$, the DTFT does not exist even though $X(z)$ does.

---

## 6. Classifying signals by frequency content (note p.49)

| Class | Where the energy is | Example |
|---|---|---|
| Low-frequency | around $\omega = 0$ ($F = 0$) | slowly varying waves, a DC level, an ECG |
| High-frequency | near $\omega = \pi$ ($F = F_s/2$) | $(-1)^n$, sharp edges |
| Medium-frequency (band-pass) | somewhere in between | a radio station's signal |

The **bandwidth** is $F_2 - F_1$, the range of frequencies that holds most of the energy (say 95%).

- **Narrowband:** $F_2 - F_1 \ll (F_1 + F_2)/2$; the spectrum is a thin spike.
- **Wideband:** the energy is spread over a broad range.
- **Bandlimited:** $X(F) = 0$ for $|F| > B$. A signal cannot be both bandlimited and time-limited.

---

## 7. Properties of the DTFT (note p.50–53)

| # | Property | $x[n]$ | $X(\omega)$ |
|---|---|---|---|
| 1 | Linearity | $a_1x_1[n] + a_2x_2[n]$ | $a_1X_1(\omega) + a_2X_2(\omega)$ |
| 2 | Time shift | $x[n-k]$ | $e^{-j\omega k}X(\omega)$ |
| 3 | Frequency shift | $e^{j\omega_0 n}x[n]$ | $X(\omega - \omega_0)$ |
| 4 | Modulation | $x[n]\cos\omega_0 n$ | $\tfrac12\big[X(\omega - \omega_0) + X(\omega + \omega_0)\big]$ |
| 5 | Convolution | $x_1[n] * x_2[n]$ | $X_1(\omega)\,X_2(\omega)$ |
| 6 | Correlation | $r_{x_1x_2}[m] = \sum_n x_1[n]\,x_2[n-m]$ | $S_{x_1x_2}(\omega) = X_1(\omega)\,X_2(-\omega)$ |
| 7 | Symmetry (real $x$) | $x[n]$ real | $X(-\omega) = X^*(\omega)$ |
| 8 | Periodicity | any $x[n]$ | $X(\omega + 2\pi) = X(\omega)$ |

Notice what row 2 says: **a time shift changes only the phase**, never the magnitude.

The proofs to have ready, two lines each:

**Time shift.** Substitute $m = n - k$:

$$
\sum_n x[n-k]\,e^{-j\omega n} = e^{-j\omega k}\sum_m x[m]\,e^{-j\omega m} = e^{-j\omega k}X(\omega).
$$

**Frequency shift.** Combine the two exponentials:

$$
\sum_n e^{j\omega_0 n}x[n]\,e^{-j\omega n} = \sum_n x[n]\,e^{-j(\omega - \omega_0)n} = X(\omega - \omega_0).
$$

**Modulation.** Write $\cos\omega_0 n = \tfrac12\big(e^{j\omega_0 n} + e^{-j\omega_0 n}\big)$ and apply the frequency shift twice.

**Correlation.** Substitute $k = n - m$ in the inner sum:

$$
S_{x_1x_2}(\omega) = \sum_m\sum_n x_1[n]\,x_2[n-m]\,e^{-j\omega m}
= \sum_n x_1[n]\,e^{-j\omega n}\sum_k x_2[k]\,e^{j\omega k}
= X_1(\omega)\,X_2(-\omega).
$$

---

## 8. The properties from the missing slides (Proakis §4.4)

| # | Property | $x[n]$ | $X(\omega)$ |
|---|---|---|---|
| 9 | Time reversal | $x[-n]$ | $X(-\omega)$ |
| 10 | Wiener–Khintchine | $r_{xx}[m]$ (autocorrelation) | $S_{xx}(\omega) = \lvert X(\omega)\rvert^2$ |
| 11 | Multiplication (windowing) | $x_1[n]\,x_2[n]$ | $\frac{1}{2\pi}\int_{-\pi}^{\pi} X_1(\lambda)\,X_2(\omega - \lambda)\,d\lambda$ |
| 12 | Differentiation in frequency | $n\,x[n]$ | $j\,\frac{dX(\omega)}{d\omega}$ |
| 13 | Parseval (general form) | $\sum_n x_1[n]\,x_2^*[n]$ | $\frac{1}{2\pi}\int_{-\pi}^{\pi} X_1(\omega)\,X_2^*(\omega)\,d\omega$ |
| 14 | Conjugation | $x^*[n]$ | $X^*(-\omega)$ |

**Time reversal.** Substitute $\ell = -n$:

$$
\sum_n x[-n]\,e^{-j\omega n} = \sum_\ell x[\ell]\,e^{-j(-\omega)\ell} = X(-\omega).
$$

**Wiener–Khintchine.** Autocorrelation is row 6 with $x_1 = x_2 = x$, so $S_{xx}(\omega) = X(\omega)\,X(-\omega) = X(\omega)\,X^*(\omega) = |X(\omega)|^2$ for real $x$. In words: *the autocorrelation and the energy density spectrum form a Fourier transform pair.*

**Windowing.** Cutting a signal short (multiplying it by a window) **convolves** its spectrum with the window's spectrum. That is why truncation smears the spectrum and adds ripples, the Gibbs phenomenon.

**Differentiation in frequency.** Differentiate the DTFT term by term:

$$
\frac{d}{d\omega}\sum_n x[n]\,e^{-j\omega n} = \sum_n(-jn)\,x[n]\,e^{-j\omega n}
\quad\Longrightarrow\quad
n\,x[n] \;\longleftrightarrow\; j\,\frac{dX(\omega)}{d\omega}.
$$

---

## 9. Ten-minute self-test

| # | Question | Answer |
|---|---|---|
| 1 | Which transform for CT periodic, CT aperiodic, DT periodic, DT aperiodic signals? | CTFS, CTFT, DTFS, DTFT |
| 2 | Coefficients of the $\pm 1$ square wave | $c_k = \frac{2}{k\pi}\sin\frac{k\pi}{2}$: odd harmonics only, falling like $1/k$, $c_0 = 0$ |
| 3 | Fourier transform of a rect pulse (height $A$, width $\tau$) | $A\tau\operatorname{sinc}(F\tau)$, with zeros at $F = k/\tau$ |
| 4 | The three Dirichlet conditions | finite discontinuities, finite maxima and minima, absolutely integrable |
| 5 | Is $\cos(\sqrt2\,\pi n)$ periodic? | No: $f_0 = 1/\sqrt2$ is irrational |
| 6 | DTFS of $\cos(\pi n/3)$ | $N = 6$, $c_1 = c_5 = \frac12$, the rest $0$ |
| 7 | DTFS of $\{1, 1, 0, 0\}$ | $\frac12,\ \frac{1-j}{4},\ 0,\ \frac{1+j}{4}$ |
| 8 | Power of a periodic signal from its $c_k$ | $P = \sum_k \lvert c_k\rvert^2$ |
| 9 | DTFT of $a^n u[n]$ and its $S_{xx}$ | $\frac{1}{1 - ae^{-j\omega}}$ and $\frac{1}{1 - 2a\cos\omega + a^2}$ |
| 10 | Energy of $e^{-0.6t}u(t)$ | $\frac{1}{2(0.6)} = 0.8333$ |
| 11 | Energy and power of $(-1)^n$ | $E = \infty$, $P = 1$: a power signal |
| 12 | For real $x[n]$, symmetry of $\lvert X\rvert$ and $\angle X$ | even and odd |
| 13 | DTFT versus z-transform | $X(\omega) = X(z)$ at $z = e^{j\omega}$, if the ROC contains the unit circle |
| 14 | $x[n]\cos\omega_0 n$ transforms to? | $\frac12[X(\omega - \omega_0) + X(\omega + \omega_0)]$ |
| 15 | Wiener–Khintchine theorem | $r_{xx}[m] \leftrightarrow S_{xx}(\omega) = \lvert X(\omega)\rvert^2$ |
