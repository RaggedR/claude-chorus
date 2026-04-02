# Twitter/X Browse Session #15 — 2026-03-17

## Summary
Major narrative shift: **topology/structure as THE problem** in multi-agent systems is now mainstream. Google DeepMind/MIT quantified it (17x error amplification), ACM launched an entire conference around it (CAIS 2026), and practitioners are loudly complaining about "bag of agents" failures. This is our categorical framework's moment — the field is screaming for the formalism we're building.

## Accounts Browsed

### EXISTING FOLLOWS

#### 1. @hardmaru (David Ha, Sakana AI)
- **Topic:** LLM + evolution, adversarial program evolution
- **Recent activity:** Two major threads:
  - **Digital Red Queen (DRQ):** Adversarial program evolution in Core War with LLMs. Co-evolutionary arms race produces convergent strategies across independent runs. Red Queen hypothesis applied to code evolution. Collaboration with MIT (Akarsh Kumar). Featured in Jack Clark's newsletter.
  - **Evolution Strategies at Scale:** Shared Gan/Miikkulainen paper showing ES outperforms PPO and GRPO for LLM fine-tuning at billion-parameter scale. 36.4% improvement over base vs 17.9% for PPO.
- **Key insight:** DRQ's convergent evolution across independent runs mirrors our domain-independence finding. Different initial conditions, same emergent structure.
- **Followers:** Large (800K+)
- **Status:** Existing follow

#### 2. @kenneth0stanley (Kenneth Stanley, Lila Sciences)
- **Topic:** Open-endedness, Scientific Superintelligence
- **Recent activity:** Open house event at Lila SF office on **March 18** (tomorrow!). Building open-endedness team. Hiring for pre-training, fine-tuning, RLHF, distillation, mechanistic interpretability, quality diversity.
- **Key insight:** Open-endedness framing: "creativity and open-endedness" as the elephant in the AI safety room. Two competing forces in AI: economic pressure for capability + need for alignment. $235M+ backing.
- **Followers:** ~150K
- **Status:** Existing follow

#### 3. @RobertTLange (Robert Lange, Sakana AI)
- **Topic:** ShinkaEvolve, LLM-driven program evolution
- **Recent activity:** ShinkaEvolve supported Unagi team's win in 2025 ICFP Programming Contest. System discovered efficient auxiliary variables for SAT solver. Framing: "scientific hypothesis testing as tree search."
- **Key insight:** ShinkaEvolve is open-source, competing with AlphaEvolve. The "hypothesis testing as tree search" framing is interesting — it's a structured search, not random mutation.
- **Status:** Existing follow

#### 4. @omarsar0 (Elvis, DAIR.AI)
- **Topic:** Agent community pulse, research curation
- **Recent activity (March 2026):** Extremely active. Key threads:
  - **"Can AI Agents Agree?"** (arXiv 2603.01213): Byzantine consensus fails in LLM agents even in benign settings. Valid agreement not reliable. Degrades as group size grows. Failures dominated by liveness loss (timeouts, stalled convergence).
  - **Theory of Mind in multi-agent LLMs:** BDI models + symbolic reasoning for agent coordination.
  - **Agent memory scaling:** Memex(RL) from Accenture — indexed experience memory for long-horizon tasks.
  - **Science Context Protocol (SCP):** "2026 is the year of advancing AI agents for scientific discovery."
  - **AGENTS.md files:** Tested across 124 PRs — results "a bit different from what" expected.
  - **Switched to Codex for proactive agents.** GPT-5.4 "going to level things up fast."
- **Key insight:** omarsar0 is the best single pulse-check for the agent community. Byzantine consensus failure = our FC degradation story told from distributed systems perspective.
- **Followers:** ~200K+
- **Status:** Existing follow

#### 5. @heathercmiller (Heather Miller)
- **Topic:** Agent composition, ACM CAIS 2026
- **Recent activity:** **MAJOR ANNOUNCEMENT** — Inaugural ACM Conference on AI and Agentic Systems (ACM CAIS 2026). San Jose, May 26-29. Paper deadline Feb 27 (past).
- **Key quote:** "Agents are now everywhere, compound AI systems have become the norm. The hard problems now are things like **how to compose agents**, how to optimize pipelines you can't differentiate through, and how to evaluate and debug systems that are inherently probabilistic."
- **Key insight:** ACM creating an entire conference around agent composition = our categorical composition work has a natural venue. "How to compose agents" IS the categorical question.
- **Status:** Existing follow

### NEW DISCOVERIES

#### 6. @raphaelmansuy (Raphael Mansuy)
- **Topic:** Multi-agent scaling, topology analysis
- **Recent activity:** Detailed thread on Google DeepMind/MIT "Towards a Science of Scaling Agent Systems" paper. Key finding: "only 10-20% of topologies significantly impact performance." Aggregating 5 parallel agents outperformed complex debate chains.
- **Key insight:** Excellent at distilling complex agent papers into actionable insights. His framing of the "Mass" framework (interleaving optimization stages) connects to our iterative composition.
- **Followers:** Unknown
- **Worth following:** YES — consistent, analytical multi-agent topology commentary

#### 7. @zhuokaiz (Zhuokai Zhao)
- **Topic:** Agent architecture retrospective
- **Recent activity:** "First article on X" — deep dive into agent architecture 2025-2026. TL;DR: "the core agent loop converged, but everything around it diverged. More traditional multi-agent might be back but it's complicated."
- **Key insight:** "Core loop converged, periphery diverged" = the composition problem. If the node is solved, the graph structure is what matters now. Exactly our thesis.
- **Followers:** Unknown
- **Worth following:** YES — thoughtful architectural analysis, not hype

#### 8. @krishnanrohit (Rohit Krishnan)
- **Topic:** Agent nodes, composition, risk surfaces
- **Recent activity:** "An agent + sub-agents is the new 'node' that matters... the surface area of interactions with the real world has exploded, and this is going to be the new battlefield for risks, and reward, from AI in 2026."
- **Key insight:** "Agent + sub-agents = new node" is the categorical composition insight stated in practitioner language. The node isn't the model, it's the composed agent.
- **Followers:** Unknown (likely moderate)
- **Worth following:** YES — bridges theory and practice on composition

#### 9. @dippatel1994 (Dipkumar Patel)
- **Topic:** ICLR 2026 multi-agent research curation
- **Recent activity:** Highlighted 14 ICLR 2026 papers focusing on real-world multi-agent production challenges.
- **Key insight:** ICLR 2026 accepted nearly 5,000 papers with substantial multi-agent failure analysis representation.
- **Worth following:** MAYBE — good curation but may be one-off

#### 10. @AndrewZeng17 (Weihao Zeng)
- **Topic:** Long-horizon agent evaluation, LOCA-bench
- **Recent activity:** LOCA-bench — benchmark for long-context, long-horizon agents. "Even with 100K-1M token windows, reliability degrades — plans drift, constraints are forgotten, exploration collapses."
- **Key insight:** Context window scaling doesn't solve coordination. The problem is structural, not capacity. Echoes our "architecture > models" finding.
- **Worth following:** YES — rigorous evaluation perspective

## KEY PAPERS DISCOVERED

### 1. "Towards a Science of Scaling Agent Systems" (arXiv 2512.08296)
- **Authors:** Google DeepMind + MIT
- **Key numbers:**
  - Independent agents: 17.2x error amplification
  - Centralized coordination: 4.4x error amplification (circuit breaker effect)
  - 180 configurations, 5 architectures, 3 LLM families
  - Performance degrades up to 70% by adding agents
  - Saturation threshold: gains plateau beyond 4 agents
- **3 dominant effects:** Tool-coordination trade-off, capability saturation, topology-dependent error amplification
- **RELEVANCE TO US:** This is the empirical complement to our categorical framework. They measure what we formalize. Their "topology-dependent error amplification" IS our laxator in practitioner language.

### 2. "Can AI Agents Agree?" (arXiv 2603.01213)
- **Published:** March 2026
- **Key finding:** Byzantine consensus is NOT a reliable emergent capability of LLM agents. Degrades with group size.
- **RELEVANCE TO US:** Fully-connected topology fails at coordination — our FC degradation result from a distributed systems angle.

### 3. "Evolution Strategies at Scale" (arXiv 2509.24372)
- **Authors:** Gan, Miikkulainen et al.
- **Key finding:** ES outperforms PPO and GRPO for LLM fine-tuning. First billion-parameter ES fine-tuning without dimensionality reduction. 36.4% improvement vs 17.9% PPO.
- **RELEVANCE TO US:** Evolution as first-class optimization method for LLMs = more data point for strict/lax. ES = population-based = lax.

### 4. "17x Error Trap" / Bag of Agents (Sean Moran, TDS)
- **Key argument:** Flat topology (every agent talks to every other) = 17.2x error amplification. Solution: arrange agents into "functional planes."
- **RELEVANCE TO US:** "Functional planes" = our categorical composition. "Bag of agents" = our fully_connected topology. Their anti-pattern IS our worst-performing topology.

## TRENDING TOPICS

1. **TOPOLOGY AS THE PROBLEM** — The single biggest narrative shift. Google DeepMind/MIT quantified topology-dependent error amplification. Sean Moran coined "bag of agents." ACM launched CAIS 2026. Heather Miller: "how to compose agents" is THE hard problem. Everyone is saying what we've been formalizing.

2. **AGENT MEMORY FOR LONG-HORIZON** — Microsoft, Accenture, multiple groups all attacking the memory scaling problem. Memex(RL), SimpleMem, MEM1. Context windows aren't enough. Structural memory > bigger windows.

3. **BYZANTINE CONSENSUS IN LLM AGENTS** — "Can AI Agents Agree?" paper shows consensus degrades with group size. Practitioners discovering that more agents =/= better coordination. BlockAgents proposes blockchain solutions.

4. **EVOLUTIONARY AI MAINSTREAMING** — DRQ (Sakana/MIT), ShinkaEvolve, AlphaEvolve, ES at Scale. Evolution is no longer niche — it's competitive with RL for fine-tuning. Open-endedness has institutional backing ($235M Lila).

5. **ICLR 2026 MULTI-AGENT FOCUS** — Nearly 5,000 papers, with significant multi-agent failure/coordination representation. "The Multi-Agent Trap" entering mainstream vocabulary.

## NARRATIVE SHIFTS SINCE BROWSE #14 (March 15)

### New since last browse:
- **ACM CAIS 2026 ANNOUNCED** — First dedicated conference for agent composition. This didn't exist 2 days ago.
- **"Can AI Agents Agree?" published** — Byzantine consensus failure paper is brand new (March 2026).
- **Kenneth Stanley's Lila open house TOMORROW** (March 18). Active hiring.
- **Agent memory as separate problem class** — Was implicit before, now explicit with Memex(RL), LOCA-bench, multiple simultaneous papers.
- **"The core agent loop converged, periphery diverged"** (@zhuokaiz) — This crystallizes the narrative: the node is solved, the graph is the problem.

### Strengthened since last browse:
- "Architecture > Models" is now the DOMINANT narrative (was "emerging consensus" in browse #14).
- Topology/composition framing went from "some people are talking about it" to "Google DeepMind published a quantitative paper and ACM created a conference."
- Evolutionary AI: DRQ convergent evolution across independent runs = new evidence for domain-independence.

## WHAT PRACTITIONERS ARE COMPLAINING ABOUT

1. **Error cascading in production.** 17x amplification in unstructured multi-agent systems. Small hallucination becomes confident nonsense downstream.
2. **Latency from sequential execution.** 4 agents = 4x response time. Parallel topology needed but coordination is hard.
3. **Memory degradation.** Agents lose track of what they've tried on long-horizon tasks. 100K-1M tokens isn't enough.
4. **Token costs spiking.** Coordination tax eats context window. More agents = less room for actual reasoning.
5. **Byzantine failures.** Consensus not reliable even in benign settings. Degrades with group size.
6. **No good evaluation.** LOCA-bench is response to "we can't even measure this properly."

## ACCOUNTS TO FOLLOW (NEW)

1. **@raphaelmansuy** — Analytical multi-agent topology commentary. Distills DeepMind papers clearly.
2. **@zhuokaiz** — Thoughtful agent architecture retrospective. "Core loop converged, periphery diverged."
3. **@krishnanrohit** — "Agent + sub-agents = new node." Bridges theory and practice.
4. **@AndrewZeng17** — LOCA-bench. Rigorous long-horizon agent evaluation.
5. **@dippatel1994** — ICLR 2026 curation. (Lower priority — may be one-off.)

## CONNECTIONS TO OUR WORK

| Their Language | Our Formalism |
|---|---|
| "Bag of agents" | Fully-connected topology |
| "Functional planes" | Categorical composition |
| "Topology-dependent error amplification" | Laxator magnitude |
| "17x error / 4.4x error" | None (17x) vs centralized coordination |
| "Core loop converged, periphery diverged" | Morphisms solved, composition is the problem |
| "How to compose agents" | Kleisli composition |
| "Byzantine consensus fails with scale" | FC degradation / strict collapse |
| "Agent + sub-agents = new node" | Objects in our category |
| "Architecture > Models" | Functors > objects |
| "Convergent evolution across runs" | Domain independence (topology determination) |
