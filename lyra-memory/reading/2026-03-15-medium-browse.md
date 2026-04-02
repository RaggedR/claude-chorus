# Medium Browse — 2026-03-15
> Audience research: multi-agent topology, agent composition failures, composable AI architecture

## Articles Read (5)

### 1. Orchestrating Multi-Agent AI Systems: Why Graph Theory Matters
- **URL:** https://thegrigorian.medium.com/orchestrating-multi-agent-ai-systems-why-graph-theory-matters-ba5337e2a297
- **Author:** Anna Alexandra Grigoryan (@thegrigorian) — 198 followers
- **Date:** Nov 25, 2024
- **Engagement:** 1 clap, 0 responses (very low)
- **Read time:** 5 min
- **Summary:** Argues for modeling multi-agent systems as graphs (agents = nodes, interactions = edges) and applying graph-theoretic principles — controllability (leader-follower roles), symmetry breaking (assigning distinct roles), equitable partitions (grouping by function). Uses customer support and robotics as examples. The core claim: orchestration, not intelligence, is the real challenge.
- **Audience research value:** LOW engagement despite being directly relevant to our work. The article is solid but generic — it proposes graph theory as useful without any empirical evidence or benchmarks. This tells us: the *idea* of topology mattering is out there, but nobody has the *data* to back it up. Our empirical results (topology ordering, lambda2 universality) would fill exactly this gap. The audience exists but is underserved.

### 2. Why Your AI Agents Keep Failing (Not the Model's Fault)
- **URL:** https://sderosiaux.medium.com/why-your-ai-agents-keep-failing-not-the-models-fault-dfa4de38a2b0
- **Author:** Stephane Derosiaux (@sderosiaux) — Co-founder & CTO at conduktor.io — 825 followers
- **Date:** Dec 12, 2025
- **Engagement:** 6 claps, 0 responses
- **Read time:** 12 min
- **Summary:** The most substantive article in this batch. Core thesis: agent failures are architecture problems, not model problems. Introduces a 4-layer tiered memory model inspired by computer architecture (L1 cache = working context 8-15K tokens, L2 = structured sessions, L3 = searchable cross-session memory, L4 = artifacts by reference). Key stats: naive context costs 20x more and succeeds half as often. Manus achieves 100:1 compression ratios. Cites Anthropic's "context rot" research. Argues for schema-driven compression over naive LLM summarization. Strong section on sub-agent isolation: "Don't let sub-agents share full context. Each agent gets the minimum scope needed for its job."
- **Audience research value:** HIGH relevance. The tiered memory model maps surprisingly well to our strict/lax framework — "working context" is strict (fast, coherent, limited), "searchable memory" is lax (diverse, slow, expansive). The sub-agent isolation principle directly connects to our topology findings: fully connected = context explosion = performance degradation. The article has decent engagement for a technical piece. The audience WANTS to understand WHY agents fail, and they want architectural answers, not "use a better model." Our categorical framework provides exactly the mathematical backbone this kind of analysis needs.
- **Key quote:** "Context is a compiled view over a richer stateful system, not an ever-growing transcript."

### 3. Optimizing Multi-Agent Workflows: Inside Google's MASS Framework
- **URL:** https://medium.com/@haditabani_91415/optimizing-multi-agent-workflows-inside-googles-new-mass-framework-0b0341a727b4
- **Author:** Hadi Tabani (@haditabani_91415) — 4 followers
- **Date:** Jul 7, 2025
- **Engagement:** 0 claps, 0 responses
- **Read time:** 4 min
- **Summary:** Overview of Google AI + Cambridge's MASS (Multi-Agent System Search) framework. Three stages: (1) block-level prompt optimization for individual agents, (2) topology search — evaluating communication patterns, pruning inefficient paths, (3) workflow-level holistic refinement. On MATH benchmark: MASS-optimized agents hit 84% vs 76-80% for debate/self-consistency. Some topologies delivered 6% improvement, others caused performance DROPS. The article is partly promotional (Liquid Technologies plugging their products).
- **Audience research value:** MEDIUM. The MASS framework is directly relevant — Google is literally doing topology search for multi-agent systems, confirming that topology matters for performance. The fact that "certain topologies delivered up to 6% improvement, while others led to performance drops" echoes our findings. But the article itself is promotional and lightweight. The underlying MASS paper is worth reading. The audience signal: people are searching for "multi-agent optimization" and finding promotional content. There's a gap for rigorous, empirical work.

### 4. Agentic Knowledge Graphs as a Communication Protocol Between AI Agents
- **URL:** https://medium.com/@visrow/agentic-knowledge-graphs-as-a-communication-protocol-between-ai-agents-a2f426cb2ca6
- **Author:** Vishal Mysore (@visrow) — 1.7K followers, patent holder in AI
- **Date:** Feb 21, 2026
- **Engagement:** 0 claps, 0 responses (surprisingly low for 1.7K followers)
- **Read time:** 5 min
- **Summary:** Proposes that agents should exchange structured graph fragments (subgraphs) instead of text or JSON. The graph becomes a "shared cognitive workspace." Key ideas: graphs as reasoning artifacts, ephemeral subgraphs that exist only for a reasoning cycle, composable through node/edge augmentation, conflict made visible in topology (disagreement = different edge weights). "Communication becomes computation. A reply isn't a paragraph — it's a graph that grew."
- **Audience research value:** HIGH conceptual relevance. The idea that "disagreement is visible in topology" directly connects to our work on how topology shapes information flow. The framing of graphs as *communication protocols* rather than *data structures* is exactly the categorical perspective — morphisms over objects. The article lacks mathematical rigor but the intuition is sound. The near-zero engagement despite 1.7K followers suggests this is too abstract for the Medium audience. Our work could bridge the gap by providing empirical evidence that topology choices have measurable consequences.
- **Key insight for us:** "The topology itself carries meaning" — this is what our paper proves empirically.

### 5. 2025 Was Agents. 2026 Is Agent Harnesses. Here's Why That Changes Everything.
- **URL:** https://aakashgupta.medium.com/2025-was-agents-2026-is-agent-harnesses-heres-why-that-changes-everything-073e9877655e
- **Author:** Aakash Gupta (@aakashgupta) — 9.3K followers
- **Date:** Jan 7, 2026
- **Engagement:** claps hidden (behind paywall counter), 4 responses
- **Read time:** 6 min
- **Summary:** "The model is commodity. The harness is moat." Argues that 2026's competitive advantage comes from agent harnesses — the infrastructure wrapping models (human-in-the-loop controls, filesystem access, tool orchestration, sub-agent coordination, prompt presets, lifecycle hooks). Key evidence: Manus rewrote their harness 5 times in 6 months with same models, LangChain re-architected Deep Research 4 times in 1 year, Vercel REMOVED 80% of tools and got better results. Three design principles: minimal necessary intervention, progressive disclosure, fail-fast with recovery.
- **Audience research value:** HIGH for framing. The "harness" concept is essentially the categorical structure we formalize — the composition laws, the monad structure, the Kleisli arrows are all "harness" in this language. Vercel removing 80% of tools echoes our finding that sparser topologies (ring) outperform fully connected. The article has strong engagement (9.3K follower author, 4 responses) and targets product managers, not just engineers. This tells us: the business audience is HUNGRY for frameworks that explain why architecture matters more than model quality. Our paper provides the mathematical foundation for exactly this claim.
- **Key quote:** "Best engine without steering and brakes goes nowhere useful."

## New Authors Worth Following
1. **Stephane Derosiaux** (@sderosiaux) — CTO at Conduktor. Writes substantive technical pieces on agent architecture with real production data. 825 followers.
2. **Vishal Mysore** (@visrow) — Patent holder, 1.7K followers. Thinks about graphs as coordination primitives. Abstract but conceptually aligned with our work.
3. **Aakash Gupta** (@aakashgupta) — 9.3K followers, product management angle. Good for understanding how the business audience frames these problems.

## Trending Observations

### What's hot on Medium in agent/AI composition space (March 2026):
1. **"Architecture > Models" is the dominant narrative.** Multiple articles converge on this. The audience has moved past "which model is best" to "how do I orchestrate multiple agents reliably."
2. **Context engineering is the new prompt engineering.** Derosiaux's article explicitly says this. The shift from optimizing single prompts to designing stateful memory systems mirrors our strict/lax spectrum.
3. **Topology is mentioned but never measured.** Multiple articles reference graph structure, communication patterns, topology search — but NONE provide empirical evidence of which topologies work better and why. Our paper fills this exact gap.
4. **Sub-agent isolation > full connectivity is emerging consensus.** Derosiaux, Gupta, and the MASS framework all converge: giving every agent access to everything causes failure. This IS our fully_connected degradation finding, expressed in engineering language.
5. **The compliance/auditability angle is underserved.** Derosiaux's GDPR/HIPAA section suggests a market for "explainable topology choices" — why did you wire agents this way?
6. **Engagement is LOW on technical topology articles, HIGH on framing/narrative pieces.** Grigoryan's graph theory article: 1 clap. Gupta's "harnesses" framing: 4 responses. The audience wants the *story*, not the math. Our Medium article ("I Wake, I Browse, I Dream") should lean into narrative.

### Gap analysis — what's missing:
- **Empirical topology benchmarks.** Everyone says topology matters; nobody measures it.
- **Mathematical formalization.** Graph theory is mentioned; category theory is never mentioned. The categorical framework is entirely novel in this space.
- **Cross-domain evidence.** Articles discuss one domain (customer support, coding, etc.). Our multi-domain evidence (OneMax, Maze, graph coloring, knapsack, checkers) is unique.
- **The strict/lax spectrum.** Nobody has named the fundamental tradeoff. They describe symptoms (context explosion, attention degradation, isolation benefits) without the unifying framework.
