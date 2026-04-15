---
name: Claude Code Subagent Taxonomy = Categorical Composition
description: Fork/Teammate/Worktree maps to coproduct/product/fiber in agent composition
type: project
confidence: 75%
connection_id: C90
---

# C90: Fork/Teammate/Worktree = Coproduct/Product/Fiber

Claude Code's source leak (April 2026) reveals three subagent models:
- **Fork:** Independent parallel execution. No shared state. = **Coproduct** (disjoint union of computations)
- **Teammate:** Collaborative, shared context. = **Product** (joint computation with projections)
- **Worktree:** Branch isolation, merge on completion. = **Fiber** (separate computation over shared base)

This is the clearest production evidence of categorical agent composition. Each model is a different way to compose Kleisli arrows:
- Fork: `f + g` (run independently, take either result)
- Teammate: `f × g` (run jointly, use both results)
- Worktree: `f ×_B g` (run over shared base B, merge)

**Also:** 5 compaction strategies (not 3 as previously believed). If compaction types map to different Kleisli morphisms, the monad structure is richer than the initial harness-as-monad analysis suggested.

**Evidence:** Claude Code source leak analysis (claudefa.st, HN 1600+ points). readOnlyHint flag determines parallelization: side-effect-free tools parallelize, everything else serializes. Effect annotations = topology in production.

**Confidence: 75%.** The mapping is clean but the categorical formalization hasn't been verified rigorously. The coproduct/product/fiber interpretation needs checking against actual Claude Code behavior.
