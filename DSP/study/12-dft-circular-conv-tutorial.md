# Tutorial 12 — DFT, IDFT, circular convolution and the FFT

Covers TT2 **Q1** (complexity, 5 marks) and **Q3** (four-point DFT, 5 marks), plus final-paper Q3c, Q4d,
Q4e, Q4h and Q6c. Pairs with the drill `DSP/practice/step12_dft_fft.py`.

---

## §1 The DFT, one output bin at a time

```text
X[k] = sum_{n=0}^{N-1} x[n] e^(-j 2 pi k n / N)          k = 0, 1, ..., N-1
x[n] = (1/N) sum_{k=0}^{N-1} X[k] e^(+j 2 pi k n / N)    the IDFT: 1/N and a PLUS sign
```

Reading it like a human: **X[k] is the correlation of x[n] with a complex exponential at frequency
2πk/N.** For each k you walk along the signal, multiply by a spinning phasor, and add up. Slowly-spinning
phasors (small k) measure low frequencies. There are exactly N of them, one per multiple of 2π/N.

Fact worth writing in the exam: **X[0] = Σ x[n] = N × (mean of the sequence)** — bin 0 is the DC value.
The 1/N in the IDFT is the price of that scaling convention.

**The 4-point twiddle table** (memorise this; it makes every 4-point question a 30-second job). With
W = e^{−j2π/4} = −j:

| k \ n | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | −j | −1 | +j |
| 2 | 1 | −1 | 1 | −1 |
| 3 | 1 | +j | −1 | −j |

Every row is the previous row multiplied by the twiddle. If you can write this table you can do any
4-point DFT by hand, in either direction.

---

## §2 Worked example — DFTs by hand (final Q6c and TT2 Q3's first half)

**Question (final Q6c).** Find the DFT of x(n) = {1, 1, 2, 1}.

**Step 1 — lay the samples under the table and multiply-add per row.**

```text
k = 0: 1(1) + 1(1) + 2(1) + 1(1)               = 5
k = 1: 1(1) + 1(-j) + 2(-1) + 1(+j) = 1 - 2 + (-j + j) = -1
k = 2: 1(1) + 1(-1) + 2(1) + 1(-1) = 1 - 1 + 2 - 1     = 1
k = 3: 1(1) + 1(+j) + 2(-1) + 1(-j) = 1 - 2 + (j - j) = -1
```

**X[k] = {5, −1, 1, −1}** — machine-checked to 1e-16 against `np.fft.fft`.

**Step 2 — check the two symmetry facts.** X[0] = 5 = the sum of the samples ✓, and for real x,
X[N−k] = X*[k]: X[3] = X*[1] = −1 ✓ (trivially, because here everything is real).

**Step 3 — the same for h(n) = {1, 2, 1}** (N = 3, so the twiddles are e^{∓j2π/3} = −0.5 ∓ 0.866j):

```text
k = 0: 1 + 2 + 1 = 4
k = 1: 1 + 2(-0.5 - 0.866j) + 1(-0.5 + 0.866j) = 1 - 1 - 0.5 + (-1.732j + 0.866j)
       = -0.5 - 0.866j = e^(-j 2pi/3)
k = 2: 1 + 2(-0.5 + 0.866j) + 1(-0.5 - 0.866j) = -0.5 + 0.866j = e^(+j 2pi/3)
```

**H[k] = {4, e^{−j2π/3}, e^{+j2π/3}}** — magnitudes {4, 1, 1}. The drill compares against these exact
values, not against decimals, which is the clean way to quote an answer in an exam.

**Step 4 — the IDFT** (needed for Q6c's second half). Apply the same table with +j and divide by N:
for H = {4, −0.5−0.866j, −0.5+0.866j} and N = 3, the three outputs come back as {1, 2, 1} ✓.

---

## §3 Circular convolution — the wrap method, step by step

**Definition.** For two length-N sequences,

```text
y[n] = sum_{k=0}^{N-1} x[k] * h[(n - k) mod N]        the mod N is what makes it "circular"
```

The *only* difference from ordinary convolution is that the index wraps: sample −1 is sample N−1.
Two ways to do that wrap, and both earn marks:

**(a) The "reverse and slide" picture.** Write x[k] on a circle. Reverse h and place it against x; each
step rotates h by one position, and you multiply-and-add the two rings. When h falls off the end of the
ring it reappears at the start — that is the wrap that the examiner wants drawn.

**(b) The number table** (faster under time pressure). **Pad h with zeros to N samples**, then for each n
take products x[k]·h[(n − k) mod N] for k = 0…N−1 and add. Because h is zero-padded, many terms vanish.

### Worked — TT2 Q3, the actual exam question: x(n) = {1,2,2,1}, h(n) = {1,2,3}, N = 4

Pad: h = {1, 2, 3, **0**} on n = 0…3.

| n | k = 0 | k = 1 | k = 2 | k = 3 | y[n] |
|---|---|---|---|---|---|
| 0 | x[0]h[0] = 1·1 = 1 | x[1]h[3] = 2·0 = 0 | x[2]h[2] = 2·3 = 6 | x[3]h[1] = 1·2 = 2 | **9** |
| 1 | x[0]h[1] = 1·2 = 2 | x[1]h[0] = 2·1 = 2 | x[2]h[3] = 2·0 = 0 | x[3]h[2] = 1·3 = 3 | **7** |
| 2 | x[0]h[2] = 1·3 = 3 | x[1]h[1] = 2·2 = 4 | x[2]h[0] = 2·1 = 2 | x[3]h[3] = 1·0 = 0 | **9** |
| 3 | x[0]h[3] = 1·0 = 0 | x[1]h[2] = 2·3 = 6 | x[2]h[1] = 2·2 = 4 | x[3]h[0] = 1·1 = 1 | **11** |

**y(n) = {9, 7, 9, 11}.** Machine-checked twice — by the table and by the DFT product.

**The DFT-product route**, which is what the phrase "results from the use of a four-point DFT" really
asks for: X[k] = {6, −1−j, 0, −1+j}, padded H[k] = {6, −2−2j, 2, −2+2j}, so

```text
Y[k] = X[k] H[k] = {36, (1+j)(2+2j), 0, (1-j)(2-2j)} = {36, 4j, 0, -4j}
```

and the inverse DFT of {36, 4j, 0, −4j} is **{9, 7, 9, 11}** ✓. Multiply in the k-domain, divide by N
and use +j in the time domain — that is all a DFT-based convolution is.

### Worked — final Q3c: x1(n) = {1,1,2,1} and x2(n) = {1,2,1,1} (10 marks, "illustrate graphically")

Same table, h = {1, 2, 1, 1} (already four samples, no padding needed):

| n | k = 0 | k = 1 | k = 2 | k = 3 | y[n] |
|---|---|---|---|---|---|
| 0 | 1·1 = 1 | 1·1 = 1 | 2·1 = 2 | 1·2 = 2 | **6** |
| 1 | 1·2 = 2 | 1·1 = 1 | 2·1 = 2 | 1·1 = 1 | **6** |
| 2 | 1·1 = 1 | 1·2 = 2 | 2·1 = 2 | 1·1 = 1 | **6** |
| 3 | 1·1 = 1 | 1·1 = 1 | 2·2 = 4 | 1·1 = 1 | **7** |

**y(n) = {6, 6, 6, 7}** — also confirmed through the DFT product (X1 = {5,−1,1,−1}, X2 = {5,−j,−1,+j},
Y = {25, +j, −1, −j}, IDFT → {6,6,6,7}) and by A/B testing: the checker computes it both ways.

### The matrix shortcut for a 4-point DFT convolution

Both operations are matrix products, and in an exam a matrix is faster and harder to get wrong. For the
DFT, X = W x with

```text
W = [ 1   1   1   1 ]        x = {1,1,2,1}  ->  W x = {5, -1, 1, -1}
    [ 1  -j  -1   j ]
    [ 1  -1   1  -1 ]
    [ 1   j  -1  -j ]
```

For the circular convolution, y = C x with C the **circulant** matrix built from h (each row is the
previous row shifted right, with the wrap):

```text
C = [ h0 h3 h2 h1 ]   = [ 1  0  3  2 ]        C x = {9, 7, 9, 11}   for TT2 Q3
    [ h1 h0 h3 h2 ]     [ 2  1  0  3 ]
    [ h2 h1 h0 h3 ]     [ 3  2  1  0 ]
    [ h3 h2 h1 h0 ]     [ 0  3  2  1 ]
```

Row 0 alone: 1·1 + 0·2 + 3·2 + 2·1 = 9 ✓. If you can write those two matrices, you can answer any
circular-convolution question in the paper in about two minutes.

---

## §4 When circular convolution equals linear convolution (final Q4h)

**The rule, stated exactly:**

```text
circular convolution (length N)  ==  linear convolution   if and only if  N >= L + M - 1
where L = len(x), M = len(h)
```

**Why:** the linear convolution has L + M − 1 samples. If N is smaller, the samples that fall past index
N−1 wrap around and add onto the first samples — "time-domain aliasing". Quote the condition, then show it:

- TT2 Q3: L = 4, M = 3 → N ≥ 6. The linear convolution is **{1, 4, 9, 11, 8, 3}** (six samples), and the
  4-point circular answer {9, 7, 9, 11} is obtained from it by folding the last two samples back:
  y[0] = 1 + 8 = 9 ✓ and y[1] = 4 + 3 = 7 ✓. That fold *is* the "graphical illustration" the question asks
  for. At N = 6 the checker reproduces {1, 4, 9, 11, 8, 3} exactly.
- Final Q3c: L = M = 4 → N ≥ 7 for linearity, but the question explicitly asks for the **circular** result
  at N = 4, so {6, 6, 6, 7} is the right answer. The linear convolution is {1, 3, 5, 7, 5, 3, 1} (seven
  samples), and folding the samples from index 4 up back to the start gives
  y[0] = 1 + 5 = 6, y[1] = 3 + 3 = 6, y[2] = 5 + 1 = 6, y[3] = 7 ✓ — a second, independent confirmation of
  {6, 6, 6, 7} (machine-checked, and note the check that both linear convolutions sum to the product of the
  sample sums: 25 = 5×5 and 36 = 6×6).

**The "fold" is the fastest sanity check you have.** Compute the linear convolution, then wrap every sample
at index ≥ N back by N and add. It reproduces the circular result in one line and it is easy to draw.

**Practical use:** to convolve two long sequences with the FFT you must zero-pad both to at least L + M − 1;
otherwise the answer is silently wrong. That is the whole reason the number 2N ≥ L + M − 1 appears in every
FFT-convolution recipe.

---

## §5 Complexity of the DFT and the FFT (TT2 Q1, 5 marks)

**Direct DFT.** Each of the N outputs needs N complex multiplications and N−1 additions:

```text
multiplications = N^2          additions = N(N-1)          ->  O(N^2)
```

**Radix-2 FFT (Cooley–Tukey).** Split the N-point DFT into the N/2-point DFTs of the even and odd samples,
then recombine with butterflies (DIT) — or split in the frequency domain and recombine (DIF):

```text
Decomposition: the brute force N^2 has huge redundancy: the twiddles repeat (W^(k+N/2) = -W^k),
so a half-size transform can be reused twice per stage.
Stages = log2(N)      butterflies per stage = N/2      each butterfly = 1 complex multiplication
multiplications = (N/2) log2(N)                             ->  O(N log2 N)
speed-up = N^2 / ((N/2) log2 N) = 2N / log2(N)
```

**The butterfly, in words:** two inputs a, b (a from the top wire, b from the bottom) give outputs a + b and
(a − b)·W^k — one complex multiplication and two additions per butterfly, and there are N/2 butterflies in
each of the log₂N stages. Every butterfly's twiddle W^k is a root of unity, which is why the whole thing is
just repeated multiply-accumulate on the unit circle.

| N | direct DFT N² | FFT (N/2)log₂N | speed-up | notes |
|---|---|---|---|---|
| 8 | 64 | 12 | 5.3× | 3 stages × 4 butterflies |
| 16 | 256 | 32 | 8× | 4 stages × 8 butterflies |
| 32 | 1 024 | 80 | 12.8× | 5 × 16 |
| 64 | 4 096 | 192 | 21.3× | 6 × 32 |
| 1 024 | 1 048 576 | 5 120 | 204.8× | 10 × 512 |
| 4 096 | 16 777 216 | 24 576 | 682.7× | 12 × 2 048 |

All rows computed and printed by `step12_dft_fft.py`. **The exam answer:** the direct DFT is O(N²) and the FFT
is O(N log₂N); for N = 1 024 that is a 205× saving, which is what made real-time spectrum analysis and fast
convolution possible. Two caveats for the last mark: N must be a power of two for radix-2 (pad if not), and
the FFT works in place with bit-reversed ordering but computes exactly the same X[k].

---


## §6 Traps

- **Forgetting the 1/N in the IDFT.** Without it the sequence comes back N times too big.
- **Wrong sign.** Forward DFT uses e^{−j…}; the inverse uses e^{+j…}. Mixing them gives a mirrored result.
- **Not zero-padding h.** The circular convolution needs both sequences at length N; padding only x gives the
  wrong wrap. In TT2 Q3 the missing pad is the difference between {9,7,9,11} and nonsense.
- **`(n − k) mod N`, not `n − k`.** With a negative index Python wraps for you (`h[-1]` is the last sample) —
  that is convenient, but write the mod explicitly so the examiner sees you know why.
- **Assuming circular = linear.** Check N ≥ L + M − 1 *first* and always say so.
- **Quoting N² for the FFT.** The FFT is (N/2)log₂N; if you write "FFT is also N², just faster", you lose the
  whole 5-mark question.
- **Confusing k with n.** k indexes frequency bins 0…N−1, n indexes time samples 0…N−1.

---

## §7 Practice set (answers below — cover them)

1. DFT of {1, 2, 3, 4}.
2. DFT of {1, 0, 1, 0}.
3. 6-point circular convolution of {1, 2, 3} and {1, 1, 1}.
4. Magnitude of the 8-point DFT of {1, 1, 1, 1, 0, 0, 0, 0}.
5. DFT-vs-FFT cost for N = 16 and N = 32.
6. What is X[0] in words?
7. Circular convolution of {1, 2, 3, 4} with {0, 0, 1, 0} — what operation is that?
8. Smallest N so that the circular convolution of a length-5 and a length-7 sequence is linear.
9. IDFT of {4, 0, 0, 0}.
10. x has length 1 000, h has length 100. Compare direct convolution with FFT convolution.
11. Why is X[N−k] = X*[k] for real x[n], and what does it let you skip?

**Answers.**

1. {10, −2 + 2j, −2, −2 − 2j}. Check: X[0] = 10 = 1+2+3+4 ✓, and X[3] = X*[1] ✓ (machine-checked).
2. {2, 0, 2, 0}: the sequence alternates, so only even bins survive (X[0] = 2 = the sum ✓).
3. **{1, 3, 6, 5, 3, 0}** — the linear convolution is {1, 3, 6, 5, 3} (five samples) and N = 6 ≥ 5, so the
   sixth output is a zero pad (machine-checked).
4. \|X\| = {4, 2.6131, 0, 1.0824, 0, 1.0824, 0, 2.6131} — a Dirichlet shape with nulls at the even bins,
   because the sequence is a rectangle of four ones padded with four zeros (machine-checked).
5. N = 16: 256 vs 32 (8×); N = 32: 1 024 vs 80 (12.8×).
6. X[0] = Σ x[n] = N × mean(x) — the **DC component**; in the z-domain it is X(z) at z = 1.
7. A **circular shift by 2**: {3, 4, 1, 2} — the samples that pass the end of the ring reappear at the start.
8. N ≥ 5 + 7 − 1 = **11**.
9. {1, 1, 1, 1} (each output is (1/4)·4), i.e. the inverse DFT of a single nonzero bin is a constant.
10. Direct: L·M = 100 000 multiplications. FFT: pad to 2048, then 3 transforms × (2048/2)·log₂2048 = 3 × 11 264
    = 33 792 plus 2 048 multiplies for the product ≈ **35 840** — about 2.8× cheaper, and the gap grows with L.
11. Because x[n] real ⟹ X(e^{jw}) is conjugate-symmetric; sampling that on the unit circle gives
    X[N−k] = X*[k]. So you only have to compute the first N/2 + 1 bins and can mirror the rest.

Check yourself in `DSP/practice/step12_dft_fft.py` — it prints the DFT of {1,1,2,1} = {5,−1,1,−1}, the two
circular convolutions ({9,7,9,11} and {6,6,6,7}), the N = 6 linear check, and the full cost table.





