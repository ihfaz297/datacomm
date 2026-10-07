# Ch5 + Ch6: Analog Transmission and Bandwidth Utilization

Source: Forouzan 5e, Ch5 (printed pages 135-154) and Ch6 (pages 155-184).
Past papers checked: 2014-15, 2015-16 (exam 2018), 2016-17, 2018-19, 2019-20,
TT-01, DataCom_TT2, and the **TT2 of 28 Aug 2025** (the `tt2/` photos). That last one
is your own teacher's most recent paper. It is almost entirely Ch5 + Ch6. Treat it as
the best guess for tomorrow.

Every number in this file was recomputed in Python.

---

## How to use this file (12 hours left)

1. Read the **Ch5 concepts + formula box** (40 min).
2. Do the **Ch5 past-paper solutions** with the answer covered (45 min).
3. Same for **Ch6** (1.5 h).
4. Do both **practice sets**, check against **Answers** at the bottom (1 h).
5. Night before / morning: the two **Doomsday boxes** only.

Symbols used everywhere (learn these first):

| Symbol | Meaning | Unit |
|---|---|---|
| N | bit rate (data rate): bits sent per second | bps |
| S | baud rate (signal rate): signal elements sent per second | baud |
| r | bits carried by one signal element ("bits per baud") | bits/baud |
| L | number of different signal elements (levels, frequencies, phases, or points) | - |
| B | bandwidth needed | Hz |
| d | a filtering factor between 0 and 1. The question tells you. If not, say "assume d = 0" | - |
| fc | carrier frequency (the centre of the band) | Hz |
| 2Δf | gap between two neighbouring FSK carrier frequencies | Hz |
| β | FM/PM factor (FM usually 4; PM 1 to 3) | - |
| n | number of input lines in a multiplexer | - |

---

# PART 1 - CHAPTER 5: ANALOG TRANSMISSION

## 5.0 What they ask (past papers)

| Year | Question | Marks | Type |
|---|---|---|---|
| **TT2 2025** Q1 | Choose a carrier, draw the **AM** signal for a given message wave | ~2-3 | drawing |
| **TT2 2025** Q2 | Choose a carrier, draw the **FM** signal for a given message wave | ~2-3 | drawing |
| **TT2 2025** Q3 | From an AM signal, find the carrier frequency and the message signal | ~2 | reading a figure |
| **TT2 2025** Q5 | Points (2,0),(3,0) / (3,0),(-3,0) / (±2,±2) / (0,2),(0,-2): draw, give peak amplitude, name the modulation | ~4 | constellation (Forouzan P5-5) |
| **TT2 2025** Q8, 2014-15 Q5c, 2019-20 Q5c | 8000 bps, 1000 baud: bits per element? how many elements? | 2-3 | r and L (Forouzan Ex 5.2) |
| 2014-15 Q5c | Name three mechanisms for digital-to-analog modulation | 1 | theory |
| 2014-15 Q4d, 2018-19 Q1b | Define bit rate, baud rate | 1 | theory |
| 2014-15 Q6b | Advantages of QAM over ASK. Explain QPSK with figures | 4 | theory + figure |
| 2014-15 Q6f, 2015-16 Q5f | Constellation for **8-PSK** with bits and phases | 4 | drawing |
| 2015-16 Q1l, 2016-17 Q5f | Bits per baud: ASK 4 amplitudes, FSK 8 frequencies, PSK 4 phases, QAM 128 points | 1-5 | r = log2 L (Forouzan P5-3) |
| 2015-16 Q2e | 2 bits at a time, 4 Mbps, carrier 10 MHz: levels, baud rate, bandwidth | 4 | MFSK (like Forouzan Ex 5.6) |
| 2015-16 Q2g | What is a carrier frequency? Explain PSK with a figure | 4 | theory + figure |
| 2015-16 Q3f, 2016-17 Q2c, 2019-20 Q2a | Constellations: BPSK peak 2 or 3; 8-QAM (amplitudes 1, 3; 4 phases); 16-QAM (2 amplitudes, 8 phases) | 5-6 | drawing (Forouzan P5-4) |
| 2015-16 Q4c | Bandwidth equation for ASK | 1 | formula |
| 2015-16 Q4e | QPSK: how many phases, what angles | 1 | fact |
| 2016-17 Q1a | Cable TV channel 6 MHz, 64-QAM: data rate per resident | 2 | Forouzan P5-10 |
| 2016-17 Q4a | Differences between ASK and FSK | 2 | theory |
| 2016-17 Q6c(i) | 1 MHz medium, 10 channels of 10 Mbps, QAM, d = 0: bits/baud and points | 5 | Forouzan P5-9 |
| 2018-19 Q1e | Bandwidth equation for BFSK | 1 | formula |
| 2018-19 Q1h | 4 bits per element, 1000 elements/s: bit rate | 1 | Forouzan Ex 5.1 |
| 2018-19 Q3b | Discuss ASK, FSK, PSK with an example | 5 | theory + figures |
| 2018-19 Q5d | Bandwidth for 12 Mbps QPSK, d = 0 | 2.5 | Forouzan Ex 5.7 |
| 2019-20 Q4d | Which of ASK/FSK/PSK/QAM is most susceptible to noise? | 1 | Forouzan Q5-5 |
| 2019-20 Q5d | 100 kHz band from 200-300 kHz, ASK with d = 1: carrier and bit rate | 2.5 | Forouzan Ex 5.3 |

**Pattern:** the teacher copies Forouzan's examples and end-of-chapter problems almost
word for word. If you can do Ex 5.1-5.7 and P5-1 to P5-12, you have seen the exam.

---

## 5.1 Concepts in plain English

### 5.1.1 Why "analog transmission" at all?

Some channels only pass a band of frequencies that does **not** start at 0 Hz. Radio,
TV channels and telephone lines are like this. This is called a **band-pass channel**.
A plain digital signal (line code from Ch4) needs a channel that starts at 0 Hz
(a **low-pass** channel). So we cannot send it directly.

Fix: take a high-frequency sine wave, the **carrier**, and change one of its three
properties to carry our data:

- amplitude (height)
- frequency (how fast it wiggles)
- phase (where in its cycle it starts)

This changing is called **modulation**. For digital data it is called **shift keying**.

### 5.1.2 Carrier signal (2015-16 Q2g asks this)

> **Carrier signal / carrier frequency:** a high-frequency sine wave produced by the sender.
> It acts as the base for the information. The receiver is tuned to that frequency. The
> data changes the carrier's amplitude, frequency or phase.

The carrier sits in the **middle** of the band we use. That is why it is called fc
("frequency of the carrier") and why "fc = middle of the band" in every numerical.

### 5.1.3 Bit rate vs baud rate (asked almost every year)

- **Bit rate N** = number of bits sent per second (bps).
- **Baud rate S** = number of **signal elements** sent per second (baud).
- One signal element can carry several bits. Analogy from the book: a baud is a car,
  a bit is a passenger. More passengers per car = fewer cars = less traffic (bandwidth).

```
r = log2 L          (L different signal elements carry r bits each)
S = N / r           (baud rate)
N = S x r           (bit rate)
```

In analog transmission, **baud rate is always less than or equal to bit rate.**

### 5.1.4 The four digital-to-analog methods (2014-15 Q5c: "name three mechanisms")

```
Digital-to-analog
 |-- ASK  (Amplitude Shift Keying)      change amplitude
 |-- FSK  (Frequency Shift Keying)      change frequency
 |-- PSK  (Phase Shift Keying)          change phase
 '-- QAM  (Quadrature Amplitude Mod.)   change amplitude AND phase
```

Three mechanisms = ASK, FSK, PSK. QAM is a mix of ASK and PSK, and it is the best one.

### 5.1.5 ASK (Amplitude Shift Keying)

- The **amplitude** changes. Frequency and phase stay the same.
- **Binary ASK** = **On-Off Keying (OOK)**: bit 1 = carrier on (full amplitude),
  bit 0 = carrier off (amplitude 0).
- How it is built: multiply a unipolar NRZ signal (1 V / 0 V) by the carrier.
- Bandwidth: **B = (1 + d) S**. For binary ASK, r = 1 so S = N.
- The band is centred on fc.

```
bits:      0        1        0        1        1
        ________ /\/\/\/\ ________ /\/\/\/\ /\/\/\/\
                 \/\/\/\/          \/\/\/\/ \/\/\/\/
         (off)    (on)     (off)    (on)     (on)
```

Weakness: noise mostly changes **amplitude**, so ASK is the **most noise-sensitive**.

### 5.1.6 FSK (Frequency Shift Keying)

- The **frequency** changes. Amplitude and phase stay the same.
- **Binary FSK (BFSK)**: bit 0 uses frequency f1, bit 1 uses frequency f2.
- f1 and f2 are each Δf away from the middle, so they are **2Δf apart**.
- Think of BFSK as **two ASK signals side by side**, one at f1 and one at f2.

```
bits:      0           1          0          1
        /\  /\  /\  /\/\/\/\/\  /\  /\   /\/\/\/\/\
          \/  \/  \/ \/\/\/\/\/   \/  \/  \/\/\/\/\/
         (slow f1)  (fast f2)   (slow f1)  (fast f2)
```

Bandwidth for BFSK (2018-19 Q1e):

```
B = (1 + d) S + 2Δf          (2Δf must be at least S)
```

**Multilevel FSK (MFSK):** use L frequencies to send r = log2 L bits at a time.
Neighbouring frequencies are 2Δf apart. With 2Δf = S (the minimum) and d = 0:

```
B = (1 + d) S + (L - 1) 2Δf   ->   B = L x S
```

MFSK uses the most bandwidth, but it is good when noise is very bad.

### 5.1.7 PSK (Phase Shift Keying)

- The **phase** changes. Amplitude and frequency stay the same.
- **BPSK** (binary PSK): bit 1 = phase 0°, bit 0 = phase 180° (the wave is flipped).
- How it is built: multiply a **polar** NRZ signal (+V / -V) by the carrier.
- Bandwidth: same as ASK, **B = (1 + d) S**. Less than FSK.

```
bits:      0         1         0         1         1
         \/\/\/\   /\/\/\/   \/\/\/\   /\/\/\/   /\/\/\/
         /\/\/\/   \/\/\/\   /\/\/\/   \/\/\/\   \/\/\/\
        (180°)     (0°)     (180°)     (0°)      (0°)
   At each 0<->1 change, the wave "jumps" (it starts going down instead of up).
```

Why PSK is better than ASK: noise changes amplitude easily, phase much less.
Why PSK is better than FSK: it needs only one carrier frequency.
Cost: the receiver hardware must tell phases apart, so it is more complex.

### 5.1.8 QPSK (Quadrature PSK) (2014-15 Q6b, 2015-16 Q4e)

- Sends **2 bits per signal element** (r = 2, L = 4).
- Built from **two BPSK modulators**:
  - the incoming bits go through a serial-to-parallel converter;
  - one bit goes to the **in-phase (I)** carrier, the next bit to the **quadrature (Q)**
    carrier (the same carrier shifted by 90°);
  - each BPSK gets bits at half the original rate;
  - the two outputs are added. The sum is one sine wave with one of **4 phases**.
- **The four phases: 45°, 135°, -135° (= 225°), -45° (= 315°).**
- Book mapping (Fig 5.11): **11 -> 45°, 01 -> 135°, 00 -> -135°, 10 -> -45°.**

```
Block diagram (draw this for "explain QPSK with figure"):

             +--> bit to I ---(x)<--- carrier cos (oscillator)
  bits --> S/P                 \
  in    converter               (+)----> QPSK signal
             +--> bit to Q ---(x)<--- carrier shifted 90°
```

Constellation of QPSK:

```
                Q
                |
         01 *   |   * 11
        (135°)  |   (45°)
     -----------+-----------> I
         00 *   |   * 10
       (-135°)  |  (-45°)
                |
```

Same bandwidth formula, B = (1 + d) S, but S = N/2. So QPSK needs **half** the
bandwidth of BPSK for the same bit rate.

### 5.1.9 Constellation diagram (always on the paper)

A constellation diagram is a dot picture of all the signal elements.

- **X axis = in-phase carrier (I).** **Y axis = quadrature carrier (Q).**
- Each **dot** = one kind of signal element. Write its bits next to it.
- From a dot at (I, Q) you can read:
  - **peak amplitude** = distance from origin = sqrt(I² + Q²)
  - **phase** = angle from the +X axis
- Number of dots = L. Bits per dot = r = log2 L.

```
   ASK (OOK)           BPSK                 QPSK
      Q                   Q                    Q
      |                   |               01 * | * 11
  ----*-----*-->I    -*---+---*--> I     ------+------> I
      0     1         0   |   1           00 * | * 10
   (at 0)  (at A)    (-A)    (+A)
```

### 5.1.10 QAM (Quadrature Amplitude Modulation)

- Change **both** amplitude and phase. QAM = ASK + PSK.
- Uses two carriers (I and Q), each with several amplitude levels.
- 4-QAM with polar levels is exactly QPSK. 16-QAM has 16 dots (r = 4). 64-QAM has 64 dots (r = 6).
- Bandwidth: same as ASK and PSK, **B = (1 + d) S**.

**Advantages of QAM over ASK** (2014-15 Q6b):
1. More bits per baud (r = 4, 6, ...), so a much higher bit rate in the same bandwidth.
2. Less sensitive to noise, because information is also in the phase, not only in the amplitude.
3. Same minimum bandwidth as ASK for the same baud rate.
4. It is the method used today (cable modems, ADSL, Wi-Fi).

### 5.1.11 Which method is most hurt by noise? (2019-20 Q4d, Forouzan Q5-5)

**ASK.** Noise is mostly added to the amplitude of a signal. ASK carries its information
only in the amplitude, so noise directly corrupts it. FSK and PSK keep the amplitude
constant, so the receiver can ignore amplitude changes. (Same logic for analog:
**AM is the most noise-sensitive** of AM, FM, PM.)

### 5.1.12 ASK vs FSK (2016-17 Q4a)

| | ASK | FSK |
|---|---|---|
| What changes | amplitude | frequency |
| Constant | frequency, phase | amplitude, phase |
| Bandwidth | (1 + d) S | (1 + d) S + 2Δf (more) |
| Noise | very sensitive | more resistant |
| Carriers | one | two (or more) frequencies |
| Build | multiply unipolar NRZ by carrier | voltage-controlled oscillator (VCO) |

### 5.1.13 Analog-to-analog: AM, FM, PM

Here the **message is already analog** (voice, music). We move it to a different
frequency range so that many stations can share the air. The message is called the
**modulating signal**. Its bandwidth is **B**.

**AM (Amplitude Modulation)**
- The carrier's amplitude follows the message. Frequency and phase do not change.
- The message becomes the **envelope** (the outline) of the carrier.
- Built with a multiplier (message x carrier).
- **B_AM = 2B.** (Upper and lower halves carry the same info.)
- AM radio: audio B = 5 kHz, so each station gets **10 kHz**. Band 530 to 1700 kHz.

**FM (Frequency Modulation)**
- The carrier's frequency follows the message's **voltage**. Amplitude stays constant.
- Message high -> waves squeezed together (higher frequency).
  Message low -> waves spread out (lower frequency).
- Built with a voltage-controlled oscillator (VCO).
- **B_FM = 2(1 + β)B**, β usually 4. (This is Carson's rule.)
- FM radio: stereo audio about 15 kHz, FCC gives **200 kHz** per station. Band 88 to 108 MHz.

**PM (Phase Modulation)**
- The carrier's phase follows the message. Amplitude and frequency stay constant.
- Same as FM except that the frequency change follows the **slope (derivative)** of the
  message, not the message itself. Built with a d/dt block plus a VCO.
- **B_PM = 2(1 + β)B**, but β is smaller (about 1 narrowband, 3 wideband).

### 5.1.14 How to DRAW AM and FM (TT2 2025 Q1, Q2)

Step 1: "choose a carrier frequency" = draw a fast sine wave of constant height in the
carrier box. Use many cycles, about 10 to 20 across the box. Write next to it,
for example, "fc = 20 Hz (any fc much larger than the message frequency)".

Step 2 (AM): draw the message curve **and its mirror image** lightly as an envelope
(above and below the axis). Then fill in the carrier wiggles so each peak touches the
upper envelope and each trough touches the lower one. **Keep the wiggle spacing the same
everywhere.** Only the height changes.

```
AM: message (envelope) is big in the middle, small at the ends
           .-''''-.
   ..-''          ''-..          <- upper envelope = message
  /\/\/\/\/\/\/\/\/\/\/\/\
  \/\/\/\/\/\/\/\/\/\/\/\/
   ''-..          ..-''          <- lower envelope = mirror
           '-....-'
  Spacing of wiggles: SAME everywhere. Height: follows message.
```

Step 3 (FM): **keep the height constant.** Where the message is high, draw the waves
**close together**. Where the message is low (most negative), draw them **far apart**.

```
FM: message rises to a peak then falls to a trough
message: high................................low
FM:     /\/\/\/\/\/\  /\  /\   /\    /\     /\
        \/\/\/\/\/\/\/  \/  \/   \/    \/     \/
        (tight = high freq)          (wide = low freq)
  Height: SAME everywhere. Spacing: follows message.
```

Mark-earning sentences to write under the figure:
- AM: "Amplitude of the carrier follows the message; frequency and phase unchanged. B_AM = 2B."
- FM: "Frequency increases when the message voltage increases; amplitude constant. B_FM = 2(1+β)B."

### 5.1.15 Reading an AM signal back (TT2 2025 Q3)

- **Carrier frequency:** count the number of complete wiggles (peaks) in a known time
  window. fc = cycles / time. If no time is given, say "fc = (number of cycles) per
  window length".
- **Modulating signal:** trace the **tops of the peaks**. That curve (the envelope) is
  the message. Draw it in the empty "modulating signal" box.
- In the 2025 figure, the wiggles are small at the start, grow to a maximum in the
  middle, then shrink again. So the message is **one slow hump** (like half a cycle of a
  sine, or one cycle of a slow wave riding on a positive offset). The carrier has
  about 30 cycles across the box (count them on the real paper; the exact count
  is your fc in cycles per window).

---

## 5.2 Formula box - Ch5

| Formula | Symbols | When to use |
|---|---|---|
| r = log2 L, L = 2^r | r bits/element, L number of elements | "how many bits per baud", "how many levels/points" |
| S = N / r, N = S x r | N bit rate (bps), S baud rate (baud) | any bit rate <-> baud rate question |
| B = (1 + d) S | B bandwidth (Hz), d 0..1 | ASK, BPSK, QPSK, QAM |
| B = (1 + d) S + 2Δf | 2Δf gap between f1 and f2 (at least S) | binary FSK |
| B = (1 + d) S + (L - 1) 2Δf -> **B = L S** (if 2Δf = S, d = 0) | L frequencies | multilevel FSK |
| fc = (f_low + f_high) / 2 | band edges | "what carrier frequency" |
| f_i = fc ± S/2, fc ± 3S/2, ... | MFSK frequencies, S apart | listing the MFSK frequencies |
| peak = sqrt(I² + Q²), phase = atan(Q/I) | dot at (I, Q) | reading a constellation |
| B_AM = 2B | B = message bandwidth | AM |
| B_FM = 2(1 + β) B | β about 4 | FM (Carson's rule) |
| B_PM = 2(1 + β) B | β about 1-3 | PM |
| channels = band width / station width | | how many stations fit (Forouzan P5-12) |

Common r values: BPSK/BASK/BFSK 1, QPSK 2, 8-PSK/8-QAM 3, 16-QAM 4, 64-QAM 6, 256-QAM 8.

---

## 5.3 Worked past-paper solutions - Ch5

### PP5-1 (TT2 2025 Q8, 2014-15 Q5c, 2019-20 Q5c) = Forouzan Ex 5.2
*An analog signal has a bit rate of 8000 bps and a baud rate of 1000 baud. How many data
elements are carried by each signal element? How many signal elements do we need?*

Given: N = 8000 bps, S = 1000 baud.

1. Bits per element: r = N / S = 8000 / 1000 = **8 bits per signal element**.
2. Signal elements needed: L = 2^r = 2^8 = **256 different signal elements**.

(2014-15 Q5c also asks: three mechanisms = **ASK, FSK, PSK**.)

### PP5-2 (2018-19 Q1h) = Forouzan Ex 5.1
*An analog signal carries 4 bits per signal element. If 1000 signal elements are sent per
second, what is the bit rate?*

r = 4, S = 1000 baud.
N = S x r = 1000 x 4 = **4000 bps**.

### PP5-3 (2015-16 Q1l, 2016-17 Q5f) = Forouzan P5-3
*Bits per baud for: (i) ASK with four amplitudes (ii) FSK with 8 frequencies (iii) PSK with
four phases (iv) QAM with 128 points.*

Rule: r = log2 L.

| Case | L | r = log2 L |
|---|---|---|
| ASK, 4 amplitudes | 4 | **2 bits/baud** |
| FSK, 8 frequencies | 8 | **3 bits/baud** |
| PSK, 4 phases | 4 | **2 bits/baud** |
| QAM, 128 points | 128 | **7 bits/baud** |

### PP5-4 (2018-19 Q5d) = Forouzan Ex 5.7
*Find the bandwidth for a signal transmitting at 12 Mbps for QPSK, d = 0.*

1. QPSK: r = 2.
2. S = N / r = 12 Mbps / 2 = 6 Mbaud.
3. B = (1 + d) S = (1 + 0) x 6 M = **6 MHz**.

### PP5-5 (2019-20 Q5d) = Forouzan Ex 5.3
*Available bandwidth 100 kHz, from 200 to 300 kHz. Carrier frequency and bit rate with ASK, d = 1?*

1. Carrier = middle of the band: fc = (200 + 300) / 2 = **250 kHz**.
2. B = (1 + d) S, so S = B / (1 + d) = 100 kHz / 2 = 50 kbaud.
3. ASK is binary, r = 1, so N = S x r = **50 kbps**.

(Compare Forouzan Ex 5.5: same band with **FSK**, d = 1, choose 2Δf = 50 kHz:
B = 2S + 50 = 100 -> S = 25 kbaud -> N = **25 kbps**. FSK gives half the bit rate
because it wastes 2Δf of the band.)

### PP5-6 (2016-17 Q1a) = Forouzan P5-10
*A cable company uses one cable TV channel (6 MHz bandwidth) for each resident. Data rate
per resident with 64-QAM?*

1. 64-QAM: r = log2 64 = 6 bits/baud.
2. Assume d = 0 (state it). Then S = B = 6 Mbaud.
3. N = S x r = 6 M x 6 = **36 Mbps**.

### PP5-7 (2016-17 Q6c(i)) = Forouzan P5-9
*Medium with 1-MHz bandwidth (low-pass). Need 10 independent channels, each at least
10 Mbps. Using QAM, d = 0. Minimum bits per baud per channel? Points in the constellation?*

1. Split the medium into 10 channels: 1 MHz / 10 = 100 kHz each.
2. d = 0, so S = B = 100 kbaud per channel.
3. r = N / S = 10 Mbps / 100 kbaud = **100 bits per baud**.
4. L = 2^r = **2^100 points** (about 1.27 x 10^30).
5. Comment: that is impossible in practice. The point of the question is that you need
   a much larger bandwidth.

### PP5-8 (2015-16 Q2e) - multilevel FSK (same method as Forouzan Ex 5.6)
*Send 2 bits at a time at 4 Mbps, carrier 10 MHz. Number of levels (frequencies), baud rate, bandwidth.*

1. Levels: L = 2^r = 2^2 = **4 frequencies**.
2. Baud rate: S = N / r = 4 Mbps / 2 = **2 Mbaud**.
3. The carriers must be 2Δf = S = 2 MHz apart.
4. Bandwidth (MFSK, d = 0): B = L x S = 4 x 2 MHz = **8 MHz**.
5. Placement around fc = 10 MHz: f1 = 7, f2 = 9, f3 = 11, f4 = 13 MHz.
   The band runs from 6 MHz to 14 MHz.

```
   |  f1  |  f2  |  f3  |  f4  |
   6      8      10     12     14  MHz
      7      9    ^   11     13
                  fc = 10 MHz          Bandwidth = 8 MHz
```

Textbook version (Forouzan Ex 5.6): 3 bits at a time, 3 Mbps, fc = 10 MHz ->
L = 8, S = 1 Mbaud, B = 8 x 1 = 8 MHz, frequencies 6.5, 7.5, ..., 13.5 MHz.

### PP5-9 (2015-16 Q4c, 2018-19 Q1e) - bandwidth equations
- ASK: **B = (1 + d) S**
- BFSK: **B = (1 + d) S + 2Δf**

### PP5-10 (2015-16 Q4e) - QPSK phases
**4 phases: 45°, 135°, 225° (-135°), 315° (-45°).** (4 phases -> 2 bits per element.)

### PP5-11 (TT2 2025 Q5) = Forouzan P5-5 - read the dots
*Draw, find peak amplitude, name the modulation. Numbers are (I, Q).*

**a. Two points (2, 0) and (3, 0)**
- Both on the I axis, same phase (0°), different distance from origin.
- Peak amplitudes: **2 and 3**.
- Only the amplitude differs -> **ASK** (binary ASK with levels 2 and 3, not OOK).

```
        Q
        |
  ------+-----*----*----> I
        0     2    3
            "0"  "1"
```

**b. Two points (3, 0) and (-3, 0)**
- Same distance (3), opposite sides: phases 0° and 180°.
- Peak amplitude: **3** (both).
- Only phase differs, two points -> **BPSK**.

```
        Q
        |
  --*---+---*--> I
   -3   |   3
  "0"       "1"
```

**c. Four points (2, 2), (-2, 2), (-2, -2), (2, -2)**
- Distance of each: sqrt(2² + 2²) = sqrt(8) = **2.83** (= 2√2).
- Phases: 45°, 135°, 225°, 315°. Same amplitude, 4 phases.
- -> **QPSK** (also called 4-QAM / 4-PSK). 2 bits per point.

```
           Q
      01 * | * 11      (-2,2)  (2,2)
   --------+--------> I
      00 * | * 10      (-2,-2) (2,-2)
```

**d. Two points (0, 2) and (0, -2)**
- On the Q axis. Distance 2 each. Phases 90° and 270° (-90°).
- Peak amplitude: **2**.
- Same amplitude, two phases -> **BPSK** (it just uses the quadrature carrier).

```
        Q
        * (0,2)   "1"
        |
  ------+------> I
        |
        * (0,-2)  "0"
```

### PP5-12 (2016-17 Q2c, 2015-16 Q3f, 2019-20 Q2a) = Forouzan P5-4 - constellations to draw

**i. BPSK with peak amplitude 2** (2015-16) or **3** (2016-17)
Two dots on the I axis at +A and -A: (2, 0) and (-2, 0) [or (3, 0) and (-3, 0)].
Phases 0° (bit 1) and 180° (bit 0). Same as the PP5-11b picture.

**ii. 8-QAM with two peak amplitudes 1 and 3, and four phases**
- 2 amplitudes x 4 phases = 8 points, so r = 3 bits per point.
- Choose phases 0°, 90°, 180°, 270°. Each phase gets one dot at distance 1 and one at 3.
- Points: (1,0), (3,0), (0,1), (0,3), (-1,0), (-3,0), (0,-1), (0,-3).

```
                 Q
                 * 010  (0,3)
                 |
                 * 011  (0,1)
                 |
  *------*-------+-------*-------*--> I
 110    111      |      001     000
(-3,0) (-1,0)    |     (1,0)   (3,0)
                 * 101  (0,-1)
                 |
                 * 100  (0,-3)
```

(Any 3-bit labels are fine as long as all 8 are different. Phases 45°, 135°, 225°,
315° are also accepted; then the dots are at (±0.71, ±0.71) and (±2.12, ±2.12).)

**iii. 16-QAM with two amplitudes and eight phases** (2019-20 wording)
- 2 amplitudes x 8 phases = 16 points, r = 4 bits.
- Phases 0°, 45°, 90°, ..., 315°. Two rings of 8 dots each.
- With the 2015-16 amplitudes **2 and 5**:
  - inner ring (radius 2): (2,0), (1.41,1.41), (0,2), (-1.41,1.41), (-2,0), (-1.41,-1.41), (0,-2), (1.41,-1.41)
  - outer ring (radius 5): (5,0), (3.54,3.54), (0,5), (-3.54,3.54), (-5,0), (-3.54,-3.54), (0,-5), (3.54,-3.54)

```
                    Q
          *         *          *        outer ring r = 5
                    |
               *    *    *              inner ring r = 2
          *    *----+----*     *  --> I
               *    *    *
                    |
          *         *          *
   (every 45°: one dot at r = 2, one at r = 5)
```

**Note on the 2015-16 wording** ("16-QAM with two amplitudes 2 and 5 and four phases"):
2 x 4 = 8 points only, so that is really 8-QAM. Write this in the exam: "2 amplitudes x 4
phases gives 8 points; for 16 points we need 8 phases" and draw the 8-phase version above.

### PP5-13 (2014-15 Q6f, 2015-16 Q5f) - 8-PSK constellation
- 8 phases, same amplitude, r = log2 8 = 3 bits per element.
- Phases 45° apart: 0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°.

| Bits | Phase |
|---|---|
| 000 | 0° |
| 001 | 45° |
| 010 | 90° |
| 011 | 135° |
| 100 | 180° |
| 101 | 225° |
| 110 | 270° |
| 111 | 315° |

```
                  Q
                 010
            011   *   001
              *   |   *
       100 *------+------* 000  --> I
              *   |   *
            101   *   111
                 110
   All 8 dots on one circle (same amplitude), 45° apart.
```

Explain in 2 lines: "8-PSK uses 8 phases of the same carrier and amplitude. Each signal
element carries 3 bits, so S = N/3."

### PP5-14 (2014-15 Q6b) - QAM over ASK + explain QPSK
- Advantages: see 5.1.10 (more bits/baud, less noise, same bandwidth, used today).
- QPSK: write section 5.1.8: S/P converter, two BPSK carriers 90° apart, added;
  4 phases 45°, 135°, 225°, 315°; r = 2; B = (1 + d) N/2. Draw the block diagram
  and the 4-dot constellation.

### PP5-15 (2015-16 Q2g) - carrier + PSK with figure
- Carrier definition: 5.1.2.
- PSK: 5.1.7 with the BPSK waveform sketch and the 2-dot constellation.
  "Phase changes, amplitude and frequency constant; 1 = 0°, 0 = 180°; less noise than
  ASK; B = (1 + d) S."

### PP5-16 (2018-19 Q3b) - discuss ASK, FSK, PSK with an example
Use bits **01011** for all three (the book's example). Draw the ASK, BFSK and BPSK
sketches from 5.1.5-5.1.7, one line each saying what changes and what stays constant,
and the bandwidth formula under each.

### PP5-17 (2019-20 Q4d) - most noise-sensitive
**ASK.** See 5.1.11.

---

## 5.4 Extra textbook examples (not yet asked, but likely)

**Forouzan Ex 5.4 (full duplex ASK).** Band 200-300 kHz split into two 50 kHz halves,
one per direction. Carriers at 225 kHz and 275 kHz. With d = 1: S = 50/2 = 25 kbaud,
**25 kbps each direction.**

**Forouzan P5-1 (baud rate):** 2000 bps FSK -> 2000 baud; 4000 bps ASK -> 4000 baud;
6000 bps QPSK -> 3000 baud; 36,000 bps 64-QAM -> 6000 baud.

**Forouzan P5-2 (bit rate from 1000 baud):** FSK 1000 bps; ASK 1000 bps; BPSK 1000 bps;
16-QAM 4000 bps.

**Forouzan P5-6:** 2 points -> 1 bit; 4 -> 2; 16 -> 4; 1024 -> 10 bits/baud.

**AM radio channels (P5-12a):** (1700 - 530) kHz / 10 kHz = **117 stations**.
**FM radio channels (P5-12b):** (108 - 88) MHz / 200 kHz = **100 channels** (only 50 used
at once in one area, alternate channels are kept empty).

---

## 5.5 Traps - Ch5

1. **Bit rate is not baud rate.** Bandwidth depends on **baud** rate S, not N. Always do S = N/r first.
2. "FSK with 8 frequencies" means L = 8, so r = 3. Not r = 8.
3. Binary ASK, BFSK, BPSK all have r = 1, so S = N.
4. FSK bandwidth has the **extra 2Δf**. Do not use (1 + d)S alone for FSK.
5. MFSK: B = L x S only when 2Δf = S and d = 0. Otherwise use the long formula.
6. If d is not given, write "assume d = 0" (minimum bandwidth) and say so.
7. Carrier = **middle** of the band, not the low edge.
8. QPSK phases are 45°, 135°, 225°, 315°, **not** 0°, 90°, 180°, 270°.
9. Peak amplitude of a QPSK dot at (2, 2) is 2.83, not 2.
10. A dot at (0, 2) is still PSK. Being on the Q axis does not make it "QAM".
11. AM bandwidth is **2B**, not B. FM uses β (usually 4): 2(1 + 4)B = 10B.
12. When drawing AM: keep wiggle **spacing** constant. When drawing FM: keep **height** constant.
13. "Number of points" is L = 2^r. Do not give r when they ask for points.

---

## 5.6 Practice set - Ch5 (answers at the bottom)

**C5-1.** A 16-QAM signal is sent at 1000 baud. What is the bit rate?

**C5-2.** (Forouzan P5-7) We must send 4000 bps. Let d = 1. Find the bandwidth for:
(a) ASK (b) FSK with 2Δf = 4 kHz (c) QPSK (d) 16-QAM.

**C5-3.** (Forouzan P5-8) A telephone line has 4 kHz bandwidth, d = 0. Maximum bit rate with:
(a) ASK (b) QPSK (c) 16-QAM (d) 64-QAM.

**C5-4.** (Forouzan P5-11) Find the bandwidth needed to modulate a 5 kHz voice with:
(a) AM (b) FM with β = 5 (c) PM with β = 1.

**C5-5.** A band runs from 200 kHz to 300 kHz. We use QPSK with d = 1. Find fc, the baud
rate and the bit rate.

**C5-6.** (Forouzan P5-4) Draw the constellation for: (a) ASK with peak amplitudes 1 and 3
(b) QPSK with peak amplitude 3. Give the (I, Q) coordinates of every dot.

**C5-7.** A constellation has 8 points: (1,1), (-1,1), (-1,-1), (1,-1), (3,3), (-3,3),
(-3,-3), (3,-3). Name the modulation, give r, and the two peak amplitudes.

**C5-8.** MFSK: send 3 bits at a time at 6 Mbps, carrier 20 MHz, 2Δf = S, d = 0. Find L, S,
B and the lowest and highest carrier frequencies.

**C5-9.** Which of AM, FM, PM is most affected by noise, and why?

**C5-10.** An analog signal carries 6 bits per signal element at 36 kbps. Find the baud rate
and the number of different signal elements.

---

## 5.7 DOOMSDAY BOX - Ch5 (15 minutes)

```
+------------------------------------------------------------------+
| r = log2 L     S = N / r     N = S x r                           |
| ASK / PSK / QAM :  B = (1+d) S                                   |
| BFSK            :  B = (1+d) S + 2Δf                             |
| MFSK (2Δf=S,d=0):  B = L x S                                     |
| fc = middle of the band                                          |
| AM: 2B     FM: 2(1+β)B (β≈4)     PM: 2(1+β)B (β≈1-3)             |
| AM radio 10 kHz/station (530-1700 kHz); FM 200 kHz (88-108 MHz)  |
|                                                                  |
| ASK=amplitude  FSK=frequency  PSK=phase  QAM=amplitude+phase     |
| BPSK 0°/180°.  QPSK 45,135,225,315 (11,01,00,10). 8-PSK: 45° apart|
| Constellation: X = I (in-phase), Y = Q (quadrature)              |
|   peak = sqrt(I²+Q²), angle = phase, #dots = L                   |
| Most noise-sensitive: ASK (and AM)                               |
| Draw AM: height follows message.  FM: spacing follows message.   |
+------------------------------------------------------------------+
```

---

# PART 2 - CHAPTER 6: BANDWIDTH UTILIZATION (MULTIPLEXING + SPREAD SPECTRUM)

## 6.0 What they ask (past papers)

| Year | Question | Marks | Type |
|---|---|---|---|
| **TT2 2025** Q6a-d | 3 voice channels of 4 kHz, guard bands 500 Hz: total bandwidth; draw the band from 1 kHz; repeat with no guard band | ~5 | FDM (Forouzan P6-1 / Ex 6.1) |
| 2018-19 Q2f | 5 channels of 100 kHz, guard band 10 kHz: minimum link bandwidth | 2.5 | Forouzan Ex 6.2 |
| 2014-15 Q4f, 2015-16 Q4i, 2018-19 Q4b | What is multiplexing and why is it needed? | 1 | theory |
| 2015-16 Q4b | One application of WDM | 1 | fact |
| 2015-16 Q5a, 2018-19 Q4e | What is TDM? Why is statistical TDM better than synchronous TDM? | 1-4 | theory |
| 2015-16 Q5b | Multilevel vs multiple-slot TDM | 4 | theory |
| 2016-17 Q4h | Explain multiple-slot multiplexing with a figure | 2 | theory + figure |
| 2015-16 Q6b | Pulse-stuffed TDM; 190 kbps + 180 kbps: frame size, frame rate, duration, data rate | 6 | Forouzan P6-9 |
| 2019-20 Q4c | What is pulse stuffing? | 1 | theory |
| 2019-20 Q3a | Four 1-Mbps lines, synchronous TDM, 1-bit unit: input/output bit duration, output bit rate, frame rate | 5 | Forouzan Ex 6.6 |
| TT-01 Q3 | Four 10-Mbps lines, same questions | 5 | same as Ex 6.6 |
| 2016-17 Q6c(ii) | TDM with 3 bits from each input + 1 framing bit: what is the output stream? | 5 | Forouzan P6-12 |
| 2014-15 Q1b(iv) | DSSS stands for what? Why is it named so? | 1 | theory |
| 2014-15 Q2a | Difference and similarity between FDM and FHSS; describe FHSS | 7.5 | theory |
| 2015-16 Q6a | Define FHSS and explain how it spreads bandwidth | 6 | Forouzan Q6-11 |
| 2019-20 Q1f | One difference between FHSS and DSSS | 1 | theory |
| 2014-15 Q2b, 2016-17 Q2f | CDMA (Walsh table, spreading codes) | 3-7.5 | **this is Ch12 in 5e**, bonus at the end |

---

## 6.1 Concepts in plain English

### 6.1.1 Multiplexing - what and why (asked 3 times)

> **Multiplexing** is the set of techniques that lets **many signals travel at the same
> time over one link**.

**Why needed:** a link (fiber, coax, microwave) usually has **far more bandwidth than one
user needs**. Unused bandwidth is wasted money. Multiplexing shares one expensive
high-bandwidth link among many users, instead of laying one cable per user.

Words:
- **MUX** (multiplexer): many inputs -> one stream (many-to-one).
- **DEMUX** (demultiplexer): one stream -> many outputs (one-to-many).
- **Link** = the physical path. **Channel** = the share of the link one pair of users gets.
  One link has n channels.

```
 line 1 --\                         /-- line 1
 line 2 ---> MUX ===== 1 link ===== DEMUX ---> line 2
 line 3 --/      (n channels)       \-- line 3
```

Three kinds:

```
Multiplexing
 |-- FDM  (Frequency-Division)   analog   - share the frequency range
 |-- WDM  (Wavelength-Division)  analog   - FDM for light in optical fiber
 '-- TDM  (Time-Division)        digital  - share time
       |-- Synchronous TDM
       '-- Statistical TDM
```

### 6.1.2 FDM (Frequency-Division Multiplexing)

- Used when the link's bandwidth (Hz) is bigger than the total of the signals.
- Each sender **modulates its own carrier frequency** (f1, f2, f3, ...). This shifts each
  signal into its own slice of the spectrum. The slices are added and sent together.
- **Guard bands** = thin strips of **unused** frequency between channels so they do not
  overlap.
- At the receiver: **band-pass filters** pick out each slice, then a demodulator shifts it back to 0.
- Everyone transmits all the time, each in its own frequency slice.
- Examples: AM/FM radio, TV (6 MHz per channel), 1G cell phones (AMPS).

```
FDM: 3 channels with 2 guard bands
 |  ch 1  |g|  ch 2  |g|  ch 3  |
 +--------+-+--------+-+--------+---> frequency
 n channels need n - 1 guard bands (only BETWEEN channels)
```

**FDM bandwidth formula:**

```
B_total = n x B_channel + (n - 1) x B_guard
```

### 6.1.3 Analog hierarchy (telephone FDM)

| Level | Made from | Voice channels | Bandwidth |
|---|---|---|---|
| Voice channel | - | 1 | 4 kHz |
| **Group** | 12 voice channels | 12 | **48 kHz** |
| **Supergroup** | 5 groups | 60 | **240 kHz** |
| **Master group** | 10 supergroups | 600 | **2.52 MHz** (2.40 + guard bands) |
| **Jumbo group** | 6 master groups | 3600 | **16.984 MHz** (15.12 + guard bands) |

Memory hook: **12, 5, 10, 6** ("12 voices, 5 groups, 10 supers, 6 masters").

### 6.1.4 WDM (Wavelength-Division Multiplexing)

- **FDM for light.** Used on **fiber-optic cable**.
- Each source sends a different **wavelength (colour)** of light: λ1, λ2, λ3.
- A **prism** combines them at the MUX and splits them at the DEMUX (a prism bends each
  wavelength by a different angle).
- **Application (2015-16 Q4b): SONET** fiber networks; fiber backbone links of telephone
  companies and ISPs.
- **DWDM** (dense WDM): channels packed very close together for even more channels.

```
 λ1 --\                                  /-- λ1
 λ2 ---> prism ==== λ1+λ2+λ3 fiber ==== prism ---> λ2
 λ3 --/                                  \-- λ3
```

### 6.1.5 Synchronous TDM (the big numerical topic)

- **Digital.** Instead of sharing frequency, the users **take turns in time**.
- Each input's stream is cut into **units** (1 bit, 1 character, or 1 block).
- The MUX takes **one unit from each input in turn** (round robin). One round = a **frame**.
- A frame has **n slots** (one per input) + maybe framing bits.
- Every input gets its slot **every frame, even if it has nothing to send**. (That is the
  "synchronous" part, and its weakness.)
- **Interleaving** = picture two rotating switches, one at the MUX and one at the DEMUX,
  turning in sync. As the switch passes an input, that input puts one unit on the link.

```
inputs (each unit lasts T):         output link (each slot lasts T/n)
 A: A3 A2 A1 --\                   Frame 3   Frame 2   Frame 1
 B: B3 B2 B1 ---> MUX ---->   | C3 B3 A3 | C2 B2 A2 | C1 B1 A1 |  --> 
 C: C3 C2 C1 --/                   <-- T --> 
                                   one frame lasts T = one input unit
```

**The key relations (n inputs, each R bps, unit = u bits):**

| Quantity | Formula |
|---|---|
| Input bit duration | 1 / R |
| Input slot duration (unit duration) | u / R |
| **Frame rate** | R / u frames per second (= unit rate of ONE input) |
| **Frame duration** | 1 / frame rate (= input unit duration) |
| Bits per frame | n x u + framing bits |
| **Output (link) bit rate** | frame rate x bits per frame (= n x R if no framing bits) |
| Output bit duration | 1 / output bit rate |
| Output slot duration | input slot duration / n (no framing bits) |
| Efficiency | useful bits / total bits per frame |

Two facts that solve most questions:
1. **Frame duration = duration of one input unit.** (Frame rate = how many units per second ONE input produces.)
2. **Output rate = n x input rate** (+ framing bits x frame rate).

### 6.1.6 Framing bits (synchronization)

- MUX and DEMUX must stay in step. Otherwise a bit for channel 2 ends up in channel 3.
- So we add **framing bits** to each frame, usually **1 bit per frame, alternating 1, 0, 1, 0...**
- They add to the frame size and to the link rate. **Do not forget them in numericals.**

### 6.1.7 Empty slots

Synchronous TDM wastes capacity: if an input is silent, its slot travels **empty**.
That is the motivation for statistical TDM.

### 6.1.8 Statistical TDM (and why it is better)

- Slots are given **only to inputs that have data**. The MUX checks inputs round robin
  and **skips** idle ones.
- Number of slots per frame **is less than** the number of inputs.
- Since a slot no longer belongs to a fixed input, **each slot carries an address** of the
  destination (log2 N bits for N outputs).
- No framing/synchronization bits needed.
- Link capacity is set from **average** traffic, so it is **less than the sum** of input rates.

**Why statistical TDM is better (2015-16 Q5a, 2018-19 Q4e):** no empty slots, so
bandwidth is used efficiently; the link can be slower (cheaper) than the sum of all
inputs, because not all inputs talk at once.

| | Synchronous TDM | Statistical TDM |
|---|---|---|
| Slot ownership | fixed, one per input every frame | dynamic, only to active inputs |
| Empty slots | yes (waste) | no |
| Slots per frame | = n | < n |
| Address in slot | not needed | needed |
| Framing bits | needed | not needed |
| Link capacity | = sum of inputs | < sum of inputs (based on statistics) |

### 6.1.9 Data rate management (inputs with different rates)

Three strategies:

**1. Multilevel multiplexing** - when one rate is a **multiple** of another.
Combine slow lines first, then combine again.

```
 20 kbps --\
            MUX -> 40 kbps --\
 20 kbps --/                  \
 40 kbps ---------------------> MUX -> 160 kbps
 40 kbps ---------------------/
 40 kbps --------------------/
```

**2. Multiple-slot allocation** - give a fast line **more than one slot** per frame.
A small DEMUX splits the fast line into several lines of the base rate.

```
 50 kbps --> [split] --> 25 kbps --\
                     --> 25 kbps ---\
 25 kbps ----------------------------> MUX -> 125 kbps
 25 kbps ----------------------------/        (the 50-kbps line
 25 kbps ---------------------------/          owns 2 of 5 slots)
```

**Multilevel vs multiple-slot (2015-16 Q5b):** multilevel adds **extra MUX stages**
(slow lines are combined first into a faster line). Multiple-slot uses **one MUX** and
gives the faster line **several slots** in each frame. Both need rates that are
integer multiples of each other.

**3. Pulse stuffing** (also called **bit padding** or **bit stuffing**)
(2019-20 Q4c: "what is pulse stuffing?")
- Used when the rates are **not** integer multiples (e.g. 46 kbps and 50 kbps).
- Make the **highest rate the dominant rate** and add **dummy bits** to the slower lines
  until they reach it. Then multiplex normally.

```
 46 kbps --> [pulse stuffing] --> 50 kbps --\
 50 kbps -----------------------------------> MUX -> 150 kbps
 50 kbps ----------------------------------/
```

### 6.1.10 Digital hierarchy: DS service and T lines

DS = Digital Signal service. T lines = the physical lines that carry them.

| Service | Line | Rate | Voice channels | Made from |
|---|---|---|---|---|
| DS-0 | - | 64 kbps | 1 | 1 PCM voice (8000 samples/s x 8 bits) |
| DS-1 | T-1 | 1.544 Mbps | 24 | 24 DS-0 + 8 kbps overhead |
| DS-2 | T-2 | 6.312 Mbps | 96 | 4 DS-1 |
| DS-3 | T-3 | 44.736 Mbps | 672 | 7 DS-2 |
| DS-4 | T-4 | 274.176 Mbps | 4032 | 6 DS-3 |

(The book's text says DS-3 is 44.376 Mbps with 1.368 Mbps overhead; its Table 6.1 says
44.736. Either is accepted. Quote 44.736 Mbps for T-3.)

Memory hook: **24, 4, 7, 6**.

**T-1 frame:**
- 24 channels x 8 bits + **1 framing bit = 193 bits per frame**.
- 8000 frames per second (one PCM sample per voice every 125 µs).
- Rate = 193 x 8000 = **1,544,000 bps = 1.544 Mbps**.
- Frame duration = 1/8000 = **125 µs**. Overhead = 1 bit x 8000 = **8 kbps**.

```
| F | ch1 (8 bits) | ch2 (8 bits) | ... | ch24 (8 bits) |   = 193 bits, 125 µs
```

**E lines** (Europe): E-1 2.048 Mbps (30 voice), E-2 8.448 (120), E-3 34.368 (480), E-4 139.264 (1920).

### 6.1.11 Spread spectrum: the idea

- Multiplexing aims at **efficiency**. Spread spectrum aims at **privacy and anti-jamming**,
  mainly in **wireless** (where anyone can listen to or jam the air).
- It deliberately **spreads** the signal's bandwidth B to a much larger B_ss (B_ss >> B).
  The extra bandwidth is redundancy, a protective "envelope" around the message.
- Two rules: (1) the spread bandwidth is far larger than needed; (2) the spreading uses a
  **spreading code** that is independent of the data (looks random, but is a known pattern).

### 6.1.12 FHSS (Frequency Hopping Spread Spectrum)

- Uses **M different carrier frequencies**. In each **hopping period** Th, the signal
  modulates **one** carrier; in the next period it **hops** to another one.
- A **pseudorandom code generator (PN)** produces a **k-bit pattern** every hop. A
  **frequency table** maps the pattern to a carrier. A **frequency synthesizer** generates
  that carrier, and the modulator puts the data on it.
- M = 2^k frequencies. Book example: k = 3, M = 8, frequencies 200-900 kHz;
  pattern 101, 111, 001, 000, 010, 011, 100 ... -> 700 kHz, 900 kHz, 300 kHz, ...
- **How it spreads bandwidth:** at any instant it uses only B, but over a full cycle it
  visits all M carriers, so it occupies B_FHSS = about M x B.
- **Privacy:** an eavesdropper without the hop sequence catches only small pieces.
- **Anti-jamming:** a jammer can ruin one hop period, not the whole message.
- **Sharing:** M stations can share the same B_ss, each on a different frequency in every hop.

```
FHSS block diagram (draw this for "describe FHSS"):

 PN code generator --k bits--> frequency table --> frequency synthesizer
                                                          |
                                                       carrier
                                                          v
 original signal ----------------------------------> modulator --> spread signal

Hopping picture (frequency vs time):
 900 |    #
 800 |
 700 | #
 ... |
 300 |       #
 200 |          #
     +--1--2--3--4--5--6--7--8--> hop periods  (pattern repeats each cycle)
```

### 6.1.13 FDM vs FHSS (2014-15 Q2a)

**Similarity:** both split the total bandwidth into M sub-bands; each station uses 1/M of
the bandwidth at a time, and M stations can share it.

**Difference:**

| FDM | FHSS |
|---|---|
| each station's frequency is **fixed** | the frequency **changes every hop** |
| goal: efficiency | goal: privacy and anti-jamming |
| no spreading code | pseudorandom code decides the hops |
| a jammer on your band blocks you all the time | a jammer hits only some hops |

### 6.1.14 DSSS (Direct Sequence Spread Spectrum)

- **Name (2014-15 Q1b-iv): Direct Sequence Spread Spectrum.** It is called "direct
  sequence" because **each data bit is directly replaced by a sequence of n bits**
  (called **chips**) from a spreading code. This spreads the spectrum.
- Chip rate = n x bit rate, so the bandwidth grows n times.
- Example: Wi-Fi uses the **Barker sequence**, n = 11, pattern 10110111000.
  Original rate N -> spread rate 11N -> bandwidth 11 times larger.
- Done by multiplying (polar NRZ) the data by the chip sequence: data bit 1 sends the
  code, data bit 0 sends the code inverted.

```
data:      |     1      |     0      |
code:      |10110111000 |10110111000 |
spread:    |10110111000 |01001000111 |    (0 -> inverted code)
```

**FHSS vs DSSS (2019-20 Q1f):** FHSS spreads by **hopping between carrier frequencies**
over time; DSSS spreads by **replacing each bit with an n-chip code** (one carrier, higher
chip rate).

---

## 6.2 Formula box - Ch6

| Formula | Symbols | When to use |
|---|---|---|
| B = n x Bc + (n - 1) x Bg | n channels, Bc channel bandwidth, Bg guard band | FDM total bandwidth |
| Bc = (B - (n-1)Bg) / n | | FDM: how wide can each channel be |
| frame rate = R / u | R input rate (bps), u bits per slot per input | synchronous TDM |
| frame duration = 1 / frame rate = u / R | | synchronous TDM |
| bits per frame = n u + f | f framing bits per frame | synchronous TDM |
| link rate = frame rate x bits per frame | | synchronous TDM |
| link rate = n R (no framing bits) | | quick check |
| output bit duration = 1 / link rate | | "output bit duration" |
| efficiency = n u / (n u + f) | | P6-4e |
| stat TDM slot = data + address, address = log2(N) bits | N outputs | statistical TDM |
| T-1: 193 bits x 8000 = 1.544 Mbps | 24 x 8 + 1 | T-1 questions |
| overhead = line rate - (channels x 64 kbps) | | DS overhead (P6-14) |
| M = 2^k, k = ceil(log2(B_ss / B)) | M hopping frequencies, k PN bits | FHSS |
| PN cycle time = M x k / (PN bit rate) | | FHSS (P6-16) |
| B_ss = n x B (chip rate = n x bit rate) | n chips per bit | DSSS |

---

## 6.3 Worked past-paper solutions - Ch6

### PP6-1 (TT2 2025 Q6a-d) - FDM with and without guard bands (= Forouzan P6-1 with n = 3)

*(a) A voice channel occupies 4 kHz. Multiplex 3 voice channels with guard bands of 500 Hz
using FDM. Required bandwidth? (b) Draw it if the medium starts at 1 kHz. (c) Same with no
guard bands. (d) Draw (c) starting at 1 kHz.*

**(a)** n = 3 channels -> n - 1 = **2** guard bands.
B = 3 x 4 kHz + 2 x 0.5 kHz = 12 + 1 = **13 kHz**.

**(b)** Start at 1 kHz and stack: channel, guard, channel, guard, channel.
- Ch 1: 1 to 5 kHz
- Guard: 5 to 5.5 kHz
- Ch 2: 5.5 to 9.5 kHz
- Guard: 9.5 to 10 kHz
- Ch 3: 10 to 14 kHz
- Total: 1 to 14 kHz = 13 kHz. ✓

```
   |  Ch 1   |g|  Ch 2   |g|  Ch 3   |
   1         5 5.5     9.5 10        14   kHz
   |<----------- 13 kHz ------------->|
```

**(c)** No guard bands: B = 3 x 4 = **12 kHz**.

**(d)**
- Ch 1: 1 to 5 kHz, Ch 2: 5 to 9 kHz, Ch 3: 9 to 13 kHz.

```
   |  Ch 1   |  Ch 2   |  Ch 3   |
   1         5         9         13   kHz
   |<--------- 12 kHz ---------->|
```

(The paper's 6.d says "draw the bandwidth for 6.b", which is clearly meant to be 6.c, the
no-guard case. Write that assumption.)

Textbook versions: Forouzan Ex 6.1 (three 4-kHz channels in 20-32 kHz, no guard bands:
20-24, 24-28, 28-32 kHz) and Forouzan P6-1 (10 channels, 500 Hz guards:
10 x 4 + 9 x 0.5 = **44.5 kHz**).

### PP6-2 (2018-19 Q2f) = Forouzan Ex 6.2
*Five channels of 100 kHz, guard band 10 kHz between channels. Minimum link bandwidth?*

5 channels -> 4 guard bands.
B = 5 x 100 + 4 x 10 = 500 + 40 = **540 kHz**.

```
| 100 |g| 100 |g| 100 |g| 100 |g| 100 |    g = 10 kHz
|<---------------- 540 kHz --------------->|
```

### PP6-3 (2019-20 Q3a) = Forouzan Ex 6.6
*Four 1-Mbps input lines are multiplexed in a synchronous TDM. The unit of data is 1 bit.
Find (i) input bit duration (ii) output bit duration (iii) output bit rate (iv) output frame rate.*

n = 4, R = 1 Mbps, u = 1 bit, no framing bits.

1. Input bit duration = 1 / R = 1 / 10^6 = **1 µs**.
2. Output bit duration = input / n = 1 µs / 4 = **0.25 µs (250 ns)**.
3. Output bit rate = 1 / 0.25 µs = **4 Mbps** (check: n x R = 4 x 1 Mbps ✓).
4. Output frame rate = rate of one input in units = **1,000,000 frames/s**
   (check: 4 Mbps / 4 bits per frame = 10^6 ✓).

### PP6-4 (TT-01 Q3) - same with 10 Mbps
*Four 10-Mbps lines, synchronous TDM, unit 1 bit. Find output bit duration, output bit rate,
output frame rate.*

1. Input bit duration = 1 / 10^7 = 0.1 µs = 100 ns.
2. Output bit duration = 100 ns / 4 = **25 ns**.
3. Output bit rate = 4 x 10 Mbps = **40 Mbps** (= 1 / 25 ns ✓).
4. Output frame rate = **10,000,000 frames/s** (= 40 Mbps / 4 bits ✓).

### PP6-5 (2015-16 Q6b) = Forouzan P6-9 - pulse stuffing
*What is pulse-stuffed TDM? Two channels, 190 kbps and 180 kbps, multiplexed with
pulse-stuffing TDM, no synchronization bits. (i) frame size (ii) frame rate (iii) frame
duration (iv) data rate.*

Definition: see 6.1.9 point 3 (make the highest rate dominant; pad slower lines with dummy bits).

1. Stuff the 180-kbps channel up to 190 kbps (add 10 kbps of dummy bits).
2. Now both are 190 kbps. Take 1 bit from each per frame.
3. (i) Frame size = 1 + 1 = **2 bits**.
4. (ii) Frame rate = 190,000 bits/s / 1 bit per frame = **190,000 frames/s**.
5. (iii) Frame duration = 1 / 190,000 = **5.26 µs**.
6. (iv) Data rate = 190,000 x 2 = **380 kbps**.

### PP6-6 (2016-17 Q6c(ii)) = Forouzan P6-12 - TDM output stream
*Synchronous TDM. Each output slot (frame) is 10 bits: 3 bits from each input + 1 framing
bit. Inputs (bits arrive as shown by the arrows, so the **rightmost bit arrives first**):*

```
Input 1: 101110111101   -->
Input 2: 11111110000    -->
Input 3: 1010000001111  -->
```

Method:
1. Cut each input into groups of 3 **starting from the right** (that end arrives first).
2. Frame k = framing bit + group k of input 1 + group k of input 2 + group k of input 3.
3. Framing bits alternate 1, 0, 1, 0 (book convention).

Groups (as written in the figure, first-arriving group first):

| Frame | Framing bit | Input 1 | Input 2 | Input 3 |
|---|---|---|---|---|
| 1 | 1 | 101 | 000 | 111 |
| 2 | 0 | 111 | 110 | 001 |
| 3 | 1 | 110 | 111 | 000 |
| 4 | 0 | 101 | 11 (only 2 bits left) | 010 |

Input 1 has 12 bits (exactly 4 groups). Input 2 has 11 bits, so its 4th group is
incomplete. Input 3 has 13 bits, one bit "1" is left for frame 5. So **3 complete
frames** can be built from the bits shown; frame 4 waits for more input-2 bits.

Output stream, written the same way as the inputs (rightmost bit leaves first, so frame 1
is on the right, and inside each frame the framing bit goes out first):

```
   frame 3        frame 2        frame 1
 000 111 110 1 | 001 110 111 0 | 111 000 101 1   -->
 (in3 in2 in1 F)
```

i.e. **...0001111101 0011101110 1110001011 -->**

Write your convention in one line ("rightmost bit sent first; frame = F, in1, in2, in3").
Any consistent convention earns the marks.

### PP6-7 (2015-16 Q5a, 2018-19 Q4e) - TDM, statistical better
- TDM: digital multiplexing; several low-rate channels share one high-rate link by
  **taking turns in time**; each gets a time slot in every frame.
- Statistical TDM is better: slots only go to inputs that have data, so **no empty
  slots**, better bandwidth use, and the link can be slower than the sum of all inputs.
  (Cost: each slot needs an address.) Use the comparison table in 6.1.8.

### PP6-8 (2015-16 Q5b, 2016-17 Q4h) - multilevel vs multiple-slot, multiple-slot figure
Write 6.1.9 parts 1 and 2 with both figures. For "multiple-slot with figure" draw the
50 / 25 / 25 / 25 kbps -> 125 kbps picture: the 50-kbps line is split into two 25-kbps
lines, so it owns **2 slots in every frame** of 5 slots.

### PP6-9 (2014-15 Q4f, 2015-16 Q4i, 2018-19 Q4b) - multiplexing
See 6.1.1. One-line answer: "Multiplexing lets several signals share one link at the same
time; it is needed because a link's bandwidth is usually much larger than one user needs,
and sharing it avoids wasting bandwidth and laying many links."

### PP6-10 (2015-16 Q4b) - WDM application
**SONET / fiber-optic backbone networks** (many optical signals of different wavelengths
on one fiber).

### PP6-11 (2014-15 Q2a, 2015-16 Q6a) - FHSS, and FDM vs FHSS
Write 6.1.12 (definition, block diagram, 8-frequency example, how it spreads:
"at any moment it uses bandwidth B, but over one cycle it uses all M carriers, so the
occupied bandwidth is about M x B >> B") and the 6.1.13 table.

### PP6-12 (2014-15 Q1b-iv) - DSSS name
**Direct Sequence Spread Spectrum.** "Direct sequence" because each data bit is
**directly replaced by a sequence of chips** (spreading code, e.g. 11-chip Barker
sequence), which spreads the bandwidth n times.

### PP6-13 (2019-20 Q1f) - FHSS vs DSSS
FHSS **changes the carrier frequency** in each hop period. DSSS keeps one carrier and
**replaces each bit by an n-chip code**.

### PP6-14 (2019-20 Q4c) - pulse stuffing
"When input rates are not integer multiples of each other, the highest rate is taken as
the dominant rate and dummy bits are added to the slower inputs to raise them to it.
Also called bit padding or bit stuffing." Example: 46 kbps stuffed to 50 kbps.

---

## 6.4 Textbook worked examples (not yet asked; same style)

**Forouzan Ex 6.5.** Figure with 3 inputs of 1 kbps, unit 1 bit.
Input slot = 1/1000 s = **1 ms**. Output slot = 1/3 ms. Frame = 3 x 1/3 = **1 ms**.

**Forouzan Ex 6.7.** Four 1-kbps connections, unit 1 bit.
(1) bit duration before MUX = **1 ms**; (2) link rate = 4 x 1 = **4 kbps**;
(3) time slot = 1/4 ms = **250 µs**; (4) frame = **1 ms**.

**Forouzan Ex 6.8.** Four channels, each 100 bytes/s, 1 byte per channel per frame.
Frame = 4 bytes = **32 bits**. Frame rate = **100 frames/s**. Frame duration = **1/100 s = 10 ms**.
Link rate = 100 x 32 = **3200 bps** (= 4 x 800 bps ✓).

**Forouzan Ex 6.9.** Four 100-kbps channels, slot = 2 bits.
Frame rate = 100,000 / 2 = **50,000 frames/s**. Frame duration = **20 µs**.
Frame = 4 x 2 = 8 bits. Link rate = 50,000 x 8 = **400 kbps**. Bit duration = **2.5 µs**.

**Forouzan Ex 6.10 (framing bit - the classic trap).** Four sources, 250 characters/s each,
unit = 1 character (8 bits), 1 sync bit per frame.
1. Source rate = 250 x 8 = **2 kbps**.
2. Character duration = 1/250 s = **4 ms**.
3. Frame rate = **250 frames/s** (one character per source per frame).
4. Frame duration = **4 ms**.
5. Bits per frame = 4 x 8 + 1 = **33 bits**.
6. Link rate = 250 x 33 = **8250 bps** (not 8000: the extra 250 bps is the sync bits).

**Forouzan Ex 6.11 (multiple-slot).** 100 kbps and 200 kbps. Give 1 slot to the first, 2
to the second. Frame = 3 bits. Frame rate = **100,000 frames/s**. Frame duration =
1/100,000 s = **10 µs** (the book prints "10 ms", a typo). Link = **300 kbps**.

**Forouzan Ex 6.3 (FDM of digital data).** Four 1-Mbps channels on a 1-MHz satellite
channel. Each gets 250 kHz. Need 1 Mbps in 250 kHz = 4 bits per Hz, so use **16-QAM**
(r = 4, d = 0).

**Forouzan Ex 6.4 (AMPS).** Each band 849 - 824 = 25 MHz. 25 MHz / 30 kHz = 833.33, in
practice **832 channels**; 42 are for control, so **790 users** at once.

**Forouzan P6-10 (T-1).** Frame duration = 1/8000 = **125 µs**. Overhead = 8000 framing bits/s = **8 kbps**.

**Forouzan P6-14 (DS overhead).** DS-1: 1.544 M - 24 x 64 k = **8 kbps**.
DS-2: 6.312 M - 96 x 64 k = **168 kbps**. DS-3: 44.376 M - 672 x 64 k = **1.368 Mbps**.
DS-4: 274.176 M - 4032 x 64 k = **16.128 Mbps**.

**Forouzan P6-3 (analog hierarchy overhead).** Group: 48 - 12 x 4 = **0**.
Supergroup: 240 - 5 x 48 = **0**. Master: 2520 - 10 x 240 = **120 kHz**.
Jumbo: 16.984 - 6 x 2.52 = **1.864 MHz**.

**Forouzan P6-18 (DSSS).** 10-Mbps medium, Barker (11 chips per bit).
Usable data rate = 10 / 11 = 0.909 Mbps. Channels = 909 kbps / 64 kbps = 14.2 -> **14 channels**.

---

## 6.5 Traps - Ch6

1. **Guard bands = n - 1**, not n. They go only between channels.
2. **Framing bits:** add them to the frame size AND to the link rate (Ex 6.10: 8250, not 8000).
3. **Frame rate is not the link bit rate.** Frame rate = units per second of ONE input.
4. If the slot is 2 bits (or 1 byte), the frame rate drops: frame rate = R / u.
5. **Frame duration = one input unit duration**, not one output bit duration.
6. Character = 8 bits unless told otherwise. Convert characters/s to bps (x 8).
7. Output bit duration = input bit duration / n **only with no framing bits**.
8. µs vs ms: 1 / 190,000 s = 5.26 µs, not ms. (Forouzan Ex 6.11 itself has this typo.)
9. Statistical TDM slots carry an **address**; they need **no** framing bits.
10. Statistical TDM: slots per frame **less than** number of inputs.
11. TDM output stream: the bit **nearest the MUX (rightmost)** arrives first. State your convention.
12. FDM and WDM are **analog**; TDM is **digital**.
13. CDMA is not a multiplexing method in Forouzan 5e (it is an access method, Ch12).
14. T-1 = 24 x 8 + **1** = 193 bits, not 192.
15. Spread spectrum makes bandwidth **larger** on purpose (privacy, anti-jamming). Multiplexing is about **efficiency**. Do not mix them up.

---

## 6.6 Practice set - Ch6 (answers at the bottom)

**C6-1.** (Forouzan P6-1) Multiplex 10 voice channels of 4 kHz with 500 Hz guard bands.
Required bandwidth?

**C6-2.** A 1 MHz link carries 8 FDM channels with 20 kHz guard bands between them. What is
the widest each channel can be?

**C6-3.** (Forouzan P6-4) Synchronous TDM of 20 sources, 100 kbps each. Each frame has 1 bit
from each source + 1 sync bit. Find (a) frame size (b) frame rate (c) frame duration
(d) output data rate (e) efficiency.

**C6-4.** (Forouzan P6-5) Repeat C6-3 if each slot carries 2 bits from each source.

**C6-5.** (Forouzan P6-7) Ten sources: six at 200 kbps, four at 400 kbps. Multilevel TDM, no
sync bits. For the final stage find frame size, frame rate, frame duration, data rate.

**C6-6.** (Forouzan P6-8) Four channels: two at 200 kbps, two at 150 kbps. Multiple-slot TDM,
no sync bits. Find frame size, frame rate, frame duration, data rate.

**C6-7.** (Forouzan P6-6) 14 sources, each 500 characters/s (8 bits). Statistical TDM,
character interleaving, 6 slots per frame, 4-bit address per slot. Find frame size, frame
rate, frame duration, data rate.

**C6-8.** (Forouzan P6-11) Synchronous TDM, 4 sources, unit = 1 character. Source 1: HELLO,
source 2: HI, source 3: silent, source 4: BYE. Show the 5 output frames.

**C6-9.** (Forouzan P6-15) FHSS with B = 4 kHz and B_ss = 100 kHz. Minimum number of bits in
the PN sequence?

**C6-10.** (Forouzan P6-16) An FHSS system uses a 4-bit PN sequence at 64 bits/s.
(a) number of channels (b) time for one full PN cycle.

---

## 6.7 DOOMSDAY BOX - Ch6 (15 minutes)

```
+--------------------------------------------------------------------+
| FDM: B = n·Bc + (n-1)·Bg           (guard bands = n - 1)           |
| Synchronous TDM (n inputs, R bps each, u bits/slot, f framing bits)|
|   frame rate = R/u     frame duration = u/R                        |
|   bits/frame = n·u + f link rate = frame rate x bits/frame (= nR)  |
|   output bit duration = 1/link rate                                |
| Statistical TDM: slots only for active inputs, slot has address,   |
|   no sync bits, link < sum of inputs.  => better (no empty slots)  |
| Different rates: multilevel (extra MUX stages), multiple-slot      |
|   (more slots per frame), pulse stuffing (dummy bits up to max)    |
| T-1 = 24x8+1 = 193 bits x 8000 = 1.544 Mbps, 125 µs/frame          |
| DS: 24, 4, 7, 6   Analog: 12 (48k), 5 (240k), 10 (2.52M), 6 (16.984M)|
| WDM = FDM for light, prism, fiber, SONET                           |
| FHSS: hop among M = 2^k carriers chosen by PN code                 |
| DSSS: each bit -> n chips (Barker n = 11), bandwidth x n           |
| SS goal = privacy + anti-jamming;  MUX goal = efficiency           |
+--------------------------------------------------------------------+
```

---

## BONUS - CDMA (Ch12 in 5e, but asked in 2014-15 Q2b and 2016-17 Q2f)

**CDMA (Code Division Multiple Access):** all stations send **at the same time on the same
frequency**. Each station has its own **chip code**. The codes are **orthogonal**
(dot product of two different codes = 0), so the receiver can separate them.
Map bit 1 -> +1, bit 0 -> -1, silent -> 0.

**Walsh table for 4 stations (2016-17 Q2f).** Build W2N from WN:
W1 = [+1]; W2N = [[WN, WN], [WN, -WN]].

```
W1 = [+1]

W2 = | +1 +1 |
     | +1 -1 |

W4 = | +1 +1 +1 +1 |   station 1 chips
     | +1 -1 +1 -1 |   station 2
     | +1 +1 -1 -1 |   station 3
     | +1 -1 -1 +1 |   station 4
```

**2014-15 Q2b:** user data 011 and 100, codes 0000 and 1010.
Codes in ±1: c1 = 0000 -> (-1,-1,-1,-1); c2 = 1010 -> (+1,-1,+1,-1).
Check orthogonal: c1·c2 = -1 + 1 - 1 + 1 = 0 ✓.
Station 1 sends 0,1,1 -> -1,+1,+1. Station 2 sends 1,0,0 -> +1,-1,-1.

| Bit | d1 | d2 | channel = d1·c1 + d2·c2 | decode 1: (ch·c1)/4 | decode 2: (ch·c2)/4 |
|---|---|---|---|---|---|
| 1 | -1 | +1 | (2, 0, 2, 0) | -4/4 = -1 -> **0** | 4/4 = +1 -> **1** |
| 2 | +1 | -1 | (-2, 0, -2, 0) | +1 -> **1** | -1 -> **0** |
| 3 | +1 | -1 | (-2, 0, -2, 0) | +1 -> **1** | -1 -> **0** |

Receiver recovers **011** for station 1 and **100** for station 2. ✓

---

# Answers

### Ch5

**C5-1.** 16-QAM: r = 4. N = 1000 x 4 = **4000 bps**.

**C5-2.** (a) ASK: S = 4000, B = 2 x 4000 = **8 kHz**. (b) FSK: B = 2 x 4000 + 4000 = **12 kHz**.
(c) QPSK: S = 2000, B = 2 x 2000 = **4 kHz**. (d) 16-QAM: S = 1000, B = **2 kHz**.

**C5-3.** S = B = 4000 baud. (a) ASK r = 1: **4 kbps**. (b) QPSK r = 2: **8 kbps**.
(c) 16-QAM r = 4: **16 kbps**. (d) 64-QAM r = 6: **24 kbps**.

**C5-4.** (a) AM: 2 x 5 = **10 kHz**. (b) FM: 2(1 + 5) x 5 = **60 kHz**. (c) PM: 2(1 + 1) x 5 = **20 kHz**.

**C5-5.** fc = **250 kHz**. S = 100 / (1 + 1) = **50 kbaud**. QPSK r = 2: N = **100 kbps**.

**C5-6.** (a) ASK: (1, 0) and (3, 0), both on the +I axis.
(b) QPSK peak 3: each coordinate = 3/√2 = 2.12. Dots at **(2.12, 2.12), (-2.12, 2.12),
(-2.12, -2.12), (2.12, -2.12)** (phases 45°, 135°, 225°, 315°).

**C5-7.** Two rings of 4 dots at the same 4 phases (45°, 135°, 225°, 315°) -> **8-QAM**,
r = log2 8 = **3 bits**. Amplitudes: sqrt(1+1) = **1.41** and sqrt(9+9) = **4.24**.

**C5-8.** L = 2^3 = **8**. S = 6 / 3 = **2 Mbaud**. B = 8 x 2 = **16 MHz** (12 to 28 MHz).
Carriers 2 MHz apart, centred on 20 MHz: 13, 15, 17, 19, 21, 23, 25, 27 MHz.
Lowest **13 MHz**, highest **27 MHz**.

**C5-9.** **AM**, because noise adds to amplitude and AM carries the information in the amplitude.
FM and PM keep the amplitude constant.

**C5-10.** S = 36,000 / 6 = **6000 baud**. L = 2^6 = **64** signal elements.

### Ch6

**C6-1.** 10 x 4 + 9 x 0.5 = **44.5 kHz**.

**C6-2.** 7 guard bands x 20 = 140 kHz. (1000 - 140) / 8 = **107.5 kHz** per channel.

**C6-3.** (a) 20 x 1 + 1 = **21 bits**. (b) **100,000 frames/s**. (c) **10 µs**.
(d) 21 x 100,000 = **2.1 Mbps**. (e) 20/21 = **95.2 %**.

**C6-4.** (a) 20 x 2 + 1 = **41 bits**. (b) 100,000 / 2 = **50,000 frames/s**. (c) **20 µs**.
(d) 41 x 50,000 = **2.05 Mbps**. (e) 40/41 = **97.6 %**.

**C6-5.** First level: pair the six 200-kbps lines into three 400-kbps lines. Final stage:
3 + 4 = 7 inputs of 400 kbps. Frame = **7 bits**. Frame rate = **400,000 frames/s**.
Duration = **2.5 µs**. Data rate = 7 x 400,000 = **2.8 Mbps**.

**C6-6.** Base unit = 50 kbps (common factor). 200-kbps lines get 4 slots each, 150-kbps
lines get 3 slots each. Frame = 4 + 4 + 3 + 3 = **14 bits**. Frame rate = **50,000 frames/s**.
Duration = **20 µs**. Data rate = 14 x 50,000 = **700 kbps** (= 200+200+150+150 ✓).

**C6-7.** Slot = 8 + 4 = 12 bits. Frame = 6 x 12 = **72 bits**. Frame rate = **500 frames/s**.
Duration = **2 ms**. Data rate = 72 x 500 = **36 kbps**.

**C6-8.** (empty slot shown as _)
Frame 1: H H _ B
Frame 2: E I _ Y
Frame 3: L _ _ E
Frame 4: L _ _ _
Frame 5: O _ _ _
(Synchronous TDM sends the empty slots too: that is the waste.)

**C6-9.** B_ss / B = 100 / 4 = 25 frequencies needed. 2^4 = 16 < 25 <= 32 = 2^5, so
**k = 5 bits**.

**C6-10.** (a) 2^4 = **16 channels**. (b) One cycle = 16 hops x 4 bits = 64 bits;
64 bits / 64 bps = **1 s**.
