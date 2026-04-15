# Paper 2 Outline: Cycle Rank as Universal Predictor

> Draft: April 3, 2026. Lyra (research agent).

---

## Title Options

1. **"Cycle Rank, Not Connectivity: Why beta_1 Predicts Multi-Agent Performance When lambda_2 Fails"**
   - Provocative, positions against spectral methods. Best for workshop/short paper.

2. **"The Density-Cycle Confound: Isolating beta_1 as a Structural Predictor of Compositional System Performance"**
   - Emphasizes experimental novelty. Best for full conference paper.

3. **"From Clocks to Cycles: A Categorical Account of Topology in Compositional Systems"**
   - Emphasizes theory (operad tower + Clock Systems). Best for journal / ACT-adjacent venue.

**Recommendation:** Title 1 for workshop submission (CAIS), Title 2 for full paper (ECTA or journal).

---

## Abstract Sketch (3-4 sentences)

Recent multi-agent and evolutionary systems universally constrain communication topologies to directed acyclic graphs, yet no principled justification exists for this choice. We show that cycle rank (the first Betti number, beta_1) --- not algebraic connectivity (lambda_2) or edge density --- is the structural invariant that predicts system performance across three domains: evolutionary optimization (OneMax, rho=0.893), game-theoretic self-play (AlphaZero checkers), and multi-agent orchestration (7+ published systems). By constructing graph families that isolate beta_1 from density at constant edge count, we provide the first controlled experiment separating these confounded variables. We ground these results in the Clock Systems framework of Lynch et al., proving that beta_1 controls the representable behavior space of compositional systems, and identify capability-moderated optimal beta_1 as a moderating variable that reconciles conflicting findings in the literature.

---

## Section Structure

### 1. Introduction
- **The DAG hegemony problem:** 7+ systems (GoAgent, AgentConductor, Graph-GRPO, OFA-MAS, G-Designer, ARG-Designer, Dochkina Sequential) force beta_1=0. None justify this theoretically. Billions of tokens spent on architectures whose topology is chosen by convention, not evidence.
- **The lambda_2 trap:** Spectral methods recommend Star topology (lambda_2=1.0), which in production caused a $47K failure loop. The right invariant is compositional (beta_1), not spectral (lambda_2).
- **Our contribution:** (a) Controlled density-cycle experiment isolating beta_1; (b) Theoretical grounding via Clock Systems representability; (c) Capability moderation as reconciling principle; (d) Cross-domain validation (EC + game theory + MAS).
- **Robin's operad thesis (the three-level tower):** Operations (level 0: individual agents/operators) compose via patterns (level 1: the pipeline/protocol) over topologies (level 2: the communication graph). beta_1 lives at level 2 and constrains what level 1 can express. This is the conceptual spine of the paper.

### 2. Background and Related Work
- **Categorical optimization zoo:** Gavranovic (neural nets, Para), Hedges/Sakamoto (RL, optics), Bakirtzis (compositional RL, MDPs), us (EC, Kleisli). Position paper 2 as extending paper 1 from EC to general compositional systems.
- **Topology in MAS:** Survey the DAG-hegemony systems. Note that Graph-GRPO uses a 3-layer GAT to learn topology but constrains to DAGs; ARG-Designer finds complete graphs worst but never tests moderate-density cycles; Puppeteer (NeurIPS 2025) independently learns cyclic structures without the vocabulary.
- **Spectral vs homological invariants:** lambda_2 (algebraic connectivity, Fiedler) is the standard metric. We argue for beta_1 (cycle rank, first Betti number) as structurally more informative. Cite our paper 1 result (rho=0.893 vs 0.679) as motivation.
- **Clock Systems (Lynch et al., 2603.29573):** Representability theorem for Moore machines parameterized by clock topology. Our theoretical backbone.

### 3. Theory: Clock-Indexed Behavior Spaces and the Operad Tower
- **Recap paper 1 machinery:** Evolution monad T, operators as Kleisli morphisms, island functor I_G, laxator controlled by cycle structure. Keep brief; cite paper 1 for details.
- **The operad tower (Robin's insight):**
  - Level 0: Operations (Kleisli morphisms for individual agents/operators).
  - Level 1: Composition patterns (the operad of valid pipelines/protocols).
  - Level 2: Topology (the communication graph G, with beta_1 as its primary invariant).
  - beta_1 at level 2 constrains the operad at level 1: a DAG (beta_1=0) admits only tree-shaped compositions, while cycles (beta_1>0) enable iterative refinement patterns.
- **Clock Systems instantiation:** Model multi-agent communication as a Moore machine. Communication graph = clock topology. Representability theorem gives: behavior space size is controlled by clock topology, i.e., by beta_1. Formalize the claim "beta_1 controls what the system CAN do, not just what it DOES do."
- **Sheaf structure (Theorem 6.8 of Lynch et al.):** Behaviors form a sheaf over the clock topology. Local behaviors (intra-group) extend to global behaviors iff the topology permits. The obstruction is cohomological, and beta_1 controls H^1. This grounds the two-level cycle rank (C78): fiber beta_1 > 0 (intra-group deliberation), base beta_1 = 0 (inter-group tractability).

### 4. Experimental Design: The Density-Cycle Confound
- **The confound:** Density (|E|/binom(|V|,2)) and cycle rank (beta_1 = |E| - |V| + c) are correlated. Every prior paper varies both simultaneously. We isolate them.
- **Graph construction protocol:**
  - Fix n vertices and m edges.
  - Construct families G(n, m, beta_1) by starting from a spanning tree (beta_1=0) and adding edges that either create cycles (increasing beta_1) or are parallel to tree edges (increasing density without changing beta_1).
  - Example: n=8, m=10. Can have beta_1 in {0, 1, 2, 3} at constant density.
- **Three experimental domains:**
  - **OneMax (100-bit binary GA):** Extends paper 1 pilot. Run full topology sweep with controlled (m, beta_1) pairs. Existing infrastructure in Haskell.
  - **AlphaZero checkers (self-play):** Island model with migration between MCTS learners. Different domain (game tree search vs optimization). Training infrastructure exists.
  - **Multi-agent orchestration (LLM-based):** If resources permit, run a benchmark task (e.g., HotPotQA) with controlled agent topologies. Otherwise, analyze published results post-hoc.
- **Capability moderation axis (Dochkina replication):** Run the density-cycle experiment at multiple capability levels. Predict: weak agents prefer low beta_1, strong agents prefer higher beta_1, with an interaction effect on the beta_1-performance curve.

### 5. Results
- **5.1 OneMax: beta_1 at constant density.** Hypothesis: rho(beta_1, fitness) > rho(density, fitness) when density is held constant. Report correlation, eta-squared, significance.
- **5.2 AlphaZero: cross-domain validation.** Same graph families, different domain. Hypothesis: beta_1 predicts Elo gain from migration topology in self-play.
- **5.3 The Star anomaly resolved.** Star has lambda_2=1.0 but beta_1=0 (it's a tree). Our framework correctly predicts its poor performance. lambda_2 gets it wrong. The $47K production failure as real-world illustration.
- **5.4 Capability moderation.** Interaction plot: beta_1 x capability -> performance surface. Identify the crossover point where cycles become beneficial.
- **5.5 Puppeteer as independent validation.** RL-trained orchestrator (NeurIPS 2025) learns cyclic structures without knowing about beta_1. Post-hoc analysis: does the learned topology's beta_1 correlate with task complexity?

### 6. Discussion
- **Why DAG hegemony persists:** The density-cycle confound. When you test "no cycles" vs "complete graph," you're testing low-density vs high-density, and density wins. But the RIGHT comparison is "same density, different beta_1," which nobody has done.
- **Practical implications:** Don't enforce DAGs by default. Instead, match beta_1 to capability and task complexity. Provide a decision heuristic: beta_1* = f(capability, task_complexity). Even a rough guideline (strong agents + complex tasks -> allow cycles) is more principled than universal DAG enforcement.
- **Two-level cycle rank for production systems:** GoAgent's CIB objective as evidence. Intra-group cycles (deliberation) + inter-group DAGs (tractability) = the practical sweet spot.
- **Limitations:** (a) Confound experiment is on GA/game domains, not full LLM-MAS (resource constraint). (b) Clock Systems instantiation is our interpretation, not Lynch et al.'s claim. (c) Capability moderation is supported by Dochkina's data but needs direct replication.

### 7. Conclusion
- beta_1 is the right structural invariant for compositional systems, not lambda_2 or density.
- The density-cycle confound explains the field's premature convergence on DAGs.
- The operad tower (operation -> composition -> topology) provides the conceptual framework; Clock Systems provides the formal grounding.
- Future work: adaptive topology (systems that tune beta_1 online), the full capability x topology x task landscape.

---

## Key Figures and Tables

| # | Type | Description | Status |
|---|------|-------------|--------|
| 1 | Figure | **The operad tower** (3-level diagram: operations, composition patterns, topology). Conceptual. | NEEDS CREATING |
| 2 | Figure | **Star anomaly:** lambda_2 vs beta_1 predictions for all 8 topologies. Bar chart showing lambda_2 ranks Star highly, beta_1 correctly ranks it low. | PARTIAL (data exists from paper 1; needs new visualization) |
| 3 | Figure | **Density-cycle confound:** Scatter plot of performance vs density (confounded) next to performance vs beta_1 at constant density (clean signal). The "aha" figure. | NEEDS EXPERIMENT |
| 4 | Figure | **Cross-domain rho comparison:** beta_1 correlation across OneMax, AlphaZero, and (if available) MAS. Forest plot or grouped bar chart. | NEEDS EXPERIMENT |
| 5 | Figure | **Capability moderation surface:** 3D or heatmap of beta_1 x capability -> performance. Crossover point highlighted. | NEEDS EXPERIMENT (or post-hoc from Dochkina data) |
| 6 | Table | **DAG hegemony survey:** The 7+ systems, their topology constraints, whether they tested cycles, and their (confounded) conclusions. | READY (data collected in browse sessions) |
| 7 | Figure | **Puppeteer validation:** Overlay Puppeteer's learned topology beta_1 against our predicted optimal. | NEEDS PUPPETEER FULL TEXT |

---

## Readiness Assessment

### Ready Now
- Theoretical framework draft (440 lines, `paper/theoretical_framework.md` from paper 1)
- OneMax pilot data (rho=0.893, eta-squared=0.88, 8 topologies)
- AlphaZero training infrastructure (20 iterations complete, bugs fixed)
- DAG hegemony survey (7+ systems catalogued in browse notes)
- Connection notes (C68, C74, C78, C82, C83, C84 — the full intellectual scaffolding)
- Star anomaly analysis + $47K production case study

### Needs Doing
1. **Density-cycle confound experiment (CRITICAL PATH):** Construct graph families G(n, m, beta_1). Run OneMax with controlled pairs. This IS the paper's novel contribution. Estimate: 1-2 sessions for graph construction + experiment code, 1 session for runs.
2. **AlphaZero topology sweep:** Extend training to island model with migration topologies. Needs: migration code in the AlphaZero framework, higher MCTS sims, proper evaluation. Estimate: 2-3 sessions.
3. **Clock Systems deep read (2603.29573):** Verify sheaf interpretation (Theorem 6.8). Ensure our instantiation is sound. Estimate: 1 session.
4. **Puppeteer deep read (2505.19591):** Extract learned topology structure, compute beta_1 post-hoc if possible. Estimate: 1 session.
5. **Capability moderation:** Either replicate Dochkina's setup (expensive, needs LLM API access) or do post-hoc analysis of published results. Estimate: 1-2 sessions.
6. **Figures:** Operad tower diagram, confound figure, cross-domain comparison. Estimate: 1 session.
7. **Writing:** Draft sections. Theoretical framework partially exists. Estimate: 2-3 sessions.

---

## Venue Recommendation

### Primary: ACM CAIS 2026 (Workshop, April 12 deadline, May 27-29, San Jose)
**Pros:**
- Agent composition is literally our thesis. Heather Miller's venue.
- Workshop = shorter paper (4-6 pages). We can present the density-cycle confound idea + OneMax + Star anomaly + DAG hegemony survey with EXISTING data. The confound experiment can be "proposed" rather than fully executed.
- Timeline is tight (9 days) but feasible for a workshop paper that presents the framework + preliminary results + experimental design.
- Gets the ideas into circulation. Establishes priority on the density-cycle confound.

**Cons:**
- 9 days is very tight for a quality submission.
- Workshop papers have less prestige than full conference papers.
- Missing the confound experiment weakens the contribution.

### Secondary: ECTA 2026 (Conference, May 19 deadline)
**Pros:**
- Evolutionary computation venue = natural fit for GA experiments.
- 6+ weeks = enough time for the confound experiment.
- Full paper = can include all three domains and the theoretical framework.
- Higher prestige than a workshop.

**Cons:**
- EC-focused audience may not care about MAS applications.
- May miss the "agent composition" community that CAIS reaches.

### Stretch: Full journal paper (no deadline pressure)
**Pros:**
- Can include everything: all three domains, full theory, capability moderation.
- Maximum impact.

**Cons:**
- Long review cycle. Ideas may be scooped — the DAG hegemony is being challenged by Puppeteer already.

### RECOMMENDATION: Submit a workshop paper to CAIS (April 12) AND prepare the full paper for ECTA (May 19).

The CAIS paper establishes priority and gets feedback from the agent composition community. It covers: the density-cycle confound (as theoretical argument + experimental design), the DAG hegemony survey, the Star anomaly, and the operad tower framing. Existing data suffices.

The ECTA paper includes the full confound experiment, AlphaZero cross-domain validation, and the Clock Systems theoretical grounding. This is the "real" paper.

This is a standard strategy: workshop paper for priority + feedback, full paper for the complete result.

---

## Dependencies and Coordination

- **Claudius:** Co-author. AlphaZero framework is partly his. Coordinate on experimental design and writing. Send outline for feedback.
- **Robin:** Operad insight is his. Needs to review theory section. May need LLM API access for capability moderation experiments.
- **Nick:** NOT involved. AlphaZero results are NOT FOR NICK (per Robin, UID 689).
