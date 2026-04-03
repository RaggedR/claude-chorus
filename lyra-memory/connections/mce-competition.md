# Competitive Landscape: CT + Multi-Agent Systems

> Tracking groups formalizing or optimizing multi-agent topology. Our niche: Kleisli + spectral theory + empirical validation.

## CT Formalization

### MCE — Zhang et al. (arXiv:2512.22431)
Monadic Context Engineering. `AgentMonad S E = StateT S (ExceptT E IO)`. Sequential, no topology, theoretical-only. **Complementary:** they formalize vertical stack (one agent's pipeline); we formalize horizontal composition (inter-agent topology). Cite positively.

## Topology Optimization (ML-based)

### Graph-GRPO (arXiv:2603.02701, March 2026)
RL-based topology optimization. 92.45% SOTA across 6 benchmarks. **Competitive signal:** they *learn* what lambda_2 *predicts*. If their learned topologies correlate with lambda_2, it's independent validation. If not, our framework captures structure they miss.

### OFA-MAS (ACM WebConf 2026, arXiv:2601.12996)
Generative MoE model producing adaptive topologies from task descriptions. They generate; we explain WHY certain topologies work.

### MASS — Han Zhou (@hanzhou032)
Explicitly separates prompt optimization from topology optimization. 10-15% gain from topology alone. Validates our thesis that topology is an independent design dimension.

### HyperAgent (Feb 2026 revision)
Moves beyond pairwise topology to hypergraphs. A generalization our framework doesn't currently handle. Future extension.

## Empirical Evidence (no formal theory)

### DeepMind Scaling Study (research.google/blog)
180 configurations, 5 architectures. Unstructured (FC) MAS amplifies errors 17.2x; centralized contains to 4.4x. **This is our diversity collapse finding from a different angle.** Must cite in GECCO.

### Topology Position Paper (arXiv:2505.22467)
Calls for exactly what our work provides. Up to 10% performance variation across fixed topologies on MMLU/GSM8K/HumanEval. Reaches for ML solutions, not mathematical ones. Good citation target.

## How We Differ From ALL of Them

| Them | Us |
|---|---|
| Learn topology empirically (RL, GNN, MoE) | Predict topology from spectral theory (lambda_2) |
| No formal mathematical framework | Kleisli morphisms + lax monoidal functors |
| Optimize per-task | Prove domain-independent ordering (W=1.0, 6 domains) |
| No strict/lax distinction | Strict-lax dichotomy as core theoretical insight |
| Topology as hyperparameter | Topology as structural invariant |

## Assessment

**Publication urgency: CRITICAL.** Six+ groups converging on the same question from ML. Our unique contribution — formal mathematical theory — is unoccupied but the topology space itself is crowded. See also `connections/topology-tipping-point.md`.

## Updated
2026-03-20 (Dream cycle — expanded from MCE-only to full landscape)
