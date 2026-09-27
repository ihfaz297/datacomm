# TT2 battle plan — transforms and discrete-time systems

CSE 325 Term Test 2. **30 minutes, 20 marks, 2 questions (Q2 and Q3 of the paper), each 10 marks.**
Quiz 2 is the third question (Q1) and it comes from the same three topics, so nothing here is wasted.

Every number in this file was produced by `DSP/practice/step10_dtft.py` … `step13_fir_window.py`
and is logged in `.scratch/verify_log.txt` — all checkers PASS on 27 Sep 2026. Nothing here is copied
out of a slide and hoped for.

Read this file for the map, then open the tutorial for the topic you are weak on:

| Tutorial | Covers | TT2 question |
|---|---|---|
| `10-dtft-worked-tutorial.md` | DTFT, H(e^jw), moving average, steady state | topic 1 (also quiz) |
| `11-ztransform-worked-tutorial.md` | z-transform, ROC, poles/zeros | topic 2 |
| `12-dft-circular-conv-tutorial.md` | DFT, IDFT, circular convolution, FFT cost | **Q1 and Q3 — the 2021-22 paper + TT2 Q3** |
| `13-fir-window-design-tutorial.md` | FIR lowpass by the window method | **Q2 and Q4 — TT2 Q2, Q4** |
| `lab-doomsday.md` | lab-exam plotting drills (steps 1–9) | not TT2, keep it for the lab |

---

## 1. The four questions you will be asked (verbatim from the TT2 photo)

The paper in `DSP/TT/TT2.HEIC` is a real CSE 325 Term Test 2. Questions 2 and 3 of that paper are the
TT2; Q1 is the quiz. Notice how little of it is "calculate" and how much is "explain" — **three of the
four answers are prose with a table or a number next to it.** Marks live in the vocabulary.

| Q | Wording | Marks | Answer lives in |
|---|---|---|---|
| 1 | Explain the computational complexity of DFT and FFT | 5 | §5 of `12-dft-circular-conv-tutorial.md` |
| 2 | Discuss the design of FIR low-pass filters using the window method | 5 | §2–§5 of `13-fir-window-design-tutorial.md` |
| 3 | Determine y(n) that results from the use of a four-point DFT for x(n) = {1,2,2,1} and h(n) = {1,2,3} | 5 | §3 of `12-dft-circular-conv-tutorial.md` |
| 4 | Discuss how each parameter affects the overall performance of the filter design: roll-off, stop-band attenuation, ripple | 5 | §6–§8 of `13-fir-window-design-tutorial.md` |

**The 30-second version of Q3**, so you can sanity-check yourself in the hall: pad h to four samples,
the four output samples are `{9, 7, 9, 11}`, and `{1,4,9,11,8,3}` is what the *linear* convolution
would have given. Verified in `step12_dft_fft.py`.

---

## 2. Syllabus → what it actually means → where to look

Quoted from `DSP/midterm-2.txt.txt`, then translated:

| Syllabus line (Mitra 4.8.x / Proakis) | Plain English | Covered by |
|---|---|---|
| 4.8 Frequency domain representation of LTI DTS | the DTFT is how you see a signal's frequencies | `step10`, tutorial 10 §1 |
| 4.8.1 Frequency response | H(e^jw) is the DTFT of h[n] | `step10`, tutorial 10 §2 |
| 4.8.2 Frequency-domain characterisation | sinusoid in → same sinusoid out, amplitude × \|H\|, phase + ∠H | `step10`, tutorial 10 §2 |
| 4.8.3 Frequency response of LTI DTS | rational H, poles decide the shape | `step11`, tutorial 11 §4 |
| 4.8.4 Frequency response of the moving average filter | H = sin(wM/2)/(M sin(w/2)) · e^-jw(M-1)/2 | `step10`, tutorial 10 §3 |
| 4.8.5 Steady-state and transient response | y = y_steady + y_transient, transient dies like α^n | tutorial 10 §5 |
| 4.8.6 Response to a causal exponential | x[n] = α^n u[n] → 1/(1 − αe^-jw) | `step10`, tutorial 10 §4 |
| 4.8.7 The concept of filtering | an LTI system *is* a filter, H(e^jw) is its shape | tutorial 13 §1 |
| Ch 3 Proakis: the z-transform and LTI analysis | X(z), ROC, poles/zeros, transfer function | `step11`, tutorial 11 |
| Ch 4 Proakis: frequency analysis of signals | DTFT properties, Parseval, energy/power | `step10`, tutorial 10 §4, §6 |
| Ch 7 Proakis + FFT, DIT, DIF | DFT, IDFT, circular convolution, N² vs (N/2)log₂N | `step12`, tutorial 12 |

Projection of what Q1 (the quiz) will be: it is always the first syllabus bullet of the list, and the
real paper asked it as **"Explain the computational complexity of DFT and FFT"**. Read the cost table in
§4 of tutorial 12 until you can write it from memory — 4 rows, 4 numbers.

---

## 3. Gap table — what the drills you already finished do *not* give you

`lab-doomsday.md` and `step1…step9` are the lab-exam drills (CT signals, sampling, aliasing,
quantization, DT sequences, convolution, correlation, moving average, spectrum). They are **plotting
drills**. TT2 has no plotting at all. These are the holes, and they are filled by `step10…step13`:

| TT2 needs | In steps 1–9? | New drill |
|---|---|---|
| DTFT / H(e^jw) of a system | no — step9 only does `np.fft.rfft` of a waveform | `step10_dtft.py` |
| z-transform, ROC, poles/zeros | no | `step11_ztransform.py` |
| DFT of an N-point sequence by hand | no — step9 uses FFT as a black box | `step12_dft_fft.py` |
| circular convolution, mod-N wrap | partially — step6 is *linear* convolution | `step12_dft_fft.py` |
| FFT cost numbers | no | `step12_dft_fft.py` |
| FIR window design, attenuation/ripple | partially — step8 is the MA filter only | `step13_fir_window.py` |

Run them in this order and stop when one prints PASS:

```bash
python DSP/practice/step10_dtft.py        # -> prints null at 2pi/M, delay (M-1)/2
python DSP/practice/step11_ztransform.py  # -> prints the SymPy sums and the ROC
python DSP/practice/step12_dft_fft.py     # -> prints {9,7,9,11} and the cost table
python DSP/practice/step13_fir_window.py  # -> prints 21/44/53/75 dB
```

Each file has `# TODO` lines; the checker at the bottom prints PASS or FAIL with the expected number.
The teaching version of each file is the matching tutorial markdown.

---

## 4. Formula sheet (the only sheet you need to reproduce in the hall)

### 4.1 Transforms — one line each

| Transform | Definition | Note |
|---|---|---|
| DTFT | X(e^jw) = Σ_{n=−∞}^{∞} x[n] e^{−jwn} | periodic in w with 2π |
| Inverse DTFT | x[n] = (1/2π) ∫_{−π}^{π} X(e^jw) e^{jwn} dw | |
| z-transform | X(z) = Σ_{n} x[n] z^{−n} | z = r e^{jw}; **the ROC is part of the answer** |
| DFT | X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0…N−1 | \|X[k]\| symmetric about N/2 |
| IDFT | x[n] = (1/N) Σ_{k=0}^{N−1} X[k] e^{+j2πkn/N} | **1/N and the + sign** |
| Link | X[k] = X(z) at z = e^{j2πk/N} | DFT = z-transform sampled on the unit circle |
| Link | DTFT = z-transform with z = e^{jw} | DTFT is the z-transform *on* the unit circle |

### 4.2 z-transform pairs with their ROC (topic 2, Q6 of the final paper)

| x[n] | X(z) | ROC |
|---|---|---|
| δ[n] | 1 | all z |
| u[n] | 1/(1 − z^{−1}) | \|z\| > 1 |
| αⁿ u[n] | 1/(1 − αz^{−1}) | \|z\| > \|α\| (right-sided, causal) |
| −αⁿ u[−n−1] | 1/(1 − αz^{−1}) | \|z\| < \|α\| (left-sided) — **same X(z), different ROC** |
| αⁿ, 0 ≤ n ≤ M−1 | (1 − α^M z^{−M})/(1 − αz^{−1}) | \|z\| > 0; M−1 poles at 0, zeros at αe^{j2πk/M}, k = 1…M−1 |
| αⁿ u[n] + bⁿ u[−n−1] | (α − b)z^{−1} / ((1 − αz^{−1})(1 − bz^{−1})) | annulus \|α\| < \|z\| < \|b\|, **empty if \|b\| ≤ \|α\|** |
| n αⁿ u[n] | αz^{−1}/(1 − αz^{−1})² | \|z\| > \|α\| |
| cos(w₀n) u[n] | (1 − z^{−1}cos w₀)/(1 − 2z^{−1}cos w₀ + z^{−2}) | \|z\| > 1 |

Checked numerically: the two-sided row at α = 0.5, b = 2, z = 1.2 gives **3.214286** from the closed form
and from a 400-term double sum (`step11_ztransform.py`). Its ROC is the annulus **0.5 < |z| < 2**, so
1.2 is inside while 0.3 and 3.0 are outside — all three are tested.

### 4.3 DTFT pairs you actually need (topic 1 / final Q2, Q5b)

| x[n] | X(e^jw) |
|---|---|
| αⁿ u[n], \|α\| < 1 | 1/(1 − αe^{−jw}), \|X\| = 1/√(1 − 2α cos w + α²) (verified to 1e-12) |
| δ[n] | 1 |
| αⁿ, 0 ≤ n ≤ M−1 | (1 − α^M e^{−jwM})/(1 − αe^{−jw}) |
| M-point MA: 1/M, 0 ≤ n ≤ M−1 | sin(wM/2)/(M sin(w/2)) · e^{−jw(M−1)/2} |
| 1, −M ≤ n ≤ M | sin(w(M+½))/sin(w/2) (Dirichlet kernel) |

Properties that carry marks: linearity, time shift g[n−n₀] ↔ e^{−jwn₀}G(e^jw), convolution
y = x ∗ h ↔ Y = X·H, Parseval Σ|x[n]|² = (1/2π)∫|X(e^jw)|²dw.

### 4.4 LTI systems in the frequency domain (topic 1)

- H(e^jw) = DTFT of h[n] = Y(e^jw)/X(e^jw).
- **Sinusoid in, sinusoid out:** x[n] = A cos(w₀n + θ) → y[n] = A\|H(e^{jw₀})\| cos(w₀n + θ + ∠H(e^{jw₀})).
- Moving average (4.8.4): \|H(0)\| = 1, first null at **w = 2π/M**, phase = −w(M−1)/2, so **linear phase =
  a pure delay of (M−1)/2 samples** (measured 2.0 for M = 5). Its sidelobes are only ~13 dB down, so it is
  a smoother, not a real lowpass filter.
- Steady state vs transient (4.8.5): the natural (transient) part decays like αⁿ when |α| < 1; the forced
  (steady-state) part is the same sinusoid with amplitude \|H\|. In a long record only the steady-state
  term is left — that is the whole answer if he asks about steady-state response.
- Pole radius controls the sharpness/ringing; poles inside the unit circle → stable.

### 4.5 FIR lowpass by the window method (TT2 Q2, Q4; final Q2b, Q3a)

```text
1. ideal brick wall, CENTRED at M/2 so the FIR comes out causal:
     h_d[n] = sin(wc(n - M/2)) / (pi (n - M/2)),  n = 0..M,   h_d[M/2] = wc/pi   (the 0/0 sample)
2. choose a window w[n] of the same length M+1
3. multiply:  h[n] = h_d[n] * w[n]          <- this IS the filter
4. check:     H(e^jw) = DTFT of h[n],  |H| against the spec
```

| Window | w[n], n = 0…M | Stopband att. (measured, M = 30) | Transition ≈ | In-band ripple (measured) |
|---|---|---|---|---|
| Rectangular | 1 | **21.2 dB** | 1.8π/M | **0.63 dB** (Gibbs) |
| Hann | 0.5 − 0.5cos(2πn/M) | **44.0 dB** | 6.2π/M | 0.024 dB |
| Hamming | 0.54 − 0.46cos(2πn/M) | **53.6 dB** | 6.6π/M | 0.033 dB |
| Blackman | 0.42 − 0.5cos(2πn/M) + 0.08cos(4πn/M) | **75.2 dB** | 11π/M | 0.003 dB |

Measured widths at M = 30, wc = 0.4π: rect 0.0598π, Hann 0.1295π, Hamming 0.1217π, Blackman 0.1585π.
The order law, measured: Hamming M = 30 → transition 0.1217π, M = 60 → **0.0610π (halved)** while the
attenuation moved 53.56 → 53.72 dB (**did not move**).

The one sentence that earns the design marks: **the window shape fixes the stop-band attenuation and the
ripple; the order M fixes the transition width (roll-off). Bigger M widens the filter and adds delay but
does nothing for the attenuation.**

### 4.6 Complexity (TT2 Q1)

| Operation | Complex multiplications | Order |
|---|---|---|
| Direct DFT, N points | N² | O(N²) |
| Radix-2 FFT, DIT or DIF | (N/2) log₂N | O(N log₂N) |
| Speed-up | 2N / log₂N | |

| N | N² | (N/2)log₂N | Speed-up (measured) |
|---|---|---|---|
| 8 | 64 | 12 | 5.3× |
| 64 | 4 096 | 192 | 21.3× |
| 1 024 | 1 048 576 | 5 120 | 204.8× |
| 4 096 | 16 777 216 | 24 576 | 682.7× |

---

## 5. Model answers to the four TT2 questions

Write these as they are. Each is about a third of a page — that is what a 10-mark answer looks like when
half the marks are for the wording.

### Q1 (5 marks) — Explain the computational complexity of DFT and FFT

The N-point DFT, X[k] = Σ_{n=0}^{N−1} x[n]e^{−j2πkn/N}, is N sums of N terms: **N² complex
multiplications and N(N−1) complex additions, i.e. O(N²)**. Every output bin costs a full pass over the
input and the twiddle factors are recomputed each time.

The FFT (Cooley–Tukey, radix-2) removes that waste by *decomposing*: an N-point DFT is split into two
N/2-point DFTs (even samples and odd samples, DIT) recombined with butterflies. log₂N such stages, each
with N/2 butterflies, gives **(N/2) log₂N complex multiplications, i.e. O(N log₂N)**. The saving is
`N² / ((N/2)log₂N) = 2N/log₂N`:

| N | direct N² | FFT (N/2)log₂N | gain |
|---|---|---|---|
| 8 | 64 | 12 | 5.3× |
| 64 | 4 096 | 192 | 21.3× |
| 1 024 | 1 048 576 | 5 120 | 204.8× |
| 4 096 | 16 777 216 | 24 576 | 682.7× |

The gain grows with N, which is why the FFT made spectrum analysis practical: an N = 1 024 transform
drops from about a million multiplications to 5 120. The price is that N must be a power of two (or you
pad, or use a mixed-radix version) and the algorithm is recursive instead of a straight definition. DIT
and DIF are the two orderings of the same idea. Every row above was computed by `step12_dft_fft.py`.

### Q2 (5 marks) — Design of FIR low-pass filters using the window method

The window method designs an FIR by truncating the *ideal* (brick-wall) impulse response with a taper:

1. **Ideal response.** The ideal LPF h_d[n] = (sin wc n)/(πn) is infinite and non-causal. Shift it by M/2
   to make it causal: h_d[n] = sin(wc(n − M/2))/(π(n − M/2)), n = 0…M, with h_d[M/2] = wc/π (the 0/0
   sample). The shift only changes phase (linear phase, delay M/2); the response is still infinite, so it
   cannot be built as it stands.
2. **Truncate with a window.** Multiply by a finite window of the same length: h[n] = h_d[n]·w[n],
   n = 0…M. Plain truncation is the rectangular window; better windows taper the ends.
3. **Why the taper matters.** Truncation is multiplication by a rectangle in time, i.e. **convolution of
   the ideal response with the window's spectrum**. The rectangular window's highest sidelobe is only
   −13 dB, so the design reaches just 21 dB of stopband attenuation and rings in the passband (Gibbs).
   Cosine-sum windows have far smaller sidelobes, so they filter much better.
4. **The trade-off.** Narrowing the window's mainlobe (better attenuation) widens the transition band.
   Measured at 31 taps, wc = 0.4π: rectangular 21.2 dB, Hann 44.0, Hamming 53.6, Blackman 75.2 dB, with
   transitions 0.06π, 0.13π, 0.12π, 0.16π.
5. **Procedure.** Choose wc to place the −6 dB point, choose the window to reach the required attenuation,
   then raise the order M until the transition fits the spec — transition ≈ c/M, so doubling M halves it
   (measured on Hamming: 0.1217π at M = 30 → 0.0610π at M = 60, attenuation unchanged at 53.6 dB). Finish
   by checking H(e^jw) = DTFT of h[n]. The result is exactly linear phase (measured error 1e-15), has no
   stability issue (FIR), and the price of a sharper filter is simply more taps and more delay.

### Q3 (5 marks) — Four-point DFT result for x(n) = {1, 2, 2, 1} and h(n) = {1, 2, 3}

Zero-pad h to four samples: h = {1, 2, 3, 0}. A 4-point DFT gives a 4-point (circular) output. Both
routes give the same numbers.

**Route A — circular convolution with the wrap, y[n] = Σ_k x[k]h[(n−k) mod 4]:**

| n | k = 0 | k = 1 | k = 2 | k = 3 | y[n] |
|---|---|---|---|---|---|
| 0 | x[0]h[0] = 1·1 = 1 | x[1]h[3] = 2·0 = 0 | x[2]h[2] = 2·3 = 6 | x[3]h[1] = 1·2 = 2 | **9** |
| 1 | x[0]h[1] = 1·2 = 2 | x[1]h[0] = 2·1 = 2 | x[2]h[3] = 2·0 = 0 | x[3]h[2] = 1·3 = 3 | **7** |
| 2 | x[0]h[2] = 1·3 = 3 | x[1]h[1] = 2·2 = 4 | x[2]h[0] = 2·1 = 2 | x[3]h[3] = 1·0 = 0 | **9** |
| 3 | x[0]h[3] = 1·0 = 0 | x[1]h[2] = 2·3 = 6 | x[2]h[1] = 2·2 = 4 | x[3]h[0] = 1·1 = 1 | **11** |

**y(n) = {9, 7, 9, 11}.**

**Route B — through the DFT product**, which is what the wording "results from the use of a four-point
DFT" literally asks for: X[k] = DFT{1,2,2,1} = {6, −1−j, 0, −1+j}; padded H[k] = DFT{1,2,3,0} =
{6, −2−2j, 2, −2+2j}; the pointwise product is Y[k] = {36, 4j, 0, −4j}; the inverse DFT of that is
{9, 7, 9, 11}. Both routes were machine-checked in `step12_dft_fft.py`.

Add the discussion line for the remaining marks: the *linear* convolution of these two sequences is
{1, 4, 9, 11, 8, 3}, which has six samples. Since N = 4 < len(x) + len(h) − 1 = 6, the last two samples
(8 and 3) **alias around** and add onto y[0] and y[1]. Choosing N ≥ 6 removes the wrap-around and the
circular result becomes the linear one (verified at N = 6).

### Q4 (5 marks) — What each parameter does (roll-off, stop-band attenuation, ripple)

| Parameter changed | Roll-off / transition band | Stop-band attenuation | Ripple |
|---|---|---|---|
| **Window shape** (M fixed) | the window's mainlobe width sets it. Rectangular is the narrowest — 0.0598π at M = 30 — and each smoother window pays width for its sidelobes: Hann 0.1295π, Hamming 0.1217π, Blackman 0.1585π | set *only* by the window's peak sidelobe: rectangular 21.2 dB, Hann 44.0, Hamming 53.6, Blackman 75.2 dB | smooth windows flatten the passband: rectangular 0.63 dB of Gibbs ringing vs Hann 0.024, Hamming 0.033, Blackman 0.003 dB |
| **Order M** (window fixed) | transition ≈ c/M, so doubling M halves it (Hamming 0.1217π at M = 30 → 0.0610π at M = 60) | unchanged (53.56 → 53.72 dB): attenuation is the window, not the length | worst ripple unchanged; you only get more, smaller ripples inside the same band |
| **Cut-off wc** | slides the whole transition band left/right | unchanged | unchanged |
| **Kaiser β** (extra knob) | traded against the attenuation by β | β sets it directly | β trades ripple against attenuation |

Consequences worth stating: a **narrow** transition band (sharp roll-off) needs a large M, hence a long
filter, more computation and more delay (group delay = M/2 samples); a **wide** transition band needs
fewer taps and gives a cheaper, lower-latency filter. Deep attenuation needs a smoother window, which
widens the mainlobe again — with a fixed length you cannot have all three. The window method always
produces an exactly linear-phase FIR (measured 1e-15), which is exactly why it is the standard hand
method; an ideal filter (brick wall, zero-width transition) is non-causal and of infinite length, so it
can never be realised physically.

---

## 6. The 30 minutes

| Time | Do |
|---|---|
| 0–2 min | read all three questions, write the formula you will need next to each |
| 2–8 min | Quiz/Q1: the DFT-vs-FFT table and the O(N²) → O(N log₂N) sentence. The 4-row table *is* the answer |
| 8–15 min | TT2 Q2: the 5-step window recipe plus the attenuation table. No arithmetic unless numbers are given |
| 15–22 min | TT2 Q3: the wrap table — 4 rows, 16 products, then the N ≥ L + M − 1 sentence |
| 22–28 min | TT2 Q4: the parameter table, three rows |
| 28–30 min | cross-check {9,7,9,11} against the DFT product and box the final answer |

If the numbers differ, the method does not: pad to N, wrap with mod N, then state N ≥ L + M − 1. If a
design is asked with numbers, use h_d[n] = sin(wc(n − M/2))/(π(n − M/2)) with the M/2 sample = wc/π,
multiply by the window, and quote that window's attenuation from §4.5.

---

## 7. Self-test (cover the right-hand column)

| # | Question | Answer |
|---|---|---|
| 1 | DFT of {1, 2, 1}? | {4, e^{−j2π/3}, e^{+j2π/3}} = {4, −0.5−0.866j, −0.5+0.866j} |
| 2 | 4-point circular convolution of {1,1,2,1} and {1,2,1,1}? | {6, 6, 6, 7} |
| 3 | When does circular convolution equal linear convolution? | N ≥ len(x) + len(h) − 1 |
| 4 | DTFT of αⁿu[n], and its magnitude? | 1/(1−αe^{−jw}); \|X\| = 1/√(1−2αcos w+α²) |
| 5 | First null of an M-point moving average? | w = 2π/M (1.2566 rad measured for M = 5), and \|H(0)\| = 1 |
| 6 | x[n] = A cos(w₀n) into h = {−3,6,−5,4} at w₀ = π/2? | H = 2 − 2j, so y[n] = 2.828A cos(w₀n − 45°) |
| 7 | ROC of αⁿu[n] + bⁿu[−n−1], α = 0.5, b = 2? | 0.5 < \|z\| < 2 (empty unless \|b\| > \|α\|) |
| 8 | z-transform of αⁿ, 0 ≤ n ≤ M−1, poles and zeros? | (1−α^M z^{−M})/(1−αz^{−1}); M−1 poles at z = 0, zeros at αe^{j2πk/M}, k = 1…M−1 |
| 9 | Hamming vs Hann attenuation at 31 taps? | 53.6 dB vs 44.0 dB (rectangle 21.2, Blackman 75.2) |
| 10 | FFT multiplications for N = 1 024? | 5 120, against 1 048 576 direct — 204.8× faster |
| 11 | Unit sample response of y(n) = 0.5y(n−1) + 2x(n)? | h[n] = 2(0.5)ⁿu[n], \|H(0)\| = 4 |
| 12 | Energy of x_a(t) = e^{−0.6t}u(t) by Parseval? | 1/(2α) = 0.8333 J (verified numerically) |

Anything you cannot answer from memory: §1 says which tutorial to re-read, and the matching
`DSP/practice/step1x_*.py` checker tells you whether you got it right.



