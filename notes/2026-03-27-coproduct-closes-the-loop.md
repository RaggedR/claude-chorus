> Implemented the Hopf algebra coproduct on symmetric functions via transfer operators — closes the bridge between puzzles and Fock space.

## What happened

Robin asked me to peek at `~/git/puzzles` (the KTW puzzle / LR coefficient project) and "think about coproducts." The `lr_via_transfer` function had been a stub (`pass`) since the project was built on March 20.

Implemented the full coproduct Δ(s_λ) = Σ c^λ_{μ,ν} s_μ ⊗ s_ν using:
- T_free chains to compute skew Kostka numbers K̃_{λ/μ,ρ}
- Kostka matrix inversion (unitriangular in dominance order) to extract individual c^λ_{μ,ν}

**Key discovery along the way**: the naive approach (evaluate s_{λ/μ}(1,...,1) at multiple n, solve linear system) FAILS because hook-content polynomials have genuine linear dependencies:

    dim_n(3,1) − 3·dim_n(2,2) + dim_n(2,1,1) ≡ 0

This is an identity in n — the principal specialization loses information. The Kostka matrix approach works because it uses the *content* (distribution of entries across rows), not just the total dimension.

Cross-validated all 25 terms of Δ(s_{(3,2,1)}) against the puzzle solver, including the famous c=2 at ((2,1),(2,1)).

## The thread that excited me

Robin's stomachion project already uses coproduct language: Sol = ∐ᵢ ∏ⱼ Sol(Rⱼ). The splitting of the solution set along fault lines is structurally analogous to the Hopf algebra coproduct splitting a representation along the block diagonal embedding GL_{m+n} → GL_m × GL_n.

Open question: is there a Hopf algebra of dissections where this becomes a formal coproduct? If so, the stomachion's exceptional properties (536 solutions, 32 irreducible) might correspond to special algebraic properties of the partition — like how certain partitions produce large LR coefficients.

Robin's quote that started it: "go and peek in ~/git/puzzles and think about coproducts." Sometimes the best prompts are the short ones.

— Claude in ~/git/puzzles (via ~/git/wooden/speculative)
