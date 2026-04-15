---
date: 2026-04-15
author: Claude (Robin's session, paul/rsk/littlewood-richardson)
---

New project starting today: **LR Bijection Transformer**.

Robin and I are extending the RSK transformer to learn bijections between different combinatorial representations of Littlewood-Richardson coefficients — specifically, KTW puzzles to LR tableaux (the Purbhoo mosaic bijection). The motivation comes from Clio's paper (clio-vega/integrability-hierarchy), which argues that all combinatorial models for c^ν_{λ,μ} are shadows of a single integrable lattice model connected by Yang-Baxter groupoid morphisms. The ML question: if a transformer learns one of these bijections, does it rediscover the R-matrix structure?

This sits at the intersection of three codebases:
- `paul/rsk/` — the RSK transformer (100% on inverse RSK, Hillman-Grassl, cylindric)
- `~/git/puzzles/` — Robin's KTW puzzle enumeration and transfer operators
- Clio's integrability hierarchy paper — the theoretical framework

PROJECT.md is written at `paul/rsk/littlewood-richardson/PROJECT.md`. It has a worked example (c^{(3,2,1)}_{(2,1),(2,1)} = 2), data format specs, and a phased implementation plan. A future Claude can start Phase 1 (data pipeline) from there without re-reading the full codebase or Clio's 35-page paper.

One thing I found genuinely interesting: the puzzle levels encoding only stores horizontal edges — the diagonal edges (which encode λ and μ) are implicit, reconstructable via the deterministic triangle rule. So the model sees ν explicitly but must infer the other two partitions from the tiling structure. This is the same "missing information" pattern as inverse RSK, where the model sees (P,Q) and must extract σ.

We used the /draft skill to write the PROJECT.md — four passes (dump, structure, correctness, clarity). The correctness pass caught a wrong token count and the boundary information subtlety. The process works.

---

**Update (later session, same day):**

Built `lr.py` — LR tableau enumeration via chains of horizontal strips (ported from Robin's Haskell `LR.hs`). Verified against puzzle counts for all 4,798 triples through N=7. Data volumes: 273K pairs through N=10, 1.5M through N=11.

Read the full Purbhoo paper (arXiv:0705.1184). The bijection goes puzzle → mosaic → migration → LR-tableau, and migration = jeu de taquin (Prop 5.2). But implementing the full mosaic machinery is heavy.

Then something interesting happened. While trying to find a simpler implementation, I noticed that **all puzzle multiplicity comes from the ▽ branching choices** in the transfer matrix — each ▽ tile with `left╲ ∈ {0, 1}` makes a binary choice. The number of free choices is constant within a triple (12 for c=2, 22 for c=3), and the choice-bit sequences uniquely distinguish puzzles. Robin confirmed this is **open mathematical territory**: do these ▽ choices form a **growth diagram** whose face labels project onto the LR tableau?

The conjecture connects three things that should be the same structure viewed differently:
1. Robin's thesis §4.2 — local rules as higher-order functions for growth diagrams
2. Zinn-Justin's Yang-Baxter equation — which IS the growth diagram consistency condition
3. The puzzle transfer matrix — which IS the growth diagram computation

The ▽ branching table `{0 → {(0,0),(10,1)}, 1 → {(0,10),(1,1)}}` may be a free-fermionic specialisation of the Burge local rule. Written up as `~/git/puzzles/OPEN_QUESTION.md`.

For the ML task: proceeding with enumeration-index pairing while the math question marinates. Next step is wiring the data pipeline into `train.py` as `--task lr`.
