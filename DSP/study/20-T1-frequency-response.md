# Topic 1 · Frequency Response of LTI Systems

*Mitra §4.8 – 4.8.7 · Question 1 of the paper · counts as **Quiz 2** (5 marks)*

This follows the order of your class note (`Note/Mid-2 note.pdf`, pages 13–24) and works through every exercise it lists: Mitra 4.54, 4.56, 4.57, 4.60, 4.61, 4.63, 4.64, 4.68 and 4.76. Every number here was checked in Python.

A good way to use it: read a section, close the file, and try to write the derivation on paper from memory. Then compare.

---

## 0. The whole topic in six sentences

1. Feed the complex sinusoid $e^{j\omega n}$ into an LTI system and the same sinusoid comes out, multiplied by one complex number, $H(e^{j\omega})$.
2. That number is $H(e^{j\omega}) = \sum_k h[k]\,e^{-j\omega k}$, the DTFT of the impulse response. It is called the **frequency response**.
3. In polar form, $H(e^{j\omega}) = |H(e^{j\omega})|\,e^{j\theta(\omega)}$. The magnitude is the gain at that frequency and $\theta(\omega)$ is the phase shift.
4. So a cosine goes in and a cosine comes out, at the same frequency, scaled by $|H|$ and shifted by $\theta$.
5. If the input is switched on at $n = 0$ instead of running forever, you get that steady-state cosine *plus* a transient, which dies away if the system is stable.
6. A filter is just an $|H|$ chosen on purpose: close to 1 at the frequencies you want to keep, close to 0 at the ones you want to remove.

---

## 1. Why $e^{j\omega n}$ is special: the eigenfunction proof

*Syllabus 4.8 and 4.8.1. The most likely "prove that" part of the question.*

Start with the idea. Convolution adds up delayed copies of the input, and for most inputs that changes the shape. A complex exponential is different: a delayed copy of it, $e^{j\omega(n-k)}$, is the original multiplied by a constant, $e^{-j\omega k}$. So when convolution adds up delayed copies, it is really adding constants times the *same* signal, and the shape survives.

**In the exam, write:**

For an LTI system with impulse response $h[n]$, the output is the convolution sum

$$
y[n] = \sum_{k=-\infty}^{\infty} h[k]\,x[n-k].
$$

Let $x[n] = e^{j\omega n}$ for all $n$. Then

$$
\begin{aligned}
y[n] &= \sum_{k=-\infty}^{\infty} h[k]\,e^{j\omega(n-k)}
      = e^{j\omega n}\underbrace{\sum_{k=-\infty}^{\infty} h[k]\,e^{-j\omega k}}_{H(e^{j\omega})} \\[4pt]
     &= H(e^{j\omega})\,e^{j\omega n}.
\end{aligned}
$$

The sum depends on $\omega$ but not on $n$, so for a given frequency it is a constant. The output is the input multiplied by a constant. Therefore $e^{j\omega n}$ is an **eigenfunction** of every LTI system, and $H(e^{j\omega})$ is the corresponding **eigenvalue**. $H(e^{j\omega})$ is called the frequency response.

Your note draws an arrow from $e^{j\omega n}$ to the word "eigenfunction" and from $H(e^{j\omega})$ to "eigenvalue". Do the same; that labelling is worth a mark.

**A small example from the note.** Suppose $H(e^{j\omega}) = 2e^{-j\pi/4}$ at some frequency. Then

$$
x[n] = e^{j\omega n} \quad\longmapsto\quad y[n] = 2e^{-j\pi/4}\,e^{j\omega n} = 2e^{j(\omega n - \pi/4)}.
$$

The amplitude doubled, the phase moved back by $\pi/4$, and the frequency $\omega$ did not change. An LTI system can never create a new frequency.

### 1a. Exercise 4.54

**(i) Show that $z^n$ is an eigenfunction, for any complex constant $z$.**

$$
y[n] = \sum_k h[k]\,z^{n-k} = z^n\sum_k h[k]\,z^{-k} = H(z)\,z^n.
$$

The sum does not depend on $n$, so $z^n$ is an eigenfunction and its eigenvalue is $H(z)$, the z-transform of $h[n]$.

**(ii) Is $v[n] = z^n u[n]$ an eigenfunction?**

$$
y[n] = \sum_k h[k]\,z^{n-k}\,u[n-k] = z^n\sum_k h[k]\,z^{-k}\,u[n-k].
$$

This time the sum still contains $u[n-k]$, so it *does* depend on $n$. It is not a constant, so $z^n u[n]$ is **not** an eigenfunction.

The reason is worth remembering. Switching the input on at $n = 0$ is exactly what creates a transient (Section 6). The output needs a few samples to settle into $H(z)\,z^n$.

---

## 2. Magnitude, phase, decibels and symmetry

*Syllabus 4.8.1 and 4.8.2.*

$H(e^{j\omega})$ is a complex number at each frequency, so it can be written two ways:

$$
H(e^{j\omega}) = H_R(\omega) + jH_I(\omega) = |H(e^{j\omega})|\,e^{j\theta(\omega)}.
$$

| Name | Formula | What it tells you |
|---|---|---|
| Magnitude response | $\lvert H(e^{j\omega})\rvert = \sqrt{H_R^2(\omega) + H_I^2(\omega)}$ | how much that frequency is amplified or shrunk |
| Phase response | $\theta(\omega) = \tan^{-1}\big(H_I(\omega)/H_R(\omega)\big)$ | how far that frequency is shifted (mind the quadrant) |
| Gain in dB | $\mathcal{G}(\omega) = 20\log_{10}\lvert H(e^{j\omega})\rvert$ | positive amplifies, zero leaves alone, negative attenuates |
| Periodicity | $H(e^{j(\omega + 2\pi)}) = H(e^{j\omega})$ | you only ever need $-\pi \le \omega \le \pi$ |
| Real $h[n]$ | $H(e^{-j\omega}) = H^*(e^{j\omega})$ | magnitude is even, phase is odd, so $0 \le \omega \le \pi$ is enough |
| Convolution | $y = h * x \iff Y(e^{j\omega}) = H(e^{j\omega})\,X(e^{j\omega})$ | so $H = Y/X$ |

**Watch the quadrant.** A calculator's $\tan^{-1}$ only returns angles between $-90^\circ$ and $+90^\circ$. If the real part $H_R$ is negative, the true angle is in the left half of the plane, so add or subtract $180^\circ$. For example, $H = -18$ at $\omega = \pi$ has phase $\pm 180^\circ$, not $0$.

---

## 3. Sinusoid in, sinusoid out: the steady-state response

*Syllabus 4.8.2. Sir has asked this derivation before (note p.19).*

> **Question.** Develop an expression for the steady-state response of an LTI discrete-time system with real impulse response $h[n]$ to the input $x[n] = A\cos(\omega_0 n + \phi)$, in terms of $H(e^{j\omega})$.

The plan: a cosine is two complex exponentials (Euler), each exponential is an eigenfunction (Section 1), so each one is simply multiplied by $H$ at its own frequency. Then put them back together.

**In the exam, write:**

By Euler's formula,

$$
x[n] = A\cos(\omega_0 n + \phi) = \frac{A}{2}\,e^{j\phi}e^{j\omega_0 n} + \frac{A}{2}\,e^{-j\phi}e^{-j\omega_0 n}.
$$

Each exponential is an eigenfunction, so by linearity

$$
y[n] = \frac{A}{2}\,e^{j\phi}H(e^{j\omega_0})\,e^{j\omega_0 n} + \frac{A}{2}\,e^{-j\phi}H(e^{-j\omega_0})\,e^{-j\omega_0 n}.
$$

Because $h[n]$ is real, $H(e^{-j\omega_0}) = H^*(e^{j\omega_0})$. Write $H(e^{j\omega_0}) = |H(e^{j\omega_0})|\,e^{j\theta(\omega_0)}$, so that $H(e^{-j\omega_0}) = |H(e^{j\omega_0})|\,e^{-j\theta(\omega_0)}$. Then

$$
\begin{aligned}
y[n] &= \frac{A}{2}\,|H(e^{j\omega_0})|\Big[e^{j(\omega_0 n + \phi + \theta(\omega_0))} + e^{-j(\omega_0 n + \phi + \theta(\omega_0))}\Big] \\[4pt]
     &= \boxed{A\,|H(e^{j\omega_0})|\cos\big(\omega_0 n + \phi + \theta(\omega_0)\big)}
\end{aligned}
$$

The output is a cosine at the **same frequency**. Its amplitude is multiplied by $|H(e^{j\omega_0})|$ and its phase is shifted by $\theta(\omega_0)$.

### 3a. Past paper 5c: $h[n] = \{-3, 6, -5, 4\}$ for $0 \le n \le 3$, input $A\cos(\omega_0 n)$

The frequency response is just the DTFT of four numbers:

$$
H(e^{j\omega}) = \sum_{n=0}^{3} h[n]\,e^{-j\omega n} = -3 + 6e^{-j\omega} - 5e^{-j2\omega} + 4e^{-j3\omega},
$$

and the output is

$$
y[n] = A\,|H(e^{j\omega_0})|\cos\big(\omega_0 n + \theta(\omega_0)\big).
$$

If sir gives a particular $\omega_0$, plug it in. These values are all checked:

| $\omega_0$ | $H(e^{j\omega_0})$ | $\lvert H\rvert$ | $\theta(\omega_0)$ |
|---|---|---|---|
| $0$ | $2$ | $2$ | $0$ |
| $\pi/4$ | $-1.586 - 2.071j$ | $2.608$ | $-127.4^\circ$ (third quadrant) |
| $\pi/2$ | $2 - 2j$ | $2.828$ | $-45^\circ$ |
| $\pi$ | $-18$ | $18$ | $\pm 180^\circ$ |

So at $\omega_0 = \pi/2$ the answer is $y[n] = 2.828A\cos(\pi n/2 - \pi/4)$.

Here is the $\pi/2$ row by hand. Going round the unit circle in quarter turns, $e^{-j\pi/2} = -j$, $e^{-j\pi} = -1$ and $e^{-j3\pi/2} = +j$. So

$$
H(e^{j\pi/2}) = -3 + 6(-j) - 5(-1) + 4(j) = 2 - 2j.
$$

### 3b. Mitra 4.68: $h[n] = (0.4)^n u[n]$ and $x[n] = \sin(\pi n/4)\,u[n]$. Find $y_{ss}[n]$.

First the frequency response. It is a geometric series, and it converges because $|0.4| < 1$:

$$
H(e^{j\omega}) = \sum_{n=0}^{\infty}\big(0.4e^{-j\omega}\big)^n = \frac{1}{1 - 0.4e^{-j\omega}}.
$$

Now evaluate it at the input frequency $\omega = \pi/4$, where $e^{-j\pi/4} = \tfrac{1}{\sqrt2} - \tfrac{j}{\sqrt2} \approx 0.7071 - 0.7071j$:

$$
\begin{aligned}
1 - 0.4e^{-j\pi/4} &= 1 - 0.4(0.7071 - 0.7071j) = 0.71716 + 0.28284j, \\[4pt]
H(e^{j\pi/4}) &= \frac{1}{0.71716 + 0.28284j} = 1.20669 - 0.47591j.
\end{aligned}
$$

So the gain and the phase are

$$
|H(e^{j\pi/4})| = 1.29715, \qquad \theta(\pi/4) = \tan^{-1}\frac{-0.47591}{1.20669} = -21.52^\circ = -0.3757 \text{ rad}.
$$

The input is a sine, so the output is a sine:

$$
\boxed{y_{ss}[n] = 1.29715\,\sin\!\left(\frac{\pi n}{4} - 0.3757\right)}
$$

Two things to notice. At $-\pi/4$ you get the conjugate, $1.20669 + 0.47591j$, with the same magnitude and phase $+21.52^\circ$; that is the symmetry from Section 2. And if you simulate the true output, by $n = 50$ it matches this formula to 15 digits, so the transient really has died out.

---

## 4. FIR frequency responses and the cascade exercises

For an FIR filter the convolution sum is finite, $y[n] = \sum_{k=N_1}^{N_2} h[k]\,x[n-k]$, so the frequency response is a finite sum with no convergence worries:

$$
H(e^{j\omega}) = \sum_{k=N_1}^{N_2} h[k]\,e^{-j\omega k}.
$$

These DTFT pairs from note p.16 are enough to do every exercise below almost in your head:

| $x[n]$ | $X(e^{j\omega})$ |
|---|---|
| $\delta[n]$ | $1$ |
| $\delta[n-k]$ | $e^{-j\omega k}$ |
| $a^n u[n]$, with $\lvert a\rvert < 1$ | $\dfrac{1}{1 - ae^{-j\omega}}$ |
| $c\,x[n]$ | $c\,X(e^{j\omega})$ |
| $x[n - n_0]$ | $e^{-j\omega n_0}X(e^{j\omega})$ |

### 4a. Mitra 4.56: $h[n] = \delta[n] - \alpha\,\delta[n-R]$. Find $G(e^{j\omega})$ for $g[n] = h[n] * h[n] * h[n]$.

Each copy of $h$ has $H(e^{j\omega}) = 1 - \alpha e^{-j\omega R}$. Convolution in time is multiplication in frequency, so three convolutions give a cube. Expand it with $(1 - u)^3 = 1 - 3u + 3u^2 - u^3$, taking $u = \alpha e^{-j\omega R}$:

$$
G(e^{j\omega}) = \big(1 - \alpha e^{-j\omega R}\big)^3 = 1 - 3\alpha e^{-j\omega R} + 3\alpha^2 e^{-j2\omega R} - \alpha^3 e^{-j3\omega R}.
$$

> **Your note has a slip here.** It writes $1 - 3e^{-j\omega R} + 3e^{-j2\omega R} + e^{-j3\omega R}$, which drops every $\alpha$ and gets the last sign wrong. Use the version above.

### 4b. Mitra 4.64: when is the cascade all-pass?

The cascade is $h_1[n] = \alpha\,\delta[n] + \delta[n-1]$ followed by $h_2[n] = \beta^n u[n]$ with $|\beta| < 1$. For which $\alpha$ and $\beta$ is $|H(e^{j\omega})| = 1$ at every frequency?

Multiply the two frequency responses:

$$
H(e^{j\omega}) = H_1(e^{j\omega})\,H_2(e^{j\omega}) = \frac{\alpha + e^{-j\omega}}{1 - \beta e^{-j\omega}}.
$$

$|H| = 1$ means the top and the bottom have the same magnitude. Square both sides, using $|z|^2 = z\,z^*$:

$$
\begin{aligned}
\big|\alpha + e^{-j\omega}\big|^2 &= \big|1 - \beta e^{-j\omega}\big|^2 \\[2pt]
\alpha^2 + 2\alpha\cos\omega + 1 &= 1 - 2\beta\cos\omega + \beta^2.
\end{aligned}
$$

This has to hold at *every* $\omega$, so the constant terms must match and the $\cos\omega$ terms must match:

$$
\alpha^2 = \beta^2 \quad\text{and}\quad 2\alpha = -2\beta
\qquad\Longrightarrow\qquad
\boxed{\alpha = -\beta, \quad |\beta| < 1}
$$

The second condition already implies the first. A filter whose magnitude is 1 at every frequency is called an **all-pass** filter: it changes only the phase. With $\beta = 0.6$ and $\alpha = -0.6$, $|H| = 1.000$ at every $\omega$ tested.

### 4c. Mitra 4.76: show that this third-order system is all-pass

$$
y[n] = d_3x[n] + d_2x[n-1] + d_1x[n-2] + x[n-3] - d_1y[n-1] - d_2y[n-2] - d_3y[n-3]
$$

Take the DTFT of both sides and solve for $Y/X$:

$$
H(e^{j\omega}) = \frac{d_3 + d_2e^{-j\omega} + d_1e^{-j2\omega} + e^{-j3\omega}}{1 + d_1e^{-j\omega} + d_2e^{-j2\omega} + d_3e^{-j3\omega}}.
$$

Call the denominator $D(e^{j\omega})$. The numerator has the same coefficients in reverse order. Factor $e^{-j3\omega}$ out of it:

$$
d_3 + d_2e^{-j\omega} + d_1e^{-j2\omega} + e^{-j3\omega}
= e^{-j3\omega}\big(1 + d_1e^{j\omega} + d_2e^{j2\omega} + d_3e^{j3\omega}\big)
= e^{-j3\omega}\,D^*(e^{j\omega}),
$$

because the $d_i$ are real. Therefore

$$
|H(e^{j\omega})| = \frac{|e^{-j3\omega}|\,|D^*(e^{j\omega})|}{|D(e^{j\omega})|} = \frac{1\cdot|D(e^{j\omega})|}{|D(e^{j\omega})|} = 1 \quad\text{for every } \omega. \qquad\blacksquare
$$

**A pattern worth spotting:** if the numerator's coefficients are the denominator's coefficients read backwards, the filter is all-pass.

### 4d. Mitra 4.61: when is this non-causal FIR zero-phase?

$$
h[n] = a_1\delta[n-3] + a_2\delta[n-2] + a_3\delta[n-1] + a_4\delta[n] + a_5\delta[n+1] + a_6\delta[n+2]
$$

"Zero phase" means $H(e^{j\omega})$ is real at every frequency. For a real $h[n]$ that happens exactly when $h[n]$ is even, $h[n] = h[-n]$, because then each pair of terms gives $h[k]\big(e^{-j\omega k} + e^{j\omega k}\big) = 2h[k]\cos\omega k$, which is real.

So match the samples in pairs:

- $n = \pm 3$: $h[3] = a_1$ but $h[-3] = 0$, so $a_1 = 0$.
- $n = \pm 2$: $a_2 = a_6$.
- $n = \pm 1$: $a_3 = a_5$.
- $n = 0$: $a_4$ can be any real number.

### 4e. Mitra 4.63: for which $k$ is the frequency response real?

$$
y[n] = a_1x[n+k] + a_2x[n+k-1] + a_3x[n+k-2] + a_2x[n+k-3] + a_1x[n+k-4]
$$

Every term carries a factor $e^{j\omega k}$, so pull it out:

$$
H(e^{j\omega}) = e^{j\omega k}\big(a_1 + a_2e^{-j\omega} + a_3e^{-j2\omega} + a_2e^{-j3\omega} + a_1e^{-j4\omega}\big).
$$

The coefficients inside are symmetric about the middle one, so factor out $e^{-j2\omega}$ and pair the terms using $e^{j\theta} + e^{-j\theta} = 2\cos\theta$:

$$
H(e^{j\omega}) = e^{j\omega(k-2)}\big[a_3 + 2a_2\cos\omega + 2a_1\cos 2\omega\big].
$$

The bracket is real. So $H$ is real at every $\omega$ exactly when $e^{j\omega(k-2)} = 1$, which means $\boxed{k = 2}$.

### 4f. Mitra 4.57: $g[n] = \alpha^n$ for $0 \le n \le M-1$. Find $G(e^{j\omega})$ and scale it to unity DC gain.

It is a finite geometric series, $\sum_{n=0}^{M-1} r^n = \dfrac{1 - r^M}{1 - r}$, with $r = \alpha e^{-j\omega}$:

$$
G(e^{j\omega}) = \sum_{n=0}^{M-1}\big(\alpha e^{-j\omega}\big)^n = \frac{1 - \alpha^M e^{-j\omega M}}{1 - \alpha e^{-j\omega}}.
$$

"DC gain" means the value at $\omega = 0$:

$$
G(e^{j0}) = \frac{1 - \alpha^M}{1 - \alpha}.
$$

To make that equal to 1, multiply $g[n]$ by its reciprocal:

$$
\boxed{g'[n] = \frac{1 - \alpha}{1 - \alpha^M}\,\alpha^n, \qquad 0 \le n \le M-1}
$$

Check: with $\alpha = 0.5$ and $M = 4$, the DC value is $1 + 0.5 + 0.25 + 0.125 = 1.875$, and $(1 - 0.0625)/0.5 = 1.875$ too.

---

## 5. The moving-average filter

*Syllabus 4.8.4. If it is asked, it is a full derivation, and it is close to free marks once you have practised it.*

Past paper 5b: *"Compute the magnitude and phase response of a 5-point moving average filter."*

**The picture first.** A moving average replaces each sample by the average of the last $M$ samples. Slow changes survive the averaging; fast wiggles cancel themselves out. So expect a low-pass filter before writing a single line.

**In the exam, write:**

The $M$-point moving-average filter is

$$
y[n] = \frac{1}{M}\sum_{\ell=0}^{M-1} x[n-\ell],
\qquad\text{so}\qquad
h[n] = \begin{cases} 1/M, & 0 \le n \le M-1, \\ 0, & \text{otherwise.} \end{cases}
$$

The impulse response has finite length, so this is an FIR filter. Its frequency response is a finite geometric series:

$$
H(e^{j\omega}) = \frac{1}{M}\sum_{n=0}^{M-1} e^{-j\omega n} = \frac{1}{M}\cdot\frac{1 - e^{-j\omega M}}{1 - e^{-j\omega}}.
$$

Factor $e^{-j\omega M/2}$ out of the numerator and $e^{-j\omega/2}$ out of the denominator, so that each bracket becomes a sine:

$$
\begin{aligned}
H(e^{j\omega})
&= \frac{1}{M}\cdot\frac{e^{-j\omega M/2}\big(e^{j\omega M/2} - e^{-j\omega M/2}\big)}{e^{-j\omega/2}\big(e^{j\omega/2} - e^{-j\omega/2}\big)}
 = \frac{1}{M}\cdot e^{-j(M-1)\omega/2}\cdot\frac{2j\sin(M\omega/2)}{2j\sin(\omega/2)} \\[6pt]
&= \boxed{\frac{1}{M}\,\frac{\sin(M\omega/2)}{\sin(\omega/2)}\;e^{-j(M-1)\omega/2}}
\end{aligned}
$$

Reading off the magnitude and the phase:

$$
|H(e^{j\omega})| = \left|\frac{1}{M}\,\frac{\sin(M\omega/2)}{\sin(\omega/2)}\right|,
\qquad
\theta(\omega) = -\frac{(M-1)\,\omega}{2} + \pi\sum_{k=1}^{\lfloor M/2\rfloor}\mu\!\left(\omega - \frac{2\pi k}{M}\right), \quad 0 \le \omega \le \pi,
$$

where $\mu(\cdot)$ is the unit step function (Mitra's notation).

**Why does the phase have those $+\pi$ jumps?** The ratio $\sin(M\omega/2)/\sin(\omega/2)$ is real, but it turns negative after each zero at $\omega = 2\pi k/M$. A negative real number is its magnitude times $e^{j\pi}$, so the phase picks up an extra $\pi$ at each zero. Between the jumps the phase is a straight line of slope $-(M-1)/2$, and a straight-line phase means a pure delay of $(M-1)/2$ samples.

### 5a. The 5-point case, with numbers

With $M = 5$:

$$
|H(e^{j\omega})| = \left|\frac{\sin(5\omega/2)}{5\sin(\omega/2)}\right|,
\qquad
\theta(\omega) = -2\omega \;\; \text{(plus } \pi \text{ after } 2\pi/5 \text{, and again after } 4\pi/5\text{)}.
$$

| $\omega$ | $0$ | $\pi/5$ | $2\pi/5$ | $\pi/2$ | $4\pi/5$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\lvert H(e^{j\omega})\rvert$ | $1$ | $0.647$ | $\mathbf{0}$ | $0.2$ | $\mathbf{0}$ | $0.2$ |

The zeros are at $\omega = 2\pi/5$ and $4\pi/5$. At $\omega = 0$ the gain is exactly 1, so DC passes untouched, and the gain is small at high frequencies. That confirms it is a **low-pass filter**.

**To sketch it:** a main lobe from $0$ to $2\pi/5$ with height 1, then small side bumps no taller than about $0.25$. The phase is a sawtooth: a line of slope $-2$ that jumps up by $\pi$ at each zero.

---

## 6. Steady-state and transient response

*Syllabus 4.8.5.*

When an input is switched on, the output has two parts:

$$
y[n] = y_{tr}[n] + y_{ss}[n].
$$

The **transient** $y_{tr}[n]$ is the system's temporary reaction right after the input starts. The **steady-state response** $y_{ss}[n]$ is what remains once the transient has died out. For a **stable** system $y_{tr}[n] \to 0$ as $n \to \infty$, so eventually $y[n] \approx y_{ss}[n]$.

### 6a. Worked example (note p.18): $h[n] = \{4, -5, 6, -3\}$ with a unit-step input

The system is $y[n] = 4x[n] - 5x[n-1] + 6x[n-2] - 3x[n-3]$. With $x[n] = u[n]$, every input from $n = 0$ on is 1, so the output just accumulates the taps:

$$
\begin{aligned}
y[0] &= 4, \\
y[1] &= 4 - 5 = -1, \\
y[2] &= 4 - 5 + 6 = 5, \\
y[3] &= 4 - 5 + 6 - 3 = 2, \\
y[n] &= 2 \quad\text{for every } n \ge 3.
\end{aligned}
$$

The steady-state value is $2 = \sum_n h[n] = H(e^{j0})$. That makes sense: a step is a "zero-frequency" input, so in steady state it is simply multiplied by the gain at $\omega = 0$. The first three outputs, $\{4, -1, 5\}$, are the **transient**. In general an FIR filter of length $L$ has a transient lasting $L - 1$ samples.

---

## 7. Response to a causal exponential

*Syllabus 4.8.6. A derivation.*

This is the precise version of Section 6: what exactly does the transient look like when $e^{j\omega n}$ is switched on at $n = 0$?

**In the exam, write:**

Let the input be $x[n] = e^{j\omega n}u[n]$ and let the system be causal, so $h[k] = 0$ for $k < 0$. Then

$$
y[n] = \sum_{k=0}^{\infty} h[k]\,e^{j\omega(n-k)}\,u[n-k].
$$

Since $u[n-k] = 0$ for $k > n$, only $0 \le k \le n$ contributes:

$$
y[n] = e^{j\omega n}\sum_{k=0}^{n} h[k]\,e^{-j\omega k}.
$$

This is **not** $H(e^{j\omega})$ yet, because the sum stops at $n$ instead of $\infty$. Write it as "the whole infinite sum minus its tail":

$$
\begin{aligned}
y[n] &= e^{j\omega n}\left(\sum_{k=0}^{\infty} h[k]\,e^{-j\omega k} - \sum_{k=n+1}^{\infty} h[k]\,e^{-j\omega k}\right) \\[6pt]
&= \underbrace{H(e^{j\omega})\,e^{j\omega n}}_{y_{ss}[n]}\;\underbrace{-\;e^{j\omega n}\sum_{k=n+1}^{\infty} h[k]\,e^{-j\omega k}}_{y_{tr}[n]}.
\end{aligned}
$$

The size of the transient is bounded by the tail of the impulse response:

$$
|y_{tr}[n]| \le \sum_{k=n+1}^{\infty} |h[k]|.
$$

If the system is stable, $h[n]$ is absolutely summable, so this tail goes to 0 as $n \to \infty$ and $y[n] \to y_{ss}[n]$. For an FIR filter whose $h[n]$ is nonzero only for $0 \le n \le N$, the tail is empty once $n \ge N$, so the transient is exactly zero after $N$ samples.

---

## 8. The concept of filtering

*Syllabus 4.8.7.*

Think of an LTI system as a row of volume knobs, one per frequency. $|H(e^{j\omega})|$ is the setting of the knob at $\omega$:

- $|H| \approx 1$: that frequency passes unchanged.
- $|H| < 1$: it is attenuated, and $|H| \approx 0$ removes it.
- $|H| > 1$: it is amplified.

The range of frequencies a filter lets through is its **passband**; the range it suppresses is its **stopband**.

| Type | Lets through | Shape of $\lvert H\rvert$ on $0 \le \omega \le \pi$ |
|---|---|---|
| Low-pass (e.g. moving average) | small $\lvert\omega\rvert$ | high at $0$, low at $\pi$ |
| High-pass | large $\lvert\omega\rvert$ | near zero at $0$, high at $\pi$ |
| Band-pass | a middle band | a bump in the middle |
| Band-stop (notch) | low and high | a dip in the middle |

A quick way to classify any filter is to compute the two ends: $H(e^{j0}) = \sum_n h[n]$ and $H(e^{j\pi}) = \sum_n (-1)^n h[n]$. Large at $0$ and small at $\pi$ means low-pass; the reverse means high-pass.

**The ideal low-pass filter** has

$$
|H(e^{j\omega})| = \begin{cases} 1, & 0 \le |\omega| \le \omega_c, \\ 0, & \omega_c < |\omega| \le \pi. \end{cases}
$$

Feed it $x[n] = A\cos\omega_1 n + B\cos\omega_2 n$ with $\omega_1 < \omega_c < \omega_2$, and only the low-frequency term survives:

$$
y[n] = A\,|H(e^{j\omega_1})|\cos\big(\omega_1 n + \theta(\omega_1)\big).
$$

**Why can't an ideal filter be built?** (past paper 2d) Its impulse response is

$$
h_{LP}[n] = \frac{\sin\omega_c n}{\pi n}, \qquad -\infty < n < \infty,
$$

which is infinitely long and nonzero for $n < 0$. It is non-causal and has no finite realisation, so in practice it can only be approximated.

### 8a. Design example (note p.20): block $\omega = 0.1$, pass $\omega = 0.4$

We want a 3-tap filter that completely removes the component at $0.1$ rad/sample and passes the one at $0.4$ rad/sample unchanged. Use a symmetric impulse response, $h[0] = h[2] = \alpha_0$ and $h[1] = \alpha_1$, because symmetry gives linear phase:

$$
H(e^{j\omega}) = \alpha_0 + \alpha_1e^{-j\omega} + \alpha_0e^{-j2\omega} = e^{-j\omega}\big(\alpha_1 + 2\alpha_0\cos\omega\big).
$$

So $|H(e^{j\omega})| = |\alpha_1 + 2\alpha_0\cos\omega|$ and $\theta(\omega) = -\omega$. The two requirements give two equations:

$$
\begin{aligned}
2\alpha_0\cos(0.1) + \alpha_1 &= 0 &&\text{(i) remove } 0.1, \\
2\alpha_0\cos(0.4) + \alpha_1 &= 1 &&\text{(ii) pass } 0.4.
\end{aligned}
$$

Subtracting (i) from (ii) eliminates $\alpha_1$:

$$
\alpha_0 = \frac{1}{2\big(\cos 0.4 - \cos 0.1\big)} = -6.762,
\qquad
\alpha_1 = -2\alpha_0\cos(0.1) = 13.456.
$$

$$
\boxed{y[n] = -6.762\,x[n] + 13.456\,x[n-1] - 6.762\,x[n-2]}
$$

Check: $|H(e^{j0.1})| = 0$ and $|H(e^{j0.4})| = 1.000$. It blocks the lower frequency and passes the higher one, so this is a high-pass filter.

### 8b. Mitra 4.60: which frequencies appear at the output? (input $x[n] = \cos\omega_0 n$)

Products of cosines create **new** frequencies. An LTI system can never do that, so none of these systems is LTI.

| System | Expanded | Frequencies in $y[n]$ |
|---|---|---|
| $y[n] = \cos(\pi n/5)\,x[n]$ | $\tfrac12\big[\cos\big((\omega_0 - \tfrac{\pi}{5})n\big) + \cos\big((\omega_0 + \tfrac{\pi}{5})n\big)\big]$ | $\omega_0 \pm \pi/5$ |
| $y[n] = x^4[n]$ | $\cos^4\omega_0 n = \tfrac38 + \tfrac12\cos 2\omega_0 n + \tfrac18\cos 4\omega_0 n$ | $0,\ 2\omega_0,\ 4\omega_0$ |
| $y[n] = x[4n]$ | $\cos(4\omega_0 n)$ | $4\omega_0$ |

---

## 9. Ten-minute self-test

Cover the right-hand column and answer out loud.

| # | Question | Answer |
|---|---|---|
| 1 | Why is $e^{j\omega n}$ an eigenfunction of an LTI system? | $y[n] = H(e^{j\omega})\,e^{j\omega n}$, and $H$ does not depend on $n$ |
| 2 | Is $z^n u[n]$ an eigenfunction? | No: the sum depends on $n$ through $u[n-k]$ |
| 3 | Symmetry of $\lvert H\rvert$ and $\theta$ for real $h[n]$ | $\lvert H\rvert$ is even, $\theta$ is odd |
| 4 | $A\cos(\omega_0 n + \phi)$ through $H$ gives? | $A\lvert H(e^{j\omega_0})\rvert\cos(\omega_0 n + \phi + \theta(\omega_0))$ |
| 5 | $H(e^{j\pi/4})$ for $h[n] = (0.4)^n u[n]$ | $1.2067 - 0.4759j$, i.e. $1.297\angle{-21.5^\circ}$ |
| 6 | $M$-point moving-average $H(e^{j\omega})$ | $\frac{1}{M}\frac{\sin(M\omega/2)}{\sin(\omega/2)}e^{-j(M-1)\omega/2}$ |
| 7 | Zeros of the 5-point moving average | $\omega = 2\pi/5$ and $4\pi/5$ |
| 8 | Step response of $h = \{4, -5, 6, -3\}$ | $4, -1, 5$, then $2$ forever ($= \sum h$) |
| 9 | $y_{tr}[n]$ for a causal exponential input | $-e^{j\omega n}\sum_{k=n+1}^{\infty} h[k]e^{-j\omega k}$ |
| 10 | All-pass condition in 4.64 | $\alpha = -\beta$, with $\lvert\beta\rvert < 1$ |
| 11 | The $k$ that makes 4.63 real | $k = 2$ |
| 12 | Why can't an ideal low-pass filter be built? | $h[n] = \sin(\omega_c n)/(\pi n)$ is infinitely long and non-causal |

*Every number in this file was checked with `python DSP/study/_mid2_verify.py`.*
