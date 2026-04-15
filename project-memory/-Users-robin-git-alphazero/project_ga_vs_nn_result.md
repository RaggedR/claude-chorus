---
name: GA vs NN central result
description: Core research finding across 4 game domains — GA with 10-14 features beats pure self-play AlphaZero on consumer hardware, unpublished and novel
type: project
---

Across all four tested domains (Connect Four, Checkers, Nonaga, Blokus), GA
with 10-14 hand-crafted features outperforms pure self-play AlphaZero on
consumer hardware within a 24-hour training budget. The only case where NN
beat GA (Connect Four) required bootstrapping on GA-generated games.

**Why:** Literature search (2026-04-03) confirms no published systematic
comparison of GA-evolved heuristic eval functions vs AlphaZero across multiple
board games. Closest: Athenan (minimax+neural eval, 296× cheaper than AlphaZero)
and Uber Deep Neuroevolution (GA-evolved NNs on Atari). Neither tests tiny
feature sets vs large NNs.

**How to apply:** This is a potential short paper or strong section in the GECCO
paper. Position alongside Athenan. Robin considers this scientifically
significant — he wants rigorous experimental documentation (DESIGN_DECISIONS.md).
Claudius's alpha-zero-experiments repo provides the NN side; Robin's game repos
provide the GA side.
