# Plan: Bijective Proof of Warnaar's Conjecture 2.7 via Local Rules

## Goal
Use the Burge local rule and growth diagram machinery to construct an explicit sign-reversing involution on the signed objects of the q-binomial decomposition, proving positivity of Q_{n,c}(q).

## Background

The conjecture states Q_{n,c}(q) has nonneg coefficients, where:
- Q_n = Σ_{j=0}^n (-1)^j q^{j(j+1)/2} [n choose j]_q h_{n-j}
- h_m = (q)_m · g_m, where g_m = [z^m] F_c(z,q) and F_c = (zq;q)_∞ · GK_c

The signed objects are tuples (j, λ, S, π) where:
- j indexes the alternating sum (sign contribution (-1)^j)
- λ is a partition in an (n-j) × j box (from [n,j]_q)
- S ⊆ {j+1,...,n} is a subset (from (q)_n/(q)_j = Π(1-q^k), sign contribution (-1)^|S|)
- π is a CPP of max-entry m = n-j (from h_m)
- Total sign = (-1)^{j+|S|}, weight = T_j + |λ| + Σ S + |π|

The Burge forward rule U_{α,β}(m,ν) = λ constructs partitions via sets A, B, C (cascade), D (free columns), with the key first-part property: λ_1 = max(α_1, β_1) + ε where ε ∈ {0,1} depends on column 1's membership in A∪B∪C∪D.

## Implementation Plan

### Phase A: Growth Diagram Construction (`growth_diagram.py`)

**A1. Implement the Burge forward rule**
- Input: partitions α, β, ν and integer m
- Work with conjugate partitions (column lengths): α', β', ν'
- Compute sets A = {i : α'_i > ν'_i} (columns where α is longer than ν)
- Compute sets B = {i : β'_i > ν'_i} (columns where β is longer than ν)
- Cascade: for each i ∈ A∩B (in order), find ε(i) = smallest integer > i not in A∪B and not already used; set C = {ε(i) | i ∈ A∩B}
- Free columns D = first m elements of complement of A∪B∪C
- λ is obtained from ν by adding a box to each column in A∪B∪C∪D (i.e., λ'_i = ν'_i + 1 for i ∈ A∪B∪C∪D)
- Output: λ = U_{α,β}(m,ν)
- Validate against thesis example: U_{(6,5,5,3),(6,6,5,2)}(1,(6,5,4,2)) = (7,6,5,3,1)
  - ν'=(4,4,3,3,2,1), A={3,5}, B={5,6}, A∩B={5}, C={7}, D={1}, so add box to cols {1,3,5,6,7} → λ'=(5,4,4,3,3,2,1) → λ=(7,6,5,3,1) ✓

**A2. Implement the Burge inverse (decomposition) rule**
- Input: partitions α, β, λ
- Compute Ā = {i : λ'_i > α'_i} (columns where λ is longer than α)
- Compute B̄ = {i : λ'_i > β'_i} (columns where λ is longer than β)
- Cascade (reverse): for each i ∈ Ā∩B̄ (in decreasing order), find δ(i) = largest integer < i not in Ā∪B̄ and not already used; C̄ = {δ(i) > 0}
- m = #{δ(i) ≤ 0} (cascades that fall off the left end)
- ν obtained from λ by removing a box from each column in Ā∪B̄∪C̄
- Output: (m, ν) such that U_{α,β}(m,ν) = λ
- Validate: D(U(m,ν)) = (m,ν) and U(D(λ)) = λ using thesis example

**A3. Implement the growth diagram class**
- `GrowthDiagram(c, cpp)`: given profile c=(c0,c1,c2) and a CPP π=(ν1,ν2,ν3), construct the full growth diagram
- The diagram has shape determined by rank r=3 and profile c
- Apply Burge rules along rows to fill in all partition entries
- Extract: boundary word γ, diagonal weights δ_k(d), the ALCD labeling at each cell
- Verify strong weight preservation: |μ^k| = |γ| + |diag(k)|_d

**A4. Validate against known results**
- For c=(2,1,1), d=4: enumerate all max-1 CPPs (5 per weight for w≥3), build growth diagrams, verify boundary partitions match expected sizes
- Cross-check: the max statistic max(π) should equal γ_1 + max_k δ_k(d) from the growth diagram

### Phase B: Refined Signed Object Enumeration (`involution_v2.py`)

**B1. Enumerate signed objects at the individual CPP level**
- For each (j, λ, S, π), record:
  - The CPP π as a triple (ν1, ν2, ν3)
  - The growth diagram GD(π) with its boundary word and ALCD labeling
  - The ε values at each cell (whether column 1 is in A∪B∪C∪D)
  - The partition λ and subset S explicitly

**B2. Weight-by-weight signed object tables**
- For each weight w, list all signed objects with sign and weight
- Verify: Σ signs = coefficient of q^w in Q_{n,c}(q)
- Display the growth diagram data alongside each object

**B3. Identify cancellation patterns**
- At each weight where cancellation occurs, identify which positive objects pair with which negative objects
- Look for patterns in how the growth diagram structure relates to the pairing

### Phase C: Involution Search and Testing

**C1. ε-toggle involution candidate**
- Key idea: in the Burge rule, ε ∈ {0,1} at each cell determines whether column 1 joins D or not
- Toggling ε changes λ_1 by ±1, which can shift weight by 1
- This maps CPPs with max entry m to modified objects, potentially changing the (j, S) component
- Implement: given (j, λ, S, π), try toggling the ε at the "outermost" cell of GD(π) and see if this produces a valid partner with opposite sign

**C2. Subset-toggle involution candidates**
- Alternative: fix π and toggle an element of S (changing sign by (-1))
- This changes weight by the toggled element k ∈ {j+1,...,n}
- Need a canonical choice of which element to toggle
- Try: toggle the smallest k ∈ S if |S| > 0 to get a partner; otherwise the object is a fixed point

**C3. Combined involution**
- The involution likely needs to combine both mechanisms:
  - Sometimes toggle an element of S (weight change = k)
  - Sometimes change j by ±1 (redistributing between λ and π via growth diagram)
- Test all candidates computationally for c=(2,1,1) n=1,2 and c=(2,2,1) n=1,2

**C4. Exhaustive search for small cases**
- For n=1 d=4 (6 objects, 1 neg): find the unique involution
- For n=2 d=4 (36 objects, 10 neg): find all valid involutions
- Characterize which rule each involution uses

### Phase D: Pattern Identification and Proof

**D1. Analyze involution structure across profiles**
- Run Phase C for d=1,2,4,5,7 (all tested profiles)
- Identify whether the same rule works uniformly

**D2. Characterize fixed points**
- The fixed points of the involution are exactly the objects contributing to Q_{n,c}(q)
- These must all be positive and their weight distribution must match Q_{n,c}(q)
- Characterize: what makes a signed object a fixed point?

**D3. Formalize the proof**
- If a uniform involution is found: write the formal proof that it is
  (a) sign-reversing on non-fixed-points
  (b) weight-preserving
  (c) an involution (applying twice gives identity)
- If the involution uses the growth diagram ε toggle: connect to the algebraic commutation lemma

**D4. Update LaTeX notes**
- Add a new section (Section 8) with the proof
- Include the involution definition, key lemma (it's an involution), fixed point characterization
- Add examples from the computational verification

## File Structure

```
growth_diagram.py    # NEW: Phase A (Burge rules, GrowthDiagram class)
involution_v2.py     # NEW: Phases B-D (refined enumeration, involution search)
involution.py        # EXISTING: keep for reference (coarser enumeration)
compute_gk.py        # EXISTING: unchanged (core CPP enumeration)
```

## Testing Strategy

- Phase A: validate against thesis examples, then cross-check with existing compute_gk.py output
- Phase B: verify signed object sums match Q_{n,c}(q) from verify_conjecture.py
- Phase C: verify involution is weight-preserving, sign-reversing, and involutory
- Phase D: verify fixed point weights match Q_{n,c}(q) coefficients

## Key Mathematical Insight

The q-binomial decomposition Q_n = Σ (-1)^j q^{T_j} [n,j]_q h_{n-j} involves:
- Positive terms (j even) contributing CPPs with max ≤ n-j
- Negative terms (j odd) contributing CPPs with max ≤ n-j

The growth diagram provides a **bridge** between these: by modifying the ε parameter at the boundary cell, we can change the max-entry constraint, effectively mapping a max-m CPP to a max-(m±1) CPP while adjusting the partition λ and/or subset S to maintain weight. This is the mechanism that should power the sign-reversing involution.

The Burge rule's first-part property (λ_1 = max(α_1,β_1) + ε) means that toggling ε at the right cell changes the "size" of the growth diagram boundary, which corresponds to shifting between adjacent terms in the alternating sum.
