# Tutorial 10 — DTFT and the frequency response of an LTI system

TT2 topic 1 (Mitra 4.8.x). Pairs with the drill `DSP/practice/step10_dtft.py`.
Work each example on paper first, then run the drill and let it tell you if you were right.

---

## §1 The DTFT in one line, and why w instead of f

```text
X(e^jw) = sum over ALL n of  x[n] * exp(-j w n)          w in radians/sample
```

Two things beginners trip on:

- **w is radians per sample, not Hz.** w = 2πf/Fs. Since the sampling rate is already baked into the
  sequence, "frequency" here only runs from 0 to π (0 to π means 0 to Fs/2 in Hz). Everything above π
  repeats: **X(e^jw) is periodic with period 2π**, so a plot from 0 to π is the whole story.
- **The sum runs over negative n too.** For a causal sequence (nothing before n = 0) it starts at n = 0,
  which is why the geometric-series tricks below work.

**The mental model:** the DTFT is a set of filters, one per w. For each w you ask "how much of a
cosine at this w is inside x[n]?" That is exactly what `exp(-j w n)` measures. So a plot of |X(e^jw)|
tells you which frequencies live in your signal and how strongly.

```python
import numpy as np
import matplotlib.pyplot as plt
w = np.linspace(0, np.pi, 1001)          # 0..pi is enough
x = np.array([1, 2, 3.0])                # sequence on n = 0, 1, 2
n = np.arange(len(x))
X = np.exp(-1j*np.outer(w, n)) @ x       # <- the one-liner that is the whole definition
plt.plot(w/np.pi, np.abs(X)); plt.xlabel("w / pi"); plt.show()
```

That single line `exp(-1j*outer(w, n)) @ x` is the DTFT, evaluated at every w at once. Use it whenever
you are not asked to show algebra.

---

## §2 Worked example 1 — DTFT of a three-sample sequence, by hand

**Question.** Find X(e^jw) for x[n] = {1, 2, 3} and evaluate |X| at w = 0, π/2, π.

**Step 1 — write the definition with the actual samples.** Only n = 0, 1, 2 contribute:

```text
X(e^jw) = 1*e^(-j0) + 2*e^(-jw) + 3*e^(-j2w)  =  1 + 2e^(-jw) + 3e^(-j2w)
```

That *is* the answer; a DTFT of a finite sequence is just a polynomial in e^{−jw}. Nothing to simplify.

**Step 2 — substitute the w values and use e^{−jπ/2} = −j, e^{−jπ} = −1:**

| w | 1 + 2e^{−jw} + 3e^{−j2w} | X | \|X\| | ∠X |
|---|---|---|---|
| 0 | 1 + 2 + 3 | 6 | 6 | 0° |
| π/2 | 1 + 2(−j) + 3(−1) = −2 − 2j | −2 − 2j | 2.828 | −135° |
| π | 1 − 2 + 3 | 2 | 2 | 0° |

Machine-checked: X = {6, −2−2j, 2}, \|X\| = {6, 2.828, 2}. The magnitude peaks at DC and dips at π because
the sequence {1,2,3} is a slow (lowpass-ish) shape — that is how you sanity-check a DTFT answer with no
extra work.

---

## §3 The two sums that unlock every DTFT question in this course

**(a) Infinite causal geometric series.** For |α| < 1,

```text
sum_{n=0}^{inf} (a e^(-jw))^n  =  1 / (1 - a e^(-jw))          -> 1/(1 - a e^(-jw))
```

This is the causal exponential pair, and it is the single most examined formula in topic 1.

**(b) Finite geometric series.** For any α,

```text
sum_{n=0}^{M-1} (a e^(-jw))^n  =  (1 - a^M e^(-jwM)) / (1 - a e^(-jw))
```

Same formula, the series just stops at M − 1. The numerator is where the "ripples" in a finite-length
response come from.

**Magnitude formula you should derive once and then memorise:**

```text
|1 - a e^(-jw)|^2 = (1 - a cos w)^2 + (a sin w)^2 = 1 - 2a cos w + a^2
=>  |X(e^jw)| = 1 / sqrt(1 - 2 a cos w + a^2)
```

Verified against the direct sum: max error 0.0 in `step10_dtft.py` (`|X| vs 1/sqrt(1-2a cos w + a^2)`).

---

## §4 Worked example 2 — the causal exponential (a real final-paper question)

**Question (2021-22 final, Q2c).** Determine the DTFT X(e^jw) of x[n] = αⁿu[n], |α| < 1.

**Step 1 — write the sum and substitute.**

```text
X(e^jw) = sum_{n=0}^{inf} a^n e^(-jwn) = sum_{n=0}^{inf} (a e^(-jw))^n
```

**Step 2 — geometric series with ratio r = αe^{−jw}.** Its magnitude is |α| < 1, so the series converges
for every w (that is why the question gives |α| < 1):

```text
X(e^jw) = 1 / (1 - a e^(-jw))                <- the answer, one line
```

**Step 3 — magnitude, if asked.** Multiply by the conjugate:

```text
|X(e^jw)| = 1 / sqrt(1 - 2a cos w + a^2)      phase = -arctan( a sin w / (1 - a cos w) )
```

**Step 4 — numbers for α = 0.5** (the drill value; substitute and evaluate):

| w | 0 | π/4 | π/2 | π |
|---|---|---|---|---|
| X(e^jw) | 2.0000 | 1.1907 − 0.6512j | 0.8000 − 0.4000j | 0.6667 |
| \|X\| | 2.0000 | 1.3572 | 0.8944 | 0.6667 |
| ∠X | 0° | −28.7° | −26.6° | 0° |

**Step 5 — read the answer like a grader.** The magnitude is largest at DC (2.0 for α = 0.5) and falls to
0.667 at π: **the causal exponential is a lowpass signal**, and the closer α is to 1 the narrower that
lowpass becomes. Writing that sentence is the interpretation mark.

```python
a, w = 0.5, np.linspace(0, np.pi, 1001)
X = 1/(1 - a*np.exp(-1j*w))               # closed form
print(np.abs(X)[0], np.abs(X)[-1])        # 2.0  0.6667
```

---

## §5 Worked example 3 — finite length (the other final-paper DTFT question)

**Question (2021-22 final, Q2e).** Find Y(e^jw) for y[n] = αⁿ, 0 ≤ n ≤ M−1, and y[n] = 0 otherwise.

**Step 1 — the same geometric series, stopped at M − 1.** Use sum (b) from §3:

```text
Y(e^jw) = (1 - a^M e^(-jwM)) / (1 - a e^(-jw))
```

**Step 2 — say what the two factors are.** The denominator is the *infinite* causal exponential of §4; the
numerator (1 − α^M e^{−jwM}) is the "it stops at M − 1" correction. So the answer is §4's answer times
(1 − α^M e^{−jwM}). If the question hands you the time-shift theorem g[n − n₀] ↔ e^{−jwn₀}G(e^jw) as a
hint, it wants exactly that: a length-M block is the infinite sequence *minus* itself delayed by M.

**Step 3 — check a value that needs no calculator: w = 0.**

```text
Y(0) = (1 - a^M)/(1 - a) = 1 + a + a^2 + ... + a^(M-1)      <- the plain sum of the samples
```

For α = 0.5, M = 5: (1 − 0.03125)/(1 − 0.5) = 0.96875/0.5 = **1.9375**, which is exactly
1 + 0.5 + 0.25 + 0.125 + 0.0625. The drill prints 1.9375 at w = 0 and matches the direct DTFT sample by
sample.

**Step 4 — the "so what".** Because the length is finite, |Y| now has **nulls**, where α^M e^{−jwM} = 1,
i.e. w = 2πk/M (for the flat case α = 1 this is the Dirichlet kernel). Finite length → ripples and nulls.
That observation is the bridge to the window method in tutorial 13: multiplying an ideal infinite response
by a finite window is what creates the ripples.

---

## §6 Worked example 4 — the 5-point moving average, magnitude and phase

**Question (2021-22 final, Q5b).** Compute the magnitude and phase response of a 5-point moving average.

**Step 1 — write h[n] and its DTFT.** h[n] = 1/5 for n = 0…4, so

```text
H(e^jw) = (1/5) sum_{n=0}^{4} e^(-jwn) = (1/5) * (1 - e^(-j5w)) / (1 - e^(-jw))
```

**Step 2 — the standard closed form.** Factor out half-angles:
1 − e^{−j5w} = e^{−j5w/2}(e^{j5w/2} − e^{−j5w/2}) = e^{−j5w/2}·2j·sin(5w/2), so

```text
H(e^jw) = [ sin(5w/2) / (5 sin(w/2)) ] * e^(-j2w)
|H|     = | sin(5w/2) / (5 sin(w/2)) |      phase H = -2w   (+180 deg wherever the bracket is negative)
```

The general M-point version is sin(wM/2)/(M sin(w/2))·e^{−jw(M−1)/2}: **magnitude is the Dirichlet kernel,
phase is a pure delay of (M−1)/2 = 2 samples.** In the exam, write the general formula and then set M = 5
— that gets full marks.

**Step 3 — evaluate (M = 5, machine-checked):**

| w | 0 | π/5 | 2π/5 (first null) | π/2 | π |
|---|---|---|---|---|---|
| H | 1 | 0.200 − 0.616j | 0 | +0.2 | +0.2 |
| \|H\| | 1 | **0.6472** | **0** | **0.2** | 0.2 |
| ∠H | 0° | −72° | — | 0°* | 0°* |

\* the bracket changes sign after each null, flipping the phase by 180°, so the measured phase is 0 at
π/2 and π although −2w = −180° and −360°. Mention the caveat — it shows you understand the sign.

**Step 4 — the interpretation marks.** H(0) = 1 (DC passes: the average of a constant is the constant),
the first null is at **w = 2π/5 = 0.4π**, and the phase is linear → a constant delay of 2 samples. The
sidelobes are only about 13 dB down, so it is a poor lowpass filter; it is a smoother.

---

## §7 H(e^jw) of any LTI system, and "sinusoid in, sinusoid out"

**The rule.** For an LTI system with impulse response h[n],

```text
H(e^jw) = DTFT of h[n] = Y(e^jw) / X(e^jw)
```

and if x[n] = A cos(w₀n + θ) then **y[n] = A|H(e^{jw₀})| cos(w₀n + θ + ∠H(e^{jw₀}))** — same frequency,
new amplitude and phase. That is 4.8.2/4.8.3, and it is the reason frequency response exists.

**Worked question (2021-22 final, Q5c).** h[n] = {−3, 6, −5, 4}, 0 ≤ n ≤ 3, x[n] = A cos(w₀n). Write the
frequency response of the system and the output.

**Step 1 — DTFT of the four samples:**

```text
H(e^jw) = -3 + 6e^(-jw) - 5e^(-j2w) + 4e^(-j3w)
```

**Step 2 — if w₀ is given, substitute.** Take w₀ = π/2, so e^{−jw₀} = −j, e^{−j2w₀} = −1, e^{−j3w₀} = +j:

```text
H = -3 + 6(-j) - 5(-1) + 4(+j) = -3 + 5 + (-6j + 4j) = 2 - 2j
|H| = sqrt(4 + 4) = 2.828        angle H = -45 deg
y[n] = 2.828 A cos(pi n / 2 - 45 deg)
```

Machine-checked at three frequencies: w₀ = π/2 → H = 2 − 2j, \|H\| = 2.8284, ∠ = −45.00°;
w₀ = π/4 → H = −1.5858 − 2.0711j, \|H\| = 2.6085, ∠ = −127.44°; w₀ = π → H = −18, \|H\| = 18, ∠ = 180°.
The same filter attenuates at π/4 and amplifies at π, so it is not a lowpass.

**If no numeric w₀ is given**, give the general H(e^jw) plus the sentence "the output is a cosine at the
same frequency with gain |H| and phase ∠H".

---

## §8 Steady state and transient (4.8.5) — the exam question that is pure prose

A recursive system driven from n = 0 has **two** parts:

```text
y[n] = y_steady[n] + y_transient[n]
```

- **Transient** = the system's own natural response (powers of its poles, e.g. 0.5ⁿ), present only
  because the input started at a finite time. It decays to zero when all poles are inside the unit circle.
- **Steady state** = the forced response, which is §7: the same sinusoid with gain |H(e^{jw₀})| and phase
  ∠H(e^{jw₀}). It is what is left after the transient dies.

**Worked.** y(n) = 0.5y(n−1) + 2x(n) with x[n] = cos(πn/2)u[n].

```text
h[n] = 2(0.5)^n u[n]        (unit sample response; see tutorial 11 §5)
H(e^jw) = 2 / (1 - 0.5 e^(-jw))
at w0 = pi/2:  H = 2/(1 - 0.5(-j)) = 2/(1 + 0.5j) = 1.6 - 0.8j
              |H| = 1.7889 ,  angle = -26.565 deg
steady state: y_ss[n] = 1.7889 cos(pi n/2 - 26.565 deg)
transient  : c * (0.5)^n      -> dies after ~10 samples (0.5^10 = 0.001)
DC gain    : H(0) = 2/(1 - 0.5) = 4
```

All four numbers machine-checked. Note the sentence a grader wants: **"the transient vanishes as n → ∞
because the only pole, z = 0.5, is inside the unit circle; the steady-state response is a cosine of the
same frequency"**. If the pole were on or outside the unit circle the system would not settle (marginally
stable or unstable).

---

## §9 Parseval — energy without integrating in time (final Q2f)

**DT version:** Σ_{n} |x[n]|² = (1/2π) ∫_{−π}^{π} |X(e^jw)|² dw.

Example: x[n] = (0.5)ⁿu[n] → E = Σ(0.25)ⁿ = 1/(1 − 0.25) = **1.3333**. Same number from the frequency
side because the DTFT pair is exact.

**CT version asked in the final paper (Q2f).** x_a(t) = e^{−αt}u(t), α = 0.6, find the total energy using
Parseval.

```text
Step 1: X_a(jΩ) = 1 / (alpha + j Omega)          (a standard CTFT pair)
Step 2: |X_a(jΩ)|^2 = 1 / (alpha^2 + Omega^2)
Step 3: E = (1/2pi) int_{-inf}^{inf} dOmega/(alpha^2 + Omega^2)
          = (1/2pi) * (1/alpha) * [arctan(Omega/alpha)]_{-inf}^{inf}
          = (1/2pi) * (1/alpha) * pi
          = 1/(2 alpha) = 1/1.2 = 0.8333 J
Step 4: cross-check in time: E = int_0^inf e^(-2 alpha t) dt = 1/(2 alpha)  (same)
```

Verified numerically: **0.83333** from the time integral, 0.83325 from a truncated frequency grid. Quote
0.8333 J. The mark is for naming Parseval and writing the 1/2π; the integral itself is one line.

---

## §10 Traps that cost marks here

- **w in radians/sample ≠ Hz.** "First null at 0.4π" and "first null at 2π/M rad/sample" are the same
  sentence; "first null at 0.4 Hz" is wrong.
- **Forgetting e^{−jw} is complex.** Do not treat H(e^jw) as a number; keep real and imaginary parts
  until you take |·|.
- **Sign errors in e^{−jwn}.** For n = 2, e^{−j2w} = (e^{−jw})². Write e^{−jw} = c as a substitution and
  the algebra collapses.
- **Reporting |X| when the question says X.** Give the complex expression and then the magnitude; both
  lines are marked.
- **Calling the moving average a good lowpass.** Sidelobes are ~13 dB down; say "poor lowpass, good
  smoother".
- **Forgetting the periodicity.** X(e^{jw}) = X(e^{j(w+2π)}); if asked for a sketch from −π to π, mirror
  the 0…π part.

---

## §11 Practice set (answers below — cover them)

1. Find X(e^jw) for x[n] = δ[n] − δ[n−1], and |X| at w = 0 and w = π.
2. Find X(e^jw) for x[n] = (0.8)ⁿu[n]. Give |X| at w = 0 and w = π.
3. An 8-point moving average: write H(e^jw), give |H(0)| and the first null.
4. h[n] = {1, −1} for n = 0, 1. Is it lowpass or highpass? Prove it with two values.
5. x[n] = 3cos(πn/4) is applied to a 4-point moving average (h[n] = 1/4, n = 0…3). Write the steady-state
   output.
6. Find the unit sample response and the DC gain of y(n) = 0.5y(n−1) + 2x(n).
7. Energy of x[n] = (0.5)ⁿu[n], both from the time sum and by Parseval.
8. h[n] = {−3, 6, −5, 4} with x[n] = A cos(πn). Write y[n].
9. The DTFT of a length-10 flat sequence of ones: give the value at w = 0 and the first positive null.
10. Why is the DTFT of a real sequence even in magnitude and odd in phase?

**Answers.**

1. X = 1 − e^{−jw}; |X| = 2|sin(w/2)|; at w = 0 → 0, at w = π → 2. (Highpass-ish difference filter.)
2. X = 1/(1 − 0.8e^{−jw}); \|X(0)\| = 1/(1 − 0.8) = 5; \|X(π)\| = 1/(1 + 0.8) = 0.5556.
3. H = sin(w·8/2)/(8 sin(w/2))·e^{−jw·3.5} = sin(4w)/(8 sin(w/2))·e^{−j3.5w}; \|H(0)\| = 1; first null at
   w = 2π/8 = **0.25π**.
4. H = 1 − e^{−jw}. \|H(0)\| = 0 (kills DC) and \|H(π)\| = 1 − (−1) = 2 → **highpass** (a first
   difference), phase linear with delay 0.5 samples.
5. \|H(π/4)\| = \|sin(4·π/8)/(4 sin(π/8))\| = 1/(4·0.38268) = **0.6533**; ∠H = −(M−1)/2·w = −1.5·π/4 =
   **−67.5°**. So y[n] = 3·0.6533 cos(πn/4 − 67.5°) = **1.960 cos(πn/4 − 67.5°)**.
6. h[n] = 2(0.5)ⁿu[n] = {2, 1, 0.5, 0.25, …}; H(0) = 2/(1 − 0.5) = **4** (a DC amplifier).
7. Time: Σ(0.25)ⁿ = 1/(1 − 0.25) = **1.3333**; Parseval gives the same because
   (1/2π)∫dw/|1 − 0.5e^{−jw}|² = Σ|h[n]|².
8. w₀ = π → e^{−jw₀} = −1, e^{−j2w₀} = 1, e^{−j3w₀} = −1:
   H = −3 + 6(−1) − 5(1) + 4(−1) = **−18**, \|H\| = 18, ∠H = 180°, so y[n] = **−18A cos(πn)**.
9. X(e^jw) = sin(5w)/sin(w/2) (Dirichlet); at w = 0 → **10**; first null where sin(5w) = 0 → w = π/5.
10. Because x[n] real means X(e^{−jw}) = X*(e^{jw}): the real part (hence the magnitude) is even in w and
    the imaginary part (hence the phase) is odd.

Check yourself by editing the numbers into `DSP/practice/step10_dtft.py` — the checker at the bottom will
tell you PASS or FAIL with the expected value.


