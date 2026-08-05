# Ch4 — Digital Transmission: line coding + PCM (2.5 hrs)

Two halves. First half is **drawing** (line coding — past paper Q13, Q14 tested exactly
this). Second half is **the quantization/encoding math you flagged as the hot topic**
(PCM — §4.2.1). Verified against your PDF, printed pages 96–125.

---

## PART 1 — Line coding (§4.1)

### 1.1 Why line-code at all? (past paper Q8b, 1 mark, pure list — memorize 5 of 6)

"Digital data is already digital — why convert to a digital *signal*?" The desirable
properties a line-coding scheme must engineer in:

1. **Baseline wandering** — long runs of same bit drift the receiver's running average
   (baseline), corrupting decoding. Good schemes prevent it.
2. **DC components** — near-zero frequencies can't pass transformers/telephone lines.
   Want no DC.
3. **Self-synchronization** — transitions in the signal let the receiver reset its
   clock (sender/receiver clocks are never perfectly matched).
4. **Built-in error detection** — some invalid patterns reveal transmission errors.
5. **Immunity to noise and interference**.
6. **Complexity** (cost) — fewer levels = cheaper/simpler.

### 1.2 Data rate vs signal rate — the r, N, S vocabulary

```
r = data elements per signal element (bits per baud)
N = data rate (bps)         S = signal rate (baud) = c × N × (1/r),  c usually ½ (average)
Bmin (bandwidth needed) = c × N × (1/r) = S
```

Book Example 4.1: r = 1, N = 100 kbps, c = ½ → S = **50 kbaud**.
Book Example 4.4: NRZ-I at... careful, the book's own numbers: N = 1 Mbps → S = N/2 =
500 kbaud → Bmin = 500 kHz. **The bandwidth is set by the BAUD rate, not the bit rate.**

### 1.3 The schemes you must be able to DRAW — **and DECODE**

⚠ **Heads up (verified from the actual past-paper images): Q13/Q14 give you a
WAVEFORM and ask you to read the bits OFF it — the reverse of drawing.** Learn the
encode direction here, then run the decode drills in `04-diagram-drills.md` §D1 (the
past paper's exact waveforms are rendered in `figs/pastpaper_p5.png` and `p6.png`).
Same rules, opposite direction; decode is faster once encoding is solid.

Drill order — do each on paper for the byte **11000100**, then for **10011001**:

**NRZ-L (level codes the bit):** high voltage = one bit value, low = the other,
for the whole bit slot. (Book convention: positive = 1... but exams state their own —
read the legend they give you.)

**NRZ-I (invert = 1):** **transition at the START of the bit slot if the bit is 1;
no transition if 0.** The level itself means nothing — *change* means 1.
- Past paper Q14: 10011001, starting LOW.
  Walk it: 1→flip(H), 0→stay(H), 0→stay(H), 1→flip(L), 1→flip(H), 0→stay(H),
  0→stay(H), 1→flip(L). Draw those 8 slots.

**RZ:** signal goes to zero in the MIDDLE of every bit (3 levels: +, 0, −). Costly
bandwidth, obsolete — one sentence of theory is enough; drawing risk is low.

**Manchester (= RZ idea + NRZ-L):** **always a transition at the MIDDLE of the bit;
the direction of that mid-bit transition IS the bit.** (Book: low→high = 1... again,
follow the exam's legend if given.) Self-synchronizing, no DC, but bandwidth = 2× NRZ.

**Differential Manchester (= RZ idea + NRZ-I):** **always a mid-bit transition (for
sync); the bit is coded by presence/absence of a transition at the START of the slot:
transition at start = 0, no transition at start = 1.**
- Past paper Q13: 11000100, starting LOW. Walk each bit: ask "start-transition?"
  (yes if bit is 0), then ALWAYS flip mid-bit.

**The drawing discipline (same spirit as DSP's "mark n=0 with an arrow"):**
1. Draw 8 bit-slot boundaries FIRST, light vertical lines.
2. Write the bit above each slot.
3. Mark the given starting level (both past-paper questions said "low immediately
   before start" — that initial condition changes the entire waveform; ignore it and
   every slot is inverted = zero marks).
4. For the Manchester family, dot the mid-slot points before drawing.

**Bipolar AMI:** 0 = zero voltage; 1s alternate +V, −V, +V... (no DC by construction).
Pseudoternary = the same with roles swapped (0s alternate). Half a mark of theory risk;
know the rule, don't over-drill.

### 1.4 Summary table (condensed from book Table 4.1 — reproduce from memory once)

| Scheme | Bandwidth (avg) | Self-sync? | DC problem? |
|---|---|---|---|
| NRZ-L | N/2 | no (long 0s or 1s) | yes |
| NRZ-I | N/2 | no (long 0s only) | yes |
| Manchester / Diff. Manchester | N | **yes** | **no** |
| AMI | N/2 | no (long 0s) | no |
| 2B1Q | N/4 | no (long same double-bits) | — |
| MLT-3 | N/3 | no (long 0s) | — |

Lower-yield extras (skim once, skip if behind): 2B1Q (2 bits → one of 4 levels, used in
DSL), 8B6T, 4D-PAM5, MLT-3 (3-level transition rules, 100 Mbps Ethernet on copper).
Block coding 4B/5B (fixes NRZ-I's long-0s problem by substitution, +20% baud, doesn't
fix DC), 8B/10B. One recognition-level sentence each is enough.

### 1.5 Clock skew problems (past paper Q16 = book Example 4.3 with flipped roles!)

Book Example 4.3: *receiver* clock 0.1% faster, 1 Mbps → receiver sees
1,001,000 bps → **1000 extra bps**.
Past paper Q16: *sender* 0.2% faster at 1 Mbps → sender emits 0.2% more bits than the
receiver expects → 1,000,000 × 0.002 = **2000 extra bps**.
The math is literally `rate × skew%`. Don't overthink; do state the direction cleanly.

---

## PART 2 — PCM: the "quantization and encoding math" (§4.2.1) — YOUR flagged hot topic

Analog → digital data in 3 steps: **Sample → Quantize → Encode.** Every sub-question
the examiner can ask lives in one of these steps.

### 2.1 Sampling — Nyquist theorem (again, but the OTHER Nyquist statement)

```
fs ≥ 2 × f_max        (sampling rate ≥ twice the HIGHEST FREQUENCY — not the bandwidth!)
```

- Low-pass signal: bandwidth and f_max coincide → fs = 2×bandwidth works.
  Book Example 4.10: low-pass, B = 200 kHz → fs = **400,000 samples/s**.
- **Bandpass signal: CANNOT determine fs from bandwidth alone** — you don't know f_max.
  Book Example 4.11 makes exactly this point. This is a designed trap; the answer to
  "bandpass signal of bandwidth 200 kHz, min sampling rate?" is *"cannot be determined
  — f_max unknown."* Saying that IS the full-marks answer.
- Telephone voice: f_max assumed 4000 Hz → fs = **8000 samples/s** (Example 4.9 —
  memorize, it anchors the classic 64 kbps result below).
- Undersampling intuition (Examples 4.7/4.8): clock hand sampled below Nyquist appears
  to run backward = wagon-wheel effect in movies. You know this cold from DSP aliasing —
  same phenomenon, same math, different textbook.

### 2.2 Quantization — the mechanical recipe

Given amplitudes in [V_min, V_max] and L levels:

```
Δ = (V_max − V_min) / L                      zone height
normalized value  = actual amplitude / Δ
quantized value   = midpoint of the zone the sample falls in
normalized error  = quantized − normalized   (always in [−Δ/2, +Δ/2] → error ≤ Δ/2)
quantization code = 0 … L−1  (which zone, bottom to top)
encoded word      = that code in binary, using nb = log2(L) bits
```

### Worked skeleton (book Figure 4.26's setup): V ∈ [−20, +20], L = 8
Δ = 40/8 = **5 V**. Zones bottom→top: [−20,−15)=code 0, [−15,−10)=1, [−10,−5)=2,
[−5,0)=3, [0,5)=4, [5,10)=5, [10,15)=6, [15,20]=7. Midpoints: −17.5, −12.5, ... +17.5.
Normalized midpoints: −3.5, −2.5, −1.5, −0.5, +0.5, +1.5, +2.5, +3.5.

Sample amplitude +7.5 V → normalized 7.5/5 = 1.5 → zone [5,10) → quantized (normalized)
= +1.5 → error 0 → code **5** → encoded **101**.
Sample −6.1 V → normalized −1.22 → zone [−10,−5) → quantized −1.5 → error −0.28 →
code **2** → encoded **010**.

**Do 3–4 of these by hand until the pipeline (normalize → zone → midpoint → error →
code → binary) runs without looking.** This is THE thing you said you need to "apply."

### 2.3 The two formulas that ride on quantization

```
SNRdB = 6.02 × nb + 1.76  dB          (nb = bits per sample)
Bit rate = fs × nb  =  2 × f_max × nb
```

- Book Example 4.12: nb = 3 → SNRdB = 6.02·3 + 1.76 = **19.82 dB**.
- Book Example 4.13 (reverse!): need SNRdB > 40 → 6.02·nb + 1.76 = 40 → nb = 6.35 →
  **round UP → 7 bits** (telephone companies use 7–8). Rounding *down* fails the
  requirement — classic half-mark loss.
- Book Example 4.14 (the classic): human voice 0–4000 Hz, 8 bits/sample →
  fs = 8000, bit rate = 8000 × 8 = **64 kbps**. Memorize this number; it's the
  sanity-anchor for every PCM bit-rate problem.

### 2.4 PCM bandwidth (one step deeper, occasionally asked)

```
Bmin = nb × B_analog        (with NRZ/bipolar line coding, c = ½, r = 1)
```
Book Example 4.15: 4 kHz analog signal, 8 bits/sample → digital needs **32 kHz**.
"The price of digitization" — bandwidth inflates nb-fold.

### 2.5 Theory bites around PCM (one line each)

- Three sampling methods: ideal (theoretical), natural (switch), **flat-top/sample-and-
  hold (practical)**. Result of sampling is PAM — still analog values.
- More levels L → less quantization error → better SNR, more bits/sample, higher bit
  rate. It's a dial trading quality against bandwidth.
- **Nonuniform quantization / companding:** voice concentrates in low amplitudes →
  use smaller Δ there, bigger Δ at high amplitudes; compress at sender, expand at
  receiver. Reduces effective quantization noise for speech.
- Decoder: staircase reconstruction → **low-pass filter** (cutoff = original f_max)
  smooths it back to analog.
- **Delta Modulation (skim-level):** sends 1 bit per sample — "went up (1) or down (0)"
  vs a staircase approximation. Simpler than PCM; adaptive DM varies δ. If behind
  schedule, this paragraph is all you need.

### 2.6 Transmission modes (§4.3 — end of chapter, cheap definitional marks)

- **Parallel**: n bits per clock tick over n wires — fast, expensive, short distances.
- **Serial**: 1 bit per tick — three flavors:
  - *Asynchronous*: byte-at-a-time, start bit (0) + stop bits (1s), gaps allowed —
    timing per byte, not per stream.
  - *Synchronous*: unbroken bit stream, receiver recovers timing from the signal itself,
    byte boundaries reconstructed at the end.
  - *Isochronous*: guaranteed fixed rate for the whole stream (real-time A/V).

---

## Self-test (closed book, ~20 min)

1. Draw NRZ-I and Differential Manchester for **01101000**, previous level low.
   *(Check yourself: NRZ-I transitions on the three 1s only; DiffMan has a start-
   transition on every 0 — that's five of them — plus a mid-flip in all 8 slots.)*
2. Why can't a long run of 0s be tolerated by NRZ-I but a long run of 1s is fine?
   *(1s force transitions = clock info; 0s produce a flat line = receiver clock drifts.)*
3. Signal ∈ [−10, +10] V, L = 16: Δ? bits/sample? SNRdB? A sample at +3.2 V —
   normalized value, code, encoded word?
   *(Δ=1.25 V; nb=4; SNRdB=25.84 dB; normalized 2.56 → zone [2.5,3.75)... careful:
   codes 0–15 bottom-up put +3.2 V in code 10 → 1010; quantized midpoint 3.125 V.)*
4. Voice band 300–3400 Hz treated as f_max = 4 kHz, 8 bits/sample: fs? bit rate?
   min channel bandwidth with NRZ? *(8000 samples/s; 64 kbps; 32 kHz)*
5. Sender clock 0.05% fast, 2 Mbps — extra bps? *(2×10⁶ × 0.0005 = 1000 bps)*

All good → go do the past paper timed (Block D). Then sleep. The sleep is part of the
plan, not a reward for finishing it.
