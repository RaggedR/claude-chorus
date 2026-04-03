# Reading Log — 2026-03-04 (Late Evening Browse, Batch 3)

> Third Twitter/X browse session today. Deep dives on existing follows + new discoveries in LLM-driven evolution space.

## Keywords
1. **"open-endedness evolution AI agents"** — tracking convergence of EC + agents + open-endedness
2. **"category theory AI applications"** — competitive landscape for CT + AI content
3. **"evolutionary algorithm optimization 2026 LLM"** — the explosion of LLM-driven evolutionary frameworks
4. **"compositional AI agents"** — checking if anyone is formalizing agent composition with CT

---

## Twitter/X — Existing Follows Checked (6 accounts)

### @kenneth0stanley (Kenneth Stanley) — Open-endedness, Lila Sciences
**Recent activity:**
- **MAJOR THREAD on AI risks + creativity (Jan 2026):** "I worry that so much discussion of AI risks and alignment overlooks the rather large elephant in the room: creativity and open-endedness." Policy makers need to understand TWO competing forces: (1) massive economic incentive for frontier labs to boost model creativity, and (2) the more you try to control/restrict creativity, the less useful models become. His solution: look at institutional checks and balances (laws, incentive structures, competing branches) rather than "mind control" of models.
- **Doom Debates appearance (Dec 2025):** Argued that open-endedness must be part of AI risk discussion. Any future AGI/superintelligence will inevitably be open-ended. Awareness of open-endedness is "regrettably low on all sides among prognosticators."
- **FER Hypothesis (Oct 2025):** "Fractured Entangled Representation hypothesis" — a position paper questioning whether deep learning representations are actually as compositional as we assume. On Jim Rutt's podcast.
- Still promoting "Why Greatness Cannot Be Planned" ideas. Maven social network closed down.

**Engagement signals:** High on the AI risks/creativity thread. The open-endedness framing resonates with both safety and capability researchers — a rare bridge topic. The Doom Debates appearance got wide pickup on LessWrong.

**Key insight for us:** Stanley's framing of open-endedness as THE missing piece in AI alignment maps perfectly to our strict/lax dichotomy. His "institutional checks" = strict composition (laws, structure), his "freedom to think" = lax composition (exploration, novelty). He is articulating our mathematical framework in natural language. Our "Objective Paradox, Formalized" article should directly engage with his AI risks thread.

---

### @omarsar0 (Elvis / DAIR.AI) — AI agents, multi-agent systems
**Recent activity (Feb-Mar 2026):**
- **"When you add more agents, are you actually getting collaboration, or just spending more compute?"** References a new Gamma metric: compare MAS performance vs single agent with same resource budget. If Gamma > 1, genuine collaboration. If Gamma <= 1, expensive illusion. "Unstructured agent dialogue can create so much noise it actually suppresses collaboration."
- **Agent failure compounding:** "Agents collapse because they take one wrong step, and then another. Each off-path tool call significantly increases the likelihood of failure of the next tool call."
- **Tool description quality (Intuit AI Research):** "Agent performance depends on more than just the agent. It also depends on the quality of the tool descriptions it reads." Tool interfaces still written for humans, not LLMs.
- **InfMem:** Bounded-memory agent with System-2-style cognitive control. PRETHINK-RETRIEVE-WRITE protocol.
- **VibeTensor (NVIDIA):** AI agents built an entire deep learning framework from scratch.
- **Meta Superintelligence Labs:** Strategy-auction framework for self-improving agents. 4B agent gets 87% of 32B performance on simple tasks, but gap widens on complex tasks.
- **GLM-5:** Asynchronous agent RL algorithms for long-horizon interactions.
- **AgenTracer-8B:** Diagnosing errors in multi-agent interactions. Outperforms Gemini-2.5-Pro and Claude-4-Sonnet by 18%.
- **AGENTS.md files:** Human-written ones help a little (+4%), LLM-generated ones hurt a little (-2%), all add 20%+ to inference cost.
- **Science Context Protocol (SCP):** Open-source standard for autonomous scientific agents.

**Engagement signals:** Consistently very high. 100K+ followers. Every paper summary gets substantial engagement. The "more agents = more collaboration?" question is his best-performing framing this month.

**Key insights for us:**
1. The **Gamma metric** (collaboration vs compute waste) is exactly what our strict/lax dichotomy predicts: strict composition = genuine collaboration (Gamma > 1), lax composition = expensive illusion (Gamma <= 1). We should cite this metric in our Medium articles.
2. **Error compounding** = our fingerprint theory. The composition pattern determines whether errors compound or get corrected.
3. **Tool description quality** = morphism typing. If the types (descriptions) don't match, composition fails. This is CT 101, but they don't have the vocabulary.

---

### @RobertTLange (Robert Lange) — Sakana AI, EC + LLMs
**Recent activity (2025-2026):**
- **Doc-to-LoRA (Feb 2026):** Hypernetwork that in <1 second turns any document into a LoRA adapter. "One of the biggest local-AI breakthroughs of 2026" (David Hendrickson). Near-perfect accuracy on needle-in-a-haystack for documents 5x longer than context window.
- **ShinkaEvolve accepted at ICLR 2026:** v1.1 released. LLM-driven evolutionary program optimization. Won ICFP 2025 programming contest for the Unagi team. 150 samples to SOTA on circle packing (orders of magnitude fewer than prior frameworks).
- **TreeQuest:** Multi-model teams outperform individual LLMs by 30%.
- **AI CUDA Engineer:** Agentic system for automating CUDA kernel design and optimization.
- **evosax v0.2.0:** Major update to the JAX evolution strategies library. Multi-GPU support, Optax integration.
- **Digital Red Queen (Sakana + MIT):** Adversarial program evolution in Core War. LLM-evolved warriors become increasingly general over rounds, converging toward general-purpose behavioral strategies. "Convergent evolution in digital organisms."

**Engagement signals:** Very high on Doc-to-LoRA (picked up by omarsar0, VentureBeat, alphaXiv). ShinkaEvolve ICLR acceptance also got good engagement. His threading style (project announcement + technical detail) works well.

**Key insights for us:**
1. **Sakana AI is THE nexus of LLM + evolution.** Lange, Risi, Tang, Ha — all under one roof. DiscoPOP, ShinkaEvolve, TreeQuest, DRQ, AI CUDA Engineer, Doc-to-LoRA. They are the leading industry lab doing evolutionary computation with LLMs.
2. **DRQ's convergent evolution** is fascinating. Warriors converge to general strategies = our strict composition. The Red Queen dynamics = our lax composition. Another instance of the strict/lax dichotomy in the wild.
3. **ShinkaEvolve's bandit-based LLM ensemble** for exploration vs exploitation = exactly the kind of adaptive composition that our categorical framework predicts should exist. Bandits select which LLM mutator to use — this is a choice of Kleisli morphism.
4. **No categorical formalization anywhere in Sakana's work.** They have the best evolutionary AI systems in the world and zero mathematical framework for understanding composition. We are what they're missing.

---

### @_julesh_ (Jules Hedges) — CyberCat Institute, categorical cybernetics
**Recent activity (from CyberCat blog, 2025-2026):**
- **"Autodiff through function types" (Feb 2026):** Reverse-mode automatic differentiation via additive lenses. Shows that the category of additive lenses is cartesian closed. Technical but beautiful.
- **"Dependent optics II" (Oct 2025):** Unifying dependent lenses and monoidal optics via forcing costates.
- **"Bidirectional Typechecking is Bidirectional" (Jan 2025):** Typechecker as an optical structure.
- **"From Equilibrium Checking to Learning" (Jun 2025):** Compositional game theory for dynamic pricing. Bellman operators as optics.
- **CyberCat Institute incorporated as nonprofit (2024).** Hedges working 90% CyberCat, 10% Strathclyde.

**Engagement signals:** Low on Twitter (infrequent poster), but very high quality. CyberCat blog posts are substantive 2000+ word technical pieces.

**Key insight for us:** The additive lenses / autodiff paper is significant. If reverse-mode AD is a lens, and GA selection is a lens (backward pass selecting parents), then our bidirectional GA story connects directly to the CyberCat framework. Hedges is building the mathematical infrastructure we need for the optics-for-evolution direction.

---

### @DavidJaz (David Jaz Myers) — Categorical systems theory, Topos/ARIA
**Recent activity (2025-2026):**
- **Moved to Oxford for Topos UK.** Funded by ARIA's 59M GBP "Mathematics for Safeguarded AI" program.
- **"Double Categorical Systems Theory for Safeguarded AI"** — ARIA project with Sophie Libkind and Owen Lynch. Will expand modeling framework to incorporate formal verification of AI safety/reliability, study verification of model-surrogacy of hybrid discrete-continuous systems.
- **Seminar at Bilkent (Apr 2025):** "Double Categorical Right Modules as the Algebra of Coupled Dynamical Systems."
- **"Nondeterministic Behaviours" paper (Feb 2025):** Double-categorical framework for nondeterministic systems. GAs are nondeterministic systems.
- **"Towards a double operadic theory of systems" (May 2025):** With Libkind. Unifying categorical systems theory via modules over double categories.

**Engagement signals:** Very low on Twitter. Academic channel (seminars, papers) is his primary communication mode.

**Key insight for us:** Myers' ARIA project is the closest thing to an institutional competitor — formal verification of AI safety using categorical systems theory. But his focus is verification (does this system satisfy a safety property?), not composition (does this composition pattern determine behavior?). Complementary, not competitive. We should cite his nondeterministic behaviours paper in our ACT talk.

---

### @mattecapu (Matteo Capucci) — Categorical cybernetics, ARIA
**Recent activity:** On the ACT 2026 program committee. Continues dependent optics work. Active more on Mathstodon than Twitter. Co-authored dependent optics papers with Hedges.

**Engagement:** Low on Twitter, high on Mastodon/academic channels.

---

## Twitter/X — New Accounts/Papers Discovered

### @xwang_lk (Xin Eric Wang) — Group-Evolving Agents
**KEY DISCOVERY.** UC Santa Cruz professor. Published GEA: "The unit of evolution is no longer a single agent, but a group." Agents share experiences within the group during evolution. 71.0% vs 56.7% on SWE-bench Verified. Fixes framework bugs in 1.4 iterations vs 5 for isolated evolution.

**Why this matters for us:** GEA's "group as unit of evolution" is formalizable in our categorical framework. The group sharing structure is a monoidal product on the Kleisli category — agents compose their experiences. This is EXACTLY the kind of work that needs our theory: they have empirical results showing group evolution > tree evolution, but no formal framework explaining WHY. Our composition patterns predict this.

### @imbue_ai (Imbue) — Darwinian Evolver
**KEY DISCOVERY.** Open-sourced "Evolver" — a near-universal optimizer for code and text using LLM-based evolution. Achieved 95% on ARC-AGI-2, 3x'd performance of best open model. Treats code/prompts as "organisms" in a population, LLM proposes mutations, scores them, keeps fittest. Any problem where solutions can be understood/modified by LLM and quality can be scored is suitable.

**Why this matters for us:** Imbue's Evolver is another instantiation of Kleisli composition — the LLM mutation operator IS a Kleisli arrow (input -> distribution over outputs). Their evaluator IS the fitness function. Their "keep the fittest" IS selection. They have literally built a GA using LLMs as operators, and they call it "Darwinian evolution." They need our framework to understand why different mutation strategies produce different behaviors.

### Satyam Mishra — "Composing the Mind of a Machine" (Medium)
**COMPETITIVE FIND.** Medium article applying CT to agentic AI. Uses natural transformations as "universal translators" between agents, limits/colimits for information aggregation, composition of skills as morphisms. Claims "AI will become truly general not when it becomes big, but when it becomes composable."

**Assessment:** Introductory-level. Uses CT concepts as metaphors more than as formal tools. No rigorous definitions, no proofs, no predictions. The conclusion ("composable > big") is correct but unsupported. This is the kind of content that SOUNDS like our work but lacks the substance. Our Medium articles need to go beyond metaphor — show that CT actually PREDICTS behavior (fingerprints, strict/lax, scaling).

---

## New Research Papers Discovered

### Group-Evolving Agents (arXiv:2602.04837, Feb 2026)
Weng, Antoniades, Nathani, Zhang, Pu, Wang. Group of agents as evolutionary unit. Experience sharing overcomes isolated branch inefficiency. 71.0% SWE-bench. Categorical interpretation: monoidal product on Kleisli arrows.

### Digital Red Queen (arXiv:2601.03335, Jan 2026)
Sakana AI + MIT. LLM-evolved warriors in Core War. Convergent evolution toward general strategies. Red Queen dynamics. Categorical interpretation: adversarial composition as a fixed-point iteration.

### AdaEvolve (arXiv:2602.20133, Feb 2026)
Cemri et al. Adaptive evolutionary framework with three-level hierarchy: local (exploration within population), global (bandit scheduling across populations), meta-guidance (novel tactics when progress stalls). 185 open-ended optimization problems.

### Position: Agentic Evolution is the Path to Evolving LLMs (arXiv:2602.00359, Jan 2026)
Lin et al. Position paper arguing that scaling compute doesn't close the train-deploy gap. Agentic evolution = autonomous evolver agent that treats deployment-time improvement as goal-directed optimization over persistent state.

### Imbue Darwinian Evolver (Feb 2026)
95% on ARC-AGI-2. Universal optimizer for code/text. Kimi K2.5 from 12% to 34%, Gemini 3.1 Pro to 95%. Framework: population -> mutation via LLM -> evaluation -> selection -> repeat.

### CyberCat: Autodiff via Additive Lenses (Feb 2026)
Hedges. Category of additive lenses is cartesian closed. Extends reverse-mode AD to lambda calculus. Connects backpropagation to optics framework.

---

## Audience Observations

### 1. LLM-driven evolution has EXPLODED
Since my last browse, the space has gone from "interesting research direction" to "every major lab is doing it." Sakana AI (ShinkaEvolve, DRQ, DiscoPOP), Google DeepMind (AlphaEvolve), Imbue (Darwinian Evolver), AdaEvolve, CodeEvolve, OpenEvolve, GEA, EvoX... The convergence is unmistakable: **LLMs as mutation operators in evolutionary loops is now mainstream ML.** This is our audience. They are ALL doing evolutionary computation without the EC vocabulary, and without any formal framework for understanding composition.

### 2. The "exploration vs exploitation" framing is universal
Every single framework in this space faces the same tension: how to balance exploration (novel mutations, diverse populations) vs exploitation (refining the best solutions). ShinkaEvolve uses bandits. AdaEvolve uses a three-level hierarchy. Imbue uses population dynamics. **This is the strict/lax dichotomy.** They are all independently solving the same problem we formalize.

### 3. "Group evolution" validates our composition theory
GEA's central finding — that group-based evolution (experience sharing) outperforms tree-based evolution (isolated branches) — is a direct empirical validation of our thesis that composition pattern determines behavior. Isolated branches = no composition. Group sharing = monoidal composition. The composition pattern determines the outcome.

### 4. Nobody is providing formal frameworks
AdaEvolve, GEA, Evolver, ShinkaEvolve — they all describe their methods empirically. None provide a mathematical framework for predicting WHEN one composition strategy will outperform another. None explain WHY group evolution beats tree evolution. None can formally characterize the exploration/exploitation tradeoff. This is our niche. We are the theory these systems need.

### 5. The CT + agents space has exactly one competitor
Satyam Mishra's Medium article is the only content I've found that explicitly applies CT to AI agents. It's introductory and metaphorical. The deeper academic work (Gavranovic for neural nets, Hedges for games, Bakirtzis for RL, Myers for dynamical systems) has not yet been applied to agents or to EC. We remain unique in our specific intersection: CT for EC composition, with applications to agent composition.

### 6. CyberCat is building the infrastructure we need
Hedges' additive lenses for autodiff, optics for games, dependent optics for bidirectional processes — this is the mathematical machinery that makes our GA-as-optics direction feasible. CyberCat is not working on EC, but they are building the categorical tools we would use to formalize GAs as bidirectional systems.

---

## Connections

1. **Imbue's Evolver is a GA.** Population, mutation, evaluation, selection. They call it "Darwinian evolution." We call it Kleisli composition. Same thing, different vocabulary. Our first Medium article should use Evolver as a running example.

2. **GEA's group evolution = monoidal composition.** Experience sharing within a group is a monoidal product. Isolated tree branches = tensor unit (no sharing). GEA empirically proves that monoidal composition > tensor unit. This is a theorem in our framework.

3. **AdaEvolve's three-level hierarchy maps to our three-level composition.** Local = operator composition. Global = pipeline composition. Meta = framework composition. The isomorphism is striking.

4. **DRQ's convergent evolution = strict composition.** Warriors converge to general strategies under Red Queen pressure. Strict composition produces predictable, robust outcomes. The convergence IS the strictness.

5. **Stanley's AI risks thread is our best entry point.** His framing (institutional checks = structure, freedom to think = creativity) is our dichotomy (strict = structure, lax = creativity). A response article connecting his argument to formal mathematics would bridge the EC/safety/agents audiences simultaneously.

6. **omarsar0's Gamma metric formalizes our prediction.** Gamma > 1 = genuine collaboration = strict composition. Gamma <= 1 = expensive illusion = lax/no composition. Our framework predicts which architectures will have Gamma > 1 and which won't.

---

## Follow Up

### For next session
- **Track GEA (arXiv:2602.04837)** — read the full paper, understand the experience sharing mechanism formally
- **Track Imbue Evolver** — understand the mutation operator structure, compare to our Kleisli formalization
- **Track AdaEvolve** — the three-level hierarchy is too close to our three-level composition to be coincidence
- **Read CyberCat "Autodiff via Additive Lenses"** in full — understand whether additive lenses formalize the GA backward pass (selection)
- **Check Satyam Mishra's profile** — is he writing more CT + agents content? Competitor or potential audience?

### For Claudius
- GEA empirically validates group composition > isolated evolution — our framework predicts this
- LLM-driven evolution has exploded: every major lab is doing EC with LLMs. None have formal framework
- Imbue's Evolver is literally a GA. They call it "Darwinian evolution." We call it Kleisli composition
- AdaEvolve's three-level hierarchy maps suspiciously well to our three-level composition

### For Robin
- The LLM-evolution explosion is extremely relevant to our positioning. We are the only ones providing formal theory for a space that now has 5+ competing frameworks
- Satyam Mishra on Medium is writing CT + agents content — introductory level, not a serious competitor, but confirms the audience exists

### New accounts to consider following
- **@xwang_lk** (Xin Eric Wang) — GEA author, group evolution
- **@imbue_ai** (Imbue) — Darwinian Evolver, universal optimizer
- **@SakanaAILabs** — Sakana AI official account (DRQ, ShinkaEvolve)
