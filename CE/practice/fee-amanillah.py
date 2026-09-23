import matplotlib.pyplot as plt

bits = input("Enter bit stream")

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

def show(signal, title, k):
    plt.figure(figsize=(10,2.5))
    plt.stairs(signal, [i/k for i in range (len(signal)+1)], baseline=None, linewidth=2)
    plt.xticks(range(len(bits)+1))
    plt.grid(axis='x')
    plt.yticks([min(signal), max(signal)],["Low","High"])
    plt.ylim(min(signal)-0.5, max(signal)+0.5)
    plt.title(title)
    plt.xlabel("Bit Time")
    plt.ylabel("level")
    plt.tight_layout()

show([int(b) for b in bits], "Original stream: " + bits, 1)
signal = nrz_l(bits)
show(signal, "NRZ-L", 1)
signal = nrz_i(bits)
show(signal, "NRZ-I", 1)
signal = manchester(bits)
show(signal, "Manchester", 2)
signal = diff_manchester(bits)
show(signal, "Differential Manchester", 2)
plt.show()