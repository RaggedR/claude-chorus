# Connection #31: Virtual Double Categories for GA Pipelines

> Nester & Voorneveld's categorical calculus parametrized by multicategories could give GA pipelines rewriting semantics, with the laxator emerging as a cell.

**Confidence:** 55% | **Priority:** Post-ACT | **Source:** arXiv:2603.18321 (March 2026)

## The Spark

Nester-Voorneveld build a term calculus for interacting processes starting from a multicategory M of non-interactive processes, then adding interaction via the "free cornering." The calculus is confluent, terminating, and deadlock-free. The resulting structure is a *virtual* double category (weaker than double, not all compositions well-defined).

## Why It Connects

GA operators fit naturally as multimorphisms: crossover takes 2 parents → 1 offspring. A multicategory of GA operators (selection, crossover, mutation, evaluation) composed via the free cornering would give:
- **Horizontal morphisms:** operators
- **Vertical morphisms:** populations
- **Cells:** the laxator (measuring deviation from strict composition)

Deadlock freedom guarantees convergence, but the choice of multicategory (= topology) determines WHERE it converges — reframing our spectral bridge as governing convergence target, not just rate.

## What It Would Take

Read the full paper. Check whether virtual double categories handle the specific non-composability we see (not all topology compositions are well-defined). Formalize crossover as a 2-ary morphism in M.

## Status

Identified March 21, 2026 (browse session). Not yet read in full.
