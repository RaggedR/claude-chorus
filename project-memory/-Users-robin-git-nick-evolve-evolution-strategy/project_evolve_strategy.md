---
name: evolve-evolution-strategy project state
description: Nick+Robin project evolving migration graphs on deceptive landscapes — key findings and repo location
type: project
---

Nick suggested "evolve the evolution strategy" — make the migration graph itself evolvable. Project lives at ~/git/nick/evolve-evolution-strategy/, repo at RaggedR/evolve-evolution-strategy.

**Why:** Robin's ACT 2026 paper showed topology determines diversity (W=1.0) across 6 honest domains. This project tests deceptive domains and evolves the graph.

**Key findings (2026-04-06):**
- Diversity ordering is universal (structural invariant via λ₂) — holds on all deceptive domains
- Fitness ordering is problem-dependent — five deceptive domains produce four distinct fitness orderings
- Evolved graphs converge to a consistent **triangle+pendant motif**: ~6 edges at n=5, moderate λ₂, asymmetric degrees, pendant vertex as diversity reservoir
- Evolved graphs beat canonical topologies on traps and HIFF, tie on MMDP, slightly lose on overlapping traps

**How to apply:** This is an active research project. The next steps are in EVOLVED_GRAPHS.md open questions: scaling to larger n, testing honest landscapes, richer graph genomes (directed/weighted), more inner seeds for noisy fitness.
