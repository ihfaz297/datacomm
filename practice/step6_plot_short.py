# The same plot as step6_plot.py, without the hand-built t/y lists.
# ax.stairs(values, edges) draws a step waveform directly: one value per step,
# and len(values)+1 edge times. The x-grid at integer ticks gives bit boundaries.

import matplotlib.pyplot as plt

bits = "10110010"


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


def plot_signal(ax, bits, signal, title):
    k = len(signal) // len(bits)                              # levels per bit
    edges = [i / k for i in range(len(signal) + 1)]           # 0, 1/k, 2/k, ...
    ax.stairs(signal, edges, baseline=None, linewidth=2)      # the waveform
    ax.set_xticks(range(len(bits) + 1))                       # bit boundaries
    ax.grid(axis='x', linestyle='--', color='red', alpha=0.5)
    ax.secondary_xaxis('top').set_xticks([i + 0.5 for i in range(len(bits))], list(bits))  # bit labels
    ax.set_yticks([-1, 1], ["Low", "High"])
    ax.set_xlim(0, len(bits))
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(title)
    ax.set_xlabel("Bit Time")
    ax.set_ylabel("Level")


fig, axes = plt.subplots(4, 1, figsize=(12, 10))
plot_signal(axes[0], bits, nrz_l(bits), "NRZ-L")
plot_signal(axes[1], bits, nrz_i(bits), "NRZ-I")
plot_signal(axes[2], bits, manchester(bits), "Manchester")
plot_signal(axes[3], bits, diff_manchester(bits), "Differential Manchester")
plt.tight_layout()
plt.show()
