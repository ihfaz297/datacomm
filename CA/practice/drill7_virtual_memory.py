# DRILL 7: virtual memory numbers
#
#   page offset bits = log2(page size)
#   VPN bits = VA bits - offset          PPN bits = PA bits - offset
#   #page table entries = 2^VPN bits     page table size = entries x PTE size
#   VIPT max cache size = associativity x page size
from cachelib import check, score

# Q1  (textbook) 32-bit VA, 4 KB pages, 4-byte PTEs.
q1_offset_bits = None
q1_vpn_bits = None
q1_page_table_MB = None

# Q2  (textbook Fig 5.20) same VA, PPN is 18 bits. Max physical memory in GB?
q2_phys_GB = None

# Q3  (old final) 48-bit VA, physical memory 4 GB, page size 64 KB.
q3_pa_bits = None
q3_offset_bits = None
q3_vpn_bits = None
q3_ppn_bits = None
q3_page_table_GB_if_4B_PTE = None

# Q4  (old final) 4 KB pages, 16-way set-associative VIPT cache: max size in KB?
q4_vipt_KB = None

# Q5  (slides) hit 100 ns, page fault rate 0.0001 %, fault penalty 10 ms. Effective access time in ns?
q5_eat_ns = None

# Q6  (Fig 5.26) Which TLB/PageTable/Cache combos are POSSIBLE? Use H/M letters in that order.
#     Give a Python set like {"HHM", "MMM"} of ALL possible ones among the 7 non-HHH combos.
q6_possible = None

# Q7  TLB reach: 64 entries, 4 KB pages, in KB?
q7_reach_KB = None

# Q8  (new) 40-bit VA, 8 KB pages, 1 GB physical memory.
q8_offset_bits = None
q8_vpn_bits = None
q8_ppn_bits = None

# Q9  One word each:
q9_vm_write_policy = None              # "write-back" or "write-through"
q9_page_placement = None               # "direct-mapped", "set-associative" or "fully-associative"
q9_who_handles_page_faults = None      # "hardware" or "software"


# ---------------- checker ----------------
check("Q1 offset", q1_offset_bits, 12)
check("Q1 VPN", q1_vpn_bits, 20)
check("Q1 table MB", q1_page_table_MB, 4)
check("Q2 phys GB", q2_phys_GB, 1)
check("Q3 PA bits", q3_pa_bits, 32)
check("Q3 offset", q3_offset_bits, 16)
check("Q3 VPN", q3_vpn_bits, 32)
check("Q3 PPN", q3_ppn_bits, 16)
check("Q3 table GB", q3_page_table_GB_if_4B_PTE, 16)
check("Q4 VIPT KB", q4_vipt_KB, 64)
check("Q5 EAT", q5_eat_ns, 110.0)
check("Q6 possible combos", q6_possible, {"HHM", "MHH", "MHM", "MMM"})
check("Q7 reach KB", q7_reach_KB, 256)
check("Q8 offset", q8_offset_bits, 13)
check("Q8 VPN", q8_vpn_bits, 27)
check("Q8 PPN", q8_ppn_bits, 17)
check("Q9 write policy", q9_vm_write_policy, "write-back")
check("Q9 placement", q9_page_placement, "fully-associative")
check("Q9 handler", q9_who_handles_page_faults, "software")
score()
