# Traps, tricks and the intuition that saves you

Read this **after** the tutorials (20–23), and once more on Sunday morning. Each entry has three parts:
**the blunder** (what goes wrong under pressure), **the picture** (an intuition you can rebuild in the hall),
and **the trick version** (how sir can twist the same question). A ✔ line gives a 5-second check.

Sir's habit: he takes a textbook example and changes **one** thing, such as the arrow position, the sign of a,
the ROC, "for all n" versus "u[n]", or the method demanded. Before writing, circle what is different from the book.

All new numbers here are checked with numpy (long division, three-ROC inverse, one-sided z, powers).

---

## A. Convolution and sequences (TT1 hurt here)

### A1. Where is n = 0? (the arrow)
**Blunder:** treating the first number as n = 0 when the arrow is elsewhere.
**Picture:** the arrow is the "you are here" pin. Everything left of it is negative time.
**Rule:** start of y = start of x + start of h. In TT1, x starts at 0 and h at −1, so y starts at −1. The answer {1, 4, 8, …} then has the arrow on **4**, not 1.
**Trick version:** the same numbers with the arrow moved shift the answer only. The values don't change, so recompute just the start index.
✔ Length = N₁ + N₂ − 1, and Σy = Σx · Σh.

### A2. x(−n + 2): fold first, or shift first?
**Blunder:** shifting the wrong way (TT1 Q1 ii).
**Picture:** don't think about "operations". Ask where each sample lands: set the argument equal to k, so **−n + 2 = k ⇒ n = 2 − k**. Sample x(k) moves to position 2 − k.
So x(0) lands at n = 2, x(1) at n = 1, x(−1) at n = 3.
In operation language: x(−n+2) = x(−(n−2)), so fold, then shift the folded signal **right** by 2.
✔ Plug in one sample: the x(0) value must sit at n = 2.

### A3. Infinite convolution: the limits
**Blunder:** writing Σ from −∞ to ∞ and getting stuck, or forgetting "for n < 0, y = 0".
**Picture:** u(k) is a gate that opens at k = 0, and u(n−k) is a gate that closes at k = n. You only sum while both gates are open: **0 ≤ k ≤ n**. If n < 0 the window is empty, so y = 0.
**Trick version:** h = aⁿu(n−2). The gate now opens at k = 2, so the sum is over 2 ≤ k ≤ n and y = 0 for n < 2.

---

## B. Topic 1: frequency response (Q1)

### B1. "Steady state" when there's no transient
**Blunder:** writing a transient for x = A cos(ω₀n), −∞ < n < ∞.
**Picture:** a transient is the system's "surprise" at the moment the input is switched on. If the input has been running forever (no u[n]), there is no switch-on moment and no surprise: **y = y_ss exactly**.
With u[n] there is a transient, and it dies only if the system is stable.
**Trick version (final 5c):** "x = A cos(ω₀n), −∞<n<∞". Answer y = A|H(e^{jω₀})|cos(ω₀n + θ(ω₀)) and stop there.

### B2. tan⁻¹ lies about the quadrant
**Blunder:** H = −1 − j → tan⁻¹(1) = 45°. Wrong: the angle is **−135°**.
**Picture:** draw the point. Re < 0 and Im < 0 is the bottom-left quadrant, so ±180° must be applied.
**Rule:** if H_R < 0, θ = tan⁻¹(H_I/H_R) ± 180°.
✔ Check with the example from 20-T1 §3a: H(e^{jπ/4}) = −1.586 − 2.071j has θ = −127.4°, not +52.6°.

### B3. sin input, not cos
**Blunder:** writing cos in the answer when the input was sin(ω₀n) (Mitra 4.68).
**Picture:** the system only scales and delays, so it **can't change sin into cos**. Whatever wave goes in comes out.
y = |H| sin(ω₀n + θ). And if the input carries its own phase φ, keep it: A cos(ω₀n + **φ + θ**).

### B4. Moving average with even M
**Blunder:** "delay = M/2", or ignoring the case where M is even.
**Picture:** the moving average's output is the average of a window, so it "belongs" to the centre of the window. The window covers n, n−1, …, n−(M−1), whose centre is **(M−1)/2** samples back. M = 4 gives a delay of **1.5** samples. A half-sample delay is fine on paper.
✔ Zeros of |H| are at 2πk/M. For M = 4 that is π/2 and π, so the filter nulls ω = π exactly when M is even.

### B5. Why the MA phase "jumps"
**Blunder:** drawing a straight line −(M−1)ω/2 all the way.
**Picture:** H = (real number R(ω)) × e^{−jω(M−1)/2}. When R goes negative after a zero, "negative" = "multiply by e^{jπ}", so the phase gets +π added. It is not a mistake, just bookkeeping for the sign.
Write: θ(ω) = −(M−1)ω/2 + π·(number of zeros below ω).

### B6. "A system creates new frequencies" means it is not LTI
**Picture:** an LTI system is a set of volume knobs, one per frequency. Knobs can turn a frequency up, down or off, but **can never add one**. Squaring, multiplying by cos and down-sampling (x[4n]) all add frequencies, so they are not LTI (Mitra 4.60).
**Trick version:** "Is y = x²[n] characterised by a frequency response?" No. It is not LTI, so H(e^{jω}) is meaningless.

### B7. ω beyond π is the same as a lower ω
**Blunder:** treating cos(1.5πn) as a high-frequency signal.
**Picture:** a DT frequency lives on a circle. 1.5π lands on the same spot as 1.5π − 2π = −0.5π, so cos(1.5πn) = cos(0.5πn).
✔ Always reduce ω into (−π, π] before reading |H|. Highest DT frequency = π, i.e. (−1)ⁿ.

### B8. "Eigenfunction" trick (4.54)
zⁿ (all n) is an eigenfunction. zⁿu[n] is **not**: switching on at n = 0 adds a transient, so the output isn't exactly H·input. Same idea as B1.

---

## C. Topic 2: z-transform (Q2)

### C1. ROC side, in one sentence
**Picture:** z⁻ⁿ with large |z| crushes the right side (n → +∞) and blows up the left side. So **the right-sided part needs |z| big (outside a circle) and the left-sided part needs |z| small (inside)**. A two-sided signal needs both, which gives a ring.
✔ The ROC is bounded by poles and never contains one.

### C2. H(z) given **without** an ROC: three different answers ★ trick
H(z) = 1/[(1 − 0.5z⁻¹)(1 − 2z⁻¹)] = (−1/3)/(1 − 0.5z⁻¹) + (4/3)/(1 − 2z⁻¹)

| ROC | h[n] | causal? | stable? |
|---|---|---|---|
| \|z\| > 2 | −(1/3)(0.5)ⁿu[n] + (4/3)2ⁿu[n] | yes | **no** (2ⁿ blows up) |
| 0.5 < \|z\| < 2 | −(1/3)(0.5)ⁿu[n] − (4/3)2ⁿu[−n−1] | no | **yes** (contains \|z\| = 1) |
| \|z\| < 0.5 | (1/3)(0.5)ⁿu[−n−1] − (4/3)2ⁿu[−n−1] | anti-causal | no |

Checked: the ring version summed at z = 1 equals H(1) = −2.
**If he asks "find h[n] such that the system is stable":** pick the ROC that contains the unit circle, which is the ring. If he says "causal": outside the largest pole. If he gives no ROC and no condition: list all three, and he'll love it.
Rule for each term: a pole p in the "outside" part gives pⁿu[n]; a pole in the "inside" part gives −pⁿu[−n−1].

### C3. Partial fractions: divide by z first
**Blunder:** doing partial fractions on X(z) directly in z, and getting a constant or the wrong shape.
**Picture:** the table entry is **z/(z − p)** ↔ pⁿu[n]. Dividing by z first guarantees each term comes back as z/(z−p) after you multiply by z again.
**Improper case:** if X(z) (in powers of z⁻¹) has the numerator degree ≥ the denominator degree, divide polynomials first. The quotient gives δ terms. The X(z)/z trick handles the "equal degree" case automatically.

### C4. Repeated poles: don't drop a term
A double pole at p needs **two** terms, B/(z−p) + C/(z−p)². The second becomes n·pⁿu[n] (via n aⁿu[n] ↔ az⁻¹/(1−az⁻¹)²; watch the extra factor of a).
✔ Check x[0] = lim_{z→∞} X(z) for causal signals (initial value theorem). In 21-T2 §8c: X(∞) = 1, and 4/9 + 5/9 + 0 = 1 ✔.

### C5. Sign inside (1 + 2z⁻¹)
1/(1 + 2z⁻¹) = 1/(1 − (−2)z⁻¹) ↔ **(−2)ⁿ**u[n]. The pole is at z = −2. (Your note slipped exactly here.)
✔ Find the pole by solving the bracket = 0: 1 + 2z⁻¹ = 0 ⇒ z = −2.

### C6. Shifted and flipped versions sir can swap in
| x[n] | X(z) | ROC |
|---|---|---|
| aⁿu[n−1] | az⁻¹/(1 − az⁻¹) | \|z\| > \|a\| |
| a^{n−1}u[n−1] | z⁻¹/(1 − az⁻¹) | \|z\| > \|a\| |
| u[−n] | 1/(1 − z) | \|z\| < 1 |
| a^{\|n\|} (\|a\|<1) | 1/(1−az⁻¹) + az/(1−az) | \|a\| < \|z\| < 1/\|a\| |
| (n+1)aⁿu[n] | 1/(1 − az⁻¹)² | \|z\| > \|a\| |
**Method for any of these:** write it as a known pair, then apply shift (z^{−k}), scaling (aⁿ → z/a), or reversal (z → 1/z, which flips the ROC).

### C7. Inverse by long division (gap filled — Proakis Ex 3.4.x)
X(z) = 1/(1 − 1.5z⁻¹ + 0.5z⁻²)
**ROC |z| > 1 (causal):** divide in **ascending powers of z⁻¹**:
→ 1 + 1.5z⁻¹ + 1.75z⁻² + 1.875z⁻³ + … ⇒ **x = {1↑, 1.5, 1.75, 1.875, 1.9375, …}**
**ROC |z| < 0.5 (anti-causal):** write the denominator in **ascending powers of z** (0.5z⁻² − 1.5z⁻¹ + 1) and divide:
→ 2z² + 6z³ + 14z⁴ + 30z⁵ + … ⇒ **x = {…, 30, 14, 6, 2, 0, 0↑}**
**Picture:** causal means the series must run toward z⁻¹ (future samples). Anti-causal means it must run toward z (past samples). The ROC tells you which direction to divide.
Long division gives numbers, not a closed form. Use it when he says "first few samples", or when the poles are ugly.
✔ Closed form for the causal case: 2 − (0.5)ⁿ, which gives 1, 1.5, 1.75 ✔.

### C8. Difference equation with initial conditions (one-sided z, Proakis 3.6) (gap filled)
**Blunder:** using the two-sided shift z⁻¹Y(z) when y(−1) ≠ 0.
**Rule (one-sided):** Z⁺{y(n−1)} = z⁻¹Y⁺(z) + **y(−1)**;  Z⁺{y(n−2)} = z⁻²Y⁺(z) + z⁻¹y(−1) + y(−2).
**Example:** y(n) = 0.5y(n−1) + x(n), x = u(n), y(−1) = 1.
> Y = 0.5[z⁻¹Y + 1] + 1/(1 − z⁻¹) ⇒ Y(1 − 0.5z⁻¹) = 0.5 + 1/(1 − z⁻¹)
> Y = 0.5/(1 − 0.5z⁻¹) + 1/[(1 − 0.5z⁻¹)(1 − z⁻¹)] = 0.5/(1−0.5z⁻¹) + [2/(1−z⁻¹) − 1/(1−0.5z⁻¹)]
> **y(n) = 2 − (0.5)^{n+1}, n ≥ 0**
✔ Recursion by hand: y(0) = 0.5·1 + 1 = 1.5, y(1) = 1.75. The formula gives 1.5, 1.75 ✔.
**Picture:** the initial condition is "energy already stored" in the system. It shows up as an extra term that decays (the zero-input response). The rest is the zero-state response.

### C9. Stability vs causality: they are separate
Causal ⇔ ROC outside the outermost pole (and includes ∞). Stable ⇔ ROC contains |z| = 1.
"Poles inside the unit circle ⇒ stable" holds **only for causal systems**. Say "causal and stable ⇔ all poles inside".

### C10. Counting poles and zeros at the origin
Convert to positive powers of z before counting. 1/(1 − az⁻¹) = z/(z − a) has a **zero at z = 0**, which people forget to draw. In final 6b, the (M−1)-fold pole at the origin carries the marks; label it "(M−1)".

---

## D. Topic 3: frequency analysis (Q3)

### D1. Is a DT sinusoid periodic? ★ trick
**Blunder:** "cos is periodic, so of course it is".
**Picture:** a DT sinusoid repeats only if after N steps it has turned through a whole number of full circles: ω₀N = 2πk, i.e. **f₀ = ω₀/2π = k/N must be rational**.
- cos(πn/3): f₀ = 1/6, so N = 6 ✔
- cos(√2πn): f₀ = 1/√2 is irrational, so **not periodic**
- **cos(n/6): f₀ = 1/(12π) is irrational, so NOT periodic**, even though cos(t/6) in CT is. A favourite trick.
- Sum cos(πn/3) + cos(πn/4): N₁ = 6, N₂ = 8, so **N = lcm = 24**.
- Final 1d: sin(5πn) and √3cos(5πn): f₀ = 5/2 → N = 2 for both, so the common period is **2**.

### D2. Energy or power?
| x[n] | Energy | Power | Type |
|---|---|---|---|
| aⁿu[n], \|a\|<1 | 1/(1−a²) (a=0.5 → 1.333) | 0 | energy |
| u[n] | ∞ | **½** (not 1!) | power |
| (−1)ⁿ, A cos(ω₀n) | ∞ | 1, A²/2 | power |
| nu[n] | ∞ | ∞ | neither |
**Picture:** power = average over a window from −N to N. u[n] is "on" for only half of that window, so P = ½.
✔ Finite energy ⇒ power 0. Finite non-zero power ⇒ energy ∞.

### D3. The 1/2π factors (Parseval)
- DT aperiodic: Σ|x|² = **(1/2π)**∫_{−π}^{π}|X(ω)|²dω
- DT periodic: (1/N)Σ|x|² = Σ|c_k|² (no 2π)
- CT in F (Hz): ∫|x|²dt = ∫|X(F)|²dF (no 2π). In Ω: (1/2π)∫|X(Ω)|²dΩ.
**Picture:** a 2π appears whenever the frequency variable is in radians, because one full turn of radians "costs" 2π. In Hz it doesn't.

### D4. CTFS vs DTFS ranges
CTFS has infinitely many c_k (k from −∞ to ∞). DTFS has only **N** distinct c_k (k = 0…N−1), because c_{k+N} = c_k.
**Picture:** a DT signal can't wiggle faster than (−1)ⁿ, so there are only N different "speeds" available.
**Trick:** "find c₇ for N = 6" → c₇ = c₁.

### D5. DTFT that doesn't exist
2ⁿu[n] (it grows) and u[n] (pole **on** the unit circle) have no ordinary DTFT. **Reason to write:** not absolutely summable / the ROC doesn't include |z| = 1. Their z-transforms exist.
Use this sentence whenever he asks you to "use the frequency domain" on a growing signal.

### D6. Square-wave variants
- ±1 even square wave: c₀ = 0, c_k = (2/kπ)sin(kπ/2).
- 0/1 square wave (same timing): it equals ½(±1 version + 1), so **c₀ = ½** and c_k = (1/kπ)sin(kπ/2).
- Shifted by T₀/4 (odd symmetry instead of even): magnitudes stay the same and only the phases change (time shift ↔ phase, the T3 §7 property).
**Picture:** shifting in time never changes *how much* of each harmonic there is, only *when* it peaks.

### D7. Wider pulse, narrower spectrum
Rect width τ → first zero at F = 1/τ. Double τ and the spectrum halves in width while its peak height Aτ doubles. If he asks "what happens to the spectrum if the pulse widens?", that is the answer, with this picture: long in time ⇔ narrow in frequency.

---

## E. Exam-hall habits (each one has cost someone marks)

1. **Write the formula before the numbers.** The formula line alone is often a mark.
2. **Box the final answer with its conditions:** n ≥ 0, ROC, |a| < 1.
3. **Read the verb:** *determine* (show working), *sketch* (draw it), *using z-transform* (that method only), *explain* (words + one formula + one picture).
4. **Every z-answer carries an ROC. Every DTFT answer checks that the DTFT exists.**
5. **If you're stuck, write definition → general formula → first step with his numbers.** Partial method beats a blank page.
6. **Time:** 45 min for 30 marks = 1.5 min per mark. A 5-mark part gets about 7 minutes. If you're over, write the method in words and move on.
