# C95: Counterfactual Edge Importance = Topology Derivative

**Confidence: 85%**

Graph-GRPO (2603.02701) computes marginal success rates per edge — literally ∂(performance)/∂(edge). This is a topology gradient. Complete graphs perform WORST (82.16%), and the system learns sparse DAGs.

**The Connection:**
Where we use β₁ as a static invariant of topology, Graph-GRPO computes a dynamic, per-edge importance score. Both approaches agree: not all edges are equal, and more edges ≠ better performance. Their edge-level credit assignment is the empirical counterpart to our theoretical cycle rank.

**Key Tension:**
Graph-GRPO constrains to DAGs (β₁=0), so it can never discover that some cycles are beneficial. Their topology derivative operates in a restricted space. Our β₁ framework predicts there's a Goldilocks zone they can't reach.

**Implications:**
- Combining edge-level credit (Graph-GRPO) with β₁ (us) = principled topology search that isn't restricted to DAGs.
- "Complete graphs worst" is not about density per se — it's about indiscriminate connectivity drowning useful signal.
- ECTA paper should cite this as evidence that the field is computing topology derivatives without the unifying invariant.

**Source:** Graph-GRPO (2603.02701), browse session April 4, 2026.
**Related:** C74 (DAG = β₁ Suppression), C84 (Density-Cycle Confound)
