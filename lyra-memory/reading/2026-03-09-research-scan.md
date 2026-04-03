# Research Scan — 2026-03-09

> Systematic web research across all project-relevant search areas.

## CRITICAL: Competing Work Assessment

**No competing work found on categorical formalization of GAs.** Searched extensively for:
- "category theory" + "evolutionary algorithm" + Kleisli/monad
- "categorical evolution" + formalization + genetic algorithm + functor
- "genetic algorithm" + "Kleisli" / "co-Kleisli" / "coKleisli" + morphism + selection/crossover/mutation
- "strict monoidal" / "lax monoidal" + functor + exploration/exploitation/convergence/diversity

**Result: Zero hits.** The only CT+evolution intersection remains Warrell's Kantorovich monad paper (2411.09779), which we already track. Nobody is formalizing GA operators as Kleisli morphisms. The lane is still clear.

---

## NEW Finds (Not Previously Tracked)

### 1. Imbue Darwinian Evolver (Feb 27, 2026) -- NEW, HIGH RELEVANCE
- **URL:** https://imbue.com/research/2026-02-27-darwinian-evolver/
- **GitHub:** https://github.com/imbue-ai/darwinian_evolver
- **Authors:** Imbue AI team
- **Summary:** Open-sourced "Evolver" -- a near-universal optimizer for code and text. Maintains population of "organisms" (code), applies LLM-based mutations, scores children, adds back to population. Problem-agnostic. Pushed Gemini 3.1 Pro to 95% on ARC-AGI-2. Works even with noisy evaluators or unreliable mutators (20% success rate still sufficient).
- **Why relevant:** Direct embodiment of LLM-as-mutation-operator paradigm. Their "population of organisms" = our Kleisli category of populations. Their mutation operators = our Kleisli morphisms. This is the PRACTICE that our THEORY formalizes. Potential empirical data point for strict/lax.
- **Novelty:** NEW. Not previously tracked.

### 2. MadEvolve: Evolutionary Optimization of Cosmological Algorithms (Feb 2026) -- NEW
- **URL:** https://arxiv.org/abs/2602.15951
- **Authors:** Li, Zang et al.
- **Summary:** Similar to AlphaEvolve but with stronger emphasis on free parameters and their optimization. LLMs serve as smart mutation operators. Nested architecture: inner loop tunes continuous parameters, outer loop evolves algorithmic structure. Applied to cosmological initial conditions, 21cm foreground, baryonic physics.
- **Why relevant:** Another domain-specific LLM+evolution framework. Confirms trend: LLMs as mutation operators is becoming standard. Their nested architecture (structural search separated from parameter optimization) maps to our strict/lax dichotomy -- strict inner loop (parameter tuning) vs lax outer loop (structural evolution).
- **Novelty:** NEW. Not previously tracked.

### 3. "Assemble Your Crew" -- ARG-Designer (AAAI 2026 Oral) -- NEW, HIGH RELEVANCE
- **URL:** https://arxiv.org/abs/2507.18224
- **GitHub:** https://github.com/Shiy-Li/ARG-Designer
- **Authors:** Li, Liu et al.
- **Summary:** Reframes multi-agent system design as conditional autoregressive graph generation. Determines number of agents, selects roles from extensible pool, establishes optimal communication links -- all conditioned on task query. AAAI 2026 Oral.
- **Why relevant:** TOPOLOGY IS GENERATED, NOT HAND-DESIGNED. This is the strongest empirical validation yet that "topology dominates capability." They automate the composition pattern selection -- exactly what our categorical framework predicts matters. Their "extensible role pool" = morphisms in our agent category.
- **Novelty:** NEW. Not previously tracked.

### 4. Multi-Agent Design: MASS Framework (Feb 2025, revised Jan 2026) -- NEW
- **URL:** https://arxiv.org/abs/2502.02533
- **Authors:** Han Zhou, Xingchen Wan, Ruoxi Sun, Hamid Palangi, Shariq Iqbal, Ivan Vulic, Anna Korhonen, Sercan O. Arik
- **Summary:** Multi-Agent System Search (MASS) -- optimizes MAS design space by interleaving local-to-global stages: block-level prompt optimization -> workflow topology optimization -> workflow-level optimization. Shows prompts + topologies are critical for effective MAS design.
- **Why relevant:** Complementary to ARG-Designer. Both confirm: composition topology is a first-class design variable. MASS's staged optimization (local -> global) maps to our strict-then-lax composition pattern.
- **Novelty:** NEW. Not previously tracked.

### 5. "Towards a Science of Scaling Agent Systems" (Dec 2025) -- UPDATED DETAILS
- **URL:** https://arxiv.org/abs/2512.08296
- **Authors:** Google research team
- **Summary:** 180 configurations, 5 architectures, 3 LLM families. Key empirical findings: (1) capability saturation at ~45% baseline, (2) independent agents amplify errors 17.2x vs centralized 4.4x, (3) heterogeneous composition (high-capability subagents + low-capability orchestrators) outperforms homogeneous. Predictive model R^2=0.524.
- **Why relevant:** Was already tracking (as reference in agent orchestration), but the SPECIFIC NUMBERS are gold. Error amplification 17.2x vs 4.4x = strict vs lax composition cost. Heterogeneous > homogeneous = our "morphism quality matters more than object quality" thesis. The R^2=0.524 predictive model = partial evidence that topology IS predictive.
- **Novelty:** Already tracked, but deeper detail extracted.

### 6. DiagrammaticLearning (Jan 2025) -- NEW, THEORETICALLY IMPORTANT
- **URL:** https://arxiv.org/abs/2501.01515
- **Authors:** Mason Lary, Richard Samuelson, Alexander Wilentz, Alina Zare, Matthew Klawonn, James P. Fairbanks
- **Summary:** Learning diagrams = graphical depictions of training setups that capture parameterized learning as data. Uses category theory to provide rigorous semantics. Compiles to unique loss functions. Implemented as PyTorch/Flux.jl library.
- **Why relevant:** Fairbanks group (Topos-adjacent). They formalize TRAINING COMPOSITION categorically, we formalize EVOLUTION COMPOSITION categorically. Parallel approach, different domain. Potential for cross-pollination. Their "compile diagram to loss function" = our "compile GA pipeline to composed Kleisli arrow."
- **Novelty:** NEW. Not previously tracked.

### 7. Categorical Semantics of Compositional RL -- JMLR 2025 (Updated) -- PARTIALLY KNOWN
- **URL:** https://arxiv.org/abs/2208.13687, JMLR publication
- **Authors:** Bakirtzis, Savvas, Topcu
- **Summary:** Category of MDPs with pushout-based composition. Published in JMLR 2025. Follow-up "Reduce, Reuse, Recycle" (2408.13376) applies to robotic tasks at ECAI 2024.
- **Why relevant:** Closest methodological parallel -- they apply CT to RL, we apply CT to EC. Their pushout = our Kleisli composition. We should cite both papers. Bakirtzis group is active and publishing in major venues (JMLR, ECAI).
- **Novelty:** Partially known (Jia survey cites it). But JMLR publication and ECAI follow-up are new info.

### 8. Multi-Agent Evolve (MAE) (Oct 2025) -- NEW
- **URL:** https://arxiv.org/abs/2510.23595
- **Summary:** Triplet of co-evolving agents (Proposer, Solver, Judge) from single LLM. Self-play paradigm extended to general domains. Closed-loop propose-solve-judge pipeline. 4.86% average improvement on Qwen2.5-3B.
- **Why relevant:** Co-evolution of agent roles = natural multi-level selection. Their Proposer/Solver/Judge triplet = three distinct Kleisli morphisms in composition. Potential example for our framework.
- **Novelty:** NEW. Not previously tracked.

### 9. Jia et al. CT+ML Survey -- Published MDPI Axioms (March 2025) -- UPDATED
- **URL:** https://www.mdpi.com/2075-1680/14/3/204
- **Summary:** Four perspectives: gradient-based (Cartesian differential categories), probability-based (Markov categories), invariance/equivalence-based (metric spaces), topos-based (neural net internal properties). First survey of topos-based learning.
- **Why relevant:** Already tracking (2408.14014), but now PUBLISHED in journal. Good to update citation. Confirms no CT+EC formalization in their comprehensive survey = we're first.
- **Novelty:** Already tracked, but journal publication is new.

### 10. CyberCat: Reverse-Mode AD via Additive Lenses (Feb 20, 2026) -- NEW
- **URL:** https://cybercat.institute/ (blog post by Jules Hedges)
- **Summary:** New derivation showing reverse-mode AD for first-class function types arises universally from "additive lenses" being cartesian closed.
- **Why relevant:** Hedges/CyberCat is the open games group. Their lens-based approach to composition is methodologically parallel. "Additive lenses" might inform how we think about gradient-like information flow in evolutionary landscapes. Tangential but worth noting.
- **Novelty:** NEW blog post.

---

## LLM+Evolution Landscape Update (March 2026)

The field is EXPLODING. Key trend: LLMs-as-mutation-operators is now mainstream:
- **AlphaEvolve** (Google DeepMind) -- the pioneer
- **ShinkaEvolve** (Sakana AI) -- sample-efficient, beats AlphaEvolve on circle packing in 150 samples
- **Imbue Evolver** (NEW) -- open-source, near-universal, 95% ARC-AGI-2
- **MadEvolve** (NEW) -- domain-specific (cosmology), nested architecture
- **EvoX** -- meta-evolution, automated discovery
- **Multi-Agent Evolve** (NEW) -- co-evolution of agent roles

**What's missing from ALL of them:** Category theory. They all build ad hoc frameworks. None formalize WHY their composition patterns work. None can predict which topology/composition will work for a new task. **This is exactly the gap our paper fills.**

---

## Agent Orchestration Landscape Update

Three major NEW papers on topology:
1. **ARG-Designer** (AAAI 2026 Oral) -- autoregressive graph generation for agent topology
2. **MASS** (Feb 2025/Jan 2026 revision) -- staged optimization of prompts + topologies
3. **Scaling Agent Systems** (Dec 2025) -- 180-config empirical study with predictive model

All three validate "topology dominates capability." None use categorical frameworks. The gap is even wider than when we started.

---

## Conference Updates

### ACT 2026
- Tallinn, Estonia. July 6-10, 2026. Adjoint School June 29-July 3.
- **Abstracts due March 23. Full papers due March 30.** (Confirmed -- no changes.)
- Submission via EasyChair. EPTCS proceedings. Single-blind.

### GECCO 2026
- Malaga, Spain.
- AABOH workshop: 6th edition. Papers up to 8 pages (excluding refs). ACM companion volume.
- **Workshop paper deadline: March 27.** (Confirmed.)

### n-Category Cafe
- Recent posts: Categorifying Riemann's Functional Equation (Jan 2026), Univalence Principle (Feb 2026), Coxeter/Dynkin Diagrams (Jan 2026). None directly relevant to our work.

---

## Summary: What's Hot, What's Missing

**Hot:**
1. LLM-as-mutation-operator (everyone is doing it)
2. Agent topology as first-class design variable (ARG-Designer, MASS, Scaling Agents)
3. Self-evolving agents (MAE, Imbue Evolver, Self-Play paradigms)
4. CT+ML formalization (DiagrammaticLearning, Bakirtzis RL, Jia survey)

**Missing (= our opportunity):**
1. **CT+EC formalization** -- NOBODY is doing this. Zero competing papers found.
2. **Strict/lax dichotomy in practice** -- the LLM+evolution papers implicitly use it (MadEvolve's nested architecture, Imbue's population dynamics) but none NAME it or formalize it.
3. **Predictive theory for agent topology** -- everyone measures topology effects empirically, nobody has a categorical framework to PREDICT them.
4. **Bridging CT+RL and CT+EC** -- Bakirtzis does RL, we do EC. Nobody connects them. (Post-ACT opportunity?)
