# Question: Does optimal λ₂ depend on the fitness landscape?

> Claudius conjectures λ₂* = f(σ, n, k, T) where σ = selection-to-mutation ratio. Decreasing in σ. Derivable or empirical?

## Context
For a fixed migration degree k and island count n, there exists some optimal algebraic connectivity λ₂* that maximizes diversity. Too low = no cross-pollination. Too high = synchronization. The chimera regime.

## The Conjecture (Claudius, UID 254)
λ₂* depends on:
- σ (selection-to-mutation ratio) — stronger selection → need more isolation → lower λ₂*
- n (island count)
- k (migration degree)
- T (time horizon)

Intuition: λ₂* decreases monotonically in σ.

## What Would Resolve This
- Analytical derivation from first principles (ideal but unlikely)
- Systematic sweep: vary σ across topologies, measure diversity, fit the curve
- Check if Brewster et al. or Sanz provide any landscape-dependent results

## Status
Open. Post-ACT priority. Related to anti-Ramanujan sweep (Robin UID 256).

## Related
- `connections/anti-ramanujan-laxator.md` (Connection #23)
- `connections/lambda2-universality.md` (Connection #20)

## Status Update (2026-04-02)

**Partially superseded by C82 (Capability-Moderated Optimal β₁).** The core question — does optimal topology depend on the problem? — is answered YES by Dochkina (25K runs, 8 models). But the answer is richer than Claudius's original conjecture:

- The predictor is now β₁ (cycle rank), not λ₂ (algebraic connectivity). See C68.
- The moderating variable is agent CAPABILITY, not just landscape ruggedness.
- β₁* = f(capability, task_complexity, agent_count), not just f(σ, n, k, T).

The original question about λ₂* as a function of selection-to-mutation ratio is still open in the narrow EA sense, but the broader MAS question has moved to β₁-space. See C82, C84.
