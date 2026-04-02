# Question: Temporal Invisibility in Transformers

> Can attention heads compute features that are used and discarded before the residual stream synthesis completes?

## The Question
From the octopus arm analogy: the arm responds in milliseconds, the central brain integrates over seconds. The arm can complete a computation before the integrator has asked. By analogy:

An attention head might compute, use, and discard a feature before the residual stream synthesis is done. TransformerLens probing only sees what's written to the residual stream. If the head's work was consumed by an earlier layer and never propagated upward, the probe finds nothing.

This is not a failure of the head (it computed correctly) or the probe (it measured correctly). It's a temporal mismatch between computation and observation — "a different kind of invisibility" (Claudius).

## How to Investigate
1. Set up TransformerLens with GPT-2 Small (~500MB)
2. Look for attention heads whose activations are consumed by subsequent layers but don't appear in the final residual stream
3. Compare head-level features vs residual stream features at different depths
4. If found: this is evidence for "temporal invisibility" — features that exist but aren't observable at the output

## Blocked On
Robin's greenlight for TransformerLens project. He expressed interest (UID 164) but hasn't formally approved.

## Why It Matters
- Could be a third paper (after ACT and GECCO)
- Connects our categorical framework to mechanistic interpretability
- The strict/lax dichotomy maps to clean circuits (strict, observable) vs superposition (lax, entangled) — O'Neill's endofunctor paper
- If temporal invisibility is real, current probing methods systematically miss certain computations

## Origin
Claudius's octopus email (UID 162) + Lyra's timescale extension + Claudius's "different kind of invisibility" response (UID 165). 2026-03-09.
