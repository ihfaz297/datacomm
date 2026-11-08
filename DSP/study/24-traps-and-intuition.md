# Traps, Tricks and the Intuition That Saves You

*Read this after the tutorials (files 20–23), and once more on Sunday morning.*

Each entry has up to four parts: **the mistake** people make under pressure, **the picture**, which is an intuition you can rebuild in the exam hall, **the twist**, which is how sir can change the same question, and a **quick check** that takes five seconds.

Sir's habit is to take a textbook example and change **one** thing: where the arrow is, the sign of $a$, the ROC, "for all $n$" versus "$u[n]$", or the method he demands. Before you start writing, circle whatever is different from the book.

All the new numbers here were checked with numpy (long division, the three-ROC inverse, the one-sided z-transform, the powers).

---

## A. Convolution and sequences (where TT1 hurt)

### A1. Where is $n = 0$? (the arrow)

**The mistake.** Treating the first number as $n = 0$ when the arrow is somewhere else.

**The picture.** The arrow is a "you are here" pin. Everything to its left is negative time.

**The rule.** The output starts at (start of $x$) + (start of $h$). In TT1, $x$ starts at $0$ and $h$ at $-1$, so $y$ starts at $-1$. The answer $\{1, 4, 8, \ldots\}$ therefore has its arrow on the $4$, not on the $1$.

**The twist.** The same numbers with the arrow moved only shift the answer. The values do not change, so recompute just the start index.

**Quick check.** The length is $N_1 + N_2 - 1$, and $\sum y = \sum x \cdot \sum h$.

### A2. $x(-n + 2)$: fold first, or shift first?

**The mistake.** Shifting the wrong way (TT1 Q1 ii).

**The picture.** Forget about "operations". Ask where each sample lands. Set the argument equal to $k$: $-n + 2 = k$, so $n = 2 - k$. The sample $x(k)$ moves to position $2 - k$. So $x(0)$ lands at $n = 2$, $x(1)$ at $n = 1$, and $x(-1)$ at $n = 3$.

In the language of operations: $x(-n + 2) = x\big(-(n - 2)\big)$, so fold first, then shift the folded signal **right** by 2.

**Quick check.** Plug in one sample: the value of $x(0)$ must end up at $n = 2$.

### A3. Infinite convolution: getting the limits right

**The mistake.** Writing $\sum_{k=-\infty}^{\infty}$ and getting stuck, or forgetting to say that $y = 0$ for $n < 0$.

**The picture.** $u(k)$ is a gate that opens at $k = 0$, and $u(n-k)$ is a gate that closes at $k = n$. You only add while both gates are open: $0 \le k \le n$. If $n < 0$ the window is empty, so $y(n) = 0$.

**The twist.** Take $h(n) = a^n u(n-2)$. The gate now opens at $k = 2$, so the sum runs over $2 \le k \le n$, and $y(n) = 0$ for $n < 2$.

---

## B. Topic 1: frequency response (Q1)

### B1. "Steady state" when there is no transient

**The mistake.** Writing a transient for $x[n] = A\cos(\omega_0 n)$, $-\infty < n < \infty$.

**The picture.** A transient is the system's surprise at the moment the input is switched on. If the input has been running forever (no $u[n]$), there is no switch-on moment and no surprise, so $y[n] = y_{ss}[n]$ exactly. With $u[n]$ there is a transient, and it dies away only if the system is stable.

**The twist (final 5c).** "$x[n] = A\cos(\omega_0 n)$, $-\infty < n < \infty$." Answer $y[n] = A\,|H(e^{j\omega_0})|\cos\big(\omega_0 n + \theta(\omega_0)\big)$ and stop there.

### B2. $\tan^{-1}$ lies about the quadrant

**The mistake.** For $H = -1 - j$, writing $\tan^{-1}(1) = 45^\circ$. The angle is actually $-135^\circ$.

**The picture.** Draw the point. A negative real part and a negative imaginary part put it in the bottom-left quadrant, so you must add or subtract $180^\circ$.

**The rule.** If $H_R < 0$, then $\theta = \tan^{-1}(H_I/H_R) \pm 180^\circ$.

**Quick check.** From Section 3a of the T1 file, $H(e^{j\pi/4}) = -1.586 - 2.071j$ has $\theta = -127.4^\circ$, not $+52.6^\circ$.

### B3. A sine went in, so a sine comes out

**The mistake.** Writing cos in the answer when the input was $\sin(\omega_0 n)$ (Mitra 4.68).

**The picture.** The system can only scale and delay, so it **cannot turn a sine into a cosine**. Whatever wave goes in comes out: $y[n] = |H|\sin(\omega_0 n + \theta)$. If the input carries its own phase $\phi$, keep it: $A\cos(\omega_0 n + \phi + \theta)$.

### B4. Moving average with an even $M$

**The mistake.** Saying the delay is $M/2$, or ignoring the even-$M$ case.

**The picture.** The output of a moving average is the average of a window, so it "belongs" to the centre of that window. The window covers $n, n-1, \ldots, n-(M-1)$, whose centre is $(M-1)/2$ samples back. For $M = 4$ the delay is $1.5$ samples. A half-sample delay is perfectly fine on paper.

**Quick check.** The zeros of $|H|$ are at $\omega = 2\pi k/M$. For $M = 4$ they are at $\pi/2$ and $\pi$, so an even-$M$ filter removes $\omega = \pi$ exactly.

### B5. Why the moving-average phase jumps

**The mistake.** Drawing the straight line $-(M-1)\omega/2$ all the way across.

**The picture.** $H(e^{j\omega})$ is a real function $R(\omega)$ times $e^{-j(M-1)\omega/2}$. When $R$ turns negative after a zero, "negative" means "multiplied by $e^{j\pi}$", so the phase gains $\pi$. It is not a mistake; it is just bookkeeping for the sign.

**Write:** $\theta(\omega) = -\dfrac{(M-1)\omega}{2} + \pi\times(\text{number of zeros below } \omega)$.

### B6. If a system creates new frequencies, it is not LTI

**The picture.** An LTI system is a set of volume knobs, one per frequency. The knobs can turn a frequency up, down or off, but they **can never add one**. Squaring, multiplying by a cosine and down-sampling ($x[4n]$) all add frequencies, so none of them is LTI (Mitra 4.60).

**The twist.** "Is $y[n] = x^2[n]$ characterised by a frequency response?" No. It is not LTI, so $H(e^{j\omega})$ has no meaning for it.

### B7. A frequency above $\pi$ is a lower frequency in disguise

**The mistake.** Treating $\cos(1.5\pi n)$ as a high-frequency signal.

**The picture.** A discrete-time frequency lives on a circle. $1.5\pi$ lands on the same spot as $1.5\pi - 2\pi = -0.5\pi$, so $\cos(1.5\pi n) = \cos(0.5\pi n)$.

**Quick check.** Always reduce $\omega$ into $(-\pi, \pi]$ before reading off $|H|$. The highest discrete-time frequency is $\pi$, which is $(-1)^n$.

### B8. The eigenfunction trick (4.54)

$z^n$ for all $n$ is an eigenfunction. $z^n u[n]$ is **not**: switching on at $n = 0$ adds a transient, so the output is not exactly $H$ times the input. It is the same idea as B1.

---

## C. Topic 2: the z-transform (Q2)

### C1. Which side the ROC is on, in one sentence

**The picture.** $z^{-n}$ with a large $|z|$ crushes the right-hand side ($n \to +\infty$) and blows up the left-hand side. So **the right-sided part needs $|z|$ large (outside a circle) and the left-sided part needs $|z|$ small (inside a circle)**. A two-sided signal needs both, which gives a ring.

**Quick check.** The ROC is bounded by poles and never contains one.

### C2. $H(z)$ given without an ROC: three different answers

$$
H(z) = \frac{1}{(1 - 0.5z^{-1})(1 - 2z^{-1})} = \frac{-1/3}{1 - 0.5z^{-1}} + \frac{4/3}{1 - 2z^{-1}}
$$

| ROC | $h[n]$ | Causal? | Stable? |
|---|---|---|---|
| $\lvert z\rvert > 2$ | $-\frac13(0.5)^n u[n] + \frac43\,2^n u[n]$ | yes | **no** ($2^n$ blows up) |
| $0.5 < \lvert z\rvert < 2$ | $-\frac13(0.5)^n u[n] - \frac43\,2^n u[-n-1]$ | no | **yes** (contains $\lvert z\rvert = 1$) |
| $\lvert z\rvert < 0.5$ | $\frac13(0.5)^n u[-n-1] - \frac43\,2^n u[-n-1]$ | anti-causal | no |

Check: summing the ring version at $z = 1$ gives $H(1) = -2$.

**If he asks for "the $h[n]$ that makes the system stable",** pick the ROC that contains the unit circle, which is the ring. If he says "causal", take the region outside the largest pole. If he gives neither an ROC nor a condition, list all three; he will love it.

**The rule for each term:** if the ROC lies outside the pole $p$ ($|z| > |p|$), that term gives $p^n u[n]$; if the ROC lies inside it ($|z| < |p|$), the term gives $-p^n u[-n-1]$.

### C3. Partial fractions: divide by $z$ first

**The mistake.** Doing partial fractions on $X(z)$ directly and ending up with a stray constant or the wrong shape.

**The picture.** The table entry is $\dfrac{z}{z - p} \leftrightarrow p^n u[n]$. Dividing by $z$ first guarantees that every term comes back in the form $\dfrac{z}{z-p}$ when you multiply by $z$ again.

**The improper case.** If the numerator's degree (in powers of $z^{-1}$) is at least the denominator's, divide the polynomials first; the quotient gives $\delta$ terms. The $X(z)/z$ trick handles the "equal degree" case automatically.

### C4. Repeated poles: don't drop a term

A double pole at $p$ needs **two** terms, $\dfrac{B}{z - p} + \dfrac{C}{(z - p)^2}$. The second one becomes $n\,p^n u[n]$, through the pair $n a^n u[n] \leftrightarrow \dfrac{az^{-1}}{(1 - az^{-1})^2}$; watch out for the extra factor of $a$.

**Quick check.** For a causal signal, $x[0] = \lim_{z\to\infty} X(z)$ (the initial value theorem). In Section 8c of the T2 file, $X(\infty) = 1$, and indeed $\frac49 + \frac59 + 0 = 1$.

### C5. The sign inside $(1 + 2z^{-1})$

$$
\frac{1}{1 + 2z^{-1}} = \frac{1}{1 - (-2)z^{-1}} \;\longleftrightarrow\; (-2)^n u[n].
$$

The pole is at $z = -2$. Your note slipped at exactly this point.

**Quick check.** Find the pole by setting the bracket to zero: $1 + 2z^{-1} = 0$ gives $z = -2$.

### C6. Shifted and flipped versions sir can swap in

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $a^n u[n-1]$ | $\dfrac{az^{-1}}{1 - az^{-1}}$ | $\lvert z\rvert > \lvert a\rvert$ |
| $a^{n-1}u[n-1]$ | $\dfrac{z^{-1}}{1 - az^{-1}}$ | $\lvert z\rvert > \lvert a\rvert$ |
| $u[-n]$ | $\dfrac{1}{1 - z}$ | $\lvert z\rvert < 1$ |
| $a^{\lvert n\rvert}$ with $\lvert a\rvert < 1$ | $\dfrac{1}{1 - az^{-1}} + \dfrac{az}{1 - az}$ | $\lvert a\rvert < \lvert z\rvert < 1/\lvert a\rvert$ |
| $(n+1)\,a^n u[n]$ | $\dfrac{1}{(1 - az^{-1})^2}$ | $\lvert z\rvert > \lvert a\rvert$ |

**The method for any of these:** write it as a known pair, then apply a shift (multiply by $z^{-k}$), scaling ($a^n$ replaces $z$ by $z/a$), or reversal ($z \to 1/z$, which flips the ROC).

### C7. The inverse by long division (Proakis Ex 3.4.x)

$$
X(z) = \frac{1}{1 - 1.5z^{-1} + 0.5z^{-2}}
$$

**With ROC $|z| > 1$ (causal),** divide in **ascending powers of $z^{-1}$**:

$$
X(z) = 1 + 1.5z^{-1} + 1.75z^{-2} + 1.875z^{-3} + \cdots
\quad\Longrightarrow\quad
x[n] = \{\underset{\uparrow}{1}, 1.5, 1.75, 1.875, 1.9375, \ldots\}.
$$

**With ROC $|z| < 0.5$ (anti-causal),** write the denominator in ascending powers of $z$, as $0.5z^{-2} - 1.5z^{-1} + 1$, and divide:

$$
X(z) = 2z^2 + 6z^3 + 14z^4 + 30z^5 + \cdots
\quad\Longrightarrow\quad
x[n] = \{\ldots, 30, 14, 6, 2, 0, \underset{\uparrow}{0}\}.
$$

**The picture.** Causal means the series must run towards $z^{-1}$ (future samples); anti-causal means it must run towards $z$ (past samples). The ROC tells you which way to divide.

Long division gives numbers, not a closed form. Use it when he says "the first few samples", or when the poles are ugly.

**Quick check.** The closed form for the causal case is $x[n] = 2 - (0.5)^n$, which gives $1, 1.5, 1.75$.

### C8. A difference equation with initial conditions (one-sided z-transform, Proakis 3.6)

**The mistake.** Using the two-sided shift $z^{-1}Y(z)$ when $y(-1) \ne 0$.

**The rule (one-sided z-transform).**

$$
\mathcal{Z}^+\{y(n-1)\} = z^{-1}Y^+(z) + y(-1),
\qquad
\mathcal{Z}^+\{y(n-2)\} = z^{-2}Y^+(z) + z^{-1}y(-1) + y(-2).
$$

**Example.** $y(n) = 0.5\,y(n-1) + x(n)$ with $x(n) = u(n)$ and $y(-1) = 1$.

$$
\begin{aligned}
Y &= 0.5\big[z^{-1}Y + 1\big] + \frac{1}{1 - z^{-1}}
\quad\Longrightarrow\quad
Y\big(1 - 0.5z^{-1}\big) = 0.5 + \frac{1}{1 - z^{-1}}, \\[6pt]
Y &= \frac{0.5}{1 - 0.5z^{-1}} + \frac{1}{(1 - 0.5z^{-1})(1 - z^{-1})}
   = \frac{0.5}{1 - 0.5z^{-1}} + \frac{2}{1 - z^{-1}} - \frac{1}{1 - 0.5z^{-1}}.
\end{aligned}
$$

$$
\boxed{y(n) = 2 - (0.5)^{n+1}, \qquad n \ge 0}
$$

The poles of $Y^+(z)$ are at $0.5$ and $1$, and a one-sided transform is always right-sided, so ROC: $|z| > 1$.

**Quick check.** By recursion, $y(0) = 0.5\cdot 1 + 1 = 1.5$ and $y(1) = 0.5\cdot 1.5 + 1 = 1.75$. The formula gives $1.5$ and $1.75$.

**The picture.** The initial condition is energy already stored in the system. It shows up as an extra term that decays away (the zero-input response); the rest is the zero-state response.

### C9. Stability and causality are separate questions

Causal means the ROC is outside the outermost pole (and includes $\infty$). Stable means the ROC contains $|z| = 1$. "Poles inside the unit circle means stable" is true **only for causal systems**, so say "causal and stable if and only if all poles are inside the unit circle".

### C10. Counting poles and zeros at the origin

Convert to positive powers of $z$ before you count. $\dfrac{1}{1 - az^{-1}} = \dfrac{z}{z - a}$ has a **zero at $z = 0$**, and people forget to draw it. In final 6b, the $(M-1)$-fold pole at the origin carries the marks, so label it "$(M-1)$".

---

## D. Topic 3: frequency analysis (Q3)

### D1. Is a discrete-time sinusoid periodic?

**The mistake.** "Cosine is periodic, so of course it is."

**The picture.** A discrete-time sinusoid repeats only if, after $N$ steps, it has turned through a whole number of full circles: $\omega_0 N = 2\pi k$. That means $f_0 = \omega_0/2\pi = k/N$ **must be rational**.

- $\cos(\pi n/3)$: $f_0 = 1/6$, so $N = 6$.
- $\cos(\sqrt2\,\pi n)$: $f_0 = 1/\sqrt2$ is irrational, so it is **not periodic**.
- $\cos(n/6)$: $f_0 = 1/(12\pi)$ is irrational, so it is **not periodic**, even though $\cos(t/6)$ in continuous time is. A favourite trick.
- $\cos(\pi n/3) + \cos(\pi n/4)$: $N_1 = 6$ and $N_2 = 8$, so $N = \operatorname{lcm}(6, 8) = 24$.
- Final 1d, $\sin(5\pi n)$ and $\sqrt3\cos(5\pi n)$: $f_0 = 5/2$ gives $N = 2$ for both, so the common period is $2$.

### D2. Energy signal or power signal?

| $x[n]$ | Energy | Power | Type |
|---|---|---|---|
| $a^n u[n]$, $\lvert a\rvert < 1$ | $\frac{1}{1 - a^2}$ ($= 1.333$ for $a = 0.5$) | $0$ | energy |
| $u[n]$ | $\infty$ | $\frac12$ (not 1) | power |
| $(-1)^n$; $A\cos(\omega_0 n)$ | $\infty$ | $1$; $\frac{A^2}{2}$ | power |
| $n\,u[n]$ | $\infty$ | $\infty$ | neither |

**The picture.** Power is an average over a window from $-N$ to $N$. $u[n]$ is "on" for only half of that window, so $P = \frac12$.

**Quick check.** Finite energy means zero power. Finite, nonzero power means infinite energy.

### D3. Where the $2\pi$ goes in Parseval

- Discrete time, aperiodic: $\displaystyle\sum_n |x[n]|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi}|X(\omega)|^2\,d\omega$.
- Discrete time, periodic: $\displaystyle\frac{1}{N}\sum_{n=0}^{N-1}|x[n]|^2 = \sum_{k=0}^{N-1}|c_k|^2$, with no $2\pi$.
- Continuous time in hertz: $\displaystyle\int|x(t)|^2\,dt = \int|X(F)|^2\,dF$, with no $2\pi$. In $\Omega$ it becomes $\frac{1}{2\pi}\int|X(\Omega)|^2\,d\Omega$.

**The picture.** A $2\pi$ appears whenever the frequency variable is in radians, because one full turn costs $2\pi$ radians. In hertz it does not.

### D4. How many coefficients: CTFS versus DTFS

The CTFS has infinitely many $c_k$ ($k$ from $-\infty$ to $\infty$). The DTFS has only $N$ distinct ones ($k = 0, \ldots, N-1$), because $c_{k+N} = c_k$.

**The picture.** A discrete-time signal cannot wiggle faster than $(-1)^n$, so only $N$ different "speeds" are available.

**The twist.** "Find $c_7$ for $N = 6$." Since $c_7 = c_1$, just give $c_1$.

### D5. A DTFT that does not exist

$2^n u[n]$ (it grows) and $u[n]$ (its pole is **on** the unit circle) have no ordinary DTFT. **The reason to write:** they are not absolutely summable; equivalently, the ROC does not include $|z| = 1$. Their z-transforms do exist. Use this sentence whenever he asks you to "use the frequency domain" on a growing signal.

### D6. Square-wave variants

- The $\pm 1$ even square wave: $c_0 = 0$ and $c_k = \frac{2}{k\pi}\sin\frac{k\pi}{2}$.
- The $0/1$ square wave with the same timing equals $\frac12(\text{the } \pm 1 \text{ version} + 1)$, so $c_0 = \frac12$ and $c_k = \frac{1}{k\pi}\sin\frac{k\pi}{2}$.
- Shifted by $T_0/4$ (odd symmetry instead of even): the magnitudes stay the same and only the phases change. That is the time-shift property from Section 7 of the T3 file.

**The picture.** Shifting in time never changes *how much* of each harmonic there is, only *when* it peaks.

### D7. A wider pulse has a narrower spectrum

A rect of width $\tau$ has its first zero at $F = 1/\tau$. Double $\tau$ and the spectrum halves in width while its peak height $A\tau$ doubles. If he asks "what happens to the spectrum if the pulse gets wider?", that is the answer, with this picture: long in time means narrow in frequency.

---

## E. Exam-hall habits (each one has cost someone marks)

1. **Write the formula before the numbers.** The formula line alone is often worth a mark.
2. **Box the final answer together with its conditions:** $n \ge 0$, the ROC, $|a| < 1$.
3. **Read the verb.** *Determine* means show the working. *Sketch* means draw it. *Using the z-transform* means that method only. *Explain* means words, one formula and one picture.
4. **Every z-transform answer carries an ROC. Every DTFT answer checks that the DTFT exists.**
5. **If you are stuck, write the definition, then the general formula, then the first step with his numbers.** A partial method beats a blank page.
6. **Time.** 40 minutes for 15 marks is about 2.7 minutes per mark, so each 5-mark topic gets about 13 minutes. If you run over, write the method in words and move on.
