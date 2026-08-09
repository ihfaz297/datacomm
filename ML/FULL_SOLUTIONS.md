# CSE 475 — TT1 SOLUTIONS (scoped to Ch1–Ch4)
**Today = TT1.** Past TT1 papers (19-TT1, 20-TT1) draw from **Ch1 (intro) + Ch2 (perceptron/Adaline/GD/scaling)** with a few **Ch3** dips (slack variable, KNN, impurity). Ch4 (preprocessing) included since it's in your deck set.
**Removed as out-of-scope (final-exam material):** neural nets/CNN/RNN/Keras, NLP/BoW/TF-IDF, Naive Bayes, k-means, boosting, confusion-matrix numericals, nested CV/ROC. All of that still lives in `exam_prep.md` + `naive_bayes_by_hand.md` for the final.

---

# 🔥 THE TT1 HOT LIST — the actual questions from both past TT1 papers
These 12 ARE the exam until proven otherwise. Full answers below (follow the links by number).

1. When do you apply RL? Diagram. → **A1**
2. Steps to build a supervised ML system → **B1**
3. How do you select the best-performing model? → **A2**
4. How do you know the model performs well on unseen data? → **A3**
5. Perceptron ↔ biological neuron → **B2**
6. What cost function is applied for Adaline? → **A4**
7. Linearly separable vs not + figure → **B4**
8. Learning rate role in gradient descent + figure → **B3**
9. Importance of feature scaling + example technique → **B5**
10. Disadvantage of batch gradient descent → **A5**
11. *(20-TT1 extras)* Role of slack variable in SVM → **A11** · Advantages/disadvantages of non-parametric model (KNN) → **A12** · Most impure node among (20,20),(40,0),(30,10) → **A13**

---

# PART A — 2-mark short answers

### A1. When do you apply reinforcement learning? Show with a diagram how RL works. `[19TT1, 20TT1]`
Apply RL when there are **no labeled examples**, but an agent makes **sequential decisions** and receives **delayed feedback** — games (chess), robotics, self-driving. The **agent** takes an **action** on the **environment**; the environment returns the new **state** and a **reward**; by trial-and-error the agent learns a policy of actions that maximizes cumulative reward.
```
        ┌────────── action ──────────┐
   [ AGENT ]                    [ ENVIRONMENT ]
        └──── state, reward ◄────────┘
```

### A2. How do you select a best-performing ML model? `[19TT1, 20TT1]`
Train **several candidate algorithms** on the training data, tune each one's hyperparameters using **cross-validation** (train on part of the training data, validate on the rest), and select the model/configuration with the best validation score. Finally confirm on the untouched test set.

### A3. How do you know your model performs well on unseen data? `[19TT1, 20TT1]`
Evaluate it on a **held-out test set** that was never used for training or tuning — its performance is an unbiased estimate of generalization. Small train/validation-test gap → model generalizes.

### A4. What cost function is applied for Adaline? `[19TT1, 20TT1]`
**Sum of Squared Errors:** J(w) = ½ Σᵢ (y⁽ⁱ⁾ − φ(z⁽ⁱ⁾))², where φ(z) = z is the **continuous linear activation** (not the thresholded label). J is **convex and differentiable**, so gradient descent is guaranteed to reach the global minimum. (Counting misclassifications instead gives a flat, gradient-zero cost — no learning signal.)

### A5. What is the disadvantage of batch gradient descent? `[19TT1, 20TT1]`
Every single weight update computes the gradient over the **entire training set** — for large datasets each update is extremely expensive, and it can't learn online/streaming. Remedies: **SGD** (update per example — noisy but fast) or **mini-batch** (per 32–128 rows — fast + vectorizable, the practical default).

### A6. What is a hyperparameter? Give examples. `[Ch1/Ch3, final-recurring]`
A setting chosen **before** training and not learned from data: learning rate η, number of epochs, k in KNN, regularization C, kernel γ, tree max_depth. (Weights = parameters, learned.) Tuned via validation/cross-validation.

### A7. Traditional programming vs machine learning `[Ch1]`
Traditional: human writes **rules**; rules + data → answers. ML: data + answers (labels) → the algorithm **learns the rules** (model), which then answers for new data.

### A8. What does "k" represent in k-NN? `[Ch3]`
The number of nearest neighbors consulted: the query point receives the **majority class among its k closest** training points under a distance metric (Euclidean p=2 / Manhattan p=1).

### A9. Curse of dimensionality `[Ch3]`
With a fixed dataset, adding dimensions makes the feature space **exponentially sparse** — even the nearest neighbors are far away, so distance-based estimates (KNN especially) become unreliable and overfit. Remedy: feature selection / dimensionality reduction.

### A10. What are outliers? `[Ch4-adjacent]`
Examples that deviate strongly from the rest of the data (measurement error or rare events). They distort means/σ (hence min-max scaling), and squared-error fits. Handle: remove, RobustScaler (median/IQR), or robust fitting (RANSAC: repeatedly fit on random subsets, keep the model with most inliers, refit on inliers).

### A11. Role of the slack variable in SVM `[20TT1]`
Slack ξᵢ ≥ 0 relaxes the hard-margin constraint so sample i may sit inside or across the margin — making the optimization **solvable for non-linearly-separable data** (soft margin). Violations are penalized by C·Σξᵢ: the SVM trades margin width against total slack. Large C → narrow margin, strict; small C → wide margin, tolerant.

### A12. Advantages & disadvantages of a non-parametric model like KNN `[20TT1]`
**Pros:** no training phase, adapts instantly when new data arrives, no assumed functional form. **Cons:** prediction is slow (searches the whole stored training set), memory-heavy, sensitive to feature scaling and irrelevant features, degrades badly in high dimensions (curse of dimensionality).
*Bonus:* KNN is a **lazy learner** — it memorizes rather than learns; all computation is deferred to prediction time. Tie in voting → use odd k / shrink k / weight votes by distance.

### A13. Which is the most impure node among (20,20), (40,0), (30,10)? `[20TT1]`
**(20,20)** — perfect 50/50 mix: Gini = 1−(0.5²+0.5²) = **0.5** (entropy = 1, maximum). (30,10): Gini = 1−(0.75²+0.25²) = 0.375. (40,0): pure, Gini = **0**.

### A14. Missing data: what is it and how do you handle it? `[Ch4]`
Absent entries (blank/NaN/NULL) that most algorithms can't process. Either **remove** affected rows/columns (`dropna` — simple, but loses samples/features) or **impute** — fill with mean/median/most-frequent of the column (`SimpleImputer`), preserving all examples.

### A15. What is an ordinal feature? `[Ch4]`
A categorical feature with an inherent **order** (T-shirt size M < L < XL) → encode as ordered integers (M=1, L=2, XL=3). A **nominal** feature (color) has no order → must be one-hot encoded instead.

### A16. Is logistic regression's output continuous or categorical? `[Ch3]`
Both, at different stages: the sigmoid outputs a **continuous probability** P(y=1|x) ∈ (0,1); after the 0.5 threshold (quantizer), the final classification is **categorical**. Say both for full marks.

### A17. What is bootstrapping in sample selection? `[Ch3 — random forests]`
Drawing a random sample of size n from the training set **with replacement** — the same example can be picked multiple times. Each random-forest tree trains on its own bootstrap sample.

### A18. Why must the activation function be differentiable (for gradient-based learning)? `[Ch2-adjacent]`
Weights are learned by **gradient descent**, which needs ∂J/∂w — and that requires differentiating through the activation. That's exactly why Adaline swaps the perceptron's step function (no useful gradient) for a continuous φ(z)=z: it makes the cost differentiable so the gradient can guide updates.

---

# PART B — 5-mark structured answers

### B1. What steps are required to build a supervised ML system? `[19TT1, 20TT1]`
```
Labels ┐
       ├→ PREPROCESSING → Training set ─→ LEARNING ALGORITHM → FINAL MODEL ─→ PREDICTION
Raw data┘   (clean, scale,  Test set ──────────────────────────↗ (evaluation)     ↓
             split)                                                        labels for new data
```
1) **Preprocessing** — handle missing values, encode categoricals, **scale features**, split train/test. 2) **Training** — fit candidate models on the training set. 3) **Model selection** — compare algorithms + hyperparameters via cross-validation. 4) **Evaluation** — measure the chosen model on the held-out **test set** (unseen data). 5) **Prediction** — deploy on genuinely new data.
*(This same diagram = the "explain each step of the pipeline" question.)*

### B2. How is the perceptron related to a biological neuron? `[19TT1, 20TT1]`
| Biological neuron | Perceptron |
|---|---|
| Dendrites receive input signals | inputs x₁ … xₘ |
| Synaptic strength | weights w₁ … wₘ |
| Cell body integrates signals | net input z = w₀ + wᵀx |
| Fires if signal exceeds threshold | step function: z ≥ 0 → +1 else −1 |
| Axon carries output | prediction ŷ |
The MCP neuron reframed the brain cell as a **logic gate with binary output**; Rosenblatt's rule made the weights **learnable**: wⱼ := wⱼ + η(y − ŷ)xⱼ (updates only on mistakes).
*If they add a compute:* x=[1,−2], w=[0.5,0.25], bias=1 → z = 1 + 0.5(1) + 0.25(−2) = **1.0 ≥ 0 → ŷ = +1**.

### B3. Role of the learning rate when minimizing cost with gradient descent + figure `[19TT1, 20TT1]`
Gradient descent steps opposite the gradient: w := w − η∇J(w); **η scales the step size**.
- **Too large:** overshoots the minimum — cost oscillates or diverges (grows every epoch).
- **Too small:** converges reliably but needs far too many epochs.
```
J(w)  η too large: bounces           η too small: crawls
  \      /\    /\                       \_
   \    /  \  /  \                        \_
    \__/    \/    \__ w                     \__→ min (eventually)
```
Well-chosen η (often with standardized features, e.g. 0.01) → few, direct steps to the minimum.

### B4. Define linearly separable and not linearly separable + figure `[19TT1, 20TT1]`
**Linearly separable:** a single straight line (hyperplane in higher-d) can split the two classes perfectly → the perceptron **converges**.
**Not linearly separable:** no such line exists (classic: XOR) → at least one point stays misclassified every epoch, so perceptron weights **update forever** — cap max epochs, or use models that still converge (Adaline/logistic minimize a continuous cost; kernel SVM bends the boundary).
```
Separable:   - - │ + +        Not separable:   + -        - + +
             - - │ + +                         - +        + - -   (mixed)
```

### B5. Importance of feature scaling + example technique `[19TT1, 20TT1]`
Unscaled features let the largest-range feature **dominate** the cost surface (gradient descent takes skewed, zigzag steps) and distance metrics (KNN/SVM). Scaling makes the cost contours **round and symmetric** → fewer, more direct steps to the minimum; Adaline converges in ~15 epochs at η=0.01 after standardization. **Exception: decision trees / random forests are scale-invariant.**
- **Standardization (example technique):** x′ = (x − μ)/σ → mean 0, unit variance. Preferred for GD/logistic/SVM. Note: does *not* make data normally distributed — only recenters/rescales.
- **Min-max normalization:** x′ = (x − xmin)/(xmax − xmin) → [0,1]; use when a bounded range is needed; sensitive to outliers.
**Worked example (20TT1 asked a fill-table):** inputs 0…5: μ = 2.5, σ ≈ 1.708 →
standardized: −1.46, −0.88, −0.29, 0.29, 0.88, 1.46 · normalized: 0, 0.2, 0.4, 0.6, 0.8, 1.0
Fit μ,σ on **training data only**; reuse them to transform test/new data.

### B6. Perceptron vs Adaline (likely pairing with A4) `[Ch2]`
Same net input z = wᵀx; the difference is **what drives the update**: perceptron uses the **thresholded predicted label** (integer ±1) — updates only on misclassification; Adaline uses the **continuous activation φ(z)=z before thresholding** — update Δw = η Σ(y − φ(z))x from the SSE gradient over the whole training set (batch GD). Continuous error ⇒ differentiable convex cost ⇒ guaranteed convergence behavior and "how wrong" matters, not just "wrong".

### B7. Batch vs Stochastic vs Mini-batch GD `[Ch2]`
| | Batch | SGD | Mini-batch |
|---|---|---|---|
| update uses | all m rows | 1 row | small subset (e.g. 32) |
| updates/epoch | 1 | m | m/batch |
| gradient noise | none | high | moderate |
| best for | small data | streaming/online | large-scale (default) |
Epoch = one full pass over training data; iterations per epoch = ⌈N/batch⌉ (e.g. 60000/128 → 469).

### B8. Slope vs derivative vs gradient `[Ch2-adjacent]`
**Slope** = rise/run of a straight line (constant). **Derivative** = slope of the tangent to a curve at a point: f′(x) = limΔ→0 [f(x+Δ)−f(x)]/Δ. **Gradient** = the **vector of partial derivatives** ∇J = [∂J/∂w₀ … ∂J/∂wₘ] for multivariable functions — points toward steepest ascent; GD steps opposite. Figures: rise/run triangle on a line; tangent touching a curve; contour plot with an arrow uphill.

### B9. One-hot encoding: how + disadvantage `[Ch4]`
Nominal features must not be integer-coded (fakes an order: blue>green>red). Create **one binary column per category**: green→[0,1,0]. **Disadvantages:** column count explodes with many categories, and **multicollinearity** — dummies are linearly dependent (they sum to 1), a problem for matrix-inversion-based methods. **Fix:** drop one redundant column (`drop_first=True`) — no information lost (all-zeros implies the dropped category).

### B10. How does L1 regularization perform feature selection? (vs L2) `[Ch4]`
Regularization adds a weight penalty to the cost to tame complexity. **L2:** λΣw² — circular budget → weights shrink smoothly, rarely to exactly zero ("weight decay"). **L1:** λΣ|w| — **diamond** budget whose **corners sit on the axes**; the cost contours typically first touch a corner, so several weights land at **exactly 0** → sparse solution → irrelevant features automatically eliminated. Stronger λ (smaller C = 1/λ) → more zeros.
```
L2: contours ⟶ ◯ tangent point off-axis (small w's)
L1: contours ⟶ ◇ corner ON axis (some wⱼ = 0)
```

### B11. Why dimensionality reduction + one technique `[Ch4]`
High-dimensional data → sparsity (curse of dimensionality), overfitting, compute cost. Techniques: **feature selection** — L1 regularization; **Sequential Backward Selection**: start with all d features, repeatedly remove the feature whose removal costs least performance until k remain; or **random-forest feature importance** (avg impurity decrease per feature). Feature extraction: PCA — project onto directions of maximum variance.

### B12. SVM is a maximum-margin classifier — explain `[Ch3]`
SVM picks the hyperplane that **maximizes the margin** — the distance to the closest samples, the **support vectors**. With the ±1 hyperplanes wᵀx+w₀ = ±1, the margin = **2/‖w‖**, so SVM minimizes ½‖w‖² subject to every sample on its correct side: yᵢ(wᵀxᵢ+w₀) ≥ 1. Only support vectors define the boundary. Intuition: wide margin ⇒ lower generalization error; narrow-margin fits overfit.

### B13. Kernel trick in SVM `[Ch3]`
Some data (XOR) is not linearly separable in its original space. **Idea:** map x → φ(x) into a higher-dimensional space where a linear separator exists; train a linear SVM there. **Problem:** building φ explicitly is expensive. **Trick:** SVM math only needs **dot products**, so use a kernel **k(x,z) = φ(x)ᵀφ(z)** computed directly in the original space — the high-dimensional mapping is never materialized. Example: (x·z)² = dot product of a quadratic 3-D mapping. **RBF kernel:** k(x,z) = exp(−γ‖x−z‖²) — a similarity measure (1 = identical, →0 = far); γ is a hyperparameter.

### B14. Decision trees: idea + structure `[Ch3]`
A tree of yes/no questions: **root node** (all data) → **internal nodes** test one feature against a threshold ("petal width ≤ 0.75?") → branches → **leaf nodes** assign classes. Grown greedily: at each node choose the split **maximizing information gain** IG = I(parent) − Σ(Nⱼ/Nₚ)I(childⱼ); recurse until pure; **prune / cap max_depth** because deep, fully-pure trees overfit. Highly interpretable.

### B15. Random forest / ensembles `[Ch3]`
(1) Draw a **bootstrap sample** (n rows, with replacement). (2) Grow a tree; at each node consider only **d random features** (d ≈ √m) and split on the best. (3) Repeat k times. (4) Predict by **majority vote**. Averaging many high-variance trees → robust, better generalization, rarely needs pruning; gives feature importance for free. Cost: compute + lost interpretability.

### B16. Overfitting vs underfitting (+ remedies) `[Ch3/Ch4]`
**Underfitting (high bias):** model too simple — poor even on training data (straight line through curved pattern). **Overfitting (high variance):** model too complex — great on training, poor on unseen data (wiggly boundary hugging noise). Both = low performance on unseen data.
**Remedies for overfitting:** collect more data · **regularization** · simpler model/fewer parameters · dimensionality reduction/feature selection.
```
underfit: ── straight thru mixed    good: ⌒ smooth curve    overfit: ʍ hugs every point
```

### B17. Regularization parameter C `[Ch3]`
scikit-learn exposes **C = 1/λ**. **Small C** = strong regularization → weights crushed → wider margin / simpler model → underfit risk. **Large C** = weak regularization → fits training data hard → overfit risk. Same role in logistic regression and soft-margin SVM (penalty C·Σξᵢ).

---

# PART C — long / numerical (Ch1–4 scope)

### C1. Gini split: Weather vs Temperature `[24F, but pure Ch3 — likely numerical]`
Parent: 4 Yes / 4 No → I = 1−(0.5²+0.5²) = **0.5**
**Weather:** Sunny{No,No,No} I=0 · Overcast{Yes,Yes} I=0 · Rain{Yes,Yes,No} I = 1−[(2/3)²+(1/3)²] = 4/9
Weighted = (3/8)(0)+(2/8)(0)+(3/8)(4/9) = 1/6 ≈ 0.167 → **IG = 0.333**
**Temperature:** Hot{No,No,Yes} 4/9 · Mild{Yes,No} 0.5 · Cool{Yes,Yes,No} 4/9
Weighted = (3/8)(4/9)+(2/8)(0.5)+(3/8)(4/9) = 0.458 → **IG = 0.042**
**Split on Weather.** (Recipe + marble-bag intuition: `gini_by_hand.md`)

### C2. Gini: which split favoured, A or B `[22F, Ch3 slide 41 — likely numerical]`
Parent (40,40): I = 0.5.
**A → (30,10),(10,30):** each 1−(0.75²+0.25²) = 0.375 → weighted 0.375 → **IG = 0.125**
**B → (20,40),(20,0):** left 1−[(1/3)²+(2/3)²] = 4/9 × weight 6/8 = 1/3; right pure 0 → **IG = 0.167**
**B favoured** — one child fully pure. Classification error scores both 0.25 (can't tell them apart) → why it's bad for growing trees; Gini/entropy are sensitive to child purity.

### C3. Perceptron trained by hand `[Ch2 — see perceptron_by_hand.md]`
Full 4-person, 4-epoch worked example with update table, final boundary x₂ = 1 + x₁/3, and the takeaways (updates only on mistakes; η scales; x scales blame; stops at *first* separating line → motivates Adaline/SVM).

### C4. Logistic regression: cost function + single-instance plot `[Ch3]`
φ(z) = 1/(1+e⁻ᶻ) squashes z into (0,1) = P(y=1|x). From maximum likelihood (product of per-sample probabilities → take log → negate to minimize):
**J(w) = Σ [ −y log φ(z) − (1−y) log(1−φ(z)) ]**
Single instance: y=1 → cost = −log φ(z): ~0 when φ(z)→1, →∞ when φ(z)→0; y=0 is the mirror (−log(1−φ(z))).
```
cost │\                       /│
     │ \  y=1        y=0    /  │
     │  \___            ___/   │
     └──────────────────────── φ(z)
     0                        1
```
Confidently-wrong predictions cost →∞ → strong gradient signal. Log form: product→sum (easy derivative, no underflow).

### C5. Explain the accuracy-vs-C validation curve `[19T2 plot — Ch3 concept]`
x-axis: C = 1/λ. **Left (small C):** strong regularization → both training & validation accuracy low = **underfitting**. Both rise as C grows. **Right (large C):** training accuracy keeps climbing but validation accuracy peaks then **drops**, gap widens = **overfitting**. Best C = validation peak (~10⁻¹–10⁰ in the shown plot).

### C6. Learning curves: accuracy vs number of training samples `[19-era figure Q]`
Two curves: training accuracy starts near 1.0 and falls slightly; validation accuracy starts low and rises. **Large persistent gap = overfitting/high variance** → more data, regularization, simpler model. **Both plateauing low & close = underfitting** → more complex model / better features. **Ideal:** both converge high with a tiny gap, approaching the desired-accuracy line.
```
acc │ train ─────────────        ideal: both ⟶ ───≈───
    │        ˰˰˰˰ val (gap!)
    └───────────────── #samples
```

---

## Do-by-hand-tonight checklist (TT1 scope)
- [ ] B2 perceptron mapping + one weight update by hand (perceptron_by_hand.md)
- [ ] B5 scaling table for 0…5 (μ=2.5, σ≈1.708)
- [ ] C1 + C2 Gini by hand (gini_by_hand.md recipe)
- [ ] Sketch once each: RL loop · pipeline diagram · η too big/small · separable vs not · L1 diamond vs L2 circle · underfit/good/overfit boundaries · sigmoid + logistic cost curves
- [ ] Say aloud: Adaline cost = SSE, convex+differentiable · batch-GD disadvantage · slack variable role · (20,20) most impure
