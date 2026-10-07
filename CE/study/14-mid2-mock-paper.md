# Mock Mid-term 2 (built only from real past questions)

```
                    Shahjalal University of Science and Technology
                  Department of Computer Science and Engineering
                     CSE 365 — Communication Engineering
                       Term Test 2 (MOCK)  —  Ch 5, 6, 7, 8, 10, 11

   Time: 60 minutes  (Part A 45 min + Part B 15 min)          Total Marks: 30
   Write your answers on blank paper. No notes. Calculator allowed.
```

Rules for yourself: start a timer. When it rings, pens down. Mark it afterwards with the chapter files.

---

## Part A — Answer ALL questions (20 marks, 45 min)

| No. | Question | Marks |
|---|---|---|
| 1 | An analog signal has a bit rate of 8000 bps and a baud rate of 1000 baud. How many data elements are carried by each signal element? How many signal elements do we need? | 2 |
| 2 | Draw the constellation diagram for the following: <br> i) BPSK, with a peak amplitude value of 3 <br> ii) 8-QAM with two different peak amplitude values, 1 and 3, and four different phases <br> iii) Four points at (2, 2), (−2, 2), (−2, −2), and (2, −2). Find the peak amplitude value and define the type of modulation. *(the numbers in parentheses are the I and Q values)* | 3 |
| 3 | Modulating signal: one slow sine wave (rises to a broad peak, then falls to a trough), as in the figure. Choose carrier frequency and draw the corresponding AM modulated signal. Then do the same for FM. *(draw the modulating signal yourself first — about one cycle across the page)* | 2 |
| 4 | a. Assume that a voice channel occupies a bandwidth of 4 kHz. We need to multiplex 3 voice channels with guard bands of 500 Hz using FDM. Calculate the required bandwidth. <br> b. Draw the bandwidth for 4.a if the starting frequency of the medium is 1 kHz. | 2 |
| 5 | Four 1 Mbps input lines are multiplexed in a synchronous TDM. The unit of data is 1 bit. Find <br> i) The input bit duration <br> ii) The output bit duration <br> iii) The output bit rate <br> iv) The output frame rate | 2 |
| 6 | Given the dataword 10100111 and the divisor 10111, show the generation of the CRC codeword at the sender site (using binary division). Then show the checking at the receiver site assuming no error has occurred. | 3 |
| 7 | a. What is the minimum Hamming distance? If we want to be able to detect two-bit errors, what should be the minimum Hamming distance? <br> b. What is the Minimum Hamming Distance of the following codebook: 00000, 00010, 00111, 10011, 11011 | 2 |
| 8 | Draw the flow diagram of the Stop and Wait Protocol with Sequence Number and Acknowledgment numbers using the following scenario: <br> i) Frame 0 is sent, but lost. <br> ii) Frame 0 is resent and acknowledged. <br> iii) Frame 1 is sent and acknowledged, but the acknowledgment is lost. <br> iv) Frame 1 is resent, but it is timed-out. <br> v) Frame 1 is resent and acknowledged. | 2 |
| 9 | We need a three-stage space-division switch with N = 100. We use 10 crossbars at the first and third stages and 4 crossbars at the middle stage. <br> i) Draw the configuration diagram. <br> ii) Calculate the total number of crosspoints. | 2 |
| | **Total Part A** | **20** |

---

## Part B — Quiz: answer any TEN (10 × 1 = 10 marks, 15 min)

| No. | Question | Marks |
|---|---|---|
| a | What is multiplexing and why is it necessary? | 1 |
| b | Why is statistical TDM better than synchronous TDM? | 1 |
| c | Write one difference between FHSS and DSSS. | 1 |
| d | What is Pulse Stuffing? | 1 |
| e | Which of the four digital-to-analog conversion techniques (ASK, FSK, PSK, or QAM) is the most susceptible to noise? Defend your answer. | 1 |
| f | What is the number of bits per baud for QAM with a constellation of 128 points? | 1 |
| g | What is the purpose of cladding in an optical fiber? | 1 |
| h | What is the difference between STP and UTP? | 1 |
| i | How does guided media differ from unguided media? | 1 |
| j | What is VCI? | 1 |
| k | What is the polynomial representation of 10110011? | 1 |
| l | Assuming even parity, find the parity bit for 11001100. | 1 |
| m | Explain why flags are needed when we use variable-size frames. | 1 |
| n | Compare and contrast byte-oriented and bit-oriented protocols. | 1 |
| | **Total Part B** | **10** |

---

### Where each question came from, and which file has the answer

| Mock Q | Real source | Answer is in |
|---|---|---|
| A1 | TT2-25 Q8 = F20 Q5c = F15 Q5c (Example 5.2) | `11-ch5-6-analog-and-multiplexing.md` |
| A2 | F17 Q2c (i, ii) + TT2-25 Q5c (P5-4, P5-5) | `11-ch5-6-analog-and-multiplexing.md` |
| A3 | TT2-25 Q1 + Q2 | `11-ch5-6-analog-and-multiplexing.md` |
| A4 | TT2-25 Q6a, 6b (P6-1) | `11-ch5-6-analog-and-multiplexing.md` |
| A5 | F20 Q3a (Example 6.6), TT1 Q3 | `11-ch5-6-analog-and-multiplexing.md` |
| A6 | F17 Q6b(ii) + F16 Q6d(ii) | `13-ch10-11-errors-and-dlc.md` |
| A7 | F17 Q6b(i) = F20 Q2e; F16 Q5e | `13-ch10-11-errors-and-dlc.md` |
| A8 | F20 Q6c (≈ F17 Q3c, P11-8) | `13-ch10-11-errors-and-dlc.md` |
| A9 | F20 Q2f = F17 Q3b (P8-12) | `12-ch7-8-media-and-switching.md` |
| B a–f | F15 Q4f / F16 Q4i; F16 Q5a / F19 Q4e; F20 Q1f; F20 Q4c; F20 Q4d; F17 Q5f(iv) | `11-ch5-6-analog-and-multiplexing.md` |
| B g–i | F17 Q4g; F20 Q4a; F17 Q1e | `12-ch7-8-media-and-switching.md` |
| B j | F16 Q4g | `12-ch7-8-media-and-switching.md` |
| B k–l | F20 Q4h; F20 Q5f | `13-ch10-11-errors-and-dlc.md` |
| B m–n | TT2-old Q4a, Q4b (Q11-2, Q11-4) | `13-ch10-11-errors-and-dlc.md` |

Source tags (TT2-25, F17, etc.) are explained in `10-mid2-battle-plan.md`, Section 4.
