# Topic 1 — Frequency response of LTI systems (Mitra 4.8) → **Quiz Q1, 10 marks**

Source of truth: your `Note/Mid-2 note.pdf` pages 13–24 (sir's flow), Mitra §4.8 and the
exercises the note lists: **4.54, 4.56, 4.57, 4.60, 4.61, 4.63, 4.64, 4.68, 4.76**.
Every number below was checked in Python (see the end of the file).

How to use this: read a section, cover the "Write this" box, try to reproduce it on paper, then compare.

---

## 0. The whole topic in 6 lines

1. Feed e^{jωn} into an LTI system and you get **H(e^{jω})·e^{jωn}**: the same signal, scaled. So e^{jωn} is an *eigenfunction* and H(e^{jω}) is its *eigenvalue*.
2. H(e^{jω}) = Σ h[k]e^{−jωk} is the **DTFT of h[n]**, also called the frequency response.
3. Write it as |H|·e^{jθ(ω)}. |H| is the gain at that frequency and θ is the phase shift.
4. A cosine in gives a cosine out: A cos(ω₀n+φ) → **A|H(e^{jω₀})| cos(ω₀n+φ+θ(ω₀))**. That is the steady-state response.
5. If the input is switched on at n = 0 (multiplied by u[n]), you get that steady state **plus** a transient that dies out when the system is stable.
6. A filter is just |H| chosen on purpose: ≈1 where you want frequencies to pass, ≈0 where you want them removed.

---

## 1. Eigenfunction proof (4.8, 4.8.1) — the most likely "prove" part

**Write this:**

> For an LTI system, y[n] = Σ_{k=−∞}^{∞} h[k] x[n−k]. Let x[n] = e^{jωn}, −∞ < n < ∞.
>
> y[n] = Σ h[k] e^{jω(n−k)} = e^{jωn} · Σ_{k} h[k] e^{−jωk}
>
> The sum depends only on ω, not on n. Call it H(e^{jω}) = Σ_k h[k]e^{−jωk}, the **frequency response**.
>
> ∴ y[n] = H(e^{jω}) · e^{jωn}. The output is the input times a constant, so **e^{jωn} is an
> eigenfunction of every LTI system and H(e^{jω}) is the corresponding eigenvalue.**

Draw an arrow from e^{jωn} to the label "eigenfunction" and from H(e^{jω}) to "eigenvalue", the way the note does. That arrow is worth a mark.

**Mini example from the note:** if H(e^{jω}) = 2e^{−jπ/4}, then x = e^{jωn} gives y = 2e^{j(ωn−π/4)}. The amplitude goes 1 → 2, the phase goes 0 → −π/4, and **the frequency ω is unchanged**. An LTI system never creates new frequencies.

### 1a. Exercise 4.54 (in the note)

**(i) Prove z^n is an eigenfunction (z a complex constant).**
y[n] = Σ h[k] z^{n−k} = z^n Σ h[k] z^{−k} = H(z)·z^n. The sum does not depend on n, so z^n is an eigenfunction and the eigenvalue is H(z), the z-transform of h.

**(ii) Is v[n] = z^n u[n] an eigenfunction?**
y[n] = Σ h[k] z^{n−k} u[n−k] = z^n Σ_k h[k] z^{−k} u[n−k]. Now the sum **depends on n** through u[n−k], so it is not a constant. **Not an eigenfunction.**
The idea behind it: switching the input on at n = 0 is exactly what creates a transient (§5).

---

## 2. Magnitude, phase, gain in dB, symmetry (4.8.1–4.8.2)

| Quantity | Formula | Meaning |
|---|---|---|
| Rectangular form | H = H_R(ω) + jH_I(ω) | |
| Magnitude response | \|H(e^{jω})\| = √(H_R² + H_I²) | amplitude gain |
| Phase response | θ(ω) = tan⁻¹(H_I / H_R) | phase shift (watch the quadrant!) |
| Polar form | H = \|H\|·e^{jθ(ω)} | |
| Gain in dB | G(ω) = 20 log₁₀\|H(e^{jω})\| | >0 amplify, =0 no change, <0 attenuate |
| Real h[n] | H(e^{−jω}) = H*(e^{jω}) | **\|H\| is even, θ is odd** |
| Periodicity | H(e^{j(ω+2π)}) = H(e^{jω}) | only need −π ≤ ω ≤ π, and 0 ≤ ω ≤ π for real h |
| Convolution | y = h ⊛ x ⇔ Y(e^{jω}) = H(e^{jω})X(e^{jω}) | so H = Y/X |

**Exam trap:** tan⁻¹ on a calculator only gives −90°…+90°. If H_R < 0, add or subtract 180°. Example: H = −18 at ω = π has phase ±180°, not 0.

---

## 3. Sinusoidal steady-state response (4.8.2) — **a derivation sir asks**

> **Q (note p.19):** Develop an expression for the steady-state response of an LTI DTS with real h[n] to a sinusoidal input, in terms of H(e^{jω}).

**Write this:**

> Let x[n] = A cos(ω₀n + φ) = (A/2)[e^{jφ}e^{jω₀n} + e^{−jφ}e^{−jω₀n}]   (Euler).
>
> Each exponential is an eigenfunction, so
> y[n] = (A/2)[e^{jφ} H(e^{jω₀}) e^{jω₀n} + e^{−jφ} H(e^{−jω₀}) e^{−jω₀n}].
>
> h[n] is real, so H(e^{−jω₀}) = H*(e^{jω₀}). Let H(e^{jω₀}) = |H|e^{jθ}, which makes H(e^{−jω₀}) = |H|e^{−jθ}.
>
> y[n] = (A|H|/2)[e^{j(ω₀n+φ+θ)} + e^{−j(ω₀n+φ+θ)}] = **A|H(e^{jω₀})| cos(ω₀n + φ + θ(ω₀))**.
>
> Same frequency. Amplitude multiplied by |H(e^{jω₀})|. Phase shifted by θ(ω₀).

### 3a. Worked: past-paper 5c — h = {−3, 6, −5, 4}, 0 ≤ n ≤ 3, x[n] = A cos(ω₀n)

> H(e^{jω}) = Σ h[n]e^{−jωn} = **−3 + 6e^{−jω} − 5e^{−j2ω} + 4e^{−j3ω}**
>
> y[n] = A|H(e^{jω₀})| cos(ω₀n + θ(ω₀))

If sir gives a number, plug it in. All of these are checked:

| ω₀ | H(e^{jω₀}) | \|H\| | θ |
|---|---|---|---|
| 0 | 2 | 2 | 0 |
| π/4 | −1.586 − 2.071j | 2.608 | −127.4° (3rd quadrant!) |
| π/2 | 2 − 2j | 2.828 | −45° → y = 2.828A cos(πn/2 − π/4) |
| π | −18 | 18 | ±180° |

How to get π/2 by hand: e^{−jπ/2} = −j, e^{−jπ} = −1, e^{−j3π/2} = +j, so H = −3 + 6(−j) − 5(−1) + 4(j) = 2 − 2j.

### 3b. Worked: Mitra 4.68 — h[n] = (0.4)ⁿu[n], x[n] = sin(πn/4)u[n], find y_ss

> H(e^{jω}) = Σ_{n≥0} (0.4e^{−jω})ⁿ = 1/(1 − 0.4e^{−jω})   (|0.4| < 1, so the geometric series converges)
>
> At ω = π/4: e^{−jπ/4} = 1/√2 − j/√2, so
> 1 − 0.4(0.7071 − 0.7071j) = 0.71716 + j0.28284
>
> H(e^{jπ/4}) = 1/(0.71716 + j0.28284) = **1.20669 − j0.47591**
>
> |H| = **1.29715**, θ = tan⁻¹(−0.47591/1.20669) = **−21.52° = −0.3757 rad**
>
> **y_ss[n] = 1.29715 sin(πn/4 − 0.3757)**

Also note: H(e^{−jπ/4}) = 1.20669 + j0.47591 (the conjugate), with the same magnitude and phase +21.52°.
Checked: the true output at n = 50 equals the y_ss formula to 15 digits, so the transient really has died.

---

## 4. Frequency response of a general FIR, and the cascade problems

FIR: y[n] = Σ_{k=N₁}^{N₂} h[k]x[n−k] ⇒ **H(e^{jω}) = Σ_{k=N₁}^{N₂} h[k]e^{−jωk}**. It is a finite sum, so there are no convergence worries.

**DTFT shortcuts (note p.16) — memorise:**

| x[n] | X(e^{jω}) |
|---|---|
| δ[n] | 1 |
| δ[n−k] | e^{−jωk} |
| aⁿu[n], \|a\|<1 | 1/(1 − ae^{−jω}) |
| c·x[n] | c·X(e^{jω}) |
| x[n−n₀] | e^{−jωn₀}X(e^{jω}) |

### 4a. Mitra 4.56 — h[n] = δ[n] − αδ[n−R], find G(e^{jω}) for g = h ⊛ h ⊛ h

> H(e^{jω}) = 1 − αe^{−jωR}
> Convolution in time = multiplication in frequency, so
> G(e^{jω}) = H³ = (1 − αe^{−jωR})³ = **1 − 3αe^{−jωR} + 3α²e^{−j2ωR} − α³e^{−j3ωR}**

⚠ The note writes "1 − 3e^{−jωR} + 3e^{−j2ωR} + e^{−3jωR}". It dropped the α's and the last sign. Expand (1 − u)³ = 1 − 3u + 3u² − u³ with u = αe^{−jωR}.

### 4b. Mitra 4.64 — cascade h₁ = αδ[n] + δ[n−1], h₂ = βⁿu[n] (|β|<1). For what α, β is |H(e^{jω})| = 1?

> H₁ = α + e^{−jω}, H₂ = 1/(1 − βe^{−jω}), so H = (α + e^{−jω})/(1 − βe^{−jω})
>
> |H| = 1 ⇒ |α + e^{−jω}|² = |1 − βe^{−jω}|²     (use |z|² = z·z*)
> α² + 2α cos ω + 1 = 1 − 2β cos ω + β²
>
> This must hold for every ω, so match the coefficients:
> constants: α² = β²; cos ω terms: 2α = −2β
> ⇒ **α = −β** (which also satisfies α² = β²), with |β| < 1.

Checked with β = 0.6, α = −0.6: |H| = 1.000 at every ω tried. A system with |H| = 1 everywhere is called an **all-pass** filter.

### 4c. Mitra 4.76 — show y[n] = d₃x[n] + d₂x[n−1] + d₁x[n−2] + x[n−3] − d₁y[n−1] − d₂y[n−2] − d₃y[n−3] is all-pass

> DTFT of both sides: H = (d₃ + d₂e^{−jω} + d₁e^{−j2ω} + e^{−j3ω}) / (1 + d₁e^{−jω} + d₂e^{−j2ω} + d₃e^{−j3ω})
> Let D(e^{jω}) = denominator. Then the numerator is e^{−j3ω}·D*(e^{jω}) (the same coefficients in reverse order).
> |H| = |e^{−j3ω}|·|D*|/|D| = 1·|D|/|D| = **1 for every ω**. ∎

**Pattern to spot:** if the numerator coefficients are the denominator coefficients reversed, the filter is all-pass.

### 4d. Mitra 4.61 — non-causal FIR h = a₁δ[n−3] + a₂δ[n−2] + a₃δ[n−1] + a₄δ[n] + a₅δ[n+1] + a₆δ[n+2]. When is it zero-phase?

> H is real (zero phase) for all ω ⇔ h[n] is even: h[n] = h[−n].
> n = ±3: h[3] = a₁ but h[−3] = 0, so **a₁ = 0**
> n = ±2: **a₂ = a₆**; n = ±1: **a₃ = a₅**; a₄ is free (any real value).

### 4e. Mitra 4.63 — y[n] = a₁x[n+k] + a₂x[n+k−1] + a₃x[n+k−2] + a₂x[n+k−3] + a₁x[n+k−4]. For what k is H real?

> H = e^{jωk}(a₁ + a₂e^{−jω} + a₃e^{−j2ω} + a₂e^{−j3ω} + a₁e^{−j4ω})
> = e^{jω(k−2)}·[a₃ + 2a₂ cos ω + 2a₁ cos 2ω]    (pull out e^{−j2ω} and pair the terms: e^{jθ}+e^{−jθ} = 2cos θ)
> The bracket is real, so H is real when e^{jω(k−2)} = 1 ⇒ **k = 2**.

### 4f. Mitra 4.57 — g[n] = αⁿ for 0 ≤ n ≤ M−1. Find G(e^{jω}) and scale it to unity DC gain.

> G(e^{jω}) = Σ_{n=0}^{M−1}(αe^{−jω})ⁿ = **(1 − αᴹe^{−jωM})/(1 − αe^{−jω})**
> DC (ω = 0): G(e^{j0}) = (1 − αᴹ)/(1 − α)
> Scale by c = (1 − α)/(1 − αᴹ): **g′[n] = ((1 − α)/(1 − αᴹ))·αⁿ, 0 ≤ n ≤ M−1**

(Checked: α = 0.5, M = 4 gives a DC value of 1.875 both ways.)

---

## 5. Moving-average filter (4.8.4) — **full derivation, 5 marks guaranteed if asked**

Past paper 5b: *"Compute the magnitude and phase response of a 5-point moving average filter."*

**Write this:**

> y[n] = (1/M) Σ_{l=0}^{M−1} x[n−l], so h[n] = 1/M for 0 ≤ n ≤ M−1 and 0 otherwise. It has finite length, so it is FIR.
>
> H(e^{jω}) = (1/M) Σ_{n=0}^{M−1} e^{−jωn} = (1/M)·(1 − e^{−jωM})/(1 − e^{−jω})   [Σ rⁿ = (1−r^M)/(1−r)]
>
> Factor e^{−jωM/2} out of the top and e^{−jω/2} out of the bottom:
> = (1/M)·e^{−jωM/2}(e^{jωM/2} − e^{−jωM/2}) / [e^{−jω/2}(e^{jω/2} − e^{−jω/2})]
> = (1/M)·e^{−jω(M−1)/2}·(2j sin(Mω/2))/(2j sin(ω/2))
>
> **H(e^{jω}) = (1/M)·[sin(Mω/2)/sin(ω/2)]·e^{−jω(M−1)/2}**
>
> **|H(e^{jω})| = |(1/M)·sin(Mω/2)/sin(ω/2)|**
>
> **θ(ω) = −(M−1)ω/2 + π·Σ_{k=1}^{⌊M/2⌋} μ(ω − 2πk/M)**, 0 ≤ ω ≤ π

**Why the +π jumps?** sin(Mω/2)/sin(ω/2) is real but goes **negative** after each zero at ω = 2πk/M. A negative real number = |·|·e^{jπ}, so the phase jumps by π there. Apart from those jumps the phase is linear, which means a pure delay of (M−1)/2 samples.

**M = 5, plugged in (checked):** |H| = |sin(5ω/2)/(5 sin(ω/2))|, θ = −2ω (+π after 2π/5 and after 4π/5)

| ω | 0 | π/5 | 2π/5 | π/2 | 4π/5 | π |
|---|---|---|---|---|---|---|
| \|H\| | 1 | 0.647 | **0** | 0.2 | **0** | 0.2 |

Zeros at ω = 2π/5 and 4π/5. |H(0)| = 1, so DC passes untouched. The gain is large near ω = 0 and small at high ω, which makes it a **low-pass filter**.

Sketch: a main lobe from 0 to 2π/5 with height 1, then small bumps of height about 0.25 or less. The phase is a sawtooth: slope −2 that jumps up by π at each zero.

---

## 6. Steady-state and transient response (4.8.5)

> **y[n] = y_ss[n] + y_tr[n]**
> - **Transient** y_tr: the temporary behaviour right after the input starts.
> - **Steady state** y_ss: what is left after the transient has died out.
> - For a **stable** system y_tr → 0 as n → ∞, so y[n] ≈ y_ss[n].

### 6a. Worked (note p.18): h = {4, −5, 6, −3}, input x[n] = u[n]

> y[n] = 4x[n] − 5x[n−1] + 6x[n−2] − 3x[n−3]
> y[0] = 4, y[1] = 4−5 = **−1**, y[2] = 4−5+6 = **5**, y[3] = 4−5+6−3 = **2**, and y[n] = 2 for all n ≥ 3
> y_ss = 2 = H(e^{j0}) = Σh[n]. u[n] is a "frequency-0" (DC) input, so it gets multiplied by H at ω = 0.
> {4, −1, 5} is the **transient**. An FIR of length L has a transient lasting L−1 samples.

---

## 7. Response to a causal exponential (4.8.6) — **derivation**

**Write this:**

> Input x[n] = e^{jωn}u[n] (switched on at n = 0); the system is causal (h[k] = 0 for k < 0).
>
> y[n] = Σ_{k=0}^{∞} h[k]e^{jω(n−k)}u[n−k]. Since u[n−k] = 0 for k > n, only 0 ≤ k ≤ n contributes:
> y[n] = e^{jωn} Σ_{k=0}^{n} h[k]e^{−jωk}   (this is **not** H(e^{jω}), because the upper limit is n, not ∞)
>
> Split the sum: Σ_{k=0}^{n} = Σ_{k=0}^{∞} − Σ_{k=n+1}^{∞}
>
> **y[n] = H(e^{jω})e^{jωn} − e^{jωn} Σ_{k=n+1}^{∞} h[k]e^{−jωk}**
>           ↑ y_ss[n]                     ↑ y_tr[n]
>
> |y_tr[n]| ≤ Σ_{k=n+1}^{∞}|h[k]| → 0 as n → ∞ when h is absolutely summable (stable), so y[n] → y_ss[n].
> For an FIR of length N+1, y_tr = 0 for n ≥ N: the transient ends after N samples.

---

## 8. The concept of filtering (4.8.7)

> Use |H(e^{jω})| to decide which frequencies survive.
> |H| ≈ 1 → passes unchanged · |H| < 1 → attenuated · |H| ≈ 0 → removed · |H| > 1 → amplified
> **Passband**: the range of frequencies the filter lets through. **Stopband**: the range it suppresses.

| Type | Passes | Sketch of \|H\| on 0…π |
|---|---|---|
| Low-pass (e.g. moving average) | small \|ω\| | high at 0, low at π |
| High-pass | large \|ω\| | ≈0 at 0, high at π |
| Band-pass | a middle band | bump in the middle |
| Band-stop (notch) | low and high | dip in the middle |

**Trick:** large H near ω = 0 means low-pass. H ≈ 0 near ω = 0 means high-pass.

**Ideal LPF:** |H| = 1 for 0 ≤ |ω| ≤ ω_c and 0 for ω_c < |ω| ≤ π. Feed in x = A cos ω₁n + B cos ω₂n with ω₁ < ω_c < ω₂ and you get **y = A|H(e^{jω₁})| cos(ω₁n + θ(ω₁))**: the high-frequency term is gone.
*Why can't an ideal filter be built?* Its h[n] = sin(ω_c n)/(πn) is infinitely long and non-zero for n < 0, so it is non-causal and has no finite realisation (past-paper 2d).

### 8a. Design example (in the note, p.20): kill 0.1 rad/sample, pass 0.4 rad/sample

> 3-tap symmetric FIR: h[0] = h[2] = α₀, h[1] = α₁.
> H(e^{jω}) = α₀ + α₁e^{−jω} + α₀e^{−j2ω} = e^{−jω}(α₁ + 2α₀ cos ω)
> |H| = |α₁ + 2α₀ cos ω|, θ = −ω (linear phase)
> Conditions: 2α₀cos(0.1) + α₁ = 0 … (i);  2α₀cos(0.4) + α₁ = 1 … (ii)
> (ii) − (i): α₀ = 1/(2[cos 0.4 − cos 0.1]) = **−6.762**;  α₁ = −2α₀cos 0.1 = **13.456**
> **y[n] = −6.762x[n] + 13.456x[n−1] − 6.762x[n−2]**
> Checked: |H(0.1)| = 0 and |H(0.4)| = 1.000. It passes the high frequency and blocks the low one, so it is a high-pass filter.

### 8b. Mitra 4.60 — what frequencies come out? (input x[n] = cos ω₀n)

Trick: products of cosines create **new** frequencies, so these systems are **not LTI**. An LTI system can never do this.

| System | Expand | Frequencies in y |
|---|---|---|
| y = cos(πn/5)·x[n] | ½[cos((ω₀−π/5)n) + cos((ω₀+π/5)n)] | **ω₀ ± π/5** |
| y = x⁴[n] | cos⁴ = 3/8 + ½cos 2ω₀n + ⅛cos 4ω₀n | **0, 2ω₀, 4ω₀** |
| y = x[4n] | cos(4ω₀n) | **4ω₀** |

---

## 9. Ten-minute self-test (cover the answers)

| # | Question | Answer |
|---|---|---|
| 1 | Why is e^{jωn} an eigenfunction of an LTI system? | y = H(e^{jω})e^{jωn}, and H does not depend on n |
| 2 | Is zⁿu[n] an eigenfunction? | No, the sum depends on n through u[n−k] |
| 3 | \|H\| and phase symmetry for real h | \|H\| even, θ odd |
| 4 | A cos(ω₀n+φ) through H → ? | A\|H(e^{jω₀})\| cos(ω₀n+φ+θ(ω₀)) |
| 5 | H for h = (0.4)ⁿu[n] at π/4 | 1.2067 − j0.4759 → 1.297∠−21.5° |
| 6 | M-point MA H(e^{jω}) | (1/M)·sin(Mω/2)/sin(ω/2)·e^{−jω(M−1)/2} |
| 7 | Zeros of a 5-point MA | ω = 2π/5, 4π/5 |
| 8 | Step response of h = {4,−5,6,−3} | 4, −1, 5, then 2 forever (y_ss = 2 = ΣH) |
| 9 | y_tr for the causal exponential input | −e^{jωn}Σ_{k=n+1}^{∞}h[k]e^{−jωk} |
| 10 | Condition for all-pass in 4.64 | α = −β, \|β\| < 1 |
| 11 | When is the 4.63 system zero-phase? | k = 2 |
| 12 | Why can't an ideal LPF be realised? | h = sin(ω_c n)/(πn) is infinite and non-causal |

Verified by `python DSP/study/_mid2_verify.py` on 9 Oct 2026 (4.68, MA table, HPF design, 4.64, 4.76, step response).
