# Chapter 7, gently 🌱

### Parallel hardware, for the CSE 329 final

> You haven't read this chapter. That's okay.
> It's one short story, and the final only ever asks about six things from it.
> We'll do them one at a time, with breaks in between.

**Time:** about 4 hours, breaks included.

**How:** do one session, answer its checkpoint on paper, take the break, then move on. Answers are folded; click the little arrow to open them (preview with `Ctrl+Shift+V`).

**Book:** Patterson & Hennessy 4e, Chapter 7 (book pages 632–660). In the course this is **Lecture 9**.

---

## 🗺️ The map

| # | Session | Time | What it can earn you |
|---|---|---|---|
| 1 | Why multicore happened | 15 min | warm-up + 2-mark definitions |
| 2 | Amdahl's law | 45 min | a 5-mark numerical (in **both** 2024 finals) |
| 3 | Flynn's taxonomy ⭐ | 60 min | 2, 5 or 10 marks (in **every** recent final) |
| 4 | SIMD, vectors, GPUs | 40 min | 5-mark "why" questions |
| 5 | Multithreading | 30 min | a 2-mark hyper-threading question |
| 6 | Shared memory vs message passing | 25 min | a likely 5-mark "differentiate" |
| 7 | Mini mock | 30 min | proof you're ready |

**Short on time?** Do Session 3, then Session 2. They carry the most marks.

**Skipped on purpose:** network topologies, benchmarks, the roofline model, the "real chips" section. They're not in the lecture and no paper has ever asked them.

---

## Session 1 · Why multicore happened (15 min)

### 🎬 The picture

For years, chips got faster by ticking faster: a higher clock rate.

Around 2004 that stopped working. A faster clock made the chip too hot to cool. This wall is called the **power wall**.

Chip makers still got more transistors every year. So instead of building one faster brain, they put **several brains on one chip**. Each brain is a **core**, and the chip is a **multicore** processor.

The catch: a program only gets faster if it is split into parts that run at the same time. Splitting is hard. The rest of the chapter is about that.

### 💡 Words to know

- **Multiprocessor**: a computer with at least two processors.
- **Multicore**: several processors ("cores") on one chip.
- **Cluster**: many whole computers on a network (a LAN) acting as one big machine.
- **Job-level parallelism**: separate, independent programs running at the same time.
- **Parallel processing program**: one program running on many processors at once.

### 💡 Why bother with many processors?

1. **Power**: many small cores do more work per watt than one huge core.
2. **Scaling**: buy more processors, get more performance.
3. **Availability**: if one of n processors dies, the other n − 1 keep working.

### 💡 Why parallel programs are hard

Picture 8 reporters writing one news story together. They must:

- decide who writes which part (**scheduling**),
- give everyone a fair share (**load balancing**),
- wait for each other (**synchronization**),
- and talk to each other (**communication**).

All four eat time, and it gets worse with more reporters. Then there's Amdahl's law, which is the next session.

### ✅ Checkpoint 1

1. Why did chips switch to multicore?
2. Name the four problems in the 8-reporters story.
3. True or false: "To benefit from a multiprocessor, an application must be concurrent."

<details><summary>Answers</summary>

1. The power wall. Raising the clock rate made chips too hot, so the extra transistors became extra cores.
2. Scheduling, load balancing, synchronization, communication.
3. False. Several ordinary programs can simply run side by side (job-level parallelism).

</details>

☕ **Break: 5 minutes.**

---

## Session 2 · Amdahl's law (45 min)

### 🎬 The picture

Cooking dinner alone takes you 100 minutes:

- 90 minutes of chopping (friends can help with this),
- 10 minutes of one pot simmering (nobody can speed this up).

With 9 friends, the chopping takes 9 minutes. Dinner takes 9 + 10 = **19 minutes**.

With 1000 friends, the chopping takes almost nothing. Dinner still takes about **10 minutes**.

So no number of friends can make dinner more than 100 ÷ 10 = **10 times** faster.

That's the whole law: **the part you can't speed up puts a ceiling on the speedup.**

### 💡 The formula

```
                      1
Speedup  =  ---------------------
             (1 - F)  +  (F / N)

F = the fraction of the time that can be sped up (the parallel part)
N = the number of processors (or how many times faster that part gets)
```

And the ceiling, when N is huge:

```
Max speedup  =  1 / (1 - F)
```

**"State Amdahl's law"** (1–2 marks), in words:

> The speedup you can get by improving one part of a system is limited by how much of the time that part is actually used.

### ✍️ Past question 1 · Final 2020-21, Q5c (5 marks)

> 80% of the work can be parallelized. How many processing units give a speedup of 4? What is the speedup for a single unit?

```
4  =  1 / (0.2 + 0.8/N)

0.2 + 0.8/N  =  1/4  =  0.25
      0.8/N  =  0.05
          N  =  16
```

- **16 processing units.**
- With one unit: 1 ÷ (0.2 + 0.8) = **1**, so no speedup.
- Bonus line for full marks: the maximum is 1 ÷ 0.2 = **5**, however many units you add.

### ✍️ Past question 2 · Final 2021-22, Q2e (5 marks)

> 50% of the execution time is multimedia work that MMX could speed up. What is the maximum speedup?

"Maximum" means pretending the multimedia part takes zero time.

```
Max speedup  =  1 / (1 - 0.5)  =  2
```

The answer is **2**. The other half doesn't get faster, so the total time can only halve.

### ✍️ Past question 3 · Final 2020-21, Q2d (5 marks)

> Derive Amdahl's speedup formula. A web server's new processor computes 10 times faster. The old one spent 40% of its time computing and 60% on I/O. What is the overall speedup?

**The derivation**, step by step:

```
Old time                 =  T
The improvable part      =  F x T     ->  now takes (F x T) / k
The untouched part       =  (1 - F) x T
New time                 =  (1 - F) x T  +  (F x T) / k

Speedup = old / new      =  1 / ( (1 - F) + F/k )
```

**The numbers:**

```
Speedup  =  1 / (0.6 + 0.4/10)  =  1 / 0.64  =  1.5625
```

Only about **1.56 times faster**, because the I/O didn't change at all.

(The 2018-19 term test had the same question with 30% computing: 1 ÷ (0.7 + 0.03) = **1.37**.)

### ✍️ Past question 4 · Term Test 2018-19 (4 marks)

> "For one program, a large number of processors gives only limited speedup." Do you agree?

> Yes. With N processors, Speedup = 1 / ((1 − F) + F/N). As N grows, F/N shrinks toward zero, so the speedup can never pass 1 / (1 − F). For example, a program that is 90% parallel gets 9.17 times faster on 100 processors and only 9.91 times faster on 1000. Real programs do even worse, because processors also lose time communicating and waiting for each other. This limit is for a fixed-size problem; if the problem grows with the machine, big machines are still useful.

### 💡 Two book words worth one line each

- **Strong scaling**: the problem stays the same size while you add processors.
- **Weak scaling**: the problem grows along with the number of processors.

Bigger problems parallelize better. And balance matters: in the book's example, if just one of 100 processors gets twice its fair share of work, the speedup falls from 91 to 48.

### ⚠️ Traps

- If solving for N gives a **negative** number, the target is **impossible**. Write that, and give the maximum.
- If N comes out as 12.67, the answer is **13** (always round up).
- F is a fraction of **time**, not of instructions.

### ✅ Checkpoint 2

1. A program is 90% parallel. Speedup on 10 processors? The maximum?
2. A program is 95% parallel. How many processors for a speedup of 8?
3. A program is 50% parallel. Can any number of processors make it 4 times faster?

<details><summary>Answers</summary>

1. 1 ÷ (0.1 + 0.09) = **5.26**. Maximum = 1 ÷ 0.1 = **10**.
2. 8 = 1 ÷ (0.05 + 0.95/N), so 0.95/N = 0.075 and N = 12.67. Round up: **13 processors**.
3. **No.** The maximum is 1 ÷ 0.5 = 2.

</details>

☕ **Break: 10 minutes. Stand up and walk around.**

---

## Session 3 · Flynn's taxonomy (60 min) ⭐

This is the big one. It was in every recent final, worth 2, 5 or even 10 marks.

### 🎬 The picture

Flynn sorts computers by counting just two things:

- **Instruction streams**: how many **bosses** are giving orders. (Each boss is a control unit with its own program counter.)
- **Data streams**: how many **piles of data** are being worked on.

Think of a kitchen:

| In the kitchen | Flynn's name |
|---|---|
| One chef cooking one dish | **SISD** |
| A head chef shouts "chop!", and ten cooks each chop their own onion | **SIMD** |
| Ten chefs, each following their own recipe | **MIMD** |
| Ten chefs each doing something different to one single dish | **MISD** (rare, barely exists) |

### 💡 The table (learn this by heart)

|  | One data stream | Many data streams |
|---|---|---|
| **One instruction stream** | **SISD**: a normal single processor (Intel Pentium 4) | **SIMD**: one instruction, lots of data (x86 SSE, vector machines, GPUs) |
| **Many instruction streams** | **MISD**: no real examples today | **MIMD**: a multiprocessor or multicore chip (Intel Xeon) |

**Full forms** (a favourite 2-mark question):

- **SISD** = Single Instruction stream, Single Data stream
- **SIMD** = Single Instruction stream, Multiple Data streams
- **MISD** = Multiple Instruction streams, Single Data stream
- **MIMD** = Multiple Instruction streams, Multiple Data streams

### 💡 Each class in two lines

**SISD**: one control unit, one ALU, one stream of data. Even a fancy pipelined or superscalar single core is still SISD, because it has only one program counter.

**SIMD**: one control unit sends the **same instruction to many ALUs at once**, each working on its own data, all in step. It's great for arrays and loops (data-level parallelism) and bad at `if`/`switch` code, where lanes with the "wrong" data must sit idle.

**MISD**: several instruction streams work on one single data stream. The book says **"no examples today"**. A systolic array is sometimes mentioned as one.

**MIMD**: every processor has **its own control unit** and runs its own program on its own data, independently. Think multicore chips and clusters. It exploits thread-level (task-level) parallelism and needs locks or messages to coordinate.

The professor's slide adds two more names:

- **SPMD** (Single Program, Multiple Data): the usual way to *program* an MIMD machine. Every processor runs the same program on its own data, but **not in lockstep**: each goes at its own pace.
- **Vector**: a kind of SIMD that streams a whole array through one fast pipelined unit, using big vector registers (classic Cray machines).

### ✍️ The diagrams (draw these)

CU = control unit (the boss) · PU = processing unit (the ALU) · MM = memory
IS = instruction stream · DS = data stream

```
SISD   one CU, one PU, one memory

        CU --IS--> PU <--DS--> MM


SIMD   one CU broadcasts each instruction to n PUs; each PU has its own data

                 +--> PU1 <--DS1--> MM1
        CU --IS--+--> PU2 <--DS2--> MM2
                 |     :
                 +--> PUn <--DSn--> MMn


MISD   n CUs give n different instruction streams;
       ONE data stream passes through every PU in turn

                   CU1         CU2             CUn
                    | IS1       | IS2           | ISn
                    v           v               v
        MM --DS--> PU1 --DS--> PU2 --> ... --> PUn --DS--> MM


MIMD   n CUs, n PUs, n data streams; each processor runs its own program

        CU1 --IS1--> PU1 <--DS1--+
        CU2 --IS2--> PU2 <--DS2--+--> shared memory, or a private memory
         :            :          |    per PU joined by a network
        CUn --ISn--> PUn <--DSn--+
```

The one thing examiners look for: **SIMD has one CU. MIMD has one CU per PU.**

### ✍️ The 10-mark answer (Final 2021-22, Q6c)

Write it in this order. It takes about 15 minutes.

1. **Intro, 2 lines:** "Flynn's taxonomy classifies computers by the number of instruction streams and data streams they handle. Each can be single or multiple, which gives four classes."
2. **The 2 × 2 table**, with an example in each box.
3. **The four diagrams.**
4. **A short paragraph per class**: copy the "two lines" above.
5. **Closing, 2 lines:** "SPMD is how MIMD machines are normally programmed, and vector processors are a form of SIMD. Modern chips mix the classes: a multicore CPU is MIMD with SIMD units inside each core, and a GPU is many SIMD units working together."

**For 5 marks** (Final 2020-21, Q2f): steps 1 and 2, one line per class, and only the SIMD diagram.

### ✍️ Quick 2-markers

**"Which category of Flynn's taxonomy is a GPU?"** (Final 2021-22)

> Mainly **SIMD**. A group of 32 GPU threads (a "warp") runs the same instruction on different data at the same time; NVIDIA calls this SIMT. The whole chip has many such groups working independently, so the textbook calls it an MIMD made of SIMD processors.

**"Differentiate SIMD and MIMD"** (Final 2015-16)

| | SIMD | MIMD |
|---|---|---|
| Control units | one for everyone | one per processor |
| How they run | in lockstep, same operation | independently, own programs |
| Parallelism | data-level | thread / task-level |
| Example | x86 SSE, GPUs | multicore Xeon, clusters |

**True or false** (Final 2015-16):

- "MISD means many instruction single data." **True.**
- "MIMD targets task-level parallelism." **True.**

### ✅ Checkpoint 3

1. Close this file. Draw all four diagrams from memory.
2. Classify each: (a) one superscalar core, (b) an 8-core laptop CPU, (c) one SSE instruction adding 4 numbers, (d) a GPU.
3. What makes SPMD different from SIMD?

<details><summary>Answers</summary>

1. Check three things: SIMD has one CU; MIMD has a CU for every PU; MISD has one data stream passing through all the PUs.
2. (a) SISD, (b) MIMD, (c) SIMD, (d) SIMD inside, MIMD as a whole.
3. SPMD processors run the same program but each at its own pace (not in lockstep), picking different work with `if` on their processor number.

</details>

☕ **Break: 10 minutes. Drink some water.**

---

## Session 4 · SIMD, vectors and GPUs (40 min)

### 🎬 The picture

A drill sergeant shouts "ADD!" once, and 64 soldiers each add their own pair of numbers at the same moment. One order gives 64 results. That's **SIMD**.

Only one sergeant (control unit) is needed, so almost all the army's budget goes on soldiers (ALUs).

### ✍️ "Explain what SIMD means and why GPUs or AI coprocessors use it" (Term Test 2 2026, 5 marks)

> **SIMD** (single instruction, multiple data) means one control unit fetches and decodes an instruction once and sends it to many processing units, which apply it to different data at the same time. *(Draw the SIMD diagram here.)*
>
> GPUs and AI coprocessors use it because:
>
> 1. **Their work is the same operation on huge amounts of independent data**: shading millions of pixels, or multiplying millions of numbers in a neural network.
> 2. **One control unit drives many ALUs**, so fetching and decoding happen once per instruction instead of once per number. Most of the chip and its power go into arithmetic, which gives far more work per watt.
> 3. **Fewer instructions** have to be fetched, since one instruction does a whole loop's work.
> 4. **Memory access is regular**: neighbouring lanes read neighbouring addresses, which can be fetched together.
> 5. **SIMD's weak spot**, code full of `if`/`switch`, rarely appears in graphics or AI.

Any four points earn the marks.

### ✍️ "Why does vector processing increase the performance of a processor?" (Final 2020-21, 5 marks)

🎬 A normal processor adding two arrays is like a clerk who, for every single pair of numbers, re-reads the instruction card and asks "am I done yet?". A vector processor reads the card once ("add these 64 pairs") and the numbers roll past on a conveyor belt.

> 1. **One vector instruction does a whole loop's work**, so far fewer instructions are fetched and decoded.
> 2. **No hazard checks inside a vector**, because its elements are independent by definition.
> 3. **Hazards between vector instructions are checked once per vector**, not once per element.
> 4. **The memory delay is paid once per vector**, since the elements arrive in a known pattern.
> 5. **No loop branch**, so no branch (control) hazards.
> 6. **Less power**, from fewer instructions and fewer checks.
>
> The book's example (DAXPY, Y = a × X + Y on 64 numbers) takes about **600** ordinary MIPS instructions but only **6** vector instructions.

### 💡 GPUs in five lines

- A GPU is an **accelerator** sitting next to the CPU (together they're "heterogeneous").
- It hides slow memory with **thousands of threads**, not with big caches.
- Its memory is built for **bandwidth** (lots of data per second), not for low delay.
- A **warp** is 32 threads running the same instruction together (SIMT).
- If threads in a warp take different `if` branches, both paths run one after the other, which is slower.

### ✅ Checkpoint 4

1. Why is SIMD cheap? Answer in one sentence.
2. Four lanes run `if (x > 0) y = 2*x; else y = -x;` with x = 3, −1, 5, −2. How many passes does it take?
3. True or false: "GPUs use graphics memory to reduce latency."

<details><summary>Answers</summary>

1. One control unit is shared by many ALUs, so the cost of fetching and decoding is spread over all of them.
2. **Two passes.** First the lanes holding 3 and 5 work while the others wait, then the lanes holding −1 and −2. Half the hardware sits idle in each pass.
3. **False.** Graphics memory is chosen for bandwidth.

</details>

☕ **Break: 5 minutes.**

---

## Session 5 · Multithreading (30 min)

### 🎬 The picture

One cashier (a core). A customer (a thread) is digging through their bag for a wallet (a stall, like waiting for memory).

A smart cashier starts serving the next customer meanwhile. To do that, the cashier keeps **a separate running total for each customer**. In hardware terms: every thread gets **its own registers and its own program counter**.

Remember: multithreading **does not add processors**. It just keeps one processor busy.

### 💡 The three kinds

| | Fine-grained | Coarse-grained | SMT (simultaneous) |
|---|---|---|---|
| Switches threads | every cycle, taking turns | only on a long stall (like waiting for main memory) | never: several threads issue in the **same** cycle |
| Hides | short and long stalls | long stalls only | everything, by filling every free slot |
| Downside | each single thread runs slower | refilling the pipeline after a switch costs time | needs a complex out-of-order core |
| Example | Sun UltraSPARC T2 | — | Intel Nehalem (Hyper-Threading) |

### ✍️ Draw it

Rows are clock cycles, columns are the 4 issue slots, a dot is a wasted slot, and A–D are four threads.

```
 Coarse-grained MT        Fine-grained MT          Simultaneous MT (SMT)
 (switch on long stall)   (switch every cycle)     (many threads per cycle)

  A  A  .  .               A  A  .  .               A  A  B  C
  A  .  .  .               B  B  B  .               B  B  C  D
  .  .  .  .  <-A stalls   C  .  .  .               A  D  D  C
  B  B  B  .  <-B runs     D  D  .  .               C  C  A  B
  B  .  .  .               A  .  .  .               D  A  B  B
  B  B  .  .               B  .  .  .               C  D  D  A
  .  .  .  .  <-B stalls   C  C  C  .               A  B  C  .
  C  C  .  .               D  D  .  .               D  D  A  B
```

- **Coarse:** whole empty rows after a stall.
- **Fine:** one thread per row, with gaps inside the rows.
- **SMT:** mixed threads in each row, so the fewest gaps.

### ✍️ "State the differences between multithreading and hyper-threading" (Final 2021-22, 2 marks)

> **Multithreading** is the general idea of running several threads to keep a processor busy. It comes in three forms: fine-grained, coarse-grained and simultaneous (SMT). **Hyper-Threading** is Intel's name for its own SMT: each core keeps two sets of registers and shows up to the operating system as **two logical processors**, while both threads share the core's execution units.

### ✅ Checkpoint 5

1. What has to be copied for each hardware thread?
2. Which kind switches every cycle? Which switches only on long stalls?
3. Hyper-Threading is Intel's version of which kind?

<details><summary>Answers</summary>

1. The registers and the program counter.
2. Fine-grained. Coarse-grained.
3. SMT (simultaneous multithreading).

</details>

☕ **Break: 5 minutes.**

---

## Session 6 · Shared memory vs message passing (25 min)

### 🎬 The picture

Ten students solving one problem together.

- **Shared memory** is one big whiteboard. Everyone reads and writes it directly. But two people mustn't write in the same spot at once, so they pass around a single marker: a **lock**.
- **Message passing** is a private notebook for everyone. To share anything, you text it. If you're waiting for a number, you just wait for the text to arrive.

### ✍️ The table (a likely 5-mark question)

| | Shared memory (SMP) | Message passing (clusters) |
|---|---|---|
| Memory | one address space for everyone | private memory for each processor |
| How they talk | ordinary loads and stores | send and receive messages |
| Coordination | locks | built in (receiving waits for the message) |
| Hardware | needs cache coherence | simpler |
| Copies of the OS | one | one per computer |
| Size | tens of processors | thousands (datacenter-sized) |
| Example | multicore chips | clusters, Google-style datacenters |

Two extra words:

- **UMA** (uniform memory access): every processor reaches memory in the same time. Easier to program.
- **NUMA** (non-uniform memory access): nearby memory is faster than faraway memory. Harder to program, but it scales bigger.

### ✅ Checkpoint 6

1. Which one needs locks? Which one needs a copy of the OS on every computer?
2. What's the difference between UMA and NUMA?

<details><summary>Answers</summary>

1. Shared memory needs locks. Message passing (clusters) needs an OS copy on every computer.
2. UMA: the same memory access time for everyone. NUMA: the time depends on how close the memory is.

</details>

☕ **Break: 10 minutes before the mock.**

---

## Session 7 · Mini mock (30 min, closed book)

Paper and a timer. No peeking.

**Q1. Answer any three (2 marks each)**

- a) Full forms of SISD and MISD.
- b) Which category of Flynn's taxonomy is a GPU?
- c) Multithreading vs hyper-threading.
- d) SIMD vs MIMD.

**Q2. Answer one (5 marks)**

- a) 80% of a program can run in parallel. How many processors give a speedup of 4? What's the speedup on one processor?
- b) Why do GPUs and AI chips use SIMD?

**Q3. (10 marks)** Explain the four classes of Flynn's taxonomy, with diagrams.

<details><summary>How to mark yourself</summary>

- **Q1:** check against Sessions 3 and 5. Full marks need the full form or the key difference, plus an example.
- **Q2a:** the equation (1), N = 16 (2), one processor gives 1 (1), the maximum of 5 (1).
- **Q2b:** the definition (1) plus four reasons (4).
- **Q3:** intro (1), table (2), four diagrams (3), a paragraph per class (3), SPMD and vector (1).
- **Below 70%?** Redo only the session where you lost marks.

</details>

---

## 🌙 The night-before card

Read this once before you sleep and once before the exam.

- **Power wall** → more cores instead of faster clocks.
- **Amdahl:** `Speedup = 1 / ((1 - F) + F/N)`, and the max is `1 / (1 - F)`.
  80% parallel → **16** processors for 4 times faster. 50% → max **2**.
- **Flynn:** SISD (Pentium 4) · SIMD (SSE, vectors, GPUs) · MISD (none) · MIMD (multicore).
  SPMD = same program, not lockstep. Vector = SIMD through one pipelined unit.
- **Diagrams:** SIMD has one CU feeding many PUs. MIMD has a CU for every PU.
- **GPUs use SIMD** because it's the same operation on tons of data, and one control unit for many ALUs means more work per watt.
- **Vectors are fast** because one instruction is a whole loop (6 vs about 600), memory delay is paid once, and there's no loop branch.
- **Multithreading:** fine = every cycle · coarse = on long stalls · SMT = same cycle. **Hyper-Threading = Intel's SMT.**
- **Shared memory** = one whiteboard + locks. **Message passing** = private notebooks + send/receive.

---

## 🎁 Bonus, only if you have spare time

- **Thread-level vs request-level parallelism** (Final 2015-16, 3 marks). *Thread-level*: the threads of **one** program cooperating and sharing data (a game running physics and graphics threads). *Request-level*: many **independent** requests from different users (a web server). Our book calls the second one "job-level parallelism".
- **The 1987 "Amdahl's law is broken" claim.** The researchers grew the problem along with the machine (weak scaling). For a fixed-size problem, Amdahl still holds.
- **The full detailed answers** for every Ch 7 question are also in the L9 tab of the Final Kit artifact.
