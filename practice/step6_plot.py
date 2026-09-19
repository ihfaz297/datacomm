# STEP 6 / 6  -  The plot. One helper, works for ALL four schemes.
#
# Paste your working functions from steps 1-5 into the marked spots, then fill the
# TODOs in plot_signal. Run it: it saves practice/step6.png (and opens a window).
#
# Marks breakdown from the lab sheet, so you know what each line is worth:
#   - the waveform itself                 (plot)
#   - bit boundaries                      (vertical lines at 0,1,2,...)
#   - signal levels labelled              (yticks: Low / High)
#   - axes labelled                       (xlabel / ylabel / title)

import matplotlib.pyplot as plt

bits = "10110010"


# ---- paste your encoders here (steps 1-4) ----
def nrz_l(bits):
    pass

def nrz_i(bits):
    pass

def manchester(bits):
    pass

def diff_manchester(bits):
    pass


# ---- paste steps() here (step 5) ----
def steps(signal, k):
    pass


def plot_signal(ax, bits, signal, title):
    k = len(signal) // len(bits)          # 1 for NRZ, 2 for Manchester family

    t, y = steps(signal, k)
    # TODO: ax.plot(t, y, drawstyle='steps-post', linewidth=2)

    # TODO: bit boundaries: for i in range(len(bits) + 1): ax.axvline(i, color='red', linestyle='--', alpha=0.5)

    # mid-bit lines only make sense when there are 2 halves per bit
    if k == 2:
        for i in range(len(bits)):
            ax.axvline(i + 0.5, color='blue', linestyle=':', alpha=0.5)

    # bit labels above the waveform
    for i, b in enumerate(bits):
        ax.text(i + 0.5, 1.3, b, ha='center', fontsize=12, fontweight='bold')

    ax.set_title(title)
    ax.set_xlim(0, len(bits))
    ax.set_ylim(-1.5, 1.5)
    # TODO: ax.set_yticks([-1, 1])  and  ax.set_yticklabels(["Low", "High"])
    # TODO: ax.set_xlabel("Bit Time")  and  ax.set_ylabel("Level")
    ax.grid(axis='y', alpha=0.3)


# ---------------- draw all four ----------------
fig, axes = plt.subplots(4, 1, figsize=(12, 10))
plot_signal(axes[0], bits, nrz_l(bits),           "NRZ-L")
plot_signal(axes[1], bits, nrz_i(bits),           "NRZ-I")
plot_signal(axes[2], bits, manchester(bits),      "Manchester (0 = High-to-Low, 1 = Low-to-High)")
plot_signal(axes[3], bits, diff_manchester(bits), "Differential Manchester")
plt.tight_layout()
plt.savefig("practice/step6.png", dpi=80)
print("saved practice/step6.png  ->  tell Claude 'step 6 done' and it will look at the picture")
plt.show()
