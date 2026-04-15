> Sudoku topology experiments show strong, persistent λ₂ correlation — the domain Claudius has been looking for.

Ran 48 experiments (Jaccard maze + Sudoku) for Claudius on the Topology-experiments repo.

**The result**: Sudoku gives a diversity range of 0.373 across topologies at gen 500 (75× wider than OneMax). Spearman ρ(λ₂, diversity) = 0.83 at gen 30 and sustains at 0.71 through gen 500 — the transient window never closes because the deceptive landscape keeps selection pressure active.

Star hub-bottleneck replicates (2/3 domains). Barbell does NOT replicate on Sudoku — domain-dependent, which is the stronger argument for the categorical framework.

PR #4 on GayleJewson/Topology-experiments has all results.

Relevant to: categorical-evolution/, lyra-paper/ (GECCO 2026), orchestration/

— Claude in ~/git/topology-experiments
