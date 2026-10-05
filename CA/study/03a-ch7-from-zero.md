# Ch 7 From Zero: the story version (read THIS first, then `03-ch7-quiz.md`)

You haven't read Ch 7. Fine. The whole chapter is **one story with one villain**. Learn the story and every section slots in.

---

## The story in 60 seconds

> Chips got too hot to make **one** core faster (the **power wall**).
> So companies put **many cores** on a chip (**multicore**).
> But software is written for **one** core, and splitting work is **hard** (**Amdahl**: the serial bit kills you).
> Two ways to let cores cooperate: **share one memory** (SMP) or **send messages** (clusters).
> Two ways to squeeze more out of **one** core: **multithreading** (keep it busy) and **SIMD/vector** (one instruction, lots of data).
> **GPUs** take SIMD + multithreading to the extreme.
> Then: how to **wire** cores together (**networks**), how to **measure** them (**benchmarks**), how to **predict** them (**roofline**), and **mistakes people make** (fallacies).

That's 7.1 → 7.13 in order. Seriously.

### Mnemonic for the chapter order: **"I Did Some Clever Hacks So Gamers Need Better Rooflines Really Fast"**
| Word | Section |
|---|---|
| **I**ntroduction | 7.1 |
| **D**ifficulty (why parallel is hard) | 7.2 |
| **S**hared memory | 7.3 |
| **C**lusters / message passing | 7.4 |
| **H**ardware multithreading | 7.5 |
| **S**ISD/SIMD/… (Flynn) | 7.6 |
| **G**PUs | 7.7 |
| **N**etworks | 7.8 |
| **B**enchmarks | 7.9 |
| **R**oofline | 7.10 |
| **R**eal stuff (4 chips) | 7.11 |
| **F**allacies | 7.12 |

---

## 7.1 Why bother? The power wall
Analogy: one chef can't cook faster without the kitchen catching fire. **Hire more chefs.**
- **Multiprocessor** = ≥ 2 processors. **Multicore** = many processors ("cores") on **one chip**.
- **Job-level parallelism** = many chefs, **different orders** (independent programs, e.g. a web server). Easy.
- **Parallel processing program** = many chefs, **one dish**. Hard.
- **Cluster** = many whole computers on a LAN acting as one.
- Bonus win: if one chef faints, the other n−1 keep cooking → **availability**.

**Sequential vs concurrent vs serial vs parallel** (the quiz loves this): **S**oftware is **S**equential or concurrent. **H**ardware is serial or parallel. Mnemonic: *"Software Sequences, Hardware Hustles in parallel."* You can mix any software with any hardware.

---

## 7.2 Why parallel is hard (the villain = Amdahl)
**8 reporters writing one news story.** What goes wrong? Mnemonic **"SLiCS"**:
- **S**cheduling: who writes which part
- **L**oad balancing: one reporter got the long part, everyone waits for them
- **C**ommunication overhead: they spend all day talking
- **S**ynchronization: waiting for each other

**Amdahl's law** = the serial part is a speed limit.
```
Speed-up = 1 / ( serial + parallel/P )
```
Intuition: if 10% must be serial, then even with **infinite** cores you get at most **10×**.
Book's punchline: to get **90×** from **100** cores, only **0.1%** can be serial. Brutal.

**Strong vs weak scaling.** Mnemonic: **"Strong = Same size, Weak = Wider work."**
- **Strong**: same problem, more cores. Hard.
- **Weak**: bigger problem as you add cores (100 cores → 100× the data). Easier, and that's how people "beat" Amdahl (the 7.12 fallacy).
- Book example: a 10×10 matrix on 100 cores gives only **10×**. A 100×100 matrix on 100 cores gives **91×**. **Bigger problems parallelize better.**
- **Load balance**: if one core gets 2% of the work instead of 1%, speed-up drops from 91 to **48**. One slow reporter halves everything.

---

## 7.3 vs 7.4: how cores cooperate. Whiteboard vs WhatsApp
| | **Shared memory (SMP)** = *one big whiteboard* | **Message passing / clusters** = *everyone has their own notebook and texts each other* |
|---|---|---|
| Address space | **one shared** | **private per node** |
| Talking | just write/read the board (**load/store**, implicit) | **send() / receive()** (explicit) |
| Danger | two people writing the same spot → need a **lock** (one marker!) | messages are slow |
| Sync | **locks**, barriers | **send/receive sync by themselves** (you wait for the text) |
| OS copies | **1** | **n** (each computer runs its own OS) |
| Scales to | tens of cores | **thousands** (Google datacenters) |
| Breakdown | one core dies → hard to fix | swap a dead machine easily → **high availability** |

Two whiteboard flavours: **UMA** = **U**niform, everyone stands the **same distance** from the board. **NUMA** = **N**on-uniform, some people stand closer (faster to their nearby memory). NUMA scales bigger but is harder to program.

**Reduction** = turning many partial sums into one, by halving: 100 cores → 50 add pairs → 25 → … → 1. Like a knockout tournament bracket. 🏆

**Cluster complaints** (mnemonic **"AIM"**): **A**dmin cost (n machines = n headaches), **I**/O interconnect (slower than the memory bus), **M**emory split (n copies of the OS waste RAM: 20 GB shared vs 5×4 GB cluster → shared gives **25% more** usable).

---

## 7.5 Hardware multithreading: keep ONE core busy
Picture a single cashier (core). A customer (thread) fumbles for their wallet (**cache miss / stall**). The cashier just stands there. Wasteful.
**Multithreading = the cashier serves the next customer while one fumbles.** To do this the cashier needs a separate "tab" per customer → **each thread gets its own registers + PC**.

Three styles. Mnemonic **"Fine Flips Frequently, Coarse Changes on Crisis, SMT Serves Several Simultaneously"**:

| Style | Cashier behaviour | Good | Bad | Real chip |
|---|---|---|---|---|
| **Fine-grained** | switches customer **every second** (every cycle), round-robin | hides short **and** long stalls | each customer is served slower | **Sun T2 (Niagara)** |
| **Coarse-grained** | switches only on a **big** fumble (L2 miss) | doesn't slow anyone down | switching has a **start-up cost** (pipeline refill), useless for short stalls | — |
| **SMT** | a **multi-lane** till serving several customers **in the same second** | fills every empty slot | needs a fancy out-of-order core | **Intel Nehalem** (2 threads) = **Hyper-Threading** |

The picture (Fig 7.5): columns = issue slots, rows = clock cycles. Coarse has whole empty **rows**. Fine has no empty rows but gaps **within** rows. **SMT has the fewest gaps.**

---

## 7.6 Flynn's taxonomy: count the streams
Two questions: how many **instruction** streams? How many **data** streams? → 4 boxes. Mnemonic: **"S I S D"** read as **"Single Instruction, Single Data"**, swap S↔M to get the rest.

```
                 1 data stream        many data streams
1 instruction    SISD  (old PC,       SIMD  (one command,
                  Pentium 4)           many data: x86 SSE, GPUs, vector)
many instr.      MISD  (NOTHING —     MIMD  (multicore,
                  no real examples)    Xeon Clovertown)
```
- **SPMD** = **S**ingle **P**rogram **M**ultiple **D**ata = how people *program* MIMD (same code on every core, `if (my_id == …)`). **Not a hardware box.**
- **MISD** = the trick answer: **"no examples today."**

### SIMD intuition: the drill sergeant 🪖
One sergeant shouts **"ADD!"** and **64 soldiers** each add their own numbers at once.
- Why it's cheap: **one** brain (control unit) for many arms (ALUs) → "**amortize the control unit**". Also less code.
- Loves: **arrays in for-loops** (everyone does the same thing) = **data-level parallelism**.
- Hates: **switch/case** (soldiers need different orders → the sergeant calls them group by group → **1/n speed**).
- x86 version = **MMX/SSE**: split one 64-bit ALU into 2×32, 4×16 or 8×8. The width is baked into the **opcode** → hundreds of opcodes (opcode explosion).

### Vector = SIMD's older, more elegant cousin (Cray)
Instead of 64 soldiers, **one very fast assembly line** (pipelined ALU) fed by **giant vector registers** (32 registers × 64 elements).
- **DAXPY** (Y = a·X + Y): normal MIPS ≈ **600** instructions, vector ≈ **6**. 🤯
- Why vectors win, mnemonic **"FIND MCP"**: **F**ewer instruction fetches, **I**ndependence guaranteed (no hazard checks inside), **N**o loop branches (no control hazards), **D**ata hazards checked once per vector, **M**emory pattern known (latency paid once), **C**ompiler-friendly, **P**ower saving.
- Vector vs SSE: vector length lives in a **register** (not the opcode), and vectors can do **strided/indexed** loads.

### 🎯 "Why do GPUs / AI chips use SIMD?" (TT2-2026 asked this). Template answer:
1. Graphics/AI = **the same operation on millions of independent pixels/numbers** → huge **data-level parallelism**.
2. SIMD = **one instruction fetch/decode drives many ALUs** → control cost shared → more of the chip and power budget goes to math → **throughput per watt**.
3. Fewer instructions, simpler hazard checks, **regular memory access** (wide coalesced loads).
4. Little branching in these kernels, so SIMD's weakness (switch/case) rarely hurts.

---

## 7.7 GPUs: SIMD + multithreading on steroids
CPU = **a few genius professors** (big caches, smart, low latency).
GPU = **a stadium of students** each doing simple sums (thousands of threads, high throughput).

Key differences, mnemonic **"No Cache, Many Threads, Fat Pipes"**:
- **No reliance on big caches**: hide memory delay by switching to **other threads** while waiting.
- **Many threads**: every processor is heavily multithreaded.
- **Fat pipes**: memory built for **bandwidth**, not latency (graphics DRAM = wider, faster). ⚠️ Trick: "GPU DRAM reduces latency" → **FALSE**, it's **bandwidth**.
- Also: GPUs are **accelerators** next to a CPU (**heterogeneous**). Programmed via APIs (**OpenGL, DirectX**), then **CUDA** (C for GPUs). Single precision ≫ double (8–10×).

NVIDIA vocabulary (the chapter's GPU is **Tesla**, **GeForce 8800 GTX**):
- **Warp = 32 threads** marching together. Mnemonic: a **warp** is a **32-person marching band**: same step, same time.
- If threads in a warp take different `if` branches → **divergence**: both paths run one after the other, so it's slower.
- **SIMT** = Single Instruction Multiple **Thread**: NVIDIA's name for "warp runs SIMD-style".
- **Thread block** ≤ **512** threads, all on one multiprocessor sharing its local memory.
- 8800 GTX: **16** multiprocessors × **8** streaming processors × 2 FLOPs × 1.35 GHz = **345.6 GFLOPs**.

Fig 7.8 (2×2 grid). Mnemonic **"Very Smart Students Teach"**:
```
               found at COMPILE time   found at RUN time
ILP            VLIW                    Superscalar
DLP            SIMD / Vector           Tesla (GPU)
```

---

## 7.8 Networks: how to wire the cores
Think of cities connected by roads.
- **Bus** = one road everyone shares. **Ring** = a circle road. **Fully connected** = a direct road between every pair of cities (amazing, insanely expensive).
- **Total bandwidth** = add up all the roads (best case). **Bisection bandwidth** = cut the map in half and count the roads crossing the cut (worst case; pick the **worst** cut).

| | Total | Bisection |
|---|---|---|
| Bus | 1 | 1 |
| Ring | **P** | **2** (cut a circle and you hit 2 roads) |
| Fully connected | **P(P−1)/2** (handshakes problem) | **(P/2)²** (every left city to every right city) |

- **2D mesh** = city grid. **n-cube** = hypercube: 2ⁿ nodes, n neighbours each.
- **Crossbar** = any-to-any in one hop, **n²** switches. **Omega** = cheaper (**2n·log₂n**), but messages can **collide**. For 8 nodes: **64 vs 48** switches.

---

## 7.9 Benchmarks: the rules of the race
"You can't change the benchmark", except that most allow **weak scaling** (a bigger problem for a bigger machine).
Mnemonic **"Lazy Students Skip Notes, Pass Barely"**:
| | Key fact |
|---|---|
| **L**inpack | dense linear algebra. **Top500 list**. Weak scaling. Can **rewrite** in any language. DAXPY is its inner loop |
| **S**PECrate | many copies of SPEC → **job-level** parallelism |
| **S**PLASH-2 | Stanford, shared memory, the **only STRONG-scaling** one |
| **N**AS | NASA fluid dynamics, 5 kernels, rewrite in **C or Fortran only** |
| **P**ARSEC | Princeton, **Pthreads + OpenMP**, emerging apps |
| **B**erkeley Design Patterns | **13 patterns** (sparse matrix, MapReduce, …). Any algorithm allowed → encourages innovation |
Downside of strict rules: **they suppress innovation** (TRUE in Check Yourself).

---

## 7.10 Roofline: one picture to predict performance
Your speed is capped by **two ceilings**, like a house roof:
- **Flat roof** = how fast the chip can **compute** (peak GFLOPs).
- **Slanted roof** = how fast memory can **feed** the chip (bandwidth × arithmetic intensity).
```
Attainable = min( Bandwidth × Arithmetic Intensity ,  Peak FLOPs )
```
**Arithmetic intensity** = FLOPs per byte fetched = "how much cooking per grocery trip".
- Low intensity → stuck under the **slanted roof** → **memory-bound**.
- High intensity → hits the **flat roof** → **compute-bound**.
- **Ridge point** = where the roofs meet. Far right = a demanding machine (only heavy kernels reach peak).
- Example: 16 GFLOPs peak, 16 GB/s. Kernel with AI 0.5 → 16×0.5 = **8 GFLOPs** (memory-bound). AI 4 → 64, capped at **16** (compute-bound).
- Fixes ("ceilings"): **compute** → balance adds/multiplies, more ILP + SIMD. **Memory** → **software prefetching**, **memory affinity** (keep data near the core that uses it). Mnemonic: **"Mix, SIMD | Prefetch, Place"**.

---

## 7.11 Four real chips (just remember the punchlines)
- **Intel Xeon (Clovertown)**: **highest peak, slowest in practice** (choked by the front-side bus). → the fallacy example.
- **AMD Opteron X4**: solid all-rounder; needed the most tuning.
- **Sun UltraSPARC T2 (Niagara)**: slow clock, **lots of threads**, the **easiest to program**.
- **IBM Cell**: **fastest**, but **no caches** (local store + DMA), so you have to rewrite code for it.

## 7.12 Fallacies & pitfalls (3 of them)
1. ❌ "**Amdahl doesn't apply** to parallel machines". They cheated with **weak scaling**.
2. ❌ "**Peak performance = real performance**". Xeon had the highest peak and was the slowest.
3. ⚠️ Pitfall: **not rewriting software** for multiprocessors. The **SGI** OS used **one lock** for the whole page table → everything serialized.

## 7.13 Why be hopeful
Software-as-a-service + clusters, science's endless hunger (>80% of the Top500 are clusters), everyone ships multicore, on-chip communication is fast, sublinear speed-up is OK now, JIT compilers, open source.

---

## 10-second recall card (cover and recite)
1. Power wall → multicore.
2. SLiCS: Scheduling, Load balance, Communication, Synchronization.
3. 90× on 100 cores → 0.1% serial.
4. Strong = Same size. Weak = Wider work.
5. Whiteboard (SMP: shared, locks, UMA/NUMA) vs WhatsApp (clusters: send/receive, n OS copies).
6. Fine flips every cycle (T2), Coarse changes on crisis, SMT serves several at once (Nehalem / Hyper-Threading).
7. Flynn: SISD P4, SIMD SSE, MISD none, MIMD Xeon. SPMD = programming style.
8. SIMD = drill sergeant; loves loops, hates switch.
9. Vector DAXPY 600 → 6.
10. GPU: No Cache, Many Threads, Fat Pipes. Warp = 32. Graphics DRAM = bandwidth, not latency.
11. Ring: P / 2. Fully connected: P(P−1)/2 / (P/2)². Crossbar n² vs Omega 2n·log₂n.
12. Roofline = min(BW × AI, peak).
