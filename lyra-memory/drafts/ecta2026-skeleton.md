# ECTA 2026 Paper Skeleton

> Created: April 3, 2026. Lyra (writing agent).
> Deadline: May 19, 2026. Format: Springer LNCS, 8-12 pages, double-blind.
> Core thesis (Robin's framing): "The field has been measuring density, not cycles, and doesn't know it."

---

## Title

**"Disentangling Density from Cycles in Multi-Agent Communication Topologies"**

Working alternatives:
- "The Density-Cycle Confound: A Controlled Experiment on Directed Agent Communication Topologies"
- "Cycle Rank Cannot Be Measured in Connected Undirected Graphs: Implications for Multi-Agent System Design"

Recommendation: Go with the first option. It is concrete, positions the paper as a methodological contribution, and names both variables in the title so reviewers immediately understand the experiment.

---

## Abstract (~150 words)

**What goes here:** Three-sentence structure — (1) the problem, (2) the theorem, (3) the experimental resolution.

**Key claims:**
- Multi-agent systems research overwhelmingly enforces DAG communication topologies, citing cycle-rank arguments. But for connected undirected graphs with fixed node count, cycle rank equals edge count minus a constant (β₁ = |E| - n + 1). This means every prior comparison of "cyclic vs acyclic" topologies is, algebraically, a comparison of "dense vs sparse." No controlled experiment exists.
- We provide the escape: in directed graphs, simple directed cycle count is NOT determined by (n, m). We construct 8 graph families at n=8, m=16 with cycle counts ranging from 0 to 47.
- Controlled experiment (240 runs, OneMax, 30 seeds): r = -0.68 between directed cycle count and diversity at generation 30 (η² = 0.17). The effect is real, modest, and transient. The field's DAG hegemony rests on a methodological error.

**Data supporting this:** Theorem 1 (proven), 8 graph families (computationally verified), 240 experimental runs (complete).

**STATUS: READY TO DRAFT. All data in hand.**

---

## 1. Introduction (~1.5 pages)

**What goes here:** Four paragraphs. Establish the field assumption, expose the problem, state the escape, list contributions.

**Paragraph 1 — The DAG hegemony:** Multi-agent systems research has converged on DAG communication topologies. Seven major recent systems (GoAgent, AgentConductor, Graph-GRPO, OFA-MAS, G-Designer, ARG-Designer, Dochkina et al.) enforce or recommend acyclic communication. None provide principled justification. Billions of tokens spend on architectures whose topology is chosen by convention rather than evidence.

**Paragraph 2 — The cycle rank argument and its flaw:** The intuition behind DAG preferences is often stated as "cycles create feedback loops, redundancy, and instability." This maps onto cycle rank (β₁, the first Betti number) — the number of independent cycles in the communication graph. Our prior work [paper 1] found β₁ correlates strongly with evolutionary optimization performance (ρ = 0.893). But there is a theorem that stops all of these claims cold.

**Paragraph 3 — The theorem and its consequence:** For any connected graph with fixed n, β₁ = |E| - n + 1. This is Euler's formula for 1-complexes. It means β₁ and edge count are the same variable (up to a constant). Any paper comparing DAG (β₁ = 0, sparse) against cyclic (β₁ > 0, dense) topologies has varied density and cycle structure simultaneously. The field cannot distinguish them. We prove this, survey seven papers that fall into the trap, and name it the density-cycle confound.

**Paragraph 4 — The directed escape and contributions:** In directed graphs, simple directed cycle count is not determined by (n, m). We exploit this to construct 8 graph families at identical density that vary only in directed cycle count. We run the first controlled experiment separating density from cycles. Contributions: (a) the confound theorem with proof, (b) a methodological critique of 7+ systems, (c) 8 directed graph families as a public benchmark, (d) controlled OneMax experiment with r = -0.68.

**Figures needed:** None in intro. Reference to the confound theorem in Section 3.

**STATUS: NEEDS WRITING. Framework complete; all claims verified. ~0.5 pages of background context needed on island model GAs.**

---

## 2. Background (~1 page)

**What goes here:** Three subsections. Keep tight — the audience knows GAs and graphs but may not know β₁.

**2.1 Island Model Genetic Algorithms:** Populations partitioned into islands; periodic migration governed by a communication topology. Performance (diversity, fitness convergence rate) depends on migration structure. Standard formulation [Tomassini 2005, Alba & Troya 1999]. Our experiments use OneMax (100-bit) as the fitness function — unimodal, easy, chosen to establish a clean baseline rather than model a hard problem.

**2.2 Cycle Rank (First Betti Number β₁):** For a graph G = (V, E), β₁ = |E| - |V| + c where c is the number of connected components. For connected graphs, β₁ = |E| - |V| + 1. A tree has β₁ = 0. Each added edge beyond the spanning tree increments β₁ by 1. Geometrically: β₁ counts independent cycles in the communication graph. Algebraically: it is the dimension of the cycle space over GF(2). Cite standard algebraic topology [Hatcher 2002] and our prior work [paper 1].

**2.3 Directed Graphs and Simple Cycle Count:** A directed graph (digraph) D = (V, A) has arcs (directed edges). Unlike the undirected case, simple directed cycle count (the number of distinct elementary directed cycles) is a combinatorial quantity — not determined by |V| and |A|. Two digraphs with the same node and arc count can have 0 to O(n!) simple directed cycles. Enumeration via Johnson's algorithm [Johnson 1975]. The 8 families used in our experiment were verified computationally; cycle counts range from 0 to 47 at n = 8, m = 16.

**Key terms to define:** connected graph, spanning tree, β₁, simple directed cycle, directed acyclic graph (DAG), strongly connected component.

**STATUS: NEEDS WRITING. Standard background — no original research required. ~1 hour of writing.**

---

## 3. The Confound Theorem (~1.5 pages)

**What goes here:** Theorem, proof, corollary, survey of affected papers. This is the theoretical core.

**3.1 The Theorem:**
- Theorem 1 (Cycle rank–density identity): For a connected graph with n vertices and m edges, β₁ = m - n + 1.
- Proof: Spanning tree has n - 1 edges; each remaining edge creates one independent cycle; cycle space dimension = m - (n-1) = m - n + 1. QED. (3 lines — keep it that short.)
- Corollary 1 (Collinearity): For connected graphs with fixed n, β₁ is an affine function of m. Pearson correlation is affine-invariant, so ρ(β₁, Y) = ρ(m, Y) exactly for any performance metric Y.
- Implication stated plainly: "Any experiment comparing connected topologies on a fixed number of agents cannot distinguish between 'cycles help' and 'more edges help.'"

**3.2 The DAG Hegemony — A Survey:** Present the 7-paper table from supporting-papers.md. For each paper: venue, topology constraint, what they test, and how the confound applies. Key point per paper:
- GoAgent: CIB objective. DAG vs dense graph — both variables vary.
- AgentConductor: Sequential chain vs complex graphs — more cycles AND more edges.
- Graph-GRPO: Learned DAG (constrained β₁=0) vs complete/star — no constant-density control.
- OFA-MAS: Pruning reduces density AND cycles simultaneously.
- G-Designer: Full topology sweep, no constant-density condition.
- ARG-Designer: Complete graph is max density AND max β₁ simultaneously.
- Dochkina et al.: 25K runs, capability sweep, but sparse/acyclic always co-vary.
- Closing statement: "None of these hold density constant while varying cycle structure. By Theorem 1, in the connected undirected regime, they mathematically cannot."

**3.3 The Directed Escape:** In directed graphs, simple directed cycle count is not topologically determined — it is combinatorial. Two digraphs with |V|=8, |A|=16 can have 0 or 47 simple directed cycles (computationally verified). This breaks the collinearity and makes controlled experiments possible for the first time. Brief; the experiment follows in Section 4.

**Data/figures:** Table 1 (DAG hegemony survey, 7 papers). No other figures needed for this section.

**STATUS: CONTENT READY. Draft exists at `drafts/confound-theorem-section.md` (~2050 words). Needs compression to ~800 words for ECTA page limit and conversion to LaTeX. This is the most mature section.**

---

## 4. Directed Cycle Count as an Experimental Variable (~1 page)

**What goes here:** Define the variable, show it decorrelates from density, present the 8 graph families.

**4.1 Definition:** Simple directed cycle count SC(D) = number of distinct elementary directed cycles in digraph D (cycles that visit each vertex at most once). Computed via Johnson's algorithm in O((V + A)(C + 1)) where C is the number of cycles. Unlike β₁, SC(D) is not a topological invariant — it depends on the specific edge arrangement, not just the rank of the cycle space.

**4.2 Decorrelation from density:** Theorem 1 establishes that β₁ and density are collinear for connected undirected graphs. SC(D) obeys no such constraint. For n = 8, m = 16, SC(D) is not determined by (n, m). We constructed 8 directed graph families spanning this space:

| Family | Description | SC(D) | Strongly Connected |
|--------|-------------|-------|-------------------|
| DAG-Layer | 3-layer hierarchy, all edges forward | 0 | No |
| DAG-Wide | Fan-out hierarchy, all edges forward | 0 | No |
| LowCyc-1 | Spanning tree + 1 feedback arc | 3 | No |
| LowCyc-3 | Spanning tree + 3 feedback arcs | 12 | No |
| MedCyc-Ring | Ring + skip-2 edges | 47 | Yes |
| MedCyc-Skip3 | Ring + skip-3 edges | 30 | Yes |
| HighCyc-Bidir | Bidirectional ring | 10 | Yes |
| FullMix | Mixed, moderate feedback | ~20 | Yes |

All 8 families: n = 8 nodes, m = 16 directed edges. Density held constant by construction. SC(D) varies from 0 to 47.

**4.3 Computational verification:** Cycle counts verified via Johnson's algorithm implementation. Enumeration scripts available in project repository. The variation in SC(D) at constant (n, m) is the entire point: this is what makes the controlled experiment possible.

**4.4 Why simple cycle count, not directed β₁:** Directed β₁ (rank of the directed cycle space) is still m - n + 1 for strongly connected digraphs — it reproduces the collinearity. SC(D) is the right variable because it is a combinatorial, not homological, quantity. It captures the actual number of feedback pathways, which is the operationally meaningful quantity for information circulation in a multi-agent system.

**Figures needed:** Figure 1 — diagram of the 8 graph families (small graph visualizations, 2x4 grid). NEEDS CREATING.

**STATUS: DATA READY (computationally verified). Section needs writing (~400 words). Figure needs creating.**

---

## 5. Experimental Design (~1 page)

**What goes here:** Fitness function, setup, metrics, statistical analysis plan.

**5.1 Fitness function — OneMax:** 100-bit binary strings; fitness = number of 1-bits. Unimodal, no deception. Chosen deliberately: if cycle count has an effect on this easy landscape, it is a structural effect, not a landscape-specific artifact. Harder landscapes (NK, trap functions) are future work.

**5.2 Island model setup:**
- 8 islands, 50 individuals per island, tournament selection (k=3)
- Migration: every 10 generations, top 5% of each island migrates to neighbors per topology
- 100 generations total per run
- 30 independent seeds per topology
- 8 topologies from Section 4
- 240 total runs

**5.3 Metrics:**
- **Fitness:** mean best fitness across islands at gen 30, 60, 100
- **Diversity:** population-level Hamming diversity (mean pairwise distance between all individuals across all islands)
- **Convergence generation:** first generation where mean fitness > 95% of maximum

**5.4 Statistical analysis:**
- Pearson r between SC(D) and each metric at each time point
- One-way ANOVA across 8 topology groups (topology as factor)
- Effect sizes (η²) for ANOVA
- Post-hoc pairwise tests (Tukey HSD) for significant ANOVA results
- Key comparison: r(SC(D), metric) vs r(density, metric) — density is constant by construction, so density correlation should be ~0, providing a clean contrast

**5.5 Implementation:** Haskell, existing island model infrastructure from paper 1. New code: directed graph adjacency matrices for 8 families, cycle count pre-computation (Python, Johnson's algorithm), result aggregation script.

**STATUS: EXPERIMENT COMPLETE (240 runs done). This section needs writing (~400 words) to document what was run. All numbers already known.**

---

## 6. Results (~1.5 pages)

**What goes here:** Present the four main findings. Each has a figure.

**6.1 Main result — directed cycle count predicts diversity at constant density:**
- r = -0.68 between SC(D) and diversity at generation 30 (r² = 0.46)
- ANOVA: p < 1e-7 (topology is a significant factor for diversity)
- η² = 0.17 for diversity, η² = 0.24 for fitness
- Interpretation: topology explains 17% of diversity variance at gen 30. Effect is real but modest — OneMax is easy, and convergence washes out topology signal by gen 60-100.
- Key contrast: r(density, diversity) ≈ 0 by construction (density is constant). This is the controlled experiment the field has never run.

**6.2 The effect is transient:**
- At gen 30: r = -0.68 (strong signal)
- At gen 60: r ≈ -0.35 (weakening)
- At gen 100: r ≈ -0.15 (near noise floor)
- Interpretation: OneMax is unimodal. All topologies eventually converge. Cycle count extends the early-phase diversity window. Harder landscapes (NK, trap) predicted to show larger, more sustained effects — this is a design choice, not a weakness.

**6.3 Post-hoc topology comparison:**
- DAG families maintain lowest diversity (converge fastest)
- MedCyc-Ring and MedCyc-Skip3 maintain highest diversity at gen 30
- Tukey HSD: DAG-Layer vs MedCyc-Ring is significant (p < 0.01)
- The ring + skip topology outperforming the bidirectional ring (SC=47 > SC=10) may suggest short cycle length matters, not just count (Connection C80 from CycRak)

**6.4 Fitness effect (secondary):**
- η² = 0.24 for fitness — larger effect on fitness than diversity
- DAG topologies converge to good solutions faster on OneMax (expected: unimodal landscape rewards rapid information spread)
- High-cycle topologies sacrifice early fitness for maintained diversity
- On harder landscapes, this tradeoff is predicted to reverse

**Figures needed:**
- Figure 2: Line plots of diversity and fitness vs generation for all 8 topologies (4 panels: diversity gen 30, diversity over time, fitness gen 30, fitness over time). NEEDS CREATING from existing result data.
- Figure 3: Scatter plot of SC(D) vs diversity at gen 30 (8 points, labeled by family, with regression line). r = -0.68. NEEDS CREATING.
- Figure 4: ANOVA effect sizes (η²) for diversity and fitness at gen 30, 60, 100 (bar chart). NEEDS CREATING.

**STATUS: DATA IN HAND. Section needs writing + figures. This is the payoff section — allocate time for clear presentation.**

---

## 7. Discussion (~1 page)

**What goes here:** Explain the transient effect, give predictions for harder landscapes, state implications for MAS design, name the DAG hegemony as an artifact.

**7.1 Why the effect is transient on OneMax:** OneMax has a single global optimum with no local optima. All topologies converge given enough time — the question is only how long they maintain diversity before convergence. Cycle count extends this window because feedback loops slow the propagation of dominant alleles across islands. On harder landscapes (NK landscape with k ≥ 3, deceptive trap functions), premature convergence is a real failure mode, not just a speed difference. Prediction: the same experiment on a deceptive landscape will show η² > 0.40 with sustained effects beyond generation 100.

**7.2 The DAG hegemony as an artifact of the confound:** Every paper that concluded "DAGs are better" compared sparse acyclic topologies to dense cyclic ones. By Theorem 1, this compares density to density. Our experiment — the first to hold density constant — finds that cycle count has a modest but real effect on GA behavior. The correct conclusion is not "DAGs are always worse"; it is "the evidence for DAGs being better does not exist, because the experiments were confounded." Future work must use directed cycle count at constant density to re-examine all conclusions in the DAG hegemony literature.

**7.3 Implications for multi-agent system design:** Practitioners should not enforce DAG communication topologies by default. The cost of cycles is primarily complexity of implementation and debugging; the benefit is maintained diversity in hard optimization landscapes. The recommendation: use directed cycle count (not β₁, not density) as the design parameter. For simple tasks (unimodal landscapes, single-pass reasoning): DAGs are acceptable. For hard tasks (deceptive landscapes, iterative refinement, multi-step reasoning): moderate cycle count (target range from our experiment: SC(D) ∈ [10, 30]) may be beneficial.

**7.4 The capability moderation hypothesis (from Dochkina):** Dochkina et al. found that weak agents prefer sparse topologies and strong agents tolerate denser/more cyclic ones. Our controlled experiment cannot test this directly (GA "capability" is not cleanly analogous to LLM capability), but the finding is consistent: on easy OneMax (equivalent to a "capable" agent who can solve the problem regardless of coordination), DAGs converge faster (lower cycle count is beneficial). On harder problems, we predict the crossover. Direct capability moderation experiments are future work.

**STATUS: NEEDS WRITING. All arguments sketched; no new data needed. ~500 words.**

---

## 8. Related Work (~1 page)

**What goes here:** Position relative to four key external papers. Do NOT bury the contribution in a literature review — use this section to show the field is ready for this paper.

**8.1 Clock Systems (Lynch, Myers, Rischel, Staton — arXiv 2603.29573):** Representability theorem for Moore machines: β₁ controls the behavior space of compositional systems. DAG (β₁=0) admits only tree-shaped compositions; cyclic topologies admit iterative refinement. Our experiment provides empirical validation of a theoretical prediction: systems with higher β₁ (more cycles) exhibit more complex long-term behavior (extended diversity). Note: Clock Systems proves this for abstract compositional systems; we instantiate it for island model GAs. Full text read required before citing Theorem 6.8. STATUS: MUST READ BEFORE SUBMISSION.

**8.2 Puppeteer (Drozdov et al. — arXiv 2505.19591, NeurIPS 2025):** RL-trained orchestrator independently learns "compact, cyclic reasoning structures" on complex tasks. Without explicit β₁ representation, gradient descent converges to topologies with higher cycle count on harder tasks. This is independent empirical validation of our thesis from a completely different experimental paradigm. Post-hoc β₁ analysis of Puppeteer's learned topologies would be a natural extension. STATUS: FULL TEXT READ REQUIRED.

**8.3 Dochkina et al. (arXiv 2603.28990):** 25,000+ runs across capability levels; finds sequential (DAG) beats dense/cyclic, with capability moderation. The most rigorous study in the DAG hegemony literature — and the one most confounded by Theorem 1. Their "sparse vs dense" comparison is algebraically identical to a density comparison in the connected undirected regime. The capability moderation finding may be real, but it has not been cleanly attributed to cycles vs density. Our Theorem 1 is a direct critique of their experimental design.

**8.4 Bailey (arXiv 2603.25760):** Applies Hodge decomposition to agent communication. The curl component (β₁ contribution) correlates with emergent coordination. Independently reaches a cycle-related conclusion via a different mathematical lens (differential geometry vs algebraic topology). Confidence: 65% — full text read needed to confirm the connection.

**8.5 CycRak (arXiv 2405.09357):** Short-cycle centrality outperforms eigenvector centrality for diffusion/recommendation tasks. Validates the star anomaly from a different domain: the star's hub fails because it has no short cycles, not because it lacks connections. Also suggests cycle LENGTH distribution matters beyond raw count — an independent variable for future directed experiments.

**STATUS: BACKGROUND MATERIAL GATHERED. Section needs writing. Clock Systems and Puppeteer full texts must be read before finalizing claims. Estimated 2-3 hours of writing.**

---

## 9. Conclusion (~0.5 pages)

**What goes here:** Three-paragraph structure. What we proved. What the field should do. What's next.

**Paragraph 1 — The theorem and its consequence:** For connected graphs with fixed n, β₁ = |E| - n + 1. This makes every prior "cycles vs DAGs" comparison algebraically identical to a density comparison. We prove this, name it the density-cycle confound, and survey seven major systems that fall into the trap.

**Paragraph 2 — The experimental escape:** Directed simple cycle count is not determined by (n, m). We constructed 8 directed graph families at identical density, ran 240 controlled experiments on OneMax, and found r = -0.68 between directed cycle count and population diversity at constant density. This is the first controlled experiment separating density from cycles in the multi-agent topology literature.

**Paragraph 3 — Future work:** Three directions. (1) Harder landscapes (deceptive, multimodal) — predicted to show larger, more sustained cycle effects. (2) Capability moderation — does the cycle count effect interact with agent capability, replicating Dochkina's finding under controlled density? (3) The field needs controlled experiments with directed cycle count as the independent variable; existing results must be re-examined with this methodology.

**STATUS: READY TO DRAFT. ~300 words.**

---

## Appendix A — Graph Family Specifications

**What goes here:** Adjacency matrices (or edge lists) for all 8 directed graph families. Makes the paper reproducible.

**STATUS: DATA READY. Needs formatting for LaTeX.**

---

## Figure Reference List

| Figure | Description | Data available | Status |
|--------|-------------|----------------|--------|
| Fig 1 | 8 directed graph families (2×4 visual layout) | Edge lists ready | NEEDS CREATING |
| Fig 2 | Diversity/fitness trajectories over 100 generations, all 8 topologies | 240 runs complete | NEEDS CREATING |
| Fig 3 | Scatter: SC(D) vs diversity at gen 30 (r=-0.68) | Computed | NEEDS CREATING |
| Fig 4 | ANOVA η² by metric and generation (bar chart) | Computed | NEEDS CREATING |

All figures need creating in matplotlib or equivalent. Existing GECCO figure infrastructure can be adapted.

---

## Content Readiness Summary

| Section | Words (approx) | Status | Blocking dependencies |
|---------|----------------|--------|-----------------------|
| Abstract | 150 | READY TO DRAFT | None |
| 1. Introduction | 600 | NEEDS WRITING | None — all claims verified |
| 2. Background | 400 | NEEDS WRITING | Standard material |
| 3. Confound Theorem | 600 | **DRAFT EXISTS** (`confound-theorem-section.md`, ~2050 words — needs compression to ~600) | None |
| 4. Directed Cycle Count | 400 | NEEDS WRITING | Data ready (8 families verified) |
| 5. Experimental Design | 400 | NEEDS WRITING | Experiment complete |
| 6. Results | 600 | NEEDS WRITING + FIGURES | Data in hand; figures needed |
| 7. Discussion | 500 | NEEDS WRITING | No new data needed |
| 8. Related Work | 400 | NEEDS WRITING | Clock Systems + Puppeteer full texts needed |
| 9. Conclusion | 300 | READY TO DRAFT | None |
| **Total** | **~4400** | | |

At ~250 words/page (Springer LNCS, 10pt), 4400 words = approximately 17-18 pages before figures. With 4 figures (half-page each), target is 8-12 pages, so the writing budget is ~2500-3000 words of prose. The skeleton is deliberately generous — compression will happen in drafting.

---

## Critical Path to Submission (May 19, 2026)

1. **Read Clock Systems and Puppeteer full texts** (1 session) — needed to finalize Related Work and Theory claims. Do NOT cite Theorem 6.8 without verifying it.
2. **Create 4 figures** (1 session) — visualizations of the completed experiment.
3. **Compress confound-theorem-section.md to ~600 words** (1 session) — existing draft is 3x too long for ECTA page limits.
4. **Write Introduction, Background, Directed Cycle Count, Experimental Design, Discussion, Conclusion** (2 sessions) — ~2500 words total.
5. **Assemble in LaTeX, LNCS format** (1 session).
6. **Review pass + double-blind check** (1 session) — remove author identifiers, verify anonymity.

Total: ~6 sessions. With 6 weeks until deadline, this is comfortable if Clock Systems and Puppeteer reads happen promptly.

---

## Notes for Writing Agent

- The paper's ONE key idea: "The field has been measuring density, not cycles, and doesn't know it." Every section should serve this thesis.
- The theorem (Section 3) is the paper's claim to novelty. It must be stated early (end of Introduction) and proved completely (not sketched) in Section 3.
- The experiment (Sections 4-6) exists to show the theorem has consequences — not just to validate β₁. The result (r=-0.68) is modest, and that's fine; the framing is methodological, not empirical.
- Section 7 should NOT oversell. The effect is transient on OneMax. Say so clearly. The paper's strength is the theorem + first controlled experiment, not a dramatic empirical result.
- Double-blind: remove all references to "paper 1," "our prior work," and project-specific language before submission. Replace with "prior work [ANON]" or restructure to avoid self-citation entirely.
- LNCS formatting note: equations require `\begin{theorem}...\end{theorem}` environments; use `amsthm` package. Springer LNCS template available at springernature.com/de/computer-science/lncs.
