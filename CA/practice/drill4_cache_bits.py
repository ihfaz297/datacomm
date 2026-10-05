# DRILL 4: how many bits does a cache really need? / tag size vs associativity
#
#   total bits = #blocks x (data bits per block + tag bits + 1 valid bit)
#   answer in Kbits where 1 Kbit = 1024 bits
from cachelib import check, score

# Q1  (textbook) 16 KB of data, 4-word blocks, direct mapped, 32-bit byte address.
q1_blocks = None
q1_tag_bits = None
q1_bits_per_block = None     # data + tag + valid
q1_total_kbits = None

# Q2  (new) 32 KB of data, 8-word blocks, direct mapped, 32-bit byte address.
q2_tag_bits = None
q2_total_kbits = None

# Q3  (textbook) 4K blocks, 4-word blocks, 32-bit address. TOTAL TAG BITS in Kbits for:
q3_dm = None
q3_2way = None
q3_4way = None
q3_fa = None

# Q4  The 4-way cache in Q3 needs how many comparators? and what size multiplexor (e.g. 4 for 4-to-1)?
q4_comparators = None
q4_mux_inputs = None


# ---------------- checker ----------------
check("Q1 blocks", q1_blocks, 1024)
check("Q1 tag bits", q1_tag_bits, 18)
check("Q1 bits per block", q1_bits_per_block, 147)
check("Q1 total Kbits", q1_total_kbits, 147)
check("Q2 tag bits", q2_tag_bits, 17)
check("Q2 total Kbits", q2_total_kbits, 274)
check("Q3 DM", q3_dm, 64)
check("Q3 2-way", q3_2way, 68)
check("Q3 4-way", q3_4way, 72)
check("Q3 FA", q3_fa, 112)
check("Q4 comparators", q4_comparators, 4)
check("Q4 mux", q4_mux_inputs, 4)
score()
