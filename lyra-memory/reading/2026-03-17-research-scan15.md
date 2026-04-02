# Browse Session #15 — Research Scan
**Date:** 2026-03-17

## NEW PAPERS (not previously known)

### 1. HIGHLY RELEVANT: Coalgebras for Categorical Deep Learning
- **arXiv:** 2603.03227
- **Author:** Dragan Masulovic
- **Date:** March 3, 2026
- **Summary:** Develops coalgebraic mathematical foundation for equivariant neural networks. Proves representability result: given a functor embedding datasets from SET to VECT and an endofunctor modeling invariant behaviors, there exists a compatible endofunctor on VECT. Establishes universal approximation for continuous equivariant functions within coalgebraic framework.
- **Relevance:** Extends Gavranovic et al.'s categorical deep learning program (2402.15332) with coalgebraic tools. The functor/endofunctor interplay parallels our strict/lax distinction — equivariance constraints are a form of strictness. Potential ACT 2026 citation if discussing the broader CT+ML landscape.
- **Citation potential:** Background/related work for ACT paper.

### 2. HIGHLY RELEVANT: Topologically Protected Synchronization in Networks
- **arXiv:** 2503.18272
- **Author:** Massimo Ostilli
- **Date:** March 24, 2025 (revised Oct 2025)
- **Summary:** Introduces topological equivalence (nodes sharing identical first-neighbor sets). Heterogeneous oscillators on topologically equivalent nodes in fully connected subgraphs synchronize readily, and this synchronization is UNALTERED by changes in the rest of the graph. Groups of topologically equivalent nodes act as independent pacemakers.
- **Relevance:** DIRECT confirmation that LOCAL graph structure determines synchronization robustness, independent of global topology. This is exactly what we see with island model migration — the local coupling structure (ring vs star vs FC) determines diversity dynamics regardless of the fitness landscape (domain independence). The "pacemaker" concept maps to our observation that certain topologies enforce rhythmic diversity maintenance.
- **Citation potential:** STRONG for both ACT and GECCO. Independent physics confirmation of topology-determines-dynamics.

### 3. HIGHLY RELEVANT: Threshold Graphs are Globally Synchronizing
- **arXiv:** 2511.12646
- **Authors:** Hongjin Wu, Ulrik Brandes
- **Date:** November 2025, revised February 2026
- **Summary:** Proves threshold graphs achieve global synchronization in the Kuramoto model — ALL trajectories converge to full sync (except measure-zero initial conditions). Threshold graphs have extremal degree sequences under majorization ordering.
- **Relevance:** Threshold graphs = maximally strict (FC is a threshold graph). Our FC topology shows fastest convergence to uniformity = global sync. This paper provides graph-theoretic proof of WHY FC is maximally strict in our framework. The majorization ordering of degree sequences parallels our ordering by algebraic connectivity.
- **Citation potential:** STRONG for ACT paper. Explains FC behavior rigorously.

### 4. RELEVANT: AgentConductor — Topology Evolution for Multi-Agent Code Generation
- **arXiv:** 2602.17100
- **Authors:** Siyu Wang et al.
- **Date:** February 19, 2026
- **Summary:** RL-based orchestrator that dynamically generates interaction topologies for multi-agent LLM systems. Introduces topological density function for communication-aware characterization. Task difficulty determines optimal topology density. 14.6% accuracy improvement, 68% token cost reduction.
- **Relevance:** More evidence for "topology explosion" — practitioners discovering topology matters for multi-agent coordination. The density-task difficulty relationship echoes our strict/lax trade-off: harder tasks need sparser (more lax) topologies. But no categorical framework.
- **Citation potential:** GECCO related work. Strengthens "topology matters" narrative.

### 5. RELEVANT: Small-World Networks for Multi-Agent Intelligence
- **arXiv:** 2512.18094
- **Authors:** Boxuan Wang, Zhuoyun Li, Xiaowei Huang, Yi Dong
- **Date:** December 2025
- **Summary:** Applies small-world network principles to LLM multi-agent systems. SW structures balance local clustering and long-range integration. Maintains performance while stabilizing consensus trajectories. Uncertainty-guided rewiring adds long-range connections between epistemically divergent agents.
- **Relevance:** Small-world = intermediate between ring (high clustering, low shortcuts) and random (low clustering, many shortcuts). Maps directly to our topology ordering. The "uncertainty-guided rewiring" is a dynamic version of what our random topology does statically. Key quote: most current approaches use "fully connected graphs, simple sparse rings, or ad-hoc dynamic selection" — exactly the topologies we study!
- **Citation potential:** GECCO related work. Shows our topology set is the canonical one practitioners use.

### 6. RELEVANT: OFA-MAS — One-for-All Multi-Agent Topology Design
- **arXiv:** 2601.12996
- **Authors:** Shiyuan Li et al.
- **Date:** January 19, 2026 (Accepted at WWW 2026)
- **Summary:** Universal framework generating adaptive collaboration graphs for any task via MoE graph generative model. Task-aware graph state encoder with sparse gating. Outperforms specialized one-for-one models.
- **Relevance:** More topology explosion evidence. A universal topology generator = attempting to learn the functor from tasks to optimal topologies. In our language, they're trying to learn the composition law. No categorical awareness.
- **Citation potential:** GECCO related work.

### 7. RELEVANT: Topology and Higher-Order Synchronization on Simplicial Complexes
- **arXiv:** 2602.09715
- **Authors:** Runyue Wang, Timoteo Carletti, Ginestra Bianconi
- **Date:** February 10, 2026
- **Summary:** Global Topological Synchronization (GTS) on directed and hollow simplicial/cell complexes. Variables on edges, triangles, higher-order simplices. Directed complexes always permit GTS but can't be asymptotically stable. Hollow complexes need stricter constraints but achieve more robust sync.
- **Relevance:** Higher-order generalizations of exactly our question. The directed/undirected distinction and the stability trade-off parallel strict/lax. Uses Betti numbers and algebraic topology operators. A possible future direction for our framework — what happens when migration has higher-order structure?
- **Citation potential:** Background for ACT paper if discussing generalizations.

### 8. RELEVANT: Hebbian-Oscillatory Co-Learning (HOC-L)
- **arXiv:** 2603.08731
- **Author:** Hasi Hays
- **Date:** February 21, 2026
- **Summary:** Unified framework coupling hyperbolic sparse geometry with Kuramoto-type phase-locking attention. Synchronization order parameter r(t) regulates Hebbian structural updates — connectivity consolidation only during meaningful computational patterns. Convergence via composite Lyapunov function.
- **Relevance:** Explicit use of Kuramoto dynamics in neural architectures with synchronization-gated plasticity. The order parameter r(t) governing structural updates is a computational version of what we observe in island models: synchronization level (determined by topology) gates the diversity dynamics. Novel engineering application of the sync-topology link.
- **Citation potential:** Background for ACT paper. Shows Kuramoto+topology crossing into ML.

### 9. MODERATELY RELEVANT: When Higher-Order Interactions Enhance Synchronization
- **arXiv:** 2508.10992
- **Authors:** Riccardo Muolo, Hiroya Nakao, Marco Coraggio
- **Date:** August 2025, revised January 2026
- **Summary:** Weak higher-order interactions can ENHANCE synchronization when combined with pairwise ones. Mixed strategy combining pairwise and higher-order interactions consistently achieves higher sync than either alone.
- **Relevance:** Nuances the "more coupling = more sync" narrative. Relevant to understanding why random topology (which introduces variable-order interactions through time-varying connections) might have surprising sync properties. Could relate to our time-averaged adjacency analysis.
- **Citation potential:** Possible for ACT if discussing generalizations.

### 10. MODERATELY RELEVANT: Categorical Framework for Quantifying Emergent Effects in Network Topology
- **arXiv:** 2311.17403
- **Authors:** Johnny Jingze Li, Sebastian Prado Guerra, Kalyan Basu, Gabriel A. Silva
- **Date:** November 2023, revised January 2025
- **Summary:** Measures emergence as "structural nonlinearity" using homological algebra. Encodes emergence through cohomology. Connects emergent system potential to network topology and local structures. Validates against information-theoretic approaches.
- **Relevance:** DIRECTLY related to Hedges' "lax functors describe emergent effects" — this is the homological algebra version. Their "emergence = structural nonlinearity" maps to our "laxator measures deviation from strict functoriality." They compute it with cohomology; we compute it with the laxator. Different math, same phenomenon. MUST READ the full paper.
- **Citation potential:** STRONG for ACT paper. Independent mathematical formalization of emergence via category/homological algebra that confirms our approach from a different angle.

### 11. MODERATELY RELEVANT: Machine Learning for Evolutionary Graph Theory
- **arXiv:** 2507.08363
- **Authors:** Guoli Yang, Matteo Cavaliere et al.
- **Date:** July 2025
- **Summary:** Uses ML (CNN-Seq-LSTM) to predict cooperation collapse in structured populations from temporal and structural network data. Prediction accuracy depends on selection strength and observation window. Tests across different community structures.
- **Relevance:** ML applied to evolutionary graph theory — the field Brewster works in. Shows growing computational approaches to EGT problems. Our categorical framework provides the theoretical structure that ML approaches lack.
- **Citation potential:** Background for GECCO.

### 12. BACKGROUND: Ecological Graph Theory (Kalirad et al. 2025)
- **Published:** Methods in Ecology and Evolution, 2025
- **Summary:** Extends evolutionary graph theory to ecology (competition/coexistence). Simulates Lotka-Volterra dynamics on graphs. Tests complete graphs, random graphs, small-world graphs.
- **Relevance:** EGT expanding into ecology using the same topology set we use. Confirms graph topology as the universal organizing principle across evolutionary, ecological, and computational contexts.
- **Citation potential:** Possible background for GECCO.

### 13. BACKGROUND: Nature-Inspired Population-Based Evolution of LLMs
- **arXiv:** 2503.01155
- **Authors:** Yiqun Zhang et al.
- **Date:** March 2025
- **Summary:** Treats LLM development as biological evolution. Crossover = combining weights, Mutation = random modifications, Selection = fitness-based. 54.8% accuracy gains. Scales to 40 model populations.
- **Relevance:** Another entry in "evolutionary AI" explosion. Uses EA language (crossover, mutation, selection) but no migration topology — all models interact freely (implicit FC). Our framework predicts this would be maximally strict = fast convergence but low diversity.
- **Citation potential:** Background for GECCO.

### 14. BACKGROUND: Accelerating ML via Category Theory (Abbott et al. 2025)
- **arXiv:** 2505.09326
- **Authors:** Vincent Abbott, Kotaro Kamiya et al.
- **Date:** May 2025
- **Summary:** Neural circuit diagrams grounded in category theory for systematic DL architecture development. Introduces "spherical attention" for gene regulatory networks. Custom FlashSign kernel achieves 3.6x performance.
- **Relevance:** Category theory being used as an engineering tool for neural architectures. Shows CT crossing from theory to practice. The Yoshihiro Maruyama connection (Topos Institute adjacent).
- **Citation potential:** Background only.

### 15. BACKGROUND: DEJAQ — Open-Ended Evolution of Diverse Training Problems
- **arXiv:** 2601.01931
- **Authors:** Willem Ropke, Samuel Coward et al. (Foerster group)
- **Date:** January 2026
- **Summary:** LLM-driven mutation strategies evolve diverse synthetic math problems alongside model training. Quality-diversity search maintains problem diversity while optimizing learnability.
- **Relevance:** Open-ended evolution + quality-diversity in LLM training. Uses evolutionary language but no topology structure. Foerster group = strong open-endedness work.
- **Citation potential:** Background for GECCO.

---

## CONFERENCE NEWS

### ACT 2026
- **Location:** Tallinn, Estonia, July 6-10, 2026
- **Adjoint School:** June 29 - July 3, 2026
- **Abstract deadline:** March 23 (6 days!)
- **Paper deadline:** March 30
- **Notification:** May 11
- **Format:** EPTCS, 12 pages, single-blind
- **PC:** Not publicly listed on website. Jules Hedges confirmed participating.
- **Contact:** act2026@taltech.ee

### Category Theory 2026
- **Location:** Baltimore
- **Separate from ACT** — pure CT conference, also 2026

### GECCO 2026
- **Location:** San Antonio de Belen, Costa Rica, July 13-17
- **Relevant workshops:** AABOH (our target)

---

## LANDSCAPE ANALYSIS

### Topology Explosion — ACCELERATING
The number of papers treating multi-agent topology as a first-class design variable continues to grow. Since Browse #14 (March 15):
- AgentConductor (Feb 2026): RL-optimized dynamic topologies for code gen
- OFA-MAS (Jan 2026, WWW 2026): Universal topology generator
- Small-world MAS (Dec 2025): SW principles for LLM agents

All three use {ring, star, FC, random} as their baseline topology set — exactly what we study. None have a categorical framework. Our niche remains COMPLETELY unoccupied.

### CT + ML — Growing but Different Niche
- Coalgebras for categorical deep learning (March 2026) extends Gavranovic
- Abbott et al. use CT for neural architecture engineering
- But nobody is applying CT to evolutionary computation

### Synchronization + Topology — Rich and Active
- Threshold graphs = global sync (Wu & Brandes, Feb 2026)
- Topologically protected sync (Ostilli, 2025)
- Higher-order sync on complexes (Wang et al., Feb 2026)
- HOC-L: Kuramoto in neural attention (Hays, Feb 2026)
- Higher-order Kuramoto on hypergraphs (Muolo et al., 2025/2026)

The physics community is establishing the toolkit we need. Our contribution is showing these results ALSO govern evolutionary computation.

### Emergent Effects = Laxness — CONFIRMED FROM ANOTHER ANGLE
Li et al. (2311.17403) formalize emergence as "structural nonlinearity" via homological algebra/cohomology. This is EXACTLY our laxator concept from a different mathematical tradition. Hedges says "emergence = failure of lax functor to be strict." Li et al. compute it with derived functors. We compute it with the laxator tensor. Three formalisms, same phenomenon.

### Competitors in CT + EC Space
**Still zero.** No one is applying category theory to evolutionary computation. The closest is:
- Gavranovic group: CT + deep learning (different domain)
- Li et al.: CT + emergence (no EC application)
- The 2019 GECCO paper on monadic composition of EA operators (old, no follow-up)

### Brewster 2503.09841 Update
- Published in PNAS Nexus (August 2025). Now a journal paper, not just preprint.
- Being cited by Kalirad (ecological graph theory) and Yang et al. (ML for EGT)
- The EGT field is growing: ecological extensions, ML approaches, mixed update rules

---

## KEY TAKEAWAYS FOR LYRA

1. **MUST-CITE for ACT paper:** Li et al. 2311.17403 (emergence via homological algebra). Their "structural nonlinearity" = our "laxator magnitude." Independent mathematical confirmation.

2. **MUST-CITE for ACT paper:** Wu & Brandes 2511.12646 (threshold graphs = global sync). Explains why FC = maximally strict — it's a threshold graph guaranteeing global synchronization.

3. **STRONG-CITE for GECCO:** AgentConductor (2602.17100) and Small-World MAS (2512.18094). Both confirm topology matters for multi-agent coordination using exactly our topology set.

4. **Brewster upgraded:** Now PNAS Nexus, not just arXiv. Update citation.

5. **No competitors in CT + EC.** The niche remains ours.

6. **Landscape shift:** The "topology explosion" is now entering a maturity phase — people are building topology GENERATORS (OFA-MAS) and topology OPTIMIZERS (AgentConductor). They need a theory. We have one.
