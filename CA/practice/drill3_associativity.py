# DRILL 3: direct mapped vs set associative vs fully associative (LRU replacement)
#
#   DM:      slot = block % #blocks
#   n-way:   set  = block % (#blocks / n), any way in that set, evict the LRU one
#   FA:      anywhere, evict the LRU one
from cachelib import check, score, simulate

# Q1  Memory block 12, cache with 8 blocks.
q1_dm_slot = None
q1_2way_set = None
q1_4way_set = None

# Q2  (textbook) 4 one-word blocks. Block addresses 0, 8, 0, 6, 8.
q2_dm_misses = None
q2_2way_misses = None
q2_fa_misses = None
q2_2way_block_evicted_when_6_arrives = None

# Q3  New one (not in the book): 4 one-word blocks. Block addresses 1, 5, 9, 1, 5, 13, 1
q3_dm_hm = None      # string like "MMHM..."
q3_2way_hm = None
q3_fa_hm = None

# Q4  Theory: n-way set associative cache with m sets.
q4_n_for_direct_mapped = None           # a number
q4_m_for_fully_associative = None       # a number

# Q5  What's the minimum possible number of misses for Q2's sequence on ANY 4-block cache?
q5_min_misses = None


# ---------------- checker ----------------
def hm(log): return "".join("H" if r[4] == "hit" else "M" for r in log)
def misses(log): return sum(r[4] == "miss" for r in log)

check("Q1 DM slot", q1_dm_slot, 4)
check("Q1 2-way set", q1_2way_set, 0)
check("Q1 4-way set", q1_4way_set, 0)
seq = [0, 8, 0, 6, 8]
check("Q2 DM misses", q2_dm_misses, misses(simulate(seq, 4, ways=1)[0]))
check("Q2 2-way misses", q2_2way_misses, misses(simulate(seq, 4, ways=2)[0]))
check("Q2 FA misses", q2_fa_misses, misses(simulate(seq, 4, ways=4)[0]))
check("Q2 evicted by 6", q2_2way_block_evicted_when_6_arrives, 8)
seq = [1, 5, 9, 1, 5, 13, 1]
check("Q3 DM", q3_dm_hm and q3_dm_hm.upper(), hm(simulate(seq, 4, ways=1)[0]))
check("Q3 2-way", q3_2way_hm and q3_2way_hm.upper(), hm(simulate(seq, 4, ways=2)[0]))
check("Q3 FA", q3_fa_hm and q3_fa_hm.upper(), hm(simulate(seq, 4, ways=4)[0]))
check("Q4 n for DM", q4_n_for_direct_mapped, 1)
check("Q4 m for FA", q4_m_for_fully_associative, 1)
check("Q5 min misses", q5_min_misses, 3)
score()
