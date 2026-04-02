# Research Scan: March 8, 2026

Systematic search across evolutionary code generation, categorical composition, and agent protocol engineering. Focus: new papers and developments since March 6, 2026.

---

## NEW FINDINGS (Post-March 6)

### 1. Sarkis & Zanasi — "Complete Diagrammatic Axiomatisations of Relative Entropy"
- **arXiv:** 2603.04530 | **Date:** March 4, 2026
- **Source:** math.CT
- **Summary:** Studies relative entropy from a categorical perspective as quantitative enrichment of categories of stochastic matrices. Complete axiomatizations for KL divergence and Renyi divergences using string diagrams enriched with quantitative equations. Uses monoidal structures (Kronecker product & direct sum) for compositional reasoning.
- **Relevance:** Demonstrates compositional/diagrammatic methods applied to information-theoretic quantities. Directly in the ACT wheelhouse. The "quantitative monoidal algebra" framework could inform how we think about fitness-preserving composition.
- **Citation priority:** MEDIUM. Not directly about EC but shows CT applied to quantitative reasoning in ML-adjacent contexts.

### 2. Aambo — "A categorical formalization of epistemic uncertainty frameworks"
- **arXiv:** 2603.04188 | **Date:** March 4, 2026
- **Source:** math.CT (cross-listed cs.AI)
- **Summary:** Category-theoretic framework for epistemic uncertainty. Defines "epistemic calculi" using enriched category theory. Shows Bayesian updating and possibilistic conditioning as specific examples of a general categorical belief-updating mechanism.
- **Relevance:** Enriched category theory applied to reasoning under uncertainty — tangential but shows growing CT+AI formalization trend.
- **Citation priority:** LOW. Interesting methodology but not GA-specific.

### 3. Aggarwal et al. — "Discovering mathematical concepts through a multi-agent system"
- **arXiv:** 2603.04528 | **Date:** March 4, 2026
- **Summary:** Multi-agent system for computational mathematical discovery. Agents pose conjectures, attempt proofs, and evolve data distributions based on feedback. Benchmark: autonomously recovering the concept of homology from polyhedral data + linear algebra. Uses ablation studies to show combined agent processes yield emergent "mathematical interestingness."
- **Relevance:** Multi-agent evolutionary discovery of mathematical structures. The conjecture-proof-feedback loop is structurally similar to our fitness evaluation cycle. The emergence of homology (a categorical concept!) from agent interaction is remarkable.
- **Citation priority:** MEDIUM. Supports the "agents discovering categorical structure" narrative.

### 4. Guo et al. — "Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through Exploration?"
- **arXiv:** 2603.03202 | **Date:** March 3, 2026
- **Summary:** Multi-agent framework where code agents autonomously evolve math problems into more complex variations. Uses code execution as environment for mathematical experimentation. Validates solvability and increased difficulty of generated problems.
- **Relevance:** Code agents doing evolutionary exploration of mathematical problem spaces — combines LLM code generation with evolutionary search.
- **Citation priority:** LOW. More about training data generation than formal composition.

### 5. Alzubi et al. — "EvoSkill: Automated Skill Discovery for Multi-Agent Systems"
- **arXiv:** 2603.02766 | **Date:** March 3, 2026
- **Summary:** Evolutionary skill discovery via iterative failure analysis. Uses Pareto frontier to govern skill retention. 7.3% improvement on OfficeQA, 12.1% on SealQA. Skills transfer zero-shot across benchmarks.
- **Relevance:** Evolutionary composition of agent capabilities. Pareto-based selection of composed skills is structurally close to our fitness-driven composition.
- **Citation priority:** LOW-MEDIUM. More engineering than theory but shows evolutionary agent composition in practice.

### 6. de Pinho & Sinapayen — "A speciation simulation that partly passes open-endedness tests"
- **arXiv:** 2603.01701 | **Date:** March 2, 2026
- **Summary:** Tests Tree of Life Simulation for Tokyo type 1 open-ended evolution. Finds unbounded total cumulative evolutionary activity but bounded normalized metrics. New evolutionary activity is persistently null — so NOT truly open-ended.
- **Relevance:** Open-endedness testing methodology. The "partially open-ended" result connects to our strict/lax dichotomy: strict composition might bound novelty, lax composition might enable unbounded exploration.
- **Citation priority:** LOW. Interesting conceptual connection but different domain (ALife, not EC+CT).

### 7. Wegmann — "The Theory behind UMAP?"
- **arXiv:** 2603.03375 | **Date:** March 2, 2026
- **Source:** math.CT
- **Summary:** Identifies and corrects errors in the categorical foundations of UMAP (Spivak's metric realization functor). Provides full self-contained derivation.
- **Relevance:** Category theory applied to practical ML algorithms. Shows both the promise and the difficulty of getting CT+ML right (even Spivak had errors).
- **Citation priority:** LOW. Shows CT+ML maturation but not directly relevant.

---

## CONFIRMED RECENT (Feb 18 - March 1)

### 8. EvoX: Meta-Evolution for Automated Discovery
- **arXiv:** 2602.23413 | **Date:** February 26, 2026
- **Authors:** Shu Liu, Shubham Agarwal, et al. (Berkeley, Stanford, Bespoke Labs)
- **Summary:** Meta-evolutionary system that jointly evolves solutions AND search strategies. Outer loop evolves the inner loop. Outperforms AlphaEvolve, OpenEvolve, GEPA, ShinkaEvolve across ~200 tasks.
- **Relevance:** HIGH. This is the new SOTA for evolutionary code optimization. The two-loop structure (solution evolution + strategy evolution) maps beautifully onto our categorical framework: the inner loop is a Kleisli morphism, the outer loop is a natural transformation between Kleisli categories. This is exactly the kind of meta-level composition our paper describes.
- **Citation priority:** HIGH for GECCO. Consider for ACT if space permits.

### 9. AdaptOrch: Task-Adaptive Multi-Agent Orchestration
- **arXiv:** 2602.16873 | **Date:** February 18, 2026
- **Author:** Geunbin Yu
- **Summary:** Formal framework for adaptive multi-agent orchestration. Four canonical topologies (parallel, sequential, hierarchical, hybrid). Topology Routing Algorithm maps task DAGs to optimal patterns. Performance Convergence Scaling Law.
- **Relevance:** Formalizes agent composition topology selection. The four topologies correspond to different categorical composition patterns. "Orchestration topology dominates over model capability" — this is the composition thesis.
- **Citation priority:** MEDIUM. Supports our claim that composition structure matters more than component quality.

### 10. Composition-RL: Compose Your Verifiable Prompts for RL
- **arXiv:** 2602.12036 | **Date:** February 12, 2026
- **Summary:** Automatically composes multiple problems into new verifiable questions for RL training. Curriculum variant increases compositional depth over time. Cross-domain composition by mixing prompt sources.
- **Relevance:** Compositional approach to RL training that mirrors compositional fitness evaluation. "Compositional depth" as a training curriculum is interesting.
- **Citation priority:** LOW. Tangential but shows "composition" language spreading.

---

## MAJOR CONTEXTUAL DEVELOPMENTS

### Quanta Magazine — "Can the Most Abstract Math Make the World a Better Place?"
- **URL:** https://www.quantamagazine.org/can-the-most-abstract-math-make-the-world-a-better-place-20260304/
- **Date:** March 4, 2026
- **Summary:** Natalie Wolchover profiles applied category theory. Features Baez (green math), Leinster, Fong (Topos), Capucci, Spivak, Hadzihasanovic, Osgood. Discusses StockFlow (epidemiology), Safeguarded AI (ARIA), database management. Notes ACT remains marginalized but gaining legitimacy.
- **Relevance:** VERY HIGH for context. This is the SECOND Quanta article on ACT in March 2026. Confirms CT visibility at all-time high. Our ACT 2026 submission rides this wave.
- **Key quote:** "Safeguarded AI" program using CT for AI safety — directly connects to our compositional verification claims.

### John Baez — "Applied Category Theory and Green Mathematics"
- **URL:** https://johncarlosbaez.wordpress.com/2026/03/05/applied-category-theory-and-green-mathematics/
- **Date:** March 5, 2026
- **Summary:** Baez comments on the Quanta article. Notes the growing mainstream visibility of ACT.

### ARIA Safeguarded AI — Double Categorical Systems Theory
- **Source:** ARIA / Topos UK / GLAIVE
- **Status:** Active, funded (part of GBP 59M program)
- **Key people:** David Dalrymple (ARIA), Sophie Libkind, David Jaz Myers, Owen Lynch (Topos UK), Jade Master, Neil Ghani, Jules Hedges (GLAIVE)
- **Summary:** Using double categorical systems theory (DCST) as mathematical framework for AI safety. Goal: explainable and auditable models of autonomous AI systems. 300-page thesis due September 2026.
- **Relevance:** HIGH. This is the most concrete CT+AI project in existence. Libkind/Myers are already cited in our paper (2505.18329). Their ARIA work validates the entire enterprise of using categorical methods for agent/system composition.

### ShinkaEvolve v1.1 — ICLR 2026
- Accepted at ICLR 2026. Released v1.1 February 2026 with new features.
- Already tracked but confirm: it's now at a top venue.

### UMass COMPSCI 692CT: Category Theory for AGI
- **Instructor:** Sridhar Mahadevan
- **Date:** Spring 2026 (ongoing)
- **Summary:** Full graduate course applying CT to AGI. Covers: categories, functors, natural transformations, Yoneda, limits/colimits, adjunctions, monads, Kan extensions. Uses both Riehl's textbook and Mahadevan's new "Categories for AGI" (2026). Two philosophical halves: (1) behavioral equivalence via Yoneda, (2) consciousness via topos theory.
- **Relevance:** MEDIUM. Shows CT+AI being taught at graduate level. The "Categories for AGI" textbook is new 2026 material worth tracking.

### CT2026 — Baltimore, July 13-18
- International Category Theory Conference at Johns Hopkins, satellite of 2026 ICM.
- Invited speakers: Cruttwell, Fritz, Hoefnagel, Moerdijk, Niefield, Walton.
- Separate from ACT 2026 (Tallinn, July 6-10).

### Protocol Wars: MCP vs A2A vs ACP
- Anthropic MCP donated to Linux Foundation (Dec 2025). Founding members: AWS, Google, Microsoft, OpenAI.
- A2A (Google): agent-to-agent communication standard.
- ACP (IBM Research): agent collaboration protocol.
- W3C working on formal specs, expected 2026-2027.
- **Key insight:** Practitioners building agent protocol stacks are independently discovering compositional patterns. "Everything is a Coding Agent" (Medium, March 2026) describes protocol layering that maps onto categorical composition.

---

## CyberCat Institute Blog
- **Last post:** February 20, 2026 — Jules Hedges on "Autodiff through function types"
- **Topic:** Extends reverse-mode AD to first-class function types via cartesian closed categories of additive lenses.
- **Hedges' caveat:** "This idea sounds like it should revolutionize machine learning, but then it doesn't."
- No new posts since February 20.

## Topos Institute Blog
- CatColab v0.4 "Robin" released (compositional notebooks, Petri net analyses).
- Tim Hosgood post (January 30, 2026).
- No new posts in March.

## n-Category Cafe
- No new March 2026 posts found in search. Last relevant: ACT 2026 announcement (Oct 2025), Category Theorists in AI (Feb 2025).

---

## KEY GAP CONFIRMED

**Searched explicitly for papers combining "evolutionary algorithm" with "category" OR "functor" OR "morphism" in 2025-2026. Found ZERO results.**

This confirms that Lyra's paper ("From Games to Graphs") occupies a genuinely novel position: there is no prior work formalizing genetic algorithm operators as categorical morphisms (Kleisli arrows). The closest are:
- Warrell (2411.09779): Kantorovich monad for GAs (probabilistic, not compositional operators)
- Gavranovic/Gavranovic (categorical deep learning): architectures, not evolution
- Bakirtzis (compositional RL): RL, not EC

---

## TRENDS (Last 2 Weeks)

1. **Meta-evolution is the new frontier.** EvoX, ShinkaEvolve v1.1, and the self-evolving agents survey all point to systems that evolve their own evolution strategies. Our categorical framework captures this naturally as natural transformations between Kleisli categories.

2. **Agent composition formalization is heating up.** AdaptOrch (formal topologies), EvoSkill (evolutionary skill discovery), and the ARIA DCST program all formalize how agents compose. But NONE use category theory for EC specifically.

3. **CT+AI visibility at all-time high.** Two Quanta articles, a full UMass graduate course, ARIA's GBP 59M program, Symbolica's $30M, and the Topos UK branch. The field is no longer marginal.

4. **Protocol engineering reinventing CT vocabulary.** MCP/A2A/ACP practitioners describe "composition," "orchestration topology," and "layered protocols" without knowing they're doing category theory. This is the "linguistic gap" noted in Lyra's connections.

5. **Open-endedness still unsolved.** de Pinho & Sinapayen's ToLSim fails open-endedness tests. The strict/lax composition dichotomy may have something to say about why.

## GAPS (Mathematical Frameworks Still Missing)

1. **No CT formalization of evolutionary operators.** Lyra's paper is the only one. Zero competition.
2. **No formal bridge between agent protocol layers and categorical composition.** MCP/A2A/ACP could be formalized as functors between protocol categories. Nobody is doing this.
3. **No formal treatment of meta-evolution.** EvoX's two-loop structure begs for a categorical treatment (e.g., 2-categorical or double-categorical).
4. **No compositional theory of open-endedness.** The strict/lax dichotomy could be the first.

## AUDIENCE SIGNALS

- **Practitioners** (Medium, DEV, engineering blogs): Talking about MCP/A2A protocol stacks, Claude Code dominance, "everything is an agent." Want practical composition patterns. Would respond to "here's the math behind why your agent composition works or doesn't."
- **Academics** (arXiv, ACT community): Focused on ARIA Safeguarded AI, double categorical systems theory, CatColab, string diagrams. Would respond to rigorous categorical formalizations with worked examples.
- **The bridge audience** (Quanta readers, cats.for.ai attendees): Want accessible explanations of why CT matters for AI. This is the Medium article audience.
