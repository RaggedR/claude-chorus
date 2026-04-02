---
name: Dirichlet noise bug fix
description: MCTS Dirichlet noise was applied AFTER search instead of BEFORE — caused value head inversion and training regression
type: feedback
---

Dirichlet noise must be injected into root node child priors BEFORE the MCTS simulation loop, not applied to the output visit distribution after search.

**Why:** The standard AlphaZero approach adds Dir(α) noise to the root's policy priors so the search tree actually explores diverse branches. Our original code ran MCTS with clean priors (deterministic search), then randomly perturbed the visit counts afterwards. This meant: (1) the search never explored alternative branches, (2) policy targets were corrupted with random noise unrelated to search quality, (3) the value head trained on poorly-explored positions and developed inverted estimates.

**How to apply:** The fix is in `mcts.py` — `search()` accepts `dirichlet_alpha` and `dirichlet_eps` params. `self_play.py` and `league.py` pass `dirichlet_alpha=0.75, dirichlet_eps=0.25` to `get_action_probs()`. At play-time (arena, evaluation), do NOT pass noise — it's only for training data generation.

**Diagnostic command:** Check value head calibration by running the network on a winning position (P1 has 3-in-a-row, col 3 wins) and a must-block position (P2 has 3-in-a-row, P1 must play col 3). Winning should be > +0.5, must-block should be < 0. If inverted, training data quality is the issue.
