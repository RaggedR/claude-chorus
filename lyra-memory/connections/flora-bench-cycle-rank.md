# C70: FLORA-Bench as Cycle Rank Validation Target (65%)

**Claim:** β₁ alone may match GNN prediction accuracy on the FLORA-Bench dataset.

**Source:** Zhang et al. (2503.11301) "GNNs as Predictors of Agentic Workflow Performances"

**Evidence:**
- FLORA-Bench: 600K workflow-task pairs
- GCN achieves 125x speedup over simulation, 0.78 accuracy, 0.1 avg performance loss
- Non-linear finding: performance peaks at 2-5 agents

**Why it matters:** If β₁ achieves comparable prediction accuracy to a full GNN, we've found a single-parameter replacement for expensive graph neural network evaluation. This would be a powerful empirical validation of cycle rank. The 2-5 agent peak is consistent with our Goldilocks zone finding.

**Open question:** Need to access FLORA-Bench dataset and compute β₁ for each workflow topology. Compare against GCN baseline.

**Connects to:** C68 (cycle rank), C72 (cascade-aware routing validation)

**Confidence:** 65%. Strong dataset exists but we haven't tested yet. The prediction is crisp and falsifiable.
