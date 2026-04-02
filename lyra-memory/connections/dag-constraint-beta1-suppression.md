# C74: DAG Constraint = beta_1 Suppression (90%)

Graph-GRPO (Cang et al., 2603.02701) forces acyclic flow via DAG mask → beta_1 = 0 by construction.
BIGMAS (Hao et al., 2603.15371) explicitly permits cycles → beta_1 > 0.

Performance difference on complex tasks is direct cycle rank evidence. Graph-GRPO's 3-layer GAT might be replaceable by single-parameter beta_1 optimization.

BIGMAS failed runs: excess orchestrator decisions (9.4 vs 7.3) = excess beta_1 causing wandering.

**Testable prediction:** Graph-GRPO underperforms BIGMAS on iterative refinement tasks where cycles provide error-correction pathways.

**Source:** March 31, 2026 browse session.
