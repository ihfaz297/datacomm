# MID-2 battle plan — **Sunday 11 Oct 2026, 10:00 AM** · 45 min · 30 marks

**Start here.** This replaces `00-tt2-battle-plan.md` as the entry point. That file was built from an
older TT2 paper (DFT/FFT/FIR windows). Those topics are **not in the updated syllabus** that sir posted
(`DSP/midterm-2.txt.txt`, the "Updated Syllabus for Mid Term 2 and Quiz 2" block).

## 1. What the exam actually is

| Q | Topic | Source | Marks | Counts as | Tutorial |
|---|---|---|---|---|---|
| **Q1** | Frequency-domain representation of LTI DTS (4.8 – 4.8.7) | Mitra Ch 4 | 10 | **Quiz 2** | `20-T1-frequency-response.md` |
| **Q2** | z-transform and LTI analysis | Proakis Ch 3 | 10 | Term Test 2 | `21-T2-ztransform.md` |
| **Q3** | Frequency analysis of signals | Proakis Ch 4 | 10 | Term Test 2 | `22-T3-frequency-analysis.md` |

**45 minutes for 30 marks = 1.5 min per mark.** Finish Q1, then go straight on to Q2 and Q3 (the notice says so).
The first syllabus post also listed Ch 5 and Ch 7 (DFT/FFT). The *updated* post dropped them. If a DFT
question shows up anyway, the old `12-dft-circular-conv-tutorial.md` and `13-fir-window-design-tutorial.md` cover it,
but don't spend Saturday there.

### Lessons from TT1 (`DSP/TT/Tt1.jpg`), so we don't lose the same marks twice

- **TT1 Q4 (convolution, Proakis Ex 2.3.2) lost marks because the method wasn't the one sir wanted.** He
  marks the **expansion** of y(n) = Σx(k)h(n−k), written out for each n with the ranges stated first.
  The tabular trick is for checking in the margin only. Revise with `23-convolution-revise.md` (45 min).
- **TT1 Q3 was "z-transform of aⁿu(n), ROC, pole-zero plot".** Sir reuses z-transform basics. For Mid-2,
  expect the harder cousins: two-sided ROC, finite aⁿ pole-zero, partial fractions.
- Sir reuses **Proakis/Mitra textbook examples word for word**. If a question looks familiar, it is the
  book example. Reproduce the book's steps.
- **Read the verb.** "Determine" = show the expansion. "Using z-transform" = Y = XH with the ROC. "Graphically" = sketches.

## 2. Predicted questions, ranked (from your note's exercise list and the 2021-22 final)

Sir sets numericals from the exercises he solved in class. These carry a ★ in your note, and the final paper
re-used several of them word for word.

### Q1 (Mitra 4.8) — expect "prove/derive" + one small numerical

| Rank | Question | Where |
|---|---|---|
| 1 | Derive \|H\| and phase of the **M-point moving average** (or "5-point", final 5b) | T1 §5 |
| 2 | **Steady-state response to A cos(ω₀n+φ)** derivation | T1 §3 |
| 3 | **Eigenfunction proof** (e^{jωn}, and 4.54: zⁿ yes, zⁿu[n] no) | T1 §1 |
| 4 | Numerical y_ss: **4.68** h = 0.4ⁿu[n], x = sin(πn/4) → 1.297 sin(πn/4 − 0.376) | T1 §3b |
| 5 | Causal exponential → y_ss + y_tr derivation; step response of {4,−5,6,−3} | T1 §6–7 |
| 6 | 4.64 (α = −β all-pass), 4.76 (all-pass proof), 4.56 ((1−αe^{−jωR})³) | T1 §4 |
| 7 | Filtering concept + LP/HP/BP/BS sketch; HPF design 0.1/0.4 | T1 §8 |
| 8 | 4.57, 4.61 (a₁=0, a₂=a₆, a₃=a₅), 4.63 (k=2), 4.60 (new frequencies) | T1 §4, §8b |

### Q2 (z-transform) — expect "z-transform + ROC + sketch" or "inverse by partial fractions"

| Rank | Question | Where |
|---|---|---|
| 1 | **aⁿu[n] + bⁿu[−n−1]**: X(z), ROC, sketch, both cases (final 6a, 4f) | T2 §3c |
| 2 | **2ⁿu[n] ⊛ 0.5ⁿu[n]** three ways (marked *Imp for exam* in the note) | T2 §8b |
| 3 | **aⁿ, 0≤n≤M−1**: X(z) and pole-zero plot (final 6b) | T2 §6b |
| 4 | y(n) = ½y(n−1) + 2x(n): H(z), h[n] (final 5a) | T2 §7a |
| 5 | Partial fractions with a double pole: (4/9)(−2)ⁿ + 5/9 + n/3 | T2 §8c |
| 6 | Finite sequences and ROC (Ex 3.1.1), properties table, Euler cos/sin | T2 §2, §4 |
| 7 | Short ones: define pole/zero, stability ⇔ ROC ∋ unit circle, significance of poles/zeros | T2 §6–7 |

### Q3 (Proakis Ch 4) — expect "derive a spectrum" + "explain/properties"

| Rank | Question | Where |
|---|---|---|
| 1 | **Square wave CTFS** c_k = (2/kπ)sin(kπ/2), odd harmonics | T3 §1b |
| 2 | **Rect pulse CTFT** → Aτ sinc(Fτ), width trade-off | T3 §2a |
| 3 | **DTFS Ex 4.2.1** (cos√2πn not periodic; cos(πn/3) → c₁ = c₅ = ½) | T3 §3a |
| 4 | DTFT of aⁿu[n] (final 2c), aⁿ finite (2e), Parseval e^{−0.6t} → 0.833 (2f) | T3 §4 |
| 5 | Power density spectrum P = Σ\|c_k\|²; energy density + Parseval derivation | T3 §3c, §4d |
| 6 | Properties table with 2-line proofs (shift, freq shift, modulation, correlation) | T3 §7–8 |
| 7 | Dirichlet conditions, the 4-transform table, symmetry, bandwidth classes | T3 §0, §2, §4e, §6 |

## 3. Errata in `Note/Mid-2 note.pdf` (don't copy these into the exam)

| Page | Note says | Correct |
|---|---|---|
| p.16 (4.56) | G = 1 − 3e^{−jωR} + 3e^{−j2ωR} + e^{−3jωR} | **1 − 3αe^{−jωR} + 3α²e^{−j2ωR} − α³e^{−j3ωR}** |
| p.27 ("Imp" ②) | X(e^{jω}) = 1/(1 − 2e^{−jω}) | **does not exist**: 2ⁿu[n] isn't summable and ROC \|z\|>2 misses the unit circle. Say so, and use the z-route |
| p.30 (sin ω₀n) | denominator 1 − 2cos ω₀ z⁻¹ **−** z⁻² | **+ z⁻²** (the p.31 table is right) |
| p.33 (double pole) | x[n] = (4/9)(**2**)ⁿu[n] + … | **(4/9)(−2)ⁿu[n]** + (5/9)u[n] + (n/3)u[n] |

Everything else in the note that I checked numerically is correct (4.68, HPF design, 4.64, 4.76, step response,
two-sided ROC, pole-zero roots, DTFS examples).

## 4. Saturday schedule (exam Sunday 10:00)

Sleep first. A tired brain loses more marks than one unread section.

| Block | Do | Check yourself with |
|---|---|---|
| Sat morning (2.5 h) | **T1** §1, §3, §5 by hand: eigenfunction, steady state, MA derivation. Then §3b 4.68 numbers | T1 §9 self-test |
| Sat late morning (45 min) | **Convolution revise**: `23-convolution-revise.md` Method A on TT1 Q4 and final Q1h by hand | its quick drill |
| Sat midday (2.5 h) | **T2** §3 (all four derivations + ROC sketch), §8b (2ⁿ ⊛ 0.5ⁿ), §6b pole-zero | T2 §9 self-test |
| Sat afternoon (2 h) | **T3** §1b square wave, §2a rect→sinc, §3a DTFS, §4a–4d | T3 §9 self-test |
| Sat evening (1.5 h) | `python DSP/study/mid2_handcalc_drill.py`: type your hand answers, get PASS/FAIL | the drill |
| Sat night (1 h) | Phone: open the illustration artifact, flip through the pictures (ROC rings, MA lobes, harmonics, transient) | — |
| Sun 8:30 | §5 below (doomsday sheet) + skim `24-traps-and-intuition.md` | — |

## 5. Doomsday sheet — if you only have 20 minutes

Write these from memory on scratch paper once. That's ~60% of the marks.

```text
CONV    y(n) = Σ x(k) h(n-k): state ranges + length N1+N2-1, then EXPAND per n; check Σy = Σx·Σh
EIGEN   x=e^{jwn} -> y = H(e^{jw}) e^{jwn},  H = Σ h[k] e^{-jwk}
SS      A cos(w0 n+φ) -> A|H(e^{jw0})| cos(w0 n + φ + θ(w0))
MA      H = (1/M) sin(Mw/2)/sin(w/2) · e^{-jw(M-1)/2};  zeros at 2πk/M;  |H(0)|=1
TRANS   y = H e^{jwn}  −  e^{jwn} Σ_{k=n+1}^{∞} h[k]e^{-jwk}   (2nd term = transient → 0 if stable)

Z       a^n u[n]      -> 1/(1-az^-1), |z|>|a|
        -a^n u[-n-1]  -> 1/(1-az^-1), |z|<|a|      SAME X(z), DIFFERENT ROC
        a^n u[n] + b^n u[-n-1] -> ROC |a|<|z|<|b|, else doesn't exist
        stable <=> ROC contains |z|=1 ; causal+stable <=> poles inside unit circle
        partial fractions on X(z)/z, cover-up, then table by ROC

FREQ    periodic <-> discrete ; discrete <-> periodic   (CTFS, CTFT, DTFS, DTFT)
        square ±1: c_k = (2/kπ) sin(kπ/2)  odd harmonics, 1/k
        rect A,τ : Aτ sinc(Fτ), zeros at k/τ
        DTFT a^n u[n] = 1/(1-ae^{-jw});  Parseval Σ|x|² = (1/2π)∫|X|²
        P = Σ|c_k|² ;  X(w) = X(z)|z=e^{jw}
```

## 6. Files in this folder

| File | What |
|---|---|
| `00-mid2-battle-plan.md` | this map |
| `20-T1-frequency-response.md` | Q1 tutorial: derivations + all Mitra 4.5x/4.6x/4.7x exercises worked |
| `21-T2-ztransform.md` | Q2 tutorial: ROC derivations, properties, poles/zeros, inversion |
| `22-T3-frequency-analysis.md` | Q3 tutorial: CTFS/CTFT/DTFS/DTFT, Parseval, properties incl. the missing slides |
| `24-traps-and-intuition.md` | blunders, sir's trick variants, intuitive pictures; read Saturday night + Sunday morning |
| `23-convolution-revise.md` | convolution the way sir marks it (expansion), plus the z-route and your tabular check |
| `mid2-illustrated.html` | phone picture book, live at https://claude.ai/artifact/EvfueYF41j9CGyLd5Nx8En |
| `mid2_handcalc_drill.py` | DataCamp-style: you type hand-calculated answers, it prints PASS/FAIL |
| `_mid2_verify.py` | the script that checked every number in the tutorials |
| `00-tt2-battle-plan.md`, `10…13-*.md`, `lab-doomsday.md` | DeepSeek's older material (DFT/FIR/lab). Out of the updated syllabus except 10/11 overlap |
