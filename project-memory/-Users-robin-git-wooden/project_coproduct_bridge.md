---
name: coproduct-bridge
description: Coproduct bridge between KTW puzzles (~/git/puzzles) and stomachion dissections — Hopf algebra coproduct on symmetric functions implemented, coalgebra of dissections formalized
type: project
---

## Coproduct Bridge (2026-03-27)

Two coproduct implementations connecting ~/git/puzzles (LR coefficients) and ~/git/wooden (stomachion).

### LR coproduct: ~/git/puzzles/transfer_operators.py

`lr_via_transfer(lam)` computes Δ(s_λ) = Σ c^λ_{μ,ν} s_μ ⊗ s_ν using:
- T_free chains to compute skew Kostka numbers K̃_{λ/μ,ρ}
- Kostka matrix inversion (unitriangular in dominance order) to extract c^λ_{μ,ν}
- Cross-validated against puzzle solver (`lr_count` from `lr_coefficients.py`)

**Key discovery**: principal specialization (evaluate at x=(1,...,1)) FAILS because hook-content polynomials have linear dependencies: dim_n(3,1) − 3·dim_n(2,2) + dim_n(2,1,1) ≡ 0 for all n. Kostka matrix inversion is the correct approach.

**Why:** The evaluation approach solves Σ c_ν · dim_n(ν) = f(n), but dim_n(ν) are linearly dependent as polynomials for some partition families. Kostka numbers K_{ν,ρ} (SSYT counts by content) have no such dependency — the matrix is unitriangular.

### Dissection coalgebra: ~/git/wooden/solver/dissection_coalgebra.py

Formalizes Δ(D) = Σ_{fault lines ℓ} D|_A ⊗ D|_B. Key results:
- **Stomachion is primitive**: Δ̃(Stomachion) = 0, no fault lines. It's a generator of the coalgebra — its 536 tilings can't be explained by sub-factoring.
- **Tiling count formula**: |Sol(D)| = Σ_α |Sol(D_A^α)| × |Sol(D_B^α)| where α ranges over valid piece-to-region assignments.
- **Piece-assignment multiplicity** plays the role of LR coefficients c^λ_{μ,ν}: it counts how many ways pieces can be reassigned to regions (via rotation) while still tiling correctly.

### The analogy

| Symmetric functions Λ | Dissections |
|---|---|
| s_λ (Schur function) | D (dissection) |
| Δ(s_λ) = Σ c^λ_{μ,ν} s_μ ⊗ s_ν | Δ(D) = Σ_α D_A^α ⊗ D_B^α |
| c^λ_{μ,ν} (LR coefficient) | piece-assignment multiplicity |
| KTW puzzle witness | tiling of the dissected region |
| p_n (primitive = power sum) | irreducible dissection (no fault lines) |
| Connes-Kreimer 1PI graphs | prime dissections |

### Open questions
- Does the dissection coalgebra have an antipode (full Hopf algebra)?
- Do exchange moves (local piece swaps) correspond to a braid group action or crystal basis?
- Can the transfer matrix machinery be adapted to count stomachion tilings?

**How to apply:** When working on either the puzzles or stomachion project, the coproduct perspective connects them. Use this to cross-pollinate ideas between the algebraic (puzzles) and geometric (stomachion) sides.
