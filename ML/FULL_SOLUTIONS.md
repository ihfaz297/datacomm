# CSE 475 — COMPLETE SOLUTIONS to every past-paper question
**Papers analyzed:** 19-T1 · 19-T2 · 20-T1 · 2022 Final · 2024 Final. Tags show where each Q appeared. Nothing from any paper is skipped.

---

# PART A — 2-mark short answers (the "Answer any FIVE" pool)

### A1. What is reinforcement learning? When do you apply it? Diagram. `[19T1, 20T1, 24F]`
RL develops an **agent** that improves by **interacting with an environment**: it takes an action, receives the new **state** and a **reward**, and learns (trial-and-error) a policy of actions that maximizes cumulative reward. Apply when there are **no labeled examples but sequential decisions with delayed feedback** — games (chess), robotics, self-driving.
```
        ┌────────── action ──────────┐
   [ AGENT ]                    [ ENVIRONMENT ]
        └──── state, reward ◄────────┘
```

### A2. Traditional programming vs machine learning `[24F]`
Traditional: human writes **rules**; rules + data → answers. ML: data + answers (labels) → algorithm **learns the rules** (model), which then produces answers for new data.

### A3. What does "k" represent in k-NN? `[24F]`
The number of nearest neighbors consulted; the query point gets the **majority class among its k closest** training points (by a distance metric like Euclidean).

### A4. Which cost function for linear regression? Why? `[24F]`
**Mean Squared Error** J(w)=½Σ(y−ŷ)². It's **convex and differentiable** (gradient descent finds the global minimum), penalizes large errors strongly, and suits continuous targets.

### A5. Curse of dimensionality `[22F, 24F]`
As the number of features grows with a fixed dataset, the feature space becomes **exponentially sparse** — even nearest neighbors are far away, so distance-based estimates (especially KNN) become unreliable and overfit. Remedy: dimensionality reduction / feature selection.

### A6. Limitation of an MLP `[24F]`
Needs large data + compute; black box (poor interpretability); prone to overfitting; deep stacks suffer **vanishing gradients**; ignores spatial structure of images (CNNs fix that).

### A7. Main limitation of ensemble learning `[24F]`
**Computational cost and lost interpretability** — you train/store many models and can no longer read a single tree's logic.

### A8. Vanishing gradient problem `[24F, 22F]`
In deep nets, backprop **multiplies many small derivatives** (sigmoid′ ≤ 0.25) layer by layer, so the gradient shrinks exponentially toward the early layers — they barely learn. RNNs suffer worst: the same weight multiplies through many time steps.

### A9. Transfer learning `[24F]`
Reusing a model pretrained on a large dataset (e.g. ImageNet) as the starting point for a related task, fine-tuning it on your smaller dataset → less data and training time.

### A10. Why is accuracy not enough for imbalanced datasets? `[24F, 22F]`
With 99:1 classes, predicting the majority always gives 99% accuracy but **never detects the minority class** (recall 0). Use precision, recall, **F1**, ROC-AUC.

### A11. Why must an ANN activation be differentiable? `[19T2-era, 22F, 24F]`
Training uses **gradient descent via backpropagation**, which needs ∂(activation)/∂z at every layer to propagate error gradients backward. No derivative → no gradient → no weight update.

### A12. Which metric for a model with continuous output? `[22F, 24F]`
Regression metrics: **MSE / RMSE / MAE / R²**.

### A13. What are outliers? `[22F, 24F]`
Examples that deviate strongly from the rest of the data (measurement error or rare events). They distort means, squared-error fits, and scaling; handle with robust methods (RANSAC, RobustScaler) or removal.

### A14. What is a hyperparameter? Examples. `[22F, 24F]`
A setting fixed **before** training, not learned from data: learning rate η, k in KNN, C, kernel γ, tree max_depth, epochs, batch size. (Learned weights = parameters.) Tuned via cross-validation.

### A15. What is missing data / how to handle? `[22F]`
Absent entries (NaN/NULL) most algorithms can't process. Either **remove** rows/columns (`dropna` — simple, loses data) or **impute** (fill with mean/median/most-frequent, `SimpleImputer` — keeps all samples).

### A16. Two important steps to preprocess text (NLP) `[22F]`
**Tokenization** and **stop-word removal** (also acceptable: lowercasing, stemming/lemmatization, punctuation stripping).

### A17. What is an ordinal feature? `[22F]`
A categorical feature with an inherent **order** (M < L < XL) → encode as ordered integers. (Nominal = no order → one-hot.)

### A18. Is logistic regression's output continuous or categorical? `[22F]`
The sigmoid produces a **continuous probability** in (0,1), but the final classification output after the 0.5 threshold is **categorical**. (Say both — that's the full mark.)

### A19. Why is CNN more suitable for image classification? `[22F]`
Convolution filters **share weights** and exploit **local spatial structure** → far fewer parameters than dense layers, translation-robust detection of edges→textures→objects.

### A20. How does batch GD differ from SGD? `[22F]`
Batch: gradient over the **whole training set**, one smooth update per epoch — stable, slow at scale. SGD: update per **single example** — noisy, fast, enables online learning. (Mini-batch = the practical middle.)

### A21. Why is kernel trick used in SVM? `[22F]`
To classify **linearly inseparable** data: it implicitly maps features to a higher-dimensional space where a linear separator exists, computing only kernel values k(x,z)=φ(x)ᵀφ(z) — never the expensive mapping itself.

### A22. What is bootstrapping in sample selection? `[22F]`
Drawing a random sample of size n **with replacement** from the training set — the same example can appear multiple times. Basis of bagging/random forests.

### A23. What is Adaline's cost function? `[19T1, 20T1]`
**Sum of Squared Errors:** J(w) = ½Σᵢ(y⁽ⁱ⁾ − φ(z⁽ⁱ⁾))², with φ(z)=z the linear activation. Convex + differentiable → gradient descent reaches the global minimum. (0/1 error counting has zero gradient — no learning signal.)

### A24. Most impure node among (20,20), (40,0), (30,10)? `[20T1]`
**(20,20)** — a perfect 50/50 mix: Gini = 1−(0.5²+0.5²) = 0.5, entropy = 1 (maximum). (40,0) is pure (0); (30,10): Gini = 1−(0.75²+0.25²) = 0.375.

### A25. Role of the slack variable in SVM `[20T1]`
Slack ξᵢ ≥ 0 lets sample i violate the margin (soft margin) so optimization **converges on non-separable data**; violations are penalized by C·Σξᵢ, trading margin width vs errors.

### A26. Advantages & disadvantages of a non-parametric model like KNN `[20T1]`
**Pros:** no training phase, adapts instantly to new data, no assumed functional form, naturally multiclass. **Cons:** prediction is slow (search whole training set), memory-heavy, sensitive to feature scale and irrelevant features, suffers curse of dimensionality.

### A27. What does the confusion matrix represent? `[24F]`
A table of predictions vs ground truth for a classifier: **TP, FN (actual +), FP, TN (actual −)** — from which accuracy, precision, recall, F1 are computed.

### A28. Why is KNN a lazy learner? `[22F, 24F]` + tie in voting? `[24F]`
It performs **no training/abstraction** — it memorizes the training set and defers all computation to prediction time (vs eager learners that fit and discard data). **Tie:** use odd k; or decrease k; or weight votes by inverse distance; or take the nearest neighbor's class.

### A29. What is feature importance? How determined? `[24F]`
A score of how much each feature contributes to predictions. Determined e.g. by **random forests**: average **impurity decrease** contributed by the feature across all trees (or by permutation: shuffle the feature, measure accuracy drop).

### A30. What is meant by hyperparameter vs model selection / how select best model? `[19T1, 20T1]`
Train several candidate algorithms, tune hyperparameters with **k-fold cross-validation on the training data**, pick the configuration with the best validation score, finally confirm on the untouched test set.

### A31. How do you know the model performs well on unseen data? `[19T1, 20T1]`
Evaluate on a **held-out test set** never used for training or tuning — its score is an unbiased estimate of generalization (optionally with CV for robustness).

---

# PART B — 5-mark structured answers (the "Answer any FOUR" pool)

### B1. Steps to build a supervised ML system `[19T1, 20T1]`
```
Raw data + labels → PREPROCESSING → Training set / Test set
Training set → LEARNING ALGORITHM (+ CV for model selection) → FINAL MODEL
Test set → EVALUATION (unseen data) → deploy → PREDICTION on new data
```
1) **Preprocessing** — clean missing values, encode categoricals, scale features, train/test split. 2) **Training** — fit candidate models. 3) **Model selection** — cross-validate, tune hyperparameters. 4) **Evaluation** — measure on held-out test set. 5) **Prediction** — deploy on new data.

### B2. Perceptron ↔ biological neuron (+ compute) `[19T1, 20T1, 24F]`
| Biology | Perceptron |
|---|---|
| Dendrites receive signals | inputs x₁…xₘ |
| Synapse strength | weights w₁…wₘ |
| Cell body integrates | net input z = wᵀx |
| Fires past threshold | step function z≥0 → +1 |
| Axon output | prediction ŷ |
**Compute (24F):** x=[1,−2], w=[0.5,0.25], bias=1 → z = 1 + 0.5(1) + 0.25(−2) = **1.0** ≥ 0 → **ŷ = +1**.

### B3. Learning rate: role, too small / too large, figure `[19T1, 20T1, 22F]`
η scales each gradient step w := w − η∇J. **Too large:** overshoots the minimum, cost oscillates or diverges. **Too small:** stable but needs impractically many epochs.
```
J(w)   too large: bounces across      too small: crawls
  \      /\    /\                        \_
   \    /  \  /  \                         \_
    \__/    \/    \___ w                     \_→ min (slowly)
```

### B4. Linearly separable vs not (figure) `[19T1, 20T1]`
Linearly separable: one hyperplane splits classes → perceptron converges. Not: no line works (XOR) → perceptron updates forever (cap epochs, or use logistic/kernel methods).
```
Separable:  - - |  + +        Not separable:  + -
            - - |  + +                        - +   (XOR)
```

### B5. Feature scaling: importance + standardization example `[19T1, 20T1, 22F, 24F]`
Features on different scales let the large-range feature dominate gradient-based costs and distance metrics (KNN, SVM) → slow, skewed learning. Scaling makes the cost surface symmetric → faster, direct convergence. **Trees/forests are scale-invariant.**
- **Standardization:** x′=(x−μ)/σ → mean 0, unit variance (preferred for GD/logistic/SVM; keeps outlier info).
- **Normalization:** x′=(x−min)/(max−min) → [0,1].
**Worked table (20T1):** inputs 0…5: μ=2.5, σ≈1.708 → standardized −1.46, −0.88, −0.29, 0.29, 0.88, 1.46; normalized 0, 0.2, 0.4, 0.6, 0.8, 1.0. Fit scaler on training data only; reuse μ,σ on test.

### B6. Batch GD disadvantage `[19T1, 20T1]` (2-mark version exists too)
Every weight update evaluates the gradient over the **entire** training set — with millions of rows each epoch is one expensive update; cannot stream/online-learn. → SGD (per-example) or mini-batch (per 32–128, vectorizable) scale better.

### B7. One-hot encoding: how + disadvantage `[19T2, 22F, 24F]`
Nominal features can't be integer-coded (would fake an order blue>green>red). Create one **binary column per category**: red→[0,0,1] etc. **Disadvantages:** dimensionality blowup for many categories, and **multicollinearity** — dummy columns sum to 1 (linearly dependent), problematic for matrix-inversion methods. **Fix:** drop one column (`drop_first=True`) — no information lost (0,0 implies the dropped one).

### B8. How does L1 regularization perform feature selection? `[19T2, 24F]`
Regularization adds a weight penalty to the cost. L2 adds λΣw² (circular budget), L1 adds λΣ|w| (**diamond** budget). The optimum is where the cost contours first touch the budget region; the diamond's **corners lie on axes**, so the touch point typically has several weights **exactly 0** → sparse weight vector → irrelevant features automatically eliminated. Increasing λ (decreasing C=1/λ) zeroes more weights.
```
L2: contours meet circle → small but nonzero w
L1: contours meet diamond corner → w on axis (some wⱼ = 0)
```

### B9. Explain how L2 regularization fights overfitting `[22F]`
Adds (λ/2)‖w‖² to the cost → large weights are penalized, so the model prefers **small, smooth weights** → simpler decision boundary that ignores noise. Gradient adds −ηλw: each step **decays weights** toward zero ("weight decay"), equivalent to a Gaussian prior on w.

### B10. Purpose of cross-validation + process + diagram `[19T2 nested, 22F, 24F]`
**Purpose:** reliable estimate of generalization + hyperparameter tuning **without touching the test set**. **k-fold:** split training data into k equal folds; train on k−1, validate on the held-out fold; rotate k times; average the k scores.
```
Fold: [VAL][tr][tr][tr][tr]
      [tr][VAL][tr][tr][tr]   → mean of 5 validation scores
      ... (k rows)
```
**Nested CV (19T2):** tuning and reporting with the *same* CV is optimistically biased → **outer loop** estimates performance; **inner loop** (inside each outer training split) runs the hyperparameter search. Diagram: each outer training block subdivided into inner folds.

### B11. ROC curve for model evaluation `[22F]`
Plot **TPR (recall) vs FPR** for every classification threshold. A curve hugging the top-left = good; the diagonal = random. **AUC** summarizes threshold-independent performance (1.0 perfect, 0.5 random) — good for comparing classifiers and for imbalanced data.

### B12. Sigmoid vs ReLU + why ReLU preferred `[24F]`
Sigmoid: φ(z)=1/(1+e⁻ᶻ) → (0,1), S-curve — saturates at both ends (derivative→0). ReLU: φ(z)=max(0,z). **ReLU preferred:** no saturation for z>0 → gradients don't vanish in deep nets; extremely cheap; sparse activations; faster convergence. (Sigmoid still fine as an output layer for probability.)

### B13. Epoch & batch + iterations `[24F]`
**Epoch** = one full pass over the training data. **Batch** = subset processed per weight update. Iterations per epoch = ⌈N/batch⌉ = 60000/128 = 468.75 → **469** (468 full batches + 1 partial of 96).

### B14. Slope, derivative, gradient `[24F]`
- **Slope** = rise/run of a straight line (constant). `y=mx+c`
- **Derivative** = slope of the tangent of a function at a point: f′(x) = lim Δ→0 [f(x+Δ)−f(x)]/Δ (varies with x).
- **Gradient** = the **vector** of all partial derivatives ∇J = [∂J/∂w₀ … ∂J/∂wₘ] of a multivariable function; points in the direction of steepest ascent (descent goes opposite).
Figures: line with rise/run triangle; curve with tangent at a point; 2D contour plot with arrows pointing uphill.

### B15. k-means limitations + k-means++ `[24F]`
Limitations: must choose **k** beforehand; result depends on **random initial centroids** (bad local optima); assumes spherical, similar-size clusters; sensitive to outliers. **k-means++**: pick the first centroid at random; pick each next centroid with probability ∝ **squared distance** from the nearest chosen centroid → well-spread seeds → better and faster convergence.

### B16. Why dimensionality reduction + one technique `[19T1-era, 20T1]`
High dimensions → sparsity (curse), overfitting, cost. Reduce with **feature selection** (L1, Sequential Backward Selection: greedily remove the feature whose removal hurts performance least until k remain; or RF importance) or **feature extraction (PCA)** — project onto the directions of maximum variance.

### B17. Outliers + RANSAC `[22F, 24F]`
Outliers skew mean/σ and squared-error fits (one far point drags the line). **RANSAC:** repeat — (1) fit model on a **random minimal subset**; (2) count **inliers** within a tolerance ε; (3) keep the model with most inliers; finally (4) refit using all inliers only → robust fit that ignores outliers.

### B18. TF-IDF: define + how it assesses relevancy `[24F]`
**tf-idf(t,d) = tf(t,d) × idf(t)**, idf(t) = log[ n_docs / (1 + df(t)) ]. tf: how often term t occurs in document d; df: how many documents contain t. A word scores high when **frequent in this document but rare across the corpus** → common words ("the") get ~0, discriminative topic words get high weight — that's word relevancy in encoding.

### B19. Purpose of learning rate (what if too small/large — same as B3) `[20T1, 22F]` — see B3.

### B20. SVM is a maximum-margin classifier — explain `[22F]`
It chooses the hyperplane wᵀx + w₀ = 0 that **maximizes the margin** — the distance to the closest points (**support vectors**). Positive/negative hyperplanes: wᵀx+w₀ = ±1; margin = **2/‖w‖**; so SVM minimizes ½‖w‖² subject to yᵢ(wᵀxᵢ+w₀) ≥ 1. Only support vectors define the boundary. Wide margin → lower generalization error; small-margin models overfit.

### B21. Kernel trick (5-mark version) `[22F, 24F]`
Data like XOR isn't linearly separable in original space. Map x → φ(x) into higher dimensions where it **is** separable, train a linear SVM there. Explicitly building φ is expensive — but SVM math only needs **dot products**, so define a kernel **k(x,z) = φ(x)ᵀφ(z)** computed directly in original space. Example: (x·z)² equals the dot product of a 3-D quadratic mapping. **RBF:** k(x,z)=exp(−γ‖x−z‖²) — a similarity score (1 identical → 0 far), γ a hyperparameter.
```
2D: + - / - +  (no line)  → φ →  3D: separable by a plane
```

### B22. Decision trees: structure `[22F]`
Root node (full dataset) → **internal nodes** ask threshold questions on one feature ("petal width ≤ 0.75?") → **branches** = answers → **leaf nodes** = class decisions. Grow by choosing splits that **maximize information gain**; deep pure trees overfit → prune / cap max_depth. Attractive because fully interpretable.

### B23. Ensemble methods: goal, main challenge, AdaBoost `[22F, 24F]`
**Goal:** combine many weak learners into one strong, lower-variance model (wisdom of the crowd). **Challenge:** computational cost + lost interpretability. **AdaBoost:** train weak learners (stumps) **sequentially**; after each round **increase the weights of misclassified examples** so the next learner focuses on the hard cases; final output = **weighted vote** of all learners. (Bagging = parallel on bootstrap samples; boosting = sequential on reweighted data.)

### B24. Random forest (how it works) `[22F-adjacent, exam-likely]`
(1) Bootstrap sample n rows with replacement; (2) grow a tree, at each node choosing the best of **d random features** (d≈√m); (3) repeat k times; (4) **majority vote**. Averaging many high-variance trees → robust, rarely needs pruning; gives feature importance free.

### B25. Normal equation for linear regression: pros/cons `[22F]`
Closed form **w = (XᵀX)⁻¹Xᵀy** — solves least squares in one step. **Pros:** no learning rate, no iterations/convergence worries. **Cons:** computing (XᵀX)⁻¹ is O(m³) in features — slow/memory-heavy for many features; fails when XᵀX is singular (collinear features). Gradient descent preferred at scale.

### B26. Normalization vs standardization — which more practical? `[22F]`
Formulas in B5. **Standardization** is usually more practical: unbounded range OK, far less sensitive to outliers (min-max squeezes everything if one outlier exists), preferred by GD/logistic/SVM. Min-max when a bounded [0,1] range is required (pixel intensities). *(Fill-the-table numbers: B5.)*

### B27. Represent a class in ML / induction vs deduction `[22F]`
A class is represented by the **learned model/hypothesis h: X → y** (e.g. weights of a decision boundary) mapping feature vectors to labels. **Induction** = training: generalize from specific labeled examples to a general rule. **Deduction** = inference: apply the general rule to a specific new case to predict its label.

### B28. Parametric vs non-parametric + examples `[24F]`
**Parametric:** fixed number of parameters learned, data then discarded — perceptron, logistic regression, linear SVM, linear regression. Fast, strong assumptions. **Non-parametric:** model complexity grows with data; keeps training data — **KNN**, decision trees, kernel SVM, random forest. Flexible, costlier, overfit-prone in high dims.

### B29. Steps for training a neural network + Keras code + softmax swap `[24F]`
Steps: define architecture → initialize weights → **forward pass** → compute **loss** → **backpropagate** gradients → **update weights** (optimizer, e.g. SGD/Adam) → repeat over epochs while monitoring validation.
`Sequential([Dense(16,relu), Dense(16,relu), Dense(1,sigmoid)])` = feed-forward net: two hidden layers of 16 ReLU neurons, one **sigmoid output neuron** giving P(y=1) — binary classifier. **Sigmoid→softmax in a 1-unit output:** softmax normalizes across units; with a single unit it always outputs 1 → useless. Softmax is for **multiclass** with one unit per class (probabilities summing to 1).

### B30. Perceptron figure labeling + RNN principle `[22F]`
Labels: x₁…xₘ inputs, w₀…wₘ weights (w₀ bias, x₀=1), Σ = net input z=wᵀx, activation function φ, threshold/quantizer, output ŷ; error (y−ŷ) feeds back to update weights.
**RNN:** the hidden state feeds back as input to the next time step → memory over sequences. Suffers **vanishing gradient** because backprop-through-time multiplies the same small derivatives across many steps → can't learn long dependencies (→ LSTM/GRU).

### B31. Email spam filter design (3–4 sentences) `[22F]`
Collect a corpus of emails labeled spam/ham. Preprocess text (tokenize, lowercase, remove stop words) and vectorize with **Bag-of-Words / TF-IDF**. Train a classifier (Naive Bayes or logistic regression) on the vectors and evaluate with precision/recall on a held-out set. Deploy: vectorize each incoming email and flag it if P(spam) exceeds a threshold.

### B32. Why limit vocabulary in Bag-of-Words `[22F]`
Vector length = vocabulary size: unlimited vocab → gigantic sparse matrices (memory/compute blowup) and rare words/typos add noise with no signal → keep top-N frequent words (or hash), improving generalization and speed.

### B33. Explain the sentiment-classification pipeline diagram `[24F]`
Context: classifying student sentiments (pos/neg) about a government decision. **Preprocessing:** collect posts + labels; clean/tokenize/vectorize (BoW/TF-IDF); split into training and test sets. **Learning:** feed training vectors + labels to the algorithm (e.g. logistic regression) → fitted model; tune with CV. **Evaluation:** run the untouched test set through the final model; report accuracy/F1. **Prediction:** new unseen posts → same preprocessing → model outputs sentiment labels.

---

# PART C — 10-mark numericals & long questions (FULL WORKING)

### C1. Confusion matrix — malignant/spam table `[19T2, 22F]`
Positive = Malignant (Spam). Classify each row: (1) M→NM **FN** · (2) M→M **TP** · (3) NM→NM **TN** · (4) M→M **TP** · (5) NM→M **FP** · (6) NM→NM **TN** · (7) NM→NM **TN** · (8) M→M **TP** · (9) M→NM **FN** · (10) NM→NM **TN**

| | Pred + | Pred − |
|---|---|---|
| **Actual +** | TP = 3 | FN = 2 |
| **Actual −** | FP = 1 | TN = 4 |

Accuracy = (3+4)/10 = **0.70** · Precision = 3/(3+1) = **0.75** · Recall = 3/(3+2) = **0.60** · F1 = 2(0.75)(0.60)/(1.35) = **0.667**

### C2. Confusion matrix — 100 pos / 50 neg `[24F]`
90 of 100 positives correct → TP=90, FN=10. 30 of 50 negatives correct → TN=30, FP=20.
Accuracy = 120/150 = **0.80** · Precision = 90/110 ≈ **0.818** · Recall = 90/100 = **0.90** · F1 = 2(.818)(.9)/1.718 ≈ **0.857**
**Why F1 for imbalance:** it's the harmonic mean of precision and recall — a classifier that ignores the minority class gets recall≈0 → F1≈0, even when accuracy looks high.

### C3. Gini first split: Weather vs Temperature `[24F]`
Parent: 4 Yes / 4 No → I = 1−(0.5²+0.5²) = **0.5**
**Weather:** Sunny {No,No,No} I=0 · Overcast {Yes,Yes} I=0 · Rain {Yes,Yes,No} I = 1−[(2/3)²+(1/3)²] = 4/9
Weighted = (3/8)0 + (2/8)0 + (3/8)(4/9) = 1/6 ≈ 0.167 → **IG = 0.5 − 0.167 = 0.333**
**Temperature:** Hot {No,No,Yes} 4/9 · Mild {Yes,No} 0.5 · Cool {Yes,Yes,No} 4/9
Weighted = (3/8)(4/9) + (2/8)(0.5) + (3/8)(4/9) = 0.458 → IG = **0.042**
**Choose Weather** (0.333 ≫ 0.042).

### C4. Gini: which split favoured, A or B `[22F]`
Parent (40,40): I = 0.5.
**A → (30,10) & (10,30):** each I = 1−(0.75²+0.25²) = 0.375 → weighted 0.375 → **IG_A = 0.125**
**B → (20,40) & (20,0):** left I = 1−[(1/3)²+(2/3)²] = 4/9, weight 60/80 → 1/3; right pure I=0 → **IG_B = 0.5−0.333 = 0.167**
**B favoured** — its right child is already pure. (Classification error scores both IG = 0.25 → can't distinguish; why it's bad for growing trees.)

### C5. k-means one iteration, Manhattan distance `[22F]`
Points A1(2,10) A2(2,5) A3(8,4) A4(5,8) A5(7,5) A6(6,4) A7(1,2) A8(4,9); centers c1=A1, c2=A4, c3=A7. P(a,b)=|x2−x1|+|y2−y1|.

| Pt | d→c1(2,10) | d→c2(5,8) | d→c3(1,2) | → cluster |
|---|---|---|---|---|
| A1 | 0 | 5 | 9 | 1 |
| A2 | 5 | 6 | **4** | 3 |
| A3 | 12 | **7** | 9 | 2 |
| A4 | 5 | 0 | 10 | 2 |
| A5 | 10 | **5** | 9 | 2 |
| A6 | 10 | **5** | 7 | 2 |
| A7 | 9 | 10 | 0 | 3 |
| A8 | 3 | **2** | 10 | 2 |

**Clusters:** C1={A1} · C2={A3,A4,A5,A6,A8} · C3={A2,A7}
**New centers:** c1=(2,10) · c2=((8+5+7+6+4)/5,(4+8+5+4+9)/5)=**(6,6)** · c3=((2+1)/2,(5+2)/2)=**(1.5,3.5)**

### C6. Naive Bayes: Play/Study/Sleep `[24F]`
**Priors:** P(Play)=5/10, P(Study)=3/10, P(Sleep)=2/10.
**Query: Near, Bad, Off.** Count within each class:
Play(5): Near 2/5, Bad 0/5, Off 5/5 · Study(3): Near 1/3, Bad 3/3, Off 1/3 · Sleep(2): Near 1/2, Bad 2/2, Off 1/2
- Play: 0.5 × 2/5 × 0 × 1 = **0**
- Study: 0.3 × 1/3 × 1 × 1/3 = **1/30 ≈ 0.033**
- Sleep: 0.2 × 1/2 × 1 × 1/2 = **1/20 = 0.05** ← max → **Sleep**
(Note the zero-probability problem for Play → Laplace add-1 smoothing in practice.)

### C7. Bag-of-Words 1-gram vectors `[22F]`
Vocabulary (alphabetical): **and, is, one, rising, sun, sweet, the, two, weather**
- "The sun is rising" → [0,1,0,1,1,0,1,0,0]
- "The weather is sweet" → [0,1,0,0,0,1,1,0,1]
- "The sun is rising, the weather is sweet, and one and one is two" → [2,3,2,1,1,1,2,1,1]

### C8. Logistic regression cost + single-instance plot `[19T2]`
Model: φ(z)=1/(1+e⁻ᶻ), z=wᵀx. From maximum likelihood (product of Bernoullis → log → negate):
**J(w) = Σᵢ [ −y⁽ⁱ⁾ log φ(z⁽ⁱ⁾) − (1−y⁽ⁱ⁾) log(1−φ(z⁽ⁱ⁾)) ]**
Single instance: if y=1, cost = −log φ(z) → 0 as φ(z)→1, → ∞ as φ(z)→0. If y=0, cost = −log(1−φ(z)) — the mirror.
```
cost│\  y=1: −log φ(z)          y=0 is the mirror image
    │ \___
    │     \____
    └───────────── φ(z)
    0            1
```
Correct confident predictions cost ~0; confident wrong predictions cost →∞ (strong gradient signal).

### C9. Explain the accuracy-vs-C validation curve `[19T2]`
x-axis: C = 1/λ (inverse regularization). **Left (small C):** strong regularization → weights crushed → both training and validation accuracy low = **underfitting**. Moving right both rise. **Right (large C):** weak regularization → training accuracy keeps climbing toward 1.0 while validation accuracy peaks (~C=10⁻¹–10⁰) then **drops** — the gap widens = **overfitting**. Best C = where validation accuracy peaks.

### C10. Learning curves (accuracy vs #training samples) `[22F]`
Shown: training accuracy high and slowly falling; validation accuracy low and rising; **persistent gap** between them = **high variance / overfitting** → remedies: more data, regularization, simpler model, fewer features. (If both plateau low & close = underfitting → more complex model/features.) **Ideal:** both curves converge close together near the desired accuracy:
```
acc │ train ────────────
    │          ⌒⌒⌒⌒⌒⌒⌒⌒  ← val, gap ≈ 0, both high
    └──────────────── #samples
```

### C11. Underfitting / overfitting / good fit — 3 boundary figures + reducing overfit `[24F]`
Straight line through mixed classes = **underfit** (high bias). Moderately curved boundary, few errors = **good fit**. Extremely wiggly boundary hugging every point = **overfit** (high variance).
**Reduce overfitting:** more training data · regularization (L1/L2) · simpler model / prune / dropout (NN) · fewer features/dimensionality reduction · early stopping · ensembling/bagging.

### C12. Decision trees: what + structure (10-mark version) `[22F]` — B22 + IG formula: IG(Dₚ,f) = I(Dₚ) − Σⱼ (Nⱼ/Nₚ) I(Dⱼ); impurity by Gini 1−Σp² or entropy −Σp log₂p; grow greedily, prune to generalize; example tree splitting on petal width then petal length.

### C13. Boosting approach of an ensemble `[24F]` — see B23 AdaBoost.

### C14. k-NN vs other supervised algorithms (10-mark) `[22F]` — combine A28 + A26 + steps: choose k & metric → find k nearest → majority vote; distance: Euclidean (p=2) / Manhattan (p=1); needs scaling; curse of dimensionality.

---

## Guaranteed-mark checklist (tick each off tonight)
- [ ] C1/C2 confusion matrices by hand
- [ ] C3/C4 Gini by hand
- [ ] C6 Naive Bayes by hand
- [ ] C5 k-means by hand
- [ ] B2 perceptron compute + B13 469 iterations
- [ ] B5 scaling table
- [ ] Sketch once: RL loop · roadmap · separable/not · η big/small · L1 diamond vs L2 circle · k-fold grid · learning curves · 3 boundary figures · sigmoid+logistic cost curves
