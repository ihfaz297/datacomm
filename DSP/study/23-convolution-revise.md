# Convolution revision — the way *sir* wants it (lesson from TT1)

**What happened in TT1:** Q4 was *"h(n) = {1, 2↑, 1, −1}. Determine the response for x(n) = {1↑, 2, 3, 1}."*
That is Proakis Example 2.3.2 word for word. You knew the fast method, but sir wanted the
**expansion**: write the convolution sum, then expand it term by term for each n. Marks go to the
*working he expects to see*, not just to the right sequence.

**Rule for Mid-2:** use **Method A (expansion)** as the answer. If the question says "using
z-transform", use **Method B**. Use Method C (your tabular trick) only as a 20-second check in the margin.
Mid-2 Q2 can easily be *"find y(n) using the z-transform"*, and that is just Method B.

---

## 0. The one formula

> **y(n) = x(n) ⊛ h(n) = Σ_{k=−∞}^{∞} x(k) h(n−k)**   (= Σ h(k)x(n−k), because convolution is commutative)

Three facts to write before any calculation (each is a line of marks):
1. **Length**: if x has N₁ samples and h has N₂, y has **N₁ + N₂ − 1** samples.
2. **Start index**: y starts at (start of x) + (start of h). **End**: (end of x) + (end of h).
3. **Non-zero range of k**: only the k where *both* x(k) and h(n−k) can be non-zero.

---

## Method A — Expansion of the sum (★ what sir marks)

### A1. TT1 Q4, done the expected way

**Given:** x(n) = {1↑, 2, 3, 1} → x(0)=1, x(1)=2, x(2)=3, x(3)=1
       h(n) = {1, 2↑, 1, −1} → h(−1)=1, h(0)=2, h(1)=1, h(2)=−1

**Step 1, ranges:** x lives on 0 ≤ n ≤ 3 and h on −1 ≤ n ≤ 2, so
y lives on (0 + (−1)) ≤ n ≤ (3 + 2), i.e. **−1 ≤ n ≤ 5**, and length = 4 + 4 − 1 = **7** ✔.

**Step 2, write the sum with x's range** (x(k) ≠ 0 only for k = 0…3):

> y(n) = Σ_{k=0}^{3} x(k)h(n−k) = x(0)h(n) + x(1)h(n−1) + x(2)h(n−2) + x(3)h(n−3)
>   = **h(n) + 2h(n−1) + 3h(n−2) + h(n−3)**

**Step 3, expand for every n.** Any h outside −1…2 is 0. Write those zeros out at least for the first n, so he sees you know them:

> y(−1) = h(−1) + 2h(−2) + 3h(−3) + h(−4) = 1 + 0 + 0 + 0 = **1**
> y(0) = h(0) + 2h(−1) + 3h(−2) + h(−3) = 2 + 2(1) + 0 + 0 = **4**
> y(1) = h(1) + 2h(0) + 3h(−1) + h(−2) = 1 + 4 + 3 + 0 = **8**
> y(2) = h(2) + 2h(1) + 3h(0) + h(−1) = −1 + 2 + 6 + 1 = **8**
> y(3) = h(3) + 2h(2) + 3h(1) + h(0) = 0 − 2 + 3 + 2 = **3**
> y(4) = h(4) + 2h(3) + 3h(2) + h(1) = 0 + 0 − 3 + 1 = **−2**
> y(5) = h(5) + 2h(4) + 3h(3) + h(2) = 0 + 0 + 0 − 1 = **−1**
> y(n) = 0 for n < −1 and n > 5

**Step 4, box it with the arrow:** **y(n) = {1, 4↑, 8, 8, 3, −2, −1}**

**Step 5, one-line check:** Σy = Σx · Σh → 1+4+8+8+3−2−1 = 21 = 7 × 3 ✔ (Σx = 7, Σh = 3).
This check catches 90% of arithmetic slips. Always do it.

### A2. Final 2021-22 Q1h — x = {−1, 3, 2, 0, 1}, −2 ≤ n ≤ 2; h = {−3, 5, 0, 1}, −1 ≤ n ≤ 2

> Ranges: y on −3 ≤ n ≤ 4, length 5 + 4 − 1 = 8.
> y(n) = Σ_{k=−2}^{2} x(k)h(n−k) = −h(n+2) + 3h(n+1) + 2h(n) + 0·h(n−1) + h(n−2)
> y(−3) = −h(−1) = −(−3) = **3**
> y(−2) = −h(0) + 3h(−1) = −5 − 9 = **−14**
> y(−1) = −h(1) + 3h(0) + 2h(−1) = 0 + 15 − 6 = **9**
> y(0) = −h(2) + 3h(1) + 2h(0) + h(−2) = −1 + 0 + 10 + 0 = **9**
> y(1) = 3h(2) + 2h(1) + h(−1) = 3 + 0 − 3 = **0**
> y(2) = 2h(2) + h(0) = 2 + 5 = **7**
> y(3) = h(1) = **0**
> y(4) = h(2) = **1**
> **y(n) = {3, −14, 9, 9↑, 0, 7, 0, 1}**   check: Σy = 15 = Σx·Σh = 5·3 ✔

### A3. Infinite sequences — same method, the sum becomes a geometric series

**x(n) = u(n), h(n) = aⁿu(n), |a| < 1 (Proakis Ex 2.3.3 type):**
> y(n) = Σ_k a^k u(k)·u(n−k). u(k) needs k ≥ 0 and u(n−k) needs k ≤ n, so the sum runs over **0 ≤ k ≤ n** (and only for n ≥ 0):
> y(n) = Σ_{k=0}^{n} a^k = **(1 − a^{n+1})/(1 − a), n ≥ 0**; y(n) = 0 for n < 0
> n → ∞: y → 1/(1−a). That is H(e^{j0}), the DC steady state (topic 1 again!)

**x = 2ⁿu(n), h = 0.5ⁿu(n)** (the "Imp for exam" one): range 0 ≤ k ≤ n →
y(n) = Σ 2^k 0.5^{n−k} = 0.5ⁿΣ4^k = **(4/3)2ⁿ − (1/3)0.5ⁿ, n ≥ 0**. See `21-T2-ztransform.md` §8b.

**The 3 phrases that earn the method marks for infinite sums:** "u(k) ≠ 0 ⇒ k ≥ 0", "u(n−k) ≠ 0 ⇒ k ≤ n",
"∴ for n ≥ 0, sum over 0 ≤ k ≤ n; for n < 0, y(n) = 0".

---

## Method B — z-transform (polynomial multiplication) ★ for Mid-2

> Convolution in time = multiplication in z: **Y(z) = X(z)H(z)**. Then read y(n) off the coefficient of z^{−n}.

**TT1 Q4 again:**
> X(z) = 1 + 2z⁻¹ + 3z⁻² + z⁻³   (x starts at n = 0)
> H(z) = z + 2 + z⁻¹ − z⁻²       (h(−1) = 1 gives a z¹ term)
> Y(z) = X(z)H(z): multiply term by term and collect the powers:
> z¹: 1·1 = **1**
> z⁰: 1·2 + 2·1 = **4**
> z⁻¹: 1·1 + 2·2 + 3·1 = **8**
> z⁻²: 1·(−1) + 2·1 + 3·2 + 1·1 = **8**
> z⁻³: 2·(−1) + 3·1 + 1·2 = **3**
> z⁻⁴: 3·(−1) + 1·1 = **−2**
> z⁻⁵: 1·(−1) = **−1**
> Y(z) = z + 4 + 8z⁻¹ + 8z⁻² + 3z⁻³ − 2z⁻⁴ − z⁻⁵ ⇒ **y(n) = {1, 4↑, 8, 8, 3, −2, −1}** (the z⁰ coefficient is n = 0)
> ROC: all z except 0 and ∞ (finite and two-sided).

For infinite signals, Method B means partial fractions. That is the 2ⁿ/0.5ⁿ example in `21-T2-ztransform.md` §8b.

---

## Method C — your tabular / multiplication trick (check only)

Write x across the top and h down the side. Fill the grid with products and add along the anti-diagonals.
Or do "long multiplication without carries": 1 2 3 1 × 1 2 1 −1 → 1, 4, 8, 8, 3, −2, −1.
Place the arrow by the start index: (start of x) + (start of h) = 0 + (−1) = −1, so the first value is y(−1).

|   | **1** | **2** | **3** | **1** |
|---|---|---|---|---|
| **1** | 1 | 2 | 3 | 1 |
| **2** | 2 | 4 | 6 | 2 |
| **1** | 1 | 2 | 3 | 1 |
| **−1** | −1 | −2 | −3 | −1 |

Anti-diagonals: 1 | 2+2 | 3+4+1 | 1+6+2−1 | 2+3−2 | 1−3 | −1 → 1, 4, 8, 8, 3, −2, −1 ✔

Use it in the margin to check Method A. **Never as the only answer** unless the question says "any method".

## Method D — graphical (fold, shift, multiply, sum) — know the 4 words

1. **Fold** h(k) → h(−k). 2. **Shift** by n → h(n−k). 3. **Multiply** x(k)·h(n−k) point by point. 4. **Sum** over k.
If he says "graphically illustrate" (final Q3c), draw x(k) and h(n−k) for 2–3 values of n and show the overlap.

---

## Which method when (read the verb!)

| Question says | Use |
|---|---|
| "Determine the response / output", "find y(n)" | **A, the expansion**, with the ranges written first |
| "using z-transform" / "in the z-domain" | **B**, with the ROC |
| "graphically" / "illustrate the computation" | **D**, with sketches |
| "using frequency domain" | Y(e^{jω}) = X(e^{jω})H(e^{jω}), only if both DTFTs exist |
| no method named and short on time | A, verified with C in the margin |

## Quick drill (cover the answers)

| # | x | h | y |
|---|---|---|---|
| 1 | {1↑, 1, 1} | {1↑, 1, 1} | {1↑, 2, 3, 2, 1} |
| 2 | {1↑, 2, 3, 1} | {1, 2↑, 1, −1} | {1, 4↑, 8, 8, 3, −2, −1} |
| 3 | {−1, 3, 2↑, 0, 1} (−2 ≤ n ≤ 2) | {−3, 5↑, 0, 1} (−1 ≤ n ≤ 2) | {3, −14, 9, 9↑, 0, 7, 0, 1} |
| 4 | u(n) | aⁿu(n) | (1−a^{n+1})/(1−a), n ≥ 0 |
| 5 | 2ⁿu(n) | 0.5ⁿu(n) | (4/3)2ⁿ − (1/3)0.5ⁿ, n ≥ 0 |

All checked with `numpy.convolve`. Also in `mid2_handcalc_drill.py` (conv section).
