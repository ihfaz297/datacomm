# CSE 475 — Exam Crash Course (built from your slides + 5 past papers)

Every question from `Questions/` is answered below, organized by topic. Numericals are fully worked at the end — **do those by hand once tonight.**

---

## 0. The map (Ch1)

- **ML** = algorithms that improve at task T, measured by P, with experience E (Tom Mitchell). vs **traditional programming**: you write rules → program computes answers. ML: you give data + answers → it learns the rules.
- **Three types:**
  - **Supervised** — labeled data → predict. *Classification* (discrete label: spam/not) or *Regression* (continuous value: price).
  - **Unsupervised** — no labels → find structure. *Clustering* (k-means), *dimensionality reduction*.
  - **Reinforcement (RL)** — no dataset at all; an **agent** interacts with an **environment**, gets **state + reward**, learns a policy of actions maximizing cumulative reward by trial-and-error. Apply when there's sequential decision-making and no labeled examples (games, robotics, chess).
  - RL diagram: `Agent --action--> Environment --state, reward--> Agent` (a loop).
- **Steps to build a supervised ML system** (the roadmap slide — memorize, it's asked 3×):
  1. **Preprocessing** — clean, scale features, split train/test
  2. **Training** — learning algorithm fits model on training set
  3. **Model selection** — compare several algorithms + hyperparameters via cross-validation
  4. **Evaluation** — measure on *held-out test set* (unseen data)
  5. **Prediction** — deploy final model on new data
- **How to select the best model?** Train several candidates, tune hyperparameters via **k-fold cross-validation** on training data, pick the one with best validation score.
- **How do you know it performs well on unseen data?** Evaluate on the **test set** that was never used in training/tuning — that's an unbiased estimate of generalization.
- **Terminology:** row = training example/instance/sample; column = feature (x); target/label = y; loss ≈ cost ≈ error function.
- **Hyperparameter** = setting chosen *before* training, not learned from data (learning rate η, k in KNN, C, max_depth, number of epochs). Parameter = learned (weights).
- **Parametric vs non-parametric:** parametric learns a fixed set of parameters, then discards data (perceptron, logistic regression, linear SVM). Non-parametric: complexity grows with data, keeps the training set (KNN, decision trees, kernel SVM).
  - KNN advantages: no training, adapts instantly, simple. Disadvantages: slow prediction (stores everything), memory-heavy, sensitive to scale & curse of dimensionality.

---

## 1. Perceptron → Adaline → Gradient Descent (Ch2)

- **Biological neuron ↔ perceptron:** dendrites = inputs xᵢ, synapse strengths = weights wᵢ, cell body integrates = weighted sum z = wᵀx, fires if signal exceeds threshold = step activation, axon output = ŷ. (Asked on ~every paper.)
- Net input **z = w₀ + w₁x₁ + … + wₘxₘ**; step function: z ≥ 0 → +1, else −1.
- **Learning rule:** wⱼ := wⱼ + η(y − ŷ)xⱼ. Updates only on mistakes. Converges **only if data is linearly separable**.
- **Linearly separable** = one straight line (hyperplane) can split the classes. **Not linearly separable** = no line works (e.g. XOR). Draw: +'s and −'s split by a line vs +'s surrounded by −'s.
- **Adaline:** same as perceptron but weight update uses the **continuous linear activation φ(z) = z** (before thresholding), not the predicted label.
- **Adaline cost function: SSE** — J(w) = ½ Σ(y⁽ⁱ⁾ − φ(z⁽ⁱ⁾))². It's **convex + differentiable** → gradient descent finds the global minimum. (Why not count misclassifications? 0/1 count is flat → gradient is zero → no learning signal.)
- **Gradient descent:** w := w − η∇J(w) — step *opposite* the gradient, downhill on the cost surface.
- **Learning rate η role:**
  - too **large** → overshoots the minimum, cost oscillates/diverges
  - too **small** → converges but painfully slowly
  - Figure: U-shaped cost bowl; big-η arrows bounce across the valley, small-η arrows crawl.
- **Batch vs Stochastic vs Mini-batch GD:**
  | | Batch | SGD | Mini-batch |
  |---|---|---|---|
  | update uses | all m samples | 1 sample | small subset (e.g. 32/128) |
  | noise | none | high | moderate |
  | speed at scale | slow (disadvantage!) | fast, erratic | fast + vectorizable — the default |
  - **Disadvantage of batch GD:** every single update re-evaluates the *entire* training set → doesn't scale to large datasets.
  - Batch GD vs SGD difference in one line: batch = one smooth update per epoch; SGD = m noisy updates per epoch, enables online learning.
- **Epoch** = one full pass over training data. **Batch** = subset used per update. **Iterations/epoch = ⌈dataset/batch⌉** → 60000/128 = 468.75 → **469**.
- **Slope vs derivative vs gradient:** slope = Δy/Δx of a line; derivative = slope of a function at a point (limit); gradient = **vector** of partial derivatives for multivariable functions, points in the direction of steepest ascent.

---

## 2. Preprocessing (Ch4)

- **Missing data:** blanks/NaN/NULL. Handle by (a) **remove** rows/columns (`dropna`) — simple but loses data; (b) **impute** — fill with mean/median/most-frequent (`SimpleImputer`).
- **Ordinal feature** = categories with order (size: M < L < XL) → map to integers. **Nominal** = no order (color) → **one-hot encode**.
- **One-hot encoding:** one binary column per category (red → [1,0,0]). **Disadvantage/demerit: multicollinearity** — the dummy columns are correlated (they sum to 1), problematic for matrix inversion; also blows up dimensionality. Fix: drop one column (`drop_first=True`) — no info lost.
- **Feature scaling — why:** gradient descent and distance-based algorithms (KNN, SVM) are dominated by the largest-scale feature; scaling makes the cost surface round → faster, more direct convergence. **Exception: decision trees / random forests are scale-invariant.**
  - **Normalization (min-max):** x′ = (x − xmin)/(xmax − xmin) → [0,1].
  - **Standardization:** x′ = (x − μ)/σ → mean 0, variance 1. Preferred for GD/logistic/SVM; keeps outlier info; note it does **not** make data normally distributed.
  - Which is more practical? **Standardization** (less sensitive to outliers; bounded range not required).
  - Fit the scaler **on training data only**, reuse those μ, σ on test data.
- **Outliers** = examples far from the rest of the data (measurement error or rare events); they distort mean-based scaling and squared-error fits. **RANSAC** handles them for regression: repeatedly (1) fit model on a random subset, (2) count inliers within a tolerance, (3) keep the model with most inliers, (4) refit on all inliers — final model ignores outliers.
- **Overfitting remedies (4):** more data · regularization · simpler model · fewer dimensions (feature selection).
- **L1 vs L2 regularization:**
  - Both add a weight penalty to the cost: L2 adds λΣwⱼ² (circular budget), L1 adds λΣ|wⱼ| (diamond budget).
  - **L2** shrinks weights smoothly toward zero → fights overfitting by capping model complexity / filtering noise.
  - **L1 → feature selection:** the diamond's sharp corners sit on the axes, so the optimum lands where many weights are **exactly zero** → sparse model, irrelevant features eliminated automatically. (Asked on 3 papers — know the diamond-vs-circle picture.)
  - scikit-learn exposes **C = 1/λ**: small C = strong regularization.
- **Other feature selection:** Sequential Backward Selection (greedily drop the feature whose removal hurts least, until k remain); **random forest feature importance** = average impurity decrease per feature across trees (no scaling needed). Feature importance = how much each feature contributes to predictions.
- **Curse of dimensionality:** as dimensions grow with fixed data, the space becomes exponentially sparse — "nearest" neighbors are all far away, so distance-based methods (KNN especially) overfit. Fix: dimensionality reduction (feature selection / PCA).
- **Dimensionality reduction — why:** fight sparsity/overfitting, compress, visualize. Technique: PCA (project onto directions of max variance) or the selection methods above.

---

## 3. Logistic Regression (Ch3)

- A **classification** model (despite the name). Better default than perceptron: **converges even when data isn't linearly separable** (smooth sigmoid vs hard step).
- **Odds** = p/(1−p); **logit** = log odds; model: logit(p) = wᵀx → invert:
- **Sigmoid: φ(z) = 1/(1 + e⁻ᶻ)** — squashes ℝ → (0,1), S-curve, output *is* P(y=1|x). Threshold at 0.5 (equivalently sign of z) → label.
- **Cost function** (from maximum likelihood, negated log-likelihood):
  **J(w) = Σ [ −y log φ(z) − (1−y) log(1−φ(z)) ]**
  - Single-instance plot: if y=1, cost = −log φ(z): →0 as φ(z)→1, →∞ as φ(z)→0. Mirror curve for y=0. Draw the two curves crossing (x-axis = φ(z) from 0 to 1).
  - Why log? Product of probabilities → sum (easier derivative, no numerical underflow); flip sign to minimize.
- Update rule ends up identical in form to Adaline's: Δwⱼ = η Σ(y − φ(z))xⱼ.
- **Output is categorical** after thresholding (the *probability* is continuous) — the 2022 final asked exactly this.
- **Linear regression cost = MSE/SSE** — because it's convex, differentiable, and penalizes large errors; suits continuous targets.

---

## 4. SVM (Ch3)

- **Maximum-margin classifier:** picks the hyperplane maximizing the **margin** = distance to closest points (**support vectors**). Larger margin → lower generalization error. Margin = **2/‖w‖**, so maximize it by minimizing ½‖w‖² subject to every point on the correct side — only support vectors define the boundary.
- **Slack variables ξᵢ (soft margin):** real data isn't separable — ξᵢ lets sample i sit inside/across the margin, at a penalty C·Σξᵢ. Guarantees convergence on non-separable data. **Role of C:** large C = narrow margin, fits hard (overfit risk); small C = wide margin, tolerant (underfit risk).
- **Kernel trick** (asked on every final): to separate non-linear data (e.g. XOR), map features to a higher-dimensional space φ(x) where they *become* linearly separable, train a linear SVM there. Computing φ explicitly is expensive — but the SVM only ever needs **dot products**, so a kernel **k(x, z) = φ(x)ᵀφ(z)** computes the high-dim similarity directly without materializing φ. **RBF/Gaussian kernel:** k(x,z) = exp(−γ‖x−z‖²) — a similarity score (1 = identical, 0 = far); γ tuned as hyperparameter.
- Why kernel trick used in SVM (one-liner): to classify linearly inseparable data efficiently by implicit high-dimensional mapping.

---

## 5. Decision Trees, Ensembles (Ch3)

- **Decision tree:** interpretable; root → internal nodes ask threshold questions on features → branches → **leaf nodes** = class decisions. Grow: split on feature with **max information gain**, recurse until pure leaves, **prune / cap max_depth** (deep pure trees overfit).
- **IG(Dₚ, f) = I(parent) − Σ (Nⱼ/Nₚ)·I(childⱼ)** — parent impurity minus weighted child impurity.
- **Impurity measures:**
  - Entropy: −Σ p log₂ p (0 pure, 1 at 50/50)
  - **Gini: 1 − Σ p²** (0 pure, 0.5 at 50/50)
  - Classification error: 1 − max p — OK for pruning, **bad for growing** (insensitive: can score two very different splits identically — see worked example below).
  - Most impure node among (20,20), (40,0), (30,10) → **(20,20)** (perfect 50/50 mix, Gini 0.5 / entropy 1). (40,0) is pure = 0.
- **Random forest:** (1) bootstrap sample (draw n **with replacement**), (2) grow a tree, choosing from d random features at each split (d ≈ √m), (3) repeat k times, (4) **majority vote**. Averages many high-variance trees → robust, rarely needs pruning. **Bootstrapping** = the sampling-with-replacement step.
- **Ensemble learning:** combine many weak learners → strong one. **Main limitation/challenge:** computational cost + loss of interpretability.
- **Boosting (AdaBoost):** train weak learners **sequentially**; after each round, **increase the weights of misclassified examples** so the next learner focuses on them; final prediction = weighted vote of all learners. (vs bagging = parallel, independent samples.)

---

## 6. KNN, Naive Bayes, k-means

- **KNN:** choose k + distance metric (Euclidean p=2, Manhattan p=1) → find k nearest training points → **majority vote**. "k" = number of neighbors consulted.
- **Lazy learner:** it does **no training at all** — just memorizes the dataset; all work happens at prediction time. Differs from other supervised algorithms which learn (and then discard data).
- **Tie in voting?** Use odd k / reduce k / weight votes by distance / pick the closest neighbor's class (sklearn picks first encountered). 
- **k-means limitations:** must pick k in advance; sensitive to initial centroids (can converge to bad local optimum); assumes spherical, equally-sized clusters. **k-means++** fixes initialization: pick first centroid at random, then pick subsequent centroids with probability proportional to squared distance from existing ones → spread-out starting centers, better/faster convergence.
- **Naive Bayes:** P(class|features) ∝ P(class)·Π P(featureᵢ|class) — "naive" = assumes features independent given class. Prior P(class) = class fraction. See worked example below.

---

## 7. Model Evaluation

- **Confusion matrix** (know cold — appears on EVERY paper):

  | | Predicted + | Predicted − |
  |---|---|---|
  | **Actual +** | TP | FN |
  | **Actual −** | FP | TN |

  - **Accuracy** = (TP+TN)/all — % correct overall
  - **Precision** = TP/(TP+FP) — of predicted positives, how many real
  - **Recall** = TP/(TP+FN) — of real positives, how many caught
  - **F1 = 2·P·R/(P+R)** — harmonic mean
  - **Why accuracy fails for imbalanced data:** predict "negative" always on a 99:1 dataset → 99% accuracy, 0 recall. **F1** balances precision & recall so a do-nothing classifier scores 0. Metrics for imbalance: precision, recall, F1, ROC-AUC.
- **Metric for continuous output (regression):** MSE / MAE / R².
- **Overfitting vs underfitting** (know the 3-plot figure: line = underfit/high bias; moderate curve = good; wiggly boundary hugging every point = overfit/high variance). Overfit = great on train, bad on test. **Reduce overfitting:** more data, regularization, simpler model, fewer features, early stopping.
- **Learning curves (accuracy vs #training samples):** big persistent gap between high train-accuracy and low validation-accuracy = **overfitting** → add data/regularize. Both curves plateau low & close = **underfitting** → more complex model/features. Ideal: both converge high with small gap (draw two curves rising and meeting near desired accuracy).
- **Validation curve (accuracy vs C, the T#2 plot):** x-axis = C (inverse regularization). Small C (left): strong regularization → both accuracies low = **underfit**. As C grows both rise; at large C training accuracy keeps climbing but validation accuracy drops = **overfit**. Best C where validation peaks (~10⁻¹–10⁰).
- **Cross-validation purpose:** reliable performance estimate + hyperparameter tuning without touching the test set. **k-fold:** split training data into k folds; train on k−1, validate on 1, rotate k times, average. Diagram: a bar split into k blocks, the shaded validation block sliding across k rows.
- **Nested CV — why:** if you tune hyperparameters with plain CV *and* report that same CV score, it's optimistically biased. Nested = **outer loop** estimates generalization, **inner loop** (inside each outer-training split) does the hyperparameter search. Figure: outer k-fold; each outer training fold subdivided again for the inner search.
- **ROC curve:** TPR vs FPR at every threshold; AUC = 1 perfect, 0.5 random. Use to compare classifiers independent of threshold.
- **Hold-out at minimum:** train/test split (70:30 common; 90:10+ for huge datasets), `stratify=y` keeps class ratios.

---

## 8. Neural network extras (asked in finals)

- **MLP** = multilayer perceptron: input → hidden layer(s) with non-linear activations → output. **Limitation:** needs lots of data/compute, black-box, prone to overfit, vanishing gradients when deep, ignores spatial structure (that's why CNN beats it on images).
- **Activation functions:** **Sigmoid** 1/(1+e⁻ᶻ) → (0,1); **ReLU** max(0, z). **ReLU preferred:** no saturation for z>0 → gradients don't vanish, much cheaper to compute, faster convergence; sigmoid saturates at both ends (derivative ≈ 0) killing learning in deep nets.
- **Why must ANN activation be differentiable?** Training = gradient descent via backpropagation, which needs ∂activation/∂z at every layer to propagate error gradients backward. Non-differentiable → no gradient → no learning.
- **Vanishing gradient problem:** in deep nets, backprop multiplies many small derivatives (sigmoid′ ≤ 0.25) layer after layer → gradient shrinks exponentially → early layers barely learn. RNNs suffer badly because the *same* weights multiply through many time steps.
- **Why CNN for images:** convolution filters share weights and exploit local spatial structure → far fewer parameters, translation-robust feature detection (edges → textures → objects).
- **RNN principle:** hidden state loops back as input for the next time step → memory of sequence; suffers vanishing gradient over long sequences.
- **Transfer learning:** reuse a model pretrained on a big dataset (e.g. ImageNet), fine-tune on your small task → less data/compute needed.
- **Perceptron figure labels (2022 final):** x₁…xₘ = inputs, w₀…wₘ = weights (w₀ = bias), Σ = net input z, then activation function, then threshold/quantizer → output ŷ; error feeds back to update weights.
- **The Keras code** `Sequential([Dense(16, relu), Dense(16, relu), Dense(1, sigmoid)])`: a feed-forward net, two hidden layers of 16 ReLU neurons each, one sigmoid output neuron giving P(class=1) for binary classification. **Sigmoid → softmax:** softmax normalizes over multiple output neurons (probabilities summing to 1) → used for **multiclass**; with a single output it's pointless (always 1). Replacing sigmoid with softmax in a 1-unit perceptron breaks binary probability output; you'd instead use 2+ units.
- **Steps to train a NN:** define architecture → initialize weights → forward pass → compute loss → backpropagate gradients → update weights (optimizer) → repeat over epochs, monitor validation.

---

## 9. NLP bits (finals)

- **Text preprocessing (name two):** tokenization, stop-word removal (also: lowercasing, stemming/lemmatization, punctuation removal).
- **Bag-of-Words:** vocabulary of unique words → each doc becomes a count vector. **Why cap vocabulary size:** vectors grow with vocab → huge sparse matrices, memory blowup, noise from rare words → keep top-N frequent words.
- **1-gram example worked below.**
- **TF-IDF = tf(t,d) × idf(t)**, idf = log(n_docs / (1 + docs containing t)). Rewards words frequent in *this* doc but rare across docs → downweights "the", highlights discriminative words. That's how it "assesses word relevancy."
- **Email spam filter design:** collect labeled spam/ham corpus → preprocess text (tokenize, clean) → vectorize (BoW/TF-IDF) → train classifier (Naive Bayes / logistic regression) → evaluate (precision/recall) → deploy, thresholding P(spam).
- **Missing data / ordinal / metrics for imbalance / logistic output** — covered above (2022 final Q1 mixes Ch4 + evaluation).
- **Induction vs deduction:** induction = learn general rule from specific examples (what ML training does); deduction = apply general rule to specific cases (what inference/prediction does). Representing a class in ML = the learned model/hypothesis h: X→y.

---

# WORKED NUMERICALS — do these by hand tonight

### A. Confusion matrix (malignant/spam version — T#2 Q6, 2022 final 3a)
Positive = Malignant (or Spam). From the 10-row table: rows 2,4,8 = TP; rows 1,9 = FN; row 5 = FP; rows 3,6,7,10 = TN.
- **TP=3, FN=2, FP=1, TN=4**
- Accuracy = 7/10 = **0.70** · Precision = 3/4 = **0.75** · Recall = 3/5 = **0.60**
- F1 = 2(.75×.60)/(.75+.60) = 0.9/1.35 = **0.667**

### B. Confusion matrix (2024 final 6a)
100 positives, 50 negatives; 90 pos & 30 neg predicted correctly.
- TP=90, FN=10, TN=30, FP=20
- Accuracy = 120/150 = **0.80** · Precision = 90/110 ≈ **0.818** · Recall = 90/100 = **0.90**
- F1 = 2(.818×.9)/(1.718) ≈ **0.857**
- F1 useful for imbalance: harmonic mean punishes whichever of P/R is low; accuracy can look great by ignoring the minority class.

### C. Gini first split (2024 final 3b)
8 rows, class Yes=4/No=4 → parent Gini = 1 − (0.5²+0.5²) = **0.5**
- **Weather:** Sunny{No,No,No} G=0 · Overcast{Yes,Yes} G=0 · Rain{Yes,Yes,No} G=1−(4/9+1/9)=**4/9**
  Weighted = (3/8)(0)+(2/8)(0)+(3/8)(4/9) = **0.167** → **IG = 0.333**
- **Temperature:** Hot{No,No,Yes} 4/9 · Mild{Yes,No} 0.5 · Cool{Yes,Yes,No} 4/9
  Weighted = (3/8)(4/9)+(2/8)(.5)+(3/8)(4/9) = **0.458** → IG = 0.042
- **Split on Weather** (IG 0.333 ≫ 0.042).

### D. Gini split A vs B (2020 mid / slide 41)
Parent (40,40), Gini 0.5.
- **A → (30,10),(10,30):** each child 1−(0.75²+0.25²)=0.375 → weighted 0.375 → **IG = 0.125**
- **B → (20,40),(20,0):** left 1−((1/3)²+(2/3)²)=4/9, weight 6/8 → 0.333; right pure 0 → **IG = 0.167**
- **B favoured** (purer child). Classification error would rate both 0.25 — why it's bad for growing.

### E. Perceptron compute (2024 final 5a)
x=[1,−2], w=[0.5,0.25], bias=1: z = 1 + (0.5)(1) + (0.25)(−2) = 1 + 0.5 − 0.5 = **1.0** ≥ 0 → **output +1**.

### F. Epoch/batch (2024 final 5b)
Epoch = full pass; batch = samples per update. 60000/128 = 468.75 → **469 iterations** (468 full + 1 partial batch).

### G. Naive Bayes (2024 final 6c)
Priors from 10 rows: **P(Play)=5/10, P(Study)=3/10, P(Sleep)=2/10.**
Query: Deadline=Near, Weather=Bad, Mood=Off.
- Play: P(Near|Play)=2/5, **P(Bad|Play)=0/5** → score **0**
- Study: (1/3)(3/3)(1/3)×0.3 = **0.033**
- Sleep: (1/2)(2/2)(1/2)×0.2 = **0.05** ← max
- **You will Sleep.** (Mention: zero-probability issue for Play → Laplace smoothing exists.)

### H. k-means one iteration (2022 final 2e) — Manhattan distance
Points A1(2,10) A2(2,5) A3(8,4) A4(5,8) A5(7,5) A6(6,4) A7(1,2) A8(4,9); centers A1, A4, A7.
Distances (to c1,c2,c3): A2:(5,6,**4**) A3:(12,**7**,9) A5:(10,**5**,9) A6:(10,**5**,7) A8:(3,**2**,10)
- **Cluster1 = {A1}** · **Cluster2 = {A3,A4,A5,A6,A8}** · **Cluster3 = {A2,A7}**
- New centers: c1=(2,10) · c2=(30/5,30/5)=**(6,6)** · c3=**(1.5,3.5)**

### I. Bag-of-Words 1-gram (2022 final 3b)
Docs: "The sun is rising" / "The weather is sweet" / "The sun is rising, the weather is sweet, and one and one is two"
Vocab (alphabetical): **and, is, one, rising, sun, sweet, the, two, weather**
- d1 = [0,1,0,1,1,0,1,0,0]
- d2 = [0,1,0,0,0,1,1,0,1]
- d3 = [2,3,2,1,1,1,2,1,1]

### J. Standardize & normalize 0–5 (2020 mid Group B)
Inputs 0,1,2,3,4,5: μ=2.5, σ=√(17.5/6)≈1.708. Norm = x/5.

| x | standardized (x−2.5)/1.708 | normalized |
|---|---|---|
| 0 | −1.46 | 0.0 |
| 1 | −0.88 | 0.2 |
| 2 | −0.29 | 0.4 |
| 3 | 0.29 | 0.6 |
| 4 | 0.88 | 0.8 |
| 5 | 1.46 | 1.0 |

---

# If you only memorize 10 things
1. The 5-step ML roadmap (preprocess → train → select → evaluate → predict)
2. Confusion matrix + accuracy/precision/recall/F1 formulas (numerical guaranteed)
3. Gini = 1−Σp², IG = parent − weighted children (numerical guaranteed)
4. Perceptron↔neuron mapping + update rule + linear separability
5. Adaline SSE cost, why differentiable matters, learning-rate too-big/too-small figure
6. Batch vs SGD vs mini-batch + batch GD's disadvantage
7. Standardization vs normalization formulas + why scaling matters (trees exempt)
8. L1 = diamond = sparse = feature selection; L2 = circle = shrink; C = 1/λ
9. Sigmoid + logistic cost curves; kernel trick in two sentences
10. Overfit/underfit curves (learning curve + validation-vs-C plot) + the 4 remedies
