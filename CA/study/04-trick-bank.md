# Trick Bank: "it's in the chapter, you just skipped it"

Cover the answer, say yours out loud, then click to reveal. Mark a ✗ next to any you miss and redo only those at the end.
In VS Code: Ctrl+Shift+V for preview, where the arrows expand.

## Part A: Ch 5.1–5.3 caches (midterm)

<details><summary>1. Does "hit time" include deciding whether it's a hit?</summary>

**Yes.** Hit time = time to access the upper level **including the time to determine hit or miss**.
</details>

<details><summary>2. What does the miss penalty include? (4 things)</summary>

Time to **access** the block in the lower level, **transmit** it, **insert** it into the level that missed, and **pass it to the requestor**.
</details>

<details><summary>3. T/F: On a read, the value returned depends on which blocks are in the cache.</summary>

**False.** The cache changes speed, never the value.
</details>

<details><summary>4. T/F: Most of the cost of the memory hierarchy is at the highest level.</summary>

**False.** It varies by computer, but in 2008 the biggest cost was usually the **DRAM**.
</details>

<details><summary>5. What is "inclusion" / a true hierarchy?</summary>

Data can't be in level i unless it is also in level i+1. Upper levels are subsets, and all data lives at the lowest level.
</details>

<details><summary>6. Why is DRAM cheaper per bit than SRAM?</summary>

DRAM uses **much less area per bit** → more capacity for the same silicon. (SRAM = 6 transistors/bit; DRAM = 1 transistor + 1 capacitor, must be refreshed.)
</details>

<details><summary>7. Why don't we store the index bits in the tag?</summary>

They are **redundant**: the index of any block in a slot is, by definition, that slot's number.
</details>

<details><summary>8. Why must a direct-mapped cache have a power-of-2 number of entries?</summary>

The index is an n-bit field of the address, which has exactly 2ⁿ values. (It also makes mod = "take the low bits".)
</details>

<details><summary>9. What's the valid bit for? What is it at power-on?</summary>

Says whether the entry holds valid data. At power-on all are **off (N)**, so the tags are meaningless garbage.
</details>

<details><summary>10. A "16 KB cache" with 4-word blocks: how many total bits really?</summary>

**147 Kbits ≈ 18.4 KB** (1.15× the data). The name counts data only.
</details>

<details><summary>11. Byte address 1200, 64 blocks of 16 bytes: which cache block? Which addresses share it?</summary>

Block address 75 → **75 mod 64 = 11**. The block holds **1200–1215**.
</details>

<details><summary>12. Can increasing block size INCREASE the miss rate? Why?</summary>

**Yes.** When the block is a big fraction of the cache there are too few blocks, more competition, and blocks get bumped before their words are used. Also the **miss penalty rises** (transfer time).
</details>

<details><summary>13. Early restart vs critical word first?</summary>

Early restart: resume as soon as the **requested word arrives** (works best for instructions). Critical word first (requested word first): memory sends the **requested word first**, then wraps around the rest. Slightly faster.
</details>

<details><summary>14. Does a cache miss cause an interrupt?</summary>

**No, a pipeline stall.** An interrupt would require saving all registers. (In-order processor assumed.)
</details>

<details><summary>15. On an instruction cache miss, what address is sent to memory and why?</summary>

**PC − 4**, because the PC was already incremented in the first cycle.
</details>

<details><summary>16. 10% stores, base CPI 1, write-through with no buffer, 100 cycles/write: new CPI?</summary>

1 + 100 × 0.10 = **11** (more than 10× slower). That's why we need a write buffer.
</details>

<details><summary>17. When does a write buffer NOT help at all?</summary>

When memory completes writes **slower than** the CPU generates them. (Bursts can stall even if the average rate is OK → make the buffer deeper.)
</details>

<details><summary>18. Another name for write-back?</summary>

**Copy-back.**
</details>

<details><summary>19. Why can write-through stores be done in 1 cycle but write-back can't?</summary>

WT: write the data while checking the tag. If it misses, memory still has the correct copy, so the overwrite is harmless. WB: the block may be **dirty and not backed up**, so you must check for a hit first (2 cycles) or use a **store buffer**.
</details>

<details><summary>20. Motivation for no-write-allocate?</summary>

Programs sometimes write **whole blocks** (e.g. the **OS zeroing a page**), so fetching the block on a write miss is wasted. Some machines set the policy **per page**.
</details>

<details><summary>21. What does a write-back buffer do to the miss penalty when a dirty block is replaced?</summary>

**Halves it** (the dirty block goes into the buffer while the new block is read), assuming no immediate second miss.
</details>

<details><summary>22. Intrinsity FastMATH: pipeline depth, cache size, block size, tag/index bits, write policy, write buffer size?</summary>

**12-stage** pipeline. **Separate 16 KB** I and D caches, **16-word blocks**, 256 blocks. **Tag 18, index 8**, block offset 4, byte offset 2. **Both WT and WB (OS chooses)**. **One-entry** write buffer. Miss rates I 0.4%, D 11.4%, combined 3.2%.
</details>

<details><summary>23. Split vs combined: which has the lower miss rate, and why use split anyway?</summary>

**Combined** has the lower miss rate (3.18% vs 3.24%), since it doesn't rigidly divide the entries. Split **doubles bandwidth** (an I and a D access in the same cycle). So miss rate isn't the only measure.
</details>

<details><summary>24. Miss penalty: one-word-wide vs 2-word-wide vs 4-bank interleaved (1/15/1 cycles, 4-word block)?</summary>

**65** (0.25 B/clk), **33** (0.48), **20** (0.80).
</details>

<details><summary>25. What does DDR mean?</summary>

**Double Data Rate**: transfers on **both the rising and falling clock edges**.
</details>

<details><summary>26. Which guidelines are valid: shorter latency → (smaller/larger) block; higher bandwidth → (smaller/larger) block?</summary>

**Shorter latency → smaller block**. **Higher bandwidth → larger block**.
</details>

<details><summary>27. When can write-buffer stalls be ignored?</summary>

Buffer depth ≥ **4 words** and memory accepts writes at ≥ **2×** the average write rate.
</details>

<details><summary>28. I-miss 2%, D-miss 4%, CPI 2, penalty 100, 36% loads/stores: CPI and perfect-cache speedup?</summary>

2 + 2 + 1.44 = **5.44** → **2.72×**. If base CPI drops to 1: 4.44 → 4.44×, and the stall fraction goes **63% → 77%**.
</details>

<details><summary>29. A 2-way set-associative cache holds how many blocks per set? DM is how many "ways"? FA with m blocks is how many ways?</summary>

2 per set. DM = **1-way**. FA = **m-way** (one set).
</details>

<details><summary>30. Set-associative = a fixed number of locations, at least how many?</summary>

**At least two.**
</details>

<details><summary>31. Block 12, 8-block cache: DM slot? 2-way set? FA?</summary>

**4**. **Set 0** (of 4). **Anywhere.**
</details>

<details><summary>32. Block addresses 0,8,0,6,8 with 4 one-word blocks: misses for DM / 2-way / FA?</summary>

**5 / 4 / 3.**
</details>

<details><summary>33. Going from 1-way to 2-way reduces the miss rate by about how much? After that?</summary>

**~15%** (10.3% → 8.6%). Then little: 8.3%, 8.1%.
</details>

<details><summary>34. Doubling associativity at a fixed size: what happens to index and tag bits?</summary>

Index **−1**, tag **+1**. Number of sets halves; comparators double.
</details>

<details><summary>35. Hardware for a 4-way set-associative cache?</summary>

**4 comparators + a 4-to-1 multiplexor.**
</details>

<details><summary>36. What's a CAM and when was it used (2008)?</summary>

Content Addressable Memory: supply data, it returns the matching index (comparison + storage in one). **8-way and above** used CAMs. 2-way/4-way used SRAM + comparators.
</details>

<details><summary>37. How many bits per set to implement LRU in a 2-way cache?</summary>

**One bit.**
</details>

<details><summary>38. Tag bits for 4K blocks, 4-word blocks, 32-bit addr: DM / 2-way / 4-way / FA?</summary>

**64K / 68K / 72K / 112K.**
</details>

<details><summary>39. Multilevel example (4 GHz, 100 ns mem, 2% L1 miss, 5 ns L2, 0.5% global): CPIs and speedup?</summary>

**9 → 3.4, 2.6× faster.**
</details>

<details><summary>40. Local miss rate of that L2?</summary>

0.5% / 2% = **25%**.
</details>

<details><summary>41. L1 optimizes ___, L2 optimizes ___.</summary>

L1 → **hit time**. L2 → **miss rate**. (L1 smaller with smaller blocks; L2 bigger, larger blocks, more associative.)
</details>

<details><summary>42. Why is Radix sort slower than Quicksort for big arrays despite fewer instructions?</summary>

**Far more cache misses** per item. Algorithm analysis ignored the memory hierarchy.
</details>

<details><summary>43. What's autotuning?</summary>

Libraries that **search their parameter space at runtime** to fit a particular machine's memory hierarchy.
</details>

## Part B: Ch 5.4 virtual memory (midterm)

<details><summary>44. Which VM motivation dominates today?</summary>

**Safe and efficient sharing of memory among multiple programs (protection)**, not "make memory look bigger".
</details>

<details><summary>45. What were overlays?</summary>

Programmer-managed pieces of a too-big program, loaded/unloaded under program control. VM removed this burden.
</details>

<details><summary>46. Cache "block" and "miss" in VM language?</summary>

**Page** and **page fault**.
</details>

<details><summary>47. Typical page sizes (2008)? Embedded?</summary>

**4–16 KB**. Servers moving to 32/64 KB. Embedded going **down to 1 KB**.
</details>

<details><summary>48. Four design decisions caused by the huge page-fault penalty?</summary>

Large pages, **fully associative** placement, faults **handled in software**, **write-back**.
</details>

<details><summary>49. How much faster is main memory than disk (book)?</summary>

About **100,000×**. A page fault = **millions** of cycles.
</details>

<details><summary>50. Segmentation vs paging?</summary>

Segmentation: **variable-size**, two-part address (segment + offset) visible to programmers, needs a **bounds check**. Paging: fixed size, the boundary is **invisible**.
</details>

<details><summary>51. Why does a page table need no tags?</summary>

It has an entry for **every** virtual page (full index = VPN). **A page table is not a cache**; the TLB is.
</details>

<details><summary>52. What's the state of a process?</summary>

**Page table + PC + registers.** To switch, the OS reloads the **page table register**.
</details>

<details><summary>53. Where does the OS keep the disk location of pages? What's swap space?</summary>

In the page table (when invalid) or a parallel structure. **Swap space** = disk space reserved for a process's **full virtual memory**, created at process creation.
</details>

<details><summary>54. How is LRU approximated for pages?</summary>

**Reference (use) bit** set on access. The OS periodically clears the bits and checks them later. (Clock / second-chance algorithm.)
</details>

<details><summary>55. Page table size: 32-bit VA, 4 KB pages, 4 B/PTE?</summary>

2²⁰ × 4 B = **4 MB per process**.
</details>

<details><summary>56. Name the 5 ways to shrink page table storage.</summary>

**Limit register**. **Two tables** growing stack-down / heap-up (MIPS). **Inverted page table** (hashing). **Multi-level** page tables. **Paged page tables**.
</details>

<details><summary>57. Why is write-back extra good for VM (besides speed)?</summary>

Disk **transfer** time is small compared with **access** time, so writing a whole page back once is far more efficient than individual words.
</details>

<details><summary>58. Without a TLB, how many memory accesses per load?</summary>

**Two**: one for the PTE, one for the data.
</details>

<details><summary>59. Typical TLB: size, hit time, miss penalty, miss rate?</summary>

**16–512 entries**, **0.5–1 cycle**, **10–100 cycles**, **0.01%–1%**.
</details>

<details><summary>60. Which TLB bits get copied back to the page table on replacement?</summary>

**Reference and dirty bits** (the only parts that change).
</details>

<details><summary>61. TLB misses vs page faults: which is more frequent?</summary>

**TLB misses**, much more.
</details>

<details><summary>62. FastMATH TLB: entries, associativity, shared?, miss cost, replacement?</summary>

**16 entries, fully associative, shared I+D**, 64-bit entries (20-bit tag, 20-bit PPN). Miss ≈ **13 cycles** (software). **Random** replacement.
</details>

<details><summary>63. Which of TLB-hit / PT-miss / cache-hit is possible?</summary>

**Impossible.** Can't have a translation in the TLB if the page isn't in memory. (Possible combos: H-H-M, M-H-H, M-H-M, M-M-M.)
</details>

<details><summary>64. "TLB hit and cache hit are independent", but what's the catch?</summary>

A cache hit can only occur **after** a TLB hit (the data must be in memory).
</details>

<details><summary>65. What's aliasing? Which cache type suffers?</summary>

Two virtual addresses for the same physical page, so data can be cached in two places. **Virtually addressed (VIVT)** caches. **VIPT has no alias problem.**
</details>

<details><summary>66. 4 KB pages, 16-way VIPT: max cache size?</summary>

16 × 4 KB = **64 KB**. (Index + offset must fit in the 12-bit page offset.)
</details>

<details><summary>67. 3 hardware capabilities needed for protection?</summary>

(1) **User and supervisor (kernel) modes**. (2) State the user can **read but not write** (mode bit, **page table pointer, TLB**). (3) Mode switching: **syscall** → supervisor (PC saved in **EPC**), **ERET** → back.
</details>

<details><summary>68. How do you avoid flushing the TLB on every context switch?</summary>

Add a **process / address space ID (ASID)** to the TLB tag. FastMATH: **8-bit ASID**.
</details>

<details><summary>69. MIPS TLB miss handler address vs general exception address?</summary>

TLB miss: **8000 0000hex**. General: **8000 0180hex**.
</details>

<details><summary>70. Does the MIPS TLB miss handler check the PTE's valid bit?</summary>

**No.** It loads blindly. If invalid, the retry raises a page fault. This makes the common case fast.
</details>

<details><summary>71. What's "unmapped" memory in MIPS?</summary>

VA **8000 0000–BFFF FFFF**: it can't page-fault (upper bits ignored). Exception handlers and the exception stack live there.
</details>

<details><summary>72. Why are x86 instructions hard to restart after a page fault?</summary>

Block-move instructions touch **thousands** of words and can fault mid-instruction, so they must be **continued mid-stream** (save special state), not restarted.
</details>

<details><summary>73. Thrashing? Working set? TLB reach of 64 entries × 4 KB?</summary>

Continuous swapping. The set of popular pages. **0.25 MB**. Fix with **variable/large page sizes**.
</details>

<details><summary>74. Match: L1 / L2 / main memory / TLB ↔ a cache for: a cache, main memory, disks, PTEs.</summary>

L1 → **a cache for a cache**. L2 → **main memory**. Main memory → **disks**. TLB → **PTEs**.
</details>

## Part C: Ch 7 (quiz)

<details><summary>75. Why "multicore" and not "multiprocessor microprocessor"?</summary>

To **avoid redundancy in naming**.
</details>

<details><summary>76. Besides performance and power, what else do multiprocessors improve?</summary>

**Availability**: with n processors, one failure still leaves **n − 1** working.
</details>

<details><summary>77. Job-level parallelism vs parallel processing program?</summary>

Independent programs at once (throughput) vs **one** program on many processors.
</details>

<details><summary>78. T/F: To benefit from a multiprocessor, an application must be concurrent.</summary>

**False.**
</details>

<details><summary>79. Four challenges from the "8 reporters" analogy?</summary>

**Scheduling, load balancing, synchronization time, communication overhead.**
</details>

<details><summary>80. Speed-up 90 on 100 processors: max sequential %?</summary>

**0.1%.**
</details>

<details><summary>81. 10 scalars + 10×10 matrix: speed-up on 10 and 100 processors? With 100×100?</summary>

**5.5 and 10**. **9.9 and 91.**
</details>

<details><summary>82. One processor with 2% / 5% of the load (100×100, 100 procs)?</summary>

**48 / 20.**
</details>

<details><summary>83. Strong vs weak scaling: memory per processor?</summary>

Strong **M/P**. Weak **M**.
</details>

<details><summary>84. T/F: Strong scaling is not bound by Amdahl's law.</summary>

**False.**
</details>

<details><summary>85. A more accurate name for "shared memory multiprocessor"?</summary>

**Shared-address multiprocessor.**
</details>

<details><summary>86. UMA vs NUMA: which is harder to program, which scales bigger?</summary>

NUMA is **harder** to program but **scales larger**, with lower latency to nearby memory.
</details>

<details><summary>87. T/F: SMPs can't exploit job-level parallelism.</summary>

**False.** Jobs run in separate virtual address spaces.
</details>

<details><summary>88. What's a reduction?</summary>

A function that processes a data structure and returns a **single value** (e.g. summing partial sums by halving).
</details>

<details><summary>89. T/F: Message-passing machines rely on locks. T/F: They need multiple copies of the program and OS.</summary>

**False** (send/receive synchronize implicitly). **True.**
</details>

<details><summary>90. Three drawbacks of clusters?</summary>

**Admin cost ≈ n machines**. Connected via the **I/O** interconnect (not memory). Memory divided + **n OS copies**.
</details>

<details><summary>91. 20 GB SMP vs 5 × 4 GB cluster, 1 GB OS: memory advantage?</summary>

19/15 ≈ **1.25** (25% more).
</details>

<details><summary>92. What makes clusters easier to administer?</summary>

**Virtual machines** (atomic start/stop, migration off failing hardware).
</details>

<details><summary>93. SETI@home stats?</summary>

>5 million users, >200 countries, >19 billion CPU hours, **257 TFLOPS** (end of 2006). An example of **grid computing**.
</details>

<details><summary>94. What must the hardware duplicate per thread for multithreading?</summary>

**Register file and PC** (independent state). Memory is shared via VM.
</details>

<details><summary>95. Fine-grained: main advantage / disadvantage?</summary>

Hides **short and long** stalls / **slows individual threads**.
</details>

<details><summary>96. Coarse-grained switches on what? Main drawback?</summary>

**Costly stalls (L2 misses)**. **Pipeline start-up cost**, so it can't hide short stalls.
</details>

<details><summary>97. Which real chips: SMT with 2 threads? Fine-grained with 8 threads/core?</summary>

**Intel Nehalem**. **Sun UltraSPARC T2 (Niagara 2)**.
</details>

<details><summary>98. T/F: SMT uses threads to improve resource utilization of a dynamically scheduled OoO processor.</summary>

**True.** (Also true: both MT and multicore rely on parallelism.)
</details>

<details><summary>99. Flynn examples from the book for SISD / SIMD / MISD / MIMD?</summary>

**Pentium 4 / x86 SSE / none today / Xeon e5345 (Clovertown).**
</details>

<details><summary>100. Is SPMD a hardware class?</summary>

**No.** It's the normal **programming style** for MIMD: one program, conditionals select the code.
</details>

<details><summary>101. Original motivation of SIMD?</summary>

**Amortize the cost of the control unit** over dozens of execution units. (Also smaller program memory.)
</details>

<details><summary>102. Where is SIMD weakest, and how bad is it?</summary>

**case/switch** statements → runs at **1/n** performance for n cases.
</details>

<details><summary>103. Where is the data width encoded in MMX/SSE vs vector?</summary>

MMX/SSE: in the **opcode** (opcode explosion). Vector: a **separate (vector-length) register** → binary compatibility.
</details>

<details><summary>104. DAXPY instruction count: MIPS vs vector? Stall frequency ratio?</summary>

**~600 vs 6**. MIPS stalls **~64×** more often.
</details>

<details><summary>105. What's strip mining?</summary>

Handling loops **longer** than the vector length: full-length chunks + leftovers.
</details>

<details><summary>106. Two vector memory access types multimedia extensions lack?</summary>

**Strided** and **indexed (gather)**.
</details>

<details><summary>107. Why weren't vectors popular outside HPC?</summary>

**Larger register state → slower context switches**, and it's hard to handle **page faults in vector loads/stores**.
</details>

<details><summary>108. GPUs' biggest architectural difference from CPUs?</summary>

They **don't rely on multilevel caches** to hide memory latency. They use **many threads**.
</details>

<details><summary>109. T/F: GPUs use graphics DRAM to reduce memory latency.</summary>

**False.** It's for **higher bandwidth**.
</details>

<details><summary>110. Pixels vs vertices ratio in games? Vertex/pixel component formats?</summary>

**20–30×** as many pixels. Vertex (x,y,z,w) as 32-bit floats. Pixel (R,G,B,A), once 8-bit ints, now SP floats 0–1.
</details>

<details><summary>111. SP vs DP speed on 2008 GPUs?</summary>

SP **8–10×** faster (DP hardware only appeared in 2008).
</details>

<details><summary>112. Warp size? Thread block max? 8800 GTX peak?</summary>

**32** threads. **512** threads. **345.6 GFLOPs**.
</details>

<details><summary>113. Fig 7.8: classify VLIW, superscalar, SIMD/vector, Tesla (static/dynamic × ILP/DLP).</summary>

VLIW = static ILP. Superscalar = dynamic ILP. SIMD/Vector = static DLP. **Tesla = dynamic DLP.**
</details>

<details><summary>114. Ring vs fully connected: total and bisection bandwidth?</summary>

Ring: **P** and **2**. FC: **P(P−1)/2** and **(P/2)²**. (Bus: 1 and 1.)
</details>

<details><summary>115. Crossbar vs Omega switches for n = 8?</summary>

**n² = 64** vs **2n log₂n = 48** (12 boxes × 4). Omega has **contention** (can't do P0→P6 and P1→P7 together).
</details>

<details><summary>116. n-cube: nodes, links per switch?</summary>

**2ⁿ** nodes, **n** links (+1 to the processor).
</details>

<details><summary>117. Which benchmark requires STRONG scaling? Which allows reprogramming in only C or Fortran?</summary>

**SPLASH/SPLASH-2**. **NAS**.
</details>

<details><summary>118. SPECrate measures what kind of parallelism?</summary>

**Job-level** (many independent copies, no communication).
</details>

<details><summary>119. Roofline formula? Kernel with AI 0.5 on 16 GFLOP/16 GB/s?</summary>

min(BW × AI, peak FP) → **8 GFLOPs (memory-bound)**.
</details>

<details><summary>120. Arithmetic intensity definition?</summary>

**FLOPs / bytes accessed from main memory.**
</details>

<details><summary>121. Opteron X2 → X4 ridge point move? Why?</summary>

**1 → 5**. 4× the peak FP with the **same socket, so the same DRAM bandwidth**.
</details>

<details><summary>122. Two computational and two memory ceilings?</summary>

FP mix balance, ILP + SIMD. **Software prefetching**, **memory affinity**.
</details>

<details><summary>123. Highest-peak multicore that delivered the lowest performance?</summary>

**Intel Xeon e5345 (Clovertown)**: dual front-side bus bottleneck.
</details>

<details><summary>124. Easiest multicore to program in 7.11? Why no base number for Cell?</summary>

**UltraSPARC T2**. Cell's SPEs have **local stores, not caches**: the code must be rewritten for **DMA**.
</details>

<details><summary>125. The "Amdahl's law broken" claim used which trick?</summary>

**Weak scaling** (1000× more work, constant sequential part).
</details>

<details><summary>126. The SGI pitfall?</summary>

The page table protected by a **single lock** → serialized page allocation, even for independent jobs. Fix: finer-grained locks.
</details>

<details><summary>127. What fraction of the Top500 were clusters (2007)?</summary>

**> 80%.**
</details>
