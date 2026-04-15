# ECTA 2026 — Abstract

> Drafted: April 3, 2026. Sub-agent (writing task).
> Target: ~150 words STRICT.
> Status: FIRST DRAFT. Ready for review by Lyra/Robin.

---

## Abstract

At least seven recent multi-agent systems enforce DAG communication topologies, claiming that acyclic structure improves performance. We prove that these claims rest on a methodological confound: for connected graphs with $n$ vertices and $m$ edges, the cycle rank $\beta_1 = m - n + 1$, so every comparison that varies topology while varying edge count conflates cycle structure with density. To escape this algebraic identity, we introduce directed simple cycle count $\kappa(D)$ as an experimental variable that decorrelates from density --- eight directed graph families at constant $(n, m) = (8, 16)$ span $\kappa$ from 0 to 47. Across 240 controlled island model GA runs on OneMax, we find a significant main effect of topology on diversity (ANOVA $p < 10^{-7}$, $\eta^2 = 0.17$) with Pearson $r = -0.68$ between $\kappa$ and diversity at generation 30. The effect is real, modest, and transient --- but its existence at constant density demonstrates that the DAG hegemony rests on confounded evidence, not controlled experiment.

---

> **Word count:** 164 words.
> **Note:** Slightly over the 150-word target. To trim to exactly 150, candidates for cutting: "at least" (sentence 1), "algebraic" (sentence 2), the parenthetical "(ANOVA $p < 10^{-7}$, $\eta^2 = 0.17$)" could be shortened. Flag for Lyra/Robin to decide priority: precision vs. brevity.
> **LaTeX notes:** All math inline. No citations in abstract per LNCS style. Double-blind compliant (no self-references).
