# Doomsday version: ONE plotting function, six lines, memorise only this.
# Called once for the original bits and once per scheme.

import matplotlib.pyplot as plt

bits = input("Enter bit stream: ") or "10110010"      # Enter alone keeps the given stream


def nrz_l(bits):
    return [1 if b == '0' else -1 for b in bits]

def nrz_i(bits):
    signal, level = [], 1
    for b in bits:
        if b == '1':
            level = -level
        signal.append(level)
    return signal

def manchester(bits):
    signal = []
    for b in bits:
        signal.extend([1, -1] if b == '0' else [-1, 1])
    return signal

def diff_manchester(bits):
    signal, level = [], 1
    for b in bits:
        if b == '1':
            level = -level
        signal.extend([-level, level])
    return signal


def show(signal, title):
    k = len(signal) // len(bits)                                         # levels per bit
    plt.figure(figsize=(10, 2.5))
    plt.stairs(signal, [i / k for i in range(len(signal) + 1)], baseline=None, linewidth=2)
    plt.xticks(range(len(bits) + 1))
    plt.grid(axis='x')                # bit boundaries
    if k == 2: [plt.axvline(i + 0.5, linestyle=':') for i in range(len(bits))]   # mid-bit
    plt.yticks([min(signal), max(signal)], ["Low", "High"])
    plt.ylim(min(signal) - .5, max(signal) + .5)
    plt.title(title); plt.xlabel("Bit Time")
    plt.ylabel("Level")
    plt.tight_layout()


print("Bit stream:", bits)
show([int(b) for b in bits], "Original bit stream " + bits)

for name, fn in [("NRZ-L", nrz_l), ("NRZ-I", nrz_i),
                 ("Manchester", manchester), ("Differential Manchester", diff_manchester)]:
    signal = fn(bits)
    #print(f"{name:24s}: {signal}")
    show(signal, name)

plt.show()
