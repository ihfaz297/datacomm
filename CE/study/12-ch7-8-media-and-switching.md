# Ch 7 Transmission Media + Ch 8 Switching (Forouzan 5e)

Tutorial-level notes for the mid-term. Every numerical below was recomputed in Python.
Past-paper questions come first. Year tags = session on the paper (e.g. "2016-17").

Sources checked: `CE/Questions/Previous Year Questions/` (2014-15, 2015-16, 2016-17, 2018-19, 2019-20),
`CE/Questions/Term Test/` (TT-01, DataCom_TT2), `CE/Questions/tt2/` (TT2 2025: no ch7/ch8 questions).
Textbook text: `CE/ch7_media.txt`, `CE/ch8_switching.txt` (extracted from the 5e PDF, pages 185-234).

---

# PART 1: CHAPTER 7, TRANSMISSION MEDIA

## 7.0 What they ask

| Year | Question | Type |
|---|---|---|
| 2014-15 Q1b(i) | Give an example for twisted-pair, coaxial and fiber-optic cable | Theory, 1 mark |
| 2014-15 Q1b(vii) | What is attenuation? How can we overcome it? | Theory |
| 2014-15 Q4c | Power reduced to one-fourth. Define the attenuation | dB numerical |
| TT-01 1a | Power reduced to one-half. What is the attenuation? | dB numerical |
| TT-01 4a, 4b | Define refraction and reflection. Name the major classes of guided media | Theory, 5 marks |
| 2015-16 Q2d | What is attenuation? Attenuation is -10 dB, original power 20 W, final power? | dB numerical |
| 2015-16 Q4d | Frequency range of VHF? | Table recall |
| 2015-16 Q4f | Two disadvantages of fiber-optic cable | Theory |
| 2016-17 Q1e | How does guided media differ from unguided media? | Differentiate |
| 2016-17 Q1f | Why do optical signals in fiber have a very short wavelength? | Theory |
| 2016-17 Q2b(ii) | 100 W at A, 90 W at B. Attenuation in dB? | dB numerical |
| 2016-17 Q4c | Define attenuation and distortion | Theory |
| 2016-17 Q4d | Advantages of optical fiber over twisted-pair and coax | Theory (= Forouzan Q7-8) |
| 2016-17 Q4g | Purpose of cladding in an optical fiber | Theory (= Forouzan Q7-7) |
| 2018-19 Q5e | Cable is -0.3 dB/km, 2 mW at start. Power at 10 km? | dB numerical |
| 2019-20 Q1g | Propagation method for radio waves? | Theory |
| 2019-20 Q4a | Difference between STP and UTP | Differentiate |

Pattern: ch7 is almost all 1-2 mark theory, plus one dB numerical nearly every year.
Many questions are copied straight from Forouzan's end-of-chapter list (Q7-1 to Q7-10).

---

## 7.1 Concepts in plain English

### What is a transmission medium?
Anything that carries a signal from sender to receiver: a cable or the air.
It sits **below** the physical layer. Forouzan jokingly calls it "layer zero".

```
 Sender                                   Receiver
 [Physical layer] ---- cable or air ---- [Physical layer]
                    (transmission medium)
```

### Two big classes

```
                 Transmission media
                /                  \
        Guided (wired)          Unguided (wireless)
       /      |       \          /       |        \
 Twisted   Coaxial   Fiber    Radio   Microwave  Infrared
  pair      cable    optic    wave
```

- **Guided** = the signal is kept inside a physical path (a "conduit"). Copper cables carry electric current. Fiber carries light.
- **Unguided** = the signal travels as electromagnetic waves through free space (air, vacuum, water). Anyone with a receiver can pick it up.

### Guided vs unguided (2016-17 Q1e)

| | Guided | Unguided |
|---|---|---|
| Path | Physical conductor (cable) | Free space, no conductor |
| Signal form | Electric current (copper) or light (fiber) | Electromagnetic waves |
| Who can receive | Only devices on the cable | Anyone with an antenna (broadcast) |
| Examples | Twisted pair, coax, fiber | Radio, microwave, infrared |
| Other name | Wired | Wireless |

### Twisted-pair cable
Two copper wires, each with plastic insulation, twisted around each other.
One wire carries the signal, the other is a ground reference. The receiver looks at the **difference** between them.

**Why twist?** Noise hits both wires. If the wires were parallel, one wire would always be closer to the noise source, so the noise would be unequal and would not cancel. Twisting swaps which wire is closer on every twist. Both wires get the same noise, the difference cancels it out. More twists per inch = better cable.

**UTP vs STP (2019-20 Q4a)**

| | UTP (Unshielded Twisted Pair) | STP (Shielded Twisted Pair) |
|---|---|---|
| Shield | None | Metal foil or braided mesh around each pair |
| Noise / crosstalk protection | Lower | Better |
| Cost, bulk | Cheap, thin, flexible | Expensive, bulkier |
| Use | Most common: phones, LANs | Mainly IBM installations |

"Crosstalk" = one wire's signal leaking into a neighbouring wire.

**UTP categories (Table 7.1).** Rated 1 (worst) to 7 (best) by EIA.

| Cat | Data rate | Use |
|---|---|---|
| 1 | < 0.1 Mbps | Telephone |
| 2 | 2 Mbps | T-1 lines |
| 3 | 10 Mbps | LANs |
| 4 | 20 Mbps | Token Ring LANs |
| 5 | 100 Mbps | LANs |
| 5E | 125 Mbps | LANs (less crosstalk) |
| 6 | 200 Mbps | LANs |
| 7 | 600 Mbps | LANs (SSTP, each pair shielded) |

Connector: **RJ45** (keyed, fits only one way).
Performance: attenuation (in dB/km) rises sharply above 100 kHz. "Gauge" = wire thickness (bigger gauge number = thinner wire).
Applications: telephone local loop, DSL, 10Base-T and 100Base-T Ethernet LANs.

### Coaxial cable
```
  [ plastic cover [ outer conductor (shield) [ insulator [ inner core ] ] ] ]
```
- Central copper core, then insulator, then an outer metal foil/braid, then a plastic cover.
- The outer conductor does two jobs: shield against noise **and** second conductor of the circuit.
- Carries higher frequencies than twisted pair. But attenuation is much higher, so it needs repeaters more often.
- Rated by **RG** (Radio Government) numbers:

| RG | Impedance | Use |
|---|---|---|
| RG-59 | 75 ohm | Cable TV |
| RG-58 | 50 ohm | Thin Ethernet (10Base2, 185 m) |
| RG-11 | 50 ohm | Thick Ethernet (10Base5, 500 m) |

- Connectors: **BNC** connector, BNC T connector, BNC terminator (stops signal reflection at the cable end).
- Applications: analog telephone networks (10,000 voice signals per cable), cable TV, traditional Ethernet.

### Examples of each cable (2014-15 Q1b(i))
- **Twisted pair:** telephone line (local loop), DSL, Ethernet LAN cable (10Base-T / 100Base-T, Cat 5 with RJ45).
- **Coaxial:** cable TV line (RG-59), thin Ethernet 10Base2 (RG-58).
- **Fiber optic:** Internet backbone / SONET, 100Base-FX Fast Ethernet, cable TV backbone (hybrid fiber-coax).

### Fiber-optic cable: the physics first
Fiber carries **light** through glass or plastic.
Light goes straight in one uniform material. When it crosses into a material of different density, it bends.

Terms:
- **Angle of incidence (I):** angle between the ray and the line **perpendicular** (the "normal") to the boundary.
- **Critical angle:** a special angle that depends on the two materials.
- **Refraction:** the ray passes into the second material and bends (changes direction).
- **Reflection:** the ray bounces back into the first material.

Light going from **more dense** to **less dense** material:

```
 I < critical angle       I = critical angle         I > critical angle
   REFRACTION               bends ALONG surface        REFLECTION
 less dense  /            less dense                  less dense
 ----------*-----         ----------*__________       ----------*-------
 more dense /              more dense /                more dense / \
           /                         /                           /   \
```

**Define refraction and reflection (TT-01 4a, Forouzan Q7-6):**
- Refraction: when light passes from one medium into another of different density, it changes direction. Happens when I < critical angle.
- Reflection: when I > critical angle, the light does not enter the second medium. It turns back into the first (denser) medium.

### How a fiber uses this
```
   ======================== cladding (less dense) ========================
   sender  \  /\  /\  /\  /\  /\  /\  /\  /\  /   core (more dense)  receiver
            \/  \/  \/  \/  \/  \/  \/  \/  \/
   ======================== cladding (less dense) ========================
```
- **Core** = the inner glass/plastic that carries the light (denser).
- **Cladding** = a less dense glass/plastic layer around the core.
- **Purpose of cladding (2016-17 Q4g):** because cladding is less dense than the core, light hitting the core-cladding boundary at more than the critical angle is **reflected back into the core** instead of escaping. The cladding keeps the light trapped inside the core so it travels the whole length of the fiber.

### Propagation modes

```
               Mode
             /      \
      Multimode    Single mode
      /       \
 Step-index  Graded-index
```

"Mode" = a path the light beams can take. "Index" = index of refraction, which tracks density.

```
a) Multimode STEP-index     (constant core density, sharp bounces, beams take
   ===================       different path lengths -> arrive at different times)
   \/\/\/\/\/   /\  /\       => most distortion
   ---------- (straight)
   ===================

b) Multimode GRADED-index   (density highest at centre, falls gradually to edge;
   ===================       beams curve smoothly back to centre)
   ~~~~~~~~~~ (smooth waves) => less distortion
   ===================

c) SINGLE mode              (very thin core, focused source, beams almost horizontal)
   ===================
   ----------------- (all beams nearly straight, arrive together)
   ===================       => least distortion, longest distance
```

| | Multimode step-index | Multimode graded-index | Single mode |
|---|---|---|---|
| Core density | Constant, sudden drop at cladding | Highest at centre, gradually decreases | Constant (step), much lower density |
| Core diameter | Large | Large (50, 62.5, 100 um) | Very small (7 um) |
| Beam paths | Many, zig-zag | Many, curved | Almost one, near horizontal |
| Distortion | Highest | Medium | Least |
| Why | Different paths = different arrival times | Curving evens out path delays | Critical angle near 90 deg, all beams same path |

Fiber sizes are written core/cladding in micrometres: 50/125, 62.5/125, 100/125 (multimode graded), 7/125 (single mode).

Cable layers (outside in): outer jacket (PVC/Teflon) -> Kevlar strands (strength) -> plastic buffer -> cladding -> core.
Connectors: **SC** (subscriber channel, cable TV, push/pull), **ST** (straight tip, networking, bayonet), **MT-RJ** (same size as RJ45).

### Fiber advantages (2016-17 Q4d, Forouzan Q7-8)
1. **Higher bandwidth** -> much higher data rate. Limited by the electronics, not the fiber.
2. **Less attenuation** -> 50 km without regeneration vs repeaters every 5 km for copper. Needs about one-tenth as many repeaters.
3. **Immune to electromagnetic interference** (light is not affected by electrical noise).
4. **Resists corrosive materials** (glass vs copper).
5. **Light weight.**
6. **Hard to tap** (copper acts like an antenna and leaks signal; fiber does not).

### Fiber disadvantages (2015-16 Q4f)
1. **Installation and maintenance** need expertise not available everywhere.
2. **Unidirectional** light propagation: two-way communication needs **two fibers**.
3. **Cost:** cable and interfaces are more expensive than other guided media.

### Why is the wavelength so short in fiber? (2016-17 Q1f)
Wavelength = speed / frequency. Light is a very high-frequency wave (about 10^14 Hz, e.g. 1300 nm light in vacuum is 3x10^8 / 1300x10^-9 = 2.3x10^14 Hz).
Huge frequency means tiny wavelength (hundreds of nanometres).
Why we want that: a very high carrier frequency gives a huge usable bandwidth (data rate), and glass has its lowest loss in the 800-1600 nm range (Figure 7.16), so the light travels far with little attenuation.

### Unguided media: how waves travel

```
 GROUND propagation        SKY propagation              LINE-OF-SIGHT
 (below 2 MHz)             (2-30 MHz)                   (above 30 MHz)
                          ~~~~ ionosphere ~~~~
   tx ~~~~~~~~~~ rx         tx   /\   rx                 tx --------> rx
   hugs earth's curve           bounces off ionosphere    straight line,
   ( earth )                  ( earth )                  antennas face each other
```

- **Ground:** low-frequency waves hug the earth, spread in all directions. More power = more distance.
- **Sky:** higher-frequency waves go up to the **ionosphere** (layer of charged particles) and reflect back down. Long distance with low power.
- **Line-of-sight:** very high frequency, straight from antenna to antenna. Antennas must be tall or close because of the earth's curve.

### Bands (Table 7.4). Know at least VHF and the propagation column.

| Band | Range | Propagation | Application |
|---|---|---|---|
| VLF | 3-30 kHz | Ground | Long-range radio navigation |
| LF | 30-300 kHz | Ground | Radio beacons, navigational locators |
| MF | 300 kHz-3 MHz | Sky | AM radio |
| HF | 3-30 MHz | Sky | Citizens band (CB), ship/aircraft |
| **VHF** | **30-300 MHz** | Sky and line-of-sight | VHF TV, FM radio |
| UHF | 300 MHz-3 GHz | Line-of-sight | UHF TV, cell phones, paging, satellite |
| SHF | 3-30 GHz | Line-of-sight | Satellite |
| EHF | 30-300 GHz | Line-of-sight | Radar, satellite |

Memory trick: each band is 10x the previous one, starting at 3 kHz. VLF, LF, MF, HF, VHF, UHF, SHF, EHF.

### Radio waves vs microwaves vs infrared

| | Radio waves | Microwaves | Infrared |
|---|---|---|---|
| Frequency | 3 kHz - 1 GHz | 1 - 300 GHz | 300 GHz - 400 THz |
| Direction | **Omnidirectional** (all directions) | **Unidirectional** (focused beam) | Line of sight, short range |
| Antenna | Omnidirectional | Parabolic dish, horn | IrDA port |
| Through walls? | Yes (low/medium freq) | No (very high freq) | No |
| Band width available | Narrow (< 1 GHz) -> low data rate | Wide (~299 GHz) -> high data rate | Very wide (~400 THz) |
| Use | **Multicast**: AM/FM radio, TV, paging, cordless phones | **Unicast**: cell phones, satellite, wireless LAN | Remote control, keyboard/mouse to PC |
| Problem | Interference from other antennas on same band | Towers must see each other, need repeaters | Sunlight interferes, so indoor only |

- **Omnidirectional** = sends in all directions, antennas do not need to be aligned.
- **Unidirectional** = sends in one narrow direction, antennas must be aligned.
- **Radio wave propagation method (2019-20 Q1g):** radio waves are omnidirectional and travel by **ground propagation** (low frequencies, VLF/LF) and **sky propagation** (MF/HF, reflected off the ionosphere), which is why they travel long distances and suit broadcasting like AM radio. At VHF and above they become line-of-sight.

### Attenuation and distortion (2014-15 Q1b(vii), 2016-17 Q4c)
This is ch3 material in 5e, but it shows up with media questions every year.
- **Attenuation** = loss of signal energy (power) as it travels through a medium. Part of the energy turns into heat in the resistance of the wire.
  **How to overcome it:** use **amplifiers** (analog) or **repeaters/regenerators** (digital) along the path to boost the signal. Or switch to a medium with lower loss (fiber).
- **Distortion** = the signal changes its **shape**. A composite signal has many frequency components, each travels at a slightly different speed, so they arrive out of step (phase shift) and the shape gets smeared.
- (Third impairment, for "name three impairments": **noise**, unwanted energy added to the signal: thermal, induced, crosstalk, impulse.)

---

## 7.2 Formula box (Ch 7)

| Formula | Symbols | When to use |
|---|---|---|
| dB = 10 log10(P2 / P1) | P1 = power at start, P2 = power at end | Any attenuation/gain question |
| P2 = P1 x 10^(dB/10) | Same, rearranged | "Find the final power" |
| Loss (dB) = (dB per km) x distance | e.g. -0.3 dB/km x 10 km | Cable rated in dB/km |
| Total dB = dB1 + dB2 + dB3 ... | Each stage's gain/loss | Cascaded stages (decibels add) |
| dBm = 10 log10(P in mW) | Power relative to 1 mW | "What is dBm?" |
| f = v / lambda | v = speed in the medium, lambda = wavelength | Convert fiber wavelength to frequency |
| Bandwidth of light = v/lambda_low - v/lambda_high | Shorter wavelength = higher frequency | Forouzan P7-7 |
| Propagation time = distance / speed | speed in fiber ~ 2x10^8 m/s | Forouzan P7-10 |

Negative dB = loss (attenuation). Positive dB = gain (amplification).
Quick values: half power = -3 dB. Quarter power = -6 dB. One-tenth = -10 dB. Double = +3 dB. Ten times = +10 dB.

---

## 7.3 Past-paper solutions (Ch 7)

### TT-01 1a. Power reduced to one-half. Attenuation? (2 marks) (= Forouzan Ex 3.26)
1. P2 = 0.5 P1.
2. dB = 10 log10(P2/P1) = 10 log10(0.5) = 10 x (-0.301) = -3.01.
3. **Attenuation = -3 dB (a 3 dB loss). Losing half the power = -3 dB.**

### 2014-15 Q4c. Power reduced to one-fourth. Define the attenuation.
1. Attenuation means loss of power as the signal travels.
2. P2 = P1/4. dB = 10 log10(0.25) = 10 x (-0.602) = -6.02.
3. **Attenuation = -6 dB (6 dB loss).** (Each halving is -3 dB, two halvings = -6 dB.)

### 2015-16 Q2d. Attenuation -10 dB, original 20 W. Final power? (1+3)
1. Define: attenuation = loss of energy of a signal while travelling through a medium.
2. -10 = 10 log10(P2 / 20)
3. log10(P2 / 20) = -1
4. P2 / 20 = 10^-1 = 0.1
5. **P2 = 20 x 0.1 = 2 W.**

### 2016-17 Q2b(ii). 100 W at A, 90 W at B. Attenuation in dB? (2 marks)
1. dB = 10 log10(90 / 100) = 10 log10(0.9)
2. log10(0.9) = -0.0458
3. **dB = -0.458, about -0.46 dB** (a loss of 0.46 dB).

### 2018-19 Q5e. Cable -0.3 dB/km, 2 mW at start. Power at 10 km? (= Forouzan Ex 3.30 with 10 km instead of 5 km)
1. Total loss = -0.3 x 10 = -3 dB.
2. -3 = 10 log10(P2 / 2 mW)
3. P2 / 2 = 10^-0.3 = 0.501
4. **P2 = 1.00 mW** (about 1 mW: -3 dB halves the power, makes sense).

(Textbook version, Ex 3.30, 5 km: loss = -1.5 dB, P2 = 2 x 10^-0.15 = 1.42 mW.)

### 2014-15 Q1b(vii). What is attenuation? How can we overcome it?
Attenuation is the loss of energy of a signal as it travels through a medium (it overcomes the medium's resistance, energy turns to heat). **Overcome it with amplifiers (or repeaters) placed along the line to boost the signal**, or use a lower-loss medium such as fiber.

### TT-01 4b. Major classes of guided media
**Twisted-pair cable, coaxial cable, fiber-optic cable.**

### 2015-16 Q4d. Frequency range of VHF?
**30 MHz to 300 MHz** (sky and line-of-sight propagation; VHF TV, FM radio).

### Other ch7 theory past questions, short answers
- 2016-17 Q1e guided vs unguided: see the table in 7.1.
- 2016-17 Q1f short wavelength: see "Why is the wavelength so short".
- 2016-17 Q4d fiber advantages, 2015-16 Q4f disadvantages, 2016-17 Q4g cladding: see 7.1.
- 2019-20 Q4a STP vs UTP: STP has a metal foil/braided-mesh shield around each pair, so less noise and crosstalk but bulkier and more expensive. UTP has no shield, cheap, most common.
- 2019-20 Q1g radio wave propagation: ground and sky propagation (omnidirectional).

### Textbook problems not covered by past papers

**Forouzan P7-10.** Light in fiber, v = 2x10^8 m/s. Delay for 10 m, 100 m, 1 km?
- t = d / v. 10 / 2x10^8 = **50 ns**. 100 m -> **0.5 us**. 1000 m -> **5 us**.

**Forouzan P7-11.** Critical angle 60 deg, light going to less dense medium. Incident angles 40, 60, 80 deg?
- 40 deg < 60: **refraction** (bends away into the less dense medium).
- 60 deg = critical: **bends along the interface**.
- 80 deg > 60: **reflection** back into the denser medium.

**Forouzan P7-7.** Bandwidth of light, v = 2x10^8 m/s.
- (a) 1000-1200 nm: f(1000) = 2x10^8 / 1000x10^-9 = 2.0x10^14 Hz. f(1200) = 1.667x10^14 Hz. **BW = 3.33x10^13 Hz = 33.3 THz.**
- (b) 1000-1400 nm: f(1400) = 1.4286x10^14 Hz. **BW = 5.71x10^13 Hz = 57.1 THz.**

**Forouzan Ex 3.28 (cascading).** Decibels just add: -3 + 7 - 3 = **+1 dB**. (Signal gained power overall.)

**Forouzan Ex 3.29.** dBm = -30 -> 10 log10(Pm) = -30 -> **Pm = 10^-3 mW**.

---

## 7.4 Traps (Ch 7)

1. **Angle of incidence is measured from the normal (the perpendicular line), not from the surface.** Bigger angle = more "grazing" = reflection.
2. Light must go from **more dense to less dense** for total reflection. That is why the cladding is **less** dense than the core. Swap them and the fiber leaks.
3. **Single mode uses step-index fiber**, not graded. Graded-index is a kind of **multimode**.
4. Attenuation in dB is **negative**. If you write "+3 dB" for a loss, you lose the mark. Say "-3 dB" or "a loss of 3 dB".
5. dB uses **10 log** for power. (20 log is for voltage; not used in Forouzan ch3 questions on power.)
6. dB per km times distance first, **then** convert. Do not convert per km and multiply powers by distance.
7. Coax has **higher bandwidth** than twisted pair **but higher attenuation** (Figure 7.9). Both are true; do not mix them up.
8. Radio waves = **omnidirectional = multicast**. Microwaves = **unidirectional = unicast**. Easy to swap.
9. Radio waves are 3 kHz - 1 GHz, microwaves 1 - 300 GHz. Forouzan says behaviour matters more than the exact frequency cut-off.
10. Fiber is **unidirectional**: two-way needs two fibers. A favourite "disadvantage".
11. Infrared fails outdoors because **sunlight contains infrared**, not because of distance alone.

---

## 7.5 Practice set (Ch 7). Answers at the very bottom.

**P7.1** A 5 mW signal enters a cable rated -0.2 dB/km. What is the power after 10 km?
**P7.2** Power at the start of a link is 50 mW and at the end is 5 mW. Attenuation in dB?
**P7.3** A 2 mW signal goes through: a cable (-4 dB), an amplifier (+10 dB), another cable (-3 dB). Final power?
**P7.4** Critical angle is 45 deg (dense to less dense). What happens at incident angles 30, 45, 70 deg?
**P7.5** Name the propagation method and one application of (a) MF, (b) UHF.
**P7.6** Differentiate single-mode and multimode graded-index fiber (3 points).
**P7.7** Why are the wires in a twisted-pair cable twisted?
**P7.8** Why can infrared not be used for outdoor communication?
**P7.9** Compare radio waves and microwaves (antenna type, direction, one use each).
**P7.10** A 1 km fiber carries light at 2x10^8 m/s. How long does a pulse take to cross it?

---

## 7.6 Doomsday box (Ch 7): 15 minutes

```
GUIDED: twisted pair, coax, fiber.   UNGUIDED: radio, microwave, infrared.
TWIST -> noise hits both wires equally -> cancels at receiver.
UTP no shield (cheap, common) | STP metal foil shield (less noise, costly, IBM).
COAX: core + insulator + outer conductor (shield AND 2nd conductor). RG-59 TV, RG-58 thin Ethernet.
FIBER: core (dense) + cladding (less dense). I > critical angle -> REFLECTION -> light stays in core.
  modes: multimode step (most distortion) / multimode graded (less) / single mode (least, thinnest).
  +: bandwidth, low attenuation (50 km vs 5 km), no EMI, no corrosion, light, hard to tap.
  -: installation skill, unidirectional (needs 2 fibers), cost.
PROPAGATION: ground <2 MHz | sky 2-30 MHz (ionosphere) | line-of-sight >30 MHz.
VHF = 30-300 MHz (FM, VHF TV).  Bands x10 each from 3 kHz: VLF LF MF HF VHF UHF SHF EHF.
RADIO omni -> multicast (AM/FM, TV). MICROWAVE uni -> unicast (cell, satellite, WLAN). IR short range indoors.
dB = 10 log10(P2/P1).  P2 = P1 x 10^(dB/10).  1/2 -> -3 dB, 1/4 -> -6 dB, 1/10 -> -10 dB.
```

---

# PART 2: CHAPTER 8, SWITCHING

## 8.0 What they ask

| Year | Question | Type |
|---|---|---|
| 2015-16 Q4a | What is the total delay in a datagram network? | Formula recall |
| 2015-16 Q4g | What is VCI? | Definition |
| 2015-16 Q4h | For n inputs and n outputs, a banyan switch has ___ stages with ___ microswitches per stage | Fill-in |
| 2015-16 Q5c | Design a three-stage 100 x 100 switch (N = 100) with k = 4 and n = 10 (4 marks) | Crosspoint numerical |
| 2015-16 Q6c | What is a virtual-circuit network? Explain its phases (6 marks) | Theory |
| 2016-17 Q3b | Three-stage, N = 100, 10 crossbars first/third stage, 4 middle. Diagram, crosspoints, simultaneous connections, single-crossbar connections, blocking factor (10 marks) | Crosspoint numerical (= Forouzan P8-12) |
| 2019-20 Q2f | Same switch as 2016-17 Q3b: diagram + total crosspoints | Crosspoint numerical |

Pattern: **the three-stage switch with N = 100 has appeared three times** (2015-16, 2016-17, 2019-20). Learn it cold. Then virtual-circuit phases, VCI, and the delay formulas.

---

## 8.1 Concepts in plain English

### Why switching?
Connecting every device to every other device (mesh) needs too many links, and most sit idle. A **switch** is a device that makes **temporary** connections between devices attached to it. A **switched network** = a set of interlinked switches. End systems (computers, phones) hang off some switches.

### Three methods

```
                 Switching
          /          |           \
  Circuit         Packet         Message
 switching       switching      switching (phased out,
                 /       \        e-mail is the idea)
      Virtual-circuit   Datagram
```

Which layer does what:
- **Physical layer:** only circuit switching (no packets exist there).
- **Data-link layer:** packet switching, usually **virtual-circuit**.
- **Network layer:** packet switching, virtual-circuit or **datagram** (the Internet uses datagram).
- **Application layer:** message switching.

### Circuit switching
A **dedicated path** between two stations is reserved before any data flows. Each link is split into n channels using FDM (frequency slices) or TDM (time slots). The connection uses one channel on each link.

Key points:
- Takes place at the **physical layer**.
- Resources (channels, buffers, switch ports, processing time) are **reserved during setup and stay dedicated until teardown**.
- Data is **not packetized**. It is a continuous flow.
- **No addressing during data transfer.** Switches route by FDM band or TDM slot. End-to-end addresses (e.g. phone numbers) are used only in setup.

**Three phases:**
1. **Setup:** A sends a setup request with M's address to switch I. Each switch reserves a channel on the next link and forwards the request. Destination M sends an **acknowledgment** back. Only when A gets the ack is the connection made.
2. **Data transfer:** data flows over the reserved channels.
3. **Teardown:** one side sends a signal to each switch to release the resources.

**Efficiency:** low. Resources are held for the whole connection even when nobody is talking.
**Delay:** minimal during data transfer. No waiting at switches.

### Packet switching
The message is cut into **packets**. **No resource reservation**: bandwidth and processing are given on demand, first-come first-served. So a packet may have to **wait** at a switch.

### Datagram network (connectionless)
- Each packet (called a **datagram**) is treated **independently**, even packets of the same message.
- Packets of one message may take **different paths**, arrive **out of order**, with **different delays**, or be **dropped**. Upper layers reorder and recover.
- **No setup or teardown phase.** The switch keeps no state about connections, so it is called **connectionless**.
- Switches are called **routers**. Each has a **routing table** keyed on the **destination address**. Table entries are dynamic, updated periodically, and **do not depend on current connections**.
- Every packet carries the **destination address** in its header, and it stays the **same for the whole journey**.
- Efficiency: better than circuit switching (resources freed whenever there is no packet).
- Delay: can be more than VC because each packet may wait at each switch.

Routing table (Fig 8.8), minimum two columns:
```
  Destination address | Output port
  1232                | 1
  4150                | 2
  9130                | 3
```

### Virtual-circuit (VC) network: a cross of the two
1. Like circuit switching: **setup, data transfer, teardown** phases.
2. Resources reserved in setup (like circuit) **or** on demand (like datagram).
3. Like datagram: data is **packetized** and each packet carries an address. But the address is **local** (it only tells the next switch what to do), not end-to-end.
4. Like circuit switching: **all packets follow the same path** set up during setup.
5. Normally at the **data-link layer** (circuit = physical, datagram = network).

**Two kinds of address:**
- **Global address:** unique in the network. Used **only during setup and teardown** to build the table entries.
- **VCI (Virtual-Circuit Identifier), also called a label (2015-16 Q4g):** a **small number with switch scope**, used **during data transfer** between two switches. A frame arrives with one VCI and leaves with a **different** VCI. It does not need to be big because each switch can reuse its own set.

```
   --[ 14 | Data ]-->  ( switch )  --[ 77 | Data ]-->
       VCI in                          VCI out (changed)
```

**Switching table** (minimum four columns):
```
        Incoming        |       Outgoing
   Port  |  VCI         |  Port  |  VCI
    1    |  14          |   3    |  22
    1    |  77          |   2    |  41
```
A frame arriving on port 1 with VCI 14 leaves on port 3 with VCI 22.

**Three phases in detail (2015-16 Q6c).** Example: A -> switch 1 -> switch 2 -> switch 3 -> B.

**(a) Setup phase, step 1: setup request** (goes A to B)
```
 A --setup--> SW1 --setup--> SW2 --setup--> SW3 --setup--> B
             fills:         fills:         fills:          picks
             in port 1      in port 1      in port 2       VCI 77
             in VCI 14      in VCI 66      in VCI 22       for frames
             out port 3     out port 2     out port 3      from A
             out VCI = ?    out VCI = ?    out VCI = ?
```
Each switch fills **three of four columns** (incoming port, incoming VCI it chooses, outgoing port). It cannot know the outgoing VCI yet.

**(a) Setup phase, step 2: acknowledgment** (goes B back to A)
```
 A <--ack(14)-- SW1 <--ack(66)-- SW2 <--ack(22)-- SW3 <--ack(77)-- B
 A uses 14     out VCI=66       out VCI=22       out VCI=77
 as its VCI
```
Each switch passes back the incoming VCI it chose. The previous switch writes that as its **outgoing VCI**. Now every table is complete. The ack carries the global source and destination addresses so each switch knows which entry to complete.

**(b) Data-transfer phase:** A sends frames with VCI 14. SW1 changes it to 66, SW2 to 22, SW3 to 77, B receives with 77. Same path for every frame.
```
 A --[14|D]--> SW1 --[66|D]--> SW2 --[22|D]--> SW3 --[77|D]--> B
```

**(c) Teardown phase:** A sends a **teardown request**. B replies with a **teardown confirmation**. All switches **delete** the entry.

**Advantage even with on-demand resources:** the source can **check** whether resources are available before sending (like phoning a restaurant to ask the wait time).

### Comparison table: circuit vs datagram vs virtual circuit (the big "differentiate" question)

| Feature | Circuit-switched | Datagram | Virtual-circuit |
|---|---|---|---|
| Layer | Physical | Network | Data-link |
| Setup/teardown phases | Yes | **No** | Yes |
| Resource reservation | Yes, for whole session | No, on demand | In setup **or** on demand |
| Data unit | Continuous stream (not packetized) | Packets (datagrams) | Packets/frames/cells |
| Path | Fixed, dedicated | Each packet may differ | Fixed, all packets same path |
| Packet order | In order | May arrive out of order | In order |
| Address during data transfer | None | Full destination address (end-to-end) | Local VCI |
| Address during setup/teardown | End-to-end | (no setup) | End-to-end (global) |
| Table at switch | None needed (FDM band / TDM slot) | Routing table: dest addr -> port (2 cols min) | Switching table: in port, in VCI -> out port, out VCI (4 cols min) |
| Table entries change when | n/a | Network topology changes | Each connection set up / torn down |
| Efficiency | Low | High | Medium |
| Delay | Low, fixed after setup | Variable, waiting at each switch | Setup + teardown once, then low |
| Connection-oriented? | Yes | No (connectionless) | Yes |

### Delay timing diagrams

Time runs down. Slanted lines = propagation (tau). Box height = transmission time (T). Example path: A -> switch -> switch -> B (two switches, three links).

**Circuit-switched (Fig 8.6)**
```
   A           S1          S2          B
   |\ setup req                         |
   | \--------------------------------\ |
   |                                   \|
   |            ack       /-------------|
   | /-------------------/              |
   |/                                   |
   |#\  DATA (long block, no waits)     |
   |##\--------------------------------\|
   |###\                                #|
   |    \------------------------------\#|
   |                 disconnect          |
   v time                                v
 Total = setup (request + ack) + propagation + data transmission + teardown
```

**Datagram (Fig 8.9)**
```
   A           S1          S2          B
   |#\          |           |           |
   |  \-------->|# wait w1  |           |
   |            | #\        |           |
   |            |   \------>|# wait w2  |
   |            |           | #\        |
   |            |           |   \------>|#
   v            v           v           v
 Total = 3T + 3tau + w1 + w2      (# = transmission T, slant = tau)
```

**Virtual-circuit (Fig 8.16)**
```
   A           S1          S2          B
   |== setup (request out, ack back) ===|
   |#\          |           |           |
   |  \-------->|#\         |           |   no waiting if resources
   |            |  \------->|#\         |   were reserved in setup
   |            |           |  \------->|#
   |== teardown (one direction) ========|
 Total = 3T + 3tau + setup delay + teardown delay
```

General rule for a path with s switches (s+1 links), ignoring processing time:
- Datagram: (s+1)T + (s+1)tau + sum of waiting times.
- VC: (s+1)T + (s+1)tau + setup + teardown.

### Structure of circuit switches

Two technologies: **space-division** and **time-division**.

#### Space-division: paths are physically separate.

**Crossbar switch:** n inputs and m outputs on a grid. A **crosspoint** (electronic microswitch, a transistor) sits at every intersection.
```
          out I   out II  out III  out IV
 in 1 -----o-------o-------o--------o----
 in 2 -----o-------o-------o--------o----
 in 3 -----o-------o-------o--------o----
         (o = crosspoint; 3 x 4 = 12 crosspoints)
```
- Crosspoints = **n x m**. 1000 x 1000 needs **1,000,000**: impractical.
- Inefficient: fewer than 25% of crosspoints are in use at any time.
- **Never blocks** (every input-output pair has its own crosspoint).

**Multistage switch (usually three stages):** share crosspoints so the total drops.

Design recipe (N inputs, N outputs):
1. Split N inputs into groups of n. Stage 1: **N/n crossbars, each n x k**.
2. Stage 2: **k crossbars, each (N/n) x (N/n)**.
3. Stage 3: **N/n crossbars, each k x n**.

Total crosspoints = **2kN + k(N/n)^2**.

```
 Stage 1 (N/n boxes)     Stage 2 (k boxes)       Stage 3 (N/n boxes)
  n in  +-------+         +-----------+          +-------+ n out
 ======>| n x k |=k=====> | N/n x N/n |=====k===>| k x n |======>
        +-------+   \   / +-----------+  \   /   +-------+
  n in  +-------+    \ /  +-----------+   \ /    +-------+ n out
 ======>| n x k |=====X==>| N/n x N/n |====X====>| k x n |======>
        +-------+    / \  +-----------+   / \    +-------+
   ...              each stage-1 box sends ONE line to EACH middle box
```

**Blocking:** an input cannot reach a free output because all middle paths are busy. Each first-stage crossbar has only k outputs, so only k of its n inputs can be connected at once. Fewer middle crossbars = more blocking. More stages = fewer crosspoints but more blocking.

**Clos criteria (non-blocking with minimum crosspoints):**
- **n = sqrt(N/2)**
- **k >= 2n - 1**
- Total crosspoints >= **4N[sqrt(2N) - 1]**, proportional to N^(3/2).
- Example: 100,000 lines need about 200 million crosspoints with Clos, vs 10 billion with one crossbar.

#### Time-division: TSI
**TSI (Time-Slot Interchange):** uses TDM inside the switch. Parts: a TDM multiplexer, a **RAM** with one location per input (each location = one time slot), a **control unit**, and a TDM demultiplexer.
- RAM is **written sequentially** (slots stored in arrival order).
- RAM is **read selectively** (control unit picks the order to send out).

Example (Fig 8.19), pattern 1->3, 2->4, 3->1, 4->2:
```
 inputs 1..4 send A,B,C,D
 [TDM] -> frame: A B C D -> [RAM: 1=A 2=B 3=C 4=D] -> read order 3,4,1,2
       -> frame out: C D A B -> [TDM demux] -> out1=C, out2=D, out3=A, out4=B
```
So output 3 gets A (from input 1). Correct.

#### Space vs time division

| | Space-division (crossbar/multistage) | Time-division (TSI) |
|---|---|---|
| How paths are separated | Physically (different wires/crosspoints) | In time (different slots) |
| Advantage | Instantaneous, no delay | **No crosspoints** needed |
| Disadvantage | Huge number of crosspoints for low blocking | Delay: every slot is stored in RAM then read out |

**TST (Time-Space-Time) switch:** combines both. Stage 1 = several TSIs, stage 2 = a crossbar (space), stage 3 = TSIs (mirror of stage 1). Fig 8.20: 12 inputs split into 3 groups of 4, three TSIs, so average delay is **one-third** of one big 12-input TSI. Optimised both in crosspoints and in delay.

### Structure of packet switches (short)
Four parts: **input ports, output ports, routing processor, switching fabric**.
- Input port: physical + data-link work (rebuild bits, decapsulate frame, check errors), then queue.
- Output port: same in reverse (queue, encapsulate, physical signal).
- Routing processor: network-layer table lookup (destination -> output port).
- Switching fabric: moves the packet from input queue to output queue. Types: crossbar, **banyan**, Batcher-banyan.

**Banyan switch (2015-16 Q4h):** multistage switch of 2x2 **microswitches** routing on the binary output-port number, one bit per stage (first stage = high-order bit).
**For n inputs and n outputs: log2(n) stages with n/2 microswitches at each stage.** 8x8 -> 3 stages, 4 microswitches each.
Problem: internal collisions even for different outputs. Fix: **Batcher-banyan** (Batcher switch sorts packets by destination first; a **trap** module stops two packets for the same output from entering together).

---

## 8.2 Formula box (Ch 8)

| Formula | Symbols | When to use |
|---|---|---|
| Crossbar crosspoints = n x m | n inputs, m outputs | Single-stage switch (N x N = N^2) |
| Stage 1: N/n crossbars of n x k | N = total lines, n = lines per group, k = middle crossbars | Three-stage design |
| Stage 2: k crossbars of (N/n) x (N/n) | | Three-stage design |
| Stage 3: N/n crossbars of k x n | | Three-stage design |
| Total = 2kN + k(N/n)^2 | | Three-stage crosspoint count |
| Max simultaneous connections = (N/n) x k | Each stage-1 box passes at most k | Blocking questions (if k < n) |
| Blocking factor = multistage connections / single-crossbar connections | Single crossbar allows N | Forouzan P8-12(e) |
| Clos: n = sqrt(N/2), k >= 2n - 1 | | Non-blocking design |
| Clos minimum crosspoints >= 4N[sqrt(2N) - 1] | | Quick check of Clos design |
| Banyan: log2(n) stages, n/2 microswitches per stage | n x n switch | Packet switch fabric |
| Datagram delay = 3T + 3tau + w1 + w2 | T = transmission time = L/R, tau = propagation = d/v, w = waiting | 2 switches, 3 links |
| VC delay = 3T + 3tau + setup + teardown | | 2 switches, 3 links |
| Circuit delay = setup + (tau + data/R) + teardown | | Circuit-switched |
| T = packet size / bit rate, tau = distance / speed | | Building blocks |

---

## 8.3 Past-paper solutions (Ch 8)

### 2015-16 Q5c. Design a three-stage 100 x 100 switch (N = 100), k = 4, n = 10. (4 marks)

Step 1. Stage 1: N/n = 100/10 = **10 crossbars, each n x k = 10 x 4** (40 crosspoints each).
Crosspoints = 10 x 40 = 400.

Step 2. Stage 2: **k = 4 crossbars, each (N/n) x (N/n) = 10 x 10** (100 each).
Crosspoints = 4 x 100 = 400.

Step 3. Stage 3: **10 crossbars, each k x n = 4 x 10** (40 each).
Crosspoints = 10 x 40 = 400.

Step 4. Total = 400 + 400 + 400 = **1200 crosspoints**.
Check with formula: 2kN + k(N/n)^2 = 2(4)(100) + 4(10)^2 = 800 + 400 = 1200. Matches.

Step 5. Compare: single 100 x 100 crossbar = 10,000. **1200 is 12% of a single-stage switch.**
(Note: k = 4 < 2n - 1 = 19, so this switch is **blocking**.)

### 2016-17 Q3b (10 marks) and 2019-20 Q2f. N = 100, 10 crossbars at first and third stages, 4 at the middle. (= Forouzan P8-12)

First, find n and k.
- 10 crossbars in stage 1 = N/n, so n = 100/10 = **10**.
- 4 crossbars in the middle, so **k = 4**.
It is the same switch as 2015-16 Q5c.

**(i) Configuration diagram**
```
       Stage 1              Stage 2               Stage 3
   10 crossbars 10x4    4 crossbars 10x10     10 crossbars 4x10

 in 1-10   [10x4] #1 ---\                 /--- [4x10] #1   out 1-10
 in 11-20  [10x4] #2 ----\--- [10x10] A --/---- [4x10] #2   out 11-20
 in 21-30  [10x4] #3 -----\-- [10x10] B -/----- [4x10] #3   out 21-30
    ...        ...    (mesh) [10x10] C  (mesh)      ...         ...
 in 91-100 [10x4] #10 -------- [10x10] D -------- [4x10] #10 out 91-100

 Wiring rule: each stage-1 crossbar has 4 outputs, one to EACH of A, B, C, D.
              each middle crossbar has 10 inputs (one from each stage-1 box)
              and 10 outputs (one to each stage-3 box).
              each stage-3 crossbar has 4 inputs, one from EACH of A, B, C, D.
```
In the exam, draw 10 small boxes on the left, 4 tall boxes in the middle, 10 small boxes on the right. Draw a line from every left box to every middle box, and from every middle box to every right box. Label sizes.

**(ii) Total crosspoints**
- Stage 1: 10 x (10 x 4) = 400
- Stage 2: 4 x (10 x 10) = 400
- Stage 3: 10 x (4 x 10) = 400
- **Total = 1200 crosspoints.**

**(iii) Possible number of simultaneous connections**
Each stage-1 crossbar has 10 inputs but only 4 outputs. So at most 4 of its 10 users can be connected at once.
10 crossbars x 4 = **40 simultaneous connections**.

**(iv) Simultaneous connections with one 100 x 100 crossbar**
Every input has its own crosspoint to every output. All 100 inputs can be connected at once: **100 simultaneous connections**.

**(v) Blocking factor**
Blocking factor = (iii) / (iv) = 40 / 100 = **0.4 (40%)**.
Meaning: the three-stage switch can only serve 40% of users at the same time. It saves crosspoints (1200 vs 10,000) at the cost of blocking.

### 2015-16 Q4a. Total delay in a datagram network?
For a packet through two switches (Fig 8.9): **Total delay = 3T + 3tau + w1 + w2**,
where T = transmission time, tau = propagation time on each link, w1, w2 = waiting times at the two switches (processing time ignored).

### 2015-16 Q4g. What is VCI?
**VCI (Virtual-Circuit Identifier) is a small number with switch scope, used in a virtual-circuit network to identify a frame between two switches during data transfer. It changes at every switch: a frame comes in with one VCI and goes out with another, looked up in the switch's table (incoming port, VCI -> outgoing port, VCI).** Also called a label.

### 2015-16 Q4h. Banyan switch, n inputs and n outputs
**log2(n) stages with n/2 microswitches at each stage.**

### 2015-16 Q6c. What is a virtual-circuit network? Explain its phases. (6 marks)
Write in this order (see 8.1 for the diagrams):
1. **Definition:** a packet-switched network that is a cross between circuit switching and datagram. It has setup, data transfer and teardown phases like circuit switching, but data is sent in packets that carry a local address (VCI), and all packets follow the same path. Usually implemented at the data-link layer (e.g. ATM, Frame Relay).
2. **Addressing:** global address (used in setup/teardown) and VCI (used in data transfer, switch scope, changes at every hop).
3. **Setup phase:**
   - Setup request: travels A -> B. Each switch makes a table entry and fills incoming port, incoming VCI, outgoing port. Destination picks its VCI (e.g. 77).
   - Acknowledgment: travels B -> A. Each switch receives the next hop's incoming VCI and writes it as its outgoing VCI. Source learns its VCI (e.g. 14).
4. **Data-transfer phase:** each switch looks up (in port, in VCI), swaps the VCI, forwards on the out port. Draw: 14 -> 66 -> 22 -> 77.
5. **Teardown phase:** A sends teardown request, B sends teardown confirmation, all switches delete the entry.
6. (Bonus line) Delay = 3T + 3tau + setup delay + teardown delay for two switches.

### Textbook examples and problems (not directly in past papers)

**Forouzan Ex 8.3.** Three-stage 200 x 200, k = 4, n = 20.
- Stage 1: 200/20 = 10 crossbars of 20 x 4 -> 10 x 80 = 800.
- Stage 2: 4 crossbars of 10 x 10 -> 400.
- Stage 3: 10 crossbars of 4 x 20 -> 800.
- **Total = 2000 crosspoints**, 5% of 200 x 200 = 40,000. Only 4 of each 20 inputs can be used at a time (blocking).

**Forouzan Ex 8.4.** Redesign the 200 x 200 switch with Clos.
- n = sqrt(200/2) = sqrt(100) = **10**. k = 2n - 1 = **19**.
- Stage 1: 200/10 = 20 crossbars of 10 x 19 -> 20 x 190 = 3800.
- Stage 2: 19 crossbars of **(N/n) x (N/n) = 20 x 20** -> 19 x 400 = 7600.
- Stage 3: 20 crossbars of 19 x 10 -> 3800.
- **Total = 15,200 crosspoints** (38% of 40,000). Check: 4N[sqrt(2N) - 1] = 800 x (20 - 1) = 15,200. Matches.
- **Warning:** the textbook prints the middle stage as "10 x 10" and the total as 9500. That is a misprint: with 20 first-stage crossbars, each middle crossbar must have 20 inputs. Use 15,200 and show the formula check. If the examiner insists on the book's figure, the method still earns the marks.

**Forouzan P8-13.** Same as P8-12 but 6 middle crossbars (n = 10, k = 6).
- Crosspoints = 10(10 x 6) + 6(10 x 10) + 10(6 x 10) = 600 + 600 + 600 = **1800**.
- Simultaneous connections = 10 x 6 = **60**. Single crossbar = 100. **Blocking factor = 0.6.**

**Forouzan P8-14.** Redesign N = 100 with Clos.
- n = sqrt(100/2) = 7.07. n must divide 100, so try the nearest divisors, 5 and 10.
- n = 5, k = 9: stage 1 = 20 crossbars of 5 x 9 (900), stage 2 = 9 crossbars of 20 x 20 (3600), stage 3 = 20 of 9 x 5 (900). **Total = 5400.**
- n = 10, k = 19: 1900 + 1900 + 1900 = 5700.
- Choose **n = 5, k = 9, 5400 crosspoints** (fewer). Lower bound 4N[sqrt(2N) - 1] = 400 x 13.14 = 5257, and 5400 is just above it. Non-blocking.

**Forouzan P8-15.** 1000 inputs/outputs.
- (a) Single crossbar: **1000 x 1000 = 1,000,000**.
- (b) Clos: n = sqrt(500) = 22.4. Bound = 4(1000)[sqrt(2000) - 1] = 174,885. Using n = 20 (divides 1000), k = 39: 2(39)(1000) + 39(50)^2 = 78,000 + 97,500 = **175,500 crosspoints** (about 17.5% of single crossbar).

**Forouzan P8-1.** Circuit-switched path, 1 Mbps, setup + teardown exchange 1000 bits, distance 5000 km, v = 2x10^8 m/s.
- tau = 5,000,000 / 2x10^8 = 25 ms. Transmission of 1000 bits = 1000 / 10^6 = 1 ms.
- Assume setup is two-way (request + ack) and teardown one-way: 3 tau + 3 transmissions = 75 + 3 = **78 ms** (same for all cases).
- (a) 1000 data bits: 78 + 25 + 1 = **104 ms**.
- (b) 100,000 bits: 78 + 25 + 100 = **203 ms**.
- (c) 1,000,000 bits: 78 + 25 + 1000 = **1103 ms**.
- (d) Per 1000 bits: 104 ms, 2.03 ms, 1.103 ms. **Circuit switching becomes efficient only when a lot of data is sent**, because the fixed setup/teardown cost gets spread out.

**Forouzan P8-2.** Five datagrams, switch delays 3, 10, 20, 7, 20 ms (switches 1-5), v = 2x10^8 m/s. Delay = path length / v + sum of switch delays.

| Datagram | Path | Propagation | Switch delays | Total |
|---|---|---|---|---|
| 1 | 3200 km, 1-3-5 | 16 ms | 3+20+20 = 43 | **59 ms** |
| 2 | 11,700 km, 1-2-5 | 58.5 ms | 3+10+20 = 33 | **91.5 ms** |
| 3 | 12,200 km, 1-2-3-5 | 61 ms | 3+10+20+20 = 53 | **114 ms** |
| 4 | 10,200 km, 1-4-5 | 51 ms | 3+7+20 = 30 | **81 ms** |
| 5 | 10,700 km, 1-4-3-5 | 53.5 ms | 3+7+20+20 = 50 | **103.5 ms** |

**Arrival order: 1, 4, 2, 5, 3.** Out of order, as datagram networks allow.

**Forouzan P8-7.** Routing table: 1233->3, 1456->2, 3255->1, 4470->4, 7176->2, 8766->3, 9144->2.
Packets: 7176 -> **port 2**, 1233 -> **port 3**, 8766 -> **port 3**, 9144 -> **port 2**.

**Forouzan P8-8.** VC switching table (in port, in VCI -> out port, out VCI):
(1,14)->(3,22), (2,71)->(4,41), (2,92)->(1,45), (3,58)->(2,43), (3,78)->(2,70), (4,56)->(3,11).
- (3, 78) -> **port 2, VCI 70**
- (2, 92) -> **port 1, VCI 45**
- (4, 56) -> **port 3, VCI 11**
- (2, 71) -> **port 4, VCI 41**

**Forouzan P8-3/P8-4 (why the addressing differs):**
- Circuit: needs end-to-end address in setup/teardown to build the path; none in data transfer because the reserved channel (slot/band) is the path. No table needed.
- Datagram: no setup, so every packet needs the full destination address.
- VC: global address in setup/teardown to build table entries; then a short local VCI is enough during data transfer.

---

## 8.4 Traps (Ch 8)

1. **n is the group size, not the number of stage-1 crossbars.** "10 crossbars at the first stage" with N = 100 means n = 10 because N/n = 10. Re-read which number they gave you.
2. **Middle crossbars are (N/n) x (N/n), not n x n.** They happen to be equal when N = 100, n = 10. They are not equal for N = 200, n = 10 (20 x 20). This is exactly the textbook's misprint in Ex 8.4.
3. Stage 1 is **n x k**, stage 3 is **k x n**. Same count, mirrored.
4. Simultaneous connections = (N/n) x k, **not** k alone and not N.
5. Clos says **k >= 2n - 1**, and n = sqrt(N/2). If sqrt(N/2) is not a whole divisor of N, pick a nearby divisor and say so.
6. A single crossbar is **non-blocking**. Multistage with small k **blocks**. Two inputs wanting the same output is "busy", not "blocking".
7. Datagram delay has **3T + 3tau** for **two** switches (three links). Count links = switches + 1.
8. VCI **changes at every switch**. A datagram's destination address **never changes**.
9. VC is normally **data-link layer**. Circuit = **physical**. Datagram = **network**.
10. In VC setup, the **request** fills three columns, the **acknowledgment** fills the outgoing VCI. Students often say the request fills all four.
11. Datagram network has **no** setup/teardown. VC and circuit both do.
12. TSI RAM: written **sequentially**, read **selectively**. Not the other way round.
13. Banyan: **log2 n** stages, **n/2** microswitches each (not n).

---

## 8.5 Practice set (Ch 8). Answers at the very bottom.

**P8.1** Three-stage switch, N = 100, n = 10, k = 6. Find total crosspoints, maximum simultaneous connections, and the blocking factor.
**P8.2** Three-stage switch, N = 50, 10 crossbars in the first stage, 3 in the middle. Find n, crossbar sizes, total crosspoints, and simultaneous connections.
**P8.3** Design a non-blocking three-stage switch for N = 32 using the Clos criteria. Give crossbar sizes and total crosspoints, and compare with a single crossbar.
**P8.4** A 1000-bit packet goes through 2 switches over 3 links. Each link is 400 km, bit rate 1 Mbps, speed 2x10^8 m/s. Waiting times are 2 ms and 3 ms. Total delay in a datagram network?
**P8.5** Same path as P8.4 in a virtual-circuit network with resources reserved in setup. Setup delay = 10 ms, teardown delay = 4 ms. Total delay?
**P8.6** How many stages and microswitches does a 64 x 64 banyan switch have?
**P8.7** A VC switch table has entries (1, 20) -> (3, 45) and (2, 20) -> (3, 18). A frame arrives on port 2 with VCI 20. What leaves, and from which port? Can two entries share the same incoming VCI?
**P8.8** Differentiate circuit switching and datagram packet switching (5 points).
**P8.9** A TSI connects 4 lines with the pattern 1->2, 2->4, 3->1, 4->3. Inputs send A, B, C, D. Give the output frame order and what each output receives.
**P8.10** Why is a circuit-switched network inefficient for computer traffic, while its delay is low?

---

## 8.6 Doomsday box (Ch 8): 15 minutes

```
SWITCHING: circuit (physical) | packet: datagram (network) / virtual-circuit (data-link) | message (app).
CIRCUIT: reserve dedicated path. Phases: SETUP (request + ack) -> DATA TRANSFER -> TEARDOWN.
  No addressing in data transfer. Low efficiency, low delay.
DATAGRAM: no setup/teardown, connectionless, each packet independent, may arrive out of order.
  Routing table: destination address -> port. Delay = 3T + 3tau + w1 + w2.
VIRTUAL CIRCUIT: setup/transfer/teardown, all packets same path, local VCI changes every hop.
  Table: in port, in VCI -> out port, out VCI. Request fills 3 cols, ACK fills out VCI.
  Delay = 3T + 3tau + setup + teardown.
CROSSBAR: n x m crosspoints, never blocks.
3-STAGE: stage1 N/n of (n x k), stage2 k of (N/n x N/n), stage3 N/n of (k x n).
  Total = 2kN + k(N/n)^2.  Max connections = (N/n)*k.  Blocking factor = that / N.
  ** N=100, n=10, k=4 -> 1200 crosspoints, 40 connections vs 100, blocking factor 0.4 **
CLOS: n = sqrt(N/2), k >= 2n-1, total >= 4N[sqrt(2N)-1].
TSI: RAM written in order, read in controlled order. No crosspoints, but delay.
TST: time-space-time = TSIs + crossbar + TSIs.
BANYAN n x n: log2(n) stages, n/2 microswitches each.
```

---

# Answers

### Ch 7 answers

**P7.1** Loss = -0.2 x 10 = -2 dB. P2 = 5 x 10^(-0.2) = **3.15 mW**.
**P7.2** 10 log10(5/50) = 10 log10(0.1) = **-10 dB**.
**P7.3** Total = -4 + 10 - 3 = +3 dB. P = 2 x 10^0.3 = **3.99 mW (about 4 mW)**. Overall gain.
**P7.4** 30 deg: **refraction**. 45 deg: **bends along the interface**. 70 deg: **reflection**.
**P7.5** (a) MF (300 kHz-3 MHz): **sky** propagation, **AM radio**. (b) UHF (300 MHz-3 GHz): **line-of-sight**, UHF TV / cell phones / satellite.
**P7.6** Single mode: very thin core (~7 um), step-index with much lower density, highly focused source, beams almost horizontal, least distortion, longest distance. Multimode graded-index: thicker core (50-100 um), density highest at centre decreasing to the edge, many beams that curve back to centre, more distortion than single mode but less than step-index.
**P7.7** Noise and crosstalk hit both wires. Twisting makes each wire alternately nearer and farther from the noise source, so both pick up equal noise. The receiver uses the difference between the wires, so the noise cancels.
**P7.8** Sunlight contains infrared waves that interfere with the signal. Infrared also cannot penetrate walls, so it is limited to short range inside a room.
**P7.9** Radio waves: omnidirectional antenna, all directions, no alignment needed, used for multicast (AM/FM radio, TV, paging). Microwaves: unidirectional antennas (parabolic dish, horn), narrow beam, antennas must be aligned, line-of-sight, used for unicast (cell phones, satellite links, wireless LANs).
**P7.10** t = 1000 / 2x10^8 = **5 us**.

### Ch 8 answers

**P8.1** Crosspoints = 2(6)(100) + 6(10)^2 = 1200 + 600 = **1800**. Connections = (100/10) x 6 = **60**. Blocking factor = 60/100 = **0.6**.
**P8.2** n = 50/10 = **5**, k = **3**. Stage 1: 10 crossbars of 5 x 3. Stage 2: 3 crossbars of 10 x 10. Stage 3: 10 crossbars of 3 x 5. Crosspoints = 150 + 300 + 150 = **600** (vs 2500 single). Connections = 10 x 3 = **30** (blocking factor 30/50 = 0.6).
**P8.3** n = sqrt(32/2) = **4**, k = 2(4) - 1 = **7**. Stage 1: 8 crossbars of 4 x 7 (224). Stage 2: 7 crossbars of 8 x 8 (448). Stage 3: 8 crossbars of 7 x 4 (224). **Total = 896** vs 32 x 32 = 1024. Check: 4(32)[sqrt(64) - 1] = 128 x 7 = 896.
**P8.4** T = 1000 / 10^6 = 1 ms. tau = 400,000 / 2x10^8 = 2 ms. Delay = 3(1) + 3(2) + 2 + 3 = **14 ms**.
**P8.5** 3(1) + 3(2) + 10 + 4 = **23 ms** (no waiting since resources were reserved).
**P8.6** log2(64) = **6 stages**, 64/2 = **32 microswitches per stage** (192 total).
**P8.7** Look up (port 2, VCI 20): it leaves on **port 3 with VCI 18**. Yes, two entries can share the same incoming VCI if they come in on **different ports**. The pair (in port, in VCI) must be unique.
**P8.8** Circuit vs datagram: (1) circuit has setup and teardown, datagram has none; (2) circuit reserves resources for the whole session, datagram allocates on demand; (3) circuit data is a continuous stream on one fixed path, datagram packets are independent and may take different paths and arrive out of order; (4) circuit needs no address during data transfer, datagram packets carry the full destination address; (5) circuit = physical layer, low efficiency, low fixed delay; datagram = network layer, better efficiency, variable delay with waiting at switches.
**P8.9** Output k receives from the input that maps to k: out1 <- in3 = C, out2 <- in1 = A, out3 <- in4 = D, out4 <- in2 = B. RAM written A B C D, read in order 3, 1, 4, 2. **Output frame: C A D B.**
**P8.10** Resources are reserved for the whole connection, and computers often stay connected while idle, so channels sit unused and other users are denied them (inefficient). But once the path exists there is no waiting at switches, so data delay is only propagation plus transmission (low delay).
