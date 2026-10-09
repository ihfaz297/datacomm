# Topic 2 — The z-transform and LTI analysis (Proakis Ch 3) → **TT2 question, 10 marks**

Source of truth: `Note/Mid-2 note.pdf` pages 25–33 (Proakis Ex 3.1.1, 3.1.2, 3.1.3, 3.1.5, 3.2.1, 3.2.2,
3.3.4) and the 2021-22 final paper (Q4a, 4b, 4f, 5a, 5f, 6a, 6b). All numbers are checked by `_mid2_verify.py`.

**The one rule that gets people killed: an X(z) without its ROC is half an answer.** Write "ROC: …" under every X(z).

---

## 0. The whole topic in 6 lines

1. X(z) = Σ x[n]z^{−n}, with z = re^{jω}. On the unit circle (r = 1) it **is** the DTFT.
2. ROC = the set of z where that sum converges. Same formula with a different ROC means a different signal.
3. Right-sided → ROC is **outside** a circle. Left-sided → **inside** a circle. Two-sided → a **ring**, or nothing.
4. Poles are where X = ∞ and zeros are where X = 0. The ROC never contains a pole.
5. For an LTI system, Y(z) = H(z)X(z). A difference equation becomes algebra.
6. Stable ⇔ the ROC contains |z| = 1. Causal and stable ⇔ **all poles inside the unit circle**.

---

## 1. Why z-transform? (2-mark definition question)

> The DTFT X(e^{jω}) = Σx[n]e^{−jωn} does not converge for every sequence: growing exponentials and
> unstable systems blow up. The z-transform replaces e^{jω} (stuck on the unit circle, |e^{jω}| = 1) by a
> general complex z = re^{jω} of any magnitude. The extra factor r^{−n} can tame the growth, so the z-transform is the
> more general form of the DTFT.
>
> **X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}**  ·  **ROC = set of all z for which X(z) is finite.**

"How is z-transform related to DFT/DTFT?" (final 4b): **X(e^{jω}) = X(z)|_{z=e^{jω}}**, which is the z-transform on the unit circle. The DFT samples that at N points: X[k] = X(z) at z = e^{j2πk/N}.

---

## 2. Finite sequences — Proakis Ex 3.1.1 (warm-up, very likely as a part)

| x[n] (↑ marks n = 0) | X(z) | ROC |
|---|---|---|
| {1↑, 2, 5, 7, 0, 1} | 1 + 2z⁻¹ + 5z⁻² + 7z⁻³ + z⁻⁵ | all z except **z = 0** |
| {1, 2, 5↑, 7, 0, 1} | z² + 2z + 5 + 7z⁻¹ + z⁻³ | all z except **z = 0 and z = ∞** |
| {0, 0, 1↑, 2, 5, 7, 0, 1} | z⁻² + 2z⁻³ + 5z⁻⁴ + 7z⁻⁵ + z⁻⁷ | all z except z = 0 |
| δ[n] | 1 | **entire z-plane** |
| δ[n−k], k > 0 | z^{−k} | all z except z = 0 |
| δ[n+k], k > 0 | z^{k} | all z except z = ∞ |

**Rule:** a negative power of z (z⁻¹ = 1/z) blows up at z = 0. A positive power blows up at z = ∞. Check which ones you have.

---

## 3. The four infinite sequences you must derive (Ex 3.1.2, 3.1.3, 3.1.5)

### 3a. Causal: x[n] = aⁿu[n]  ★

> X(z) = Σ_{n=0}^{∞} aⁿz^{−n} = Σ_{n=0}^{∞}(az⁻¹)ⁿ = 1/(1 − az⁻¹) = z/(z − a)
> The geometric series converges if |az⁻¹| < 1, i.e. **ROC: |z| > |a|** (outside the circle of radius |a|).

Ex 3.1.2 is a = ½: X = 1/(1 − ½z⁻¹), ROC |z| > ½.

### 3b. Anti-causal: x[n] = −aⁿu[−n−1]  ★

> X(z) = Σ_{n=−∞}^{−1} (−aⁿ)z^{−n} = −Σ_{l=1}^{∞}(a⁻¹z)^l   [l = −n]
> = −(a⁻¹z)/(1 − a⁻¹z)   [A + A² + … = A/(1−A)]
> = z/(z − a) = **1/(1 − az⁻¹)**, converging if |a⁻¹z| < 1, so **ROC: |z| < |a|** (inside the circle).

**The punchline (write it!):** 3a and 3b have the **same closed form** with **different ROCs**. A closed-form expression does not uniquely specify the signal. *A discrete-time signal is uniquely identified by its z-transform X(z) **together with** its ROC.*

### 3c. Two-sided: x[n] = aⁿu[n] + bⁿu[−n−1]  ★★ (final 6a, 10 marks; also 4f)

> X(z) = Σ_{n=0}^{∞}(az⁻¹)ⁿ + Σ_{l=1}^{∞}(b⁻¹z)^l = 1/(1 − az⁻¹) − 1/(1 − bz⁻¹)
> First sum converges for |z| > |a|. Second sum converges for |z| < |b|.
>
> **Case 1: |b| ≤ |a|** → the regions |z| > |a| and |z| < |b| do not overlap → **X(z) does not exist.**
> **Case 2: |a| < |b|** → they overlap in a ring → **ROC: |a| < |z| < |b|**
>
> X(z) = (a − b)z⁻¹ / [(1 − az⁻¹)(1 − bz⁻¹)]   (equivalently (b − a)/(a + b − z − abz⁻¹), the note's form)

**Sketch the ROC**: two concentric circles of radius |a| and |b| with the ring between them shaded. For case 1, draw the two regions not touching.
Check value: a = 0.5, b = 2, z = 1.2 gives X = 3.2143 from the closed form and from the summed series. ✔

### 3d. Sum of two causal exponentials — Ex 3.2.1: x[n] = [3(2ⁿ) − 4(3ⁿ)]u[n]

> X(z) = 3/(1 − 2z⁻¹) − 4/(1 − 3z⁻¹)
> ROC₁: |z| > 2, ROC₂: |z| > 3 → **ROC = intersection: |z| > 3**

### 3e. Families of signals vs ROC (the table in the note — draw it if asked "characteristic families")

| | Finite duration | Infinite duration |
|---|---|---|
| **Causal** (right-sided, n ≥ 0) | all z except z = 0 | **\|z\| > r₂** (outside) |
| **Anti-causal** (left-sided) | all z except z = ∞ | **\|z\| < r₁** (inside) |
| **Two-sided** | all z except 0 and ∞ | **r₂ < \|z\| < r₁** (ring) |

---

## 4. Properties (table worth 5 marks on its own)

| Property | Time domain | z-domain | ROC |
|---|---|---|---|
| Linearity | a₁x₁[n] + a₂x₂[n] | a₁X₁(z) + a₂X₂(z) | at least ROC₁ ∩ ROC₂ |
| Time shift | x[n−k] | z^{−k}X(z) | same, except maybe z = 0 (k>0) or z = ∞ (k<0) |
| z-scaling | aⁿx[n] | X(a⁻¹z) | \|a\|r₂ < \|z\| < \|a\|r₁ |
| Time reversal | x[−n] | X(z⁻¹) | 1/r₁ < \|z\| < 1/r₂ |
| Conjugation | x*[n] | X*(z*) | same ROC |
| Differentiation in z | n x[n] | −z dX(z)/dz | same ROC |
| Convolution | x₁[n] ⊛ x₂[n] | X₁(z)X₂(z) | at least ROC₁ ∩ ROC₂ |

Proofs sir likes (2–3 lines each):
- **Time shift:** Σx[n−k]z^{−n}, let m = n−k → Σx[m]z^{−(m+k)} = z^{−k}X(z).
- **Scaling:** Σaⁿx[n]z^{−n} = Σx[n](a⁻¹z)^{−n} = X(a⁻¹z).
- **Linearity:** split the sum.

### 4a. Using Euler + linearity — Ex 3.2.2

> cos(ω₀n)u[n] = ½e^{jω₀n}u[n] + ½e^{−jω₀n}u[n]. Each term is aⁿu[n] with a = e^{±jω₀}, |a| = 1.
> X(z) = ½/(1 − e^{jω₀}z⁻¹) + ½/(1 − e^{−jω₀}z⁻¹) = **(1 − z⁻¹cos ω₀)/(1 − 2z⁻¹cos ω₀ + z⁻²)**, ROC |z| > 1
>
> sin(ω₀n)u[n] = (1/2j)[e^{jω₀n} − e^{−jω₀n}]u[n] → **z⁻¹ sin ω₀ / (1 − 2z⁻¹cos ω₀ + z⁻²)**, ROC |z| > 1

⚠ **Note erratum:** on note p.30 the sin denominator is written "1 − 2cos ω₀z⁻¹ **−** z⁻²". It must be **+ z⁻²**, because e^{jω₀}e^{−jω₀}z⁻² = +z⁻². The pairs table on p.31 has it right.

---

## 5. Common pairs (memorise the left half; the right half follows from properties)

| x[n] | X(z) | ROC |
|---|---|---|
| δ[n] | 1 | all z |
| u[n] | 1/(1 − z⁻¹) | \|z\| > 1 |
| aⁿu[n] | 1/(1 − az⁻¹) | \|z\| > \|a\| |
| −aⁿu[−n−1] | 1/(1 − az⁻¹) | \|z\| < \|a\| |
| naⁿu[n] | az⁻¹/(1 − az⁻¹)² | \|z\| > \|a\| |
| −naⁿu[−n−1] | az⁻¹/(1 − az⁻¹)² | \|z\| < \|a\| |
| cos(ω₀n)u[n] | (1 − z⁻¹cos ω₀)/(1 − 2z⁻¹cos ω₀ + z⁻²) | \|z\| > 1 |
| sin(ω₀n)u[n] | z⁻¹sin ω₀/(1 − 2z⁻¹cos ω₀ + z⁻²) | \|z\| > 1 |
| aⁿcos(ω₀n)u[n] | (1 − az⁻¹cos ω₀)/(1 − 2az⁻¹cos ω₀ + a²z⁻²) | \|z\| > \|a\| |
| aⁿsin(ω₀n)u[n] | az⁻¹sin ω₀/(1 − 2az⁻¹cos ω₀ + a²z⁻²) | \|z\| > \|a\| |

---

## 6. Poles and zeros (final 4a, 5f, 6b)

**Definitions (2 marks):** *Zeros* are the values of z where X(z) = 0. *Poles* are the values of z where X(z) = ∞. In a plot, poles are ×, zeros are ○.

**Rational form:** X(z) = B(z)/A(z) = G·z^{N−M}·Π(z − z_k)/Π(z − p_k)
- If N > M: z^{N−M} gives N−M extra **zeros at z = 0**. If N < M: M−N extra **poles at z = 0**.
- Counting at 0 and ∞ too: number of zeros = number of poles.
- Complex poles and zeros come in conjugate pairs when the coefficients are real.

### 6a. Worked (note p.32): X(z) = z(2z² − 2z + 1)/(16z³ + 6z + 5)

> Zeros: z = 0, and 2z² − 2z + 1 = 0 → **z = 0.5 ± j0.5**
> Poles: 16z³ + 6z + 5 = 0 → **z = −0.5, 0.25 ± j0.75** (try z = −0.5: 16(−0.125) − 3 + 5 = 0 ✔, then divide)
> If causal: ROC is outside the largest pole, **|z| > |0.25 ± j0.75| = 0.79**. That contains |z| = 1, so it is stable.

### 6b. Final 6b (10 marks): x[n] = aⁿ for 0 ≤ n ≤ M−1, 0 otherwise. z-transform and pole-zero plot

> X(z) = Σ_{n=0}^{M−1}(az⁻¹)ⁿ = (1 − aᴹz⁻ᴹ)/(1 − az⁻¹) = **(zᴹ − aᴹ) / (z^{M−1}(z − a))**
> ROC: finite and causal, so **|z| > 0** (all z except 0).
> Zeros: zᴹ = aᴹ → **z_k = a·e^{j2πk/M}, k = 0, 1, …, M−1** (M points equally spaced on a circle of radius |a|)
> Poles: z^{M−1} = 0 → **M−1 poles at z = 0**, plus one pole at z = a
> The pole at z = a **cancels** the zero at k = 0 (z₀ = a).
> **Final: M−1 zeros at ae^{j2πk/M}, k = 1…M−1; M−1 poles at the origin.**

Sketch for M = 8: a circle of radius a, ○ at 7 of the 8 equally spaced points (the k = 0 spot on the positive real axis is empty: pole-zero cancellation), and an × labelled "7th order" at the origin.

### 6c. Significance of poles and zeros (final 5f, 5 marks)

- Poles decide the **natural modes** and the shape of h[n]: a real pole p gives pⁿ; a complex pair re^{±jω₀} gives rⁿcos(ω₀n + φ), which rings.
- Pole radius: **inside the unit circle → decays (stable); on it → sustained; outside → grows (unstable)**. The closer a pole is to |z| = 1, the slower the decay and the sharper the peak in |H|.
- Pole angle ω₀ is where |H(e^{jω})| **peaks** (resonance). A zero on the unit circle at angle ω₀ makes **|H(e^{jω₀})| = 0** (a notch).
- Geometric view: |H(e^{jω})| ∝ (product of distances from e^{jω} to the zeros)/(product of distances to the poles).
- Causal and stable ⇔ all poles inside the unit circle.

---

## 7. System function and stability

> h[n] ←z→ H(z): the **system function**. Y(z) = H(z)X(z), so **H(z) = Y(z)/X(z)**.
>
> For an LCCDE y[n] = −Σ_{k=1}^{N}a_k y[n−k] + Σ_{k=0}^{M}b_k x[n−k]:
> **H(z) = Σb_k z^{−k} / (1 + Σa_k z^{−k})**, which is a rational system function.

**Stability proof (note p.31–32):** stable ⇔ Σ|h[n]| < ∞. |H(z)| ≤ Σ|h[n]||z^{−n}|, which equals Σ|h[n]| on |z| = 1.
So **an LTI system is stable ⇔ the ROC of H(z) contains the unit circle.** A causal system's ROC is outside its largest pole, so **causal and stable ⇔ every pole has |p| < 1.**

### 7a. Ex 3.3.4 = final 5a ★ — y(n) = ½y(n−1) + 2x(n): system function and unit sample response

> Y(z) = ½z⁻¹Y(z) + 2X(z) → Y(z)(1 − ½z⁻¹) = 2X(z)
> **H(z) = 2/(1 − ½z⁻¹)**: pole at z = ½, zero at z = 0
> From the table (aⁿu[n] ↔ 1/(1 − az⁻¹)): **h[n] = 2(½)ⁿu[n]** = {2, 1, 0.5, 0.25, …}
> The pole at ½ is inside the unit circle, so the system is stable. (H(e^{j0}) = 2/(1 − ½) = 4.)

### 7b. FIR: y[n] = 3x[n] − 4x[n−1] + x[n−2], find h[n]

> H(z) = 3 − 4z⁻¹ + z⁻² → **h[n] = 3δ[n] − 4δ[n−1] + δ[n−2]** = {3↑, −4, 1}

---

## 8. Inverse z-transform — three methods

1. **Power series expansion**: read x[n] off the coefficient of z^{−n}.
2. **Contour integration**: x[n] = (1/2πj)∮X(z)z^{n−1}dz. Just *state* it; nobody makes you evaluate it in 45 min.
3. **Partial fractions + table lookup**: the main method.

### 8a. Power series — X(z) = log(1 + az⁻¹), |z| > |a|

> log(1+u) = u − u²/2 + u³/3 − … = Σ_{n≥1}(−1)^{n+1}uⁿ/n, with u = az⁻¹
> X(z) = Σ_{n≥1}[(−1)^{n+1}aⁿ/n] z^{−n} ⇒ **x[n] = (−1)^{n+1}aⁿ/n for n ≥ 1, and 0 for n ≤ 0**

Use this method when a series is known (log, exp, sin/cos, geometric).

### 8b. Partial fractions, distinct poles — the "Imp for exam" problem ★★★

> **x[n] = 2ⁿu[n], h[n] = (0.5)ⁿu[n]. Find y = x ⊛ h (1) in the time domain, (3) with the z-transform.**

**(1) Time domain:**
> y[n] = Σ_{k=0}^{n} 2^k(0.5)^{n−k} = (0.5)ⁿΣ_{k=0}^{n}4^k = (0.5)ⁿ(4^{n+1} − 1)/3
> = **(4/3)2ⁿ − (1/3)(0.5)ⁿ, n ≥ 0**

**(3) z-domain:**
> X(z) = 1/(1 − 2z⁻¹), ROC |z| > 2.  H(z) = 1/(1 − 0.5z⁻¹), ROC |z| > 0.5
> Y(z) = 1/[(1 − 2z⁻¹)(1 − 0.5z⁻¹)] = z²/[(z−2)(z−0.5)], ROC at least |z| > 2
> Y(z)/z = z/[(z−2)(z−0.5)] = A/(z−2) + B/(z−0.5)
> z = 2: A = 2/1.5 = **4/3**;  z = 0.5: B = 0.5/(−1.5) = **−1/3**
> Y(z) = (4/3)/(1 − 2z⁻¹) − (1/3)/(1 − 0.5z⁻¹) ⇒ **y[n] = (4/3)2ⁿu[n] − (1/3)(0.5)ⁿu[n]**

Checked against numpy's convolve for n = 0…7: {1, 2.5, 5.25, 10.625, …}. Both methods agree.

**(2) "Frequency domain"** — ⚠ the note writes X(e^{jω}) = 1/(1 − 2e^{−jω}). **That DTFT does not exist**: 2ⁿu[n] is not absolutely summable, and the ROC |z| > 2 does not contain the unit circle. If sir asks for method (2), write Y(e^{jω}) = X(e^{jω})H(e^{jω}) as the *principle*, then add one line: *"Since |z| > 2 excludes |z| = 1, the DTFT of 2ⁿu[n] does not converge; the z-transform is required. This is exactly why the z-transform generalises the DTFT."* That line turns his trap into marks.

**Steps (write these at the top of any partial-fraction answer):**
1. Find the poles p₁…p_K and their multiplicities.
2. Expand X(z)/z (this keeps it strictly proper and gives the z/(z−p) form back).
3. Get the coefficients by the cover-up rule (put z = pole), or by comparing coefficients.
4. Multiply back by z, convert z/(z−p) = 1/(1 − pz⁻¹), and read pⁿu[n] off the table, choosing causal or anti-causal **by the ROC**.

### 8c. Partial fractions, repeated pole — poles at −2 and a double pole at 1

> X(z) = 1/[(1 + 2z⁻¹)(1 − z⁻¹)²] ⇒ X(z)/z = z²/[(z+2)(z−1)²] = A/(z+2) + B/(z−1) + C/(z−1)²
> z² = A(z−1)² + B(z−1)(z+2) + C(z+2)
> z = 1: 1 = 3C → **C = 1/3**;  z = −2: 4 = 9A → **A = 4/9**;  z² coefficient: 1 = A + B → **B = 5/9**
> X(z) = (4/9)/(1 + 2z⁻¹) + (5/9)/(1 − z⁻¹) + (1/3)·z⁻¹/(1 − z⁻¹)²
> **x[n] = (4/9)(−2)ⁿu[n] + (5/9)u[n] + (1/3)n·u[n]**   (assuming causal)

⚠ **Note erratum:** the note's last line has "(4/9)(2)ⁿ". It must be **(−2)ⁿ**, because 1/(1 + 2z⁻¹) = 1/(1 − (−2)z⁻¹). Quick check: x[1] from long division is 0. (4/9)(−2) + 5/9 + 1/3 = 0 ✔, while (4/9)(2) + 5/9 + 1/3 = 16/9 ✘.

---

## 9. Ten-minute self-test

| # | Question | Answer |
|---|---|---|
| 1 | X(z) and ROC of {1, 2, 5↑, 7, 0, 1} | z² + 2z + 5 + 7z⁻¹ + z⁻³; all z except 0 and ∞ |
| 2 | aⁿu[n] vs −aⁿu[−n−1] | same 1/(1−az⁻¹); ROC \|z\|>\|a\| vs \|z\|<\|a\| |
| 3 | ROC of aⁿu[n] + bⁿu[−n−1] | \|a\| < \|z\| < \|b\|; does not exist if \|b\| ≤ \|a\| |
| 4 | ROC of [3·2ⁿ − 4·3ⁿ]u[n] | \|z\| > 3 |
| 5 | Z{nx[n]} | −z dX/dz |
| 6 | Poles/zeros of aⁿ, 0≤n≤M−1 | M−1 zeros at ae^{j2πk/M} (k=1…M−1), M−1 poles at 0 |
| 7 | Stability condition in terms of ROC | ROC contains \|z\| = 1; causal: all poles inside |
| 8 | h[n] for y = ½y(n−1) + 2x(n) | 2(½)ⁿu[n] |
| 9 | 2ⁿu[n] ⊛ 0.5ⁿu[n] | (4/3)2ⁿ − (1/3)0.5ⁿ, n ≥ 0 |
| 10 | Inverse of 1/[(1+2z⁻¹)(1−z⁻¹)²], causal | (4/9)(−2)ⁿ + 5/9 + n/3, n ≥ 0 |
| 11 | Inverse of log(1 + az⁻¹) | (−1)^{n+1}aⁿ/n, n ≥ 1 |
| 12 | Three inversion methods | power series, contour integral, partial fractions |
