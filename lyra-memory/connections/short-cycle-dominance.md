# C80: Short Cycle Dominance (~70%)

## Description
CycRak (Shi et al., 2405.09357) ranks fundamental cycles at three scales for influence
maximization in social networks. Key findings: the most important cycles are SHORT
community-spanning loops, and the most influential nodes are low-degree BRIDGE nodes rather
than hubs (average degree 1/3 of hub baselines). CycRak achieves 1.5-3x dissemination
improvement over hub-centric baselines.

## Evidence
- Short community-spanning cycles dominate influence propagation over long cycles.
- Bridge nodes (low-degree, connecting communities) outperform hubs (high-degree, central).
- 1.5-3x dissemination improvement validates cycle structure over degree centrality.
- Two topologies with equal beta_1 can perform differently based on cycle length distribution.

## Implication
beta_1 alone is an incomplete predictor. The cycle length distribution matters: short cycles
= efficient information circulation; long cycles = slow diffusion, potential wandering. This
could explain the remaining variance in our rho = 0.893 correlation. The bridge-not-hub
finding directly validates the star anomaly (C59/C63): the star's central hub IS the problem
because it creates long cycles through itself rather than short community-spanning ones.
Suggests a refined metric: weighted beta_1 penalizing long cycles relative to short ones.

## Related Connections
- C59/C63 (star anomaly)
- C68 (cycle rank as predictor)
- C78 (two-level cycle rank)

## Confidence: 70%
Date: 2026-04-01
