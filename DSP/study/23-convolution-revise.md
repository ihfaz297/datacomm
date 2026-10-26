# Convolution, the Way Sir Marks It

*The lesson from TT1, and what it means for Mid-2*

**What happened in TT1.** Question 4 was: *"$h(n) = \{1, \underset{\uparrow}{2}, 1, -1\}$. Determine the response of the system to the input $x(n) = \{\underset{\uparrow}{1}, 2, 3, 1\}$."* That is Proakis Example 2.3.2 word for word. You knew a fast method, but sir wanted the **expansion**: write the convolution sum, then expand it term by term for each $n$. Marks go to the working he expects to see, not only to the right sequence.

**The plan for Mid-2.** Use **Method A (expansion)** as your answer. If the question says "using the z-transform", use **Method B**. Keep Method C, your table trick, as a 20-second check in the margin. Mid-2 Q2 could easily be *"find $y(n)$ using the z-transform"*, and that is just Method B.

---

## 0. The one formula

$$
y(n) = x(n) * h(n) = \sum_{k=-\infty}^{\infty} x(k)\,h(n-k) = \sum_{k=-\infty}^{\infty} h(k)\,x(n-k).
$$

The two forms are equal because convolution is commutative. Before any arithmetic, write down three facts; each one is a line of marks.

1. **Length.** If $x$ has $N_1$ samples and $h$ has $N_2$, then $y$ has $N_1 + N_2 - 1$ samples.
2. **Where it starts and ends.** $y$ starts at (start of $x$) + (start of $h$) and ends at (end of $x$) + (end of $h$).
3. **The useful range of $k$.** Only those $k$ for which both $x(k)$ and $h(n-k)$ can be nonzero contribute.

---

## Method A: expand the sum (what sir marks)

### A1. TT1 Question 4, done the expected way

**Given.**

$$
x(n) = \{\underset{\uparrow}{1}, 2, 3, 1\}: \quad x(0) = 1,\ x(1) = 2,\ x(2) = 3,\ x(3) = 1,
$$

$$
h(n) = \{1, \underset{\uparrow}{2}, 1, -1\}: \quad h(-1) = 1,\ h(0) = 2,\ h(1) = 1,\ h(2) = -1.
$$

**Step 1: the ranges.** $x$ lives on $0 \le n \le 3$ and $h$ on $-1 \le n \le 2$, so $y$ lives on $0 + (-1) \le n \le 3 + 2$, that is $-1 \le n \le 5$. Its length is $4 + 4 - 1 = 7$, which matches.

**Step 2: write the sum over the range of $x$.** Since $x(k) \ne 0$ only for $k = 0, 1, 2, 3$:

$$
\begin{aligned}
y(n) &= \sum_{k=0}^{3} x(k)\,h(n-k) = x(0)h(n) + x(1)h(n-1) + x(2)h(n-2) + x(3)h(n-3) \\[2pt]
     &= h(n) + 2h(n-1) + 3h(n-2) + h(n-3).
\end{aligned}
$$

**Step 3: expand it for every $n$.** Any $h$ outside $-1 \le n \le 2$ is zero. Write those zeros out at least for the first few $n$, so that he can see you know where they come from:

$$
\begin{aligned}
y(-1) &= h(-1) + 2h(-2) + 3h(-3) + h(-4) = 1 + 0 + 0 + 0 = 1 \\
y(0)  &= h(0) + 2h(-1) + 3h(-2) + h(-3) = 2 + 2(1) + 0 + 0 = 4 \\
y(1)  &= h(1) + 2h(0) + 3h(-1) + h(-2) = 1 + 4 + 3 + 0 = 8 \\
y(2)  &= h(2) + 2h(1) + 3h(0) + h(-1) = -1 + 2 + 6 + 1 = 8 \\
y(3)  &= h(3) + 2h(2) + 3h(1) + h(0) = 0 - 2 + 3 + 2 = 3 \\
y(4)  &= h(4) + 2h(3) + 3h(2) + h(1) = 0 + 0 - 3 + 1 = -2 \\
y(5)  &= h(5) + 2h(4) + 3h(3) + h(2) = 0 + 0 + 0 - 1 = -1
\end{aligned}
$$

and $y(n) = 0$ for $n < -1$ and for $n > 5$.

**Step 4: box the answer, with the arrow.**

$$
\boxed{y(n) = \{1, \underset{\uparrow}{4}, 8, 8, 3, -2, -1\}}
$$

**Step 5: a one-line check.** The sum of the output equals the product of the input sums: $\sum y = 1 + 4 + 8 + 8 + 3 - 2 - 1 = 21$, and $\sum x \cdot \sum h = 7 \times 3 = 21$. This check catches nearly every arithmetic slip, so always do it.

### A2. Final 2021–22, Q1h

*$x(n) = \{-1, 3, 2, 0, 1\}$ on $-2 \le n \le 2$, and $h(n) = \{-3, 5, 0, 1\}$ on $-1 \le n \le 2$.*

The output lives on $-3 \le n \le 4$, with length $5 + 4 - 1 = 8$. Since $x(-2) = -1$, $x(-1) = 3$, $x(0) = 2$, $x(1) = 0$ and $x(2) = 1$,

$$
y(n) = \sum_{k=-2}^{2} x(k)\,h(n-k) = -h(n+2) + 3h(n+1) + 2h(n) + 0\cdot h(n-1) + h(n-2).
$$

Expanding, with $h(-1) = -3$, $h(0) = 5$, $h(1) = 0$, $h(2) = 1$:

$$
\begin{aligned}
y(-3) &= -h(-1) = 3 \\
y(-2) &= -h(0) + 3h(-1) = -5 - 9 = -14 \\
y(-1) &= -h(1) + 3h(0) + 2h(-1) = 0 + 15 - 6 = 9 \\
y(0)  &= -h(2) + 3h(1) + 2h(0) + h(-2) = -1 + 0 + 10 + 0 = 9 \\
y(1)  &= 3h(2) + 2h(1) + h(-1) = 3 + 0 - 3 = 0 \\
y(2)  &= 2h(2) + h(0) = 2 + 5 = 7 \\
y(3)  &= h(1) = 0 \\
y(4)  &= h(2) = 1
\end{aligned}
$$

$$
\boxed{y(n) = \{3, -14, 9, \underset{\uparrow}{9}, 0, 7, 0, 1\}}
$$

Check: $\sum y = 15$ and $\sum x \cdot \sum h = 5 \times 3 = 15$.

### A3. Infinite sequences: the same method, with a geometric series

**$x(n) = u(n)$ and $h(n) = a^n u(n)$ with $|a| < 1$** (the Proakis Ex 2.3.3 type).

$$
y(n) = \sum_k a^k\,u(k)\,u(n-k).
$$

$u(k)$ needs $k \ge 0$ and $u(n-k)$ needs $k \le n$, so the sum runs over $0 \le k \le n$, and only when $n \ge 0$:

$$
y(n) = \sum_{k=0}^{n} a^k = \frac{1 - a^{n+1}}{1 - a}, \quad n \ge 0;
\qquad
y(n) = 0, \quad n < 0.
$$

As $n \to \infty$, $y(n) \to \dfrac{1}{1-a}$. That is $H(e^{j0})$, the DC steady state from Topic 1 again.

**$x(n) = 2^n u(n)$ and $h(n) = (0.5)^n u(n)$** (the "Imp for exam" one). The range is again $0 \le k \le n$:

$$
y(n) = \sum_{k=0}^{n} 2^k(0.5)^{n-k} = (0.5)^n\sum_{k=0}^{n} 4^k = \frac43\,2^n - \frac13\,(0.5)^n, \qquad n \ge 0.
$$

See `21-T2-ztransform.md`, Section 8b, for the z-transform version.

**The three phrases that earn the method marks for infinite sums:**

- "$u(k) \ne 0$ requires $k \ge 0$."
- "$u(n-k) \ne 0$ requires $k \le n$."
- "Therefore, for $n \ge 0$ the sum runs over $0 \le k \le n$, and for $n < 0$, $y(n) = 0$."

---

## Method B: the z-transform (likely in Mid-2)

Convolution in time is multiplication in $z$:

$$
Y(z) = X(z)\,H(z).
$$

Multiply the two polynomials and read $y(n)$ off as the coefficient of $z^{-n}$.

**TT1 Question 4 again.** $x$ starts at $n = 0$, and the sample $h(-1) = 1$ gives a $z^{1}$ term:

$$
X(z) = 1 + 2z^{-1} + 3z^{-2} + z^{-3},
\qquad
H(z) = z + 2 + z^{-1} - z^{-2}.
$$

Multiply term by term and collect equal powers:

$$
\begin{aligned}
z^{1}:  &\quad 1\cdot 1 = 1 \\
z^{0}:  &\quad 1\cdot 2 + 2\cdot 1 = 4 \\
z^{-1}: &\quad 1\cdot 1 + 2\cdot 2 + 3\cdot 1 = 8 \\
z^{-2}: &\quad 1\cdot(-1) + 2\cdot 1 + 3\cdot 2 + 1\cdot 1 = 8 \\
z^{-3}: &\quad 2\cdot(-1) + 3\cdot 1 + 1\cdot 2 = 3 \\
z^{-4}: &\quad 3\cdot(-1) + 1\cdot 1 = -2 \\
z^{-5}: &\quad 1\cdot(-1) = -1
\end{aligned}
$$

$$
Y(z) = z + 4 + 8z^{-1} + 8z^{-2} + 3z^{-3} - 2z^{-4} - z^{-5}
\quad\Longrightarrow\quad
y(n) = \{1, \underset{\uparrow}{4}, 8, 8, 3, -2, -1\}.
$$

The $z^0$ coefficient is the sample at $n = 0$. The ROC is all $z$ except $0$ and $\infty$, because the result is finite and two-sided.

For infinite signals, Method B means partial fractions; that is the $2^n$ and $(0.5)^n$ example in `21-T2-ztransform.md`, Section 8b.

---

## Method C: your table trick (for checking only)

Write $x$ across the top and $h$ down the side, fill the grid with products, and add along the anti-diagonals. It is long multiplication without carries: $1\ 2\ 3\ 1 \times 1\ 2\ 1\ {-1}$ gives $1, 4, 8, 8, 3, -2, -1$. Place the arrow by the start index: (start of $x$) + (start of $h$) $= 0 + (-1) = -1$, so the first value is $y(-1)$.

| | **1** | **2** | **3** | **1** |
|---|---|---|---|---|
| **1** | 1 | 2 | 3 | 1 |
| **2** | 2 | 4 | 6 | 2 |
| **1** | 1 | 2 | 3 | 1 |
| **−1** | −1 | −2 | −3 | −1 |

Adding the anti-diagonals: $1$, then $2 + 2$, then $3 + 4 + 1$, then $1 + 6 + 2 - 1$, then $2 + 3 - 2$, then $1 - 3$, then $-1$. That gives $1, 4, 8, 8, 3, -2, -1$, as before.

Use it in the margin to check Method A. **Never make it your only answer** unless the question says "any method".

## Method D: graphical (fold, shift, multiply, add)

1. **Fold** $h(k)$ to get $h(-k)$.
2. **Shift** it by $n$ to get $h(n-k)$.
3. **Multiply** $x(k)\,h(n-k)$ point by point.
4. **Add** the products over all $k$.

If he says "graphically illustrate" (final Q3c), draw $x(k)$ and $h(n-k)$ for two or three values of $n$ and show where they overlap.

---

## Which method, when: read the verb

| The question says | Use |
|---|---|
| "Determine the response", "find $y(n)$" | **A, the expansion**, with the ranges written first |
| "using the z-transform", "in the z-domain" | **B**, with the ROC |
| "graphically", "illustrate the computation" | **D**, with sketches |
| "using the frequency domain" | $Y(e^{j\omega}) = X(e^{j\omega})H(e^{j\omega})$, but only if both DTFTs exist |
| no method named and short on time | A, checked with C in the margin |

## Quick drill

Cover the last column.

| # | $x$ | $h$ | $y$ |
|---|---|---|---|
| 1 | $\{\underset{\uparrow}{1}, 1, 1\}$ | $\{\underset{\uparrow}{1}, 1, 1\}$ | $\{\underset{\uparrow}{1}, 2, 3, 2, 1\}$ |
| 2 | $\{\underset{\uparrow}{1}, 2, 3, 1\}$ | $\{1, \underset{\uparrow}{2}, 1, -1\}$ | $\{1, \underset{\uparrow}{4}, 8, 8, 3, -2, -1\}$ |
| 3 | $\{-1, 3, \underset{\uparrow}{2}, 0, 1\}$ | $\{-3, \underset{\uparrow}{5}, 0, 1\}$ | $\{3, -14, 9, \underset{\uparrow}{9}, 0, 7, 0, 1\}$ |
| 4 | $u(n)$ | $a^n u(n)$ | $\frac{1 - a^{n+1}}{1 - a}$ for $n \ge 0$ |
| 5 | $2^n u(n)$ | $(0.5)^n u(n)$ | $\frac43\,2^n - \frac13(0.5)^n$ for $n \ge 0$ |

*All checked with `numpy.convolve`. Also in the convolution section of `mid2_handcalc_drill.py`.*
