# Comp Archi — Battle Plan (TT2 midterm 11 AM + Ch 7 quiz)

Textbook = Patterson & Hennessy, *Computer Organization and Design*, **4th ed** (`Resources/MK...pdf`).
Book page = PDF page − 27 (book p.457 is PDF p.484).

| Exam | Syllabus | Notes file | Drills |
|---|---|---|---|
| **Midterm (TT2)** | 5.1 Intro, 5.2 Caches (incl. writes), 5.3 Cache performance, 5.4 Virtual memory | `01-ch5-caches.md`, `02-ch5-virtual-memory.md` | `practice/drill1`–`drill7` |
| **Quiz** | All of Ch 7 (7.1–7.13) | `03-ch7-quiz.md` | `practice/drill8_ch7_numbers.py` |
| Both | Trick questions (small print, elaborations, Check Yourself) | `04-trick-bank.md` | self-test |

---

## What the past papers say (read this once)

The examiner changed ~2 years ago, so I weighted papers by how recent they are:

| Paper | Likely examiner | What it asked from our syllabus |
|---|---|---|
| **TT2 2025** (`Term Test/TT2.pdf`) | **current** | (a) spatial vs temporal locality, (b) advantages of fully associative over direct mapped, (2) **the textbook's Fig 5.6 cache table, 3 reads, show final state + explain** (6 of 10 marks) |
| **TT2 2026** (`Tt/IMG_6138`) | **current** | IEEE-754 (old syllabus) + **"What is SIMD, why do GPUs / AI coprocessors use it?"** (Ch 7!) |
| TT1 2025 / 2026 | current | Short definitions: buses, CISC/RISC, PC, endianness, heap, Von Neumann vs Harvard |
| Final Jun 2024 (2020-21 session) | probably the old examiner | write-allocate hit/miss counting, split vs unified AMAT, 64-bit tag/index/offset trace, VIPT size, 48-bit VA page table, TLB, multi-level page table |
| Final 2024 (2021-22 session) | probably the old examiner | 4-way index size, set-assoc definition, tag/index/offset trace, write-allocate counting, why write-through pairs with no-write-allocate |

**What this tells us about the current examiner:**
1. **Format:** 30 min, 10 marks. Two short 2-mark "explain/differentiate" questions, then one 6-mark worked problem.
2. **The worked problem is copied from the textbook.** TT2-2025 Q2 *is* Fig 5.6 (same addresses, same table). So every worked EXAMPLE in 5.1–5.4 is a candidate. They're all in `01`/`02` with answers.
3. **He likes "why" questions with a modern twist** (GPUs/AI → SIMD). For Ch 7, expect "why does X use Y".
4. Don't count on repeats. Count on the **same type**: definition, difference, or a textbook trace or calculation.

---

## Priority list (if you only get through the top N, take the top N)

### Midterm (Ch 5)
1. **Tag / index / offset splitting**, plus a **direct-mapped trace with a table** (Fig 5.6 style). This is the 6-mark question. → drill1, drill2
2. **Locality**: temporal vs spatial, definitions + example (loops = temporal, arrays/sequential instructions = spatial).
3. **DM vs set-assoc vs fully assoc**: where block 12 goes, the 0-8-0-6-8 example, pros/cons. → drill3
4. **Write-through vs write-back, write-allocate vs no-write-allocate, write buffer.** → drill6
5. **CPI with stalls / AMAT / multilevel cache** numbers. → drill5
6. **VM:** page fault, page table, TLB, why write-back, why fully associative, page-table size calc, the 7-combo table (Fig 5.26). → drill7
7. Bits in a cache (147 Kbits) and tag bits vs associativity (64K/68K/72K/112K). → drill4

### Quiz (Ch 7)
1. Flynn: SISD/SIMD/MISD/MIMD with the book's examples, plus SPMD and Vector
2. SIMD and why GPUs use it; vector vs scalar advantages
3. Multithreading: fine vs coarse vs SMT (pros/cons + issue-slot picture)
4. Shared memory (UMA/NUMA, locks) vs message passing / clusters
5. Amdahl numbers: 0.1% sequential; 10 vs 100 processors; load balancing 48 / 20; strong vs weak scaling
6. GPUs (warp, SIMT, CUDA), network topologies (bisection bandwidth), roofline formula, fallacies

---

## Schedule (7 h, starting now)

| Time | Do |
|---|---|
| 0:00–0:10 | This file. Open `04-trick-bank.md` once just to see what kind of questions are in it |
| 0:10–1:40 | `01-ch5-caches.md`, then **drill1 → drill2 → drill3** (run each, fix FAILs) |
| 1:40–2:20 | `01` writes + performance section, then **drill5, drill6, drill4** |
| 2:20–3:10 | `02-ch5-virtual-memory.md`, then **drill7** |
| 3:10–3:20 | Break. Walk. Water. |
| 3:20–4:40 | `03-ch7-quiz.md`, then **drill8** |
| 4:40–5:30 | `04-trick-bank.md`: cover the answers, say each out loud, mark the ones you miss |
| 5:30–6:15 | Sleep 40 min if you can. Seriously. A 40-min nap beats 40 more minutes of reading at 5 AM |
| 6:15–6:45 | Re-do only the drills you FAILed + your marked trick questions |
| 6:45–7:00 | Doomsday list below. Leave. |

Run a drill: `python CA/practice/drill1_address_split.py` from the `datacomm` folder (or `python practice/drill1_address_split.py` from `CA`).

---

## Doomsday list: the fewest things that still earn marks

If you wake up at 10:15 having slept through everything, learn just these:

1. **Temporal** = same item again soon (loops). **Spatial** = nearby items soon (arrays, sequential code).
2. **DM index = (block address) mod (#blocks)**. **Set = (block address) mod (#sets)**. Block address = ⌊byte address / bytes per block⌋.
3. Address = **[ tag | index | offset ]**. offset = log2(block bytes), index = log2(#sets), tag = the rest.
4. Trace table: for each address, find the index. If valid and tag matches → **hit**. Otherwise **miss**: write V=Y, the new tag and Memory(addr). Always say "replaces X" when evicting.
5. **AMAT = hit time + miss rate × miss penalty.** **CPI = base CPI + misses/instr × penalty** (count I-fetch misses for every instruction + data misses × load/store fraction).
6. **Write-through** updates cache and memory (use a write buffer). **Write-back** updates only the cache, writes memory on replacement (dirty bit). **VM is always write-back.**
7. **Fully assoc advantage:** fewest conflict misses, block can go anywhere. **Cost:** a comparator per entry, slower and more power-hungry.
8. **TLB** = a cache of page-table entries. **Page fault** = page not in memory (valid bit off), OS handles it, millions of cycles.
9. **SIMD** = one instruction, many data elements (data-level parallelism). GPUs use it because pixels and tensors are the same op on lots of independent data. That amortises fetch/decode/control over many ALUs, which is power-efficient.
10. **Fine MT** switches every cycle. **Coarse MT** switches only on long stalls. **SMT** issues from several threads in the same cycle.
