# Naive Bayes By Hand — The Fortune Teller Who Just Counts 🔮

> Not in Ch1–4 slides, but it IS on the 2024 final (Q6c). Free marks: it's counting + multiplying.

## The idea in 3 lines
- Perceptron/logistic **learn a boundary**. Naive Bayes doesn't learn anything — it **counts evidence** and asks: *"given what I'm seeing, which class was most likely to produce it?"*
- **Bayes:** P(class | evidence) ∝ P(class) · P(evidence | class)
- **"Naive"** = assume the features are independent given the class, so the joint likelihood factorizes into a product of easy per-feature counts:

**score(class) = P(class) · P(x₁|class) · P(x₂|class) · … · P(xₘ|class)**

Compute the score for every class, **biggest score wins**. (We can skip the denominator P(evidence) — it's the same for all classes.)

## The 2024 final question, fully worked

Your last 10 days:

| # | Deadline | Weather | Mood | Activity |
|---|---|---|---|---|
| 1 | Urgent | Good | Off | Play |
| 2 | Urgent | Bad | Off | Study |
| 3 | Near | Good | Off | Play |
| 4 | None | Good | Off | Play |
| 5 | None | Bad | On | Sleep |
| 6 | None | Good | Off | Play |
| 7 | Near | Bad | On | Study |
| 8 | Near | Bad | Off | Sleep |
| 9 | Near | Good | Off | Play |
| 10 | Urgent | Bad | On | Study |

**(i) Priors** — just class fractions:
- P(Play) = 5/10 = 0.5 · P(Study) = 3/10 = 0.3 · P(Sleep) = 2/10 = 0.2

**(ii) Tonight: Deadline = Near, Weather = Bad, Mood = Off. What do you do?**

Build likelihoods by counting *within each class*:

| | Play (5 rows) | Study (3 rows) | Sleep (2 rows) |
|---|---|---|---|
| P(Near \| class) | 2/5 | 1/3 | 1/2 |
| P(Bad \| class) | **0/5** | 3/3 = 1 | 2/2 = 1 |
| P(Off \| class) | 5/5 = 1 | 1/3 | 1/2 |

(Check Play's counts: Play rows are 1,3,4,6,9 → deadlines U,N,N,N,N... wait: Urgent, Near, None, None, Near → Near appears 2 times → 2/5. Weather: all Good → Bad 0/5. Mood: all Off → 5/5.)

Multiply everything per class:

- **Play:** 0.5 × 2/5 × **0** × 1 = **0** ← one zero kills the whole product
- **Study:** 0.3 × 1/3 × 1 × 1/3 = 1/30 ≈ **0.033**
- **Sleep:** 0.2 × 1/2 × 1 × 1/2 = 1/20 = **0.05** ← winner

**Answer: you will Sleep.** 😴

Optional flex — normalize to real probabilities: P(Sleep) = 0.05/(0.05+0.033) = **60%**, P(Study) = 40%, P(Play) = 0%.

## The zero-probability trap (mention this for bonus credit)
You've *never* played in bad weather, so P(Bad|Play) = 0 nukes Play to score 0 — even if every other feature screamed "Play". One unseen combo shouldn't mean "impossible."

**Fix: Laplace (add-1) smoothing** — add 1 to every count:
P(Bad | Play) = (0 + 1)/(5 + 2) = 1/7   (denominator: 5 Play rows + 2 possible weather values)
Now nothing is ever exactly zero.

## Why Alvee runs this in production
- **Trains in one pass** (just counting) — milliseconds, no gradient descent, no tuning.
- Handles **huge feature counts** (10k+ words in spam filtering) and works decently with little data.
- Outputs probabilities, updates trivially with new data.
- Weakness: the independence assumption is a lie (words co-occur!) — probabilities get overconfident, but the *ranking* (argmax) usually stays right, which is all a classifier needs.

## Exam recipe (memorize)
1. Priors = class counts / total.
2. For each class: multiply prior × P(each observed feature value | class), counting within that class's rows only.
3. Biggest product wins. If a zero appears, say the word "Laplace smoothing."
