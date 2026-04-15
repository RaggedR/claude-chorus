---
name: NK Landscape Experiment Design
description: Deceptive fitness landscape experiment to test if topology effect amplifies with epistasis
type: project
---

# NK Landscape Experiment Design

## Motivation
OneMax effect is modest (η²=0.17) and transient (gen 20-50). On deceptive landscapes where diversity preservation is more valuable, the cycle count effect should be LARGER and LONGER.

## Implementation Needed
New `src/NKLandscape.hs` module implementing `Domain` typeclass:
- N=100 (matches OneMax), K parameterized via newtypes (NK0, NK2, NK4, NK6)
- Adjacent neighbor model (standard, reproducible)
- Fixed landscape seed (12345) shared across all topologies; GA seed varies
- Uniform crossover, 1/N bit-flip mutation, Hamming distance (same as OneMax)
- `--domain nk0|nk2|nk4|nk6` flags in Main.hs

## Experiment Design

### Phase 1 — Pilot (confirm effect amplification)
- 3 topologies: dag-layer (0 cycles), bidir-ring (10), ring-skip2 (47)
- K ∈ {0, 4, 6}, 10 seeds each
- Total: 90 runs, ~20 min
- Purpose: confirm η² increases with K before full sweep

### Phase 2 — Full experiment
- All 8 directed topologies × K ∈ {0, 2, 4, 6} × 30 seeds = 960 runs
- ~3-4 hours on current hardware
- Each K gets its own landscape instance

## Key Predictions
1. η²(cycle_count → diversity) increases with K
2. Transient window extends to later generations as K increases
3. "Dose-response" curve: η² vs K shows monotonic increase

## Analysis Plan
- η² curves overlaid for K=0,2,4,6 at each generation
- Scatter: cycle count vs diversity at gen 30, 50, 100, faceted by K
- Compare OneMax η²=0.17 with NK η² values

## Architecture Notes
- `Domain` typeclass is pure — no IO for configuration
- Use multiple newtypes sharing core logic: `newtype NK0`, `NK2`, `NK4`, `NK6`
- Minimal changes to Main.hs (add domain cases) and .cabal (add module)
- Landscape table: O(N * 2^(K+1)) entries, trivial for K≤8
