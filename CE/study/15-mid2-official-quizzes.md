# Official Forouzan 5e chapter quizzes (Ch 5, 6, 7, 8, 10, 11)

Source: the McGraw-Hill companion site for this exact textbook edition,
https://highered.mheducation.com/sites/0073376221/sitemap.html

These are the publisher's own multiple-choice quizzes, 109 questions in total. The answer key was read from the
site's quiz page, then every answer was checked against the textbook. **Seven of the site's keys are wrong**, and
the key at the bottom of this file uses the corrected answers. Each fix is listed in the table just below, with the reason.

## How to use this

- Do one chapter's quiz straight after you study that chapter. It takes 10 to 15 minutes.
- Cover the key. Write your letters on paper. Then mark yourself against the key at the very bottom.
- Any question you miss, look it up in the chapter file named under its heading.
- These are the exact style of a 1-mark quiz question, so the quiz part of your exam should feel familiar.

## Where the site's answer key is wrong or the question is broken

| Question | Problem | Site's key | Use this | Why |
|---|---|---|---|---|
| Ch6 Q1 | WRONG KEY | D) PDM | A) FDM | The site says PDM, which the book never covers. FDM is the analog multiplexing technique. WDM is analog too, but only for light. |
| Ch7 Q6 | AMBIGUOUS | D) None of the choices are correct | D) None of the choices are correct | Badly written. Twisted-pair, coaxial and fiber are ALL guided, so all three are 'not unguided'. The site keys D. The teacher is unlikely to copy this one. |
| Ch7 Q12 | TYPO | C) fiber-optic | C) fiber-optic | 'TP' should be 'ST'. Fiber connectors are SC, ST and MT-RJ. The answer, fiber-optic, is right. |
| Ch7 Q13 | WRONG KEY | A) below | B) above | Infrared is 300 GHz to 400 THz. Microwaves are 1 to 300 GHz. So infrared is ABOVE microwave (Forouzan 7.3.3). |
| Ch8 Q1 | AMBIGUOUS | D) None of the choices are correct | D) None of the choices are correct | The book does not split circuit switching into categories. It says there are THREE switching methods overall: circuit, packet, message. The site keys 'None'. |
| Ch8 Q2 | WRONG KEY | B) three | A) two | Book, 8.1.1: packet switching has TWO subcategories, virtual-circuit and datagram. |
| Ch8 Q7 | WRONG KEY | C) three | A) one | Book, 8.3.1: a datagram network has no setup or teardown phase, only data transfer. That is one phase. The quiz's own Q13 agrees. |
| Ch8 Q8 | TYPO | C) three | C) three | 'virtual-switch' means virtual-circuit. Three phases: setup, data transfer, teardown. |
| Ch8 Q12 | WRONG KEY | B) changes at each switch | A) remains the same from the source to the destination | Book, 8.3.1: the destination address remains the same during the entire journey. It is the VCI that changes at each switch, in virtual-circuit networks. |
| Ch10 Q20 | WRONG KEY | C) both detect and correct | A) only detect | A checksum only DETECTS errors. Correcting needs a code like Hamming. |
| Ch11 Q16 | WRONG KEY | A) byte | B) bit | HDLC is BIT-oriented: flag 01111110 and bit stuffing. PPP is the byte-oriented one (Q17). |

---

## Chapter 5: Analog Transmission

Study file for this chapter: [11-ch5-6-analog-and-multiplexing.md](11-ch5-6-analog-and-multiplexing.md)

**1.** ASK, PSK, FSK, and QAM are examples of ________ conversion.

- A) digital-to-digital
- B) digital-to-analog
- C) analog-to-analog
- D) analog-to-digital

**2.** AM, FM, and PM are examples of ________ conversion.

- A) digital-to-digital
- B) digital-to-analog
- C) analog-to-analog
- D) analog-to-digital

**3.** In QAM, both ________ of a carrier frequency are varied.

- A) frequency and amplitude
- B) phase and frequency
- C) amplitude and phase
- D) None of the choices are correct

**4.** In ________, the amplitude of the carrier signal is varied to create signal elements. Both frequency and phase remain constant.

- A) ASK
- B) PSK
- C) FSK
- D) QAM

**5.** In _________, the frequency of the carrier signal is varied to represent data. Both peak amplitude and phase remain constant.

- A) ASK
- B) PSK
- C) FSK
- D) QAM

**6.** In ________, the phase of the carrier is varied to represent two or more different signal elements. Both peak amplitude and frequency remain constant.

- A) ASK
- B) PSK
- C) FSK
- D) QAM

**7.** Quadrature amplitude modulation (QAM) is a combination of ___________.

- A) ASK and FSK
- B) ASK and PSK
- C) PSK and FSK
- D) None of the choices are correct

**8.** ________ uses two carriers, one in-phase and the other quadrature.

- A) ASK
- B) PSK
- C) FSK
- D) QAM

**9.** How many carrier frequencies are used in BASK?

- A) 1
- B) 2
- C) 3
- D) None of the choices are correct

**10.** How many carrier frequencies are used in BFSK?

- A) 1
- B) 2
- C) 3
- D) None of the choices are correct

**11.** How many carrier frequencies are used in BPSK?

- A) 1
- B) 2
- C) 3
- D) None of the choices are correct

**12.** Which of the following is not an analog-to-analog conversion?

- A) AM
- B) PM
- C) FM
- D) QAM

**13.** In _____ transmission, the carrier signal is modulated so that its amplitude varies with the changing amplitudes of the modulating signal.

- A) AM
- B) PM
- C) FM
- D) None of the choices are correct

**14.** In the analog transmission of the digital signal, the baud rate is ___________ the bit rate.

- A) always less than
- B) less than or equal to
- C) always greater than
- D) is greater than or equal to

**15.** In ASK, the bandwidth is ________.

- A) less than the signal rate
- B) equal or greater than signal rate
- C) always equal to signal rate
- D) five times the signal rate

**16.** With the same signal rate, the bandwidth of FSK is normally ___________ the bandwidth for ASK.

- A) greater than
- B) less than
- C) equal to
- D) None of the choices are correct

**17.** The bandwidth of an AM signal is ______________ the bandwidth of the original analog signal.

- A) equal to
- B) two times
- C) three times
- D) None of the choices are correct

**18.** In AM radio, the allocated bandwidth for each station is ___________ kHz.

- A) 15
- B) 20
- C) 10
- D) None of the choices are correct

**19.** In FM radio, the allocated bandwidth for each station is ___________ kHz.

- A) 100
- B) 200
- C) 300
- D) None of the choices are correct

---

## Chapter 6: Bandwidth Utilization

Study file for this chapter: [11-ch5-6-analog-and-multiplexing.md](11-ch5-6-analog-and-multiplexing.md)

**1.** Which multiplexing technique is used for analog signals?

- A) FDM
- B) TDM
- C) WDM
- D) PDM

**2.** Which multiplexing technique is used for digital signals?

- A) FDM
- B) TDM
- C) WDM
- D) PDM

**3.** Which multiplexing technique shifts each signal to a different carrier frequency?

- A) FDM
- B) TDM
- C) WDM
- D) PDM

**4.** Which multiplexing technique involves signals composed of light beams?

- A) FDM
- B) TDM
- C) WDM
- D) PDM

**5.** ________ is the set of techniques that allows the simultaneous transmission of multiple signals across a single data link.

- A) Demodulating
- B) Multiplexing
- C) Compressing
- D) None of the choices are correct

**6.** ____ is designed to use the high bandwidth capability of fiber-optic cable.

- A) FDM
- B) TDM
- C) WDM
- D) None of the choices are correct

**7.** ______ is an analog multiplexing technique to combine optical signals.

- A) FDM
- B) TDM
- C) WDM
- D) None of the choices are correct

**8.** _____ is a digital process that allows several connections to share the high bandwidth of a link.

- A) FDM
- B) TDM
- C) WDM
- D) None of the choices are correct

**9.** We can divide ____ into two different schemes: synchronous or statistical.

- A) FDM
- B) TDM
- C) WDM
- D) None of the choices are correct

**10.** In ________ TDM, each input connection has an allotment in the output even if it is not sending data.

- A) synchronous
- B) statistical
- C) isochronous
- D) None of the choices are correct

**11.** In ________ TDM, slots are dynamically allocated to improve bandwidth efficiency.

- A) synchronous
- B) statistical
- C) isochronous
- D) None of the choices are correct

**12.** The _______ technique uses M different carrier frequencies that are modulated by the source signal. At one moment, the signal modulates one carrier frequency; at the next moment, the signal modulates another carrier frequency.

- A) FDM
- B) DSSS
- C) FHSS
- D) TDM

**13.** The ______ technique expands the bandwidth of a signal by replacing each data bit with n bits using a spreading code.

- A) FDM
- B) DSSS
- C) FHSS
- D) TDM

**14.** Groups, super groups, master groups, and jumbo groups are terms used in ______________.

- A) FDM
- B) DSSS
- C) FHSS
- D) TDM

**15.** Multilevel multiplexing is a strategy used in ___________.

- A) FDM
- B) DSSS
- C) FHSS
- D) TDM

**16.** Multislot allocation is a strategy used in ___________.

- A) FDM
- B) DSSS
- C) FHSS
- D) TDM

**17.** Pulse stuffing is a strategy used in ___________.

- A) FDM
- B) DSSS
- C) FHSS
- D) TDM

**18.** Frame synchronization is a strategy used in ___________.

- A) FDM
- B) DSSS
- C) FHSS
- D) TDM

**19.** A T-1 line uses ___________ frames.

- A) 6000
- B) 8000
- C) 10000
- D) 12000

**20.** We need addressing mechanism in ___________ TDM.

- A) synchronous
- B) statistical
- C) both synchronous and statistical
- D) None of the above choices are correct

---

## Chapter 7: Transmission Media

Study file for this chapter: [12-ch7-8-media-and-switching.md](12-ch7-8-media-and-switching.md)

**1.** Transmission media are usually categorized as _______.

- A) fixed or unfixed
- B) guided or unguided
- C) determinate or indeterminate
- D) metallic or nonmetallic

**2.** Transmission media lie below the _______ layer.

- A) physical
- B) network
- C) transport
- D) application

**3.** _______ cable consists of an inner copper core and a second conducting outer sheath.

- A) Twisted-pair
- B) Coaxial
- C) Fiber-optic
- D) Shielded twisted-pair

**4.** In fiber optics, the signal is _______ waves.

- A) light
- B) radio
- C) infrared
- D) very low-frequency

**5.** Which of the following is not a guided medium?

- A) twisted-pair cable
- B) coaxial cable
- C) fiber-optic cable
- D) atmosphere

**6.** Which of the following is not an unguided medium?

- A) twisted-pair cable
- B) coaxial cable
- C) fiber-optic cable
- D) None of the choices are correct

**7.** Twisting in a twisted-pair help reduce the __________.

- A) length
- B) cost
- C) noise
- D) None of the choices are correct

**8.** Noise in a coaxial cable is reduced by ___________________.

- A) twisting the cable
- B) the outer conductor
- C) the inner conductor
- D) None of the choices are correct

**9.** UTP and STP are different implementations of ___________________ cable.

- A) twisted-pair
- B) coaxial
- C) fiber-optic
- D) None of the choices are correct

**10.** RJ-45 is a type of connectors used in _________ cabling.

- A) twisted-pair
- B) coaxial
- C) fiber-optic
- D) None of the choices are correct

**11.** RG rating is used in _________ cable.

- A) twisted-pair
- B) coaxial
- C) fiber-optic
- D) None of the choices are correct

**12.** SC and TP are two types of connectors used in _________ cabling.

- A) twisted-pair
- B) coaxial
- C) fiber-optic
- D) None of the choices are correct

**13.** The infrared wave has frequencies ________ microwave.

- A) below
- B) above
- C) the same as
- D) None of the choices are correct

**14.** BNC is a type of connectors used in _________ cabling.

- A) twisted-pair
- B) coaxial
- C) fiber-optic
- D) None of the choices are correct

---

## Chapter 8: Switching

Study file for this chapter: [12-ch7-8-media-and-switching.md](12-ch7-8-media-and-switching.md)

**1.** Circuit switching can be divided into ________ categories.

- A) two
- B) three
- C) four
- D) None of the choices are correct

**2.** Packet switching can be divided into ________ categories.

- A) two
- B) three
- C) four
- D) None of the choices are correct

**3.** Circuit switching is normally used in ___________ layer.

- A) physical
- B) data-link
- C) network
- D) application

**4.** Packet switching is normally used in ___________ layers.

- A) physical and data-link
- B) data-link and network
- C) network and transport
- D) transport and application

**5.** Message switching is normally used in ___________ layer.

- A) physical
- B) data-link
- C) network
- D) application

**6.** In a circuit-switching network, we have ___________ phase(s).

- A) one
- B) two
- C) three
- D) None of the choices are correct

**7.** In a datagram network, we have ___________ phase(s).

- A) one
- B) two
- C) three
- D) None of the choices are correct

**8.** In a virtual-switch network, we have ___________ phase(s).

- A) one
- B) two
- C) three
- D) None of the choices are correct

**9.** In a ___________ network, each packet is treated independently from all other packets.

- A) circuit-switched
- B) virtual-circuit
- C) datagram
- D) None of the choices are correct

**10.** In a datagram network, the routing table is based on the ___________ in the packet.

- A) flow label
- B) destination address
- C) VCI
- D) None of the choices are correct

**11.** In a virtual-circuit network, the routing table is based on the ___________ in the packet.

- A) flow label
- B) destination address
- C) VCI
- D) None of the choices are correct

**12.** In a datagram network, the destination address ________________________.

- A) remains the same from the source to the destination
- B) changes at each switch
- C) changes at the destination
- D) None of the choices are correct

**13.** In a datagram network, we need ______________ phase(s).

- A) tear-down
- B) setup
- C) setup and tear-down
- D) None of the choices are correct

**14.** In a virtual-circuit network, we need ______________ phase(s).

- A) tear-down
- B) setup
- C) setup and tear-down
- D) None of the choices are correct

**15.** In a __________network, all packets in a message follow the same path.

- A) datagram
- B) virtual-circuit
- C) circuit-switched
- D) None of the choices are correct

**16.** In a __________network, each packet in a message may follow a different path.

- A) datagram
- B) virtual-circuit
- C) circuit-switched
- D) None of the choices are correct

---

## Chapter 10: Error Detection and Correction

Study file for this chapter: [13-ch10-11-errors-and-dlc.md](13-ch10-11-errors-and-dlc.md)

**1.** Which of the following best describes a single-bit error?

- A) A single bit is inverted
- B) A single bit per transmission is inverted
- C) A single bit per data unit is inverted
- D) All of the choices are correct

**2.** Which error detection method uses one's complement arithmetic?

- A) Simple parity check
- B) Checksum
- C) Two-dimensional parity check
- D) CRC

**3.** Which error detection method consists of just one redundant bit per data unit?

- A) Two-dimensional parity check
- B) CRC
- C) Simple parity check
- D) Checksum

**4.** Which error detection method involves polynomials?

- A) CRC
- B) Simple parity check
- C) Two-dimensional parity check
- D) Checksum

**5.** If the ASCII character G is sent and the character D is received, what type of error is this?

- A) Single-bit
- B) Multiple-bit
- C) Burst
- D) Recoverable

**6.** If the ASCII character H is sent and the character L is received, what type of error is this?

- A) Burst
- B) Recoverable
- C) Single-bit
- D) Multiple-bit

**7.** In cyclic redundancy checking, what forms the check bits?

- A) The remainder
- B) The divisor
- C) The quotient
- D) The dividend

**8.** In CRC, if the dataword is 111111, the divisor 1010, and the remainder 110, what is the codeword at the receiver?

- A) 111111011
- B) 1010110
- C) 111111110
- D) 110111111

**9.** In CRC, if the dataword is 111111 and the divisor 1010, what is the dividend at the sender?

- A) 1111110000
- B) 111111000
- C) 111111
- D) 1111111010

**10.** At the CRC generator, _______ is (are) added to the dataword after the division process to create the codeword.

- A) 0’s
- B) 1’s
- C) the remainder
- D) the divisor

**11.** The sum of the checksum and data at the receiver is _______ if no error is detected.

- A) − 0
- B) + 0
- C) the complement of the checksum
- D) the complement of the dataword

**12.** In CRC, the quotient at the sender _______.

- A) becomes the dividend at the receiver
- B) becomes the divisor at the receiver
- C) is the remainder
- D) is discarded

**13.** At the CRC checker, _______ means that the dataword is damaged.

- A) a string of alternating 1s and 0s
- B) a nonzero remainder
- C) a string of 0s
- D) None of the choices are correct

**14.** A codeword of 10 bits has only four 0s, how many terms are in the polynomial representation of this code?

- A) 4
- B) 6
- C) 8
- D) None of the choices are correct

**15.** In CRC, if the remainder is only three bits, the divisor should be __________ bits.

- A) 3
- B) 2
- C) 4
- D) None of the choices are correct

**16.** How many bits are in the divisor if we use CRC-8?

- A) 9
- B) 8
- C) 10
- D) None of the choices are correct

**17.** Checksum uses ____________ addition.

- A) one’s complement
- B) two’s complement
- C) three’s complement
- D) None of the choices are correct

**18.** To detect five errors, the Hamming distance between each pair of codewords should be at least_________.

- A) 5
- B) 6
- C) 11
- D) None of the choices are correct

**19.** To correct five errors, the Hamming distance between each pair of codewords should be at least_________.

- A) 5
- B) 6
- C) 11
- D) None of the choices are correct

**20.** A checksum can _________ errors.

- A) only detect
- B) only correct
- C) both detect and correct
- D) None of the choices are correct

---

## Chapter 11: Data Link Control

Study file for this chapter: [13-ch10-11-errors-and-dlc.md](13-ch10-11-errors-and-dlc.md)

**1.** HDLC is an acronym for _______.

- A) High-Duplex Line Communication
- B) Half-Duplex Link Combination
- C) High-Level Data Link Control
- D) Host Double-Level Circuit

**2.** The shortest frame in HDLC protocol is usually the _______ frame.

- A) information
- B) management
- C) supervisory
- D) None of the choices are correct

**3.** The address field of a frame in HDLC protocol contains the address of the _______ station.

- A) primary
- B) secondary
- C) tertiary
- D) primary or secondary

**4.** The HDLC _______ field defines the beginning and end of a frame.

- A) control
- B) flag
- C) FCS
- D) None of the choices are correct

**5.** What is present in all HDLC control fields?

- A) N(R)
- B) N(S)
- C) Code bits
- D) P/F bit

**6.** According to the PPP transition-phase diagram, options are negotiated in the _______ state.

- A) networking
- B) terminating
- C) establishing
- D) authenticating

**7.** According to the PPP transition-phase diagram, verification of user identification occurs in the _______ state.

- A) networking
- B) terminating
- C) establishing
- D) authenticating

**8.** In the PPP frame, the _______ field defines the contents of the data field.

- A) FCS
- B) flag
- C) control
- D) protocol

**9.** In the PPP frame, the _______ field is similar to that of the U-frame in HDLC.

- A) flag
- B) protocol
- C) FCS
- D) control

**10.** In the PPP frame, the _______ field has a value of 11111111 to indicate the broadcast address of HDLC.

- A) protocol
- B) address
- C) control
- D) FCS

**11.** In PPP, what is the purpose of LCP packets?

- A) Configuration
- B) Termination
- C) Option negotiation
- D) All of the choices are correct

**12.** In the PPP frame, the _______ field is for error control.

- A) FCS
- B) flag
- C) control
- D) protocol

**13.** For CHAP authentication, the user takes the system’s _______ and its own _______ to create a result that is then sent to the system.

- A) authentication identification; password
- B) password; authentication identification
- C) challenge value; password
- D) password; challenge value

**14.** In byte stuffing, we need sometimes to add a (an) ___________ in the payload.

- A) flag byte
- B) ESC byte
- C) null byte
- D) None of the choices are correct

**15.** In bit stuffing, we sometimes need to add an extra ___________ bit in the payload.

- A) 0’s
- B) 1’s
- C) 0’s or 1’s
- D) None of the choices are correct

**16.** HDLC is a ________oriented protocol

- A) byte
- B) bit
- C) byte or bit
- D) None of the choices are correct

**17.** PPP is a ________ oriented protocol

- A) byte
- B) bit
- C) byte or bit
- D) None of the choices are correct

**18.** In PPP, the address field defines ___________ of the packet.

- A) the sender
- B) the receiver
- C) either the sender or the receiver
- D) None of the choices are correct

**19.** In PPP, the ___________ field defines the type of payload encapsulated in the frame.

- A) address
- B) control
- C) protocol
- D) None of the choices are correct

**20.** In PPP, the CHAP protocol uses ____________ steps to authenticate the parties in communication.

- A) one
- B) two
- C) three
- D) None of the choices are correct

---

# Answer key

A **bold** letter means the site's own key was wrong and this is the corrected answer. A letter with * means the question is ambiguous or has a typo, so read its row in the table at the top.

**Chapter 5: Analog Transmission**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ans | B | C | C | A | C | B | B | D | A | B | A | D | A | B | B | A | B | C | B |

**Chapter 6: Bandwidth Utilization**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ans | **A** | B | A | C | B | C | C | B | B | A | B | C | B | A | D | D | D | D | B | B |

**Chapter 7: Transmission Media**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ans | B | A | B | A | D | D* | C | B | A | A | B | C* | **B** | B |

**Chapter 8: Switching**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ans | D* | **A** | A | B | D | C | **A** | C* | C | B | C | **A** | D | C | B | A |

**Chapter 10: Error Detection and Correction**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ans | C | B | C | A | C | C | A | C | B | C | A | D | B | B | C | A | A | B | C | **A** |

**Chapter 11: Data Link Control**

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ans | C | C | B | B | D | C | D | D | D | B | D | A | C | B | A | **B** | A | D | C | C |

