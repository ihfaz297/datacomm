# Tutorial 11 — the z-transform, ROC, poles and zeros

TT2 topic 2 (Proakis Ch 3). Pairs with the drill `DSP/practice/step11_ztransform.py`.

---

## §1 The definition, and the one sentence that separates a pass from a fail

```text
X(z) = sum over all n of x[n] z^(-n)          z is COMPLEX: z = r e^(jw)
```

**A z-transform answer is not finished without its ROC.** The same X(z) belongs to two different
sequences depending on the region of convergence:

| Sequence | X(z) | ROC |
|---|---|---|
| αⁿ u[n] | 1/(1 − αz^{−1}) | \|z\| > \|α\| |
| −αⁿ u[−n−1] | 1/(1 − αz^{−1}) | \|z\| < \|α\| |

Same algebraic expression, opposite regions. Writing "1/(1 − 0.5z^{−1})" and stopping is a half-mark answer;
writing "…, ROC |z| > 0.5 (causal, right-sided)" is full marks.

**Why the ROC exists.** The sum Σ x[n]z^{−n} is a power series; it converges only for the z where |x[n]z^{−n}|
shrinks. For a right-sided (causal) sequence that is *outside* the outermost pole, for a left-sided sequence
*inside* the innermost pole, and for a two-sided sequence an **annulus** between two poles.

---

## §2 The five rules that decide any ROC

1. The ROC is an annulus (ring) centred on the origin: **r₁ < |z| < r₂**, never a circle or a disk with holes.
2. **Right-sided** (causal, starts at finite n): ROC is *outside* the outermost pole, |z| > max|pole|.
3. **Left-sided**: ROC is *inside* the innermost pole, |z| < min|pole|.
4. **Finite-length** (zero outside a finite interval): ROC is the whole plane except possibly z = 0 and/or
   z = ∞. A finite causal block → |z| > 0.
5. The ROC never contains a pole, and it is connected. For a two-sided sum of a right-sided and a left-sided
   part, the ROC is **max|left poles| < |z| < min|right poles|** — and if that interval is empty, the
   two-sided z-transform **does not exist**.

**The stability line worth memorising:** an LTI system is stable ⟺ its ROC includes the unit circle |z| = 1.
For a causal system that collapses to "all poles inside the unit circle".

---

## §3 Worked example A — the two-sided sequence (2021-22 final, Q6a, 10 marks)

**Question.** Determine the z-transform and the ROC of x(n) = αⁿu(n) + bⁿu(−n−1), and sketch the ROC.

**Step 1 — split the sum into the two halves** and treat each with §2's rules.

```text
Part 1: a^n u[n]        ->  sum_{n=0}^{inf} (a/z)^n = 1/(1 - a/z)      valid when |a/z| < 1  i.e. |z| > |a|
Part 2: b^n u[-n-1]     ->  sum_{n=-inf}^{-1} (b/z)^n
```

**Step 2 — do Part 2 properly** (this is where marks are lost). Substitute m = −n:

```text
sum_{n=-inf}^{-1} b^n z^(-n) = sum_{m=1}^{inf} b^(-m) z^m = sum_{m=1}^{inf} (z/b)^m = (z/b)/(1 - z/b)
                                                                                  = -1/(1 - b/z)
valid when |z/b| < 1  i.e. |z| < |b|
```

**Step 3 — add them.**

```text
X(z) = 1/(1 - a/z) - 1/(1 - b/z)
     = [(1 - b/z) - (1 - a/z)] / [(1 - a/z)(1 - b/z)]
     = (a - b) z^(-1) / [(1 - a z^(-1))(1 - b z^(-1))]
```

**Step 4 — state the ROC (both conditions must hold at once):**

```text
ROC:  |a| < |z| < |b|        an annulus between the two poles,  EMPTY if |b| <= |a|
```

**Step 5 — sketch it.** Draw the z-plane: circle of radius |α| (dashed, "pole"), circle of radius |b|
(dash-dot, "pole"), shade the ring between them, mark the unit circle, and write the two conditions.
For α = 0.5, b = 2 the ring is 0.5 < |z| < 2 (exactly what `step11_ztransform.py` draws).

**Step 6 — check with a number.** At α = 0.5, b = 2, z = 1.2 (inside the ring):

```text
closed form : 1/(1 - 0.5/1.2) - 1/(1 - 2/1.2) = 1.714286 + 1.5 = 3.214286
double sum  : sum over n = -400..399 of x[n] z^(-n) = 3.214286      <- identical, machine-checked
```

**The discussion mark:** because 0.5 < |z| < 2 *contains* the unit circle, this two-sided sequence is
absolutely summable in the sense that its transform converges at |z| = 1 — but note that if you were asked
for the *causal* sequence αⁿu[n] instead, the ROC would move to |z| > 0.5. Also: if |b| ≤ |α| (say α = 2,
b = 0.5) the two conditions contradict and **no z-transform exists**; the drill tests exactly that case.

---

## §4 Worked example B — finite length, poles and zeros (2021-22 final, Q6b, 10 marks)

**Question.** Determine the z-transform of x(n) = αⁿ for 0 ≤ n ≤ M−1, x(n) = 0 otherwise, and determine
the pole-zero plot.

**Step 1 — finite geometric sum.** Ratio α/z, M terms:

```text
X(z) = sum_{n=0}^{M-1} a^n z^(-n) = (1 - a^M z^(-M)) / (1 - a z^(-1))
```

**Step 2 — over a common denominator to expose the poles and zeros** (multiply top and bottom by z^M):

```text
X(z) = (z^M - a^M) / (z^(M-1) (z - a))
```

**Step 3 — zeros.** z^M = α^M → z = α e^{j2πk/M} for k = 0, 1, …, M−1: **M zeros equally spaced on a circle
of radius α.**

**Step 4 — cancel the root that is also a pole.** The k = 0 root is z = α, which is exactly the denominator
factor (z − α). **It cancels**, so

```text
zeros : z = a e^(j 2 pi k / M),  k = 1 .. M-1       (M - 1 of them)
poles : z = 0,  multiplicity M - 1                  (M - 1 of them)
ROC   : |z| > 0   (finite-length causal block -> everything except the origin)
```

**Step 5 — check it numerically.** M = 8, α = 0.5, so zeros at 0.5·e^{j2πk/8}:

| k | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| zero | 0.3536+0.3536j | 0.5j | −0.3536+0.3536j | −0.5 | −0.3536−0.3536j | −0.5j | 0.3536−0.3536j |

`np.roots` in the drill returns exactly these seven. Note the bug that was found there: `np.angle` returns
(−π, π], so comparing angles directly to 2πk/M fails for k > M/2 — wrap with `np.mod(np.angle(z), 2*np.pi)`.
Remember that if you implement it yourself.

**Step 6 — the interpretation marks.** The zeros sit on a circle of radius α, equally spaced, with the DC
zero cancelled; the origin carries an (M−1)-fold pole. As α → 1 the zeros migrate onto the unit circle and
become the DFT nulls of a rectangular pulse — the same "finite length → ripples and nulls" story as
tutorial 10 §5.

---

## §5 From a difference equation to H(z), h[n], and the frequency response

**The method.** Take the z-transform of both sides, use the time-shift property
**x[n − n₀] ↔ z^{−n₀}X(z)**, and solve for H(z) = Y(z)/X(z).

**Worked (2021-22 final, Q5a).** y(n) = 0.5y(n−1) + 2x(n). Find the unit sample response.

```text
Step 1: Y(z) = 0.5 z^(-1) Y(z) + 2 X(z)
Step 2: Y(z)[1 - 0.5 z^(-1)] = 2 X(z)
Step 3: H(z) = Y(z)/X(z) = 2 / (1 - 0.5 z^(-1))       pole z = 0.5, zero at the origin
Step 4: causal -> ROC |z| > 0.5, contains the unit circle -> STABLE
Step 5: use the pair 1/(1 - a z^(-1)) <-> a^n u[n] with a = 0.5:
        h[n] = 2 (0.5)^n u[n] = {2, 1, 0.5, 0.25, 0.125, ...}      machine-checked
Step 6: sanity checks: h[0] = 2 straight from the difference equation (y(-1) = 0), and
        h[n]/h[n-1] = 0.5 = the pole. One line each.
Step 7: frequency response = H(z) on the unit circle:
        H(e^jw) = 2/(1 - 0.5 e^(-jw)),  |H(0)| = 2/(1 - 0.5) = 4
```

**Significance of poles and zeros** (2021-22 final Q4a and Q4f — pure prose, free marks):

- **Poles** are where |H| → ∞. They set the *natural response* (each pole contributes |pole|ⁿ) and hence
  stability and ringing: all inside the unit circle → stable and decaying; on the circle → marginally stable
  (sustained oscillation, as in a digital oscillator); outside → unstable.
- **Zeros** are where |H| = 0. They decide which frequencies are *blocked*: a zero at z = 1 kills DC (that is
  why the first difference 1 − z^{−1} is a highpass), and a zero pair on the unit circle at z = e^{±jw₀}
  notches exactly that frequency.
- The *relative* positions of poles and zeros give the whole shape of |H|: peaks near poles, dips near zeros.
  That is the fastest way to sketch a frequency response in an exam.

---

## §6 SymPy does the series for you (allowed in the lab exam)

```python
import sympy as sp
a, z, n = sp.symbols("a z n"); M = sp.symbols("M", integer=True, positive=True)
sp.summation((a/z)**n, (n, 0, sp.oo))     # Piecewise((1/(1 - a/z), Abs(a/z) < 1), (Sum(...), True))
sp.summation((a/z)**n, (n, 0, M - 1))     # Piecewise((M, Eq(a/z, 1)), ((1 - (a/z)**M)/(1 - a/z), True))
sp.apart(X/z, z).doit()                   # partial fractions for the inverse transform
```

Two things SymPy hands you for free: the **ROC condition** (the `Abs(a/z) < 1` branch) and the finite-sum
formula. Paste the output into your answer — it is a valid derivation. `step11_ztransform.py` prints both,
plus the two-sided value 3.214286 at z = 1.2.

---

## §7 How the three transforms are related (final Q4b — a one-mark question)

```text
DFT          x[n] finite length N            X[k]   = sum_{n=0}^{N-1} x[n] e^(-j 2 pi k n / N)
z-transform  any x[n]                        X(z)   = sum_n x[n] z^(-n)
DTFT         any x[n] (absolutely summable)  X(e^jw) = X(z) with z = e^(jw)

=>  X[k] = X(z) evaluated at z = e^(j 2 pi k / N)
=>  the DFT is the z-transform SAMPLED at N equally spaced points ON the unit circle
=>  the DTFT is the z-transform along the whole unit circle
```

So the DFT is the "digitised" version of the DTFT (and of the z-transform on |z| = 1). That is why the DFT
is periodic with period N, mirroring the 2π periodicity of the DTFT. One relation answers "how is the
z-transform related to the DFT?", "what does the unit circle mean?" and "why is the DFT periodic?".

---

## §8 Traps

- **Omitting the ROC** — half the marks of a z-transform question.
- **Cancelling a pole but keeping it in the list.** In §4 the root at z = α is both a zero and a pole; the
  pole-zero plot must show it in neither list.
- **Sign of the left-sided term.** αⁿu[−n−1] carries a *minus* sign (the sum starts at m = 1). Losing it
  flips the ROC.
- **Confusing the ROC with the unit circle.** Poles inside the unit circle → a stable *causal* system; the
  ROC is the region *outside* those poles. "The ROC is |z| = 1" is always wrong — it is a region, not a circle.
- **Forgetting that a system's stability = the ROC covers the unit circle.** Say it in those words.

---

## §9 Practice set (answers below — cover them)

1. z-transform and ROC of x[n] = (0.8)ⁿu[n].
2. z-transform and ROC of x[n] = (0.8)ⁿu[n] − 3ⁿu[−n−1]. Evaluate at z = 1.5.
3. z-transform of δ[n − 3] and its ROC.
4. z-transform of x[n] = (0.7)ⁿ for 0 ≤ n ≤ 5, evaluated at z = 1.2, with its zeros and poles.
5. Which sequence has X(z) = 1/(1 − 0.5z^{−1}) with ROC |z| < 0.5?
6. Inverse z-transform of X(z) = 1/((1 − 0.5z^{−1})(1 − 0.25z^{−1})), ROC |z| > 0.5, by partial fractions.
7. Poles, zeros, stability and h[n] for H(z) = (1 − z^{−1})/(1 − 0.5z^{−1}), causal.
8. ROC and stability of x[n] = (1/3)ⁿu[n] + (1/2)ⁿu[−n−1].
9. Sketch |H(e^jw)| for a system with a zero at z = 1 and a pole at z = 0.8. What filter is it?
10. Why is X[k] periodic with period N?

**Answers.**

1. X(z) = 1/(1 − 0.8z^{−1}), ROC |z| > 0.8 (causal, right-sided).
2. X(z) = 1/(1 − 0.8z^{−1}) − 1/(1 − 3z^{−1}), ROC 0.8 < |z| < 3. At z = 1.5: 2.142857 + 1 = **3.142857**
   (machine-checked).
3. X(z) = z^{−3}, ROC the whole plane except z = 0 (write |z| > 0). At z = 1.5 → 0.296296.
4. X(z) = (1 − 0.7^6 z^{−6})/(1 − 0.7z^{−1}) = (z^6 − 0.7^6)/(z^5(z − 0.7)); at z = 1.2 the value is
   **2.305439**, identical to the direct six-term sum. Zeros at 0.7e^{j2πk/6} = {0.35+0.6062j, −0.35+0.6062j,
   −0.7, −0.35−0.6062j, 0.35−0.6062j}; five poles at the origin; ROC |z| > 0.
5. x[n] = −(0.5)ⁿu[−n−1] — the left-sided twin of (0.5)ⁿu[n].
6. A = 1/(1 − 0.5) = 2 for the pole 0.5 and B = 1/(1 − 2) = −1 for the pole 0.25, so
   **x[n] = (2(0.5)ⁿ − (0.25)ⁿ)u[n]**. Check: x[0] = 1, x[1] = 0.75, x[2] = 0.4375, which is exactly the
   long-division expansion of the power series.
7. Zero at z = 1, pole at z = 0.5 (stable, causal). H = (1 − z^{−1})·1/(1 − 0.5z^{−1}), so
   h[n] = (0.5)ⁿu[n] − (0.5)^{n−1}u[n−1] → **h[0] = 1 and h[n] = −(0.5)ⁿ for n ≥ 1**, i.e.
   {1, −0.5, −0.25, −0.125, …} (machine-checked). H(1) = 0 (DC blocked), H(−1) = 2/1.5 = 1.333 → **highpass**.
8. |α| = 1/3 < |b| = 1/2, so the annulus **1/3 < |z| < 1/2** is non-empty but does **not** contain the unit
   circle: the sequence is not absolutely summable and a causal system with those poles would be unstable.
9. The zero at z = 1 kills DC and the pole at 0.8 lifts the low frequencies near it → **highpass**
   (first-difference-like): |H| ≈ 0 at w = 0, rising towards w = π.
10. Because substituting z = e^{j2πk/N} reproduces the DFT twiddle factors, and N equally spaced points on a
    circle repeat every N samples of k: X[k + N] = X[k].

Check yourself in `DSP/practice/step11_ztransform.py` — the checker prints the SymPy sums, the two-sided
value at z = 1.2 (3.214286), the three ROC tests, and the zeros/poles.


