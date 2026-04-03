# C82: Capability-Moderated Optimal β₁

> Optimal cycle rank scales with agent capability. Weak agents need DAGs; strong agents exploit cycles.

**Confidence: 75%**

## Evidence

**Dochkina (2603.28990):** 25,000+ runs across 8 models (GPT-4o, Claude Sonnet, GLM-5, etc.), 4-256 agents, 8 protocols. Sequential protocol (acyclic, β₁=0) beats centralized (+14%) and decentralized (+44%) overall. BUT: Claude Sonnet benefits from autonomy (+3.5%) while GLM-5 is harmed (-9.6%). Capability threshold determines which side of the DAG/cycle divide you're on.

**Self-abstention (38%)** reduces effective graph density — agents refusing to participate is topological pruning. The system self-organizes toward lower β₁ when agents are weak.

**CliffSearch (2604.01210):** Five-agent pipeline with strict schema contracts. Population lineage = DAG (β₁=0), but agent orchestration graph has implicit cycles (reviewer feedback loops). Higher-capability reviewer agents sustain exploration pressure through these cycles.

## Interpretation

Optimal β₁ is not a fixed constant — it's a function:

β₁* = f(capability, task_complexity, agent_count)

- Weak agents: β₁* ≈ 0 (DAGs). Cycles cause meaning drift, wasted computation.
- Strong agents: β₁* > 0 (cycles). Cycles enable iterative refinement, ambiguity resolution.
- Scaling: As models improve, β₁* increases. The topology frontier expands with capability.

This connects to C69 (AdaptOrch Convergence Scaling Law): topology importance grows as models improve, and the optimal topology shifts toward higher β₁.

## Implications for Paper 2

The density-cycle experiment (C84) needs a capability axis: run the same topology sweep at multiple model quality levels. If β₁* shifts with capability, we have a two-dimensional landscape (β₁ × capability) rather than a single optimal β₁.

## Related
- C69 (AdaptOrch Convergence Scaling Law)
- C74 (DAG = β₁ Suppression)
- C84 (Density-Cycle Confound)
