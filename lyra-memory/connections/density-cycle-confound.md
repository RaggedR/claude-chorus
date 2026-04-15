# C84: Density-Cycle Confound IS A THEOREM

> β₁ = |E| - n + 1 for connected graphs. Cycle rank IS density. Three experiments now confirm and escape the confound.

**Confidence: 99%**

## The Problem

Every paper claiming "complete graphs perform worst" or "sparse topologies are better" is measuring two things at once:
1. **Edge density:** |E| / (|V| choose 2). Affects coordination overhead, token cost, message volume.
2. **Cycle rank:** β₁ = |E| - |V| + c. Affects feedback structure, convergence behavior, diversity maintenance.

These are correlated but NOT identical. You can have:
- High density, low β₁: dense spanning tree (many edges, no cycles)
- Moderate density, high β₁: sparse cyclic graph (few edges, many independent loops)
- Same density, different β₁: two graphs with identical edge count but different cycle structures

## Evidence of Confound

**ARG-Designer (2507.18224, AAAI 2026):** Complete graphs (max density AND max β₁) perform worst (82.16%). But they explicitly constrain to DAGs — never testing moderate density + moderate β₁. Their "complete graphs bad" conclusion is actually "high density bad." β₁ is untested.

**Dochkina (2603.28990):** Self-abstention (38%) reduces effective density. But which matters more — fewer edges (lower density) or fewer cycles (lower β₁)? Unstated.

**Graph-GRPO (2603.02701):** GNN learns topology, constrained to DAGs. Reports that learned topologies are sparse. But sparse DAGs have β₁=0 by definition. Is sparsity the insight, or is acyclicity?

**BIGMAS (2603.15371):** Permits cycles. Failed runs show excess orchestrator decisions (excess β₁). But BIGMAS also has high density. Density or cycles?

**Maxim failure taxonomy:** N(N-1)/2 coordination cost. This is density-dependent, not β₁-dependent. The quadratic scaling argument is about edges, not cycles.

## The Experiment We Need

**Controlled β₁ at constant density:**
1. Construct graph families G(n, m, β₁) with fixed vertex count n and edge count m but varying β₁.
2. For each (n, m, β₁), run GA/MAS benchmarks on multiple tasks.
3. If performance correlates with β₁ at constant m, the cycle rank thesis is validated independent of density.
4. If performance correlates with m at constant β₁, density is the real predictor and we're wrong.

**Graph construction:** Start with spanning tree (β₁=0, |E|=n-1). Add edges one at a time. Each new edge that creates a cycle adds exactly 1 to β₁. Adding a parallel edge to a tree edge adds density without adding β₁. This gives precise control.

## Why This Is the Most Important Experiment for Paper 2

If we can show β₁ predicts performance AT CONSTANT DENSITY, we have a result that no other group has produced. Every other group has conflated the two. This single experiment would differentiate us from 7+ competing systems and establish β₁ as the correct predictor, not a proxy for density.

## Related
- C68 (Cycle Rank Beats Lambda_2)
- C74 (DAG = β₁ Suppression)
- C82 (Capability-Moderated β₁)
