---
name: Jaccard maze phenotype fix
description: db449ea replaced Hamming with Jaccard on spanning-tree edge sets — dropped diversity floor from 0.997 to 0.631
type: project
---

Commit db449ea (2026-04-04) fixed the maze diversity metric. Old Hamming distance on 420-element edge permutations gave near-maximal diversity (~0.997) regardless of topology — a floor effect that masked all topology signal.

The Jaccard fix decodes each maze into its spanning tree edge set via Kruskal, then computes 1 - |intersection|/|union|. Two structurally similar mazes share most edges → near 0. Tradeoff: adds a Kruskal pass per diversity evaluation (~2× cost).

**Why:** Without this fix, the maze domain is useless for topology experiments. With it, the diversity floor drops to ~0.63, giving room for topology-dependent separation.

**How to apply:** All maze experiments from 2026-04-04 onward use Jaccard. Prior pilot results (pilot_maze_15x15, pilot_maze_8x8) used Hamming and showed null results — don't compare directly.
