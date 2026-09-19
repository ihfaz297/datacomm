# STEP 4 / 6  -  Differential Manchester  (NRZ-I + a forced transition in the MIDDLE)
#
# Rule (exactly as the lab question states it):
#     bit '0'  ->  transition at the BEGINNING of the bit   (flip level)
#     bit '1'  ->  NO transition at the beginning            (keep level)
#     ALWAYS a transition in the middle of the bit           (flip level again)
#     initial level = +1 (High)
#
# Per bit you do:  [maybe flip]  append  [always flip]  append
# That's it. Two appends per bit -> 16 values.

bits = "10110010"


# def diff_manchester(bits):
#     signal = []
#     level = 1                 # start High
#     for b in bits:
#         # TODO: if b is '0', flip level          (beginning-of-bit transition)
#         # TODO: append level                     (first half)
#         # TODO: flip level                       (middle transition, ALWAYS)
#         # TODO: append level                     (second half)
#         pass
#     return signal
def diff_manchester(bits):
    signal = []
    level = 1
    for b in bits:
        if b=='1':
            level = -level
        signal.extend([-level, level])
        pass
    return signal

# ---------------- checker: don't edit below ----------------
out = diff_manchester(bits)
expected = [1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1]
print("Bit stream :", bits)
print("Your output:", out, f"({len(out)} values)")
print("PASS  ->  open step5_steps.py" if out == expected else f"FAIL  ->  expected {expected}")
