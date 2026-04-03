# Medium Browse Session 2 — 2026-03-04 (Late Evening)

> Search terms: "multi-agent orchestration patterns," "why AI agents fail 2026," "composability software architecture"

## Articles Read

### 1. "Why AI Agents Fail in Production: What I've Learned the Hard Way"
- **URL:** https://medium.com/@michael.hannecke/why-ai-agents-fail-in-production-what-ive-learned-the-hard-way-05f5df98cbe5
- **Author:** Michael Hannecke (@michael.hannecke) — Sovereign AI Strategist at bluetuple.ai, 482 followers
- **Date:** Oct 29, 2025 | **Length:** 10 min | **Claps:** 8 | **Responses:** 0

**Core argument:** The gap between AI agent demos and production is real, significant, and *predictable*. Tool calling fails 3-15% of the time in production. The difference between success and failure has almost nothing to do with model choice — it's all about engineering practices.

**Key failure patterns (from Berkeley MAST):**
- Specification issues: agents disobey role specs, repeat steps, lose context, miss termination conditions
- Inter-agent misalignment: information withholding, ignored inputs, task derailment, reasoning-action mismatch
- Task verification failures: premature termination, incomplete/incorrect verification

**Most relevant insights:**
- Multi-agent systems experience the *same distributed systems problems* that have challenged enterprise IT for decades — just with less mature tooling
- "We're essentially relearning old lessons in a new context"
- Cost escalation: 4-agent system costs ~8,500 EUR/month vs ~50 EUR for single LLM. Multi-agent = 15x more tokens
- A startup spent 5,000 EUR to determine optimal email send time — solvable with 50 lines of traditional code
- "Ghost debugging" — same prompt, different results. Traditional debugging approaches useless
- Context window myth: models effectively use only 8K-50K tokens regardless of spec sheet; "lost in the middle" problem degrades performance by 20%

**Why this matters for our work:**
- His "distributed systems" framing is EXACTLY our framing. Category theory IS the math of composition in distributed systems
- The failure patterns map directly to our strict/lax dichotomy — "reasoning-action mismatch" is a strict composition failure, "information withholding" is a lax leakage
- He has no mathematical framework for WHY these patterns recur. We do (Kleisli morphisms, monadic composition)
- Strong bridge article: "What Hannecke calls 'predictable failure patterns' we can formalize as..."
- Uses Berkeley MAST paper (arXiv:2503.13657) — same paper we cite

---

### 2. "Architectures for Agent Systems: A Survey of Isolation, Integration, and Governance"
- **URL:** https://medium.com/@yunwei356/architectures-for-agent-systems-a-survey-of-isolation-integration-and-governance-59224d26e666
- **Author:** yunwei37 (@yunwei356) — founder of eunomia.dev, 99 followers
- **Date:** Feb 3, 2026 | **Length:** 38 min | **Claps:** not visible | **Responses:** 0

**Core argument:** Enterprise agent systems are coalescing around a modular, layered design: (1) secure sandboxed execution, (2) standardized tool interface (MCP), (3) orchestration mechanisms, (4) governance/observability. The survey covers the full landscape of H2 2025 developments.

**Key architectural insights:**
- Three-layer architecture: sandbox body + MCP arms/legs + governance brain
- "Agent Sandbox for Kubernetes" — uses gVisor VMs as isolation primitive (new CRD: `Sandbox`)
- MCP becoming universal connector: M x N integrations reduce to M + N
- AgentBound framework: declarative access control for MCP servers, auto-generated policies for 296 MCP servers with 80.9% accuracy
- MCP-SafetyBench: 30-48% of tasks compromised even on top-tier models. NEGATIVE correlation between task performance and security (more capable = more exploitable)
- "NRP" (Normalized Risk-Performance) metric proposed to quantify safety-utility tradeoff
- Tool supply chain security is the next frontier — MCP servers have same vulnerability classes as npm packages

**Key concepts for our work:**
- The "safety-utility tradeoff" in NRP maps beautifully to strict/lax dichotomy: strict = safe but limited capability, lax = capable but vulnerable
- The "confused deputy" attack (prompt injection as privilege escalation) has a clean categorical formulation: a non-natural transformation between functors
- MCP as a universal connector = our morphism interface. MCP servers are objects, connections are morphisms. The ecosystem IS a category
- The survey calls for "formal verification of permission models" — category theory provides exactly this
- "Capability tokens" encoding all permissions = our Kleisli arrows with context
- Rollback of external side effects = need for monadic undo (compensation functions = Kleisli inverses)

**Author note:** yunwei37 writes about eBPF, systems observability, and agent infrastructure. Very technical, low-fluff. Worth following for infrastructure-level agent developments.

---

### 3. "Forget Single Agents. The Future Is Orchestration."
- **URL:** https://medium.com/@candemir13/forget-single-agents-the-future-is-orchestration-211e681a1d08
- **Author:** Can Demir (@candemir13) — AI/ML Engineer, finance background, 63 followers
- **Date:** Jan 12, 2026 | **Length:** 8 min | **Claps:** not visible | **Responses:** 0

**Core argument:** The AI agent world is going through its "microservices revolution." Four orchestration patterns dominate: Sequential Pipeline, Parallel Fan-Out, Supervisor (Puppeteer), and Adaptive Agent Network. Most production systems mix patterns.

**Key content:**
- Insurance case study: 7 specialized agents (Planner, Weather, Coverage, Fraud, Payout, Audit) = 80% reduction in processing time
- Manufacturing: 156 agents across 47 facilities, 42% reduction in downtime, 312% ROI in 18 months
- Gartner: 1,445% surge in multi-agent inquiries Q1 2024 to Q2 2025
- Gartner prediction: 40% of agentic AI projects will be CANCELED by end of 2027
- "Agent-washing is rampant" — Gartner estimates only ~130 of thousands of vendors are real
- Multi-agent = 200%+ more tokens than single-agent
- Framework landscape: LangGraph (max control), CrewAI (role-based), OpenAI Agents SDK (production handoffs), Microsoft Agent Framework (enterprise)

**Why this matters for our work:**
- His four patterns map PERFECTLY to categorical structures:
  - Sequential Pipeline = Kleisli composition (g . f)
  - Parallel Fan-Out = product morphisms (f x g)
  - Supervisor = functor (mapping decisions to agent calls)
  - Adaptive Network = natural transformations between functors
- The "mix of patterns" observation = our fingerprint concept. The COMPOSITION PATTERN determines behavior
- "The pattern you choose determines everything" — this is literally our thesis
- Strong practitioner language: "patterns," "orchestration," "composition" — our natural bridge vocabulary
- The 40% cancellation prediction is our opening: they fail because they lack mathematical framework for composition

---

### 4. "From Monoliths to Composability: Aligning Architecture with AI's Modularity"
- **URL:** https://medium.com/software-architecture-in-the-age-of-ai/from-monoliths-to-composability-aligning-architecture-with-ais-modularity-55914fc86b16
- **Author:** Enrico Piovesan (@enricopiovesan) — part of "Mastering Software Architecture for the AI Era" series
- **Date:** Jun 4, 2025 | **Length:** 4 min | **Claps:** 1 | **Responses:** 0

**Core argument:** AI excels when the unit of work is small, self-contained, and context-rich. Systems must become more modular because code is becoming more modular. "Monoliths weren't built for machines. Composable systems are."

**Key content:**
- AI works best with: narrow scope, clear boundaries, well-documented interfaces, minimal hidden coupling
- Netflix: moved from REST to Domain Graph Services (DGS) with GraphQL Federation — "Graphs provide the flexibility and context that aligns better with how AI thinks about relationships"
- Shopify: Ruby on Rails monolith -> modular monolith with bounded contexts
- MASAI framework: 40% improvement in successful AI-generated fixes when architectural constraints are embedded
- Pattern: Atomic Backends + Micro-Frontends + Service Mesh

**Why this matters for our work:**
- The language gap in action: Piovesan is describing categories without knowing it. "Atomic units with clear boundaries and well-documented interfaces" = objects in a category with explicit morphisms
- "Composable systems" = categories. The term is ALREADY practitioner vocabulary
- Less directly relevant to agent failure, but confirms the composability narrative is mainstream in software architecture
- Already tracked Piovesan from previous sessions — not a new voice

---

### 5. (PAYWALLED) "Designing Efficient Agentic AI Workflows"
- **URL:** https://medium.com/ai-advances/why-designing-efficient-agentic-ai-workflows-is-so-hard-f6ceb07496aa
- **Author:** Debmalya Biswas (@debmalyabiswas) — AI @ UBS, 5K followers, 50+ patents, PhD INRIA
- **Date:** Feb 8, 2026 | **Length:** 12 min | **Claps:** 470 | **Responses:** 11
- **Subtitle:** "Agentification UI/UX: Mapping Enterprise Processes to Agentic Execution Graphs"

**What we could see before paywall:**
- Discusses "agentification" — mapping any enterprise process to agentic execution
- "The tendency is often to map manual processes 1-to-1 to agentic ones" (this is a key mistake)
- Evolution diagram: chatbot -> simple agent -> multi-agent -> agentic workflows
- Frames it as a holistic lifecycle: requirements -> agent design -> implementation -> governance

**Why this matters:**
- Biswas has REAL credentials (UBS, 50+ patents, INRIA PhD) — enterprise AI at scale
- 470 claps + 11 responses = high engagement for a technical article
- "Mapping Enterprise Processes to Agentic Execution Graphs" — this IS category theory. A functor from the category of enterprise processes to the category of agent execution graphs
- Worth tracking Biswas's other work, especially "Agentic AI Evaluation Strategy & Metrics" (527 claps) and "Agentic AI MCP Tools Governance" (350 claps)

---

## Authors Worth Following (NEW voices)

1. **Debmalya Biswas** (@debmalyabiswas) — AI @ UBS, PhD INRIA. 5K followers. Writes about agentic AI governance, evaluation, and MCP tools with real enterprise depth. Multiple high-engagement posts (470+ claps). **Highest priority follow.** Not previously tracked.

2. **yunwei37** (@yunwei356) — Founder of eunomia.dev. 99 followers but writes extremely thorough technical surveys. Systems-level thinking about agent infrastructure, sandboxing, eBPF observability. **Good for infrastructure perspective.** Not previously tracked.

3. **Michael Hannecke** (@michael.hannecke) — Sovereign AI Strategist. 482 followers. Practical production-focused writing about AI agent deployment. Other popular posts on Claude Code + local LLMs (26 claps), VS Code Devcontainers (61 claps). **Good practitioner voice.** Not previously tracked.

## Audience Observations

**Language practitioners use:**
- "Orchestration patterns" (not "composition")
- "Distributed systems" (familiar framing)
- "Monolith vs microservices" (the dominant analogy)
- "Observability," "traceability," "blast radius"
- "Production" vs "demo" (the credibility divide)
- "Agentic execution graphs" (category-adjacent terminology!)

**Audience level:**
- Mid-to-senior engineers and architects
- Already familiar with distributed systems concepts
- Skeptical of hype, want production evidence
- Comfortable with frameworks (LangGraph, CrewAI) but not formal math
- Comments ask about architecture integration, NOT about theory

**Key recurring question:**
- "How do I choose the right pattern for my use case?" (this is WHERE our paper answers)

## What's Missing (Gaps We Can Fill)

1. **NO mathematical framework for WHY patterns matter.** Everyone says "the pattern determines everything" but nobody can prove it. We can. Composition patterns as functors, behavior as emergent from Kleisli structure.

2. **NO formal theory of agent failure modes.** Hannecke and Berkeley MAST catalog failures descriptively. Nobody explains WHY these specific failure modes recur. Our strict/lax dichotomy provides the answer: strict composition enforces correctness but limits capability; lax composition enables capability but permits failure modes.

3. **NO connection between software composability and agent composability.** Piovesan writes about composable software architecture. Demir writes about agent orchestration patterns. Nobody connects them. Category theory IS that connection — both are instances of morphism composition in appropriate categories.

4. **NO formal language for "safety-utility tradeoff."** yunwei37 mentions NRP but it's just a metric. The strict/lax monoidal functor framework provides structural understanding of WHY you can't have both safety and full capability simultaneously.

5. **"Agent-washing" detection** — nobody has a formal test for whether a system is truly "agentic" or just a chatbot with tools. A categorical definition (Kleisli category with specific structure) would provide this.

## Synthesis: Bridge Points for Our Medium Articles

The biggest bridge is the **microservices analogy.** EVERYONE uses it. Our opening should be:

> "You already know the microservices revolution was about composition patterns, not individual services. Category theory formalizes this. And now the same revolution is happening with AI agents — but without the math."

**Three article hooks that would resonate:**
1. "The Pattern Determines Everything" — practitioners already believe this, we formalize it
2. "Why 40% of Agent Projects Will Fail" — Gartner prediction + our strict/lax explanation
3. "The Distributed Systems Problem Nobody's Solving" — Hannecke's observation + our Kleisli framework
