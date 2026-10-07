# DRILL 2: direct-mapped trace tables (TT2-2025 gave 6/10 marks for exactly this)
#
# Draw the table on paper (Index | V | Tag | Data) and update it after every access.
# Then type: hits/misses as a string like "MMHH" and the final table as {index: tag} for VALID lines only.
# Indexes and tags as ints: 0b010 is fine.
from cachelib import check, score, simulate

# ---- PART A: TT2-2025 Q2 ------------------------------------------------------
# 8-block DM cache, 1-byte blocks, 32-block memory (5-bit addresses). Initial state:
#   000 Y tag 10  Mem(10000)
#   010 Y tag 11  Mem(11010)
#   110 Y tag 10  Mem(10110)    all others N
# Reads: (a) 00011   (b) 10010   (c) 00011 again
a_hm = None            # e.g. "MHM"
a_final = None         # e.g. {0b000: 0b10, 0b010: 0b11, ...}
a_which_data_was_replaced = None   # address (as 0b.....) evicted in (b), or None-> leave as ... if nothing

# ---- PART B: textbook Fig 5.6 -------------------------------------------------
# Same cache, EMPTY at start. Word addresses (decimal): 22, 26, 22, 26, 16, 3, 16, 18, 16
b_hm = None
b_final = None

# ---- PART C: Final 2024 Q6a (32-byte blocks, 32 lines, DM) --------------------
# Byte addresses (dec): 0, 4, 16, 132, 232, 160, 1024, 30, 140, 3100, 180, 2180
c_hm = None            # 12 letters
c_hit_ratio = None     # as a fraction, e.g. 0.5

# ---- PART D: why was (b) in Part A a miss and not a hit? one word: "conflict", "compulsory" or "capacity"
d_kind_of_miss = None


# ---------------- checker ----------------
def hm(log): return "".join("H" if r[4] == "hit" else "M" for r in log)
def final(sets): return {s: v[0] for s, v in sets.items() if v}

log, sets = simulate([0b00011, 0b10010, 0b00011], 8, initial={0: [0b10], 2: [0b11], 6: [0b10]})
check("A hit/miss", a_hm and a_hm.upper(), hm(log))
check("A final table", a_final, final(sets))
check("A evicted address", a_which_data_was_replaced, 0b11010)

log, sets = simulate([22, 26, 22, 26, 16, 3, 16, 18, 16], 8)
check("B hit/miss", b_hm and b_hm.upper(), hm(log))
check("B final table", b_final, final(sets))

log, _ = simulate([0, 4, 16, 132, 232, 160, 1024, 30, 140, 3100, 180, 2180], 32, block_size=32)
check("C hit/miss", c_hm and c_hm.upper(), hm(log))
check("C hit ratio", c_hit_ratio, 4 / 12)
check("D kind of miss", d_kind_of_miss, "conflict")
score()
