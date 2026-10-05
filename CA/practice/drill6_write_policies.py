# DRILL 6: write policies, the counting question both old finals asked
#
# Fully associative, write-back, "many entries" (nothing ever gets evicted). Starts EMPTY.
#   Reads ALWAYS bring the block in.
#   write-allocate:     a write miss brings the block in
#   no-write-allocate:  a write miss goes to memory only, the block stays OUT of the cache
from cachelib import check, score, write_policy

# Q1  W[100], W[100], R[200], W[200], W[100]
q1_nwa_hm = None     # e.g. "MMHMM"
q1_wa_hm = None

# Q2  R[400], W[500], R[100], W[400], R[500]
q2_nwa_hm = None
q2_wa_hm = None

# Q3  (new) W[300], R[300], W[300], R[700], W[700], W[100], R[100]
q3_nwa_hm = None
q3_wa_hm = None

# Q4  Concepts. Answer with the policy names exactly as in quotes:
#     "write-through" / "write-back" / "write-allocate" / "no-write-allocate"
q4_needs_dirty_bit = None
q4_memory_always_consistent = None
q4_usually_paired_with_write_back = None
q4_usually_paired_with_write_through = None
q4_used_by_virtual_memory = None


# ---------------- checker ----------------
def hm(lst): return "".join("H" if x == "hit" else "M" for x in lst)

for name, ops, nwa, wa in [
    ("Q1", [("W", 100), ("W", 100), ("R", 200), ("W", 200), ("W", 100)], q1_nwa_hm, q1_wa_hm),
    ("Q2", [("R", 400), ("W", 500), ("R", 100), ("W", 400), ("R", 500)], q2_nwa_hm, q2_wa_hm),
    ("Q3", [("W", 300), ("R", 300), ("W", 300), ("R", 700), ("W", 700), ("W", 100), ("R", 100)], q3_nwa_hm, q3_wa_hm),
]:
    check(f"{name} no-write-allocate", nwa and nwa.upper(), hm(write_policy(ops, False)))
    check(f"{name} write-allocate", wa and wa.upper(), hm(write_policy(ops, True)))

check("Q4 dirty bit", q4_needs_dirty_bit, "write-back")
check("Q4 always consistent", q4_memory_always_consistent, "write-through")
check("Q4 pairs with WB", q4_usually_paired_with_write_back, "write-allocate")
check("Q4 pairs with WT", q4_usually_paired_with_write_through, "no-write-allocate")
check("Q4 VM uses", q4_used_by_virtual_memory, "write-back")
score()
