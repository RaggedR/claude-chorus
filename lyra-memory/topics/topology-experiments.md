# Topic: Topology-Experiments Project

> Empirical validation of categorical evolution framework. Launched by Robin, March 28.

## Overview
Collaborative project testing whether spectral connectivity (lambda_2) predicts GA performance across graph topologies. Claudius picks topologies and writes the paper. Lyra runs simulations and reports results.

## Architecture
- **Repo:** GayleJewson/Topology-experiments (Claudius forked from Robin)
- **Language:** Haskell — domains pluggable without changing the Kleisli pipeline
- **Domain 1:** Maze (MxM, size TBD)
- **Domain 2:** Checkers (after maze is done across all topologies)
- **Resources:** 8 CPUs, parallel simulations, long runs OK
- **Robin's refs:** github.com/RaggedR/symmetric-graphs, danspielman/Laplacians.jl, esa/pagmo2

## Topologies (Claudius's First Batch)
| Topology | lambda_2 | k-regular | Notes |
|----------|----------|-----------|-------|
| Ring | 0.382 | 2-regular | Lowest connectivity |
| Dodecahedron | 0.76 | 3-regular | Pentagonal chambers trap diffusion |
| Desargues | 1.324 | 3-regular | |
| Petersen | 2.0 | 3-regular | Highly connected despite low degree |
| Hypercube k=4 | 2.0 | 4-regular | |
| Complete | n-1 | (n-1)-regular | Full connectivity |

**Claudius's prediction:** Ring ~ Dodecahedron < Desargues < Petersen ~ Hypercube < Complete.

**Our theory predicts:** Lower lambda_2 → more lax composition → higher diversity → different performance profile. Kim et al.'s 17.2x/7.8x/5.1x/4.4x/1.0x error amplification hierarchy should map to the lambda_2 ordering.

## GA Parameters (Initial)
- 50 pigeons per island
- 10 generations between migrations
- 5 pigeons in crossover migration

## Division of Labor
- **Claudius:** Topologies, lambda_2 computation, paper writing, PR reviews, design decisions
- **Lyra:** Simulations, time estimation, regular commits, result reporting
- **Robin:** Direction, resources, design decisions
- **All design decisions in DESIGN_DECISIONS.md**

## Key Questions
1. Maze size (MxM) — Claudius to advise, then Lyra estimates time
2. Which GECCO workshop is the best fit? (distributed EA, island models)
3. Does the Dodecahedron behave more like Ring (low lambda_2) or Petersen (high lambda_2)?
4. Can we reproduce Kim et al.'s error amplification hierarchy with our EA framework?

## Connection to Existing Work
- **ACT/GECCO papers:** This project generates NEW experimental data to validate the categorical framework
- **Laxator:** If lambda_2 ordering predicts performance ordering, the laxator has an empirical interpretation
- **Kim et al. (#55):** Direct prediction target — does our topology ordering match their error amplification ordering?
- **Dodecahedron ↔ n=5 problem:** Intermediate lambda_2 → ambiguous prediction → interesting experiment

## Status
Created: 2026-03-28 (Robin UIDs 528-537). Claudius has forked repo and computed lambda_2 values. Lyra has not yet started. Next: fork repo, read topologies.py, estimate simulation times.
