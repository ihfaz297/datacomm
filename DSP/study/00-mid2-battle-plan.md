# Mid-2 Battle Plan

*Sunday 11 October 2026, 10:00 AM · 40 minutes · 15 marks*

**Start here.** This is the map for the Mid-2 exam, built on the updated syllabus sir posted (`DSP/midterm-2.txt.txt`, the block titled "Updated Syllabus for Mid Term 2 and Quiz 2").

> **Reading these notes.** Open any of these files in VS Code and press `Ctrl+Shift+V` (or `Ctrl+K V` for a side-by-side view). The preview typesets the maths. The raw file with its dollar signs is not meant to be read directly.

---

## 1. The finalised syllabus, and what the paper looks like

Sir's **updated** notice has three topics, one question each:

| Q | Topic | Source | Marks | Counts as | Study file |
|---|---|---|---|---|---|
| **Q1** | Frequency-domain representation of LTI discrete-time systems (§4.8 to §4.8.7) | Mitra, Ch 4 | 5 | **Quiz 2** | `20-T1-frequency-response.md` |
| **Q2** | The z-transform and its application to the analysis of LTI systems | Proakis, Ch 3 | 5 | Term Test 2 | `21-T2-ztransform.md` |
| **Q3** | Frequency analysis of signals | Proakis, Ch 4 | 5 | Term Test 2 | `22-T3-frequency-analysis.md` |

The Q1 sub-topics, as listed in the notice: frequency-domain representation (4.8), frequency response (4.8.1), frequency-domain characterisation (4.8.2), frequency response of LTI systems (4.8.3), the moving-average filter (4.8.4), steady-state and transient response (4.8.5), response to a causal exponential (4.8.6), and the concept of filtering (4.8.7).

**What was dropped.** Sir's first post also listed Proakis Ch 5 (frequency-domain analysis of LTI systems) and Ch 7 (the DFT, FFT, DIT and DIF). The updated post removed both, so don't spend any time on them.

**Timing.** 40 minutes for 15 marks is about 2.7 minutes per mark, so roughly 13 minutes per topic. Sir cut the format from 30 marks and 45 minutes, so expect shorter questions: one derivation or one standard example per topic. Finish Q1, then go straight on to Q2 and Q3; the notice says so.

### Lessons from TT1 (`DSP/TT/Tt1.jpg`), so the same marks aren't lost twice

- **TT1 Q4 (convolution, Proakis Ex 2.3.2) lost marks because the method wasn't the one sir wanted.** He marks the **expansion** of $y(n) = \sum_k x(k)\,h(n-k)$, written out for each $n$ with the ranges stated first. The table trick is for checking in the margin only. Revise with `23-convolution-revise.md` (about 45 minutes).
- **TT1 Q3 was "the z-transform of $a^n u(n)$, its ROC, and the pole-zero plot".** Sir reuses z-transform basics. For Mid-2, expect the harder relatives: a two-sided ROC, the pole-zero plot of a finite $a^n$, partial fractions.
- **Sir reuses Proakis and Mitra examples word for word.** If a question looks familiar, it is the book example. Reproduce the book's steps.
- **Read the verb.** "Determine" means show the expansion. "Using the z-transform" means $Y = XH$ with the ROC. "Graphically" means sketches.

---

## 2. Predicted questions, ranked

These come from the exercise list in your note and from the 2021–22 final. Sir sets numericals from the exercises he solved in class, and the final reused several of them word for word.

### Q1 (Mitra 4.8): expect a "prove" or "derive" part plus one small numerical

| Rank | Question | Where |
|---|---|---|
| 1 | Derive $\lvert H\rvert$ and the phase of the **$M$-point moving average** (or "5-point", final 5b) | T1 §5 |
| 2 | **Steady-state response to $A\cos(\omega_0 n + \phi)$**, the derivation | T1 §3 |
| 3 | **Eigenfunction proof** ($e^{j\omega n}$; and 4.54: $z^n$ is one, $z^n u[n]$ is not) | T1 §1 |
| 4 | Numerical $y_{ss}$: **4.68**, $h = 0.4^n u[n]$, $x = \sin(\pi n/4)$, giving $1.297\sin(\pi n/4 - 0.376)$ | T1 §3b |
| 5 | Causal exponential, $y_{ss} + y_{tr}$ derivation; step response of $\{4, -5, 6, -3\}$ | T1 §6–7 |
| 6 | 4.64 ($\alpha = -\beta$, all-pass), 4.76 (all-pass proof), 4.56 ($(1 - \alpha e^{-j\omega R})^3$) | T1 §4 |
| 7 | The concept of filtering, with LP/HP/BP/BS sketches; the high-pass design for 0.1 and 0.4 | T1 §8 |
| 8 | 4.57, 4.61 ($a_1 = 0$, $a_2 = a_6$, $a_3 = a_5$), 4.63 ($k = 2$), 4.60 (new frequencies) | T1 §4, §8b |

### Q2 (the z-transform): expect "z-transform + ROC + sketch" or "inverse by partial fractions"

| Rank | Question | Where |
|---|---|---|
| 1 | **$a^n u[n] + b^n u[-n-1]$**: $X(z)$, ROC, sketch, both cases (final 6a, 4f) | T2 §3c |
| 2 | **$2^n u[n] * 0.5^n u[n]$** three ways (marked "Imp for exam" in the note) | T2 §8b |
| 3 | **$a^n$ for $0 \le n \le M-1$**: $X(z)$ and the pole-zero plot (final 6b) | T2 §6b |
| 4 | $y(n) = \frac12 y(n-1) + 2x(n)$: find $H(z)$ and $h[n]$ (final 5a) | T2 §7a |
| 5 | Partial fractions with a double pole: $\frac49(-2)^n + \frac59 + \frac{n}{3}$ | T2 §8c |
| 6 | Finite sequences and their ROCs (Ex 3.1.1), the properties table, Euler for cos and sin | T2 §2, §4 |
| 7 | Short ones: define poles and zeros; stability means the ROC contains the unit circle; significance of poles and zeros | T2 §6–7 |

### Q3 (Proakis Ch 4): expect "derive a spectrum" plus "explain" or "properties"

| Rank | Question | Where |
|---|---|---|
| 1 | **Square wave, CTFS**: $c_k = \frac{2}{k\pi}\sin\frac{k\pi}{2}$, odd harmonics only | T3 §1b |
| 2 | **Rectangular pulse, CTFT**: $A\tau\operatorname{sinc}(F\tau)$ and the width trade-off | T3 §2a |
| 3 | **DTFS, Ex 4.2.1**: $\cos(\sqrt2\pi n)$ is not periodic; $\cos(\pi n/3)$ gives $c_1 = c_5 = \frac12$ | T3 §3a |
| 4 | DTFT of $a^n u[n]$ (final 2c), of a finite $a^n$ (2e); Parseval for $e^{-0.6t}$, giving $0.833$ (2f) | T3 §4 |
| 5 | Power density spectrum $P = \sum \lvert c_k\rvert^2$; energy density and the Parseval derivation | T3 §3c, §4d |
| 6 | The properties table with two-line proofs (time shift, frequency shift, modulation, correlation) | T3 §7–8 |
| 7 | Dirichlet conditions, the four-transform table, symmetry, bandwidth classes | T3 §0, §2, §4e, §6 |

---

## 3. Mistakes in your class note (`Note/Mid-2 note.pdf`): don't copy these

| Page | The note says | Correct version |
|---|---|---|
| p.16 (4.56) | $G = 1 - 3e^{-j\omega R} + 3e^{-j2\omega R} + e^{-j3\omega R}$ | $1 - 3\alpha e^{-j\omega R} + 3\alpha^2e^{-j2\omega R} - \alpha^3e^{-j3\omega R}$ |
| p.27 ("Imp", part 2) | $X(e^{j\omega}) = \frac{1}{1 - 2e^{-j\omega}}$ | **does not exist**: $2^n u[n]$ is not summable, and the ROC $\lvert z\rvert > 2$ misses the unit circle. Say so, and use the z-route |
| p.30 ($\sin\omega_0 n$) | denominator $1 - 2\cos\omega_0\,z^{-1} - z^{-2}$ | $+\,z^{-2}$ (the table on p.31 is right) |
| p.33 (double pole) | $x[n] = \frac49(2)^n u[n] + \cdots$ | $\frac49(-2)^n u[n] + \frac59 u[n] + \frac{n}{3}u[n]$ |

Everything else in the note that was checked numerically is correct: 4.68, the high-pass design, 4.64, 4.76, the step response, the two-sided ROC, the pole-zero roots and the DTFS examples.

---

## 4. Saturday schedule (exam on Sunday at 10:00)

Sleep first. A tired brain loses more marks than one unread section.

| Block | Do | Check yourself with |
|---|---|---|
| Morning (2.5 h) | **T1** §1, §3 and §5 by hand: eigenfunction, steady state, moving-average derivation. Then the numbers in §3b (4.68) | T1 §9 self-test |
| Late morning (45 min) | **Convolution**: Method A from `23-convolution-revise.md` on TT1 Q4 and final Q1h, by hand | its quick drill |
| Midday (2.5 h) | **T2** §3 (all four derivations and the ROC sketch), §8b ($2^n * 0.5^n$), §6b (pole-zero plot) | T2 §9 self-test |
| Afternoon (2 h) | **T3** §1b square wave, §2a rect to sinc, §3a DTFS, §4a–4d | T3 §9 self-test |
| Evening (1.5 h) | `python DSP/study/mid2_handcalc_drill.py`: type in your hand answers and get PASS or FAIL | the drill |
| Night (1 h) | On your phone, flip through the illustrated artifact: ROC rings, moving-average lobes, harmonics, the transient | — |
| Sunday 8:30 | Section 5 below, then skim `24-traps-and-intuition.md` | — |

---

## 5. The doomsday sheet: if you only have 20 minutes

Write these out from memory on scratch paper once. They cover roughly 60% of the marks.

**Convolution.** State the ranges and the length $N_1 + N_2 - 1$, then expand for each $n$, and check that $\sum y = \sum x\cdot\sum h$:

$$
y(n) = \sum_k x(k)\,h(n-k).
$$

**Topic 1: frequency response.**

$$
\begin{aligned}
&\text{Eigenfunction:} && e^{j\omega n} \;\longmapsto\; H(e^{j\omega})\,e^{j\omega n}, \qquad H(e^{j\omega}) = \sum_k h[k]\,e^{-j\omega k} \\[4pt]
&\text{Steady state:} && A\cos(\omega_0 n + \phi) \;\longmapsto\; A\,|H(e^{j\omega_0})|\cos\big(\omega_0 n + \phi + \theta(\omega_0)\big) \\[4pt]
&\text{Moving average:} && H(e^{j\omega}) = \frac{1}{M}\,\frac{\sin(M\omega/2)}{\sin(\omega/2)}\,e^{-j(M-1)\omega/2}, \quad \text{zeros at } \frac{2\pi k}{M}, \quad |H(e^{j0})| = 1 \\[4pt]
&\text{Transient:} && y[n] = H(e^{j\omega})\,e^{j\omega n} - e^{j\omega n}\sum_{k=n+1}^{\infty} h[k]\,e^{-j\omega k} \quad (\text{the second term} \to 0 \text{ if stable})
\end{aligned}
$$

**Topic 2: the z-transform.**

$$
\begin{aligned}
a^n u[n] &\;\longleftrightarrow\; \frac{1}{1 - az^{-1}}, \quad |z| > |a| \\[4pt]
-a^n u[-n-1] &\;\longleftrightarrow\; \frac{1}{1 - az^{-1}}, \quad |z| < |a| \qquad \text{(same } X(z)\text{, different ROC)} \\[4pt]
a^n u[n] + b^n u[-n-1] &\;\longrightarrow\; \text{ROC } |a| < |z| < |b|, \text{ otherwise it does not exist}
\end{aligned}
$$

**Write the ROC with every $X(z)$, $H(z)$ and $Y(z)$**, using magnitudes ($|z| > |a|$) and a one-word reason; sir cuts marks for any missing one. Stable if and only if the ROC contains $|z| = 1$. Causal and stable if and only if all poles are inside the unit circle. For an inverse, do partial fractions on $X(z)/z$, use the cover-up rule, then pick each term from the table according to the ROC.

**Topic 3: frequency analysis.**

$$
\begin{aligned}
&\text{Periodic} \leftrightarrow \text{discrete}, \quad \text{discrete} \leftrightarrow \text{periodic} \qquad \text{(CTFS, CTFT, DTFS, DTFT)} \\[4pt]
&\text{Square wave } \pm 1: \quad c_k = \frac{2}{k\pi}\sin\frac{k\pi}{2}, \quad \text{odd harmonics only, falling like } 1/k \\[4pt]
&\text{Rect pulse } (A, \tau): \quad X(F) = A\tau\operatorname{sinc}(F\tau), \quad \text{zeros at } F = k/\tau \\[4pt]
&\text{DTFT of } a^n u[n] = \frac{1}{1 - ae^{-j\omega}}, \qquad \sum_n |x[n]|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi}|X(\omega)|^2\,d\omega \\[4pt]
&P = \sum_k |c_k|^2, \qquad X(\omega) = X(z)\big|_{z = e^{j\omega}}
\end{aligned}
$$

---

## 6. The files in this folder

| File | What it is |
|---|---|
| `00-mid2-battle-plan.md` | this map |
| `20-T1-frequency-response.md` | Q1: the derivations, and every Mitra 4.5x/4.6x/4.7x exercise worked |
| `21-T2-ztransform.md` | Q2: ROC derivations, properties, poles and zeros, inversion |
| `22-T3-frequency-analysis.md` | Q3: CTFS, CTFT, DTFS and DTFT, Parseval, the properties (including the missing slides) |
| `23-convolution-revise.md` | convolution the way sir marks it (expansion), plus the z-route and your table check |
| `24-traps-and-intuition.md` | common mistakes, sir's trick variants, intuitive pictures; read Saturday night and Sunday morning |
| `mid2-notes.html` | these six files typeset for the phone, live at https://claude.ai/artifact/NR1NcgWMjgyLmYUKjiWVvD |
| `_build_mid2_notes.js`, `_mid2_notes_template.html` | rebuild `mid2-notes.html` after editing any of the six files (instructions at the top of the script) |
| `mid2-illustrated.html` | the phone picture book, live at https://claude.ai/artifact/EvfueYF41j9CGyLd5Nx8En |
| `mid2_handcalc_drill.py` | DataCamp style: type in hand-calculated answers and it prints PASS or FAIL |
| `_mid2_verify.py` | the script that checked every number in the tutorials |
| `lab-doomsday.md` | the DSP lab-exam cheat sheet; not part of Mid-2 |
