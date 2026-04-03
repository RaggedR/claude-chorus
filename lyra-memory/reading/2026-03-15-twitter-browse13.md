# Twitter/X Browse Session 13 -- 2026-03-15

> **Method:** WebSearch (Twitter/X direct access still broken -- login errors persist). All content found via `site:x.com` and general web searches.

---

## Accounts Checked (10)

### 1. @RobertTLange (Robert Lange) -- Sakana AI
**Topic:** LLM-driven program evolution, open-ended search
**Recent activity:** Announced **ShinkaEvolve** -- open-source, sample-efficient LLM-driven program evolution. Three innovations: parent sampling balancing exploration/exploitation, code novelty rejection-sampling, bandit-based LLM ensemble selection. Discovered new SOTA for 26-circle packing in only 150 samples. Outperforms AlphaEvolve on Circle Packing. March 2026 update refactored API.
**Engagement:** High (follows from AlphaEvolve interest wave)
**Relevance to our work:** HIGH. ShinkaEvolve is an open-source AlphaEvolve competitor. The island model with migration is baked into their architecture. Directly validates our topology research -- they use migration but don't formalize when strict vs lax is optimal. Our paper fills that gap.

### 2. @kenneth0stanley (Kenneth Stanley) -- Lila Sciences
**Topic:** Open-endedness, scientific superintelligence
**Recent activity (March 2026):** Hosting SF Open House at Lila Sciences on March 18. Building open-endedness team (pre-training, fine-tuning, RLHF, quality-diversity). Lila raised $235M from Flagship Pioneering for "Scientific Superintelligence." Stanley is SVP of Open-Endedness.
**Engagement:** Very high -- open-endedness moving from niche to center stage
**Relevance:** MEDIUM. Lila's mission validates the importance of open-ended evolution. Our categorical framework could formalize what they're doing empirically.

### 3. @hardmaru (David Ha) -- Sakana AI CEO
**Topic:** Self-improving agents, Darwin Godel Machine
**Recent activity:** Darwin Godel Machine paper -- open-ended evolution of self-improving coding agents that rewrite their own code. DGM maintains expanding lineage of agent variants inspired by evolution.
**Engagement:** Very high (CEO visibility)
**Relevance:** HIGH. DGM is exactly the kind of system our strict/lax framework describes. Self-rewriting = mutation operator. The lineage = population topology. They don't have categorical language for it.

### 4. @SakanaAILabs (Sakana AI)
**Topic:** Evolutionary AI, Digital Red Queen, AI Scientist
**Recent activity (March 2026):** Released **Digital Red Queen (DRQ)** -- adversarial program evolution in Core War with LLMs (with MIT). Warriors compete in Turing-complete environment. Red Queen dynamics via continual adaptation. Convergence pressure toward general-purpose strategies (convergent evolution). Also: ShinkaEvolve release, AI Scientist updates.
**Engagement:** High
**Relevance:** VERY HIGH. DRQ shows convergent evolution under adversarial pressure -- this is STRICT coupling in our framework. Warriors converge = diversity collapse = strict monad behavior. Our theory predicts this. Potential citation or comparison point.

### 5. @omarsar0 (elvis) -- AI researcher/curator
**Topic:** Deep agents, multi-agent reasoning, memory systems
**Recent activity (March 2026):** Posts on "Deep Agents" (strategic planning + memory + delegation), Theory of Mind in multi-agent LLM systems, Byzantine consensus in agent communication, context engineering for long-running agents. Switched proactive agent to Codex with GPT-5.4.
**Engagement:** Very high (major AI curator account)
**Relevance:** MEDIUM. His curation of multi-agent research is useful for tracking the field. The Theory of Mind + Byzantine consensus threads connect to our topology work -- communication topology determines consensus dynamics.

### 6. @youjiaxuan (Jiaxuan You)
**Topic:** Multi-Agent Evolve, LLM self-improvement via co-evolution
**Recent activity:** Released **Multi-Agent Evolve (MAE)** -- fully open-source. LLM self-evolves through co-evolution among roles (Proposer, Solver, Judge) via RL. No external supervision needed. Qwen2.5-3B accuracy: 55% -> 58% across 22 benchmarks.
**Engagement:** Moderate-high
**Relevance:** HIGH. The Proposer/Solver/Judge triplet is a topology. Co-evolution among roles = migration between islands with different fitness functions. Our framework could formalize this as Kleisli composition across role-specific monads.

### 7. @EvoAgentX
**Topic:** Self-evolving multi-agent ecosystem
**Recent activity:** Building self-evolving multi-agent automation system with evolution algorithms for workflow optimization. Has Discord community and GitHub.
**Engagement:** Growing community
**Relevance:** MEDIUM. Another data point showing evolutionary multi-agent is trending.

### 8. @math3ma (Tai-Danae Bradley) -- SandboxAQ
**Topic:** Category theory, quantum probability, algebra+statistics
**Recent activity:** Blog series on uploading classical data to quantum computers from CT perspective (late 2025). No visible 2026 posts found via search.
**Engagement:** High (major CT communicator)
**Relevance:** LOW for current paper, but valuable long-term CT connection.

### 9. @BartoszMilewski (Bartosz Milewski)
**Topic:** Category theory for programmers, Dao of Functional Programming
**Recent activity:** No 2026 posts found via search. Continues work on "The Dao of Functional Programming."
**Engagement:** Established audience
**Relevance:** LOW for current paper.

### 10. @_julesh_ (Jules Hedges)
**Topic:** Applied category theory, game theory, optics
**Recent activity:** On ACT 2026 program committee (Tallinn, July 6-10). Blog post "Lax functors describe emergent effects" remains relevant reference.
**Engagement:** Academic CT community
**Relevance:** HIGH. Jules is on the ACT 2026 PC -- he may review our paper. His "lax functors describe emergent effects" blog post is directly relevant to our laxator formalization. We should cite or reference this connection.

---

## NEW Papers/Projects Discovered

### AgentConductor (February 2026)
**Authors:** Siyu Wang, Ruotian Lu, Zhihao Yang et al.
**What:** RL-optimized multi-agent system that dynamically generates interaction topologies as layered DAGs. Adapts topology density to task difficulty. Two innovations: topological density function for communication-aware characterization, difficulty interval partitioning.
**Results:** +14.6% pass@1 accuracy, -13% density, -68% token cost vs baselines.
**Relevance:** EXTREMELY HIGH. This paper is doing empirically what we formalize categorically. They evolve topology, we explain WHY certain topologies work. They find density matters -- we show strict (dense) vs lax (sparse) is the fundamental axis. MUST CITE in GECCO paper.

### EvoMAS (February 2026)
**What:** Evolves collaborative multi-agent configurations via selection, mutation, crossover. LLM guides evolutionary search over configuration pool.
**Results:** 44.5% performance by evolving task-adaptive architectures.
**Relevance:** HIGH. Another topology-evolution system. Validates our thesis.

### Agent0 (Huaxiu Yao, UNC/Salesforce/Stanford)
**What:** Self-evolving agents from zero data. Curriculum agent + executor agent co-evolve. External tools enhance executor, pressuring curriculum agent to create harder tasks.
**Results:** +18% math reasoning, +24% general reasoning on Qwen3-8B.
**Relevance:** MEDIUM. Co-evolution pattern, but less about topology.

### OpenEvolve
**What:** Open-source evolutionary coding agent using MAP-Elites + island model with migration. LLM-guided code edits.
**Relevance:** HIGH. Explicitly uses island model with migration topology. Ring topology default. Validates our experimental setup directly.

### IEEE-JAS Survey: "The Confluence of Evolutionary Computation and Multi-Agent Systems"
**What:** Comprehensive survey of EC+MAS intersection. Growing trend with IoT.
**Relevance:** MEDIUM. Good reference for related work section.

---

## NEW Accounts Worth Following

1. **@HuaxiuYaoML** (Huaxiu Yao) -- Agent0, self-evolving agents from zero data. UNC-Chapel Hill.
2. **@zhuokaiz** (Zhuokai Zhao) -- Writes technical deep-dives on agent architecture evolution. "Core agent loop converged, everything around it diverged."
3. **@_samvelyan** (Mikayel Samvelyan) -- Excited about open-endedness moving to ICLR center stage. Connected to Rocktaschel's keynote.
4. **@mikeknoop** (Mike Knoop) -- Thoughtful AlphaEvolve analysis distinguishing neural networks vs symbolic programs as architectural substrates.
5. **@pushmeet** (Pushmeet Kohli, DeepMind) -- AlphaEvolve Ramsey number results. Independent math discovery.

---

## Trending Themes

1. **Evolutionary LLM agents are mainstream now.** AlphaEvolve, ShinkaEvolve, DRQ, OpenEvolve, Multi-Agent Evolve, Agent0, EvoMAS, AgentConductor -- at least 8 major systems in the last 3 months. The field has EXPLODED.

2. **Topology is the new bottleneck.** AgentConductor explicitly optimizes topology. OpenEvolve uses island model. Multi-Agent Evolve defines role topologies. Everyone is discovering that HOW agents connect matters as much as WHAT they do. Our paper is positioned perfectly.

3. **Strict vs Lax is everywhere (unnamed).** DRQ shows convergence pressure (strict). ShinkaEvolve balances exploration/exploitation (strict/lax). Multi-Agent Evolve co-evolves roles (topology-mediated coupling). Nobody has the categorical language for it yet.

4. **Open-endedness is center stage.** Kenneth Stanley at Lila ($235M), Sakana AI's Darwin Godel Machine, ICLR keynote on open-endedness. The field has moved from niche to mainstream in 12 months.

5. **Self-evolving is the new paradigm.** Agent0 (zero data), DGM (self-rewriting code), Multi-Agent Evolve (no supervision). The pattern is: let the system evolve itself. This is exactly what our categorical framework formalizes -- the monad captures the self-referential structure of evolution.

---

## Action Items for Papers

- **CITE AgentConductor** in GECCO paper related work (topology evolution, published Feb 2026)
- **CITE OpenEvolve** as validation of island model with ring topology default
- **NOTE Jules Hedges** on ACT 2026 PC -- his "lax functors = emergent effects" is directly relevant
- **Consider DRQ** as convergent-evolution (strict coupling) example in discussion
- **ShinkaEvolve** as open-source comparison point for reproducibility argument

## Twitter/X Status
Still broken for direct access. WebSearch with `site:x.com` works well as workaround. Sufficient for audience research. Do not attempt login.
