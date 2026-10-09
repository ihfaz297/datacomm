# Topic 3 — Frequency analysis of signals (Proakis Ch 4) → **TT2 question, 10 marks**

Source of truth: `Note/Mid-2 note.pdf` pages 34–53 (Proakis 4.1–4.4, Ex 4.1.2, 4.2.1) and the 2021-22
final (Q1b, 1c, 2c, 2e, 2f). Your note says the **last few slides were missing**. §8 fills that gap from
Proakis §4.4 (time reversal, Wiener–Khintchine, windowing, differentiation in frequency, Parseval).
All numbers are checked by `_mid2_verify.py`.

---

## 0. The whole topic in one table — **draw this first in any "explain" answer**

| | **Periodic** → spectrum is **discrete** | **Aperiodic** → spectrum is **continuous** |
|---|---|---|
| **Continuous time** → spectrum **aperiodic** | **CTFS**: c_k = (1/T_p)∫_{T_p} x(t)e^{−j2πkF₀t}dt; x(t) = Σ_k c_k e^{j2πkF₀t} | **CTFT**: X(F) = ∫x(t)e^{−j2πFt}dt; x(t) = ∫X(F)e^{j2πFt}dF |
| **Discrete time** → spectrum **periodic** | **DTFS**: c_k = (1/N)Σ_{n=0}^{N−1}x[n]e^{−j2πkn/N}; x[n] = Σ_{k=0}^{N−1}c_k e^{j2πkn/N} | **DTFT**: X(ω) = Σ_n x[n]e^{−jωn}; x[n] = (1/2π)∫_{2π}X(ω)e^{jωn}dω |

Read the table as a duality: **periodic in one domain ⇔ discrete in the other; discrete in one ⇔ periodic in the other.**

Vocabulary (note p.34): **frequency analysis** = resolving a signal into its frequency components. **Harmonics** = kF₀, multiples of the fundamental. **Bandwidth** = the range of frequencies where the energy or power is concentrated. **Resonance** = a system's tendency to respond with a much larger amplitude at specific frequencies.
Examples: sinusoidal carrier → periodic, ECG → aperiodic, speech → aperiodic, vibration → periodic.

---

## 1. CT Fourier series

> Any periodic x(t) with period T₀ (Ω₀ = 2π/T₀) can be written as a weighted sum of complex exponentials at the
> harmonic frequencies kΩ₀: x(t) = Σ c_k e^{jkΩ₀t}. **The weight c_k says how much of harmonic k is present.**

### 1a. Spectrum by inspection (note p.35)

| x(t) | Coefficients |
|---|---|
| cos Ω₀t = ½e^{jΩ₀t} + ½e^{−jΩ₀t} | c₁ = c₋₁ = ½, all others 0 (c₀ = 0, so no DC) |
| A cos(Ω₀t + φ) | c₁ = (A/2)e^{jφ}, c₋₁ = (A/2)e^{−jφ} = c₁* (conjugate symmetry) |

Magnitude plot: two lines of height ½ at ±Ω₀. Phase plot: +φ at +Ω₀ and −φ at −Ω₀.

### 1b. Square wave ±1 (even, period T₀, +1 for |t| < T₀/4) ★ — full derivation

> c_k = (1/T₀)∫_{−T₀/2}^{T₀/2}x(t)e^{−jkΩ₀t}dt. x(t) is **even** and sin is odd, so the sin part integrates to 0:
> c_k = (2/T₀)∫₀^{T₀/2}x(t)cos(kΩ₀t)dt = (2/T₀)[∫₀^{T₀/4}cos(kΩ₀t)dt − ∫_{T₀/4}^{T₀/2}cos(kΩ₀t)dt]
> = (2/T₀)·(1/kΩ₀)[sin(kπ/2) − 0 − (sin kπ − sin(kπ/2))] = (4 sin(kπ/2))/(kΩ₀T₀)
> **c_k = (2/(kπ))·sin(kπ/2)**   (using Ω₀T₀ = 2π)
>
> k = 0: c₀ = 0 (equal time at +1 and −1, so the average is 0)
> even k: sin(kπ/2) = 0 → c_k = 0
> odd k: c_k = ±2/(kπ), so |c_k| = 2/(π|k|): c₁ = 0.637, c₃ = −0.212, c₅ = 0.127, …
> **Only odd harmonics survive, and they fall off like 1/k.**

Variant: a 0/1 square wave (50% duty) has c₀ = **½** and c_k = (1/kπ)sin(kπ/2).

---

## 2. CT Fourier transform

> Aperiodic x(t): let T_p → ∞ in the CTFS. The lines merge into a continuous spectrum.
> **Analysis:** X(Ω) = ∫x(t)e^{−jΩt}dt  ·  **Synthesis:** x(t) = (1/2π)∫X(Ω)e^{jΩt}dΩ
> With F (Hz), Ω = 2πF: X(F) = ∫x(t)e^{−j2πFt}dt, x(t) = ∫X(F)e^{j2πFt}dF

**Dirichlet conditions** (final 1c — "briefly demonstrate"):
1. x(t) has a finite number of finite discontinuities (in any finite interval / one period).
2. x(t) has a finite number of maxima and minima.
3. x(t) is absolutely integrable: ∫|x(t)|dt < ∞ (over one period, for the CTFS).
Sufficient, not necessary. Then the series or transform converges to x(t), and to the midpoint at a jump.

### 2a. Rectangular pulse → sinc (Ex 4.1.2) ★

> x(t) = A for |t| < τ/2, 0 otherwise. It is aperiodic and satisfies Dirichlet.
> X(Ω) = ∫_{−τ/2}^{τ/2}Ae^{−jΩt}dt = (A/(−jΩ))[e^{−jΩτ/2} − e^{jΩτ/2}] = **2A sin(Ωτ/2)/Ω**
> In F: X(F) = Aτ·sin(πFτ)/(πFτ) = **Aτ·sinc(Fτ)**
> X(0) = Aτ, the area of the pulse. Zeros at F = ±1/τ, ±2/τ, … (Ω = 2π/τ, …)
> **A wider pulse gives a narrower sinc, and vice versa** (time–bandwidth trade-off).

### 2b. Intuition, duality, magnitude vs phase (note p.38–39)

- x(t) = (1/2π)∫X(Ω)e^{jΩt}dΩ: **X(Ω) is the weight that frequency Ω carries in the reconstruction sum.** One dominant |X| means x(t) looks like an almost clean sinusoid at that frequency. A spread-out |X| means no clean tone.
- **Duality:** the two formulas are almost the same with t and Ω swapped. Rect ↔ sinc, sinc ↔ rect, convolution ↔ multiplication, multiplication ↔ convolution.
- **Phase carries most of the information.** Magnitude tells *how much* of each frequency there is. Phase tells *when* each component peaks relative to the others. Keep the magnitude and scramble the phase, and every recognisable structure is destroyed. So a filter should preserve phase relationships, which is why **linear-phase filters** are used: they delay every frequency by the same amount.

---

## 3. DT Fourier series (periodic sequences)

> x[n] = x[n+N]. **Synthesis:** x[n] = Σ_{k=0}^{N−1}c_k e^{j2πkn/N}  ·  **Analysis:** c_k = (1/N)Σ_{n=0}^{N−1}x[n]e^{−j2πkn/N}
> c_{k+N} = c_k: the spectrum is periodic with period N, so only N distinct coefficients exist.
> For sampling rate F_s, k = 0…N−1 covers 0 ≤ F < F_s (F_k = kF_s/N).

### 3a. Ex 4.2.1 ★ — determine the spectra

**(a) x[n] = cos(√2·πn):** ω₀ = √2π, so f₀ = ω₀/2π = 1/√2, which is **irrational**. A DT sinusoid is periodic only if f₀ = k/N is rational, so **this signal is not periodic** and has no DTFS. Its spectrum is a single frequency component at ω = ±√2π (within −π…π: ±(2 − √2)π, because it aliases).

**(b) x[n] = cos(πn/3):** f₀ = 1/6, so **N = 6**.
> cos(πn/3) = cos(2πn/6) = ½e^{j2πn/6} + ½e^{−j2πn/6}, and e^{−j2πn/6} = e^{j2π(5)n/6}
> Match with Σc_k e^{j2πkn/6}: **c₁ = c₅ = ½, c₀ = c₂ = c₃ = c₄ = 0**   (checked with an FFT)

**(c) x[n] = {1, 1, 0, 0} periodic, N = 4:**
> c_k = ¼(1 + e^{−jπk/2}) → **c₀ = ½, c₁ = ¼(1 − j), c₂ = 0, c₃ = ¼(1 + j)**   (checked)

### 3b. DTFS of a periodic rectangular pulse train (note p.43) ★

> One period: x[n] = 1 for −N₁ ≤ n ≤ N₁ (2N₁+1 ones), 0 elsewhere.
> c_k = (1/N)Σ_{n=−N₁}^{N₁}e^{−j2πkn/N}
> **k = 0, ±N, …:** c₀ = (2N₁+1)/N, the average value (DC).
> **otherwise:** geometric sum, multiply top and bottom by e^{jα/2} with α = 2πk/N:
> c_k = (1/N)·sin(α(N₁+½))/sin(α/2) = **(1/N)·sin(2πk(N₁+½)/N)/sin(πk/N)**

Check (N = 10, N₁ = 2): c₀ = 0.5, c₁ = 0.3236, c₂ = 0, c₃ = −0.1236, c₅ = 0.1 (FFT agrees). This is the discrete cousin of the sinc.

### 3c. Power density spectrum of a periodic signal (Parseval, DT periodic)

> P_x = (1/N)Σ_{n=0}^{N−1}|x[n]|² = (1/N)Σ x[n]x*[n]. Substitute x*[n] = Σc_k*e^{−j2πkn/N}:
> = Σ_k c_k*·[(1/N)Σ_n x[n]e^{−j2πkn/N}] = Σ_k c_k*c_k
> **P_x = Σ_{k=0}^{N−1}|c_k|²**: the total power is the sum of the powers in each harmonic.
> |c_k|² vs k is the **power density spectrum**. For real x[n], c_k* = c_{−k} = c_{N−k}, so |c_k| is symmetric and you only need k = 0…N/2.

Check: the N = 10 pulse train has P = 5/10 = 0.5 = Σ|c_k|² ✔.

---

## 4. DTFT (aperiodic sequences)

> **Analysis:** X(ω) = Σ_{n=−∞}^{∞}x[n]e^{−jωn}  ·  **Synthesis:** x[n] = (1/2π)∫_{2π}X(ω)e^{jωn}dω
> **Always periodic with 2π**: X(ω+2π) = X(ω), because e^{−j2πn} = 1.
> Converges if Σ|x[n]| < ∞ (absolutely summable). The spectrum is continuous.

### 4a. Final 2c ★ — DTFT of x[n] = aⁿu[n], |a| < 1

> X(ω) = Σ_{n=0}^{∞}(ae^{−jω})ⁿ = **1/(1 − ae^{−jω})**   (|ae^{−jω}| = |a| < 1, so it converges)
> |X(ω)|² = 1/(1 − 2a cos ω + a²)   (this is the energy density spectrum S_xx(ω))
> a = 0.5: S_xx(0) = 4, S_xx(π) = 0.444, so the energy sits at low frequency: a **low-pass signal**.
> (For a < 0 it flips to high-pass.)

### 4b. Final 2e ★ — x[n] = aⁿ for 0 ≤ n ≤ M−1 (hint: time shift g[n−n₀] ↔ e^{−jωn₀}G)

> Route 1 (direct): X(ω) = Σ_{n=0}^{M−1}(ae^{−jω})ⁿ = **(1 − aᴹe^{−jωM})/(1 − ae^{−jω})**
> Route 2 (the hint): x[n] = aⁿu[n] − aᴹ·a^{n−M}u[n−M] → X = 1/(1−ae^{−jω}) − aᴹe^{−jωM}/(1−ae^{−jω}). Same answer, and it uses the shift theorem as the question wants.

### 4c. Rectangular sequence (Proakis Ex 4.2.3) — x[n] = A for 0 ≤ n ≤ L−1

> X(ω) = A(1 − e^{−jωL})/(1 − e^{−jω}) = **A·e^{−jω(L−1)/2}·sin(ωL/2)/sin(ω/2)**
> |X(0)| = AL; zeros at ω = 2πk/L. This is the moving-average shape (topic 1 §5) and the discrete "sinc".

### 4d. Energy density spectrum and Parseval (aperiodic)

> E_x = Σ|x[n]|² = Σx[n]x*[n] = Σx[n]·(1/2π)∫X*(ω)e^{−jωn}dω = (1/2π)∫X*(ω)[Σx[n]e^{−jωn}]dω
> **E_x = Σ|x[n]|² = (1/2π)∫_{−π}^{π}|X(ω)|²dω**, and **S_xx(ω) = |X(ω)|²** is the energy density spectrum:
> how much energy sits in each small slice of frequency.

**Final 2f (CT Parseval) — x_a(t) = e^{−αt}u(t), α = 0.6, find the energy:**
> X(F) = 1/(α + j2πF), |X(F)|² = 1/(α² + 4π²F²)
> E = ∫|x(t)|²dt = ∫₀^∞e^{−2αt}dt = **1/(2α) = 1/1.2 = 0.8333 J** = ∫|X(F)|²dF (Parseval says both sides match)
> Checked numerically: 0.83333.

**Final 1b — x[n] = (−1)ⁿ: energy and power:**
> |x[n]|² = 1 for every n → E = Σ1 = **∞** (not an energy signal)
> P = lim (1/(2N+1))Σ_{−N}^{N}1 = **1** → a **power signal**. Spectrally it is all at ω = π (the highest DT frequency), because (−1)ⁿ = cos πn.

### 4e. Symmetry for real signals (note p.48, 51)

> X(ω) = Σx[n]cos ωn − jΣx[n]sin ωn = X_R(ω) + jX_I(ω)
> cos is even and sin is odd ⇒ **X_R(−ω) = X_R(ω)** (even), **X_I(−ω) = −X_I(ω)** (odd): *Hermitian symmetry*, X(−ω) = X*(ω)
> ⇒ **|X(−ω)| = |X(ω)|** (even magnitude), **∠X(−ω) = −∠X(ω)** (odd phase), S_xx(−ω) = S_xx(ω)
> ⇒ for real signals only 0 ≤ ω ≤ π (0 ≤ F ≤ F_s/2) is needed. This halves the computation.

---

## 5. Fourier transform ↔ z-transform (note p.49)

> X(z) = Σx[n]z^{−n}, ROC r₂ < |z| < r₁. Put z = re^{jω}: X(z)|_{z=re^{jω}} = Σ[x[n]r^{−n}]e^{−jωn}
> = the DTFT of x[n]r^{−n}. If the ROC contains |z| = 1, set r = 1:
> **X(ω) = X(z)|_{z=e^{jω}}: the Fourier transform is the z-transform evaluated on the unit circle.**
> If the ROC doesn't include the unit circle (e.g. 2ⁿu[n]), the DTFT doesn't exist but X(z) does.

---

## 6. Frequency-domain classification: bandwidth (note p.49)

| Class | Energy concentrated | Example |
|---|---|---|
| Low-frequency | around ω = 0 (F = 0) | slow wave, DC voltage, ECG |
| High-frequency | near ω = π (F = F_s/2) | (−1)ⁿ, edges |
| Medium / band-pass | somewhere in between | a radio station |

**Bandwidth** = F₂ − F₁, the range of frequencies holding (say) 95% of the energy.
- **Narrowband**: F₂ − F₁ ≪ (F₁+F₂)/2, a thin spike.
- **Wideband**: a broad spread.
- **Bandlimited**: X(F) = 0 for |F| > B. A signal can't be both bandlimited and time-limited.

---

## 7. Properties of the DTFT — the table (note p.50–53) ★

| # | Property | x[n] | X(ω) |
|---|---|---|---|
| 1 | Linearity | a₁x₁ + a₂x₂ | a₁X₁ + a₂X₂ |
| 2 | Time shift | x[n−k] | e^{−jωk}X(ω) → **a shift changes only the phase** |
| 3 | Frequency shift | e^{jω₀n}x[n] | X(ω − ω₀) |
| 4 | Modulation | x[n]cos ω₀n | ½[X(ω−ω₀) + X(ω+ω₀)] |
| 5 | Convolution | x₁ ⊛ x₂ | X₁(ω)X₂(ω) |
| 6 | Correlation | r_{x₁x₂}[m] = Σx₁[n]x₂[n−m] | S_{x₁x₂}(ω) = X₁(ω)X₂(−ω) |
| 7 | Symmetry (real x) | x real | X(−ω) = X*(ω) |
| 8 | Periodicity | — | X(ω+2π) = X(ω) |

Proofs to have ready (two lines each):
- **Time shift:** Σx[n−k]e^{−jωn}; let m = n−k → e^{−jωk}Σx[m]e^{−jωm}.
- **Frequency shift:** Σe^{jω₀n}x[n]e^{−jωn} = Σx[n]e^{−j(ω−ω₀)n} = X(ω−ω₀).
- **Modulation:** cos ω₀n = ½(e^{jω₀n} + e^{−jω₀n}), then apply the frequency shift twice.
- **Correlation:** S(ω) = Σ_m Σ_n x₁[n]x₂[n−m]e^{−jωm}; let k = n−m → Σx₁[n]e^{−jωn}·Σx₂[k]e^{+jωk} = X₁(ω)X₂(−ω).

## 8. The properties from the missing slides (Proakis §4.4) — fill-in

| # | Property | x[n] | X(ω) |
|---|---|---|---|
| 9 | Time reversal | x[−n] | X(−ω) |
| 10 | **Wiener–Khintchine** | r_xx[m] (autocorrelation) | **S_xx(ω) = \|X(ω)\|²**: the energy density spectrum is the FT of the autocorrelation |
| 11 | Multiplication (windowing) | x₁[n]x₂[n] | (1/2π)∫X₁(λ)X₂(ω−λ)dλ (periodic convolution) |
| 12 | Differentiation in frequency | n·x[n] | j·dX(ω)/dω |
| 13 | Parseval | Σx₁[n]x₂*[n] | (1/2π)∫X₁(ω)X₂*(ω)dω |
| 14 | Conjugation | x*[n] | X*(−ω) |

- **Time reversal:** Σx[−n]e^{−jωn}; let l = −n → Σx[l]e^{−j(−ω)l} = X(−ω).
- **Wiener–Khintchine:** autocorrelation is row 6 with x₂ = x₁, so S_xx = X(ω)X(−ω) = X(ω)X*(ω) = |X(ω)|² for real x. Write *"the autocorrelation and the energy density spectrum form a Fourier pair."*
- **Windowing:** truncating a signal (multiplying by a window) **convolves** its spectrum with the window's spectrum. That's why truncation smears and ripples the spectrum (Gibbs).
- **Differentiation in freq:** d/dω Σx[n]e^{−jωn} = Σ(−jn)x[n]e^{−jωn} ⇒ nx[n] ↔ j dX/dω.

---

## 9. Ten-minute self-test

| # | Question | Answer |
|---|---|---|
| 1 | Which transform for: CT periodic / CT aperiodic / DT periodic / DT aperiodic? | CTFS / CTFT / DTFS / DTFT |
| 2 | Square wave ±1 coefficients | c_k = (2/kπ)sin(kπ/2): odd harmonics only, ∝ 1/k, c₀ = 0 |
| 3 | FT of a rect pulse (A, width τ) | Aτ sinc(Fτ); zeros at F = k/τ |
| 4 | Three Dirichlet conditions | finite discontinuities, finite max/min, absolutely integrable |
| 5 | Is cos(√2πn) periodic? | No, f₀ = 1/√2 is irrational |
| 6 | DTFS of cos(πn/3) | N = 6, c₁ = c₅ = ½, the rest 0 |
| 7 | DTFS of {1,1,0,0} | ½, (1−j)/4, 0, (1+j)/4 |
| 8 | Power of a periodic signal from c_k | P = Σ\|c_k\|² |
| 9 | DTFT of aⁿu[n] and its S_xx | 1/(1−ae^{−jω}); 1/(1−2a cos ω+a²) |
| 10 | Energy of e^{−0.6t}u(t) | 1/(2·0.6) = 0.8333 |
| 11 | E and P of (−1)ⁿ | E = ∞, P = 1 (power signal) |
| 12 | Real x[n]: symmetry of \|X\| and ∠X | even, odd |
| 13 | DTFT vs z-transform | X(ω) = X(z) at z = e^{jω}, if the ROC contains the unit circle |
| 14 | x[n]cos ω₀n ↔ ? | ½[X(ω−ω₀) + X(ω+ω₀)] |
| 15 | Wiener–Khintchine | r_xx[m] ↔ S_xx(ω) = \|X(ω)\|² |
