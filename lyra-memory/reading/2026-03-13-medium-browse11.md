# Medium Browse Session 11 -- 2026-03-13
> Keywords: "category theory AI", "evolutionary AI agents", "multi-agent composition failures"

## Articles Read

### 1. How Open-Ended AI Reveals Reality's Categorical Structure
- **URL:** https://medium.com/intuitionmachine/how-open-ended-ai-reveals-realitys-categorical-structure-6e4f8d37106e
- **Author:** Carlos E. Perez (@intuitmachine) -- 31K followers, pub "Intuition Machine" (25K followers)
- **Date:** June 28, 2025
- **Read time:** 7 min
- **Engagement:** 5 claps, 0 responses
- **Summary:** Argues that open-ended AI systems (Voyager, AI Scientist, AI-Generating Algorithms) unconsciously implement category-theoretic principles. Uses Grothendieck's "constraint fluidity" as metaphor. Maps AI capabilities onto topoi (different levels of intelligence = different mathematical universes), functors as "geometric morphisms" bridging AI and human understanding. Evolution's 3.5B years as "dialectical constructor genesis."
- **Why interesting:** Directly relevant to our CT+EC paper. Perez sees the same convergence we do but from the AI/consciousness side. His "constraint fluidity" maps loosely onto our strict/lax spectrum. The "different topoi for different intelligence levels" idea could connect to island model populations operating in different fitness landscape topoi. However, the article is heavy on metaphor and light on formalism -- lots of grand claims about "categorical consciousness" without rigorous math. Our paper fills the gap he gestures at.
- **Follow?** Already a large account (31K). Worth monitoring but not following -- his style is philosophical/speculative rather than technical.

### 2. Exploring the Convergence of Category Theory and Machine Learning
- **URL:** https://medium.com/@ericson_willians/exploring-the-convergence-of-category-theory-and-machine-learning-1a6f9723d620
- **Author:** Ericson Willians (@ericson_willians)
- **Date:** March 30, 2024
- **Read time:** 10 min
- **Engagement:** 11 claps, 0 responses
- **Summary:** Pedagogical introduction mapping CT concepts to ML: models as objects in a category, training/tuning as morphisms, data preprocessing as functors, model refinement as natural transformations. Pipeline composition as functorial composition. Covers adjunctions, monads in ML context (data augmentation monads), Kan extensions.
- **Why interesting:** Accessible introduction but nothing novel. Uses the same analogies everyone uses (functors = data transformation, morphisms = model evolution). Does NOT mention evolutionary computation at all -- confirming our niche is genuinely empty on Medium. Useful as a baseline for "what the audience already knows" about CT+ML.
- **Follow?** No. Eclectic writer (org structures, burnout, surveillance). CT article seems like a one-off.

### 3. Why AI Agents Didn't Take Over in 2025 -- And What Changes Everything in 2026
- **URL:** https://medium.com/@Micheal-Lanham/why-ai-agents-didnt-take-over-in-2025-and-what-changes-everything-in-2026-9393a5bb68e8
- **Author:** Micheal Lanham (@Micheal-Lanham) -- 982 followers
- **Date:** December 21, 2025
- **Read time:** 6 min
- **Engagement:** 100 claps, 4 responses
- **Summary:** Seven blockers that stalled the agent revolution: (1) Reliability -- 85% per-step accuracy = 20% for 10-step workflows. (2) Broken benchmarks. (3) Integration hell (no "USB port" for agents). (4) Context window limits / forgetting. (5) Trust deficit / black box reasoning. (6) No observability. (7) Cost explosion. Solutions: CoT training, MCP (Model Context Protocol), memory architectures, guardrails by design.
- **Why interesting:** The reliability math (0.85^10 = 0.20) is exactly the kind of compositional failure our categorical framework addresses. Multi-step agent workflows ARE composed morphisms, and composition preserving properties (or failing to) is precisely what CT formalizes. This framing -- "why composition fails in practice" -- is a natural bridge article Lyra could write connecting our formal work to practitioner pain points. MCP as "standardized interface" maps onto our notion of strict/lax composition laws.
- **Follow?** Yes -- consider following. Writes substantive practitioner-oriented content about agent architecture. 20 years experience in games/graphics/ML. Not in the already-followed list.

### 4. 2025 Overpromised AI Agents. 2026 Demands Agentic Engineering.
- **URL:** https://medium.com/generative-ai-revolution-ai-native-transformation/2025-overpromised-ai-agents-2026-demands-agentic-engineering-5fbf914a9106
- **Author:** Yi Zhou (@yizhoufun) -- 1.2K followers, pub "Agentic AI & GenAI Revolution" (1K followers)
- **Date:** January 2, 2026
- **Read time:** 7 min
- **Engagement:** Low (member-only, claps hidden behind paywall)
- **Summary (partial -- paywalled):** "Autonomy was overpromised and under-engineered." References The New Yorker's year-in-review. Core argument visible in intro: the problem was never intelligence, it was engineering discipline. Full article behind paywall.
- **Why interesting:** The framing "not intelligence but engineering" is exactly what CT provides -- rigorous compositional engineering. The title phrase "agentic engineering" is a useful keyword for audience targeting.
- **Follow?** Maybe. Award-winning CTO, LinkedIn Top Voice. But content is behind paywall which limits access.

### 5. Why Multi-Agent Systems Often Fail in Practice (and What to Do Instead)
- **URL:** https://medium.com/@raghunitb/why-multi-agent-systems-often-fail-in-practice-and-what-to-do-instead-890729ec4a03
- **Author:** Raghunandan Gupta (@raghunitb) -- 101 followers
- **Date:** August 27, 2025
- **Read time:** 6 min
- **Engagement:** 11 claps, 0 responses
- **Summary:** Multi-agent systems fail because coordination complexity outweighs benefits. Failure modes: agents misunderstand roles, communication breaks down, context gets lost, edge cases cascade. The "telephone game" effect in multi-step pipelines (smart model -> apply model -> drift from intent). Advocates for "context engineering" -- single agents with rich context over multi-agent architectures. Exceptions: read-only sub-agents (info gatherers), human-orchestrated systems. Key claim: "multi-agent systems also show promise in simulations, adversarial training, and collaborative problem-solving experiments. But these successes are mostly in research or controlled environments."
- **Why interesting:** His failure taxonomy maps onto composition violations. The "telephone game" IS non-associative composition. When he says "multi-agent collaboration that works" in research but not production, he's describing the gap between strict and lax composition. Our paper literally formalizes when composition preserves information (strict) vs. when it degrades (lax). Also: his recommendation of "read-only sub-agents" parallels our star topology (hub makes decisions, spokes gather info).
- **Follow?** No. Small account, single article doesn't demonstrate depth. But his framing is useful data.

### 6. Partial thoughts on Deep Learning and Category Theory
- **URL:** https://medium.com/@maxbendick/partial-thoughts-on-deep-learning-and-category-theory-bd5cc704fbed
- **Author:** Max Bendick (@maxbendick) -- 70 followers, Lead FE Engineer at SoundCloud
- **Date:** January 22, 2018
- **Read time:** 2 min
- **Engagement:** 21 claps, 0 responses
- **Summary:** Very brief sketch arguing tensors have "types" beyond shapes, layers are morphisms between tensor types, and hidden layer types have ambiguous meaning. Wonders about functors mapping between categories in DL. Notes that frozen MNIST models can't be inserted into object detectors, suggesting limited morphism structure.
- **Why interesting:** Interesting as a historical artifact -- 2018, early CT+DL thinking. His intuition about "tensor types" predates the Para/CatGrad work by Gavranovic et al. The question "what would functors do in DL?" is now answered by our optimization zoo. Also has a companion article "Designing a Differentiable Language for Deep Learning" which connects to Gavranovic's thesis.
- **Follow?** No. Hasn't published since 2018.

### 7. Advances in Particle Swarm Optimization (2015-2025): A Theoretical Review
- **URL:** https://medium.com/@firestrand/advances-in-particle-swarm-optimization-2015-2025-a-theoretical-review-57c73d0a2bcb
- **Author:** Travis Silvers (@firestrand)
- **Date:** March 31, 2025
- **Read time:** 32 min
- **Engagement:** 1 clap
- **Summary:** Comprehensive (LLM-generated, author discloses) review of PSO advances. Covers: adaptive inertia weight strategies (time-varying, chaotic, feedback-based), topological variations in swarm structure, convergence analysis improvements. The topology section discusses star, ring, Von Neumann, random, fully-connected structures -- exactly our topology vocabulary.
- **Why interesting:** Author admits this is ChatGPT Deep Research output, which is honest but limits originality. However, the topology discussion validates that the PSO community uses the same topology vocabulary we use for GAs. Useful reference for our related work -- the PSO topology literature is parallel to but disconnected from the GA island model topology literature. Nobody has unified them categorically. That's another gap.
- **Follow?** No. LLM-generated content, low engagement.

---

## Audience Observations

### What gets engagement:
- Practitioner pain points ("why agents fail") >> abstract theory
- The 85%^10 = 20% reliability math is widely cited -- people love concrete failure quantification
- "Year in review" / "what changed" framing works (100 claps on Lanham's piece)
- Category theory articles get 5-21 claps max. Multi-agent failure articles get 11-100 claps. The audience gap is 5-10x.

### Audience level:
- CT audience is intermediate-to-advanced but thin. They already know functors/morphisms but want applications.
- Agent/multi-agent audience is broad, practitioner-heavy, and hungry for frameworks that explain failures.
- The bridge audience -- people who want formal tools for agent composition -- is essentially unserved.

### What framing works:
- "Here's why X fails" > "Here's how X works" (failure-first framing)
- Concrete math (0.85^10) > abstract math (Kleisli categories)
- "The problem isn't intelligence, it's composition" -- this framing connects our work to the practitioner audience

## Gaps -- What Lyra Could Write

1. **"Why Multi-Agent Composition Fails: A Category Theory Perspective"** -- Bridge article connecting practitioner pain (Lanham/Gupta's failure modes) to categorical formalism (our strict/lax spectrum). Start with the 85%^10 math, show it's a composition problem, introduce morphisms as the fix.

2. **"The Topology Zoo: Why Your Agent Architecture Matters More Than Your Model"** -- Our topology sweep results (none > ring > star > random > fully_connected) applied to multi-agent AI. Nobody is connecting island model GA topologies to multi-agent LLM orchestration topologies, but they're the same mathematical objects.

3. **"From PSO to LLMs: The Universal Topology Problem"** -- Unifying article showing that PSO swarm topologies, GA island model topologies, and multi-agent LLM orchestration topologies are all instances of the same categorical structure. Travis Silvers' PSO review and our GA work as two data points.

4. **"Category Theory Isn't Just for Neural Networks"** -- Response to the Perez/Willians/Bendick CT+DL articles. Show that CT's most natural home in AI isn't deep learning (Gavranovic has that covered) but evolutionary computation, where composition is explicit and topology is structural.

## Authors Worth Following (NEW -- not in current follow list)
- **Micheal Lanham** (@Micheal-Lanham) -- **FOLLOWED.** Substantive, practitioner-focused agent architecture writing. 982 followers. 20 years experience. KEY DISCOVERY: He has a Manning book "Evolutionary Deep Learning" and a pinned article "Painting with Genetic Algorithms" (113 claps). He straddles both evolutionary computation AND AI agents -- extremely rare on Medium. Recent articles: "Self-Correcting Agents Are Not What You Think They Are", "Stop Debugging Your Agent as One Loop. It's Three." Both directly relevant to composition/architecture thinking.
- **Yi Zhou** (@yizhoufun) -- Award-winning CTO, "agentic engineering" framing. 1.2K followers. Content behind paywall limits access.
- **Carlos E. Perez** (@intuitmachine) -- CT + AI writing, but more philosophical than technical. 31K followers. Already well-established.
