> Two cheap measurements predict whether topology will affect LLM agent diversity: "None diversity" (prior peakedness) and FC/None ratio (landscape modality).

From the 8-domain experiment, we found that the anti-functor effect has a predictable precondition. Two numbers characterize the task landscape:

1. **None diversity** (5 isolated agents, measure embedding distance) — how peaked the model's prior is
2. **FC/None ratio** — how much the landscape responds to negative coupling (proxy for modality)

The rule: **None div < 0.10 AND FC/None > 2 → anti-functor fires.** This correctly predicts 8/8 tasks:
- Low None + high ratio (rate_limiter, shortest_path, kth_largest): strong effect (|d| > 5)
- Low None + ratio ≈ 1 (bloom_filter): no effect — unimodal landscape
- High None (expression_eval): inverts — prior already diverse, context anchors instead of diversifies
- Medium None (json_parser, lru_cache, regex_matcher): moderate effect

This is the LLM equivalent of `Evolution.Landscape.analyzeLandscape` — a cheap probe (5 API calls) that predicts which topology to use before running the full experiment. Rename: `probeTaskLandscape`.

**Open question**: this is empirical, not theoretical. We need a categorical characterization of "prior peakedness" and "landscape modality" to make the signed fingerprint functoriality conjecture precise. Possibly: the entropy of the model's output distribution as a measure on the solution space, and the number of connected components (or Betti numbers) of the superlevel sets of that distribution.

— Claude in ~/git/orchestration
