# CE Mid-term 2 — Battle Plan (12 hours, Ch 5, 6, 7, 8, 10, 11)

Book: Forouzan, *Data Communications and Networking*, **5e** (`CE/Data-Communications-and-Network by BEHROUZ A. FOROUZAN-5e.pdf`).

Your study files (written in parallel, read them in this order):

| File | Covers |
|---|---|
| [11-ch5-6-analog-and-multiplexing.md](11-ch5-6-analog-and-multiplexing.md) | Ch5 ASK/FSK/PSK/QAM, constellation, bit rate vs baud rate, AM/FM/PM. Ch6 FDM, TDM, WDM, FHSS/DSSS |
| [12-ch7-8-media-and-switching.md](12-ch7-8-media-and-switching.md) | Ch7 cables, fiber, wireless. Ch8 circuit / datagram / virtual-circuit switching, crossbar and 3-stage switch |
| [13-ch10-11-errors-and-dlc.md](13-ch10-11-errors-and-dlc.md) | Ch10 Hamming distance, parity, CRC, checksum, FEC. Ch11 framing, stuffing, Stop-and-Wait, HDLC, PPP |
| [14-mid2-mock-paper.md](14-mid2-mock-paper.md) | A timed mock paper built only from real past questions |
| [../Questions/official-solutions/](../Questions/official-solutions/) | The publisher's own solutions to the **odd-numbered** end-of-chapter Questions and Problems, one PDF per chapter. Use it to check answers to past-paper questions copied from odd problems, such as P5-5, P6-1, P6-9 and P11-7. One known typo: its P6-9 frame duration says 5.3 ms, but the right answer is 5.26 µs |
| [15-mid2-official-quizzes.md](15-mid2-official-quizzes.md) | The publisher's own 109 multiple-choice questions for these chapters, with a corrected answer key. Do one chapter's set (10 to 15 min) right after each study block. Best practice for the quiz part |

---

## 1. The key finding (read this first)

**The teachers copy questions straight from the textbook's end-of-chapter exercises and worked Examples. Then they reuse them across years.** I checked every past question against the 5e PDF:

| Past question | Textbook source | Seen in |
|---|---|---|
| "8000 bps and a baud rate of 1000 baud…" | **Example 5.2**, word for word | 2014-15, 2019-20, **TT2 2025** |
| "Draw the constellation… (2,0) and (3,0)…" (4 parts) | **P5-5**, word for word | **TT2 2025** |
| "BPSK peak 2 / 8-QAM amplitudes 1 and 3, four phases" | **P5-4** | 2015-16, 2016-17, 2019-20 |
| "Bits per baud: ASK 4 amplitudes, FSK 8 freqs…" | **P5-3** | 2015-16, 2016-17 |
| "100 kHz from 200 to 300 kHz… ASK with d=1" | **Example 5.3** | 2019-20 |
| "12 Mbps for QPSK, d=0" | **Example 5.7** | 2018-19 |
| "Corporation, 1-MHz, 10 channels, QAM" / "Cable TV 6 MHz 64-QAM" | **P5-9 / P5-10** | 2016-17 |
| "Voice channel 4 kHz… guard bands of 500 Hz… FDM" | **P6-1** (10 channels → 3 channels) | **TT2 2025** |
| "Five channels 100 kHz, guard band 10 kHz" | **Example 6.2** | 2018-19 |
| "Four 1-Mbps lines… synchronous TDM… bit duration…" | **Example 6.6** | 2019-20, TT1 (as 10 Mbps) |
| "190 kbps and 180 kbps… pulse-stuffing TDM" | **P6-9** | 2015-16 |
| "Output stream, 10-bit slot, 3 bits + 1 framing bit" | **P6-12** | 2016-17 |
| "Three-stage switch N=100, 10 crossbars, 4 middle" | **P8-12** | 2016-17, 2019-20 (2015-16 is the Example 8.3 pattern) |
| "Min Hamming distance / detect two-bit errors" | **Q10-5, Q10-6** | 2016-17, 2019-20 |
| "CRC dataword …, divisor 10111" | **P10-12** pattern | 2015-16, 2016-17 |
| "Polynomial of …, shift … four bits to the right" | **P10-14** | 2016-17, 2019-20 |
| "Stop-and-Wait: Frame 0 sent but lost…" | **P11-8** (+ P11-7) | 2016-17, 2019-20 |
| "Why flags for variable-size frames" / "byte vs bit-oriented" | **Q11-2, Q11-4** | TT2 (old) |
| "Guided vs unguided", "cladding", "fiber advantages", "refraction/reflection" | **Q7-3, Q7-7, Q7-8, Q7-6** | 2016-17, TT1 |
| "Most susceptible to noise (ASK/FSK/PSK/QAM)" | **Q5-5** | 2019-20 |
| "Statistical vs synchronous TDM", "multilevel / multiple-slot" | **Q6-9, Q6-8** | 2015-16, 2016-17, 2018-19 |
| "Define FHSS and explain how it achieves bandwidth spreading" | **Q6-11** | 2015-16 |

So: **the end-of-chapter Questions/Problems lists for Ch5, 6, 7, 8, 10, 11 are the real question bank.** If you have spare time, work those, not random internet questions.

---

## 2. What the exam probably looks like

You have two 2nd-term-test papers. They look different, so expect something between them.

| | **TT2 2025** (`Questions/tt2/*.jpeg`, CSE365, 28 Aug 2025) | **TT2 older** (`Term Test/DataCom_TT2.pdf`) |
|---|---|---|
| Time | 1 hour | 30 min |
| Marks | 20 | 20 |
| Questions | 8 (with sub-parts a–d), marks per question not printed | 4 × 5 marks |
| Answer where | **Directly on the question paper** (blank boxes to draw in) | Script |
| Style | Almost all **draw** or **calculate**: AM/FM sketch, PCM, constellations, FDM bandwidth drawing, bit/baud | All **explain/compare** + one table (parity code) |
| Chapters | Ch4 PCM (2 of 8 Qs), Ch5 (5 Qs), Ch6 FDM (1 Q) | Ch2 (1 Q), Ch10 (1 Q), Ch9/11 data-link (2 Qs) |

**My best guess for tomorrow** (newest paper = strongest signal):

- **20 marks, about 1 hour, no choice** ("answer all"). Roughly 3 minutes per mark. Maybe a short quiz on top (1-mark definitions, like the finals' "answer any five" blocks).
- **6–8 questions, each 2–5 marks.** Most will be numericals or drawings with textbook numbers.
- Your syllabus is wider than TT2 2025's (it ran Ch4–6 only). So expect **about one question per chapter**: Ch5 (2 Qs, it's the biggest), Ch6 (1–2), Ch7 (1 short), Ch8 (1), Ch10 (1–2), Ch11 (1).
- **Small risk:** TT2 2025 asked PCM (Ch4) twice. You already know Ch4, so just glance at `03-ch4-digital-transmission.md` PCM section in the morning.

How much of each old paper was Ch1–4 (the part you already know):

| Paper | Ch1–4 share (approx.) | Ch5–11 share |
|---|---|---|
| TT1 (`TT-01.pdf`) | 50% (attenuation, NRZ-L, protocols) | 50% (sync TDM, media) |
| TT2 older | 25% (four levels of addressing) | 75% |
| TT2 2025 | 25% (two PCM questions) | 75% |
| Final 2014-15 (100 marks) | ~55% | ~35% (+ ~10% Ch12: CDMA, CSMA/CD) |
| Final 2015-16 (100 marks) | ~45% | ~50% (+ ARP, router) |
| Final 2016-17 (100 marks) | ~50% | ~45% (+ CDMA, CSMA) |
| Final 2018-19 (50 marks) | ~55% | ~45% |
| Final 2019-20 (50 marks) | ~45% | ~50% |

---

## 3. Frequency table and the ranking (the plan is built on this)

"Count" = how many separate questions/sub-questions hit the topic across all 9 papers.
"Yield" = expected marks per hour of study. Cheap formulas that keep showing up win.

| Rank | Topic | Count | Typical marks | Study time | Yield | File |
|---|---|---|---|---|---|---|
| **1** | **Bits per baud, bit rate vs baud rate** (`r = log2 L`, `S = N / r`) | **8** (8000/1000 question alone x3) | 1–5 | 20 min | Very high | 11 |
| **2** | **Constellation diagrams** (BPSK, QPSK, 8-PSK, 8-QAM, 16-QAM; read I/Q points, peak amplitude) | **8** | 2–6 | 45 min | Very high | 11 |
| **3** | **Hamming distance, min Hamming distance, detect/correct rules** | **6** | 1–4 | 20 min | Very high | 13 |
| **4** | **Modulation bandwidth formulas** (`B = (1+d)S`, carrier freq, BFSK/MFSK, QAM data rate) | **7** | 1–5 | 30 min | High | 11 |
| **5** | **FDM bandwidth with guard bands + synchronous TDM numericals** (bit duration, frame rate, output stream) | **6** (FDM 3, sync TDM 3) | 2.5–5 | 45 min | High | 11 |
| **6** | **CRC generation/check + polynomial representation/shift** | **8** (CRC 4, polynomial 4) | 1–10 | 60 min | High | 13 |
| **7** | **AM / FM drawing** (and read carrier/modulating signal off an AM picture) | 3 (all in TT2 2025) | ~2–3 each | 30 min | High (this teacher's style) | 11 |
| **8** | **Stop-and-Wait flow diagram** (frame lost / ACK lost scenario) | 2 (+2 short ACK/NAK Qs) | 5–10 | 30 min | High | 13 |
| 9 | Simple parity + checksum (table C(4,3), even parity bit, wrapped sum) | 5 | 1–6 | 30 min | Medium-high | 13 |
| 10 | Three-stage space-division switch (crosspoints, blocking) | 3 (x3 repeat, same numbers) | 2.5–10 | 30 min | Medium-high | 12 |
| 11 | Multiplexing/TDM definitions (why multiplex, statistical vs sync, multilevel / multiple-slot / pulse stuffing) | 9 | 1–4 | 30 min | Medium | 11 |
| 12 | Framing: flags, byte- vs bit-oriented, byte/bit stuffing, DLL duties | 4 (TT2 older was half this) | 5 | 30 min | Medium | 13 |
| 13 | ASK/FSK/PSK/QAM concept questions (process, differences, noise) | 6 | 1–5 | 20 min | Medium | 11 |
| 14 | Spread spectrum FHSS / DSSS | 4 | 1–7.5 | 20 min | Medium | 11 |
| 15 | Transmission media short answers (guided vs unguided, fiber pros/cons, cladding, STP/UTP, VHF, propagation) | 11 (mostly 1–2 marks) | 1–5 | 40 min | Medium | 12 |
| 16 | Virtual-circuit network phases, VCI, datagram delay, Banyan | 4 | 1–6 | 20 min | Medium-low | 12 |
| 17 | Error types, burst error, FEC, chunk interleaving | 6 | 1–3 | 15 min | Medium-low | 13 |

Out of your syllabus (skip): CDMA / Walsh chips, CSMA/CD, CSMA/CA (Ch12), ARP and router interfaces (Ch9). Hamming *code* construction (2014-15 Q5b) is a 4e topic; 5e only mentions it in Q10-7.

---

## 4. Every Ch5–11 question, verbatim, grouped by chapter

Source tags:
- **TT2-25** = `Questions/tt2/` photos (CSE365 TT2, SUST, 28 Aug 2025, 1 h, 20 marks). No per-question marks printed.
- **TT2-old** = `Term Test/DataCom_TT2.pdf` (30 min, 20 marks).
- **TT1** = `Term Test/TT-01.pdf` (30 min, 20 marks).
- **F15** = Final, session 2014-15 (held May 2017, 100 marks, 3 h). Right edge of photo cuts some mark labels.
- **F16** = Final, session 2015-16 (held 2018, 100 marks, 3 h).
- **F17** = Final, session 2016-17 (held June 2019, 100 marks, 3 h).
- **F19** = Final, session 2018-19 (held June 2021, 50 marks, 2 h).
- **F20** = Final, session 2019-20 (held June 2022, 50 marks, 2 h).

`(REPEAT xN)` = the same question (same numbers or near-identical wording) appears N times.

### Chapter 5 — Analog transmission

**Bit rate / baud rate / bits per baud**
- **(REPEAT x3)** "An analog signal has a bit rate of 8000 bps and a baud rate of 1000 baud. How many data elements are carried by each signal element? How many signal elements do we need?" — **TT2-25 Q8**; **F20 Q5c** [2.5]; **F15 Q5c** (second half) [part of 10]. = Example 5.2.
- F15 Q5c (first half): "Name three mechanism for modulating digital data into an analog signal." [part of 10]
- **(REPEAT x2)** F16 Q1(l): "What is the number of bits per baud for the FSK with eight different frequencies?" [1]
- F17 Q5(f): "What is the number of bits per baud for the following techniques? i) ASK with four different amplitudes ii) FSK with 8 different frequencies iii) PSK with four different phases iv) QAM with a constellation of 128 points." [1+1+1+2]
- F19 Q1(h): "An analog signal carries 4 bits per signal element. What is the bit rate, if 1000 signal elements are sent per second?" [1]
- **(REPEAT x2)** F15 Q4(d): "Define: Bit rate, Baud rate." [~2]; F19 Q1(b): "Distinguish between data rate and signal rate." [1]

**Bandwidth / carrier frequency numericals**
- F16 Q2(e): "If you want to send a data of 2 bits at a time with a bit rate of 4 Mbps and the carrier frequency of 10 MHz; calculate the number of levels (different frequencies), the baud rate, and the bandwidth." [1+1+2] (= Example 5.6 with 2 bits instead of 3)
- **(REPEAT x2)** F16 Q4(c): "What is the bandwidth equation for Amplitude Shift Keying (ASK)?" [1]; F19 Q1(e): "Write down the equation of bandwidth requirement for BFSK." [1]
- F20 Q5(d): "We have an available bandwidth of 100 kHz which spans from 200 to 300 kHz. What are the carrier frequency and the bit rate if we modulated our data by using ASK with d = 1?" [2.5] (= Example 5.3)
- F19 Q5(d): "Find the bandwidth for a signal transmitting at 12 Mbps for QPSK, where the value of d = 0." [2.5] (= Example 5.7)
- F17 Q1(a): "A cable company uses one of the cable TV channels (with a bandwidth of 6 MHz) to provide digital communication for each resident. What is the available data rate for each resident if the company uses a 64-QAM technique?" [2] (= P5-10)
- F17 Q6(c)(i): "A corporation has a medium with a 1-MHz bandwidth (lowpass). The corporation needs to create 10 separate independent channels each capable of sending at least 10 Mbps. The company has decided to use QAM technology. What is the minimum number of bits per baud for each channel? What is the number of points in the constellation diagram for each channel? Let d = 0." [5] (= P5-9)

**Constellation diagrams**
- **TT2-25 Q5**: "Draw the constellation diagram for the following cases. Find the peak amplitude value for each case and define the type of modulation (ASK, FSK, PSK, or QPSK). The numbers in parentheses define the values of I and Q respectively. a. Two points at (2, 0) and (3, 0) b. Two points at (3, 0) and (−3, 0) c. Four points at (2, 2), (−2, 2), (−2, −2), and (2, −2) d. Two points at (0, 2) and (0, −2)" (= P5-5)
- **(REPEAT x3 for 8-QAM)** F16 Q3(f): "Draw the constellation diagram for the following: i) BPSK, with a peak amplitude value of 2 [2] ii) 8-QAM with two different peak amplitude values, 1 and 3, and four different phases [2] iii) 16-QAM with two different peak amplitude values, 2 and 5, and four different phases [2]" (as printed; two amplitudes × four phases gives only 8 points, so for 16 points you'd need 8 phases — see F20 below)
- F17 Q2(c): "Draw the constellation diagram for the following: i) BPSK, with a peak amplitude value of 3 ii) 8-QAM with two different peak amplitude values, 1 and 3, and four different phases" [5]
- F20 Q2(a): "Draw the constellation diagram for the following: i) 8-QAM with two different amplitudes and four different phases. ii) 16-QAM with two different amplitudes and eight different phases." [2.5]
- **(REPEAT x2)** F15 Q6(f) and F16 Q5(f): "Draw and explain constellation diagram for 8-PSK with appropriate data bits and phases." [F16: 2+2; F15: ~5]
- F16 Q4(e): "In QPSK how many possible phases can be found in a sine wave? Write down the phase angles." [1]
- F15 Q6(b): "List some of the advantages of QAM over ASK? Explain QPSK with appropriate figures." [~5]

**Concept questions (ASK/FSK/PSK)**
- F19 Q3(b): "Discuss the process of ASK, FSK, PSK with an example." [5]
- F17 Q4(a): "What are the differences between ASK and FSK?" [2]
- F16 Q2(g): "What is a carrier frequency? Explain PSK with an appropriate figure." [1+3]
- F20 Q4(d): "Which of the four digital-to-analog conversion techniques (ASK, FSK, PSK, or QAM) is the most susceptible to noise? Defend your answer." [1] (= Q5-5)

**Analog-to-analog (AM / FM) — only in TT2-25, but this is the newest paper**
- **TT2-25 Q1**: "Choose carrier frequency and draw corresponding AM modulated signal in above figure (Figure 1)." (Figure 1 modulating signal: about 1.5 cycles of a sine whose swing gets smaller to the right — starts mid-high, deep trough, then a smaller hump and smaller dip.)
- **TT2-25 Q2**: "Choose carrier frequency and draw FM modulated signal in the above figure (Figure 2)." (Figure 2 modulating signal: one slow wave — rises to a broad peak, then falls to a trough at the right end.)
- **TT2-25 Q3**: "Determine the carrier frequency and modulating signal from the AM modulated signal in the above figure (Figure 3)." (Figure 3: a fast carrier, about 20–25 cycles, whose envelope is small at both ends and largest in the middle — so the modulating signal is one smooth hump.)

### Chapter 6 — Bandwidth utilization (multiplexing, spread spectrum)

**FDM numericals**
- **TT2-25 Q6**: "a. Assume that a voice channel occupies a bandwidth of 4 kHz. We need to multiplex 3 voice channels with guard bands of 500 Hz using FDM. Calculate the required bandwidth. b. Draw the bandwidth for 6.a if the staring frequency of the medium is 1 kHz. c. Assume that a voice channel occupies a bandwidth of 4 kHz. We need to multiplex 3 voice channels with no guard bands using FDM. Calculate the required bandwidth. d. Draw the bandwidth for 6.b if the staring frequency of the medium is 1 kHz." (6.d says "6.b" but almost certainly means 6.c.) (= P6-1 / Example 6.1)
- F19 Q2(f): "Five channels, each with a 100 kHz bandwidth, are to be multiplexed together. What is the minimum bandwidth of the link if there is a need for a guard band of 10 kHz between the channels to prevent interference?" [2.5] (= Example 6.2)
- F16 Q4(b): "Write down one application of WDM." [1]

**Synchronous TDM numericals**
- **(REPEAT x2)** TT1 Q3: "Four 10Mbps input lines are multiplexed in a synchronous TDM. The unit of data is 1 bit. Find - i) The output bit duration ii) The output bit rate iii) The output frame rate" [5]; F20 Q3(a): "Four 1Mbps input lines are multiplexed in a synchronous TDM. The unit of data is 1bit. Find i) The input bit duration ii) The output bit duration iii) The output bit rate iv) The output frame rate" [5] (= Example 6.6)
- F17 Q6(c)(ii): "Figure below shows a multiplexer in a synchronous TDM system. Each output slot is only 10 bits long (3 bits taken from each input plus 1 framing bit). What is the output stream? The bits arrive at the multiplexer as shown by the arrows." Inputs: `101110111101`, `11111110000`, `1010000001111`. [5] (= P6-12; digits read from photo, double-check the 2nd line has 11 digits as printed)
- F16 Q6(b): "What is pulse-stuffed TDM? Two channels, one with a bit rate of 190 kbps and another with a bit rate of 180 kbps, are to be multiplexed using pulse-stuffing TDM with no synchronization bits. Answer the following questions: i) What is the size of a frame in bits? ii) What is the frame rate? iii) What is the duration of a frame? iv) What is the data rate?" [2+4] (= P6-9)

**Multiplexing definitions**
- **(REPEAT x3)** F15 Q4(f) and F16 Q4(i): "What is multiplexing and why is it necessary?" [1–2]; F19 Q4(b): "What is the purpose of multiplexing?" [1]
- **(REPEAT x2)** F16 Q5(a): "What is a TDM? Why statistical TDM is better than synchronous TDM?" [2+2]; F19 Q4(e): "Why is statistical TDM better than synchronous TDM?" [1]
- **(REPEAT x2)** F16 Q5(b): "Distinguish between multi-level and multiple-slot TDM." [4]; F17 Q4(h): "Explain Multiple-slot multiplexing with a figure." [2]
- F20 Q4(c): "What is Pulse Stuffing?" [1]

**Spread spectrum**
- **(REPEAT x2 for FHSS)** F15 Q2(a): "What is the difference and similarity between FDM and FHSS? Describe FHSS." [7.5]; F16 Q6(a): "Define FHSS and explain how it achieves bandwidth spreading." [6]
- F15 Q1(b)(iv): "DSSS-stands for what? Why does it named so?" [1]
- F20 Q1(f): "Write one difference between FHSS and DSSS." [1]

### Chapter 7 — Transmission media

- TT1 Q4: "a. Define refraction and reflection. b. Name the major classes of guided media." [5]
- F17 Q1(e): "How does guided media differ from unguided media?" [2]
- F15 Q1(b)(i): "Give example for twisted pair cable, coaxial cable and fiber optic cable." [1]
- **(REPEAT x2, fiber pros/cons)** F17 Q4(d): "Name the advantages of optical fiber over twisted-pair and coaxial cable." [2]; F16 Q4(f): "Write down two disadvantages of Fiber optic cable." [1]
- F17 Q4(g): "What is the purpose of cladding in an optical fiber?" [2]
- F17 Q1(f): "Why do optical signals used in fiber optic cables have a very short wave length?" [2]
- F20 Q4(a): "What is the difference between STP and UTP?" [1]
- F16 Q4(d): "What is the frequency range of VHF?" [1]
- F20 Q1(g): "What is the propagation method for Radio wave?" [1]

### Chapter 8 — Switching

- **(REPEAT x3)** F17 Q3(b): "We need a three-stage space-division switch with N = 100. We use 10 crossbars at the first and third stages and 4 crossbars at the middle stage. i) Draw the configuration diagram. ii) Calculate the total number of cross points. iii) Find the possible number of simultaneous connections. iv) Find the possible number of simultaneous connections if we use one single crossbar (100 x 100). v) Find the blocking factor, the ratio of the number of connections in c and in d." [10] (= P8-12)
  - F20 Q2(f): same switch, only "i) Draw the configuration diagram. ii) Calculate the total number of crosspoints." [2.5]
  - F16 Q5(c): "Design a three-stage, 100 × 100 switch (N = 100) with k = 4 and n = 10." [4]
- F16 Q4(h): "For n inputs and n outputs, Banyan switch has ______ stages with ______ microswitches at each stage." [1]
- F16 Q6(c): "What is a Virtual-Circuit Network? Explain different phases of it." [6]
- F16 Q4(g): "What is VCI?" [1]
- F16 Q4(a): "What is the total delay in a Datagram network?" [1]

### Chapter 10 — Error detection and correction

**Hamming distance**
- **(REPEAT x2)** F17 Q6(b)(i): "What is the minimum Hamming distance? If we want to be able to detect two-bit errors, what should be the minimum Hamming distance?" [2]; F20 Q2(e): same words [2.5] (= Q10-5, Q10-6)
- F16 Q5(e): "What is minimum hamming distance? What is the Minimum Hamming Distance of the following codebook: 00000, 00010, 00111, 10011, 11011" [1+3]
- **(REPEAT x3, compute d(x,y))** F16 Q4(k): "What is the Hamming distance for d(10000, 00100)?" [1]; F19 Q1(a): "What is the hamming distance between 1001 and 0001?" [1]; F20 Q4(g): "What is the hamming distance for each of the following codewords? i) d(10000, 11010) ii) d(11111, 10000)" [1]

**Parity and checksum**
- TT2-old Q1: "Let us assume that k = 3 and n = 4. Show the list of datawords and codewords in a table for Simple parity-check code C(4,3)." [5] (book's Table 10.2 is C(5,4); same idea, one bit smaller)
- **(REPEAT x2)** F15 Q6(e): "Explain Simple Parity Check and Checksum with appropriate example." [~5]; F16 Q6(e): "Explain Simple Parity Check and Checksum with appropriate example. Find the parity bits for the following bit pattern, using simple parity. Do the same for two-dimensional parity. Assume even parity. ← 0011101 1100111 1111111 0000" [2+1+1+1+1]
- F20 Q5(f): "Assuming even parity, find the parity bit for 11001100." [2.5]
- F20 Q3(c): "Suppose you want to send a data of five 8-bit numbers: 16, 19, 25, 0, 9. Calculate wrapped sum and checksum. If there is no error occurred in transmission, show that the data have not been corrupted on the receiver side." [5]

**CRC and polynomials**
- **(REPEAT x4, CRC by long division)**
  - F15 Q5(a): "Which type of technique the CRC is? For CRC code 1101 and data 1011011, define the code word. If there is an error in receiver side, write the process of detection." [10]
  - F16 Q6(d): "Given the dataword 1010011110 and the divisor 10111 i) Show the generation of the CRC codeword at the sender site. [3] ii) Show the checking of the codeword at the receiver site assuming no error has occurred. [3]"
  - F17 Q6(b)(ii): "Given the dataword 10100111 and the divisor 10111, show the generation of the CRC codeword at the sender site (using binary division)." [5]
  - F19 Q6(a): "Given, the dataword is 1010100110 and the divisor is 11001, what is the generated CRC codeword? Show the decoding at the receiver." [5]
- **(REPEAT x2)** F17 Q1(h): "What is the polynomial representation of 10101011?" [2]; F20 Q4(h): "What is the polynomial representation of 10110011?" [1]
- F20 Q1(d): "What is the binary representation of x^8 + x^3?" [1]
- F20 Q1(e): "What is the result of shifting 111110 four bits to the right?" [1] (= P10-14d)

**Error types, FEC, interleaving**
- F19 Q5(a): "Define the types of errors that occur during digital communication." [2.5]
- F16 Q4(j): "What is a burst error?" [1]
- **(REPEAT x2)** F15 Q4(g): "Define: Forward Error Correction and Retransmission." [~2]; F19 Q4(d): "Define forward error correction." [1]
- F17 Q6(b)(iii): "Describe Chunk Interleaving process." [3]
- F15 Q5(b): "'Hamming Code is a more acceptable process'-true or false-justify. Define the hamming code for the data 1001101 step by step." [10] (4e-style topic; low priority)

### Chapter 11 — Data link control

- **(REPEAT x2)** F17 Q3(c): "i) Explain Stop-and-Wait Protocol. [4] ii) Draw the flow diagram of Stop and Wait Protocol with Sequence Number and Acknowledgment numbers using the following scenario: 1) Frame 0 is sent, but lost. 2) Frame 0 is resent and acknowledged. 3) Frame 1 is sent and acknowledged, but the acknowledgment is lost. 4) Frame 1 is resent and acknowledged. [6]" (= P11-8)
  - F20 Q6(c): "Draw the flow diagram of the Stop and Wait Protocol with Sequence Number and Acknowledgment numbers using the following scenario: i) Frame 0 is sent, but lost. ii) Frame 0 is resent and acknowledged. iii) Frame 1 is sent and acknowledged, but the acknowledgment is lost. iv) Frame 1 is resent, but it is timed-out. v) Frame 1 is resent and acknowledged." [5]
- F15 Q1(b)(v): "What is the meaning of ACK-3 and NAK-3?" [1]
- F16 Q4(l): "How many protocols does a noisy channel have?" [1] (4e wording; in 5e think "Stop-and-Wait, Go-Back-N, Selective-Repeat")
- TT2-old Q3: "Briefly explain the key responsibilities of Data link layer." [5] (5e §9.1 — framing, flow control, error control, congestion control)
- TT2-old Q4: "a. Explain why flags are needed when we use variable-size frames. b. Compare and contrast byte-oriented and bit-oriented protocols." [5] (= Q11-2, Q11-4)
- **(REPEAT x2 for byte vs bit)** F15 Q3(a): "What is the advantage of bit oriented protocol over byte oriented protocol in case of error handling (describe with an example)? Define a bit oriented protocol." [~10, mark cut off]

### Readability notes

- F15 photo: right edge cut. Visible: Q1a "5*2=10", Q1b "5*1=5", Q2 "2*7.5", Q4 "5*…", Q5 "10*2", Q6 "4*…". Q3's mark label is not visible. Text itself is fully readable.
- F16 page 1: a folded strip at the very bottom shows a half-hidden line ("…suppose a process… stages takes 20ms") — **unreadable**, and probably the start of another page under the fold, not a Ch5–11 question.
- TT2-25: no marks per question printed, only "Marks: 20". Figures described in words above.
- Everything else was clear.

---

## 5. The 12-hour schedule (highest yield first)

Rule for every block: **read the worked example, close the file, redo it on paper, then do the matching past question above.** Reading alone does not count.

| Clock | Block | What exactly | File |
|---|---|---|---|
| 0:00–1:15 | **B1. Ch5 numbers** | `r = log2 L`, `S = N/r`, `B = (1+d)S`, carrier = middle of band, BFSK/MFSK, QAM data rate. Do: the 8000/1000 question, P5-3 (4 parts), F20 Q5d, F19 Q5d, F16 Q2e, F17 Q1a, F17 Q6c(i). Then constellations: P5-5 (TT2-25 Q5, all 4), BPSK/8-QAM, 8-PSK with bit labels. | 11 |
| 1:15–1:50 | **B2. AM / FM / PM drawings + Ch5 theory** | Draw AM and FM once each for a sine modulating signal (TT2-25 Q1, Q2). Read the AM picture backwards (Q3). Memorise: ASK vs FSK, which is noisiest and why, QAM advantage. | 11 |
| 1:50–2:05 | **Break 1** | Eat, walk, water. No phone scrolling. | — |
| 2:05–3:05 | **B3. Ch6** | FDM bandwidth with/without guard bands + draw the band (TT2-25 Q6, F19 Q2f). Sync TDM (Example 6.6 / F20 Q3a / TT1 Q3). Output-stream question (F17 Q6c-ii). Pulse stuffing (F16 Q6b). Then the definitions: why multiplex, statistical vs sync, multilevel / multiple-slot, FHSS vs DSSS, WDM use. | 11 |
| 3:05–4:20 | **B4. Ch10** | Hamming distance (XOR, count 1s), d_min rules, codebook d_min (F16 Q5e). Parity table C(4,3), even parity bit. **Two CRC divisions by hand** (F17 10100111/10111 and F19 1010100110/11001) incl. receiver check. Polynomials both ways + shifting. Checksum with 16,19,25,0,9. | 13 |
| 4:20–5:00 | **B5. Ch11** | Draw the Stop-and-Wait diagram for F20 Q6c (5 steps) **twice**, from memory the second time. Flags for variable-size frames, byte vs bit-oriented, byte stuffing, bit stuffing (after five 1s add a 0). DLL duties list. | 13 |
| 5:00–5:45 | **B6. Ch7 + Ch8** | 3-stage switch N=100 (crosspoints, connections, blocking) — one numeric, done once, it's x3. VC network phases (setup, data transfer, teardown), VCI, datagram total delay, Banyan stages. Media short answers: guided vs unguided, 3 guided classes, fiber pros/cons, cladding, STP vs UTP, VHF range, propagation types. | 12 |
| 5:45–9:45 | **Break 2: SLEEP (4 h)** | Set two alarms. Sleep moves short-term memory into long-term memory. Skipping it costs more marks than any block above. | — |
| 9:45–10:15 | **B7. Formula rewrite** | Write the Section 7 checklist from memory on blank paper. Check. Re-learn only the ones you missed. Glance at Ch4 PCM (TT2-25 asked it). | this file |
| 10:15–11:15 | **B8. Timed mock** | `14-mid2-mock-paper.md`. Real timing: 45 min Part A + 15 min Part B. Closed book. | 14 |
| 11:15–11:45 | **B9. Mark + patch** | Mark against the chapter files. Fix only the two worst topics. | 11–13 |
| 11:45–12:00 | Go | Pens, pencil, ruler, eraser, calculator. Last look at the checklist. | — |

### If you only have 3 hours

| Time | Do this |
|---|---|
| 0:00–0:35 | Bits/baud (`r = log2 L`, `S = N/r`), 8000/1000 question, `B = (1+d)S`. Constellations: P5-5 four cases + 8-QAM (1 and 3, four phases). |
| 0:35–1:05 | Hamming distance + d_min rules + even parity + **one** CRC division with receiver check. |
| 1:05–1:35 | FDM `n·B + (n−1)·g` (TT2-25 Q6) and sync TDM Example 6.6 (four 1-Mbps lines). |
| 1:35–2:00 | Stop-and-Wait diagram (F20 Q6c), byte vs bit-oriented in 4 lines. |
| 2:00–2:20 | Sketch AM and FM once. |
| 2:20–2:40 | 3-stage switch crosspoint formula with N=100, n=10, k=4. |
| 2:40–3:00 | Rewrite Section 7 checklist from memory. |

### If you only have 1 hour

| Time | Do this |
|---|---|
| 0–15 min | `r = log2 L`, `S = N/r`, `B = (1+d)S`. Answer the 8000/1000 question. Draw the 8-QAM constellation (circles radius 1 and 3, points at 0°, 90°, 180°, 270°). |
| 15–30 min | d(x,y) = number of 1s in x XOR y. Detect s errors: d_min = s+1. Correct t: d_min = 2t+1. One CRC: append (divisor length − 1) zeros, XOR-divide, remainder is the CRC. |
| 30–40 min | FDM total = channels × width + gaps × guard. Sync TDM: output bit rate = n × input; output bit duration = input duration / n. |
| 40–50 min | Stop-and-Wait diagram: frames 0,1,0,1…; ACK number = next frame expected; lost frame/ACK → timer runs out → resend same number. |
| 50–60 min | Rewrite Section 7 checklist once. |

---

## 6. Doomsday answers (fewest words that still earn marks)

- "Why multiplex?" → "To share one expensive high-bandwidth link among many devices; the link's capacity is bigger than one device needs."
- "Statistical vs synchronous TDM" → "Synchronous gives every input a fixed slot even if it has nothing to send (empty slots waste bandwidth). Statistical gives slots only to inputs that have data, so no empty slots; each slot must carry an address."
- "Most noise-susceptible" → "ASK, because noise mainly changes amplitude, and ASK stores the data in the amplitude."
- "Why flags for variable-size frames" → "Receiver needs to know where one frame ends and the next starts; with variable sizes there's no fixed length to count, so a special flag pattern marks the boundaries."
- "Byte vs bit-oriented" → "Byte-oriented: data are 8-bit characters, flag is a byte, uses byte stuffing (escape byte). Bit-oriented: data are a bit stream, flag is 01111110, uses bit stuffing (0 after five 1s). Bit-oriented is more efficient and handles any data."
- "Cladding" → "Less dense layer around the core so light hitting the boundary reflects back into the core instead of leaking out."

---

## 7. Night-before / morning-of checklist (rewrite from memory)

**Ch5**
- `r = log2 L`  (L = number of signal levels / points / frequencies / phases)
- `S = N / r`  (baud = bit rate / bits per signal element),  `N = S × r`
- ASK, PSK, QAM bandwidth: `B = (1 + d) × S`; carrier `fc` = middle of the band
- BFSK: `B = (1 + d) × S + 2Δf`; MFSK (carriers S apart, d=0): `B = L × S`
- Peak amplitude of an I/Q point = `√(I² + Q²)`; phase = angle from +I axis
- Constellation reading: points only on I axis, different distances → ASK; same distance, different angles → PSK; both differ → QAM; BPSK = (A,0),(−A,0); QPSK = 4 points at 45°,135°,225°,315°
- AM: `B = 2B_audio`; FM: `B = 2(1 + β)B_audio`; PM: `B = 2(1 + β)B_audio` (β differs)
- AM picture: carrier = the fast wiggles; modulating signal = the envelope (trace the peaks). FM picture: wiggles get tighter where the modulating signal is high.

**Ch6**
- FDM: `B_link = n × B_channel + (n − 1) × guard`
- Sync TDM (n inputs, 1 unit = 1 bit): output bit rate = `n × input rate`; output bit duration = `input bit duration / n`; frame rate = input rate (in units/s); frame duration = 1 / frame rate = one input bit duration; frame size = `n × unit + sync bits`
- Pulse stuffing: add dummy bits so the slow line matches the fast line, then treat as equal rates
- FHSS = hop between carrier frequencies using a pseudorandom code; DSSS = replace each bit with n chips (spreading code)

**Ch7**
- Guided = twisted-pair, coaxial, fiber-optic. Unguided = radio, microwave, infrared
- Propagation: ground, sky, line-of-sight. VHF = 30–300 MHz (sky and line-of-sight; VHF TV, FM radio)
- Fiber: core denser than cladding; critical angle; light reflects

**Ch8**
- 3-stage switch: N inputs, first stage N/n crossbars of n×k, middle k crossbars of (N/n)×(N/n), last stage N/n of k×n
- Crosspoints = `2kN + k(N/n)²`;  single crossbar = `N²`
- Clos: `n = √(N/2)`, `k = 2n − 1`
- Banyan, n inputs: `log2 n` stages, `n/2` microswitches each
- Datagram total delay (2 switches): `3T + 3τ + w1 + w2`
- VC phases: setup → data transfer → teardown

**Ch10**
- `d(x, y)` = number of 1s in `x XOR y`
- Detect s errors: `d_min = s + 1`. Correct t errors: `d_min = 2t + 1`
- Simple parity: `n = k + 1`, `d_min = 2`, detects any odd number of errors
- CRC: add (divisor bits − 1) zeros, XOR long division, append remainder. Receiver divides whole codeword: remainder 0 = no error
- Polynomial: rightmost bit is `x^0`. Shift left m bits = multiply by `x^m`; right = divide (drop low terms)
- Checksum (m-bit): add all, wrap carries back in (wrapped sum), checksum = complement of wrapped sum. Receiver: add all + checksum, wrap, complement → 0 means OK

**Ch11**
- Bit stuffing: after five consecutive 1s insert a 0. Flag = `01111110`
- Byte stuffing: put ESC before any data byte that looks like FLAG or ESC
- Stop-and-Wait: sequence numbers 0,1,0,1 (mod 2); ACK number = number of the **next** frame expected; sender keeps a copy + timer, resends on timeout
- HDLC frame types: I-frame, S-frame, U-frame. PPP is byte-oriented, HDLC is bit-oriented

**Exam technique**
- 20 marks in 60 min = 3 min per mark. A 2-mark question gets 6 minutes, not 15.
- Always write the formula first, then numbers, then the unit. Formula alone earns part marks.
- For drawings: label axes, label I and Q, write amplitudes and angles on the picture.
