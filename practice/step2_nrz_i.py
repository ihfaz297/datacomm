# STEP 2 / 6  -  NRZ-I  (I = INVERT: a CHANGE of level says the bit)
#
# Rule:
#     bit '1'  ->  flip the current level      (transition)
#     bit '0'  ->  keep the current level      (no transition)
#     initial level = +1 (High)
#
# So you need a variable that REMEMBERS the current level between bits.
# Hint: flipping is   level = -level

bits = "10110010"


def nrz_i(bits):
    signal = []
    level = 1                 # start High
    for b in bits:
        # TODO: if b is '1', flip level
        if b =='1':
            level = -level
        # TODO: append level to signal (for BOTH cases)
        signal.append(level)
        pass
    return signal


# ---------------- checker: don't edit below ----------------
out = nrz_i(bits)
expected = [-1, -1, 1, -1, -1, -1, 1, 1]
print("Bit stream :", bits)
print("Your output:", out)
print("PASS  ->  open step3_manchester.py" if out == expected else f"FAIL  ->  expected {expected}")
