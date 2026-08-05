# CE Midterm — Battle Plan (9 hours, exam ~12PM)

**Book confirmed: Forouzan, Data Communications and Networking, 5e** (the PDF in `CE/`).
Chapter numbers match yours exactly:
- Ch1 Introduction, Ch2 Network Models (OSI is §2.3 — you're done here)
- Ch3 Introduction to Physical Layer = "Data and Signals" (the math chapter)
- Ch4 Digital Transmission = line coding + PCM (the "quantization and encoding" chapter)

## The single most important discovery tonight

`CE/Copy of SolnCSE630 SUST_TT1.pdf` (a past paper, different supervisor, but same
textbook/course) is **not just similar to the book — some questions are the book's own
worked Examples, transcribed almost verbatim.** Confirmed match:

> Past paper Q11: *"We have a channel with a 1-MHz bandwidth. The SNR for this channel
> is 63. What are the appropriate bit rate and signal level?"*
> Textbook **Example 3.41**: identical numbers, identical question.

This means: **working every numbered Example in Ch3 §3.4–3.6 and Ch4 §4.1–4.2 is not
optional extra practice — it is the highest-density thing you can do with your hours.**
A different supervisor may not reuse this exact paper, but they are drawing from the
same textbook's example pool, so the *types* and *typical numbers* transfer even if the
exact question doesn't.

## What the past paper actually tested (use this as your weighting)

| # | Topic | Chapter | Book anchor |
|---|---|---|---|
| 1–6 | OSI layer responsibilities (routing, recovery, flow control, encryption), OSI↔TCP/IP correspondence, PDU segmentation + sequence numbers | Ch2 | §2.2–2.3 |
| 7, 12 | Composite signal → draw in frequency domain / bandwidth | Ch3 | §3.2.5–3.2.6 |
| 8a | Bandwidth-delay product (max bits filling a link, full-duplex burst size) | Ch3 | §3.6.4 |
| 8b | Why digital data still needs line coding (list reasons) | Ch4 | §4.1.1 |
| 9, 10 | Attenuation in dB, cascaded amplifier dB | Ch3 | §3.4.1 |
| 11 | Shannon capacity + Nyquist signal levels together | Ch3 | §3.5.3 (= Example 3.41, verbatim) |
| 13, 14 | Decode a line-coding graph: Differential Manchester, NRZ-I | Ch4 | §4.1.2 |
| 15 | All 7 OSI layers, their task, addressing | Ch2 (classic 7-layer, book only briefly covers OSI — see cue sheet) |
| 16 | Clock skew → extra bits/sec at a given data rate | Ch4 | §4.1.1 Self-sync (= Example 4.3 pattern) |

**Notably absent from this past paper but you flagged it as "hot": PCM quantization +
encoding math (§4.2.1).** Different supervisor, different year — cover it anyway,
it's cheap and mechanical once you've seen it once (see `03-ch4-digital-transmission.md`).

## Schedule (~9 hours total, budget for sleep)

| Block | Hrs | What |
|---|---|---|
| A | 1.0 | `01-ch1-2-cuesheet.md` — full Ch1 (topologies + mesh math, switching, criteria, standards) + Ch2 (layering, OSI drills, encapsulation, addressing). Now real coverage, not a skim. |
| B | 2.25 | `02-ch3-data-signals.md` — dB/attenuation, Nyquist, Shannon, bandwidth-delay product, composite signal bandwidth. Work every example by hand, don't just read. |
| C | 2.25 | `03-ch4-digital-transmission.md` — line coding schemes (esp. NRZ-I, Manchester, Diff. Manchester — draw them by hand), then PCM sampling/quantization/encoding math. |
| C½ | 0.5 | `04-diagram-drills.md` — **~40% of the past paper was diagram questions.** Waveform DECODE (Q13/Q14 direction!), frequency-domain spikes + bandwidth spans, OSI table with bit-widths. Rendered originals in `study/figs/`. |
| D | 1.0 | Redo the past paper (`figs/pastpaper_p*.png` — use the images, not the text extraction, so you get the actual waveform questions) closed-book, timed. Fix only what breaks. |
| — | ~2.0 | **Sleep.** You said it yourself — DSP taught you this works. Don't skip it. |

Within Block A, if you're running past the hour: Ch1's §1.7 (history + standards) is
the lowest-yield section — drop to skim-only there first, never from the topology or
switching sections.

## If you get down to 3 hours

Priority order (highest mark-per-minute first, based on the past paper's actual mark
distribution): **dB/attenuation → Nyquist+Shannon → OSI layer functions/TCP-IP mapping →
line coding (NRZ-I, Manchester family) → PCM quantization formula.** Skip DM (delta
modulation) and the multilevel schemes (2B1Q/8B6T/MLT-3) guilt-free if time runs out —
they're real but lower-yield than the above.

## Exam-room rules
- **Show the formula, then substitute, then answer** — partial credit lives in the
  substitution step, same as your DSP TT1.
- For dB problems: attenuation is **negative**, gain is **positive**. Cascaded dB
  values **add**, they don't multiply.
- For any line-coding graph question: **mark the bit boundaries and the mid-bit point**
  explicitly before drawing transitions. This is exactly the "mark n=0 with an arrow"
  discipline from DSP — same idea, different notation.
- State units on every final numeric answer (bps vs kbps vs Mbps trips people up under
  time pressure more than the math does).
