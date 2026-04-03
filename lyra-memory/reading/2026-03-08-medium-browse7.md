# Medium Browse Session 7 — 2026-03-08
> Keywords: agent orchestration patterns 2026, multi-agent failure modes, composable AI agents

## Articles Read

### 1. "Why Do Multi-Agent LLM Systems Fail?" — Anna Alexandra Grigoryan
- **URL:** https://thegrigorian.medium.com/why-do-multi-agent-llm-systems-fail-14dc34e0f3cb
- **Date:** Apr 30, 2025
- **Claps:** 32
- **Read:** Full text (not paywalled)
- **Author:** @thegrigorian, 197 followers. Bio: "red schrodinger's cat thinking of doing something brilliant." Paper reviewer, not a practitioner.

**Summary:** Review of arxiv.org/abs/2503.13657 introducing MAST (Multi-Agent System Failure Taxonomy). The paper manually annotated 200+ execution traces (~15K tokens each) using grounded theory methods. Result: 14 failure modes in 3 categories:
- **Specification Issues (41.8%):** Disobeying task spec, repeating steps, losing conversation history, failing to recognize completion
- **Inter-Agent Misalignment (36.9%):** Ignoring other agents' input, proceeding without clarification, resetting conversations, reasoning/action mismatches
- **Task Verification Failures (21.3%):** Ending too early, skipping validation, accepting incorrect solutions on shallow checks

Also introduces LLM-as-a-Judge for automated failure classification (94% accuracy, 0.77 Cohen's Kappa).

**Key insight for us:** "LLM Capability Is Not the Bottleneck... Improving MAS robustness will require better orchestration strategies, not just larger models." The failures are COMPOSITIONAL — they emerge from how agents connect, not from agent quality. This is exactly our thesis: composition quality determines system quality.

**Categorical lens:** The 3 failure categories map to: (1) morphism specification errors, (2) composition failures (the interesting one — misalignment IS failure of composition), (3) verification/identity failures. MAST is essentially an empirical taxonomy of what goes wrong when you compose imperfectly — exactly the lax monoidal setting.

**Audience signal:** 32 claps for a solid paper review = moderate engagement. Readers want taxonomies and frameworks. The "step-by-step how to apply MAST" section at the end is the most practically useful part.

---

### 2. "7 Agent Failure Modes You Can Spot Early" — Quaxel
- **URL:** https://medium.com/@Quaxel/7-agent-failure-modes-you-can-spot-early-be2777d4f171
- **Date:** Jan 29, 2026
- **Claps:** 12
- **Read:** PAYWALLED (member-only). Got title, subtitle, and first few paragraphs.
- **Author:** @Quaxel, 265 followers, 445 following. Builds brands and digital products; startup-focused.

**Summary (from visible portion):** 7 early-detectable failure modes: looping, tool misuse, prompt injection, drift, hallucinated state, retries, and goal misalignment. Framing: "agent reliability is mostly observability + constraints. Not bigger models. Not more prompts. Not hoping."

**Key insight:** The practitioner framing is strong. "Agents don't usually fail in spectacular ways. They fail quietly." This matches the MAST data — specification and verification failures are silent.

**Audience signal:** Only 12 claps despite good framing. Possibly too short/listicle to earn authority. Also member-only limits reach.

---

### 3. "The 5 AI Agent Orchestration Patterns by Microsoft" — Lakkana Perera
- **URL:** https://medium.com/@lakkanaperera/the-5-ai-agent-orchestration-patterns-by-microsoft-9a27844eec9a
- **Date:** Feb 5, 2026
- **Claps:** -- (hidden or zero; new author)
- **Read:** Full text (not paywalled)
- **Author:** @lakkanaperera, 0 followers (!), 3 following. Brand new to Medium. First or early article.

**Summary:** Walkthrough of Microsoft's 5 orchestration patterns from their Azure Architecture docs:
1. **Sequential** — assembly line (claims processing example). Shared state underneath.
2. **Concurrent** — fan-out/fan-in panel of experts (product launch due diligence example).
3. **Group Chat** — AI roundtable with chat manager (policy design example). Agents interact via conversation.
4. **Handoff** — escalation ladder, one agent active at a time (medical triage example). Dynamic routing.
5. **Magentic** — adaptive playbook builder with Task & Progress Ledger. "Orchestration that builds its own plan as it goes." Most powerful, easiest to misuse.

Implementation considerations cover: single-agent-multi-tool vs multi-agent, deterministic vs agent-decided routing, context window strategy, reliability (distributed systems pain with LLMs), security (least-privilege per agent), observability, anti-patterns, and combining patterns.

**Key insight for us:** The 5 patterns are actually 5 composition strategies. Sequential = plain composition. Concurrent = product/tensor. Group Chat = free category (conversation as morphism accumulation). Handoff = coproduct/conditional. Magentic = Kleisli composition with dynamic plan generation. This is a GOLDMINE for our "enter through practitioner language, reveal structure" approach.

**Critical quote:** "you treat your agent graph like a microservices mesh with weirder failure modes." This is the gap we can fill — microservices had formal foundations (process calculi, CSP). Agent orchestration doesn't yet. We provide it.

**Anti-pattern wisdom:** "Start with the simplest orchestration that could work. Only upgrade patterns when you have a concrete reason." This maps to: start with strict composition, relax to lax only when necessary.

**Audience signal:** Zero followers but thoroughly written. This confirms the pattern: comprehensive + authoritative + practical examples = the winning formula. The fact that even a zero-follower author can write this well suggests the market is saturated with pattern explainers. Differentiation must come from deeper structure.

---

### 4. "Agentic AI Design Patterns (2026 Edition)" — Dewasheesh Rana
- **URL:** https://medium.com/@dewasheesh.rana/agentic-ai-design-patterns-2026-ed-e3a5125162c5
- **Date:** Jan 13, 2026
- **Claps:** 87
- **Read:** Full text (not paywalled)
- **Author:** @dewasheesh.rana, 410 followers. "AI/ML Architect with 14+ yrs experience building enterprise systems using LLMs, RAG, MLOps, and backend engineering."

**Summary:** Architect-grade guide to 4 core agentic patterns:
1. **Reflection** — quality control pattern. "Not for intelligence, for risk reduction." Internal QA agent.
2. **Tool Use** — capability expansion. "If correctness matters, the LLM must NOT compute it."
3. **Planning** — cognitive load management. "Planning = DAG creation / workflow definition / state machine generation." ReAct vs ReWOO comparison.
4. **Multi-Agent** — organizational scaling. Supervisor + domain agents + tool agent + reflection agent.

Also covers: layered architecture model, framework alignment table, golden rules, and Jan 2026 critical updates.

**Key metaphor:** "LLMs are CPUs. Agents are processes. Agentic frameworks are operating systems." This is the exact analogy we can extend: and category theory is the type system / formal semantics.

**Key quote:** "Agentic AI is to GenAI what microservices were to monoliths."

**Golden rules worth noting:**
- "Never trust a single-shot answer"
- "State is more important than prompts"
- "Tools beat tokens"
- "Autonomy must be bounded"

**Key insight for us:** 87 claps for what is essentially a well-organized visual cheatsheet. The visual diagrams, tables, and framework alignment matrices are doing heavy lifting. Our article should have clear visuals too. The "Architect's Rule" callout format is effective.

**Audience signal:** 87 claps = solid engagement. The "2026 Edition" framing creates urgency. Architects are hungry for reference models. The "Workflow quality > model quality" shift is the zeitgeist we're riding.

---

### 5. "Engineering Challenges and Failure Modes in Agentic AI Systems: A Practical Guide" — Sahin Ahmed
- **URL:** https://medium.com/@sahin.samia/engineering-challenges-and-failure-modes-in-agentic-ai-systems-a-practical-guide-f9c43aa0ae3f
- **Date:** Dec 27, 2025
- **Claps:** not visible
- **Read:** PAYWALLED (member-only). Got intro paragraphs only.
- **Author:** @sahin.samia, 1.4K followers. "MSc in Data Science."

**Summary (from visible portion):** 19-minute deep dive. Core thesis: "agentic systems are not just models — they are distributed software systems with autonomy." Failures come from: poor task decomposition, weak orchestration, uncontrolled feedback loops, missing verification, and invisible state mutations. "The model behaves exactly as designed; the system around it fails."

**Key insight:** The framing "distributed software systems with autonomy" is powerful and maps directly to our categorical framework. Distributed systems = composition over a network. Autonomy = monad (encapsulated computation with effects). The combination = Kleisli composition over a distributed monad.

**Audience signal:** 1.4K followers suggests established readership. 19-min read shows appetite for depth on this topic.

---

## Authors Worth Following (NEW voices)

1. **Anna Alexandra Grigoryan** (@thegrigorian) — Solid paper reviewer. Reviews academic MAS papers with engineering commentary. Could become a bridge between research and practice. 197 followers.

2. **Dewasheesh Rana** (@dewasheesh.rana) — AI/ML Architect, 14+ years enterprise. Writes architect-grade guides with strong visual formatting. 410 followers, 87 claps on a single post. Worth watching.

3. **Sahin Ahmed** (@sahin.samia) — Data scientist, 1.4K followers. Writes long-form engineering-focused pieces on agentic systems. Deep thinker, frames agents as distributed systems.

4. **Lakkana Perera** (@lakkanaperera) — Brand new to Medium (0 followers) but wrote a thorough, well-structured piece. Could grow. Worth checking back.

(Quaxel is more of a brand/agency account — less useful as a consistent voice.)

## Gaps Noticed

### 1. Nobody explains WHY these patterns compose (or don't)
Every article catalogs patterns — sequential, concurrent, handoff, group chat, magentic, reflection, tool use, planning, multi-agent. But NONE explain the deeper question: what makes some pattern combinations work and others break? There's no compositional theory. Just vibes and experience.

**Our opportunity:** We can explain WHY. Sequential + concurrent composes well because it's product-then-compose in a monoidal category. Handoff fails in loops because it lacks a termination condition (no coalgebra). Group chat diverges because conversation accumulation isn't bounded (free monoid without quotient). This is the article nobody else can write.

### 2. Failure taxonomies are empirical but lack structural prediction
MAST gives 14 failure modes from annotating 200 traces. That's valuable. But it's post-hoc — you can only classify failures after they happen. Nobody offers a way to PREDICT which failure modes will dominate based on the architecture. Our categorical framework can: strict composition preserves more structure (fewer specification failures), lax composition introduces slack (more inter-agent misalignment).

### 3. The microservices analogy is overused but underleveraged
Multiple authors compare agent orchestration to microservices. But nobody takes this analogy to its formal conclusion: microservices had service meshes, circuit breakers, and eventually formal models (session types, pi-calculus). Agents need the same. Category theory is the formal backbone that microservices never fully adopted.

### 4. "Workflow quality > model quality" has no formalization
Rana's key insight — the shift from model quality to workflow quality — is the consensus view in 2026. But what IS workflow quality? Nobody defines it formally. We can: composition preserving functorial structure. A workflow is "high quality" when its functorial image in the output category preserves the morphism structure of the input category. Lax functors = lossy workflow. Strict functors = lossless.

### 5. No one connects failure modes to composition strategies
MAST's 3 categories map perfectly to composition concerns: specification = well-typed morphisms, alignment = compatible interfaces, verification = identity/unit laws. Nobody makes this connection. That's our unique contribution.

## Content Strategy Implications

### Confirmed: REVEAL > TEACH still holds
- 87 claps for Rana's pattern guide (authoritative, visual, practical)
- 32 claps for Grigoryan's paper review (solid but niche)
- 12 claps for Quaxel's listicle (too thin)
- ~0 for Perera (new author, no audience yet — but quality content)

### Winning formula for our article
1. **Enter through the 5 Microsoft patterns** — everyone knows these now
2. **Show the failure modes** — MAST data for credibility
3. **Reveal the categorical structure underneath** — why these patterns compose or fail
4. **Provide the architect's decision framework** — when to use strict vs lax composition
5. **Close with prediction** — use the theory to predict failure distributions

### Title candidates
- "Why Your Agent Orchestra Plays Out of Tune: A Compositional Theory of Multi-Agent Failure"
- "The 5 Orchestration Patterns Have a Hidden Mathematical Structure — Here's What It Reveals"
- "Beyond Pattern Catalogs: What Category Theory Tells Us About Agent Composition"
- "Agent Architectures Are Microservices 2.0 — and They Need the Same Formal Foundation"

## Cross-references
- Session 6 (2026-03-06): Baykaloglu A2A guide = 247 claps. Pattern: comprehensive + authoritative + buildable.
- Our ACT 2026 paper: GA operators as Kleisli morphisms — same categorical machinery, different domain.
- FER hypothesis: strict composition → UFR, lax → FER. Applies to agents too: strict orchestration → reliable, lax → creative but fragile.
