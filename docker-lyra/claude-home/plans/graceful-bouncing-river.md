# Plan: Derive Generalized Local Rules from the Cascade Commutator

## Context

The research documents establish two parallel frameworks:
- **Algebraic**: Commutation relations between vertex operators (COMMUTATION.tex, ADJOINT.tex Part II)
- **Bijective**: Growth diagram local rules (UNDERLYING_SET.tex, COMMUTATION.tex Section 5)

The standard correspondence: `T(v)P(w) = 1/(1-vw) P(w)T(v)` ↔ Burge local rule. Each commutation step = one local rule application. The scalar `1/(1-vw)` generates face labels.

The Q-weighted cascade commutator in ADJOINT.tex Part II gives:
```
Q*(w)Q(z) = Σ_{a,b} P_a T_b z^a w^b Φ_{a,b}(zw)
```
where `Φ_{a,b}(t) = Σ_k Q_{a+k} Q_{b+k} t^k`.

**Goal**: Derive the "generalized local rule" — the bijective counterpart of the Q-weighted cascade — and write it as Part III of ADJOINT.tex.

## Files to modify

- `/Users/robin/git/research/ADJOINT.tex` — Add Part III (new sections after current Section 14)

## Content structure for Part III

### Section 15: The Standard Algebra–Bijection Correspondence (recap)
- The commutation `T_n P_m = Σ_k P_{m-k} T_{n-k}` IS the Burge local rule
- Face label GF = `1/(1-t)` — universal, profile-independent
- Bijective interpretation: cascade parameter k = |A ∩ B| (overlap in conjugate coordinates)
- Reference the detailed dictionary from COMMUTATION.tex Remark 8

### Section 16: The Q-Kernel
- Derive Q*(w)Q(z) = Σ_{a,b} P_a T_b z^a w^b Φ_{a,b}(zw) from the standard cascade
- Define the Q-kernel: Φ_{a,b}(t) = Σ_{k≥0} Q_{a+k}(q) Q_{b+k}(q) t^k
- Properties:
  - Φ_{a,b}(0) = Q_a Q_b (the k=0 term)
  - Φ_{0,0}(t) = C_0(t) = Σ Q_n² t^n (vacuum expectation)
  - Φ_{a,0}(t) = C_a(t) (cross-correlation from Section 13)
  - Symmetry: Φ_{a,b}(t) = Φ_{b,a}(t) (from commutativity of multiplication)

### Section 17: The Generalized Local Rule
- **Definition**: Same partition geometry as Burge (diamond ν; α, β; λ with cascade k), but face label k carries weight Q_{a+k} · Q_{b+k}
- Weight condition: preserved (same as standard Burge: |λ| = |α| + |β| - |ν| + k)
- The Q-kernel replaces 1/(1-t) as the face-label generating function
- Invertibility: the inverse Q-enriched rule exists (from inverse Burge)

### Section 18: The Q-Enriched Growth Diagram
- Standard GD: face labels ∈ Z≥0, all equally weighted → ALCD
- Q-enriched GD: face labels carry Q-weights → "Q-ALCD"
- The standard GD gives the Borodin product (Level 0)
- The Q-enriched GD gives the cross-correlations (Level Q)
- The commutator [Q(z), Q*(w)] measures the obstruction: the degree to which the Q-enriched creation/annihilation fails to commute

### Section 19: Special Cases and Examples
- d=1: Q_n = 1, Φ_{a,b}(t) = 1/(1-t) — standard Burge recovered
- d=2 (Rogers-Ramanujan): Q_n = q^{n²}, face weight = q^{(a+k)² + (b+k)²} — quadratic form
- d=4, c=(2,2,0): Q_1 = q² + q³ + q⁴ + q⁵, compute Φ_{1,0}(t) and Φ_{1,1}(t) explicitly

### Section 20: Connection to the Involution
- The generalized local rule gives the peel/glue mechanism with Q-weights
- The Q-kernel Φ_{a,b}(t) is the "coupling constant" for the involution
- If Q_n ∈ N[q] (the conjecture), all face labels in the Q-enriched GD are non-negative
- The commutator on the vacuum: the terms with k ≥ 1 are the "cross-level interactions" that the involution must cancel
- Update the open questions to include the new framework

## Verification
1. Compile with `pdflatex -interaction=nonstopmode ADJOINT.tex`
2. Check that the derivation is internally consistent (the Q-kernel reduces to known cases)
3. Verify that d=2 example matches Rogers-Ramanujan formulas
4. Verify page count is reasonable (~18-20 pages total)
