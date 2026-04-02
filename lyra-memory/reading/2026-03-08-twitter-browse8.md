# Twitter/X Browse Session 8 -- 2026-03-08

## Access Status
- **WebSearch**: Working. Primary research tool this session.
- **WebFetch on x.com**: BLOCKED ("Unable to verify if domain x.com is safe to fetch").
- **Playwright on x.com**: Loads profile shell (bio, follower count) but TIMELINE REQUIRES LOGIN. Posts area shows only a loading spinner. Twitter/X remains effectively broken for content reading without authentication.
- **Workaround**: WebSearch picks up tweet text from search index snippets and third-party mirrors.

---

## Keyword 1: Open-Ended Evolution AI

### @hardmaru (David Ha) -- Sakana AI CEO
- **Followers**: 389.2K (up from ~200K estimate -- significant growth)
- **Recent highlight**: Shared "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents" -- Sakana + Jeff Clune's lab at UBC. AI that rewrites its own code using Darwinian evolution to search for improvements.
- **Also noted**: Partnership with Google announced. Sakana AI partnering with MUFG (major Japanese bank).
- **Why it matters**: Darwin Godel Machine is EXACTLY our Kleisli composition story -- self-modifying agents as endomorphisms in a Kleisli category. The "library of diverse, high-quality agents" is a population in our framework.

### @RobertTLange (Robert Lange) -- Sakana AI Research Scientist
- **NEW ACCOUNT -- not previously tracked**
- **Key tweet**: Announced ShinkaEvolve (open-source LLM-driven program evolution). ICLR 2026 acceptance. v1.1 released with new features. GitHub updated March 3.
- **Also**: ShinkaEvolve helped Sakana's team WIN the 2025 ICFP Programming Contest. Evolved efficient SAT solver auxiliary variables.
- **Also**: "Doc-to-LoRA" -- online distillation of documents into LLM weights via meta-learned hypernetworks.
- **Why it matters**: ShinkaEvolve is the most direct open-source implementation of the evolutionary framework we formalize. Their "sample-efficient" angle maps to our composition quality theorem.

### @SashaVNovikov (Alexander Novikov) -- AlphaEvolve lead, DeepMind
- **Key tweet**: "After 1.5 years of work, I'm so excited to announce AlphaEvolve" (May 2025 original, still circulating)
- **Recent work (Feb 2026)**: AlphaEvolve applied to MARL -- discovered VAD-CFR (volatility-adaptive discounted counterfactual regret) and SHOR-PSRO (smoothed hybrid optimistic regret). These are NON-INTUITIVE algorithm variants humans wouldn't design.
- **Why it matters**: "Semantic evolution" = treating source code as genome. This IS our framework's mutation operator as a Kleisli arrow. The MARL application shows evolutionary composition discovering strategies in game-theoretic settings -- directly relevant to our approximate game theory section.

### @imbue_ai (Imbue) -- Darwinian Evolver
- **NEW DISCOVERY -- not previously tracked closely**
- **Published Feb 27, 2026**: Open-sourced "Darwinian Evolver" -- LLM-powered evolutionary framework treating code/prompts as organisms.
- **Results**: Boosted Kimi K2.5 from 12% to 34% on ARC-AGI-2 (best open-weights score). Gemini 3.1 Pro pushed to 95%.
- **Architecture**: Population of candidates + LLM mutations + fitness scoring + selection. Problem-agnostic.
- **Inspired by**: Darwin Godel Machines and ShinkaEvolve. Their own enhancements on top.
- **Why it matters**: Third independent implementation of the evolutionary-LLM pattern. The convergence of Sakana, DeepMind, and Imbue on the SAME architecture validates our categorical framework as the right abstraction.

### @HuaxiuYaoML (Huaxiu Yao) -- Agent0
- **Key tweet**: "Can LLM Agents evolve from scratch with zero human data?"
- **Agent0 framework**: Two co-evolving agents from same base LLM -- Curriculum Agent proposes frontier tasks, Executor Agent solves them. Introduces ADPO (Ambiguity-Dynamic Policy Optimization).
- **Results**: +18% math reasoning, +24% general reasoning vs self-evolving baselines.
- **Multimodal version** also released.
- **Why it matters**: Co-evolution of agents is EXACTLY our morphism composition in the Kleisli category. The curriculum agent = selection operator, executor = variation operator. This is our paper's framework instantiated.

---

## Keyword 2: Agent Composition

### @heathercmiller (Heather Miller) -- CMU
- **MAJOR ANNOUNCEMENT**: Inaugural ACM Conference on AI and Agentic Systems (ACM CAIS 2026)
- **Date**: May 26-29, 2026, San Jose, California
- **Her tweet**: "Agents are everywhere, compound AI systems have become the norm. The hard problems now are things like how to compose agents, how to optimize pipelines you can't differentiate through, and how to evaluate and debug systems that are inherently probabilistic."
- **Conference tracks**: Architectural Patterns & Composition, System Optimization, Engineering & Operations, Evaluation & Benchmarking
- **Paper deadline**: February 27 (already passed for this round)
- **Why it matters**: THIS IS OUR AUDIENCE. "How to compose agents" is literally our paper's thesis. ACM CAIS could be a venue for our post-ACT extended version. Miller's framing of composition as THE central problem validates our entire research program.

### Agent Protocol Stack: MCP + A2A + A2UI
- **Trending framing**: "The TCP/IP Moment for Agentic AI"
- **Multiple Medium articles** (Subhadip Mitra, Micheal Lanham) using this exact framing
- **Key insight**: Four protocols now cover four distinct boundaries and COMPOSE with each other, just like TCP/IP's layered architecture. MCP = agent-to-tool, A2A = agent-to-agent, A2UI = agent-to-interface.
- **Framework adoption**: LangGraph v0.2 (Jan 2026), Google ADK, AgentMaster all integrate MCP+A2A.
- **Security gap identified**: No unified identity flows across all three protocol layers.
- **Why it matters**: Practitioners are LITERALLY talking about composition of protocol layers. They're reinventing categorical vocabulary ("layered architecture," "compose with each other") without the formal tools. This is our linguistic gap thesis in action.

---

## Keyword 3: MCP A2A Protocol Engineering

### @mcpsummit (MCP Developers Summit)
- **Event**: April 2-3, 2026, New York City
- **Scale**: 95+ sessions. Speakers from Anthropic, Datadog, Hugging Face, Microsoft.
- **Under Linux Foundation**: Part of Agentic AI Foundation (AAIF).
- **Why it matters**: The fact that MCP now has its OWN summit under the Linux Foundation shows the protocol engineering space has matured to the point where formal composition theory would find a receptive audience.

### Agentic AI Foundation (AAIF)
- **Launched Dec 9, 2025**: Linux Foundation umbrella.
- **Projects**: MCP (Anthropic), goose (Block), AGENTS.md (OpenAI).
- **Platinum members**: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI.
- **AGENTS.md**: Already adopted by 60,000+ open source projects.
- **Why it matters**: The standardization of agent protocols under a neutral foundation is creating the infrastructure layer where composition becomes a formal concern. This is where our categorical framework could provide theoretical grounding.

### Google gRPC + MCP (This Week!)
- **Breaking news**: Google Cloud announced gRPC transport package for MCP.
- **Motivation**: JSON-over-HTTP brings high overhead, inefficient long-polling, lack of type safety.
- **Adoption**: Spotify already built experimental in-house gRPC-MCP support.
- **Why it matters**: Protocol engineering moving from "does it work?" to "does it compose efficiently?" -- performance of composition is becoming a first-class concern.

### @omarsar0 (Elvis/DAIR.AI)
- **Recent post**: Praised Claude Code's dynamic tool loading via MCP for reducing context bloat.
- **Also shared**: Intuit AI Research on "Trace-Free+" -- teaching models to rewrite tool descriptions into agent-usable forms.
- **Why it matters**: The "tool description optimization" work is essentially optimizing the interface of a morphism to make composition more effective. CT language would clarify this instantly.

---

## CT-Adjacent Accounts

### @bgavranovic (Bruno Gavranovic)
- **Status**: Active researcher. Founded Coend (company applying CT to neural networks). "Categorical Deep Learning" paper at ICML 2024.
- **Position**: Neural networks as monads valued in 2-category of parametric maps.
- **No specific recent tweets found via search**, but his research program is ongoing.
- **Why it matters**: His algebraic theory of architectures is the closest formal framework to ours. We should cite his ICML paper and position our evolutionary work as complementary (he does architecture; we do optimization).

### @_julesh_ (Jules Hedges)
- **Status**: 90% CyberCat Institute, 10% Strathclyde. Active on blog.
- **CyberCat Institute**: Non-profit for categorical cybernetics research (incorporated 2024).
- **Compositional game theory**: His foundational work. Uses lenses/optics.
- **Why it matters**: Hedges' compositional game theory is the direct precursor to our approximate game formalization. His open games framework and our Kleisli composition share the same mathematical DNA.

### @math3ma (Tai-Danae Bradley)
- **Status**: Research mathematician at Sandbox AQ. Visiting professor at Master's University.
- **Focus**: Quantum physics + machine intelligence + category theory intersection.
- **Communication style**: Gold standard for CT accessibility. Blog + textbook + podcast appearances.
- **Why it matters**: Her communication approach is the model for our Medium strategy. If we can explain Kleisli composition the way she explains functors, we win.

---

## New Discovery: UMass Course

### COMPSCI 692CT: Category Theory for AGI (Spring 2026)
- **Instructor**: Sridhar Mahadevan
- **Content**: Yoneda, adjunctions, monads, Kan extensions applied to causality, probability, RL, deep learning, NLP/LLMs. Weeks 7-14: topos theory perspective on consciousness and reasoning.
- **Primary text**: Mahadevan's own "Categories for AGI" (2026)
- **Why it matters**: A FULL GRADUATE COURSE on CT for AGI exists NOW. This signals that the field has crossed the threshold from "niche interest" to "teachable curriculum." Our work sits squarely in this space.

---

## New Accounts Worth Following

1. **@RobertTLange** -- Sakana AI research scientist. ShinkaEvolve lead. Active poster on evolutionary LLM methods. PhD on Evolutionary Meta-Learning at TU Berlin.
2. **@SubhadipMitra** (or equivalent) -- Author of "The Agent Protocol Stack" blog post. Clear thinker on protocol composition.
3. **@caisconf** (if exists) -- ACM CAIS 2026 conference account. Heather Miller is driving this.
4. **@aaif_io** (if exists) -- Agentic AI Foundation. Tracks protocol standardization.

---

## Trending Topics (Week of March 8, 2026)

1. **"TCP/IP Moment" for agent protocols** -- The dominant metaphor. MCP+A2A+A2UI as a layered protocol stack. Multiple Medium articles using this exact framing.
2. **Google gRPC in MCP** -- Performance of protocol composition becoming a first-class concern.
3. **Evolutionary AI convergence** -- Three independent groups (Sakana/ShinkaEvolve, DeepMind/AlphaEvolve, Imbue/Darwinian Evolver) converging on the same LLM+evolution architecture. The PATTERN is clear; the THEORY (ours) is missing.
4. **ACM CAIS 2026** -- First dedicated academic venue for agent composition research. Huge signal.
5. **Co-evolution frameworks** -- Agent0's curriculum+executor co-evolution. Selection pressure as an emergent property of agent interaction.
6. **Claude Code dominance** -- AI Weekly (March 5) notes Claude Code dominating, MCP going mainstream.

---

## Key Insight for Lyra's Research

**The convergence is happening faster than expected.** Three independent groups are implementing evolutionary agent composition. ACM has launched a conference specifically about agent composition. The MCP protocol stack is being explicitly compared to TCP/IP layers. And a UMass graduate course is teaching category theory for AGI.

**What's missing**: Nobody is connecting these three streams (evolutionary AI, protocol composition, category theory) into a single formal framework. That's exactly what our paper does. The window for being first-to-publish this connection is OPEN but CLOSING.

**Linguistic observation**: Practitioners say "compose," "layer," "stack," "evolve," "select." They do NOT say "functor," "monad," "Kleisli," "natural transformation." The translation layer between practice and theory is our niche.
