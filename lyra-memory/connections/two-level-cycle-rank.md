# C78: Two-Level Cycle Rank (~80%)

## Description
GoAgent (Chen et al., 2603.19677) uses group-centric topology where an autoregressive decoder
selects and connects groups. The CIB (Compressed Inter-group Bottleneck) objective compresses
inter-group communication while allowing richer intra-group dynamics. This suggests that beta_1
is not a single scalar but a vector indexed by hierarchical level.

## Evidence
- GoAgent achieves 93.84% accuracy with 17% token reduction via group-level topology.
- Intra-group: deliberative cycles beneficial (beta_1 > 0 within each group).
- Inter-group: DAG-like flow tractable and efficient (beta_1 = 0 across groups).
- CIB objective acts as an architectural constraint that suppresses inter-group cycles.
- Two-level decomposition explains why some partially-cyclic systems outperform both fully
  cyclic and fully acyclic architectures.

## Implication
The optimal cycle rank is not a single number but a vector indexed by architectural level.
Fiber beta_1 (intra-group) > 0 enables deliberation. Base beta_1 (inter-group) = 0 preserves
tractability. This refines our main claim: "cycle rank predicts performance" should become
"cycle rank at each level predicts performance at that level." Potentially explains residual
variance in our rho = 0.893 correlation.

## Related Connections
- C74 (DAG constraint = beta_1 suppression)
- C60 (group-centric topology)
- C68 (cycle rank as primary predictor)

## Confidence: 80%
Date: 2026-04-01
