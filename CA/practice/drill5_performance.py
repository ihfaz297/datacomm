# DRILL 5: CPI with stalls, AMAT, multilevel caches, memory organisation
#
#   stall cycles/instr = I-miss rate x penalty + (loads+stores fraction) x D-miss rate x penalty
#   CPI = base CPI + stall cycles/instr
#   AMAT = hit time + miss rate x miss penalty
#   cycles = ns / (clock period in ns)
# Floats are checked to ~1%.
from cachelib import check, score

# Q1  (textbook) I-miss 2%, D-miss 4%, base CPI 2, penalty 100 cycles, loads+stores = 36%.
q1_cpi = None
q1_speedup_perfect_cache = None
q1_cpi_if_base_becomes_1 = None
q1_stall_fraction_before = None   # stall cycles / total, e.g. 0.63
q1_stall_fraction_after = None

# Q2  (textbook) clock 1 ns, miss penalty 20 cycles, miss rate 0.05, hit time 1 cycle. AMAT in ns:
q2_amat_ns = None

# Q3  (textbook) 4 GHz, base CPI 1.0, main memory 100 ns, L1 miss rate 2%/instr.
#     Add L2: 5 ns access, miss rate to main memory 0.5%.
q3_mem_penalty_cycles = None
q3_cpi_L1_only = None
q3_L2_penalty_cycles = None
q3_cpi_with_L2 = None
q3_speedup = None
q3_L2_local_miss_rate = None      # as a fraction

# Q4  (textbook) 1 cycle address, 15 cycles per DRAM access, 1 cycle per word sent, 4-word block.
q4_one_word_wide = None
q4_two_word_wide = None
q4_interleaved_4_banks = None

# Q5  (new) I-miss 1%, D-miss 5%, 30% loads/stores, penalty 50, base CPI 1.5.
q5_cpi = None

# Q6  (new) hit time 2 cycles, miss rate 4%, penalty 60 cycles.
q6_amat = None

# Q7  (old final) split 16KB I + 16KB D vs unified 32KB: AMAT of each, and which wins ("split"/"unified")?
#     I misses/1000 instr = 3.82, D = 40.9, unified = 43.3; 36% loads/stores; hit 1; penalty 100;
#     unified pays +1 cycle on data accesses.
q7_amat_split = None
q7_amat_unified = None
q7_winner = None


# ---------------- checker ----------------
check("Q1 CPI", q1_cpi, 5.44)
check("Q1 speedup", q1_speedup_perfect_cache, 2.72)
check("Q1 CPI base 1", q1_cpi_if_base_becomes_1, 4.44)
check("Q1 stall frac before", q1_stall_fraction_before, 0.63, tol=0.02)
check("Q1 stall frac after", q1_stall_fraction_after, 0.77, tol=0.02)
check("Q2 AMAT ns", q2_amat_ns, 2.0)
check("Q3 mem penalty", q3_mem_penalty_cycles, 400)
check("Q3 CPI L1 only", q3_cpi_L1_only, 9.0)
check("Q3 L2 penalty", q3_L2_penalty_cycles, 20)
check("Q3 CPI with L2", q3_cpi_with_L2, 3.4)
check("Q3 speedup", q3_speedup, 2.6, tol=0.03)
check("Q3 L2 local miss rate", q3_L2_local_miss_rate, 0.25)
check("Q4 one-word-wide", q4_one_word_wide, 65)
check("Q4 two-word-wide", q4_two_word_wide, 33)
check("Q4 interleaved", q4_interleaved_4_banks, 20)
check("Q5 CPI", q5_cpi, 2.75)
check("Q6 AMAT", q6_amat, 4.4)
check("Q7 AMAT split", q7_amat_split, 4.24, tol=0.02)
check("Q7 AMAT unified", q7_amat_unified, 4.44, tol=0.02)
check("Q7 winner", q7_winner, "split")
score()
