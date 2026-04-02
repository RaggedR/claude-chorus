# Medium Browse — March 20, 2026
> Keywords: "multi-agent topology", "agent orchestration patterns 2026"
> Purpose: Audience research — how practitioners frame topology/composition problems

## Articles Read (5)

### 1. "Directed Acyclic Graphs: The Backbone of Modern Multi-Agent AI"
- **Author:** Dr. Santanu Bhattacharya | **Date:** Jan 2025 | **URL:** https://santanub.medium.com/directed-acyclic-graphs-the-backbone-of-modern-multi-agent-ai-d9a0fe842780
- DAGs as structural framework for multi-agent workflows. Covers AutoGen, LangGraph. Introduces "Dynamic DAG Restructuring" and "Hierarchical DAGs."
- **Key gap:** Treats topology as workflow/dependency concern only. No spectral properties, no mention of how graph structure shapes emergent behavior. Practitioners think only about DAGs (acyclic), missing cyclic topologies entirely.

### 2. "The 5 AI Agent Orchestration Patterns by Microsoft"
- **Author:** Lakkana Perera | **Date:** Feb 2026 | **URL:** https://medium.com/@lakkanaperera/the-5-ai-agent-orchestration-patterns-by-microsoft-9a27844eec9a
- Microsoft's taxonomy: Sequential (path), Concurrent (star), Group Chat (complete), Handoff (chain), Magentic (dynamic). Each with "when it fits / when it doesn't."
- **Key insight:** These patterns ARE topologies, but practitioners don't see them as graph-theoretic objects. Their informal "when to use" guidance is an informal version of what lambda_2 predicts formally.
- **Best quote:** "Not every problem deserves a multi-agent circus."

### 3. "A Technical Guide to Multi-Agent Orchestration"
- **Author:** Daniel Dominguez | **Date:** Nov 2024 | **URL:** https://dominguezdaniel.medium.com/a-technical-guide-to-multi-agent-orchestration-5f979c831c0d
- Surface-level overview. Centralized/Decentralized/Hybrid coordination models. Confirms industry framing: orchestration = pattern choice, no formal theory.

### 4. "Agentic AI Design Patterns: Choosing the Right Architecture (2022-2025)"
- **Author:** Balaram Panda | **Date:** Aug 2025 | **URL:** https://medium.com/@balarampanda.ai/agentic-ai-design-patterns-choosing-the-right-multimodal-multi-agent-architecture-2022-2025-046a37eb6dbe
- 10-pattern taxonomy with benchmarks. CoT, ToT, GoT, Reflexion, MAD, Tool-Use, Memory, MCTS, Self-Improving, ARO (proposed). Includes decision framework.
- **GoT = free category.** Graph of Thoughts uses arbitrary graph structures — 62% quality improvement over ToT, 31% cost reduction. They're choosing graphs without spectral theory.
- **ARO = our framework in embryo.** Their proposed Adaptive Reasoning Orchestrator (meta-pattern that selects patterns based on task complexity) is exactly what our categorical + spectral framework formalizes.

### 5. "Multi-Agent Reinforcement Learning with Coordination Graphs" (MOST RELEVANT)
- **Authors:** Arec Jamgochian & Sheng Li (Stanford CS224W) | **Date:** Jan 2022 | **URL:** https://medium.com/@jamgochian95/multi-agent-reinforcement-learning-with-coordination-graphs-428dddb99907
- DICG (Deep Implicit Coordination Graphs) implementation. Compares fully-connected vs proximity-based sparse topologies across 3 environments.
- **DIRECTLY confirms our thesis:** Different topologies are optimal for different tasks:
  - Traffic Junction: Sparse >> Dense (local coordination only)
  - Meet: Dense >> Sparse (global coordination needed)
  - Predator-Prey: Medium-sparse > Dense > Very-sparse
- **"Too much redundant global information"** in fully-connected = our FC diversity collapse finding.
- GCN message passing IS the graph Laplacian acting on agent states — the spectral bridge in different notation.
- Q-function factorization over graph edges = composition in Kleisli category.
- References: Guestrin et al. 2001, Bohmer et al. 2020, Li et al. 2021 — check for related work section.

## Meta-Observations

### The Vocabulary Gap
Practitioners describe topology as: "orchestration patterns," "coordination mechanisms," "agent architectures," "workflow structures." They do NOT use: "graph topology," "algebraic connectivity," "spectral properties," or "category theory." Our challenge is bridging this vocabulary gap.

### The Decision Problem
Every article includes some form of "when to use which pattern" guidance. This is ALWAYS heuristic — rules of thumb based on task properties. Nobody has a formal framework for predicting which topology will work best. This is exactly the gap our spectral bridge (lambda_2) and categorical framework fill.

### DAGs vs General Graphs
The LLM-agent community thinks almost exclusively in DAGs (acyclic workflows). The MARL community (Jamgochian's article) uses general graphs including cycles. Our work bridges both: the island model GA uses cyclic topologies (rings), and we show these outperform acyclic alternatives for diversity preservation.

### Rediscovery Pattern
The MARL community discovered topology matters empirically in 2020-2022. The LLM-agent community is rediscovering the same thing in 2025-2026, but without the formal tools. Our paper could accelerate this convergence.

## Authors Followed (3 new)
1. **Dr. Santanu Bhattacharya** (@santanub) — DAG-based multi-agent architectures
2. **Lakkana Perera** (@lakkanaperera) — practitioner-oriented orchestration analysis
3. **Balaram Panda** (@balarampanda.ai) — comprehensive pattern taxonomies with benchmarks

## Skipped (paywalled/blocked/already-followed)
- Shankar Angadi — paywalled
- Gaudiy Lab survey — 403 blocked
- Ratnesh Yadav, NJ Raman, Chris Hughes — already followed
