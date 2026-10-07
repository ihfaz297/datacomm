# DRILL 1: split an address into TAG | INDEX | OFFSET   (the 6-mark question lives on this)
#
# Recipe:
#   offset bits = log2(block size in BYTES)        (byte-addressed)
#   #sets       = #blocks / associativity          (DM: associativity = 1)
#   index bits  = log2(#sets)
#   tag bits    = address bits - index - offset
#   For a given address:  offset = addr % blockbytes
#                         block address = addr // blockbytes
#                         index = block address % #sets
#                         tag   = block address // #sets
#
# Do it on PAPER first, then type your numbers below (replace None) and run:
#   python CA/practice/drill1_address_split.py
from cachelib import check, score

# Q1  Intrinsity FastMATH: 16 KB cache, 16-word (64-byte) blocks, direct mapped, 32-bit byte addresses.
q1_offset_bits = None      # byte-offset + block-offset together
q1_index_bits  = None
q1_tag_bits    = None

# Q2  (textbook) 64 blocks, 16 bytes per block. Byte address 1200.
q2_block_address = None
q2_cache_block   = None
q2_first_byte_in_block = None
q2_last_byte_in_block  = None

# Q3  (Final 2024) Main memory 64 KB, cache 4 KB, block 16 B, byte addressable, assume direct mapped.
q3_address_bits = None
q3_offset_bits  = None
q3_index_bits   = None
q3_tag_bits     = None
#     ... and split address 0x0C14  (answer index in decimal OR hex like 0xC1, both are ints in Python)
q3_tag    = None
q3_index  = None
q3_offset = None

# Q4  (Final 2024) 64-bit address, Tag = bits 63-10, Index = bits 9-5, Offset = bits 4-0.
q4_block_size_bytes = None
q4_number_of_blocks = None
#     Split byte address 3100 (decimal)
q4_tag    = None
q4_index  = None
q4_offset = None

# Q5  (Final 2024) 128 KB cache, 16-byte blocks, 4-way set associative, 32-bit address.
q5_sets       = None
q5_index_bits = None
q5_tag_bits   = None

# Q6  (Fig 5.6) 8-block DM cache, 1-word blocks, WORD addresses. Address 26.
q6_index = None   # give as int, e.g. 0b101 or 5
q6_tag   = None

# Q7  Same 8-block cache. Which word address is in slot with index 010 and tag 10? (book: j*8 + i)
q7_address = None


# ---------------- checker (don't peek) ----------------
check("Q1 offset bits", q1_offset_bits, 6)
check("Q1 index bits", q1_index_bits, 8)
check("Q1 tag bits", q1_tag_bits, 18)
check("Q2 block address", q2_block_address, 75)
check("Q2 cache block", q2_cache_block, 11)
check("Q2 first byte", q2_first_byte_in_block, 1200)
check("Q2 last byte", q2_last_byte_in_block, 1215)
check("Q3 address bits", q3_address_bits, 16)
check("Q3 offset bits", q3_offset_bits, 4)
check("Q3 index bits", q3_index_bits, 8)
check("Q3 tag bits", q3_tag_bits, 4)
check("Q3 tag of 0x0C14", q3_tag, 0x0)
check("Q3 index of 0x0C14", q3_index, 0xC1)
check("Q3 offset of 0x0C14", q3_offset, 0x4)
check("Q4 block size", q4_block_size_bytes, 32)
check("Q4 #blocks", q4_number_of_blocks, 32)
check("Q4 tag of 3100", q4_tag, 3)
check("Q4 index of 3100", q4_index, 0)
check("Q4 offset of 3100", q4_offset, 28)
check("Q5 sets", q5_sets, 2048)
check("Q5 index bits", q5_index_bits, 11)
check("Q5 tag bits", q5_tag_bits, 17)
check("Q6 index of 26", q6_index, 0b010)
check("Q6 tag of 26", q6_tag, 0b11)
check("Q7 address", q7_address, 18)
score()
