# Perceptron Trained By Hand — The Bouncer Learns 🚪

**Setup.** Four people, owner gives ground truth:

| Person | Coolness x₁ | Dress x₂ | Truth y |
|---|---|---|---|
| Alex | 4 | 3 | +1 (in) |
| Blake | 1 | 1 | −1 (out) |
| Cara | 3 | 4 | +1 (in) |
| Dan | 2 | 1 | −1 (out) |

Init w = [w₀, w₁, w₂] = [0, 0, 0], η = 0.5, x₀ = 1 (bias input).

**Per person:** z = w₀ + w₁x₁ + w₂x₂ → ŷ = +1 if z ≥ 0 else −1 → if wrong, Δwⱼ = η(y−ŷ)xⱼ.
With η = 0.5 and (y−ŷ) = ±2, a mistake means simply **w += x** (missed VIP) or **w −= x** (scrub let in). Correct → no update.

## Epoch 1
| Person | z | ŷ | y | update → new w |
|---|---|---|---|---|
| Alex | 0 | +1 | +1 | ✓ — |
| Blake | 0 | +1 | −1 | ✗ w −= [1,1,1] → **[−1,−1,−1]** |
| Cara | −1−3−4 = −8 | −1 | +1 | ✗ w += [1,3,4] → **[0,2,3]** |
| Dan | 0+4+3 = 7 | +1 | −1 | ✗ w −= [1,2,1] → **[−1,0,2]** |

## Epoch 2
| Person | z | ŷ | y | update → new w |
|---|---|---|---|---|
| Alex | −1+0+6 = 5 | +1 | +1 | ✓ |
| Blake | −1+0+2 = 1 | +1 | −1 | ✗ → **[−2,−1,1]** |
| Cara | −2−3+4 = −1 | −1 | +1 | ✗ → **[−1,2,5]** |
| Dan | −1+4+5 = 8 | +1 | −1 | ✗ → **[−2,0,4]** |

## Epoch 3
| Person | z | ŷ | y | update → new w |
|---|---|---|---|---|
| Alex | −2+0+12 = 10 | +1 | +1 | ✓ |
| Blake | −2+0+4 = 2 | +1 | −1 | ✗ → **[−3,−1,3]** |
| Cara | −3−3+12 = 6 | +1 | +1 | ✓ |
| Dan | −3−2+3 = −2 | −1 | −1 | ✓ |

## Epoch 4 — all correct → converged
z values with w = [−3,−1,3]: Alex 2 ✓, Blake −1 ✓, Cara 6 ✓, Dan −2 ✓.

**Final rule:** −3 − x₁ + 3x₂ ≥ 0 → boundary line **x₂ = 1 + x₁/3**

```
Dress (x2)
 4 |          C(+)          .
 3 |            .    A(+)     <- x2 = 1 + x1/3
 2 |     .
 1 |. B(-)   D(-)
   +---------------------------> Coolness (x1)
     1    2    3    4
```

## Takeaways (exam gold)
- **Weights change only on mistakes.** Error = (y−ŷ) is 0, +2, or −2. Missed positive → weights pushed *toward* the point (+2ηx); false positive → pushed *away* (−2ηx).
- **η = volume knob** — scales how violently one mistake moves the line. **xⱼ scales blame** — the feature that was large during the mistake gets the biggest adjustment.
- **The model learns from data, not intuition:** final weights say dress (+3) is what separates the classes; coolness (−1) even counts slightly against — because that's the line that separates *these four people*.
- **Perceptron stops at the FIRST separating line, not the best one** (Alex z=2, Blake z=−1 — both nearly on the boundary). Motivation for **Adaline** (continuous cost — *how* wrong matters) and **SVM** (maximize margin).
- **Not linearly separable → never converges** — some point stays misclassified every epoch, weights update forever. Hence: cap max epochs; requirement of linear separability.
