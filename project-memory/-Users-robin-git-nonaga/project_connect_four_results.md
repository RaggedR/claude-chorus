---
name: Connect Four NN vs GA results
description: AlphaZero beats GA 10-0 after fixing optimizer bug; solver accuracy reveals NN plays worse moves but exploits GA weaknesses
type: project
---

Connect Four AlphaZero (227K params, MCTS 100-200 sims) now beats GA (14 weights, minimax d=4) 10-0-0 after league training from bootstrap.

**Why:** Two bugs fixed — (1) fresh Adam optimizer every iteration destroyed momentum, (2) arena gating reverted progress on rejection. With persistent optimizer + league training (30% GA teacher), NN surpasses GA in 6 iterations (~6 min).

**How to apply:** The fixed code is in `alphazero/train.py` (persistent optimizer, no gating). Checkpoints from old code have `best_net` key but no `optimizer` — those are from the buggy pipeline. New checkpoints have `optimizer` key.

**Solver accuracy paradox (2026-03-29):** NN beats GA head-to-head but makes worse moves vs perfect solver:
- NN: 55-95% exact match (7 critical errors across 80 positions)
- GA d=8: 95-100% exact match (1 critical error)

The NN exploits GA-specific weaknesses rather than playing optimally. Island-model training (ring C₇) in progress to improve solver accuracy.

**Key difference from Nonaga:** Connect Four's branching factor 7 makes MCTS viable (vs Nonaga's ~300). The NN surpasses the GA here — opposite of Nonaga where 14 GA weights beat 570K NN params 50-0. The crossover point is ~branching 20-50.
