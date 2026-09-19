# STEP 3 / 6  -  Manchester  (NRZ-L + a forced transition in the MIDDLE of every bit)
#
# Each bit now has TWO halves, so the list gets TWO numbers per bit (16 for 8 bits).
#
# Rule:
#     bit '0'  ->  High then Low   ->  [ 1, -1]
#     bit '1'  ->  Low  then High  ->  [-1,  1]
#
# Hint: signal.append(x) adds ONE value.  signal.extend([a, b]) adds TWO.

bits = "10110010"


def manchester(bits):
    signal = []
    for b in bits:
        # TODO: if b is '0' extend with [1, -1], otherwise extend with [-1, 1]
        pass
    return signal


# ---------------- checker: don't edit below ----------------
out = manchester(bits)
expected = [-1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1]
print("Bit stream :", bits)
print("Your output:", out, f"({len(out)} values)")
print("PASS  ->  open step4_diff_manchester.py" if out == expected else f"FAIL  ->  expected {expected}")
