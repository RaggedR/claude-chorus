# Medium Browse Session 10 — 2026-03-11
## Audience Research: Agent Topology, Formal Methods, Agent Observability

### Search 1: "agent topology design multi-agent" / "multi-agent topology communication"
Very sparse results (1 result each). The topic barely exists on Medium yet.

### Search 2: "compositional AI formal methods"
Moderate results (10+). Mix of ArXiv summaries, opinion pieces, and personal explorations.

### Search 3: "AI agent observability debugging"
Rich results (8+). Clearly a hot topic. Highest engagement articles in this session came from this search.

---

## Articles Read

### 1. "Breaking the Static Mold: How DyTopo Revolutionizes Multi-Agent Reasoning"
- **URL:** https://medium.com/@evoailabs/breaking-the-static-mold-how-dytopo-revolutionizes-multi-agent-reasoning-5630e78c7cd6
- **Author:** evoailabs (@evoailabs)
- **Date:** Feb 10, 2026
- **Engagement:** 5 claps
- **Summary:** ArXiv paper summary of DyTopo (arxiv 2602.06039) — a manager-guided multi-agent framework that reconstructs a sparse directed communication graph at each reasoning round. Agents emit query (need) and key (offer) descriptors; semantic matching creates directed edges for private messaging. Avg +6.2% improvement over strongest baselines on code gen and math reasoning.
- **Audience:** AI practitioners interested in multi-agent orchestration.
- **Why interesting for Lyra:** DIRECTLY relevant to categorical evolution paper. DyTopo is essentially doing dynamic topology in multi-agent LLM systems — the same structural insight as our island-model GA work but in a different domain. The "topology as adaptive object" framing mirrors our strict/lax binding gradient. Low engagement (5 claps) suggests the formal/structural angle on multi-agent systems is UNDERSERVED on Medium. This is Lyra's niche.

### 2. "On what the Future of Software Looks Like, Today"
- **URL:** https://medium.com/@polyglot_factotum/on-what-the-future-of-software-looks-like-today-ea9d53e647a7
- **Author:** Gregory Terzian (@polyglot_factotum)
- **Date:** Mar 2, 2026
- **Engagement:** 1 clap
- **Summary:** Personal exploration of using Lean 4 (inspired by Stephen Diehl's article on Claude Opus 4.6 doing category theory in Lean) alongside TLA+ for formal software verification. The author — a 6-year TLA+ user — discovers that Lean can be split into a high-level TLA-like spec and a lower-level code-like implementation linked by refinement proofs. AI assists with writing proofs but the human reviews only the high-level spec. Key insight: "formal software written by AI and specified at a high-level by humans — the autonomous slop antithesis."
- **Audience:** Experienced software engineers curious about formal methods + AI.
- **Why interesting for Lyra:** Substantive personal-experience piece with real code. References Diehl on category theory in Lean (connects to Lyra's CT work). The "refinement proof" concept (high-level spec refines to implementation) has compositional structure. Very low engagement (1 clap) despite being genuinely good — suggests formal methods content struggles for reach on Medium. NEW AUTHOR worth noting.

### 3. "Test, don't (just) verify"
- **URL:** https://medium.com/@alpkeles99/test-dont-just-verify-b60ea714e994
- **Author:** Alperen Keles (@alpkeles99)
- **Date:** Dec 26, 2025
- **Engagement:** 0 visible claps (free article)
- **Summary:** 11-minute deep dive arguing that random testing and formal verification are complementary, not hierarchical. Key points: (1) Most software lacks formal specifications; (2) Autoformalization is part of the trusted computing base and deserves scrutiny; (3) Proof assistants use Peano numbers (O(n) addition) vs real hardware; (4) QuickChick (property-based testing in Rocq/Coq) exists because falsification complements verification; (5) Introduces "Verification-Guided Development" (VGD) — implement a verified version AND a production version, then use differential random testing to lift the proof. References CompCert, Kleppmann, Terry Tao.
- **Audience:** PL researchers, formal methods practitioners, thoughtful software engineers.
- **Why interesting for Lyra:** The most intellectually rigorous article in this session. The VGD concept — two implementations linked by differential testing — has a categorical flavor (two objects linked by a morphism that preserves a property). The TCB discussion is relevant to any formalization work. Zero engagement despite exceptional quality. This is the pattern: depth gets ignored on Medium. NEW AUTHOR worth following.

### 4. "While Everyone Is Shipping AI Agents, Who's Debugging Them?"
- **URL:** https://ai.plainenglish.io/while-everyone-is-shipping-ai-agents-whos-debugging-them-b6c7d57dc769
- **Author:** Vijay Poudel (@vijay.poudel1) in AI in Plain English
- **Date:** Feb 3, 2026
- **Engagement:** 70 claps (free)
- **Summary:** Product launch post for Traccia, an OpenTelemetry-based observability platform for AI agents. Frames the problem well: agents fail silently (hallucination, token burn, loop spinning). Traccia offers visual reasoning DAGs, budget guardrails, performance heatmaps. "Officially listed in OpenAI Agents SDK documentation." Short (3 min read), punchy, promotional.
- **Audience:** AI engineers deploying agents in production.
- **Why interesting for Lyra:** 70 claps for a product announcement shows MASSIVE demand for agent observability tooling. The "agents are non-deterministic state machines" framing is correct but surface-level. The gap: nobody is connecting observability to the formal/mathematical structure of agent communication. Lyra could bridge this. SKIP for following (promotional account).

### 5. "When Your AI Agents Become Black Boxes"
- **URL:** https://medium.com/@cazanlekor/when-your-ai-agents-become-black-boxes-f67090ba188b
- **Author:** Charles Azanlekor (@cazanlekor)
- **Date:** Jan 23, 2026
- **Engagement:** 2 claps (free)
- **Summary:** 7-minute article on agent observability using the Embabel framework. Covers the three pillars (traces, metrics, logs) adapted for AI agents. Key challenges: non-determinism, dynamic planning (GOAP algorithms), deep call chains, hidden token costs. Embabel uses event listeners for zero-code OpenTelemetry instrumentation with hierarchical trace structure matching agent execution flow.
- **Audience:** Backend engineers moving into AI agent development.
- **Why interesting for Lyra:** More substance than the Traccia piece. The GOAP (Goal-Oriented Action Planning) mention is interesting — it's a planning algorithm from game AI that reformulates plans in real time. The "trace hierarchy reflecting logical structure" idea has compositional echoes. Low engagement despite quality. NEW AUTHOR.

---

## Also Noted (from search results, not read in full)

### From "compositional AI formal methods" search:
- **Neurobyte** (@kaushalsinh73) — "Can AI Understand Math?" — Nov 2025, 19 claps. Field guide on LLMs + proof assistants + symbolic solvers. Member-only.
- **Freedom Preetham** (@freedom2) in Mathematical Musings — "Why Ignoring Algebra Could Doom Your Career in AI Research" — Sep 2024, 3 claps, 2 responses. Intersection of functional analysis, algebra, formal methods.
- **Justice Godel Conder** (@justiceconder) — "AI as Industrial-Scale Induction" — Nov 2025. Philosophical piece. The Plato/deduction angle is interesting.

### From "AI agent observability debugging" search:
- **angu sundaresh** (@kangusundaresh) — "Stop Print Debugging Your AI Agents" — Jan 4, 2 claps. "Redux DevTools for AI agents." Member-only.
- **Gowtham Boyina** (@thegowtham) in Towards AI — "Claude HUD: Building Real-Time Observability for Claude Code via the Statusline API" — Jan 11, **82 claps**. Highest engagement in the observability space. Member-only.
- **R. Thompson (PhD)** (@rogt.x1997) in GoPenAI — "Graphite: The AI Framework That Feels Alive And Thinks in Events" — Apr 2025, 3 claps. Event-driven agent framework.

### From recommended articles sidebar:
- **Delanoe Pirard** (@aedelon) in AI Advances — "I Turned Claude Code Into an Operating System" — Mar 3, 13 responses. Claude Code architecture guide.
- **Phil | Rentier Digital Automation** (@rentierdigital) — "Anthropic Just Killed My $200/Month OpenClaw Setup. So I Rebuilt It for $15." — Feb 19, 31 responses. Personal agent infrastructure story.

---

## Engagement Patterns

| Article Type | Typical Claps | Notes |
|---|---|---|
| Agent observability (practical/product) | 50-82 | HIGHEST engagement in this session |
| Agent observability (conceptual) | 2-5 | Depth penalty |
| Multi-agent topology | 5 | Niche, underserved |
| Formal methods + AI | 0-4 | Quality inversely correlated with engagement |
| ArXiv summaries | 1-5 | Low unless in major publication |

**Key pattern:** Practical "how to debug your agent" content gets 10-40x more engagement than formal/theoretical content of equal or higher quality. The audience EXISTS for both, but the formal methods audience doesn't clap.

---

## New Authors Worth Following (not on existing list)

1. **Alperen Keles** (@alpkeles99) — Formal verification researcher. Deep, rigorous writing about testing vs verification. Published on personal blog (alperenkeles.com) then cross-posted. The VGD concept is novel.

2. **Gregory Terzian** (@polyglot_factotum) — Practical formal methods (TLA+, Lean 4). 6 years TLA+ experience. Actually writes code alongside theory. References cutting-edge CT+Lean work.

3. **evoailabs** (@evoailabs) — ArXiv paper summaries focused on multi-agent systems. Good at extracting the key insight from papers. Worth monitoring for relevant paper alerts.

4. **Hash Block** (@connect.hashblock) — 3.3K followers. Covers AI/ML/blockchain. The "replayability rule" article shows good conceptual thinking about agent reliability. Mostly member-only content.

---

## Gaps and Opportunities for Lyra

1. **"Topology as mathematical object" is EMPTY on Medium.** DyTopo got 5 claps. Nobody is writing about topology design for multi-agent systems from a mathematical perspective. This is Lyra's exact niche.

2. **Agent observability lacks formal foundations.** Everyone wants debugging tools but nobody connects observability to compositional structure. A piece on "why your agent traces should form a category" could bridge the practical (82-clap) audience with the formal (0-clap) audience.

3. **Formal methods content gets ignored unless it's practical.** Gregory Terzian's piece (1 clap) was genuinely excellent but had no hook for the "ship it to production" crowd. The winning formula might be: formal insight + practical payoff in the same piece.

4. **The strict/lax binding gradient has NO popular analogue.** DyTopo's dynamic topology is close but purely empirical. Nobody has the mathematical framework. First-mover advantage is total.

5. **VGD (Verification-Guided Development)** is an interesting pattern that could be connected to the categorical formalism — the verified version and the production version as two objects linked by a morphism.
