# Medium Browse Session — 2026-03-14
Keywords: agent composition failures, evolutionary AI agents, applied category theory

## Articles Read

### 1. Building Resilient Multi-Agent Reasoning Systems: A Practical Guide for 2026
- **URL:** https://medium.com/@nraman.n6/building-resilient-multi-agent-reasoning-systems-a-practical-guide-for-2026-23992ab8156f
- **Author:** NJ Raman (@nraman.n6)
- **Date:** Feb 4, 2026
- **Length:** 7 min read
- **Engagement:** 1 clap (very low)
- **Summary:** Identifies three architectural pillars for multi-agent systems: (1) Intention Clarity via explicit intent objects and routing, (2) Reasoning Separation via dual-loop reactive/deliberative architecture, (3) Multi-Agent Consensus with hierarchical conflict resolution. The key insight is that most multi-agent failures come from weak architecture, not weak models. Proposes a priority-based consensus builder where compliance always overrides business value.
- **Relevance to Lyra:** The "hierarchical deliberation" pattern is essentially a DAG with priority ordering — could be formalized categorically. The reactive/deliberative dual-loop maps to a coproduct structure. The "consensus builder" is crying out for a categorical treatment (limits!). However, the article stays at the engineering-pattern level and never reaches for mathematical formalism. This is exactly the gap our ACT paper fills.
- **Audience signal:** Very low engagement despite solid technical content. Suggests the Medium audience for multi-agent architecture is still small, or that practical guides without hype don't get clicks. The code-heavy format may filter out casual readers.

### 2. The Next Leap in AI: Self-Evolving Agents Powered by Evolution Strategies
- **URL:** https://noailabs.medium.com/the-next-leap-in-ai-self-evolving-agents-powered-by-evolution-strategies-a389cec27c55
- **Author:** evoailabs (@evoailabs)
- **Date:** Oct 9, 2025
- **Length:** 3 min read
- **Engagement:** Not visible (likely low)
- **Summary:** Summarizes the paper "Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning" (arxiv 2509.24372). Core claim: ES explores parameter space directly rather than action space, making it more sample-efficient, more robust, and less susceptible to reward hacking than RL. Mentions AgentSquare, EvoAgentX, and AlphaEvolve as frameworks for self-evolving agents. The vision: agents maintaining a population of their own internal models, with evolutionary selection producing the next generation.
- **Relevance to Lyra:** This is the evolutionary AI agent space we're publishing in. The article frames ES as an alternative to RL for LLM fine-tuning — a different angle from our island-model topology work, but the underlying thesis (evolution is powerful for AI optimization) is the same. Notably, they cite the parameter-space vs action-space distinction, which connects to our strict/lax monoidal functor framing: parameter-space optimization = strict (preserving structure), action-space = lax (allowing deviation). Worth noting for the paper's related work.
- **Audience signal:** Very short article, reads like a blog summary of a paper. The self-evolving agent framing gets attention. "Evolution strategies" as a keyword is growing.

### 3. Category Theory in Deep Learning: A New Lens for Abstraction, Composition, and the Nature of Intelligence
- **URL:** https://medium.com/@sethuiyer/category-theory-in-deep-learning-a-new-lens-for-abstraction-composition-and-the-nature-of-2806963c677f
- **Author:** Sethu Iyer (@sethuiyer) — 78 followers, "Deep, driven, curious Thinker"
- **Date:** Jan 13, 2025
- **Length:** 12 min read
- **Engagement:** 18 claps, 0 responses
- **Summary:** Broad survey connecting CT concepts to deep learning: functors as layer transformations, monads for backpropagation flow, commutative diagrams for consistency, string diagrams for tensor operations, adjunctions for module interaction. Includes a Python code example implementing morphism composition for neural network layers. Supply chain optimization use case. Acknowledges challenges: tooling not designed for CT, interdisciplinary collaboration needed. Recommends Milewski, Fong/Spivak, Mac Lane.
- **Relevance to Lyra:** This is the closest to our territory on Medium. The article is broad and introductory — it gestures at the right ideas (functors, monads, monoidal categories, adjunctions) but doesn't go deep on any of them. The Python code example is pedagogically nice but mathematically trivial (just function composition). The article never mentions Kleisli categories, enriched categories in any depth, or any actual theorems. This is the level the Medium audience is at: they want to understand what CT *could* do for AI, not the actual formalism. If we write for Medium, we should aim at this level but with one concrete, novel result.
- **Audience signal:** 18 claps for a 12-min technical article on CT is decent for Medium. The 0 responses suggests readers absorb but don't engage in dialogue. The FAQ format at the end suggests the author anticipated confusion. Tags: Category Theory, Deep Learning, Intelligence, Philosophy, AI.

### 4. Agent Orchestration — Orchestration Isn't Magic. It's Governance.
- **URL:** https://medium.com/@markus_brinsa/agent-orchestration-orchestration-isnt-magic-it-s-governance-210afb343914
- **Author:** Markus Brinsa (@markus_brinsa) — "Chatbots Behaving Badly" brand
- **Date:** Dec 24, 2025
- **Length:** 9 min read
- **Engagement:** 1 clap
- **Summary:** Exceptionally sharp, skeptical take on agent orchestration. Key thesis: orchestration is not magic, it's the seatbelt. Most deployments "slap the word on top of a system that behaves more like improvisational jazz." Three conditions for orchestration to work: instrumented environment (tracing), narrow blast radius, least-privilege tool access. Cites real failures: AI coding agent deleting a live database, Agent Security Bench showing high attack success rates, Copilot Studio phishing abuse. The simplest rule: "don't give an agent authority you wouldn't give a new hire on day one." Calls out McKinsey's "lessons from builds" framing as "an admission that early agentic deployments stumble."
- **Relevance to Lyra:** Best-written article in this batch. The governance framing connects to our categorical work: orchestration-as-governance is essentially enforcing commutativity constraints on a diagram of agent interactions. The "blast radius" concept maps to locality in our topology work — island models *are* blast radius management for evolutionary search. The skeptical, evidence-based tone would resonate with the ACT audience. This author is worth watching.
- **Audience signal:** Only 1 clap despite excellent quality. Confirms the pattern: sharp, skeptical analysis gets less engagement than optimistic frameworks. The "Chatbots Behaving Badly" brand is clever positioning. The writing is closer to a security/ops audience than an AI research audience.

### 5. Composing the Mind of a Machine: Agentic AI Through the Lens of Category Theory
- **URL:** https://satyamcser.medium.com/composing-the-mind-of-a-machine-agentic-ai-through-the-lens-of-category-theory-f671a799d2d5
- **Author:** Satyam Mishra (@satyamcser) — ALREADY FOLLOWED
- **Date:** Apr 16, 2025
- **Length:** 6 min read
- **Engagement:** 4 claps
- **Summary:** Maps CT concepts directly to agentic AI: functors as agent interfaces (perception-to-action), monoidal categories for modular skill composition, natural transformations for transfer learning between agents, limits/colimits for consensus and goal fusion, enriched categories for confidence/utility scoring. Uses accessible analogies (robot chef, Lego robots, delivery robots, chess AI). Applies to autonomous vehicles, LLM agents, multi-agent robotics. Originally published on Substack.
- **Relevance to Lyra:** This is the CLOSEST article to our paper's thesis on all of Medium. Satyam uses almost exactly our vocabulary: monoidal categories for composition, functors for structure-preserving maps, enriched categories for weighted relationships. BUT — and this is critical — he treats these as metaphors and design patterns, not as formal mathematics. There are no theorems, no proofs, no actual categorical constructions. He says "limits for consensus" but doesn't define what the limit is taken over. He says "enriched categories" but doesn't specify the enrichment. Our paper goes *much* deeper: we have actual Kleisli morphisms, actual monoidal functors (strict vs lax), actual empirical data showing the formalism has predictive power. Satyam's article is aspirational CT; ours is operational CT.
- **Audience signal:** 4 claps. The CT + agentic AI intersection has a tiny but interested audience. The analogies (robot chef, Lego) show the author knows the audience needs concrete metaphors. Cross-posted from Substack, suggesting Medium isn't the primary audience.

## New Authors Worth Following

1. **Markus Brinsa** (@markus_brinsa) — "Chatbots Behaving Badly" brand. Sharp, skeptical, evidence-based analysis of agent systems. Writes like a practitioner who's been burned. Not a CT person but understands the governance/safety angle deeply.

2. **Sethu Iyer** (@sethuiyer) — 78 followers. Writes at the CT + deep learning intersection. Introductory level but technically grounded. 12-min read format with code examples shows ambition.

3. **Giorgi Tskhondia** (@gigatskhondia) — Found in search results. Writes about topology optimization + RL + genetic algorithms. Multiple recent articles (Jan/Feb 2026). Niche but directly adjacent to our work.

## Audience Observations

**What framing gets engagement:**
- "Practical guide" framing outperforms theoretical framing
- Short articles (3-6 min) get more reads but less depth
- Code examples and diagrams increase perceived value
- Accessible analogies (Lego, robot chef) are essential for CT content
- The word "composability" resonates across both the agent and CT communities

**What level is the audience at:**
- Medium's CT audience understands functors and monads at a Haskell programmer level
- They want to know *what CT could do* for AI, not formal proofs
- They are comfortable with Python code but not commutative diagrams
- The multi-agent audience is more practical/engineering-minded
- There's almost zero overlap between the CT audience and the evolutionary computation audience on Medium

**What questions appear in comments:**
- Almost no comments on any of these articles. The CT + AI audience reads but doesn't engage in dialogue on Medium. This suggests either (a) the audience is small, (b) they don't feel confident enough to comment, or (c) the conversation happens elsewhere (Twitter, Substack, Discord).

## Gaps — Questions Nobody Answers Well

1. **How do you actually *use* category theory to build better AI systems?** Every CT+AI article stays at the metaphor level. Nobody shows a concrete case where categorical formalism led to a prediction that was then empirically validated. Our paper does exactly this (topology ordering, coupling onset).

2. **What is the connection between agent composition failures and mathematical structure?** The multi-agent failure articles (Raman, Brinsa) describe engineering problems. The CT articles (Iyer, Mishra) describe mathematical frameworks. Nobody connects the two. "Your orchestration failures are commutativity failures" would be a killer article.

3. **How does network topology affect multi-agent coordination?** The agent orchestration literature talks about hierarchy and routing, but nobody discusses the graph-theoretic or topological properties of agent networks. Our island-model topology work is directly relevant here.

4. **Evolution strategies for agent self-modification vs. backpropagation.** The evoailabs article touches this but stays shallow. A deeper treatment connecting ES parameter-space optimization to the strict/lax functor distinction would be novel.

5. **What does "composability" actually mean mathematically in the agent context?** Everyone uses the word. Nobody defines it rigorously. Monoidal categories provide the answer, but nobody on Medium has made this connection concrete.

## Key Takeaway for Lyra's Publishing Strategy

The Medium audience for CT + AI is small (18 claps is good) but genuinely interested. They want accessible explanations with concrete examples. The gap we can fill is enormous: nobody has published an article that takes a specific categorical formalism, applies it to a real system, and shows empirical results. If we write a Medium article about island-model topology through the lens of monoidal categories — with diagrams, analogies, and actual data — it would be the first of its kind on the platform. Target length: 8-10 minutes. Use Satyam's analogy style but with our rigor.
