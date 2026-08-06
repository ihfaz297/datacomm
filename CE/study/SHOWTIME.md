# SHOWTIME — CE midterm, everything from tonight in one pass

Read top to bottom once. Every line is either a real "wait, why" from this session or
a mark sitting in plain sight. **10 minutes only? Read the bold lines.**

---

## 1. The five formulas that carry the paper

```
dB = 10 log10(P2/P1)                     add across stages; ratio back: 10^(dB/10)
Nyquist:  BitRate = 2 × B × log2(L)      noiseless channel
Shannon:  C = B × log2(1 + SNR)          noisy channel — SNR is the RATIO, not dB!
Latency = propagation + transmission (+ queuing + processing)
BDP: bits in flight = bandwidth × delay;  full-duplex burst = 2 × bandwidth × delay
```

**Anchors: −3 dB ⇔ half power. +3 dB ⇔ double. ±10 dB ⇔ ×10 or ÷10.** Any dB answer
that violates these is wrong before you finish writing it.

**SNRdB = 10·log₁₀(SNR) ⇔ SNR = 10^(SNRdB/10).** Convert BEFORE Shannon. High-SNR
shortcut for checking: C ≈ B × SNRdB/3.

## 2. The two-step dance (past paper Q11 = book Example 3.41 verbatim)

**Shannon first → ceiling. Pick a rate below it. Nyquist second → levels needed.**
B = 1 MHz, SNR = 63: C = 10⁶·log₂64 = 6 Mbps → choose 4 Mbps → 4M = 2·10⁶·log₂L →
L = 4. Magic sentence: *"Shannon gives the upper limit; Nyquist tells us how many
signal levels we need."* Exam SNRs make 1+SNR a power of 2 (7, 15, 31, 63, 127...) —
if yours doesn't, re-read the question.

## 3. The TWO Nyquists are one Nyquist

**Channel capacity 2·B·log₂L and sampling theorem fs = 2·f_max are the same equation:**
n_b = log₂L bridges them (8 levels ⇔ 3 bits). PCM asks what the encoder *produces*
(2·f_max·n_b); capacity asks what the wire *carries* (2·B·log₂L). Producer vs pipe.

**Routing rule: "sample/quantize/voice/digitize" → PCM formula. "channel/levels/SNR/
noiseless" → Nyquist; SNR present → Shannon first.**

## 4. Sampling traps

- **fs ≥ 2 × HIGHEST FREQUENCY — not 2 × bandwidth.** They coincide only for
  low-pass (band touches 0).
- **Bandpass + only bandwidth given → "CANNOT be determined, f_max unknown."**
  Refusing to compute IS the full-marks answer (book Example 4.11). Low-pass B given
  → fs = 2B instantly. Two shapes, two reflexes.
- **Sampling output = PAM: discrete in TIME, still ANALOG in amplitude.** Digital only
  after quantization. Each PCM box kills one continuity: sample→time, quantize→
  amplitude, encode→bits.
- Undersampling = clock hand seeming to run backward = wagon wheels in movies = the
  aliasing you already know from DSP.

## 5. Quantization — the pipeline + tonight's comedy award

```
Δ = (Vmax − Vmin)/L → normalize (amp/Δ) → zone → midpoint → error (≤ Δ/2) →
code (0..L−1 bottom-up) → binary word (nb = log2 L bits)
```

- **The range (Vmax, Vmin) is a DESIGN choice printed in the question — NEVER the
  max/min of the sample data.** (19.7 is near the ceiling, it is not the ceiling.)
- Figure axis in "D" units: D = Δ. 4D = 4Δ = 20 V when Δ = 5.
- **SNRdB = 6.02·n_b + 1.76.** Reversed ("need SNRdB > 40") → solve n_b = 6.35 →
  **round UP** → 7 bits.
- **Voice anchor: 4 kHz → fs = 8000 → × 8 bits = 64 kbps.** Sanity-checks every PCM
  answer. PCM bandwidth price: B_min = n_b × B_analog (4 kHz voice → 32 kHz).
- Symmetric range sanity check: ±V with L=8 → codes 0–3 negative, 4–7 positive. A
  negative sample landing in code 5 = your zone walk slipped.

## 6. Line coding — what it IS, in one line

**The agreed convention for what a bit physically looks like on the wire — Morse code
for bits.** Not an enhancement; without it there's no transmission at all. The whole
chapter = which conventions keep the receiver's clock synced (transitions), avoid DC
(zero average), and spend least bandwidth.

Why-list (past paper asked it as "write points only"): **baseline wandering, DC
components, self-synchronization, built-in error detection, noise immunity,
complexity.**

## 7. Decode taxonomy — where the eyes go (the whole skill in one table)

| Scheme | Look at | Rule |
|---|---|---|
| NRZ-L | inside slot | level = bit (per legend) |
| AMI | inside slot | pulse = 1 (alternating ±), zero = 0 |
| NRZ-I | **boundaries** | transition = **1** (Invert-on-1) |
| Diff. Manchester | **boundaries** (X out mids first!) | transition = **0** (the contrarian) |
| Manchester | **mid-slot** | direction: low→high = 1, high→low = 0 |

**NRZ-I and DiffMan are polarity-opposite twins. Apply the wrong one → perfect
bit-flip of the right answer.**

## 8. Frame discipline — tonight's 10001000 incident

**Before decoding ANYTHING: establish where slot 1 starts.** The sliver of level at
the y-axis is the pre-signal, slot 1 begins AT the axis — the first dashed line is
slot 1's END, not its start. Checks: (1) count exactly 8 complete slots for 8 bits;
(2) diff Manchester: every slot owns exactly one mid-flip — an orphaned transition
outside all slots = your grid is shifted. **X the mids, circle the boundaries,
same = 1, changed = 0.**

## 9. Why differential encoding exists

**"Did it change?" survives accidents that "what level is it?" doesn't:** flip the
wires (polarity inversion) and NRZ-L reads everything inverted, NRZ-I/DiffMan read
perfectly — transitions survive inversion. Plus comparing adjacent levels beats
measuring against a drifting threshold (baseline wandering). One-liner: *"the bit is
coded as presence/absence of a transition, so the scheme is immune to polarity
inversion and less sensitive to baseline drift."*

## 10. Baud vs bit rate — vehicles vs passengers

**S = c × N × (1/r), c = ½ average; B_min ≈ S. Bandwidth follows BAUD, not bits.**
Same 1 Mbps: NRZ (r=1) → 500 kbaud/kHz; Manchester (r=½) → 1 Mbaud/MHz (double!);
2B1Q (r=2) → 250 kbaud/kHz. Table 4.1's bandwidth column is just this formula pre-run.
(Book Example 4.4 has a typo — says 10 Mbps, computes 1 Mbps. Trust the method.)

Clock skew: **extra bps = rate × skew fraction.** 1 Mbps, 0.2% fast sender → 2000
extra bps. Direction just changes who has surplus.

## 11. Manchester family summary

**Manchester = RZ's mid-bit idea + NRZ-L. Differential Manchester = RZ + NRZ-I.
Both: self-sync (guaranteed mid transition), zero DC, cost = DOUBLE the bandwidth of
NRZ.** AMI: 3 levels, 1s alternate polarity → no DC, same bandwidth as NRZ, but long
0s still break sync (scrambling fixes it — recognition level).

## 12. OSI rapid-fire (the .5-mark farm)

- Best path/routing → **Network**. Lost PDU recovery → **Transport**. Flow control
  (overwhelmed receiver) → **Transport**. Encryption → **Presentation**. Chunking →
  **Transport**; order guaranteed by **sequence numbers**.
- Framing/MAC/hop-to-hop → Data link. Bits on wire → Physical. Dialog/checkpoints →
  Session. Compression/translation → Presentation. Process-to-process → Transport
  (ports); host-to-host → Network.
- **Addressing + widths (write them in Q15-style answers): port 16 bit, IP 32 bit,
  MAC 48 bit.** Names at Application, NOTHING at Physical (bits can't be addressed).
- PDU ladder: **message → segment/user datagram → datagram → frame → bits.**
- Mapping: App+Pres+Session → Application; Data link+Physical → Network Access.
  Why merged: session features live in transport protocols; apps build their own
  presentation. **ISO is the organization, OSI is the model.** Why OSI lost (any 2):
  TCP/IP entrenched; session/presentation never fully defined; no performance win.
- Device layer counts: **host 5, router 3 (1 network + n data-link + n physical for
  n links), switch 2.** Router with 3 links: 1/3/3.
- **Switch needs no address to forward** — frames are addressed to Host 3, never to
  the switch; it reads the destination field like a mail sorter reads envelopes.
  Routers DO have per-link addresses (off-network frames are sent TO the router).

## 13. Ch1 one-glancers

- 5 components: **message, sender, receiver, medium, protocol.** Effectiveness: 
  **delivery, accuracy, timeliness, jitter** (jitter = *variation* in delay).
- Criteria: **performance (throughput & delay — they conflict), reliability, security.**
- **Mesh links = n(n−1)/2, ports = n−1.** n=6 → 15 links, 5 ports. Same formula for
  "n LANs fully interconnected by WANs." Star = n links, ring = n, bus = 1 backbone
  + n drops.
- Failures: hub dies → star dead; one station dies → simple ring dead; backbone cut →
  bus fully dead (reflections both ways); mesh shrugs.
- Simplex (keyboard) / half-duplex (walkie-talkie) / full-duplex (phone).
- **Circuit-switched: reserves a path, efficient only at full capacity, no storing.
  Packet-switched: store-and-forward, shares on demand, cost = queuing delay.**
  Local phone call = circuit-switched, point-to-point.
- internet (lowercase) = any connected networks; Internet (capital) = the big one.
- Unicode 2³² symbols; 16-bit pixels → 65,536 colors.

## 14. Ch3 leftovers that cost half-marks

- Sine wave = **A, f, φ** — s(t) = A·sin(2πft + φ). T = 1/f. Phase recipe:
  fraction-of-cycle × 360° (1/6 cycle late → 60°).
- **λ = propagation speed / f.** Bit length = speed × bit duration.
- Impairments by mechanism: **attenuation** (energy loss → dB), **distortion**
  (components arrive at different phases → shape changes), **noise** (thermal /
  induced / crosstalk / impulse). "Shape changed, power fine" → distortion.
- **Periodic → discrete spike spectrum; nonperiodic → continuous curve.** "Draw the
  bandwidth" = spikes + labeled span-arrow (B = f_high − f_low).
- Transmission vs propagation: short message + fat pipe → propagation dominates;
  big file + thin pipe → transmission dominates. SAY which dominates.
- Throughput = actual (≤ bandwidth = potential). Baseband needs low-pass channel;
  broadband/modulation uses bandpass.

## 15. Exam-room protocol

- **Formula → substitution → answer with units.** The marks live in the middle step.
- Diagram answers: label axes, mark slot boundaries BEFORE drawing, arrow the
  bandwidth span, state the starting level.
- "Explain why X" → one mechanism sentence beats a paragraph. All the one-liners
  above are pre-built for this.
- 20 marks, 60 minutes → **3 min/mark. A stuck 1.5-marker gets 5 minutes MAX, then
  skip and return.**

## If you only remember ten things

1. −3 dB = half power; dB adds across stages.
2. Shannon = ceiling, then Nyquist = levels. SNR in Shannon is the ratio, never dB.
3. fs = 2·f_max, NOT 2×bandwidth — bandpass with no f_max = "cannot be determined."
4. Quantizer range comes from the QUESTION, never from the sample data.
5. SNRdB = 6.02n_b + 1.76; round n_b UP. Voice = 64 kbps, always.
6. NRZ-I: transition = 1. DiffMan: transition = 0, X out the mid-flips first.
7. Frame first: slot 1 starts at the axis; count 8 slots; orphan transition = shifted grid.
8. Bandwidth follows baud (S = c·N/r), so Manchester costs double, 2B1Q costs half.
9. Port 16 / IP 32 / MAC 48; message→segment→datagram→frame→bits.
10. Whatever breaks, write the formula and substitute anyway — the method is most
    of the mark.

You walked into DSP "fucked" and walked out with a folder. Same folder energy today.
Go get it. Again.
