# STEP 5 / 6  -  Turning a list of levels into something matplotlib can draw
#
# Matplotlib draws lines between (x, y) points. A digital waveform is FLAT during
# each level, then jumps. So every level v at index i becomes a flat segment:
#
#       from time  i/k   to time  (i+1)/k      at height v
#
# where k = how many levels per bit (1 for NRZ, 2 for Manchester family).
# We produce two lists:  t = [start, end, start, end, ...]   y = [v, v, v, v, ...]
#
# Example, k = 1, signal [ -1, 1 ]:
#       t = [0, 1, 1, 2]        y = [-1, -1, 1, 1]
# Example, k = 2, signal [ 1, -1, -1, 1 ]  (2 bits):
#       t = [0, 0.5, 0.5, 1, 1, 1.5, 1.5, 2]     y = [1, 1, -1, -1, -1, -1, 1, 1]

def steps(signal, k):
    t = []
    y = []
    for i, v in enumerate(signal):
        # TODO: t.extend([ start, end ])   with start = i / k  and end = (i + 1) / k
        # TODO: y.extend([ v, v ])
        pass
    return t, y


# ---------------- checker: don't edit below ----------------
ok = True
t, y = steps([-1, 1], 1)
print("k=1  t =", t, " y =", y)
ok &= (t == [0, 1, 1, 2] and y == [-1, -1, 1, 1])
t, y = steps([1, -1, -1, 1], 2)
print("k=2  t =", t, " y =", y)
ok &= (t == [0, 0.5, 0.5, 1, 1, 1.5, 1.5, 2] and y == [1, 1, -1, -1, -1, -1, 1, 1])
print("PASS  ->  open step6_plot.py" if ok else "FAIL  ->  compare with the examples in the comment above")
