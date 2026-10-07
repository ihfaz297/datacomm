# Tutorial 13 — FIR low-pass design by the window method

Covers TT2 **Q2** (design discussion, 5 marks) and **Q4** (roll-off / stop-band attenuation / ripple,
5 marks), plus final-paper Q2b, Q2d and Q3a. Pairs with `DSP/practice/step13_fir_window.py`.

---

## §1 Why an ideal filter cannot be built (final Q2d — a 5-mark prose question)

The ideal lowpass is the **brick wall**: |H| = 1 for |w| ≤ wc and 0 above, with a vertical transition.

```text
h_d[n] = (1/2pi) int_{-wc}^{wc} e^(jwn) dw = sin(wc n) / (pi n)        <-- a sinc, in BOTH directions
```

Three reasons it is physically unrealisable, and each is a mark:

1. **It is infinite in length.** The sinc decays like 1/n but never ends, so it needs an infinite number of
   taps and infinite delay, and the filter would have to know all future samples.
2. **It is non-causal.** h_d[n] ≠ 0 for n < 0, so the output would depend on inputs that have not happened
   yet (the sharp transition in frequency is what demands this).
3. **The transition is instantaneous** — zero width — which is the frequency-domain version of a step, and
   a step in the frequency response corresponds to an infinitely long, slowly decaying impulse response
   (Paley–Wiener). Truncation is the only remedy, and truncation creates ripples (Gibbs).

Practical designs therefore accept a **finite transition band** and **finite attenuation**; that is exactly
what the window method delivers.

---

## §2 The design recipe (memorise these five lines — they are TT2 Q2)

```text
1. IDEAL:    h_d[n] = sin(wc (n - M/2)) / (pi (n - M/2)) ,  n = 0 .. M     (M even -> M+1 taps)
             h_d[M/2] = wc / pi                    <- the 0/0 sample, evaluated by the limit
2. WINDOW:   choose w[n] of the same length M+1 (rect / Hann / Hamming / Blackman / Kaiser)
3. MULTIPLY: h[n] = h_d[n] * w[n]                 <- this IS the finished FIR filter
4. NORMALISE: h /= sum(h)  if you want H(0) = 1 exactly (optional but honest)
5. CHECK:    H(e^jw) = DTFT of h[n];  |H| vs the spec (cutoff, transition, attenuation, ripple)
```

Two facts behind step 1 that earn marks: the **shift by M/2** makes h[n] causal *and* symmetric, which is
what gives exact linear phase with group delay M/2; and h_d[M/2] = wc/π because sin(x)/x → 1 as x → 0.

Fact behind step 3: multiplying in the time domain = **convolving with the window's spectrum** in the
frequency domain. So the designed |H| is the brick wall "smeared" by the window's mainlobe (that widening
*is* the transition band) and shaken by its sidelobes (those *are* the stopband ripples).

---

## §3 Worked design example 1 — 5 taps, wc = π/2, rectangular window

**Step 1 — the ideal taps.** M = 4 (so 5 taps), M/2 = 2, wc = π/2. For each n, k = n − 2:

| n | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| k = n − 2 | −2 | −1 | 0 | 1 | 2 |
| sin(πk/2) | sin(−π) = 0 | sin(−π/2) = −1 | 0/0 → use wc/π | sin(π/2) = 1 | sin(π) = 0 |
| h_d[n] | 0 | 1/π = 0.3183 | **wc/π = 0.5** | 0.3183 | 0 |

**h_d = {0, 0.3183, 0.5, 0.3183, 0}** — symmetric about n = 2 ✓ (the symmetry is the linear-phase guarantee).

**Step 2 — the rectangular window is just w[n] = 1**, so the design is done: h[n] = h_d[n].

**Step 3 — check H(0), which must be the sum of the taps:**

```text
H(0) = 0 + 0.3183 + 0.5 + 0.3183 + 0 = 1.1366      -- not 1!
```

That 13.66 % overshoot is the **truncation error** — the same reason the passband of a boxcar filter has
ripple. Normalise if you want unity DC gain: **h = {0, 0.2800, 0.4399, 0.2800, 0}** (divide by 1.1366,
machine-checked). Saying why you normalise is worth a mark.

**Step 4 — the honest caveat.** Five taps is far too short for a real filter: the transition band of a
rectangular window is 1.8π/M = 1.8π/4 = 0.45π — nearly half the band. This example is *arithmetic practice*;
the numbers you should quote in the discussion are the M = 30 ones in §5.

---

## §4 Worked design example 2 — same 5 taps with a Hann window

Hann for M = 4: w[n] = 0.5 − 0.5cos(2πn/4) = 0.5 − 0.5cos(πn/2):

| n | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| w[n] | 0.5 − 0.5(1) = 0 | 0.5 − 0.5(0) = 0.5 | 0.5 − 0.5(−1) = 1 | 0.5 | 0 |
| h_d[n] | 0 | 0.3183 | 0.5 | 0.3183 | 0 |
| h[n] = h_d·w | 0 | **0.1592** | **0.5** | **0.1592** | 0 |

**DC gain: H(0) = 0.8183** (machine-checked), so normalised: **h = {0, 0.1945, 0.6110, 0.1945, 0}**.

Read what the window did: it **killed the end taps** (both were already 0 here because wc = π/2 puts zeros of
the sinc at the edges) and it **scaled the inner taps down**. In a longer filter the effect is dramatic:
the taps nearest the ends are the ones that cause the ringing, and the taper suppresses them. That is the
whole idea of the window method in one sentence.

---

## §5 The measured window table (M = 30, 31 taps, wc = 0.4π)

These are the numbers to quote. They come from `step13_fir_window.py`, which designs each filter with the
recipe above and then *measures* |H| on a 4001-point grid instead of trusting the textbook.

| Window | w[n] | Stopband attenuation (measured) | Transition width (measured) | Window mainlobe | In-band ripple (measured) |
|---|---|---|---|---|---|
| Rectangular | 1 | **21.22 dB** | 0.0598π | 0.1290π | **0.6297 dB** |
| Hann | 0.5 − 0.5cos(2πn/M) | **43.95 dB** | 0.1295π | 0.2665π | 0.0243 dB |
| Hamming | 0.54 − 0.46cos(2πn/M) | **53.56 dB** | 0.1217π | 0.2795π | 0.0329 dB |
| Blackman | 0.42 − 0.5cos(2πn/M) + 0.08cos(4πn/M) | **75.21 dB** | 0.1585π | 0.4000π | 0.0031 dB |

Textbook values for the attenuation are 21 / 44 / 53 / 74 dB — the measurements match within 1 dB, which is
the standard check. **All four designs came out exactly linear phase** (the drill tests
imag(H·e^{jwM/2}) and gets ~1e-15 for every window), because h[n] is symmetric about M/2.

**The order law (measured, not assumed).** Hamming, M = 30 vs M = 60 at the same cut-off:

```text
transition width: 0.1217pi  ->  0.0610pi     HALVED (transition ~ 1/M)
attenuation     : 53.56 dB ->  53.72 dB     UNCHANGED
```

So: **M buys transition sharpness; the window buys attenuation.** Memorise that sentence — it is the answer
to TT2 Q4 and to half of Q2.

**How the textbook numbers arise.** Rectangular window: its Fourier transform is the Dirichlet kernel, whose
first sidelobe is only 13 dB down → 21 dB of stopband attenuation and 0.63 dB of Gibbs ringing. Hann/Hamming/
Blackman are cosine sums that make the window go smoothly to zero at both ends, dropping the sidelobes to
−31/−43/−58 dB, hence 44/53/75 dB of attenuation — at the price of a 2–2.7× wider mainlobe (a wider
transition).

---

## §6 What every parameter does (TT2 Q4, 5 marks — write this table)

| Change this | Roll-off (transition) | Stop-band attenuation | Ripple |
|---|---|---|---|
| **Window shape** (M fixed) | Rectangular is the narrowest (0.0598π at M = 30). Smoother windows widen it: Hann 0.1295π, Hamming 0.1217π, Blackman 0.1585π | Rectangular 21.2 dB, Hann 44.0, Hamming 53.6, Blackman 75.2 dB — set by the window's peak sidelobe, nothing else | Rectangular 0.63 dB (Gibbs); Hann 0.024, Hamming 0.033, Blackman 0.003 dB |
| **Order M** (window fixed) | transition ≈ c/M: doubling M halves it (Hamming 0.1217π → 0.0610π for M 30 → 60) | unchanged (53.56 → 53.72 dB) | worst ripple unchanged; more ripples fit inside the same band |
| **Cut-off wc** | slides the transition band left/right | unchanged | unchanged |
| **Kaiser β** (extra knob, same M) | β trades transition against attenuation continuously | β sets it directly (~ β → attenuation) | β also trades ripple against attenuation |

Plus the qualitative lines a grader is looking for:

- A **narrow transition** = sharp roll-off = a "brick-wall-like" filter. It needs a large M: more taps, more
  computation, more memory and — critically — **more delay (group delay = M/2 samples)**.
- A **wide transition** = cheap, few taps, low latency, but it cannot separate close frequencies.
- **Attenuation is a function of the window only.** No amount of extra order moves it; you must change the
  window (or use a Kaiser with a different β).
- Ripple and attenuation improve together with smoother windows, but the transition gets worse — you cannot
  improve all three at a fixed length, which is why the Kaiser window parameterises the trade-off with β.

---

## §7 Narrow vs wide transition band (final Q3a, 10 marks)

**Roll-off** is how fast |H| falls from the passband to the stopband — the slope of the transition band, or
equivalently how narrow the transition band is. A filter with a narrow transition band is described as having
a "sharp roll-off" or being "close to ideal".

| | Narrow transition band | Wide transition band |
|---|---|---|
| Order M required | large (transition ∝ 1/M) | small |
| Delay | large (M/2 samples) | small |
| Computation / memory | large | small |
| Selectivity | high — can separate closely spaced frequencies (e.g. 1 000 Hz vs 1 100 Hz) | low — will pass/attenuate both |
| Best used when | signal and interference are close in frequency, or a strict spec is given | the interferer is far from the band of interest; low-latency or cheap hardware |
| Design effort | more taps, more arithmetic in the design and more to verify | trivial |
| Numeric examples (M = 30) | rectangular 0.0598π with only 21 dB attenuation | Blackman 0.1585π with 75 dB attenuation |

**The decision procedure to write down:** (1) fix wc from the band edges; (2) pick the window whose
attenuation meets the stopband spec (44 dB → Hann, 53 dB → Hamming, 75 dB → Blackman); (3) compute the order
from the required transition width, using Δw in rad/sample: **M ≈ 6.2π/Δw (Hann), 6.6π/Δw (Hamming),
11π/Δw (Blackman)**; (4) implement h[n] = h_d[n]w[n] and verify |H|.

Worked sizing example: 50 dB attenuation required (Hann's 44 dB is not enough, so Hamming) with a transition
of Δw = 0.1π rad/sample → M = 6.6π/0.1π = **66, i.e. 67 taps, group delay M/2 = 33 samples**. That is the
number to hand in.

If a narrow transition *and* the longest M you can afford are still not enough, move to an equiripple
(Parks–McClellan/Remez) design, or use a Kaiser window with an optimal β — that is the honest answer for
the last mark.

---

## §8 Pass-band and stop-band ripple (final Q2b, 5 marks)

**What the two ripples are.** |H| is not flat in the passband (±δp around 1 — measured here as 0.63 dB for the
rectangular window) and not flat in the stopband (it oscillates between 0 and −δs — measured as −21.2 dB worst
case). Both come from the same cause: truncation is multiplication by a window, and the window's sidelobes
spill everywhere after the convolution.

**Effects of pass-band ripple:** frequencies *inside* the band are not amplified equally, so the filter
distorts the wanted signal (amplitude distortion, and with the phase variation, waveform distortion). In audio
it is audible colouration; in a measurement channel it is a systematic error. If a spec says "passband ripple
≤ 0.1 dB", the rectangular window (0.63 dB) fails and Hann (0.024 dB) passes.

**Effects of stop-band ripple:** the unwanted frequencies are *not removed*, only reduced — and the ripple
means the *worst case* decides whether the spec is met. A −53 dB spec with a −40 dB ripple peak leaks the
interferer through; sidelobes far from the cutoff also leave broadband noise, so the stopband must be quoted
as worst-case attenuation, never as an average.

**The trade to state:** making the window smoother (a) reduces both ripples and (b) widens the mainlobe, hence
widens the transition band. That is the fundamental fixed-order trade — which is why Blackman reaches 75 dB
with only 0.003 dB of ripple, at the cost of the widest transition of the four (0.1585π vs 0.0598π for the
rectangular window at the same M = 30).

---

## §9 Traps

- **Not centring h_d at M/2.** The shift makes the filter causal and the phase exactly linear; without it the
  design is not what the question asked for.
- **Forgetting h_d[M/2] = wc/π.** Write "the 0/0 sample is evaluated by the limit sin(x)/x → 1, giving wc/π" —
  that sentence is a mark.
- **Windows of the wrong length.** w[n] has exactly M+1 samples, using n = 0…M (so 2πn/M inside the cosines,
  not 2πn/(M+1)). Mixing those is the commonest numerical slip.
- **Quoting attenuation as if M changed it.** M changes the transition only (measured 53.56 → 53.72 dB).
- **Forgetting to normalise, or not saying why you did not.** A design with H(0) = 1.1366 has 1.1 dB of gain error.
- **Claiming an ideal filter is achievable with enough taps.** It is not: non-causal, infinitely long, and its
  transition has zero width.

---

## §10 Practice set (answers below — cover them)

1. Design a 5-tap low-pass with wc = π/2 using the rectangular window: give h[n] and H(0).
2. The same design with the Hann window: give h[n], H(0) and the normalised taps.
3. Why is the k = 0 tap h_d[M/2] = wc/π and not 0/0?
4. Why must h_d be centred at M/2?
5. A spec needs 60 dB of stopband attenuation. With the measured numbers, which windows qualify?
6. 50 dB attenuation and Δw = 0.1π are required. Which window, and what order?
7. Which window gives the narrowest transition at M = 30, and what does it cost?
8. For an M = 30 rectangular design, is the −6 dB point exactly at wc? Explain.
9. Why does the rectangular window give only ~21 dB, and where does 13 dB come from?
10. State the passband-ripple and stopband-ripple effects in one sentence each.

**Answers.**

1. h_d = h = **{0, 1/π, 0.5, 1/π, 0}** = {0, 0.3183, 0.5, 0.3183, 0}; H(0) = **1.1366** (13.7 % overshoot —
   normalise to {0, 0.2800, 0.4399, 0.2800, 0} for unity DC gain).
2. w = {0, 0.5, 1, 0.5, 0} → h = **{0, 0.1592, 0.5, 0.1592, 0}**, H(0) = **0.8183**, normalised
   **{0, 0.1945, 0.6110, 0.1945, 0}**.
3. Because sin(wc·0)/(π·0) is 0/0, and the limit of sin(x)/x as x → 0 is 1, so the tap is wc/π — which is also
   the DC gain of the ideal lowpass divided by 2π.
4. So that h[n] is even-symmetric about M/2, which makes H(e^jw) exactly linear phase with constant group
   delay M/2 samples — and it makes the filter causal, as a real-time implementation requires.
5. **Blackman (75.2 dB) qualifies**; Hann (43.95 dB) and Hamming (53.56 dB) do not, and the rectangular window
   (21.2 dB) is far off. A Kaiser window with a large enough β would also qualify.
6. **Hamming** (53.6 dB > 50 dB, while Hann's 44 dB fails) → M ≈ 6.6π/0.1π = **66** (67 taps, delay 33 samples).
7. **Rectangular**, 0.0598π at M = 30. It costs the worst attenuation (21.2 dB) and the worst ripple
   (0.63 dB of Gibbs ringing) of the four.
8. Not exactly, but close: h_d is truncated and windowed, so |H| is the ideal response convolved with the
   Dirichlet kernel, which spreads the transition over ≈1.8π/M ≈ 0.06π. The −6 dB point therefore lands
   within about half a transition width of wc.
9. The rectangular window's spectrum is the Dirichlet kernel sin(wN/2)/sin(w/2), whose first sidelobe is only
   13 dB below the mainlobe; convolving the ideal brick wall with that kernel leaves stopband peaks about
   13 dB down, and the measured worst case is 21.2 dB because wc and M place the evaluated points between the
   sidelobe peaks.
10. Passband ripple: different in-band frequencies get different gains, so the wanted signal is distorted.
    Stopband ripple: the unwanted frequencies are only attenuated, not removed, and the worst-case sidelobe
    peak decides whether the spec is satisfied.

Check yourself in `DSP/practice/step13_fir_window.py` — it prints the four attenuation / transition / ripple
numbers, the exact linear-phase error, and the 1/M law for Hamming.



