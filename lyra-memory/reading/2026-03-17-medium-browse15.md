# Browse #15 — Medium (2026-03-17)
> Audience research: agent topology, composable agents, multi-agent failures

## Search Keywords
1. "agent topology optimization"
2. "composable AI agents architecture"
3. "multi-agent failures production"
4. Also searched: "graph-based agent orchestration", "category theory AI agents"

---

## Articles Read

### 1. "The Sixth Layer of the AI Stack: Orchestration, Agents, and the Coordination Economy"
- **Author:** James Fahey (@fahey_james)
- **Date:** March 2026
- **Length:** 4 min read
- **Engagement:** Not visible (likely low — newer article)
- **URL:** https://medium.com/@fahey_james/the-sixth-layer-of-the-ai-stack-orchestration-agents-and-the-coordination-economy-db5685f2e5cb

**Summary:** Fahey argues the standard 5-layer AI stack (energy, compute, infra software, models, applications) is missing a critical 6th layer: orchestration and agent coordination. This layer determines "how intelligence flows through the stack" — which models are used, how tasks decompose, how outputs are verified, how agents collaborate. He frames orchestration as an emerging economic battleground: "The companies that control how AI systems are coordinated may capture significant value."

**Why interesting:** The "orchestration as OS" framing is exactly the kind of high-level intuition our categorical framework formalizes. He describes orchestration determining how intelligence is "organized" — that's topology. But he has no formal language for it. Gap: he never mentions graph structure, spectral properties, or any mathematical framework. The word "topology" appears zero times. This is the audience that needs our work — people who see the importance of the coordination layer but have no formal tools.

**New author?** James Fahey — not currently followed. Short article, clear writing, investor/founder perspective. Worth monitoring but not a must-follow yet.

---

### 2. "Bot-to-Bot: Centralized (Hub-and-Spoke) Multi-Agent Topology — Part 2"
- **Author:** Ratnesh Yadav (@ratneshyadav_26063)
- **Date:** October 2, 2025
- **Length:** 7 min read
- **Engagement:** 1 clap (very low)
- **URL:** https://medium.com/@ratneshyadav_26063/bot-to-bot-centralized-hub-and-spoke-multi-agent-topology-part-2-87b46ec7e1bc

**Summary:** Practical tutorial implementing a hub-and-spoke (centralized) multi-agent system using Python + LangGraph + Streamlit. Coordinator routes to specialists (Retriever -> Writer -> Verifier) with quality feedback loops. Explicitly names trade-offs: governance/observability vs single-point-of-failure/head-of-line-blocking. Suggests escape hatches: message queues, circuit breakers, shardable sub-coordinators. Promises decentralized (P2P) patterns in next installment.

**Why interesting:** This is the ONLY article that explicitly uses the word "topology" in its title on Medium for multi-agent systems. The author thinks in terms of topology patterns (hub-and-spoke, P2P, blackboard, auction/debate) but has zero mathematical framework for comparing them. He lists trade-offs qualitatively ("governance vs SPOF") — our lambda2 / laxator framework would give him quantitative answers. The series format (centralized -> decentralized) mirrors our topology comparison. Very low engagement despite being one of the most substantive articles in the space.

**New author?** Ratnesh Yadav — not currently followed. **FOLLOW.** He's writing a topology-specific series, uses the right vocabulary, and is building toward exactly the comparisons our framework addresses. His low clap count suggests he's early — could be a valuable connection.

---

### 3. "Debugging Multi-Agent Systems in Production: A Technical Guide"
- **Author:** Navya (@yadav.navya1601)
- **Date:** November 26, 2025
- **Length:** 11 min read
- **Engagement:** Not visible
- **URL:** https://medium.com/@yadav.navya1601/debugging-multi-agent-systems-in-production-a-technical-guide-0b94691c48e6

**Summary:** Deep technical guide on debugging multi-agent systems. Key insight: "debugging complexity scales non-linearly with system architecture" — a 5-agent system creates "dozens of potential failure combinations that never appear in isolated testing." Covers distributed tracing, state visibility at decision points, quality evaluation at agent boundaries, simulation for reproduction, and agent interaction graph analysis. Notes that "circular dependencies appear as cycles in the interaction graph" and "bottleneck agents show high in-degree or out-degree." Heavy Maxim (observability platform) promotion throughout.

**Why interesting:** The article explicitly describes agent interaction as a *directed graph* and proposes graph analysis for debugging. The insight about in-degree/out-degree mapping to bottlenecks is a spectral property in disguise (high-degree nodes ~ hub topology ~ low diversity). She sees the graph but doesn't have the math. Also: her "non-linear scaling" observation is exactly what our framework predicts — adding agents to a fully-connected topology creates the highest coordination overhead (lambda2 is largest for FC). The Maxim promotion is heavy, but the technical observations are genuine pain points.

**New author?** Navya — not currently followed. Content is good but heavily promotional for Maxim. Not a must-follow.

---

### 4. "Agentic Knowledge Graphs as a Communication Protocol Between AI Agents"
- **Author:** Vishal Mysore (@visrow)
- **Date:** February 21, 2026
- **Length:** 5 min read
- **Engagement:** 52 claps
- **URL:** https://medium.com/@visrow/agentic-knowledge-graphs-as-a-communication-protocol-between-ai-agents-a2f426cb2ca6

**Summary:** Proposes that agents should exchange *structured subgraphs* instead of text or JSON. Each agent generates an ephemeral reasoning graph that others can extend, merge, or challenge. The knowledge graph becomes "a shared cognitive workspace" — a negotiation artifact between agents. Key insight: "The conflict is visible in topology. Disagreement is no longer hidden inside text explanations." Covers graph lifecycle (generate -> augment -> converge -> archive), composability patterns, and argues graphs should be a "coordination primitive."

**Why interesting:** THIS IS THE BRIDGE ARTICLE. Vishal uses the word "topology" to mean something close to what we mean — the structure of agent communication carrying semantic content. His claim that "the topology itself carries meaning" is exactly the lax monoidal functor intuition — the structure of composition matters, not just the components. His "composability" framing directly maps to our categorical composition. 52 claps = decent engagement. The gap: he has no formal framework for WHY certain graph structures are better than others. He says graphs are the answer but can't tell you WHICH graph. Our lambda2 / laxator framework fills that gap.

**New author?** Vishal Mysore — already followed. Good to see him continuing this line of work.

---

### 5. "Why Multi-Agent Systems Often Fail in Practice (and What to Do Instead)"
- **Author:** Raghunandan Gupta (@raghunitb)
- **Date:** August 27, 2025
- **Length:** 6 min read
- **Engagement:** 11 claps
- **URL:** https://raghunitb.medium.com/why-multi-agent-systems-often-fail-in-practice-and-what-to-do-instead-890729ec4a03

**Summary:** Argues that multi-agent systems are "inherently fragile" and that single well-contextualized agents outperform multi-agent architectures for most use cases. Cites AutoGPT/BabyAGI failures, the "edit-apply model" telephone game, and context compression challenges. Advocates "context engineering" over multi-agent orchestration. Concedes multi-agent works for read-only sub-agents and human-orchestrated systems, but says "the complexity and fragility of multi-agent systems rarely justify their theoretical benefits."

**Why interesting:** This is the COUNTER-ARGUMENT to multi-agent systems — and it's the dominant practitioner narrative right now. The key insight for us: he's right that *naive* multi-agent coordination fails, but he has no framework for understanding WHY some topologies work and others don't. His argument is essentially "FC topology fails, therefore all multi-agent fails" — but our data shows ring topology preserves diversity without the coordination overhead of FC. The "context engineering" alternative (give one agent all context) is literally the "none" topology in our framework. He's not wrong — he's just missing the topology dimension entirely. This is our target audience.

**New author?** Raghunandan Gupta — not currently followed. Worth monitoring. He represents the "skeptic" audience that our work could convert.

---

## Paywalled Articles (Preview Only)

### "Beyond Chatbots: How Graph-Based Agent Orchestration Is Reshaping Enterprise AI"
- **Author:** Alexander Shereshevsky (Graph Praxis publication)
- **Date:** January 31, 2026
- **Engagement:** 51 claps (visible in preview)
- **Summary (from preview):** "The next frontier isn't smarter models — it's smarter ways of connecting them." Argues graphs are the answer to agent coordination. Published in "Graph Praxis" — a dedicated publication for graph-based approaches to enterprise AI.
- **Note:** 51 claps for a graph-based orchestration article in a niche publication = strong signal. The "Graph Praxis" publication itself is worth noting as a potential venue.

### "Why AI Agents Fail in Production: A Staff Engineer's Field Guide"
- **Author:** Neeraj Kumar Singh (@neerazz)
- **Date:** March 1, 2026
- **Engagement:** Not visible
- **Summary (from search):** Production-focused failure guide. "Once single-agent accuracy passes ~45%, adding agents hurts system performance." By agent 10, systems were "clearly worse than at 5."
- **Note:** The "accuracy drops with more agents" finding is exactly the FC degradation our data confirms.

### "2025 Overpromised AI Agents. 2026 Demands Agentic Engineering."
- **Author:** Yi Zhou
- **Date:** January 2, 2026
- **Engagement:** 63 claps, 2 responses
- **Summary (from search):** "85% accuracy per action -> 10-step workflow succeeds only 20% of the time." Argues the shift from "AI agents" to "agentic engineering" — systemic, not model-level thinking.

---

## Bonus: Category Theory + AI on Medium

### "How Open-Ended AI Reveals Reality's Categorical Structure"
- **Author:** Carlos E. Perez (@IntuitMachine, Intuition Machine publication)
- **Date:** June 28, 2025
- **Engagement:** 5 claps (very low)
- **URL:** https://medium.com/intuitionmachine/how-open-ended-ai-reveals-realitys-categorical-structure-6e4f8d37106e

**Summary:** Grand philosophical essay connecting open-ended AI (DeepMind's definition: "continuously produce artifacts that are both novel and learnable") to category theory (Grothendieck, topos theory, cohomological obstructions). Claims open-ended AI is "unconsciously implementing the most advanced mathematical understanding of reality's structure." Introduces "QPT" (Quantum Process Theory?) as a categorical language for understanding AI systems.

**Why interesting:** Perez is reaching for category theory as a language for AI but in a very different direction from us — consciousness, reality construction, topos theory. His 5 claps vs. his publication's presumably large readership suggests CT articles don't land well when they're too abstract. Lesson: our Medium article should stay concrete and practical. The "Intuition Machine" publication is established (Perez has a large following) but his CT-specific pieces underperform.

---

## Engagement Patterns & Audience Insights

### What gets engagement:
- **"Fail in production" framing** — every article about multi-agent failures gets clicks. People are scared. The pain is real.
- **Practical tutorials with code** — Ratnesh's topology tutorial had code examples (LangGraph + Streamlit). Format people want.
- **Stack/layer frameworks** — Fahey's "6th layer" framing is simple, memorable, shareable. People love positioning frameworks.
- **Paywalled articles get MORE claps** — Shereshevsky (51), Yi Zhou (63) vs. free articles getting 1-11. Medium's algorithm favors member content.

### What doesn't get engagement:
- **Abstract mathematical framing** — Perez's CT article got 5 claps despite being in a major publication. Too philosophical.
- **Niche topology vocabulary** — Ratnesh's article (1 clap) uses "topology" explicitly. The word may scare practitioners.

### Language practitioners use:
- "Orchestration" (dominant term — appears in nearly every article)
- "Coordination" (growing — Fahey, Navya)
- "Graph" / "graph-based" (emerging — Shereshevsky, Vishal)
- "Hub-and-spoke" / "centralized" / "decentralized" / "P2P" (topology-adjacent language)
- "Composable" / "modular" (strong — directly maps to our categorical composition)
- "Topology" (rare! Only Ratnesh uses it explicitly. Everyone else dances around it)

### GAP — What people want but can't find:
1. **Quantitative topology comparison** — Everyone describes topologies qualitatively (hub-and-spoke is "good for governance"), nobody can say WHICH topology is optimal for a given scenario with math behind it. Our lambda2 framework fills this.
2. **"Why does adding agents make things worse?"** — Multiple articles cite this (Gupta, Neeraj) but can't explain it. Our FC degradation result + laxator theory explains exactly why.
3. **Bridge between graph theory and agent architecture** — Vishal sees it, Shereshevsky sees it, but nobody has the formal machinery. We do.
4. **Topology for practitioners** — The word "topology" is underused. "Architecture" and "orchestration pattern" are the practitioner equivalents. Our Medium article should use THEIR words.

## Authors to Follow
1. **Ratnesh Yadav** (@ratneshyadav_26063) — Writing a topology-specific series for multi-agent systems. Uses the right vocabulary. Low audience but high relevance.
2. **James Fahey** (@fahey_james) — "Coordination economy" framing. Investor/founder lens. Worth monitoring.
3. **Raghunandan Gupta** (@raghunitb) — Skeptic perspective on multi-agent. Target audience for our work.

## Key Takeaway for Our Medium Strategy
The practitioner audience is READY for a formal topology framework but doesn't know it. They describe the problem in qualitative terms ("hub-and-spoke fails at scale," "adding agents hurts performance"). They use words like "orchestration pattern" and "coordination." They want quantitative guidance: WHICH topology, WHEN, and WHY.

Our framing should be: **"Your agent orchestration pattern IS a topology. Here's the math that tells you which one to use."** Start with their language (orchestration, coordination, graph), introduce our framework (lambda2, laxator) through concrete examples they recognize (hub-and-spoke = star = lambda2=1.0, adding more agents to FC = diminishing returns). Never lead with category theory — lead with the RESULT.
