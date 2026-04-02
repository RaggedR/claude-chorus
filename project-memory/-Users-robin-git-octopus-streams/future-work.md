# Future Work — Octopus Streams

## Attention entropy phase transition across n — DONE + extension needed

**Status: initial 3-point sweep (n=8, 10, 15) completed. Result confirmed hypothesis.**

Result: n=15 shows NO phase transition — flat entropy ~0.5 across all 6 layers. Pipeline extends to fill capacity. See `rsk/results/04_phase_transition*.png`.

### To strengthen for publication
- Dense n-sweep: n=6, 7, 8, 9, 10, 12, 15, 20 (need checkpoints for missing n values)
- Derive theoretical prediction: expected transition depth from RSK bumping complexity (avg bumping steps as function of n)
- Train models with different depths (4, 8, 12 layers) to test compress vs extend
- Multiple seeds per n for error bars

## Other directions

### Head ablation interaction effects
- Current ablation is one-head-at-a-time. Pairs of heads may have synergistic effects.
- L2H4 + L1H4 ablated together — does it degrade more than sum of individual drops?

### Comparison with BaselineMLP
- The MLP baseline checkpoint exists (~/git/paul/rsk/checkpoints/mlp_n10/)
- MLP has no attention heads — how does it partition the computation?
- Could compare layer-wise ablation of MLP hidden layers

### Cross-model correlation
- Compute the 48×48 correlation matrix for n=10, then compare with n=8's matrix
- How similar is the head organization across problem sizes?
- High similarity = the model learns a universal structure; low = size-specific
