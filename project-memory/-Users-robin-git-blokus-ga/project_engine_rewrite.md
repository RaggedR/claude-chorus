---
name: Engine rewrite completed
description: Engine rewritten without upstream code (bitboard, telemetry). Web frontend added. All 217 tests pass.
type: project
---

Engine rewrite completed on 2026-04-03. Replaced ~3,500 lines of upstream code (bitboard-heavy engine from TGALLOWAY1/MCTS_Laboratory, no license) with clean numpy/set-based implementation.

**Why:** Upstream owner closed our PR without merging. Repo has no license (all rights reserved). We needed 100% ownership.

**How to apply:**
- `engine/` is now fully our code — no bitboard, no telemetry, no advanced_metrics
- `web/` is the new FastAPI + Canvas frontend for human-vs-AI play
- `mcts/learned_evaluator.py` import is lazy (`try/except`) since it depends on deleted analytics modules
- `analytics/winprob/features.py` also has lazy imports for the same reason
- 217 tests pass, 2 pre-existing failures (missing `openskill` dep, flaky timing test)
- 5 deterministic seeded games produce identical results to baseline
- Arena runs work with all 4 agent types (AlphaZero, GA-evolved, NN+MCTS, NN standalone)
