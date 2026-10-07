# DSP Midterm 2 + Quiz 2 Battle Plan

This guide follows the latest scope note in `midterm-2.txt.txt`: three questions, one from each topic; Q1 is the 10-mark quiz and Q2–Q3 make up the 20-mark term test. Total time is 45 minutes.

## Battle plan: prepare to solve, not just recognize

The exam has three 10-mark questions in 45 minutes. Prepare one reliable solve-path per topic, then do a timed mixed rehearsal. Don't spend the whole session rereading notes.

### Scope and likely solve-paths

| Exam question | Core skills to rehearse | A complete answer usually shows |
|---|---|---|
| LTI frequency response | Get `H(z)` from a difference equation or `h[n]`; evaluate on the unit circle; find gain/phase; moving average; sinusoidal or causal-exponential response | Transform/equation, ROC or unit-circle condition, simplified response, and a short interpretation |
| z-transform and LTI analysis | Transform pairs and properties; inverse transform with ROC; poles/zeros; causality and stability; solve a zero-state system | Transform and ROC, algebra or partial fractions, sequence/system conclusion |
| Frequency analysis of signals | Direct DTFT sums; periodic signal/Fourier-series coefficients; frequency and phase interpretation; use the convention in the question | The transform/coefficient definition, substitutions, simplified result, and correct frequency units/convention |

The notice gives three broad topics, not exact question wording. Treat the solve-paths as coverage, not a prediction. Chapter 5 LTI frequency-domain analysis and DFT/FFT are absent from the updated list; don't let older syllabus text or assignment material displace the three listed topics. For Topic 3, use the Proakis Chapter 4 material and class notes as the authority on whether the instructor expects DTFT, Fourier series, CTFT, or a mix. The local CTFT notes make CTFT conventions worth a brief check if they were taught.

### One focused study session (about 3 hours)

If you have less time, preserve the order and shorten each block. If you have multiple days, repeat the practice-and-correction blocks with fresh problems.

1. **Scope check — 10 min.** Read `midterm-2.txt.txt`; write the three topics from memory. Put a mark next to anything you cannot explain without looking.
2. **z-transform — 40 min.** From `Chapter 3_z_Transform.pdf`, practice transform/inverse pairs, ROC selection, and one difference equation. For each result state right/left sidedness and stability where applicable.
3. **LTI frequency response — 40 min.** Use `Chapter 4.8.6_4.8.7.pdf` and the matching Chapter 4 problems. Solve one difference-equation response, one moving-average response, and one sinusoidal or causal-exponential response. Include transient versus steady state.
4. **Frequency analysis — 40 min.** From the course's Chapter 4 frequency-analysis material, do one direct DTFT and one periodic-signal/Fourier-series problem. Check transform convention, signs, periodicity, and units. Add a CTFT problem only if covered in class.
5. **Closed-notes mixed drill — 35 min.** Do one representative problem from each topic with no notes. Spend up to 10 minutes per problem; use the remaining 5 minutes to check.
6. **Repair — 15 min.** Rework only missed steps from a blank page. Make a short error list (for example: wrong ROC, sign in delay, phase omitted) and review that list before the exam.

### Readiness gate

You are ready to move on from a topic when you can solve one representative problem from a blank page, explain why the ROC/unit-circle/convention is valid, and check the final answer in under 12 minutes. If not, do another worked problem and then retry without looking. Recognizing a formula while reading is not a pass.

### Exam execution: 45 minutes

All three questions are 10 marks, so use **about 13 minutes per question plus 6 minutes to review**. Start with the quiz question as instructed, but move on at 13 minutes if you are stuck; return during the review window. If a question is unusually long, bank the marks you can earn and keep the same overall limit.

- **First 1 minute:** scan all three, note subparts, and mark any immediately familiar question.
- **About 13 minutes per question:** write the governing formula, show substitutions/algebra, box the requested result, and state the key check or interpretation.
- **Final 6 minutes:** check signs, indices, units, ROC and stability claims, phase, and whether you answered every subpart. Do not spend the whole review correcting one cosmetic detail.

If stuck, write the definition and the first valid transformation step, then continue with what follows. For a z-transform question, never leave the ROC unstated; for a frequency-response question, explain why the unit circle is allowed; for a spectrum question, name the transform/convention you used.

## 1. What is in the folder, and what to prioritize

| Material | How it helps |
|---|---|
| `midterm-2.txt.txt` | Latest exam scope and format. Start here. |
| `DSP.md` | Topic outline for the course; it has an older, broader list. |
| `Chapter 4 Problems.pdf`, `Chapter 4.8.6_4.8.7.pdf` | Practice for LTI frequency response, exponential response, and filtering. |
| `Chapter 3_z_Transform.pdf` | Main reference for z-transforms and their use with LTI systems. |
| `Chapter 2.pdf` | Discrete-time sequences and systems background. |
| `DSP_Chapter4_Frequency_Analysis_CTFT.pdf` | Frequency-analysis notes; the filename indicates continuous-time Fourier transform material. Review the matching transform conventions below if this is part of your lecturer's Chapter 4. |
| `CSE 0714 3276- Assignment 1–4.pdf` | Earlier exercises: Assignments 1–2 include spectrum/harmonics and frequency-bin work; Assignment 3 covers sampling, aliasing, and image quantization; Assignment 4 covers convolution, correlation, and averaging. These are useful foundations, but the latest midterm note does not list all of them as standalone topics. |
| `practice/` | Python demonstrations for sampling, aliasing, quantization, sequence operations, convolution, correlation, moving average, and FFT spectra. Useful background, but the scripts are mostly from earlier lab/assignment work. |
| `study/lab-doomsday.md` | Earlier lab-test revision sheet, not the current midterm scope. |

The newest midterm note names **three** topics: (1) LTI discrete-time frequency response, (2) z-transform, and (3) frequency analysis of signals. It does not list Chapter 5, DFT/FFT, image quantization, or the earlier lab syllabus. Those appear in older notes or practice files, so prioritize the three-topic update. The exact boundary of “Frequency Analysis” is not spelled out; the folder contains a CTFT file, so review its transform conventions too if your lecturer covered it in class.

## 2. The big picture

These topics fit together:

1. The **z-transform** turns a sequence or difference equation into algebra in (z). It gives the system function (H(z)), while the region of convergence (ROC) tells you which time sequence it represents.
2. The **frequency response** is (H(z)) evaluated on the unit circle, (z=e^{j\omega}), when the ROC includes that circle. It tells you how an LTI system changes each sinusoidal frequency.
3. **Frequency analysis** describes a signal as a combination of frequency components. For an LTI system, each component is scaled and phase-shifted independently.

Keep these variables distinct:

| Symbol | Meaning | Units |
|---|---|---|
| (n) | discrete-time sample index | samples |
| (\omega) | discrete-time angular frequency | rad/sample; periodic every (2\pi) |
| (f) | ordinary frequency | Hz |
| (\Omega) | continuous-time angular frequency | rad/s |
| (z) | complex z-transform variable | complex |

For sampling at (F_s), (\omega=2\pi f/F_s). Do not use continuous-time (\Omega) and discrete-time (\omega) interchangeably.

## 3. Topic 1 — LTI systems and frequency response

### 3.1 LTI system basics

An LTI system is fully described by its impulse response (h[n]). For input (x[n]),

\[
y[n]=x[n]*h[n]=\sum_{k=-\infty}^{\infty}x[k]h[n-k].
\]

The DTFT converts convolution into multiplication:

\[
Y(e^{j\omega})=X(e^{j\omega})H(e^{j\omega}), \qquad
H(e^{j\omega})=\sum_n h[n]e^{-j\omega n}.
\]

Complex exponentials are eigenfunctions of LTI systems. If (x[n]=e^{j\omega_0n}), then (y[n]=H(e^{j\omega_0})e^{j\omega_0n}). Write the frequency response as

\[
H(e^{j\omega})=|H(e^{j\omega})|e^{j\phi(\omega)}.
\]

Thus an input sinusoid (A\cos(\omega_0n+\theta)) produces the steady-state output

\[
y_{ss}[n]=A|H(e^{j\omega_0})|\cos\big(\omega_0n+\theta+\phi(\omega_0)\big).
\]

At frequency (\omega_0), the magnitude response sets the output amplitude; the phase response adds a phase shift.

### 3.2 Get the response from a difference equation

For a linear constant-coefficient difference equation under initial rest,

\[
y[n]+a_1y[n-1]+\cdots+a_Ny[n-N]
=b_0x[n]+b_1x[n-1]+\cdots+b_Mx[n-M],
\]

take the z-transform and form

\[
H(z)=\frac{Y(z)}{X(z)}
=\frac{b_0+b_1z^{-1}+\cdots+b_Mz^{-M}}
{1+a_1z^{-1}+\cdots+a_Nz^{-N}}.
\]

Then set (z=e^{j\omega}) to obtain (H(e^{j\omega})), provided the ROC includes the unit circle. To get magnitude and phase, use the complex number's modulus and argument; for a quotient, subtract denominator phase from numerator phase.

**Worked example.** Let (y[n]-0.5y[n-1]=x[n]), with a causal system and initial rest.

\[
H(z)=\frac{1}{1-0.5z^{-1}},\qquad h[n]=(0.5)^nu[n],\quad \text{ROC: }|z|>0.5.
\]

Because the ROC includes (|z|=1), the frequency response exists:

\[
H(e^{j\omega})=\frac{1}{1-0.5e^{-j\omega}},\quad
|H(e^{j\omega})|=\frac{1}{\sqrt{1.25-\cos\omega}}.
\]

At DC ((\omega=0)), the gain is (2); at Nyquist ((\omega=\pi)), it is (2/3). Low frequencies pass with more gain, so this is low-pass in character.

### 3.3 Moving-average filter

An (M)-point causal moving average is

\[
h[n]=\begin{cases}1/M,&0\le n\le M-1,\\0,&\text{otherwise},\end{cases}
\quad
H(e^{j\omega})=\frac1M\sum_{k=0}^{M-1}e^{-j\omega k}
=e^{-j\omega(M-1)/2}\frac{\sin(M\omega/2)}{M\sin(\omega/2)}.
\]

At (\omega=0), use the limit: (H(1)=1), so a constant signal is unchanged. Zeros occur at (\omega=2\pi r/M) for integer (r) except multiples of (M). The centered exponential factor gives linear phase and delay ((M-1)/2) samples. For (M=3),

\[
H(e^{j\omega})=\tfrac13 e^{-j\omega}(1+2\cos\omega),
\]

with zeros at (\omega=\pm2\pi/3) in the principal interval.

### 3.4 Transient and steady-state response

For a stable system driven by a sinusoid that starts at (n=0), the total output typically has two parts:

\[
y[n]=y_{ss}[n]+y_{tr}[n].
\]

The steady-state part oscillates at the input frequency and is determined using (H(e^{j\omega_0})). The transient part comes from system poles and initial/start-up conditions; for a stable system it decays. Do not treat the full response to a causal input as the steady-state sinusoid at every sample.

**Causal exponential example.** For (h[n]=(0.5)^nu[n]) and step input (x[n]=u[n]),

\[
y[n]=\sum_{k=0}^n(0.5)^k=2\big(1-(0.5)^{n+1}\big)u[n]
=\underbrace{2u[n]}_{\text{steady value}}-\underbrace{2(0.5)^{n+1}u[n]}_{\text{decaying transient}}.
\]

It begins at (y[0]=1) and approaches (2). More generally, for (x[n]=b^nu[n]), convolution with (h[n]=a^nu[n]) gives (y[n]=\sum_{k=0}^na^{n-k}b^k); if (a\ne b), this is ((a^{n+1}-b^{n+1})/(a-b)\,u[n]). If (a=b), it is ((n+1)a^nu[n]).

### 3.5 Filtering language

An ideal low-pass keeps a selected band and removes everything outside it; high-pass, band-pass, and band-stop filters select other frequency ranges. A moving average is a simple low-pass smoother. A filter with a sharp ideal cutoff often has an infinite-duration impulse response; practical filters trade cutoff sharpness, ripple, delay, and complexity.

## 4. Topic 2 — The z-transform

### 4.1 Definition and core pairs

The bilateral z-transform is

\[
X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}.
\]

Always give the **ROC** when identifying a transform. The same algebraic expression can represent different sequences with different ROCs.

| Sequence | Z-transform | ROC |
|---|---|---|
| (\delta[n]) | (1) | all (z) |
| (\delta[n-n_0]) | (z^{-n_0}) | (z\ne0) if (n_0>0) |
| (a^nu[n]) | (1/(1-az^{-1})) | (|z|>|a|) |
| (-a^nu[-n-1]) | (1/(1-az^{-1})) | (|z|<|a|) |

The last two rows have the same formula but different time support and ROC. This is why the ROC is part of the answer.

### 4.2 Properties used most often

| Time-domain operation | Z-domain result |
|---|---|
| (x[n-n_0]), delay by (n_0) | (z^{-n_0}X(z)) |
| (a^nx[n]) | (X(z/a)) |
| (x[n]*h[n]) | (X(z)H(z)) |
| (x[-n]) | (X(z^{-1})) |

For rational transforms, factor numerator and denominator. Roots of the numerator are zeros; roots of the denominator are poles. Poles determine the possible ROC boundaries.

### 4.3 Causality, stability, and the unit circle

For a rational (H(z)):

- **Causal** means the ROC is outside the outermost pole.
- **Stable** means the ROC includes the unit circle (|z|=1).
- A causal, stable rational system has every pole strictly inside the unit circle.
- The frequency response (H(e^{j\omega})) exists when the unit circle is in the ROC.

These checks are related but not interchangeable. A system may be causal and unstable; a noncausal system may be stable.

### 4.4 Analyze a system with the z-transform

For (y[n]-0.5y[n-1]=x[n]), assuming initial rest:

1. Transform both sides: (Y(z)-0.5z^{-1}Y(z)=X(z)).
2. Solve for the system function: (H(z)=Y(z)/X(z)=1/(1-0.5z^{-1})).
3. The pole is (z=0.5). Causality selects ROC (|z|>0.5).
4. Inverse-transform: (h[n]=(0.5)^nu[n]).
5. Since this ROC contains the unit circle, the system is stable and has the frequency response from Section 3.2.

With an input (x[n]=u[n]), use convolution or (Y(z)=H(z)X(z)), where (X(z)=1/(1-z^{-1})) for (|z|>1), and invert with partial fractions. Under initial rest, the result is (2(1-(0.5)^{n+1})u[n]).

**Initial conditions matter.** (H(z)=Y(z)/X(z)) describes the zero-state system (initial rest). If the problem supplies nonzero stored values, keep their extra terms when transforming the difference equation. Don't silently use the initial-rest formula.

## 5. Topic 3 — Frequency analysis of signals

### 5.1 Discrete-time Fourier transform (DTFT)

For an aperiodic sequence,

\[
X(e^{j\omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega n},\qquad
x[n]=\frac1{2\pi}\int_{-\pi}^{\pi}X(e^{j\omega})e^{j\omega n}\,d\omega.
\]

The DTFT is continuous in (\omega) and repeats every (2\pi): (X(e^{j(\omega+2\pi)})=X(e^{j\omega})). A time shift multiplies the spectrum by a phase factor: (x[n-n_0]\leftrightarrow e^{-j\omega n_0}X(e^{j\omega})). A finite sequence is often handled by applying the definition directly.

**Worked example.** Let (x[n]=\delta[n]+2\delta[n-1]). Then

\[
X(e^{j\omega})=1+2e^{-j\omega},\quad
|X(e^{j\omega})|=\sqrt{5+4\cos\omega},\quad
\angle X=\operatorname{atan2}(-2\sin\omega,1+2\cos\omega).
\]

Check the signs by substituting the samples into (\sum_nx[n]e^{-j\omega n}).

### 5.2 Periodic discrete-time signals and Fourier series

For an (N)-periodic sequence, one common discrete-time Fourier-series convention is

\[
x[n]=\sum_{k=0}^{N-1}C_k e^{j2\pi kn/N},\qquad
C_k=\frac1N\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}.
\]

There are only (N) distinct harmonics, indexed modulo (N). Some books put (1/N) in the synthesis equation instead; follow the convention used in the question and keep the pair consistent.

For a real cosine, (A\cos(\omega_0n+\theta)), use

\[
A\cos(\omega_0n+\theta)=\frac A2e^{j\theta}e^{j\omega_0n}+\frac A2e^{-j\theta}e^{-j\omega_0n}.
\]

So it consists of positive- and negative-frequency components. In discrete time, frequencies that differ by (2\pi k) are identical: (e^{j(\omega+2\pi k)n}=e^{j\omega n}). Use a principal interval such as ([-\pi,\pi)) when reporting unique frequencies.

### 5.3 Useful frequency-analysis properties

| Operation | Frequency-domain effect |
|---|---|
| (a x_1[n]+b x_2[n]) | (aX_1(e^{j\omega})+bX_2(e^{j\omega})) |
| (x[n-n_0]) | (e^{-j\omega n_0}X(e^{j\omega})) |
| (x[n]*h[n]) | (X(e^{j\omega})H(e^{j\omega})) |
| (x[n]e^{j\omega_0n}) | (X(e^{j(\omega-\omega_0)})) |

Parseval's relation connects energy in time and frequency:

\[
\sum_n|x[n]|^2=\frac1{2\pi}\int_{-\pi}^{\pi}|X(e^{j\omega})|^2\,d\omega.
\]

### 5.4 If the CTFT notes are in scope

The continuous-time Fourier transform uses ordinary time (t) and angular frequency (\Omega):

\[
X(j\Omega)=\int_{-\infty}^{\infty}x(t)e^{-j\Omega t}\,dt,\qquad
x(t)=\frac1{2\pi}\int_{-\infty}^{\infty}X(j\Omega)e^{j\Omega t}\,d\Omega.
\]

Unlike the DTFT, a general CTFT spectrum is not periodic. For $x(t)=e^{j\Omega_0t}$, the transform is $2\pi\delta(\Omega-\Omega_0)$; for $A\cos(\Omega_0t)$, it is $\pi A[\delta(\Omega-\Omega_0)+\delta(\Omega+\Omega_0)]$. Keep the $1/(2\pi)$ inverse-transform factor with this convention.

## 6. Common exam moves and errors

1. **For a system question:** write the difference equation, take the z-transform under stated initial conditions, find (H(z)), identify poles/ROC, then evaluate on (z=e^{j\omega}) only if allowed by the ROC.
2. **For a sequence spectrum:** write the nonzero samples and evaluate the DTFT sum term by term. Use Euler's identity to make magnitude/phase or sinusoidal components clear.
3. **For a filter question:** compute the finite sum for (H(e^{j\omega})), then identify DC gain, zeros, magnitude behavior, and delay/phase.
4. **For a response question:** distinguish the full causal response from steady state; show the transient term and its limiting behavior.
5. **For z-transform inversion:** state the ROC, then pick the right-sided or left-sided pair. An algebraic expression without an ROC may not determine a unique sequence.

Avoid these mistakes:

- Dropping the ROC or assuming every geometric sequence is right-sided.
- Claiming stability from pole locations before identifying causality/ROC.
- Evaluating (H(e^{j\omega})) when the unit circle is outside the ROC.
- Forgetting that (e^{-j\omega n_0}) is the factor for a delay (x[n-n_0]).
- Calling the response “steady state” while including the start-up transient.
- Mixing Hz, rad/s, and rad/sample, or forgetting DTFT periodicity.
- Using an inconsistent Fourier-series normalization.

## 7. Short self-check (answers included)

**A.** Find (H(z)), the causal impulse response, and stability for (y[n]-0.25y[n-1]=x[n]).

**Answer:** (H(z)=1/(1-0.25z^{-1})), ROC (|z|>0.25); (h[n]=(0.25)^nu[n]). The unit circle lies in the ROC, so it is stable.

**B.** Find the DTFT of (x[n]=3\delta[n]+\delta[n-2]).

**Answer:** (X(e^{j\omega})=3+e^{-j2\omega}). Its magnitude is \(\sqrt{10+6\cos(2\omega)}\).

**C.** Give the response of an (M=3) moving average to a constant input (x[n]=5), away from start-up boundaries.

**Answer:** DC gain is one, so the steady output remains 5. For a causal sequence beginning at (n=0), the first two outputs depend on how missing pre-start samples are treated; after the window is full, the output is 5.

**D.** For (h[n]=(0.5)^nu[n]) and (x[n]=u[n]), identify steady state and transient.

**Answer:** (y[n]=2-2(0.5)^{n+1}) for (n\ge0); steady value (2), transient (-2(0.5)^{n+1}), which decays to zero.

## 8. 45-minute exam approach

The note says Q1 is the quiz question and Q2–Q3 are the term-test questions. Since there are three topics in three questions, budget roughly 12–13 minutes per question and reserve the last 5 minutes to check signs, ROCs, and arithmetic. If you finish the quiz question early, move on as the note says.

On each solution, make the method visible: formula → substitution → simplified answer → one interpretation/check. For system problems, a boxed ROC and a one-sentence stability/causality conclusion are quick, high-value checks. For frequency response, report both magnitude and phase if asked; for frequency analysis, clearly state whether the answer is a DTFT, Fourier-series coefficient set, or CTFT.

### Suggested review order

1. Memorize transform pairs, ROC rules, and the relation (H(e^{j\omega})=H(z)|_{z=e^{j\omega}}).
2. Work difference-equation → (H(z)) → impulse response → stability/frequency response examples.
3. Practice direct DTFT sums and one periodic Fourier-series coefficient calculation.
4. Re-derive the moving-average response and a step/exponential response from convolution.
5. Use Assignment 4 and the Chapter 4.8.6/4.8.7 material for worked exercises; use the Python `practice/` files as visual review, not as a substitute for the newer written syllabus.
