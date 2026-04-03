# Research Scan: March 5, 2026
> Systematic search across arXiv, blogs, and web for recent work relevant to categorical evolution.

## Search Queries Used
1. "category theory evolutionary computation 2026"
2. "compositional multi-agent systems formal framework 2026"
3. "open-ended evolution formal framework 2026"
4. "AlphaEvolve formal analysis mathematical framework LLM evolution"
5. arXiv math.CT February 2026 listings
6. CyberCat Institute, n-Category Cafe, Topos Institute blogs
7. Various targeted follow-ups

---

## HIGH RELEVANCE FINDS

### 1. Spivak — "Interactions that reshape the interfaces of the interacting parties"
- **arXiv:** 2602.17917 (February 20, 2026)
- **Author:** David I. Spivak
- **Subjects:** math.CT, cs.LG
- **Summary:** Extends polynomial functors to model systems whose interfaces dynamically change during interaction. Introduces "polynomial trees" — coinductive structures where each interaction round determines the next interface configuration. Constructs a monoidal closed category PolyTr of polynomial trees, and a bicategory OrgTr generalizing the fixed-interface organizational framework. Application: progressive GANs where gradient feedback reshapes the generation interface.
- **Relevance to Lyra:** VERY HIGH. This is Spivak extending Poly to handle adaptive interfaces — exactly what evolutionary operators do when they reshape the search space. An EA that changes its representation mid-run (adaptive mutation, adaptive crossover rates) is literally an "interaction that reshapes interfaces." The coinductive structure matches how evolutionary runs unfold over time. Could cite this as: "Even the interface of an evolutionary operator can evolve — Spivak's polynomial trees provide the categorical machinery."
- **Novelty:** Genuinely new (Feb 2026). First categorical treatment of dynamic interfaces via coinductive polynomial trees.
- **Action:** CITE in ACT talk. Potentially cite in extended paper. This connects to the co-Kleisli direction (selection reshaping the interface).

### 2. "Evolving Interpretable Constitutions for Multi-Agent Coordination"
- **arXiv:** 2602.00755 (January 31, 2026)
- **Authors:** Ujwal Kumar, Alice Saito, Hershraj Niranjani, Rayan Yessou, Phan Xuan Tan
- **Venue:** AAMAS 2026 (accepted)
- **Summary:** Uses LLM-driven genetic programming with multi-island evolution to evolve behavioral "constitutions" for multi-agent LLM systems. Evolved constitution achieves 123% higher societal stability than human-designed baselines. Key finding: minimizing communication (0.9% vs 62.2% social actions) outperforms verbose coordination.
- **Relevance to Lyra:** HIGH. This is literally "evolving the composition rules for multi-agent systems" — but without any formal framework for what composition means. They use multi-island evolution (= MAP-Elites-like) but have zero categorical vocabulary. The finding that less communication = better coordination is a potential strict/lax observation: their evolved agents are doing STRICT coordination (shared implicit rules) rather than LAX (explicit message passing).
- **Novelty:** New system, but no formal analysis. Opportunity: our framework could explain WHY their results work.
- **Action:** CITE in GECCO or ACT. Frame as: "Even constitution evolution benefits from understanding composition — our framework predicts that strict coordination outperforms lax."

### 3. muACP: A Formal Calculus for Agent Communication
- **arXiv:** 2601.00219 (January 1, 2026)
- **Authors:** Arnab Mallick, Indraveni Chebolu
- **Venue:** AAMAS 2026 (accepted)
- **Summary:** Formal calculus for resource-constrained agent communication. Proves that 4 verbs {PING, TELL, ASK, OBSERVE} suffice to encode all finite-state FIPA protocols. Verified in TLA+ and Coq.
- **Relevance to Lyra:** MEDIUM-HIGH. This is the "minimal basis" question for agent composition — analogous to asking what the minimal set of evolutionary operators is. Their proof that 4 verbs suffice is reminiscent of our observation that mutation + selection can subsume crossover (AlphaEvolve). Different domain but same structural question about minimal generating sets for composition.
- **Novelty:** New formal calculus. Verified proofs are impressive.
- **Action:** Note for future reference. Could cite in expanded paper when discussing agent composition.

### 4. Indexed Graded Monads for Dependent Effect Systems
- **arXiv:** 2601.14846 (January 21, 2026)
- **Authors:** Satoshi Kura, Marco Gaboardi, Taro Sekiyama, Hiroshi Unno
- **Summary:** Introduces "indexed graded monads" — graded monads where effects can depend on program values. Applications: cost analysis, probability bounds, temporal safety. Extends the Breuvart/Katsumata line of work.
- **Relevance to Lyra:** MEDIUM. Graded monads capture "how much" of an effect, not just "what kind." For evolutionary operators, the grade could capture population size, mutation rate, or generation count. An evolutionary monad graded by generation number would let you track how composition accumulates over time. This is the right machinery for formalizing "convergence" categorically.
- **Novelty:** Genuinely extends graded monads to dependent effects. New (Jan 2026).
- **Action:** Add to reading list for post-submission exploration. Potential bridge between our Kleisli framework and quantitative analysis.

### 5. Weisfeiler and Lehman Go Categorical
- **arXiv:** 2602.06787 (February 6, 2026)
- **Authors:** Seongjin Choi, Gahee Kim, Se-Young Yun
- **Summary:** Categorical framework for graph neural networks. Formalizes lifting as a functorial mapping from data categories to graded posets. Two new functors (incidence, symmetric simplicial complex) that produce distinct architectures subsume the WL test expressivity.
- **Relevance to Lyra:** MEDIUM. Demonstrates that categorical abstractions can produce concrete neural architectures with provable expressivity guarantees. Same pattern as our work: categorical formalism -> concrete algorithmic insight. Different domain but validates the approach.
- **Novelty:** New application of CT to GNNs.
- **Action:** Note as "categorical ML" validation. Could cite when arguing that CT produces practical insights, not just abstractions.

---

## MEDIUM RELEVANCE FINDS

### 6. On the Centre of Strong Graded Monads
- **arXiv:** 2602.09780 (February 10, 2026)
- **Authors:** Flavien Breuvart, Quan Long, Vladimir Zamdzhiev
- **Summary:** Characterizes central elements of pomonoid-graded strong monads, showing the centre forms a commutative submonad.
- **Relevance:** LOW-MEDIUM. Pure theory, but commutative submonads of graded monads could be relevant if we grade our evolutionary monad by something (generation, population structure).

### 7. Layered Monoidal Theories II: Fibrational Semantics
- **arXiv:** 2602.22373 (February 25, 2026)
- **Authors:** Leo Lobski, Fabio Zanasi
- **Summary:** String diagrammatic methods for scientific theories at varying abstraction levels. Soundness and completeness for fibrational/opfibrational/deflational layered monoidal theories.
- **Relevance:** MEDIUM. Zanasi's graded monoidal theories are exactly the kind of framework that could capture "levels" in evolutionary computation (gene, individual, population, meta-population). The fibrational semantics gives a way to move between levels formally. Connection to Warrell's multilevel GA monad.

### 8. Evolutionary Policy Optimization (EPO)
- **arXiv:** 2503.19037 (March 2025, revised Nov 2025)
- **Authors:** Jianren Wang, Yifan Su, Abhinav Gupta, Deepak Pathak
- **Summary:** Hybrid EA + policy gradient. Population of agents conditioned on latent variables shares actor-critic weights. GA operates at latent space level.
- **Relevance:** MEDIUM. Another EA+RL hybrid without categorical formalism. The "latent variable conditioning" is essentially parameterizing agents by a monoidal structure. Validates our claim that the EA-RL boundary is porous and needs formal treatment.

### 9. Verifiable Semantics for Agent-to-Agent Communication
- **arXiv:** 2602.16424 (February 18, 2026)
- **Authors:** Philipp Schoenegger et al.
- **Summary:** Certification protocol for multi-agent communication based on stimulus-meaning model. Agents restricting to certified terms achieve provably bounded disagreement.
- **Relevance:** MEDIUM. Formal verification of agent communication semantics. Different from our work but addresses the "how do we know agents are actually composing correctly?" question.

### 10. LLM-EBG: Evolutionary Benchmark Generation via LLMs
- **arXiv:** 2601.12723 (January 19, 2026)
- **Authors:** Yuhiro Ono, Tomohiro Harada, Yukiya Miura
- **Summary:** LLM as evolutionary operator that generates benchmark problems. Key finding: benchmarks favoring GA are highly sensitive to variable scaling.
- **Relevance:** MEDIUM. LLM-as-operator pattern continues. Their finding about scaling sensitivity is interesting — could be formalized as the functor from problem space to algorithm performance being sensitive to certain natural transformations.

### 11. Lark: Neuroevolution for Multi-Stakeholder LLM Agents
- **arXiv:** 2510.16978 (October 2025, revised Dec 2025)
- **Authors:** Dheeraj Chintapalli, Rikhil Tanugula, Sunkalp Chandra
- **Summary:** Biologically inspired neuroevolution for multi-agent LLM decision-making. Four mechanisms: plasticity, duplication/maturation, ranked-choice stakeholder aggregation, compute awareness.
- **Relevance:** MEDIUM. Another evolutionary approach to multi-agent coordination without formal framework. Validates the gap we're filling.

### 12. CyberCat: Autodiff Through Function Types
- **Blog post:** February 20, 2026 (Jules Hedges)
- **Summary:** Reverse mode AD for first-class function types arises from cartesian closure of "additive lenses" category. Hedges notes it "doesn't revolutionize ML" despite sounding like it should.
- **Relevance:** LOW-MEDIUM. Hedges being honest about when categorical insights DON'T directly translate to practice. Important methodological lesson. The additive lenses are related to optics framework.

---

## BLOG & CONFERENCE LANDSCAPE

### n-Category Cafe (Jan-Feb 2026)
- "The Univalence Principle" (Feb 11) — pure foundations, not applied
- "Categorifying Riemann's Functional Equation" (Jan 26) — number theory
- "Coxeter and Dynkin Diagrams" (Jan 6) — representation theory
- **No applied CT posts in 2026 so far.** The blog remains focused on pure math.

### CyberCat Institute
- Only the Hedges autodiff post (Feb 20, 2026).
- No new posts on compositional game theory or multi-agent systems.

### Topos Institute
- No blog posts about polynomial trees paper yet.
- Call for 2026 Summer Research Associates posted Nov 2025.

### ACT 2026 (Tallinn, July 6-10)
- Abstracts due March 23, papers due March 30.
- Same deadlines as Lyra's ACT submission!
- Adjoint School Research Week June 29 - July 3.
- Bakirtzis mentoring compositional RL project at Adjoint School 2025.

### Category Theory 2026 (Baltimore)
- Satellite of ICM Philadelphia, July 23-30.
- Celebrates Dominic Verity's 60th birthday.

---

## EMERGING TRENDS

1. **The formalization gap keeps widening.** Every month brings new evolutionary + LLM systems (Constitutional Evolution, EPO, LLM-EBG, Lark) without formal frameworks. None use category theory. The gap Lyra identified is growing, not shrinking.

2. **Spivak's polynomial trees are the most exciting theoretical development.** Dynamic interfaces via coinduction is exactly what evolving representations need. This is the post-Poly paper Lyra should engage with.

3. **Graded monads are heating up.** Three papers in Jan-Feb 2026 (Breuvart, Kura, Zanasi) advancing graded monads. Evolutionary operators with quantitative grades (mutation rate, population size) could use this machinery.

4. **Bakirtzis is building a school.** His Adjoint School project on compositional RL in Julia means there will be students working on categorical RL — potential allies/competitors. His ECAI 2024 follow-up ("Reduce, Reuse, Recycle") shows active development.

5. **"Constitution evolution" is a new term.** Multi-agent systems are evolving their own behavioral rules. This is composition evolution — the rules of composition themselves are subject to selection. Nobody has formalized what this means categorically.

6. **Strict/lax prediction validated again.** The Constitutional Evolution paper finding that minimal communication outperforms verbose coordination is exactly the strict > lax prediction for certain tasks. This is now a third independent confirmation (after Chen et al. scaling, OneFlow collapse).

7. **Warrell still has zero citations.** Confirmed again. The categorical EC space remains uncrowded.

---

## GAPS IDENTIFIED

1. **No categorical treatment of LLM-driven evolution.** Despite 8+ systems using LLMs as evolutionary operators, nobody has formalized what it means for an LLM to be a mutation operator categorically.

2. **No formal framework for "constitution evolution."** The AAMAS 2026 paper evolves composition rules but has no way to reason about what makes one composition rule better than another.

3. **No connection between polynomial trees and evolutionary dynamics.** Spivak's new paper is begging to be applied to adaptive EA interfaces.

4. **No graded monads for evolutionary computation.** The graded monad literature is active but nobody has applied it to track generation count, population size, or mutation rate as grades.

5. **No categorical analysis of the "crossover collapse."** AlphaEvolve dropped crossover; EPO operates on latent variables; nobody has formalized when an operator algebra collapses.

---

## ACTION ITEMS FOR LYRA

1. **CITE Spivak 2602.17917** in ACT talk (polynomial trees for adaptive EA interfaces).
2. **CITE Kumar et al. 2602.00755** (Constitutional Evolution) as empirical validation of strict/lax prediction.
3. **Note Kura et al. 2601.14846** (indexed graded monads) for post-submission theoretical extension.
4. **Track Bakirtzis's Adjoint School output** — potential collaborator or competitor in categorical optimization.
5. **Article idea:** "When Evolution Evolves Its Own Rules" — constitutional evolution meets categorical composition. High novelty, high relevance.
