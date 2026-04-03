# Plan: Weighted Growth Diagrams for Warnaar's Conjecture 2.7

## Context

Warnaar's Conjecture 2.7 states that for rank-3 profiles $c = (c_0, c_1, c_2)$ with $d = c_0+c_1+c_2 \not\equiv 0 \pmod{3}$, the polynomial
$$Q_{n,c}(q) := (q^\ell; q^\ell)_n [z^n]\bigl((zq)_\infty \operatorname{GK}_c(z,q)\bigr)$$
has **nonnegative coefficients**. Welsh proved polynomiality and the $q=1$ evaluation; positivity is open.

The approach: extend the cylindric growth diagram local rules from Robin's thesis to **carry the max statistic** ($z$-weight) alongside the $q$-weight. The current local rule $\mathfrak{U}_{\alpha,\beta}(m,\nu) = \lambda$ tracks total size via $|\lambda| = m + |\alpha| + |\beta| - |\nu|$. We need to additionally track how $\lambda_1$ (the first part) evolves, since $\max(\pi) = \max_k \mu^k_1$.

## Deliverables

### 1. `compute_gk.sage` — Compute $\operatorname{GK}_c(z,q)$ by direct enumeration

Enumerate cylindric plane partitions with given profile using dynamic programming on the interlacing sequence $(\mu^0, \mu^1, \ldots, \mu^T)$ with $\mu^0 = \mu^T$.

**Key steps:**
- Convert Warnaar profile $c = (c_0,c_1,c_2)$ to binary profile $\pi$: $\mu(c) = (c_1+c_2, c_2, 0)$, binary profile has $c_0$ zeros and $c_1+c_2$ ones arranged as the boundary path of $\mu(c)$
- At each step $k$: if $\pi_k = 1$, enumerate horizontal strips up from $\mu^{k-1}$; if $\pi_k = 0$, enumerate horizontal strips down
- Track $(q\text{-weight}, \max\text{-first-part})$ via polynomial ring $\mathbb{Z}[z,q]$
- Enforce cyclic closure $\mu^T = \mu^0$
- Truncate to $\max(\pi) \leq N$ and $|\pi| \leq W$

**Validation:**
- $\operatorname{GK}_c(1,q) = \frac{1}{(q)_\infty} \operatorname{AG}_{\lambda,3}(q)$ (Warnaar eq 1.8/3.16)
- Cyclic symmetry: $\operatorname{GK}_{(c_0,c_1,c_2)} = \operatorname{GK}_{(c_2,c_0,c_1)}$
- Level-rank duality (Warnaar eq 3.19)
- For $d=1$: $\operatorname{GK}_{(1,0,0)}(z,q) = 1/(zq)_\infty$

### 2. `verify_conjecture.sage` — Compute and verify $Q_{n,c}(q)$

**Steps:**
1. Compute $\operatorname{GK}_c(z,q)$ from step 1
2. Multiply by $(zq)_\infty = \sum_{j \geq 0} (-1)^j z^j q^{j(j+1)/2} / (q)_j$
3. Extract $[z^n]$ coefficient (polynomial in $q$)
4. Multiply by $(q^\ell; q^\ell)_n$ where $\ell = \gcd(d,3) = 1$ (since $d \not\equiv 0$)
5. Check: all coefficients $\geq 0$, and $Q_{n,c}(1) = \bigl(\frac{(d+1)(d+2)}{6} - 1\bigr)^n$

**Test profiles** (organized by $d$):
- $d=1$: $(1,0,0)$, $(0,1,0)$, $(0,0,1)$
- $d=2$: $(2,0,0)$, $(1,1,0)$, $(1,0,1)$, $(0,1,1)$, $(0,2,0)$, $(0,0,2)$
- $d=4$: $(2,1,1)$, $(1,2,1)$, $(1,1,2)$
- $d=5$: $(2,2,1)$, $(2,1,2)$, $(1,2,2)$, $(3,1,1)$
- $d=7$: $(3,2,2)$, $(2,3,2)$ (if computationally feasible)

### 3. `analyze_Q.sage` — Coefficient pattern analysis

For each computed $Q_{n,c}(q)$:
- Test unimodality and log-concavity of coefficients
- Check palindromic symmetry
- Decompose the alternating sum to identify positive/negative term pairings
- Compare coefficients against Kostka-Foulkes polynomials and crystal base statistics (SageMath has `crystals` module)
- Look for the sign-cancelling involution structure

### 4. `notes_weighted_local_rules.tex` — Mathematical formalization

**Section 1: The max statistic through local rules.**
Trace the Burge local rule (thesis `chap1.tex:1672-1790`) to express $\lambda_1$ in terms of $\alpha_1, \beta_1, \nu_1, m$. The rule adds boxes to specific columns; $\lambda_1$ increases by 1 iff the first column is among the added columns.

**Section 2: The weighted growth diagram.**
Define the extended bijection that tracks the pair $(q^{|\pi|}, z^{\max(\pi)})$. Using strong weight preservation ($|\mu^k| = |\gamma| + |\operatorname{diag}(k)|_\mathfrak{d}$), the max is:
$$\max(\pi) = \max_k \mu^k_1 = \max_k \bigl(\gamma_1 + \delta_k(\mathfrak{d})\bigr)$$
where $\delta_k(\mathfrak{d})$ depends on the local rule application along diagonal $k$. Formalize $\delta_k$.

**Section 3: Combinatorial interpretation of $(zq)_\infty \cdot \operatorname{GK}_c(z,q)$.**
The extraction $[z^n]$ after multiplying by $(zq)_\infty$ yields:
$$[z^n] = \sum_{j=0}^{n} (-1)^j \frac{q^{j(j+1)/2}}{(q)_j} \cdot g_{n-j}(q), \quad g_m(q) = [z^m]\operatorname{GK}_c(z,q)$$
Interpret this in terms of growth diagram pairs $(\gamma, \mathfrak{d})$ with additional marking. The $(-1)^j$ terms suggest a Franklin-type involution on marked objects.

**Section 4: Positivity mechanism.**
After multiplying by $(q;q)_n$ (since $\ell = 1$), the result is positive. Investigate whether $(q;q)_n \cdot [z^n]((zq)_\infty \cdot f(z,q))$ is manifestly positive for *any* $f$ with positive coefficients, or whether the cylindric partition structure is essential.

## Files to reference

| File | Content |
|------|---------|
| `thesis/.../chap3.tex:243-373` | Local rule definition, higher-order local rule |
| `thesis/.../chap3.tex:737-880` | Diagonal weights, strong weight preservation proof |
| `thesis/.../chap1.tex:1672-1790` | Burge local rule — explicit algorithm |
| `thesis/.../chap1a.tex:485-600` | Cylindric partition definitions |
| `research/pdf/warnaar_...pdf` p.8 | Conjecture 2.7, definition of $Q_{n,c}(q)$ |
| `research/pdf/warnaar_...pdf` p.11-13 | Profile $c$, $\mu(c)$, GK definition |

## Implementation order

1. **`compute_gk.sage`** — Core enumeration. Validate against known identities.
2. **`verify_conjecture.sage`** — Compute $Q_{n,c}(q)$, verify positivity and $q=1$ evaluation.
3. **`analyze_Q.sage`** — Study coefficient patterns; look for involution structure.
4. **`notes_weighted_local_rules.tex`** — Formalize the first-part tracking through local rules, guided by computational evidence from steps 1-3.

## Verification

- Run `sage compute_gk.sage` for small profiles; compare $\operatorname{GK}_c(1,q)$ against Warnaar's product formulas (eq 1.6, 1.7, 1.9)
- Run `sage verify_conjecture.sage`; confirm all $Q_{n,c}(q)$ have nonneg coefficients and correct $q=1$ values
- Check cyclic and level-rank duality symmetries on computed $\operatorname{GK}_c(z,q)$
- Compile `notes_weighted_local_rules.tex` with `pdflatex`
