# Gini Impurity By Hand — The Marble Bag Game 🎱

## Why does Gini exist?
A decision tree must choose **which question to ask first** ("split on Weather or Temperature?"). A good question sorts data into piles that are as **unmixed** as possible. So we need a number that measures "how mixed is this pile" — that number is **impurity**.

## What Gini actually means
**Gini = 1 − Σ p²** where p = fraction of each class in the pile.

The story: a pile is a bag of marbles (Yes-marbles, No-marbles).
- Draw a marble, then **guess its color by drawing a second one** and copying it.
- **Σp² = probability the two draws match** (p_yes² + p_no²).
- **Gini = 1 − Σp² = probability you guess WRONG.**

So Gini is literally: *"if I label a random member of this pile by the pile's own mix, how often am I wrong?"*
- Pure pile (all Yes): p=1 → Gini = 1−1 = **0** (never wrong — perfect pile)
- 50/50 pile: 1−(0.5²+0.5²) = **0.5** (max for 2 classes — coin-flip chaos)
- 75/25 pile: 1−(0.5625+0.0625) = **0.375** (mostly sorted)

A split is good if the **children's average Gini is much lower than the parent's** — that drop is the **Information Gain**:
**IG = Gini(parent) − Σ (childSize/parentSize) · Gini(child)**

## THE RECIPE (works on every exam version)
1. **Parent impurity:** count classes over all rows → Gini.
2. For each candidate feature: **sort the rows into piles** by that feature's value.
3. **Gini of each pile** (count Yes/No inside the pile only).
4. **Weighted average** of pile Ginis — weight = pile size / total rows.
5. **IG = parent − weighted average.** Do this per feature; **biggest IG wins the split.**

## The 2024-final problem, step by step
| # | Weather | Temp | Class |
|---|---|---|---|
| 1 | Sunny | Hot | No |
| 2 | Sunny | Hot | No |
| 3 | Overcast | Hot | Yes |
| 4 | Rain | Mild | Yes |
| 5 | Rain | Cool | Yes |
| 6 | Rain | Cool | No |
| 7 | Overcast | Cool | Yes |
| 8 | Sunny | Mild | No |

**Step 1 — parent:** 4 Yes, 4 No → Gini = 1 − (4/8)² − (4/8)² = 1 − 0.25 − 0.25 = **0.5**

**Step 2–4 — split by Weather:**
- Sunny = rows {1,2,8} → {No,No,No} → 3 rows, pure → Gini **0**
- Overcast = rows {3,7} → {Yes,Yes} → 2 rows, pure → Gini **0**
- Rain = rows {4,5,6} → {Yes,Yes,No} → Gini = 1 − (2/3)² − (1/3)² = 1 − 4/9 − 1/9 = **4/9**
- Weighted = (3/8)(0) + (2/8)(0) + (3/8)(4/9) = 12/72 = **1/6 ≈ 0.167**

**Step 5:** IG(Weather) = 0.5 − 0.167 = **0.333**

**Same for Temperature:**
- Hot = {1,2,3} → {No,No,Yes} → 1 − (1/3)² − (2/3)² = **4/9**
- Mild = {4,8} → {Yes,No} → 50/50 → **0.5**
- Cool = {5,6,7} → {Yes,No,Yes} → **4/9**
- Weighted = (3/8)(4/9) + (2/8)(0.5) + (3/8)(4/9) = 1/6 + 1/8 + 1/6 = **0.458**
- IG(Temp) = 0.5 − 0.458 = **0.042**

**Verdict: split on Weather (0.333 ≫ 0.042).**

Sanity check without math: Weather instantly produces TWO pure piles (Sunny=all No, Overcast=all Yes) — only Rain stays messy. Temperature leaves every pile mixed. Of course Weather wins; the math just proves it.

## Why Gini and not "just count errors"?
Classification error (1 − max p) is **insensitive**: in the (40,40)→A vs B problem, it scores both splits identically (IG 0.25), but split B makes one child **completely pure** — clearly better. Gini uses p², so it rewards *how pure* each child is, not just the majority count. Entropy (−Σp log₂p) behaves like Gini; Gini is the default (e.g. sklearn) because it's cheaper (no logarithms).

## Exam speed-ups
- Pure pile → write Gini = 0 instantly, no formula needed.
- 50/50 pile → 0.5. {2/3, 1/3} pile → 4/9. (These three cover most exam piles.)
- Weights are just (pile size / total) — they must sum to 1.
- Show IG for BOTH features and end with "choose X because higher information gain" — that's the rubric line.
