# Ch10 + Ch11: Error Detection/Correction and Data Link Control

Forouzan 5e, chapters 10 and 11. Some old past papers use the 4e book (Hamming code by bit positions, Go-Back-N, Selective Repeat). Those parts are covered too, marked **[4e]**.

Every CRC, checksum, Hamming distance, parity and stuffing result in this file was checked with a Python script.

How to use this file:
1. Read the "What they ask" table for each chapter (2 min).
2. Learn the method once from a worked solution, then cover it and redo it.
3. Do the practice set. Answers are at the very bottom.
4. If you are out of time, read only the two **Doomsday** boxes.

---

# PART A: CHAPTER 10, ERROR DETECTION AND CORRECTION

## A1. What they ask (from SUST past papers)

| Year | Question | Marks | Section below |
|---|---|---|---|
| 2014-15 Q5a | What type of technique is CRC? CRC divisor 1101, data 1011011: find the codeword and show detection at the receiver | 10 | A5.1 |
| 2014-15 Q5b | "Hamming code is a more acceptable process", true or false? Find the Hamming code for 1001101 step by step | 10 | A5.6 |
| 2014-15 Q6e, 2015-16 Q6e | Explain simple parity check and checksum with examples | 2-6 | A3.5, A3.8 |
| 2015-16 Q6e | Even parity for `0011101 1100111 1111111 0000`, simple and 2D | 4 | A5.7 |
| 2014-15 Q4g, 2018-19 Q4d | Define forward error correction (and retransmission) | 1-2 | A3.10 |
| 2015-16 Q4j, 2018-19 Q5a | What is a burst error? Types of errors | 1-2.5 | A3.1 |
| 2015-16 Q4k | Hamming distance d(10000, 00100) | 1 | A5.8 |
| 2018-19 Q1a | Hamming distance between 1001 and 0001 | 1 | A5.8 |
| 2019-20 Q4g | d(10000, 11010) and d(11111, 10000) | 1 | A5.8 |
| 2015-16 Q5e | Define minimum Hamming distance; find d_min of {00000, 00010, 00111, 10011, 11011} | 4 | A5.9 |
| 2016-17 Q6b(i), 2019-20 Q2e | What is d_min? To detect 2-bit errors, what should d_min be? | 2-2.5 | A5.10 |
| 2015-16 Q6d | Dataword 1010011110, divisor 10111: CRC at sender and check at receiver | 6 | A5.2 |
| 2016-17 Q6b(ii) | Dataword 10100111, divisor 10111: CRC codeword | 5 | A5.3 |
| 2018-19 Q6a | Dataword 1010100110, divisor 11001: CRC codeword and decoding | 5 | A5.4 |
| 2016-17 Q1h, 2019-20 Q4h | Polynomial for 10101011 and for 10110011 | 1-2 | A5.11 |
| 2019-20 Q1d, Q1e | Binary for x^5 + x^2; shift 111110 four bits right | 1 each | A5.11 |
| 2019-20 Q3c | Five 8-bit numbers 16, 19, 25, 0, 9: wrapped sum and checksum, receiver check | 5 | A5.5 |
| 2019-20 Q5f | Even parity bit for 11001100 | 2.5 | A5.7 |
| 2016-17 Q6b(iii) | Describe chunk interleaving | 3 | A3.10 |
| TT2 Q1 | k = 3, n = 4: table of datawords and codewords for simple parity C(4,3) | 5 | A5.12 |

**Pattern:** a CRC long division shows up in almost every paper (5-10 marks). Hamming distance and d_min show up every year. Checksum and parity alternate.

---

## A2. The big picture in one paragraph

Bits get flipped by noise on the way. To notice that, the sender adds **extra bits** (redundancy) worked out from the data. The receiver recomputes them. If they do not match, there was an error. Then the receiver either **throws the data away and asks again** (retransmission) or **fixes it itself** (forward error correction). Detection is easy. Correction is harder because you must also know *where* the error is.

---

## A3. Concepts in plain English

### A3.1 Types of errors
- **Single-bit error:** only 1 bit in the data unit changed (0 became 1 or 1 became 0).
- **Burst error:** 2 or more bits changed. The **length of the burst** is counted from the first corrupted bit to the last corrupted bit, including the good bits in between.
  ```
  Sent:      0 1 0 0 0 1 0 0 0 1 0 0 0 0 1 1
  Received:  0 1 0 1 1 1 0 1 0 1 1 0 0 0 1 1
                   ^-------------^            burst length = 8 bits
  ```
- Burst errors are **more likely** than single-bit errors. Noise lasts longer than one bit. Example: noise of 1/100 s at 1 kbps hits 10 bits; at 1 Mbps it hits 10,000 bits. Rule: **bits hit = data rate x noise duration**.

### A3.2 Redundancy, detection vs correction
- **Redundant bits** = extra bits added by the sender and removed by the receiver.
- **Detection** asks one yes/no question: "is anything wrong?"
- **Correction** must find the exact position(s). Much harder. For 1 error in 8 bits there are 8 places to check. For 2 errors there are 28 pairs.
- Two ways to deal with an error:
  1. **Retransmission (ARQ):** detect, discard, the sender sends again.
  2. **Forward error correction (FEC):** the receiver fixes it without asking again.

### A3.3 Block coding: dataword, codeword
- Split the message into blocks of **k bits**. Each block is a **dataword**.
- Add **r redundant bits**. The result is an **n-bit codeword**, with **n = k + r**.
- There are 2^k datawords but 2^n possible n-bit patterns. Only 2^k of them are **valid** codewords. The other 2^n - 2^k are **invalid**.
- **Detection works like this:** if the receiver gets an invalid codeword, an error happened. If the errors happen to turn the codeword into a *different valid* codeword, the error goes **undetected**.

Forouzan Ex 10.1, the code C(3,2):

| Dataword | Codeword |
|---|---|
| 00 | 000 |
| 01 | 011 |
| 10 | 101 |
| 11 | 110 |

Send 011. If you receive 111 (1 bit flipped), it is invalid, so the error is detected. If you receive 000 (2 bits flipped), it is valid, so the error is missed.

### A3.4 Hamming distance
- **Hamming distance d(x, y)** = the number of positions where two equal-length words differ.
- **Trick:** XOR the two words and count the 1s.
  ```
  d(10101, 11110):   10101
                   ^ 11110
                   -------
                     01011   -> three 1s -> d = 3      (Forouzan Ex 10.2)
  ```
- **Minimum Hamming distance d_min** = the smallest distance between *any pair* of valid codewords in the code.
- For a **linear** code (XOR of two valid codewords is also valid), d_min = the number of 1s in the non-zero codeword with the fewest 1s.

**The two rules (memorize):**
```
+-------------------------------------------------------------+
|  To DETECT up to s errors:   d_min = s + 1                  |
|  To CORRECT up to t errors:  d_min = 2t + 1                 |
|                                                             |
|  Reverse: given d_min ->  detects s = d_min - 1             |
|                           corrects t = floor((d_min - 1)/2) |
+-------------------------------------------------------------+
```
Why: if s bits flip, the received word is at distance s from the sent one. It must not land on another valid word, so valid words must be at least s + 1 apart. To *correct*, the received word must be closer to the right codeword than to any other, so the "circles" of radius t around codewords must not touch: d_min > 2t.

Examples: d_min = 2 (parity) detects 1 error and corrects 0. d_min = 3 (Hamming) detects 2 or corrects 1. d_min = 4 detects 3 (Forouzan Ex 10.4).

### A3.5 Simple parity-check code
- Add **1 parity bit** to k data bits, so n = k + 1.
- **Even parity:** choose the bit so the total number of 1s is even. The parity bit = XOR of all data bits (1 if the count of 1s is odd).
- **Odd parity:** make the total odd. (Forouzan uses even unless told otherwise.)
- Receiver: XOR all n bits. This 1-bit result is the **syndrome**. Syndrome 0 means accept. Syndrome 1 means discard.
- d_min = 2, so it **detects any odd number of errors** and **misses any even number** (2 flips cancel out).

Forouzan Ex 10.7: dataword 1011 gives codeword 10111.
- Receive 10111: syndrome 0, accept.
- Receive 10011 (1 error): syndrome 1, discard.
- Receive 00110 (2 errors): syndrome 0. Wrong dataword 0011 accepted. **Missed.**
- Receive 01011 (3 errors): syndrome 1, discard. Odd counts are caught.

### A3.6 Two-dimensional parity [4e]
Put the data units in rows of a table. Add a parity bit to **each row** and a parity row for **each column**. Send the whole table.
- Detects **all 1-, 2- and 3-bit errors**. Some 4-bit errors in a rectangle (2 rows x 2 columns) slip through.
- A single error shows up in exactly one row and one column, so you can even locate and fix it.
- A worked example is in A5.7.

### A3.7 CRC (Cyclic Redundancy Check)
**What type of technique is CRC?** It is an **error-detection** technique. It is a **cyclic code** (a linear block code where rotating any codeword gives another codeword). It uses **modulo-2 binary division**. It is used in LANs and WANs (Ethernet, HDLC, PPP).

**Modulo-2 arithmetic:** add and subtract are both **XOR**, with no carries and no borrows. 1+1 = 0, 1+0 = 1, 0+0 = 0.

**Words:**
- **Divisor** (also called the **generator**, g(x)) is agreed in advance. It has r + 1 bits.
- **r = number of check bits = (divisor length - 1).**
- **Augmented dataword** = the dataword with r zeros added on the right.
- **Remainder** = the r check bits (CRC). **Syndrome** = the remainder computed at the receiver.

**Sender (encoder):**
1. Append r zeros to the dataword.
2. Divide by the divisor using modulo-2 long division.
3. Throw away the quotient. The **r-bit remainder** is the CRC.
4. **Codeword = dataword followed by the remainder.** (Do not send the zeros.)

**Receiver (decoder):**
1. Divide the whole received codeword by the same divisor.
2. Remainder (syndrome) all 0s: no error, accept the first k bits as the dataword.
3. Remainder not all 0s: error, discard.

**The one rule of the long division:** at each step look at the **leftmost bit** of the current chunk.
- If it is 1, XOR with the divisor (quotient bit 1).
- If it is 0, XOR with all 0s (quotient bit 0).
- Drop the leftmost bit (it is always 0 now), bring down the next bit, and repeat until no bits are left.

```
              CRC ENCODER                                   CRC DECODER
  dataword (k bits)                               received codeword (n bits)
        |                                                   |
        v                                                   v
  [ append r zeros ]                               +-----------------+
        |                                          |  divide by the  |<-- same divisor
        v                                          |  divisor (mod 2)|
  +-----------------+                              +-----------------+
  | divide by       |<-- divisor (r+1 bits)                 |
  | divisor (mod 2) |    shared by both sides                v
  +-----------------+                              syndrome (r bits)
        |                                                   |
        v                                          all 0s? --yes--> accept dataword
  remainder (r bits)                                        |
        |                                                   no --> discard
        v
  codeword = dataword | remainder  ---- unreliable link ---->
```

**Polynomials (a shorthand for bit patterns).** Bit i from the right (starting at 0) becomes the term x^i.
`1000011` = x^6 + x + 1. The **degree** is the highest power, which is (number of bits - 1).
- **Shift left by m bits** (add m zeros) means multiply by x^m. **Shift right by m bits** (drop m bits on the right) means divide by x^m and throw away the negative powers.

**What makes a good generator g(x)** (Forouzan 10.3.4):
1. It has at least 2 terms, and the x^0 term is 1 (the rightmost bit is 1). Then it **catches all single-bit errors**.
2. It does not divide x^t + 1 for t between 2 and n - 1. Then it **catches all isolated double errors**.
3. It has the factor (x + 1). Then it **catches all odd numbers of errors**.
4. With r check bits it **catches all burst errors of length L <= r**. For L = r + 1 the detection probability is 1 - (1/2)^(r-1). For L > r + 1 it is 1 - (1/2)^r.

Standard generators (Table 10.4): CRC-8 (ATM header), CRC-10 (ATM AAL), **CRC-16 x^16 + x^12 + x^5 + 1 (HDLC)**, **CRC-32 (LANs/Ethernet)**.

### A3.8 Checksum
Used mostly at the network and transport layers (the Internet checksum). It works on a message of any length.

**Idea:** split the data into m-bit words, add them up, and send the **complement of the sum**. The receiver adds everything, including the checksum, and should get all 1s. Complementing that gives all 0s, so it accepts.

**One's complement addition (wrapping):** if the sum needs more than m bits, cut off the extra bits on the left and **add them back** at the right end. Repeat until it fits in m bits.

**Checksum = complement of the wrapped sum** (flip every bit, which is the same as (2^m - 1) - sum).

| Sender | Receiver |
|---|---|
| 1. Split into m-bit words (16-bit in the Internet) | 1. Split into m-bit words, including the checksum |
| 2. Set the checksum to 0 | 2. Add all words in one's complement |
| 3. Add all words in one's complement | 3. Complement the sum |
| 4. Complement the sum. This is the checksum | 4. Result 0: accept. Otherwise: reject |

**Weakness:** it is not weighted, so swapping two words or +1 in one word and -1 in another goes undetected.
**Fletcher checksum** fixes this by weighting each item by its position. It uses two running sums, R = (R + D) mod 256 and L = (L + R) mod 256, and the checksum is L x 256 + R. 8-bit Fletcher gives a 16-bit checksum. 16-bit Fletcher gives a 32-bit checksum.
**Adler checksum** is a 32-bit checksum like 16-bit Fletcher, but it works on single bytes, uses the **prime modulus 65,521**, and starts with R = 1.

### A3.9 Hamming code [4e; 5e only mentions it]
- A single-error-**correcting** code with **d_min = 3**. It corrects 1 error or detects 2.
- 4e table form: n = 2^m - 1, k = n - m, for example **C(7,4)** (m = 3 check bits).
- **Position method** (what the 2014-15 paper wants). Parity bits sit at positions that are **powers of 2: 1, 2, 4, 8, ...**. Data bits fill the remaining positions.
- **Number of parity bits r** for m data bits: the smallest r with **2^r >= m + r + 1**.
- Parity bit at position p checks every position whose binary number has that bit set:
  - r1 checks 1, 3, 5, 7, 9, 11 (binary ends in 1)
  - r2 checks 2, 3, 6, 7, 10, 11
  - r4 checks 4, 5, 6, 7 (and 12-15)
  - r8 checks 8, 9, 10, 11 (and 12-15)
- At the receiver, recompute each check. Write a 1 for each check that fails. The binary number (r8 r4 r2 r1) gives the **position of the bad bit**. Flip it.

### A3.10 Forward error correction (FEC), 5e 10.5
**Definition:** the receiver corrects errors itself, with no retransmission, using redundant bits sent in advance. It is needed for **real-time audio and video**, where waiting for a resend causes unacceptable delay.
**Retransmission (ARQ, Automatic Repeat reQuest):** the receiver only detects errors, discards the bad unit, and the sender sends it again (after a timeout or a NAK).

FEC methods in 5e:
1. **Hamming distance:** make d_min = 2t + 1. This is costly. Example: the BCH code sends 255 bits for 99 data bits to correct 23 errors.
2. **XOR:** send N chunks plus R = P1 XOR P2 XOR ... XOR PN. Any **one** lost chunk = the XOR of all the others and R. With N = 4 this costs 25% extra.
3. **Chunk interleaving:** split each packet into small chunks. Build the packets *column-wise*, so each sent packet carries one chunk from each of several original packets. If one sent packet is lost, every original packet loses only **one small chunk**, which is fine for audio and video.
   ```
   Original packets (rows)        Sent packets (columns)
   P1: 01 02 03 04 05             S1: 01 06 11 16 21
   P2: 06 07 08 09 10             S2: 02 07 12 17 22
   P3: 11 12 13 14 15     ==>     S3: 03 08 13 18 23   <- lost
   P4: 16 17 18 19 20             S4: 04 09 14 19 24
   P5: 21 22 23 24 25             S5: 05 10 15 20 25
   Result: every original packet misses only 1 chunk (03, 08, 13, 18, 23).
   ```
4. **Hamming + interleaving:** m codewords that each correct t bits, sent column by column, can fix a burst of **m x t** bits.
5. **Compounding high- and low-resolution packets:** each packet also carries a low-resolution copy of the previous packet. If a packet is lost, play its low-resolution copy.

---

## A4. Formula and rules box

```
n = k + r                 dataword k bits, r redundant bits, codeword n bits
valid codewords = 2^k     invalid = 2^n - 2^k
d(x,y) = number of 1s in (x XOR y)
detect s errors:  d_min = s + 1
correct t errors: d_min = 2t + 1
simple parity:    d_min = 2, detects any odd number of errors
Hamming code:     d_min = 3;  2^r >= m + r + 1;  parity bits at positions 1,2,4,8
4e Hamming C(n,k): n = 2^m - 1, k = n - m
CRC:  r = len(divisor) - 1; append r zeros; remainder = r bits; codeword = data | remainder
      receiver: syndrome 000..0 -> accept
CRC catches: all single-bit errors if x^0 term = 1 and >= 2 terms
             all odd errors if (x+1) is a factor
             all bursts with L <= r
             L = r+1: P(detect) = 1 - (1/2)^(r-1);  L > r+1: 1 - (1/2)^r
checksum: one's complement sum (wrap carries), checksum = complement = (2^m - 1) - sum
          receiver: sum of all incl. checksum = all 1s -> complement = 0 -> accept
bits hit by noise = data rate x noise duration
```

---

## A5. Worked past-paper solutions

### A5.0 Warm-up: the textbook CRC (Forouzan Fig 10.6 / 10.7)
Dataword **1001**, divisor **1011** (so r = 3, append 000).
```
Encode: divide 1001 000 by 1011
    quotient: 1010
    1001000      <- dividend
    1011
    ----
     0100
     0000   (leftmost 0 -> use 0s)
     ----
      1000
      1011
      ----
       0110
       0000   (leftmost 0 -> use 0s)
       ----
        110   <- REMAINDER
```
Codeword = 1001 | 110 = **1001110**.

Receiver gets 1001110 (no error):
```
    1001110
    1011
    ----
     0101
     0000
     ----
      1011
      1011
      ----
       0000
       0000
       ----
        000   <- syndrome all zero -> accept 1001
```
Receiver gets 1000110 (bit 3 flipped):
```
    1000110
    1011
    ----
     0111
     0000
     ----
      1111
      1011
      ----
       1000
       1011
       ----
        011   <- syndrome non-zero -> discard
```
**How to read the layout:** each new row is the last XOR result *without its leftmost bit*, plus the next bit brought down from the dividend. Everything stays aligned in columns.

---

### A5.1 [2014-15 Q5a] CRC divisor 1101, data 1011011 (10 marks)

**Part 1: "Which type of technique is CRC?"**
CRC is an **error-detecting** technique based on **cyclic codes**. The sender appends a remainder obtained by **modulo-2 (XOR) division** by a fixed generator. The receiver repeats the division and checks for a zero remainder.

**Part 2: find the codeword.**
- Divisor 1101 has 4 bits, so r = 3. Append **000**.
- Dividend = 1011011 000.
```
    quotient: 1100101
    1011011000      <- dividend
    1101
    ----
     1100
     1101
     ----
      0011
      0000   (leftmost 0 -> use 0s)
      ----
       0111
       0000   (leftmost 0 -> use 0s)
       ----
        1110
        1101
        ----
         0110
         0000   (leftmost 0 -> use 0s)
         ----
          1100
          1101
          ----
           001   <- REMAINDER
```
Remainder = 001. **Codeword = 1011011 001 = `1011011001`.**

**Part 3: detection at the receiver.**
Case A, no error: divide the received word 1011011001 by 1101.
```
    1011011001
    1101
    ----
     1100
     1101
     ----
      0011
      0000
      ----
       0111
       0000
       ----
        1110
        1101
        ----
         0110
         0000
         ----
          1101
          1101
          ----
           000   <- syndrome 000 -> no error, accept 1011011
```
Case B, there is an error. Suppose bit 4 flips during transmission: we receive `1010011001`.
```
    1010011001
    1101
    ----
     1110
     1101
     ----
      0111
      0000
      ----
       1111
       1101
       ----
        0100
        0000
        ----
         1000
         1101
         ----
          1011
          1101
          ----
           110   <- syndrome 110 (non-zero) -> ERROR DETECTED, discard
```
**Answer: codeword 1011011001. The receiver divides by 1101. Remainder 000 means accept. Any non-zero remainder (for example 110) means discard and ask for a resend.**

---

### A5.2 [2015-16 Q6d] Dataword 1010011110, divisor 10111 (3 + 3 marks)

(i) **Sender.** The divisor has 5 bits, so r = 4. Append **0000**.
```
    quotient: 1001101110
    10100111100000      <- dividend
    10111
    -----
     00111
     00000   (leftmost 0 -> use 0s)
     -----
      01111
      00000   (leftmost 0 -> use 0s)
      -----
       11111
       10111
       -----
        10001
        10111
        -----
         01100
         00000   (leftmost 0 -> use 0s)
         -----
          11000
          10111
          -----
           11110
           10111
           -----
            10010
            10111
            -----
             01010
             00000   (leftmost 0 -> use 0s)
             -----
              1010   <- REMAINDER
```
**Codeword = 1010011110 | 1010 = `10100111101010`.**

(ii) **Receiver, no error.** Divide 10100111101010 by 10111.
```
    10100111101010
    10111
    -----
     00111
     00000
     -----
      01111
      00000
      -----
       11111
       10111
       -----
        10001
        10111
        -----
         01100
         00000
         -----
          11001
          10111
          -----
           11100
           10111
           -----
            10111
            10111
            -----
             00000
             00000
             -----
              0000   <- syndrome 0000 -> no error, dataword 1010011110 accepted
```
**Answer: codeword 10100111101010, syndrome 0000.**

(Forouzan P10-12 is almost the same question with dataword 101001111. Its remainder is 0101 and its codeword is 1010011110101.)

---

### A5.3 [2016-17 Q6b(ii)] Dataword 10100111, divisor 10111 (5 marks)
r = 4, so append 0000.
```
    quotient: 10011011
    101001110000      <- dividend
    10111
    -----
     00111
     00000   (leftmost 0 -> use 0s)
     -----
      01111
      00000   (leftmost 0 -> use 0s)
      -----
       11111
       10111
       -----
        10000
        10111
        -----
         01110
         00000   (leftmost 0 -> use 0s)
         -----
          11100
          10111
          -----
           10110
           10111
           -----
            0001   <- REMAINDER
```
**Codeword = 10100111 | 0001 = `101001110001`.**
Check (worth writing if you have time): 101001110001 divided by 10111 leaves remainder 0000.

---

### A5.4 [2018-19 Q6a] Dataword 1010100110, divisor 11001 (5 marks)
r = 4, so append 0000.
```
    quotient: 1100011010
    10101001100000      <- dividend
    11001
    -----
     11000
     11001
     -----
      00010
      00000   (leftmost 0 -> use 0s)
      -----
       00101
       00000   (leftmost 0 -> use 0s)
       -----
        01011
        00000   (leftmost 0 -> use 0s)
        -----
         10110
         11001
         -----
          11110
          11001
          -----
           01110
           00000   (leftmost 0 -> use 0s)
           -----
            11100
            11001
            -----
             01010
             00000   (leftmost 0 -> use 0s)
             -----
              1010   <- REMAINDER
```
**Generated CRC codeword = 1010100110 | 1010 = `10101001101010`.**

**Decoding at the receiver** (no error):
```
    10101001101010
    11001
    -----
     11000
     11001
     -----
      00010
      00000
      -----
       00101
       00000
       -----
        01011
        00000
        -----
         10110
         11001
         -----
          11111
          11001
          -----
           01100
           00000
           -----
            11001
            11001
            -----
             00000
             00000
             -----
              0000   <- syndrome 0000 -> accept, dataword = first 10 bits = 1010100110
```

---

### A5.5 [2019-20 Q3c] Checksum of five 8-bit numbers 16, 19, 25, 0, 9 (5 marks)

**Sender:**
```
  16 = 00010000
  19 = 00010011
  25 = 00011001
   0 = 00000000
   9 = 00001001
  -------------
 sum = 01000101  = 69   (fits in 8 bits, no carry to wrap)
```
- Wrapped sum = **69 = 01000101**.
- Checksum = complement = **10111010 = 186** (check: 255 - 69 = 186).
- Send: 16, 19, 25, 0, 9, **186**.

**Receiver (no error):**
```
  16 + 19 + 25 + 0 + 9 + 186 = 255 = 11111111   (one's complement sum)
  complement(11111111)       =       00000000   -> 0 -> data not corrupted, accept
```
**Answer: wrapped sum = 69 (01000101), checksum = 186 (10111010), and the receiver's new checksum is 0, so the data is accepted.**

**Textbook version with wrapping (Forouzan Ex 10.11-10.13), 4-bit numbers 7, 11, 12, 0, 6.** Learn this one too, because here the carry actually wraps.
```
Sender:  7 + 11 + 12 + 0 + 6 = 36 = 10 0100   (6 bits, too long for 4)
         wrap: 0100 + 10 = 0110 = 6            <- wrapped sum
         checksum = complement(0110) = 1001 = 9  (= 15 - 6)
         send (7, 11, 12, 0, 6, 9)
Receiver: 7 + 11 + 12 + 0 + 6 + 9 = 45 = 10 1101
         wrap: 1101 + 10 = 1111 = 15
         complement(1111) = 0000 -> accept
```

**16-bit Internet checksum (Forouzan P10-18)**, words A7A2, CABF, 903A, A123 (hex):
```
   A7A2 + CABF + 903A + A123 = 2A3BE    (hex, more than 16 bits)
   wrap: A3BE + 2 = A3C0                <- sum
   checksum = FFFF - A3C0 = 5C3F
```

---

### A5.6 [2014-15 Q5b] Is Hamming code "a more acceptable process"? Hamming code for 1001101 (10 marks)

**True or false, and why.** **True**, for single-bit errors. Parity and CRC can only *detect* errors and then need a retransmission. A Hamming code can **locate and correct** a single-bit error at the receiver (FEC), using only a few extra bits (r parity bits with 2^r >= m + r + 1, which is 4 bits for 7 data bits). Its limit: it corrects only **1 error** per codeword (d_min = 3). For burst errors it needs interleaving.

**Step 1: number of parity bits.** m = 7 data bits.
r = 3: 2^3 = 8 >= 7 + 3 + 1 = 11? No.
r = 4: 2^4 = 16 >= 7 + 4 + 1 = 12? **Yes.** So r = 4 and the codeword is **11 bits**.

**Step 2: place the bits.** Parity bits go at positions 1, 2, 4, 8. Data fills positions 11, 10, 9, 7, 6, 5, 3, starting with the leftmost data bit at the highest position.
```
Position :  11  10   9   8   7   6   5   4   3   2   1
Type     :  d   d    d   r8  d   d   d   r4  d   r2  r1
Data     :  1   0    0   ?   1   1   0   ?   1   ?   ?
```

**Step 3: compute each parity bit (even parity).**
| Parity bit | Checks positions | Data bits there | Number of 1s | Value |
|---|---|---|---|---|
| r1 | 1, 3, 5, 7, 9, 11 | 1, 0, 1, 0, 1 | 3 (odd) | **1** |
| r2 | 2, 3, 6, 7, 10, 11 | 1, 1, 1, 0, 1 | 4 (even) | **0** |
| r4 | 4, 5, 6, 7 | 0, 1, 1 | 2 (even) | **0** |
| r8 | 8, 9, 10, 11 | 0, 0, 1 | 1 (odd) | **1** |

**Step 4: the codeword.**
```
Position :  11  10   9   8   7   6   5   4   3   2   1
Codeword :  1   0    0   1   1   1   0   0   1   0   1
```
**Hamming code = `10011100101`.**

**Step 5 (shows understanding, earns extra marks): correcting an error.** Suppose bit 7 flips, so we receive 10010100101. Recheck each group:
- r1 group (1, 3, 5, 7, 9, 11) = 1, 1, 0, 0, 0, 1: three 1s, odd, so **1**.
- r2 group (2, 3, 6, 7, 10, 11) = 0, 1, 1, 0, 0, 1: three 1s, odd, so **1**.
- r4 group (4, 5, 6, 7) = 0, 0, 1, 0: one 1, odd, so **1**.
- r8 group (8, 9, 10, 11) = 1, 0, 0, 1: even, so **0**.

Read r8 r4 r2 r1 = 0111 = **7**. Bit 7 is wrong. Flip it back to get the correct codeword.

**4e table version, for comparison.** 4e defines C(7,4) with r0 = a2+a1+a0, r1 = a3+a2+a1, r2 = a1+a0+a3. For example, 0111 becomes 0111001. Use the position method unless the question gives these equations.

---

### A5.7 [2015-16 Q6e and 2019-20 Q5f] Parity bits, simple and 2D, even parity

**2019-20 Q5f: 11001100.** It has four 1s, which is already even. **Parity bit = 0**, codeword 110011000.

**2015-16 Q6e: 0011101, 1100111, 1111111, 0000 (even parity).**

**Simple parity** (one bit per unit, appended at the end):
| Unit | 1s | Parity | Sent |
|---|---|---|---|
| 0011101 | 4 | 0 | 0011101**0** |
| 1100111 | 5 | 1 | 1100111**1** |
| 1111111 | 7 | 1 | 1111111**1** |
| 0000 | 0 | 0 | 0000**0** |

**Two-dimensional parity.** The rows need equal length, so write 0000 as 0000000 (leading zeros change nothing). Row parity goes at the right. The column parity row goes at the bottom.
```
                 data      | row parity
 row 1        0 0 1 1 1 0 1 | 0
 row 2        1 1 0 0 1 1 1 | 1
 row 3        1 1 1 1 1 1 1 | 1
 row 4        0 0 0 0 0 0 0 | 0
              --------------+--
 column par.  0 0 0 0 1 0 1 | 0
```
Column 5, for example: 1, 1, 1, 0 has three 1s, so its parity is 1.
**Sent: 00111010 11001111 11111111 00000000 00001010.**

Explaining simple parity: "one extra bit makes the count of 1s even. The receiver XORs all bits. Syndrome 0 means accept. It detects any odd number of errors but misses 2 errors." Then give the 1011 to 10111 example from A3.5.

---

### A5.8 Hamming distance one-liners
| Pair | XOR | d |
|---|---|---|
| 10000, 00100 (2015-16) | 10100 | **2** |
| 1001, 0001 (2018-19) | 1000 | **1** |
| 10000, 11010 (2019-20) | 01010 | **2** |
| 11111, 10000 (2019-20) | 01111 | **4** |

### A5.9 [2015-16 Q5e] d_min of {00000, 00010, 00111, 10011, 11011}
**Definition:** the minimum Hamming distance is the smallest Hamming distance between all possible pairs of codewords in the set.

There are 5 words, so C(5,2) = 10 pairs:
| Pair | d | Pair | d |
|---|---|---|---|
| 00000-00010 | **1** | 00010-10011 | 2 |
| 00000-00111 | 3 | 00010-11011 | 3 |
| 00000-10011 | 3 | 00111-10011 | 2 |
| 00000-11011 | 4 | 00111-11011 | 3 |
| 00010-00111 | 2 | 10011-11011 | **1** |

**d_min = 1.** (So this code cannot even guarantee detecting a single error.)

### A5.10 [2016-17, 2019-20] d_min to detect two-bit errors
d_min = s + 1 with s = 2, so **d_min = 3**.

### A5.11 Polynomials
- **10101011** (2016-17): positions 7 to 0 hold 1 0 1 0 1 0 1 1, so **x^7 + x^5 + x^3 + x + 1**.
- **10110011** (2019-20): 1 0 1 1 0 0 1 1, so **x^7 + x^5 + x^4 + x + 1**.
- **x^5 + x^2** to binary (2019-20): powers 5 down to 0 are 1 0 0 1 0 0, so **100100**.
- **Shift 111110 four bits right** (2019-20): drop the 4 rightmost bits to get **11**. In polynomials: (x^5+x^4+x^3+x^2+x) / x^4 = x + 1 (the x^0 and negative-power terms are dropped). Shifting left 3 would instead give 111110000.

### A5.12 [TT2 Q1] Simple parity code C(4,3), k = 3, n = 4 (even parity)
| Dataword | Codeword | Dataword | Codeword |
|---|---|---|---|
| 000 | 0000 | 100 | 1001 |
| 001 | 0011 | 101 | 1010 |
| 010 | 0101 | 110 | 1100 |
| 011 | 0110 | 111 | 1111 |

There are 2^3 = 8 valid codewords out of 2^4 = 16 patterns, so 8 are invalid. d_min = 2.

---

## A6. Traps (Ch10)
1. **Append r = (divisor length - 1) zeros, not divisor-length zeros.** Divisor 10111 needs 4 zeros.
2. **When the leftmost bit is 0, XOR with all 0s.** Do not skip the step, because the quotient needs a 0 there and alignment breaks if you skip.
3. **The codeword is dataword + remainder.** Do not send the augmented zeros, and do not send the quotient.
4. The remainder always has **exactly r bits**. Keep leading zeros (0001, not 1).
5. **Receiver: divide the whole codeword, with no extra zeros appended.**
6. CRC uses **XOR**, not ordinary subtraction. There are no borrows.
7. In checksum, **wrap the carry back in**, maybe more than once (31 = 1 1111 becomes 1 + 1111 = 1 0000, which becomes 0000 + 1 = 0001).
8. Checksum = **complement** of the sum. Do not send the sum itself.
9. d_min for **detect** is s + 1. For **correct** it is 2t + 1. Do not swap them.
10. Simple parity **misses even numbers of errors**. It detects odd numbers (not just 1).
11. Hamming parity positions are **1, 2, 4, 8**, counted from the **right**. Write the position row first, then fill in the bits.
12. Polynomial powers count from **0 at the rightmost bit**. Degree = number of bits - 1.
13. "Burst length" counts from the first bad bit to the last bad bit, including good bits in between.

---

## A7. Doomsday box, Ch10 (memorize in 15 minutes)
```
* single-bit = 1 bit changed; burst = 2+ bits; burst more likely
* d(x,y) = count 1s of x XOR y;  d_min = smallest over all pairs
* DETECT s: d_min = s+1     CORRECT t: d_min = 2t+1     parity d_min = 2
* even parity bit = XOR of data bits (makes total 1s even)
* CRC: r = len(divisor)-1; append r zeros; XOR-divide (leftmost 0 -> XOR 0000);
       remainder (r bits) appended to data; receiver remainder 0 -> accept
* checksum: add (wrap carries), complement; receiver total = all 1s -> 0 -> accept
* Hamming: 2^r >= m+r+1; parity at 1,2,4,8; r1:1,3,5,7,9,11  r2:2,3,6,7,10,11
           r4:4-7  r8:8-11; syndrome bits = position of the bad bit
* 1001101 -> 10011100101 (classic exam answer)
* FEC = receiver fixes itself (no resend), for real-time; ARQ = detect + resend
* polynomial: bit i from right -> x^i
```

---
---

# PART B: CHAPTER 11, DATA LINK CONTROL (DLC)

## B1. What they ask

| Year | Question | Marks | Section |
|---|---|---|---|
| 2016-17 Q3c | (i) Explain the Stop-and-Wait protocol. (ii) Draw its flow diagram with seq/ack numbers: frame 0 lost; frame 0 resent and ACKed; frame 1 sent, ACK lost; frame 1 resent and ACKed | 4 + 6 | B3.5, B5.1 |
| 2019-20 Q6c | Same, plus "frame 1 resent but timed out" before the final resend | 5 | B5.2 |
| TT2 Q3 | Key responsibilities of the data link layer | 5 | B3.1 |
| TT2 Q4a | Why are flags needed with variable-size frames? | 2.5 | B3.2 |
| TT2 Q4b | Compare byte-oriented and bit-oriented protocols | 2.5 | B3.2, B5.4 |
| 2014-15 Q3a | Advantage of a bit-oriented protocol over a byte-oriented one for error handling (with example). Define a bit-oriented protocol | 7.5 | B5.4 |
| 2014-15 Q1b(v) | Meaning of ACK-3 and NAK-3 | 1 | B5.5 |
| 2015-16 Q4l | How many protocols does a noisy channel have? | 1 | B5.6 |
| 2015-16 Q1g | How many bits fit on a link with 2 ms delay at 10 Mbps? (bandwidth-delay product) | 1 | B5.7 |

**Pattern:** the **Stop-and-Wait flow diagram** is the big-mark question (6-10 marks), in two papers with almost the same scenario. Framing, stuffing and byte vs bit are the short-answer favourites.

---

## B2. The big picture
The physical layer moves raw bits. The **data link layer (DLL)** turns them into a reliable **node-to-node** (hop-to-hop) link. It has two sublayers. **DLC (data link control)** handles framing, flow control and error control (this chapter). **MAC (media access control)** decides who talks on a shared medium (chapter 12).

---

## B3. Concepts in plain English

### B3.1 DLC services (TT2 Q3)
1. **Framing:** pack bits into frames so each frame is distinguishable. Add the sender and receiver (link-layer) addresses in the header.
2. **Flow control:** do not let a fast sender overwhelm a slow receiver. The receiver gives feedback (stop / slow down / send more). Buffers at both ends help.
3. **Error control:** a CRC is added by the sender and checked by the receiver. A corrupted frame is **silently discarded**. Either nothing more happens (Ethernet) or an **ACK** is sent for good frames, and a missing ACK causes a resend.
4. **Connectionless or connection-oriented service.** Connectionless: frames are independent and unnumbered (most LANs). Connection-oriented: setup, then transfer of numbered, in-order frames, then teardown (PPP, some WANs).

(For a 5-mark "responsibilities of DLL" answer, also list **physical addressing**, **media access control** on shared links, and **node-to-node delivery**.)

### B3.2 Framing
- **Frame:** the unit of data at the DLL. It is the envelope around a network-layer packet: header (addresses, control), data, and trailer (CRC).
- **Why not one huge frame?** One bit error would force resending everything. Small frames mean a small loss.
- **Fixed-size framing:** the size itself marks the boundary, so no flag is needed. Example: ATM cells, 53 bytes.
- **Variable-size framing:** needs a **delimiter (flag)** to mark where a frame starts and ends.

**Why flags are needed with variable-size frames (TT2 Q4a):** the receiver sees a continuous bit stream. Since frames have no fixed length, it cannot count bits to find boundaries. A special **flag pattern at the start and end** tells it "a frame begins here" and "a frame ends here". Stuffing is then needed so the flag pattern never appears by accident inside the data.

**Character-oriented (byte-oriented) framing:**
```
+------+--------+------------------------------------+---------+------+
| Flag | Header | data: variable number of 8-bit chars | Trailer | Flag |
+------+--------+------------------------------------+---------+------+
```
- Data is a sequence of **8-bit characters** (for example ASCII). The flag is a special byte.
- **Byte stuffing (character stuffing):** if the data contains a byte equal to the **flag** or the **ESC** (escape) byte, put an extra **ESC** byte before it. The receiver removes each ESC and treats the next byte as plain data.
- Problem: it is tied to 8-bit characters, which clashes with 16/32-bit Unicode. The trend is toward bit-oriented protocols.

**Bit-oriented framing:**
```
 01111110 | Header | data: any number of bits | Trailer | 01111110
   flag                                                    flag
```
- Data is a **sequence of bits** (text, image, audio, anything).
- The flag is **01111110** (a 0, six 1s, a 0).
- **Bit stuffing:** after a **0 followed by five consecutive 1s**, the sender inserts an extra **0**, whatever the next bit is. Then six 1s in a row can never appear inside the data. The receiver deletes the 0 that follows five 1s.
- The real flags are **not** stuffed.

| | Byte-oriented | Bit-oriented |
|---|---|---|
| Data unit | 8-bit characters | Bits |
| Flag | A special byte (PPP: 01111110) | 01111110 |
| Transparency | Byte stuffing with ESC | Bit stuffing (0 after five 1s) |
| Overhead per stuff | 1 whole byte | 1 bit |
| Works with Unicode/binary | Awkward | Yes |
| Example | PPP | HDLC (and Ethernet's ancestor) |

### B3.3 Flow and error control
- **Flow control** prevents losing frames at the receiver (overflow). It balances the producer (sender) with the consumer (receiver).
- **Error control** prevents delivering corrupted frames to the network layer. It is done with CRC, discarding, ACKs and resending.
- They can be **combined**: one ACK says both "I got it fine" (error control) and "send the next one" (flow control).

### B3.4 Simple protocol
No flow control and no error control. The receiver is assumed never to be overwhelmed. The sender sends frames one after another. Each side's FSM has one state (Ready).

### B3.5 Stop-and-Wait protocol (2016-17 Q3c(i))
**Explanation, ready to write in the exam:**
1. The sender sends **one frame**, keeps a **copy**, starts a **timer**, and then **stops and waits** for an ACK.
2. The receiver checks the CRC. A good frame is delivered and an **ACK** is sent. A corrupted frame is **silently discarded** (no ACK).
3. If the ACK arrives before the timer expires, the sender stops the timer, discards the copy, and sends the next frame.
4. If the timer expires (the frame or the ACK was lost or corrupted), the sender **resends the saved copy** and restarts the timer.
5. **Sequence numbers** stop duplicates. They only need to be **0, 1, 0, 1, ... (modulo 2)**. The **ACK number = the sequence number of the next frame expected**, so frame 0 is answered with ACK 1, and frame 1 with ACK 0.
6. Only **one frame and one ACK** are in the channel at any time. It is simple but wasteful on long or fast links (see bandwidth-delay, B3.8).

**Why sequence numbers (Forouzan Ex 11.3 vs 11.4):** without them, if an ACK is lost the sender resends, and the receiver delivers the **same packet twice** (a duplicate). With sequence numbers the receiver sees "I expect 0, this is 1 again", discards it, and re-sends the ACK.

**FSMs (Forouzan Fig 11.11):**
```
SENDER                                                RECEIVER
         packet from network layer:                    +-------+  error-free frame arrived:
         make frame, save copy, send,                  |       |  deliver packet, send ACK
         start timer                                   | Ready |<-----+
 +-------+ ----------------------------> +----------+  |       |------+
 | Ready |                               | Blocking |  |       |  corrupted frame arrived:
 +-------+ <---------------------------- +----------+  +-------+  discard it
         error-free ACK arrived:            |    ^
         stop timer, discard saved frame    |    |  time-out: resend saved frame,
                                            +----+  restart timer
                                            |    ^
                                            +----+  corrupted ACK arrived: discard ACK
```
(With sequence numbers, the sender in Blocking also discards an ACK with the wrong number, and the receiver discards a frame with the wrong number but **still re-sends the ACK**.)

### B3.6 Piggybacking
When both sides send data, a node **puts the ACK for received frames inside its own outgoing data frame** instead of sending a separate ACK frame. This saves bandwidth and frames. It is more complex, so it is uncommon at the DLL. In HDLC the I-frame's N(R) field carries the piggybacked ACK.

### B3.7 Noisy-channel protocols [4e]: Go-Back-N and Selective Repeat
4e splits the protocols by channel:
- **Noiseless channel:** Simplest, and Stop-and-Wait. That is 2 protocols.
- **Noisy channel:** Stop-and-Wait ARQ, Go-Back-N ARQ, Selective Repeat ARQ. That is **3 protocols**.

(5e: "four protocols were defined traditionally: Simple, Stop-and-Wait, Go-Back-N, Selective-Repeat". The last two moved to chapter 23.)

**ARQ = Automatic Repeat reQuest:** detect, then resend.

**Sliding window:** with an m-bit sequence field, the numbers run 0 to 2^m - 1 and then wrap. The **send window** is the set of frames that may be outstanding (sent but not yet ACKed).

| | Stop-and-Wait ARQ | Go-Back-N ARQ | Selective Repeat ARQ |
|---|---|---|---|
| Send window | 1 | **at most 2^m - 1** | **at most 2^(m-1)** |
| Receive window | 1 | 1 | same as send window, 2^(m-1) |
| On a lost or bad frame | Resend that frame | Resend **that frame and all after it** | Resend **only that frame** |
| Out-of-order frames at receiver | n/a | Discarded | Buffered, delivered in order later |
| ACK | ACK = next expected | **Cumulative** ACK n = all frames before n are received | ACK for each frame, plus **NAK n** = frame n is missing |
| Best for | Short links | Low-error links (simple receiver) | Noisy links (efficient, complex receiver) |

Go-Back-N example (4e Ex 11.7): frames 0, 1, 2, 3 are sent and frame 1 is lost. The receiver discards 2 and 3 because they are out of order. The timer for 1 expires and the sender resends **1, 2, 3**. In Selective Repeat only **1** would be resent, and 2 and 3 would wait in the receiver's buffer.

Stop-and-Wait ARQ = Go-Back-N with m = 1 (window 1, sequence numbers mod 2).

### B3.8 Bandwidth-delay product and link utilization [4e Ex 11.4, 11.5]
- **Bandwidth-delay product = bandwidth x delay** = the number of bits that "fill the pipe". Use the **round-trip** time when asking how many bits the sender could send while waiting for an ACK.
- **Utilization of Stop-and-Wait = frame size / (bandwidth x RTT).**

4e Ex 11.4: 1 Mbps line, 20 ms round trip, so the product is 1,000,000 x 0.020 = **20,000 bits**. With 1000-bit frames in Stop-and-Wait, utilization = 1000 / 20,000 = **5%**.
4e Ex 11.5: if the protocol can have 15 frames outstanding, utilization = 15,000 / 20,000 = **75%**. That is why sliding windows (pipelining) exist.

### B3.9 HDLC (High-level Data Link Control)
- A **bit-oriented** protocol for **point-to-point and multipoint** links. It implements Stop-and-Wait (and, in 4e, the ARQ protocols). It is the ancestor of PPP and Ethernet framing.

**Transfer modes and configurations:**
- **NRM (Normal Response Mode):** an **unbalanced** configuration. One **primary** station sends **commands**. **Secondary** stations can only **respond**. It works point-to-point or multipoint.
- **ABM (Asynchronous Balanced Mode):** a **balanced** configuration, point-to-point. Each station is **combined**, meaning both primary and secondary (peers). This is the common mode today.
```
NRM point-to-point:   Primary --command--> Secondary
                      Primary <--response-- Secondary
NRM multipoint:       Primary --command--> Secondary, Secondary, ...
ABM:                  Combined <--command/response--> Combined
```

**HDLC frame (Fig 11.16):**
```
+----------+---------+---------+---------------------+----------+----------+
|   Flag   | Address | Control |  Information (data) |   FCS    |   Flag   |
| 01111110 | 1+ byte | 1-2 B   |  variable           | 2 or 4 B | 01111110 |
+----------+---------+---------+---------------------+----------+----------+
  I-frame: has user data (and may piggyback an ACK)
  S-frame: NO information field (flow/error control only)
  U-frame: has a management-information field (link setup/teardown)
```
- **Flag:** 01111110 at both ends. The ending flag of one frame can be the start flag of the next.
- **Address:** the secondary station's address ("to" if a primary sent the frame, "from" if a secondary sent it).
- **FCS (Frame Check Sequence):** a CRC-16 or CRC-32.

**Control field (8 bits, Fig 11.17):**
```
            bit:  1     2  3  4     5     6  7  8
I-frame:       |  0  |  N(S)     | P/F |  N(R)     |
S-frame:       |  1  0 |  code   | P/F |  N(R)     |
U-frame:       |  1  1 |  code   | P/F |  code (3) |
```
- **N(S):** the send sequence number (3 bits, 0 to 7). **N(R):** the receive number, meaning the ACK (next frame expected) or the NAK number.
- **P/F bit:** **Poll** when a primary sends it to a secondary. **Final** when a secondary sends it to a primary.
- **S-frame codes:** **00 RR** (Receive Ready = ACK). **10 RNR** (Receive Not Ready = ACK + "I'm busy, stop"). **01 REJ** (Reject = NAK, used by Go-Back-N). **11 SREJ** (Selective Reject = NAK, used by Selective Repeat).
- **U-frame:** 2 + 3 code bits allow up to 32 types. Examples: SABM (set ABM, connect), UA (unnumbered ACK), DISC (disconnect).
  Connection example (Forouzan Ex 11.5): A sends SABM, B replies UA, data is exchanged, A sends DISC, B replies UA.

### B3.10 PPP (Point-to-Point Protocol)
The most common protocol for **home-to-ISP** point-to-point links (dial-up, DSL).

**Provides:** a defined frame format, link negotiation (LCP), payloads from several network layers (multiplexing), optional **authentication** (PAP/CHAP), **network address configuration** (IPCP gives a home user a temporary IP), and **Multilink PPP**.
**Does NOT provide:** **flow control**. Error control is limited to **detection only** (CRC, then silently discard). There are no sequence numbers (frames can arrive out of order) and no multipoint addressing.

**PPP frame (byte-oriented, Fig 11.20):**
```
+----------+----------+----------+-----------+-----------------+---------+----------+
|   Flag   | Address  | Control  | Protocol  | Payload         |   FCS   |   Flag   |
| 01111110 | 11111111 | 00000011 | 1-2 bytes | variable,       | 2-4 B   | 01111110 |
|  1 byte  |  1 byte  |  1 byte  |           | max 1500 default|  (CRC)  |  1 byte  |
+----------+----------+----------+-----------+-----------------+---------+----------+
```
- **Address 11111111** is a broadcast address. It is constant because a point-to-point link has only one other end.
- **Control 00000011** imitates an HDLC U-frame. It is constant because there is no flow control.
- **Protocol** says what the payload is: 0xC021 = LCP, 0xC023 = PAP, 0xC223 = CHAP, 0x8021 = IPCP, 0x0021 = IP data.
- **Byte stuffing:** the escape byte is **01111101** (0x7D). It is stuffed before any flag-like or escape-like byte in the payload.

**Transition phases (FSM, Fig 11.21):**
```
            carrier detected            authentication needed
   [Dead] ------------------> [Establish] ------------------> [Authenticate]
     ^  ^                          |                            |         |
     |  | carrier detection        | no authentication          | success | failed
     |  +----- failed -------------+ needed                     v         |
     |                             +----------------------> [Network]     |
     |                                                          |         |
     |                                     network-layer config |         |
     | carrier dropped                                          v         |
   [Terminate] <---------------- done ------------------------ [Open]    |
        ^                                              (data transfer)    |
        +-----------------------------------------------------------------+
```
Dead (no carrier) -> **Establish** (LCP negotiates options) -> **Authenticate** (optional, PAP or CHAP) -> **Network** (NCP, for example IPCP, configures the network layer) -> **Open** (data transfer) -> **Terminate** -> Dead.

**Multiplexing:** one PPP link carries packets of **LCP** (link setup, maintenance, teardown), **AP** (PAP: 2-step, username + password sent in clear; CHAP: 3-way challenge-response, password never sent), and **NCPs** (one per network protocol, for example IPCP). Then it carries the actual data.

**HDLC vs PPP** in one line: HDLC is bit-oriented and multipoint-capable, with flow/error control through S-frames. PPP is byte-oriented and point-to-point only, has no flow control, adds authentication and network configuration, and has a fixed address and control field.

---

## B4. Formula and rules box
```
bit stuffing:   after 0 + five 1s (i.e. any 5 consecutive 1s in data) insert a 0
bit unstuffing: after five 1s in received data, delete the next bit (a 0)
byte stuffing:  put ESC before every FLAG or ESC byte in the data
byte unstuff:   delete an ESC, keep the next byte as plain data
flag (bit-oriented, HDLC, PPP) = 01111110       PPP escape = 01111101
Stop-and-Wait:  seq 0,1,0,1 (mod 2); ACK number = next frame expected
                frame 0 -> ACK 1, frame 1 -> ACK 0
m-bit sequence field: numbers 0 .. 2^m - 1
Go-Back-N:      send window <= 2^m - 1, receive window = 1
Selective Rep.: send window = receive window <= 2^(m-1)
bandwidth-delay product = bandwidth x delay (bits)
Stop-and-Wait utilization = frame bits / (bandwidth x RTT)
HDLC control: I = 0|N(S)|P/F|N(R)   S = 10|code|P/F|N(R)   U = 11|code|P/F|code
S codes: RR 00, REJ 01, RNR 10, SREJ 11
PPP: address 11111111, control 00000011, payload <= 1500 default, FCS 2-4 bytes
```

---

## B5. Worked past-paper solutions

### B5.1 [2016-17 Q3c(ii)] Stop-and-Wait flow diagram (6 marks)
Scenario: (1) Frame 0 is sent but lost. (2) Frame 0 is resent and acknowledged. (3) Frame 1 is sent and acknowledged, but the ACK is lost. (4) Frame 1 is resent and acknowledged.
(This is Forouzan P11-8.)

```
      SENDER                                              RECEIVER
   (Sn = next to send)                              (Rn = next expected)
        |                                                 |  Rn = 0
 start  |------ Frame 0 ------------X  (lost)             |
 timer  |                                                 |
        |                                                 |
 time-  |                                                 |
 out,   |------ Frame 0 (resent) ------------------------>|  seq 0 = Rn: accept,
 restart|                                                 |  deliver packet, Rn = 1
        |<------------------------------------- ACK 1 ----|
 stop   |                                                 |
 timer  |                                                 |
 start  |------ Frame 1 --------------------------------->|  seq 1 = Rn: accept,
 timer  |                                                 |  deliver packet, Rn = 0
        |          (lost)  X-------------------- ACK 0 ---|
        |                                                 |
 time-  |                                                 |
 out,   |------ Frame 1 (resent) ------------------------>|  seq 1 != Rn (0):
 restart|                                                 |  DUPLICATE, discard,
        |<------------------------------------- ACK 0 ----|  re-send ACK 0
 stop   |                                                 |
 timer  v                                                 v
      time                                              time
```
**Points to say in words (these earn the marks):**
- The sender keeps a copy of each frame until its ACK arrives. A timer is started for each send.
- A lost frame produces no ACK. The timer expires and the sender resends the same frame with the same sequence number.
- A lost ACK makes the sender resend frame 1. The receiver is expecting 0, so it recognises frame 1 as a **duplicate**, **discards** it (the packet is not delivered twice), and **re-sends ACK 0**.
- ACK numbers always name the **next frame expected**.

In the exam draw it with **slanted arrows** going down the page (time runs downward). A slanted arrow shows the propagation delay.

### B5.2 [2019-20 Q6c] Five-step version (5 marks)
(1) Frame 0 is sent but lost. (2) Frame 0 is resent and acknowledged. (3) Frame 1 is sent and acknowledged, but the ACK is lost. (4) **Frame 1 is resent, but it times out.** (5) Frame 1 is resent and acknowledged.
(Forouzan P11-7 has the same wording.)

The first three steps are the same as B5.1. Step 4 means the resent copy also gets no ACK in time. Draw the resent frame as lost. (Equally valid: it arrives, the receiver discards the duplicate and sends ACK 0, and that ACK is lost.)
```
      SENDER                                              RECEIVER
        |                                                 |  Rn = 0
 start  |------ Frame 0 ------------X  (lost)             |
 t-out  |------ Frame 0 (resent) ------------------------>|  accept, deliver, Rn = 1
        |<------------------------------------- ACK 1 ----|
 stop   |                                                 |
 start  |------ Frame 1 --------------------------------->|  accept, deliver, Rn = 0
        |          (lost)  X-------------------- ACK 0 ---|
 t-out  |------ Frame 1 (resent) -------X  (lost)         |   <- step 4: no ACK,
        |                                                 |      timer expires again
 t-out  |------ Frame 1 (resent again) ------------------>|  seq 1 != Rn: duplicate,
 restart|                                                 |  discard, re-send ACK 0
        |<------------------------------------- ACK 0 ----|
 stop   v                                                 v
```
**Key line:** each time-out causes the same frame, with the **same sequence number**, to be resent. The receiver delivers each packet **exactly once**.

### B5.3 Textbook timeline (Forouzan Ex 11.4, Fig 11.13), for practice
Frame 0 is ACKed (ACK 1). Frame 1 is lost, then resent and ACKed (ACK 0). Frame 0 is sent and ACKed, but ACK 1 is lost. Frame 0 is resent. The receiver expects 1, so it **discards** frame 0 and re-sends ACK 1.

### B5.4 [2014-15 Q3a, TT2 Q4b] Bit-oriented vs byte-oriented
**Definition:** a **bit-oriented protocol** treats the frame's data section as a **sequence of bits** with no character structure. It can carry text, graphics, audio or video. It marks frame boundaries with the flag **01111110** and keeps the data transparent with **bit stuffing**. **HDLC** is the standard example.

**Advantages for error handling, with an example:**
1. **Transparency at minimum cost.** If the data contains the flag pattern, only **one bit** is stuffed (01111110 becomes 011111010), not a whole byte. Fewer extra bits means less to corrupt and less overhead.
2. **No dependence on a character set.** Byte-oriented framing assumes 8-bit characters, so 16/32-bit Unicode or binary data breaks it. Bit-oriented framing works for any data.
3. **Built-in error and flow control (HDLC).** Every frame carries an **FCS (CRC-16/32)** that detects errors. **S-frames** report them: RR (ACK), REJ (go back and resend from N(R)), SREJ (resend only frame N(R)), RNR (stop sending). **Example:** node B gets I-frames 0 and 1, then frame 1 fails the CRC. B sends **REJ 1**, and A resends from frame 1 at once instead of waiting for a timeout (Forouzan Ex 11.6).
4. A corrupted byte-stuffed frame can lose its ESC/flag sync for a whole byte boundary. A bit-oriented receiver just hunts for the next 01111110.

| Byte-oriented | Bit-oriented |
|---|---|
| Data = 8-bit characters | Data = bits |
| Flag is a special byte; byte stuffing with ESC | Flag 01111110; bit stuffing |
| 1 extra byte per conflict | 1 extra bit per conflict |
| Clashes with Unicode | Any data |
| e.g. PPP | e.g. HDLC |

### B5.5 [2014-15 Q1b(v)] Meaning of ACK-3 and NAK-3
- **ACK 3:** a positive acknowledgment. It means "all frames up to and including 2 arrived safely, and **I am expecting frame 3** next". ACK numbers name the next frame expected. In Go-Back-N it is **cumulative**.
- **NAK 3:** a negative acknowledgment. It means "**frame 3 was lost or damaged, resend frame 3**". It is used in Selective Repeat ARQ (HDLC SREJ). An HDLC **REJ 3** means "go back and resend from frame 3".

### B5.6 [2015-16 Q4l] How many protocols does a noisy channel have?
**Three:** Stop-and-Wait ARQ, Go-Back-N ARQ, Selective Repeat ARQ. (A noiseless channel has two: Simplest and Stop-and-Wait.)

### B5.7 [2015-16 Q1g] Bits on a 10 Mbps link with 2 ms delay
Bandwidth-delay product = 10 x 10^6 bits/s x 2 x 10^-3 s = **20,000 bits**.

### B5.8 Bit stuffing worked both ways (Forouzan Fig 11.4, P11-3, P11-4)
**Method:** scan left to right and count consecutive 1s. When the count reaches 5, write an extra 0 and reset the count. Any 0 also resets the count.

**Fig 11.4, sender:**
```
data:     000 11111 1100 11111 01000
                   ^              ^      after each run of five 1s
stuffed:  000 11111 [0] 1100 11111 [0] 01000
        = 000111110110011111001000          (2 extra bits)
```
**Receiver:** after every five 1s, delete the next bit (it must be the stuffed 0). That gives back 0001111111001111101000.

**P11-3:** stuff `0001111111001111101000111111111110000111`.
```
000 11111[0] 1100 11111[0] 01000 11111[0] 11111[0] 10000111
= 00011111011001111100100011111011111010000111       (4 bits stuffed)
```
**P11-4:** unstuff `00011111000001111101110100111011111000001111`.
```
000 11111 (0) 0000 11111 (0) 1110100111 0 11111 (0) 00001111      (0) = removed
= 00011111000011111111010011101111100001111          (3 bits removed)
```
**Classic one-liner:** the flag-like pattern 01111110 inside the data becomes **011111010**.

### B5.9 Byte stuffing both ways (Forouzan P11-1, P11-2)
E = escape byte, F = flag byte, D = ordinary data byte.
**Stuff** `D E D D F D D E E D F D`: put an E before every E and every F.
```
D [E]E D D [E]F D D [E]E [E]E D [E]F D
= D E E D D E F D D E E E E D E F D
```
**Unstuff** `E E D E F D D E F E E D D D`: each E means "delete me, keep the next byte".
```
(E)E D (E)F D D (E)F (E)E D D D
= E D F D D F E D D D
```

---

## B6. Traps (Ch11)
1. **ACK number = NEXT frame expected**, not the frame just received. Frame 0 gets **ACK 1**.
2. In Stop-and-Wait the sequence numbers are only **0 and 1**. Do not write frame 2.
3. A **duplicate** frame is **discarded but still ACKed**. Forgetting the re-sent ACK loses marks, because without it the sender would loop forever.
4. A corrupted frame is **silently discarded**. In basic Stop-and-Wait the receiver does NOT send a NAK.
5. The timer is at the **sender only**. The receiver has no timer.
6. Bit stuffing: stuff after **five** 1s, not six. Stuff even if the next bit is 0. Never stuff the real flags.
7. When unstuffing, the receiver first finds the frame (flags), then removes the stuffed bits from the data.
8. Go-Back-N window **2^m - 1**, Selective Repeat **2^(m-1)**. Do not mix them up.
9. PPP has **no flow control**, and its error control is detection only.
10. HDLC **NRM = unbalanced** (primary/secondary). **ABM = balanced** (combined stations).
11. S-frames have **no information field**. U-frames do (management data).
12. Bandwidth-delay uses the **round trip** for utilization questions, but plain "delay" when asked how many bits fit on the link.

---

## B7. Doomsday box, Ch11 (memorize in 15 minutes)
```
* DLC = framing + flow control + error control (node-to-node)
* variable frames need FLAGS; flag = 01111110
* byte stuffing: ESC before FLAG/ESC in data (PPP, ESC = 01111101)
* bit stuffing: 0 after five 1s; 01111110 in data -> 011111010
* Stop-and-Wait: send 1 frame, keep copy, start timer, wait for ACK
     lost frame or lost ACK -> timeout -> resend same seq no.
     seq 0/1; ACK = next expected (F0->ACK1, F1->ACK0)
     duplicate -> discard + re-send ACK
* piggybacking = ACK rides inside a data frame going the other way
* noisy-channel protocols: Stop-and-Wait ARQ, Go-Back-N, Selective Repeat
     GBN window 2^m - 1 (resend all from lost one); SR 2^(m-1) (resend only lost)
* bandwidth-delay = bandwidth x delay; S&W utilization = frame / (BW x RTT)
* HDLC: bit-oriented; NRM (primary/secondary) vs ABM (combined)
     frame: Flag|Addr|Control|Info|FCS|Flag;  I(0..) S(10..) U(11..)
     S codes RR 00, REJ 01, RNR 10, SREJ 11
* PPP: byte-oriented; Flag|11111111|00000011|Protocol|Payload|FCS|Flag
     phases Dead->Establish->Authenticate->Network->Open->Terminate->Dead
     no flow control; LCP, PAP/CHAP, NCP (IPCP)
```

---
---

# PRACTICE SETS

## Practice: Chapter 10
1. Find d(01011, 11110).
2. (a) What d_min do you need to detect 3 errors? (b) To correct 2 errors? (c) A code has d_min = 5. How many errors can it detect, and how many can it correct?
3. Dataword 110101, divisor 1011. Find the CRC codeword by long division.
4. The receiver gets 1100100 with divisor 1011. Is there an error? Show the division.
5. Find the 4-bit one's complement checksum of 5, 9, 14, 3, and show the receiver's check.
6. Build the even-parity 2D table for the rows 1010110, 0110001, 1110000.
7. Find the Hamming code (position method, even parity) for the 4-bit data 1011.
8. (a) Write 1100101 as a polynomial. (b) Which generator guarantees catching all single-bit errors: x^3 + x + 1 or x^4 + x^2? Why?
9. What is the maximum number of bits a 2 ms noise burst can corrupt at 12 kbps?
10. Why can't simple parity detect a 2-bit error? Give an example.

## Practice: Chapter 11
1. Bit-stuff 0111111011111100.
2. Unstuff 0111110111110110.
3. Byte-stuff D F E D (F = flag, E = escape).
4. An HDLC control field is 10010011. What type of frame is it, what does it mean, and what is N(R)?
5. A 2 Mbps link has a 30 ms round-trip time and 1500-bit frames. Find the bandwidth-delay product and the Stop-and-Wait utilization. How many frames must be outstanding to fill the pipe?
6. The sequence field is m = 3 bits. Find the maximum send window for Go-Back-N and for Selective Repeat.
7. Go-Back-N: frames 0 to 6 are sent and the timer for frame 3 expires. Which frames are resent? What would Selective Repeat resend?
8. Draw Stop-and-Wait for: frame 0 sent and ACKed; frame 1 sent and corrupted; frame 1 resent and ACKed; frame 0 sent and ACKed.
9. Why is the PPP address field fixed at 11111111? Why is there no flow control?
10. In a bit-oriented protocol, do we remove the flags first or unstuff first?

---

# Answers

### Chapter 10 answers
1. 01011 XOR 11110 = 10101, so **d = 3**.
2. (a) d_min = 3 + 1 = **4**. (b) 2(2) + 1 = **5**. (c) It detects **4** and corrects **2**.
3. r = 3, so the dividend is 110101000.
   ```
    quotient: 111101
    110101000
    1011
    ----
     1100
     1011
     ----
      1111
      1011
      ----
       1000
       1011
       ----
        0110
        0000
        ----
         1100
         1011
         ----
          111   <- remainder
   ```
   **Codeword = 110101111.**
4. ```
    1100100
    1011
    ----
     1111
     1011
     ----
      1000
      1011
      ----
       0110
       0000
       ----
        110   <- syndrome non-zero
   ```
   **Error detected, discard.** (A valid codeword with the same first 4 bits is 1100010, which gives syndrome 000.)
5. 5 + 9 + 14 + 3 = 31 = 1 1111. Wrap: 1111 + 1 = 1 0000. Wrap again: 0000 + 1 = **0001**, so the sum is 1. **Checksum = 1110 = 14.** Receiver: 5 + 9 + 14 + 3 + 14 = 45 = 10 1101. Wrap: 1101 + 10 = 1111. Complement gives **0000**, so accept.
6. ```
     1 0 1 0 1 1 0 | 0
     0 1 1 0 0 0 1 | 1
     1 1 1 0 0 0 0 | 1
     --------------+--
     0 0 1 0 1 1 1 | 0
   ```
7. Positions 7 6 5 4 3 2 1 = d d d r4 d r2 r1, with data 1, 0, 1, ?, 1, ?, ?. r1 (3, 5, 7) = 1, 1, 1, so r1 = 1. r2 (3, 6, 7) = 1, 0, 1, so r2 = 0. r4 (5, 6, 7) = 1, 0, 1, so r4 = 0. **Codeword 1010101.**
8. (a) **x^6 + x^5 + x^2 + 1.** (b) **x^3 + x + 1**, because it has more than one term and its x^0 coefficient is 1. x^4 + x^2 has no x^0 term, so some single-bit errors divide evenly and are missed.
9. 12,000 x 0.002 = **24 bits**.
10. Two flips keep the count of 1s even, so the syndrome stays 0. Example: 10111 sent, 00110 received (r0 and a3 flipped). The syndrome is 0 and the wrong data 0011 is accepted.

### Chapter 11 answers
1. 0 11111 [0] 1 0 11111 [0] 1 0 0, so **011111010111110100**.
2. 0 11111 (0) 11111 (0) 110, so **01111111111110**.
3. **D E F E E D** (an ESC before F and an ESC before E).
4. The first bits are 10, so it is an **S-frame**. Code 01 = **REJ** (reject, a NAK for Go-Back-N). P/F = 0. **N(R) = 011 = 3**: resend starting from frame 3.
5. BDP = 2 x 10^6 x 0.030 = **60,000 bits**. Utilization = 1500 / 60,000 = **2.5%**. Frames needed = 60,000 / 1500 = **40**.
6. Go-Back-N: 2^3 - 1 = **7**. Selective Repeat: 2^2 = **4**.
7. Go-Back-N resends **3, 4, 5, 6**. Selective Repeat resends **only 3**.
8. Frame 0 goes out and is accepted (Rn becomes 1), and ACK 1 comes back. Frame 1 arrives corrupted, so the receiver silently discards it and sends no ACK. The sender's timer expires and frame 1 is resent. It is accepted (Rn becomes 0) and ACK 0 comes back. Frame 0 is accepted (Rn becomes 1) and ACK 1 comes back. Draw it with the timer start, stop and time-out marks.
9. A point-to-point link has only one other end, so no real address is needed. 11111111 is the broadcast address ("whoever is on the other end"). PPP was kept simple on purpose. The upper layers (for example TCP) handle flow control and lost data. PPP only detects errors with the CRC and silently discards bad frames.
10. **Remove the flags first.** Detecting the flags is how the receiver finds the frame boundaries. Then it unstuffs the data between them. (If it unstuffed first, the flag 01111110 itself would be altered.)
