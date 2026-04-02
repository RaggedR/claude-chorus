---
name: Connect Four project status
description: State of the project as of 2026-03-28 — AlphaZero retraining in progress after Dirichlet bug fix, GA at smoke-test quality
type: project
---

## Status as of 2026-03-28

**AlphaZero**: Retraining in progress (another Claude instance is running it). The Dirichlet noise bug was the main issue — see dirichlet_bug.md. Pre-fix, GA beat AZ 40-0. Checkpoint progression showed value head inversion at iter 10 (winning positions scored -0.64, losing scored +0.98). The training loop was also overhauled by Robin: persistent optimizer, no arena gating, gradient clipping, larger batch (256), smaller buffer (20K), temperature threshold raised to 15.

**GA**: Trained with smoke-test config only (2 islands, pop 6, 2 gens, depth 2). Real training (7-island C₇ ring, 200 gens, ~12.5h) hasn't run yet. Even the smoke-test GA achieved 95% solver accuracy at depth 4 and beat AZ 40-0.

**What's built**: Game engine (19 tests), AlphaZero full pipeline, GA full pipeline, arena.py, solver.py
**What's NOT built**: sae/, sae_ga/, export.py, index.html

**Why:** The goal is to compare three approaches: hand-crafted features (GA) vs learned features (AZ) vs extracted features (SAE-GA). The hypothesis is SAE-GA > AZ > GA in playing strength.

**How to apply:** After retraining completes, run `python arena.py --accuracy` to evaluate. If AZ still loses to GA, investigate the value head calibration first (the diagnostic in the 2026-03-28 session showed exactly how to check this). The network architecture is verified to learn correctly from clean data.
