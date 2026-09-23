# LAB 1 STEP 2 / 2  -  bit stuffing
#
# Rule: walk the bits, count consecutive 1s. The moment the count reaches 5,
#       insert a '0' after it and reset the count. Any '0' in the data resets the count.
#
# You need three things: the output string, a counter of consecutive 1s, a counter of inserted bits.

def bit_stuff(data):
    stuffed  = ""
    ones     = 0
    inserted = 0
    for bit in data:
        # TODO: add bit to stuffed
        stuffed = stuffed + bit
        # TODO: if bit is '1': ones += 1, and if ones == 5: add '0', inserted += 1, ones = 0
        if(bit=='1'):
            ones += 1
            if(ones == 5): 
                stuffed += '0'
                ones = 0
                inserted += 1
        # TODO: else: ones = 0
        else : 
            ones = 0
        pass
    return stuffed, inserted


# ---------------- checker: don't edit below ----------------
tests = {
    "01111110":     ("011111010", 1),
    "0111111111":   ("01111101111", 1),
    "1111111111":   ("111110111110", 2),
    "0110111111100":("01101111101100", 1),
    "1010":         ("1010", 0),
}
ok = True
for data, (s, n) in tests.items():
    got = bit_stuff(data)
    good = got == (s, n)
    ok &= good
    print(f"{data:14s} -> {got}   {'ok' if good else f'expected {(s, n)}'}")
print("PASS  ->  Lab 1 done. Read Q1/Q3/Q4 once in the cheat sheet, then pcm.py" if ok else "FAIL")
