# STEP 1 / 6  -  NRZ-L  (L = LEVEL: the voltage level itself says the bit)
#
# Rule (textbook convention, same as the lab notebook):
#     bit '0'  ->  +1  (High)
#     bit '1'  ->  -1  (Low)
#
# A signal is just a Python list of levels, ONE number per bit.
# Fill in the TODO, then run:   python CE/practice/step1_nrz_l.py

bits = "10110010"


def nrz_l(bits):
    signal = []
    for b in bits:
        # TODO: if b is '0' append 1 to signal, otherwise append -1
        if b=='0':
            signal.append(1)
        else :
            signal.append(-1)
        pass
    return signal


# ---------------- checker: don't edit below ----------------
out = nrz_l(bits)
expected = [-1, 1, -1, -1, 1, 1, -1, 1]
print("Bit stream :", bits)
print("Your output:", out)
print("PASS  ->  open step2_nrz_i.py" if out == expected else f"FAIL  ->  expected {expected}")
