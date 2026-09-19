# Lab 2 Exam Guide — Line Coding in Python (NRZ-L, NRZ-I, Manchester, Diff. Manchester)

Every question in Lab 2 is the **same program with one function swapped**.

---

## 0. The one idea that makes all four schemes trivial

A digital signal is just a **list of voltage levels over time**.

- NRZ-L / NRZ-I: **1 level per bit** -> for `"10110010"` the list has 8 numbers.
- Manchester / Diff. Manchester: **2 levels per bit** (first half, second half) -> 16 numbers.

Encoding = walk through the bits, decide the level(s), append to the list.
Plotting = draw each level as a flat horizontal step. Done.

You do **not** need to memorise the 150-line notebook. You need:
1. `bits = "..."`
2. one small `encode(bits)` function (the rule)
3. one `plot_signal(...)` helper (same for all schemes)
4. call, print, plot.

---

## 1. The four rules (memorise this table, it's the whole exam)

Convention = exactly Forouzan Fig 4.6 / 4.8 = exactly what the lab notebook used.

| Scheme | Rule in words | Code line | Start level |
|---|---|---|---|
| **NRZ-L** | **Level** says the bit. 0 -> High, 1 -> Low | `1 if b=='0' else -1` | – |
| **NRZ-I** | **Invert** (flip) on 1, stay on 0 | `if b=='1': level = -level` | +1 |
| **Manchester** | Mid-bit transition direction says the bit. 0 -> High-to-Low, 1 -> Low-to-High | `[1,-1] if b=='0' else [-1,1]` | – |
| **Diff. Manchester** | Flip at **start** if 0, don't if 1. **Always** flip at middle | `if b=='0': level=-level` ... then `level=-level` for the middle | +1 |

Mnemonic: **L = Level, I = Invert.** Manchester is NRZ-L with a forced middle transition.
Differential Manchester is NRZ-I with a forced middle transition.

If ma'am gives a **different convention** (e.g. 1 -> High), you flip ONE comparison or ONE
number. Read her rule, then edit the line. Don't rewrite.

---

## 2. Hand-trace for `10110010` (so you can check your printed output)

Do this on rough paper in the exam BEFORE running. If your print matches, you're done.

```
bit:        1    0    1    1    0    0    1    0
NRZ-L:     -1   +1   -1   -1   +1   +1   -1   +1       (1->Low, 0->High)
NRZ-I:     -1   -1   +1   -1   -1   -1   +1   +1       (start +1; flip on every 1)
```
NRZ-I trace: start +1 -> bit1 flip -> -1 -> bit0 stay -1 -> bit1 flip -> +1 -> bit1 flip -> -1
-> 0 stay -> 0 stay -> bit1 flip -> +1 -> 0 stay +1.

```
Manchester  (0 = H,L   1 = L,H)
bit:      1      0      1      1      0      0      1      0
halves:  -1,+1  +1,-1  -1,+1  -1,+1  +1,-1  +1,-1  -1,+1  +1,-1

Diff. Manchester (start High; 0 = flip at start; ALWAYS flip at middle)
bit:      1      0      1      1      0      0      1      0
halves:  +1,-1  +1,-1  -1,+1  +1,-1  +1,-1  +1,-1  -1,+1  -1,+1
```
Diff. Manchester trace: level=+1.
bit 1: no flip -> +1, mid flip -> -1.
bit 0: flip -> +1, mid -> -1.
bit 1: no flip -> -1, mid -> +1.
bit 1: no flip -> +1, mid -> -1.
bit 0: flip -> +1, mid -> -1.
bit 0: flip -> +1, mid -> -1.
bit 1: no flip -> -1, mid -> +1.
bit 0: flip -> -1, mid -> +1.

Expected prints (these are the notebook's exact outputs):
```
NRZ-L : [-1, 1, -1, -1, 1, 1, -1, 1]
NRZ-I : [-1, -1, 1, -1, -1, -1, 1, 1]
Manch : [-1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1]
DiffM : [1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1]
```

---

## 3. THE TEMPLATE (~40 lines; works for every scheme)

Build it **in this order** in separate Colab cells. That is the "procedural" ma'am wants,
and each cell is a checkpoint that earns marks even if the next one breaks.

### Cell 1 — input  [2 marks]
```python
import matplotlib.pyplot as plt

bits = "10110010"                    # or: bits = input("Enter bit stream: ")
print("Bit Stream:", bits)
```

### Cell 2 — the encoder(s)  [5–7 marks each]
```python
def nrz_l(bits):
    signal = []
    for b in bits:
        if b == '0':
            signal.append(1)         # 0 -> High
        else:
            signal.append(-1)        # 1 -> Low
    return signal

def nrz_i(bits):
    signal = []
    level = 1                        # initial level High
    for b in bits:
        if b == '1':
            level = -level           # 1 -> invert
        signal.append(level)         # 0 -> keep
    return signal

def manchester(bits):
    signal = []
    for b in bits:
        if b == '0':
            signal.extend([1, -1])   # 0 -> High then Low
        else:
            signal.extend([-1, 1])   # 1 -> Low then High
    return signal

def diff_manchester(bits):
    signal = []
    level = 1                        # initial level High
    for b in bits:
        if b == '0':
            level = -level           # 0 -> transition at beginning
        signal.append(level)         # first half
        level = -level               # middle transition (always)
        signal.append(level)         # second half
    return signal
```

### Cell 3 — display the values  [3 marks]
```python
signal = manchester(bits)            # swap the function name per question
print("Encoded signal:", signal)
```

### Cell 4 — the plot helper (SAME for every scheme)  [5 marks + 3 for labels]
```python
def plot_signal(ax, bits, signal, title):
    k = len(signal) // len(bits)     # 1 = one level per bit, 2 = two halves per bit

    t, y = [], []
    for i, v in enumerate(signal):   # each level becomes a flat step
        t.extend([i / k, (i + 1) / k])
        y.extend([v, v])
    ax.plot(t, y, drawstyle='steps-post', linewidth=2)

    for i in range(len(bits) + 1):   # bit boundaries
        ax.axvline(i, color='red', linestyle='--', alpha=0.5)
    if k == 2:                       # mid-bit transitions
        for i in range(len(bits)):
            ax.axvline(i + 0.5, color='blue', linestyle=':', alpha=0.5)

    for i, b in enumerate(bits):     # bit labels on top
        ax.text(i + 0.5, 1.3, b, ha='center', fontsize=12, fontweight='bold')

    ax.set_title(title)
    ax.set_xlim(0, len(bits))
    ax.set_ylim(-1.5, 1.5)
    ax.set_yticks([-1, 1])
    ax.set_yticklabels(["Low (-1)", "High (+1)"])
    ax.set_xlabel("Bit Time")
    ax.set_ylabel("Signal Level")
    ax.grid(axis='y', alpha=0.3)
```

### Cell 5 — draw  (Q1 wants 2 signals, Q2/Q3 want "original bits + encoded")
```python
fig, axes = plt.subplots(2, 1, figsize=(12, 6))
plot_signal(axes[0], bits, nrz_l(bits), "NRZ-L Encoding")
plot_signal(axes[1], bits, nrz_i(bits), "NRZ-I Encoding")
plt.tight_layout()
plt.show()
```
For "plot the original bit stream" (Q2/Q3), the cheap way is just a bits row:
```python
fig, axes = plt.subplots(2, 1, figsize=(12, 6), gridspec_kw={'height_ratios': [1, 2]})

axes[0].set_xlim(0, len(bits)); axes[0].set_ylim(-1, 1); axes[0].set_yticks([])
axes[0].set_title("Original Bit Stream")
for i, b in enumerate(bits):
    axes[0].text(i + 0.5, 0, b, ha='center', va='center', fontsize=14, fontweight='bold')
    axes[0].axvline(i, color='gray', linestyle='--', alpha=0.4)
axes[0].axvline(len(bits), color='gray', linestyle='--', alpha=0.4)

plot_signal(axes[1], bits, manchester(bits), "Manchester Encoding (0 = High-to-Low, 1 = Low-to-High)")
plt.tight_layout()
plt.show()
```
(If short on time, plotting the **NRZ-L** waveform as "the original bit stream"
is also accepted in most labs. It IS the raw bits as levels.)

---

## 4. Why the plot code works (in case she asks "explain your plotting")

- Each level `v` at index `i` must be drawn **flat** from time `i/k` to `(i+1)/k`.
  So we push two time points and the same `v` twice -> a horizontal segment.
- `drawstyle='steps-post'` makes matplotlib join those with **vertical jumps**, not
  slanted lines. That's what makes it look like a digital waveform.
- `k = len(signal)//len(bits)` auto-detects "1 level per bit" vs "2 halves per bit",
  so one helper handles all four schemes.
- `axvline` at every integer = bit boundary; at every `.5` = mid-bit (only meaningful
  for the biphase schemes).

---

## 5. The written-explanation marks (copy these sentences)

**Q2 — "explain the transition in the middle of every bit" [4 marks]**
> In Manchester encoding each bit period is split into two halves and there is always
> a transition at the middle of the bit. The direction of that transition carries the
> data (0 = High-to-Low, 1 = Low-to-High). Because a transition is guaranteed every bit,
> the receiver can recover the clock from the signal itself (self-synchronisation),
> and since every bit spends half its time High and half Low, there is no DC
> component. The cost is that the signal rate is doubled (r = 1/2, S = N baud),
> so it needs twice the bandwidth of NRZ.

**Q3 — "difference between Manchester and Differential Manchester" [3 marks]**
> In Manchester the bit value is given by the *direction* of the mid-bit transition
> (absolute levels, like NRZ-L + RZ). In Differential Manchester the mid-bit transition
> is only for synchronisation; the bit value is given by whether or not there is a
> transition at the *beginning* of the bit (0 = transition, 1 = no transition), i.e. it
> is relative to the previous level, like NRZ-I + RZ. Differential Manchester therefore
> still decodes correctly if the wire polarity is accidentally reversed; Manchester does
> not. Both have r = 1/2, average signal rate N baud, and no DC component.

**Bonus one-liners she may ask:**
- Why NRZ-I over NRZ-L? Long run of 1s in NRZ-L -> baseline wandering + sync loss; NRZ-I
  still has transitions on every 1. Polarity flip breaks NRZ-L, not NRZ-I.
- Signal rate: NRZ average S = N/2 baud; Manchester family S = N baud.
- Bandwidth: minimum B = S, so Manchester needs 2x the bandwidth of NRZ.

---

## 6. Variations ma'am could throw (and the 1-line fix for each)

| If the question says... | Change |
|---|---|
| different bit stream | `bits = "..."` only |
| take input from user | `bits = input("Enter bit stream: ")` |
| NRZ-L: 1 -> High, 0 -> Low | swap the `1` and `-1` in `nrz_l` |
| NRZ-I: initial level Low | `level = -1` |
| NRZ-I: transition on 0 instead of 1 | `if b == '0': level = -level` |
| Manchester: 1 -> High-to-Low (IEEE 802.3 style) | swap the two `extend` lists |
| Diff. Manchester: transition at start for 1 | `if b == '1': level = -level` |
| Diff. Manchester: initial level Low | `level = -1` |
| "use levels 0 and 1 / 0 and 5V" | replace `-1` with `0` (or `5`/`0`), and fix `set_ylim`/`set_yticks` |
| **AMI** (bipolar) | `0 -> 0`, `1 -> alternate +1/-1`: see below |
| **Pseudoternary** | same as AMI with `'0'` and `'1'` swapped |
| **RZ** (polar) | `1 -> [1, 0]`, `0 -> [-1, 0]` — two halves like Manchester |
| **Unipolar NRZ** | `1 -> 1`, `0 -> 0` |
| count transitions / signal rate | `sum(1 for i in range(1,len(s)) if s[i]!=s[i-1])` |

```python
def ami(bits):
    signal = []
    last = -1                        # so first 1 becomes +1
    for b in bits:
        if b == '0':
            signal.append(0)
        else:
            last = -last
            signal.append(last)
    return signal

def rz(bits):
    signal = []
    for b in bits:
        if b == '1':
            signal.extend([1, 0])
        else:
            signal.extend([-1, 0])
    return signal
```
For AMI/RZ set `ax.set_yticks([-1, 0, 1])` and labels `["-V", "0", "+V"]`.

**Decode (if she flips it around — "given signal, recover bits"):**
```python
def decode_nrz_l(signal):
    return "".join('0' if v == 1 else '1' for v in signal)

def decode_manchester(signal):          # look at each pair
    bits = ""
    for i in range(0, len(signal), 2):
        bits += '0' if signal[i] == 1 else '1'   # High-then-Low = 0
    return bits

def decode_nrz_i(signal, start=1):
    bits = ""; prev = start
    for v in signal:
        bits += '1' if v != prev else '0'
        prev = v
    return bits
```

---

## 7. Colab pitfalls that cost people 10 minutes

- Bits are a **string**, so compare with `'0'` (quotes), not `0`.
- `append` adds one value; `extend` adds a list of values. Manchester needs `extend`.
- Forgot `import matplotlib.pyplot as plt` -> NameError. It goes in cell 1.
- No plot shown -> you forgot `plt.show()` (or you defined the function but never called it).
- Plot looks slanted -> you forgot `drawstyle='steps-post'`.
- Plot is just one flat line -> you passed `bits` (string) instead of `signal` (list).
- `plt.subplots(2, 1)` returns `(fig, axes)`; use `axes[0]`, `axes[1]`. With `subplots(1,1)` there's no indexing, it's just `ax`.
- Run cells **top to bottom** after any edit (Runtime -> Run all) so the function definitions are fresh.

---

## 8. 60-second exam checklist

1. Cell 1: import + `bits` + print. Run.
2. Cell 2: the ONE encoder the question asks for (copy rule from the table). Run.
3. Cell 3: `signal = fn(bits)`; `print(signal)`. **Compare with hand trace.**
4. Cell 4: `plot_signal` helper. Run (nothing shows yet, that's fine).
5. Cell 5: subplots -> call helper -> `plt.show()`.
6. Markdown cell: paste the explanation sentences from section 5.
7. Only then: make it pretty / add the "original bits" row / take `input()`.
