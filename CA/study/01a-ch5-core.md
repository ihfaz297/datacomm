# Ch 5 CORE: read this, not 01/02 (those are reference only)

Ordered by marks. Parts 1–3 = ~80% of the paper. ~60 min to learn, then do drills 1, 2, 6.

---

## PART 1: The 6-mark question: cache trace table

### Step 1: split the address
```
| TAG | INDEX | OFFSET |
offset = log2(block size)      (1-byte/1-word blocks → 0 bits)
index  = log2(number of sets)  (direct mapped: sets = blocks)
tag    = everything left
```
8-block cache, 5-bit address `10110` → index = **last 3 bits** `110`, tag = **first 2** `10`.

### Step 2: for each access, go to that index row
- V = N → **MISS** (empty). Write V=Y, tag, Memory(addr).
- V = Y, tag same → **HIT**. Change nothing.
- V = Y, tag different → **MISS**, **replace** the old block. Write the new tag + data.

### Worked (TT2-2025, exactly this came):
Start: `000: Y 10 Mem(10000)`, `010: Y 11 Mem(11010)`, `110: Y 10 Mem(10110)`.
| Read | Index | Tag | Row has | Result |
|---|---|---|---|---|
| 00011 | 011 | 00 | V=N | **MISS**, fill: Y 00 Mem(00011) |
| 10010 | 010 | 10 | tag 11 ≠ 10 | **MISS**, replace Mem(11010) with Mem(10010), tag ← 10 |
| 00011 | 011 | 00 | tag 00 = 00 | **HIT** |

Final: `000 Y 10 Mem(10000) · 010 Y 10 Mem(10010) · 011 Y 00 Mem(00011) · 110 Y 10 Mem(10110)`, rest N.

**For full marks write all 5 per access:** binary → index/tag → what you compared → H/M → what changed. Draw the final table.

### Set-associative / fully associative version
- set = block address **mod #sets**. Inside the set, a block can go in **any** way. When full, evict **LRU** (least recently used).
- Fully associative = **one set**, no index bits, search every tag.
- Famous example, 4 blocks, addresses **0,8,0,6,8**: DM **5 misses**, 2-way **4**, FA **3**.

### Bigger blocks (bytes)
block address = ⌊byte addr ÷ block size⌋, offset = remainder. Byte 1200, 16 B blocks, 64 blocks → block 75 → slot **75 mod 64 = 11**.

---

## PART 2: The 2-mark "explain" questions (model answers, say them out loud)

**Temporal vs spatial locality**
Temporal: a recently used item will be used **again soon** (loops). Spatial: items **near** a used item will be used soon (arrays, sequential instructions). Caches keep recent data (temporal) and fetch whole multi-word blocks (spatial).

**Fully associative vs direct mapped**
DM: each block has **one** possible slot. Simple, **1 comparator**, fast, but **conflict misses** when two hot blocks share a slot.
FA: a block can go **anywhere**. **No conflict misses, lowest miss rate**, free choice of victim (LRU). Cost: **a comparator per entry**, more power, slower hit. Only practical for small caches like TLBs.
Set-associative = the middle ground (n slots per set).

**Write-through vs write-back** (mnemonic: *Through = Twice, Back = Later*)
WT: every write goes to the **cache AND memory**, so memory is always up to date. Slow, so it uses a **write buffer** (a queue; the CPU stalls only if the buffer is full).
WB: write **only the cache** and mark it **dirty**. Memory is updated **later, when the block is replaced**. Faster, more complex.

**Write-allocate vs no-write-allocate** (what happens on a write MISS)
WA: **bring the block into the cache**, then write. Pairs with **write-back**.
NWA: write **memory only**, cache untouched. Pairs with **write-through**. (Useful when whole blocks are overwritten, e.g. the OS zeroing a page.)
Counting trick: under NWA, writing the same address twice = **two misses**.

**Split vs unified cache**
Split = separate I-cache and D-cache. **Double bandwidth** (an instruction and a data access in the same cycle). Unified = one shared cache with a slightly **lower miss rate** (flexible sharing). Split usually wins overall, so miss rate isn't everything.

**Block size trade-off**
Bigger blocks → fewer misses (spatial locality), **but** a bigger **miss penalty**. If too big, there are too few blocks and the miss rate **rises** again.

**Multilevel cache**
L2 catches L1's misses, so the L1 miss penalty becomes small. **L1 focuses on hit time** (small, fast). **L2 focuses on miss rate** (big, more associative).

---

## PART 3: Numbers (one formula each)

```
AMAT = hit time + miss rate × miss penalty
CPI  = base CPI + (I-miss rate × penalty) + (load/store % × D-miss rate × penalty)
```
- AMAT: hit 1, miss rate 5%, penalty 20 → **2 cycles**.
- CPI: I 2%, D 4%, base 2, penalty 100, 36% ld/st → 2 + 2 + 1.44 = **5.44** (perfect cache is 2.72× faster).
- 2-level: 4 GHz, memory 100 ns = **400 cycles**, L2 5 ns = **20 cycles**, L1 miss 2%, global miss 0.5%:
  L1 only: 1 + 0.02×400 = **9**. With L2: 1 + 0.02×20 + 0.005×400 = **3.4**. Speedup **2.6**.

---

## PART 4: Virtual memory in 12 lines

1. VM = **main memory acts as a cache for disk**. Main reason today: **protection / safe sharing** between programs.
2. Page = block. **Page fault** = miss (the page is on disk). Costs **millions of cycles**, handled by the **OS (software)**.
3. Address: `| virtual page number | page offset |`. The offset is **not translated**. VPN → PPN via the **page table**.
4. **Page table**: in memory, one per process, indexed by VPN, valid bit (0 → page fault). **No tags** (it's not a cache).
5. Because faults are so expensive: **big pages** (4–16 KB), **fully associative** placement, **LRU** (via a reference bit), **write-back always** (+ dirty bit).
6. Page table size: 32-bit VA, 4 KB pages → 2²⁰ entries × 4 B = **4 MB**. Too big → **multi-level page tables**.
7. **TLB** = a small, fast cache of page table entries, so translation doesn't cost an extra memory access every time.
8. TLB miss ≠ page fault: TLB miss with the page in memory → reload the TLB. Page not in memory → page fault.
9. **Impossible**: TLB hit + page not in memory. Data in the cache + page not in memory.
10. Bits: offset = log2(page size), VPN = VA bits − offset, PPN = PA bits − offset.
11. **VIPT** cache max size = ways × page size (4 KB pages, 16-way → 64 KB).
12. Protection: **user/kernel mode**, the user can't write the page table / TLB, **syscall** to enter the OS.

---

**Then:** drill1 → drill2 → drill6 → drill7. Skip 01/02 unless a drill FAILs and you want the detail.
