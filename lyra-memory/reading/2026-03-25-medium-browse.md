# Medium Browse Session — March 25, 2026

## Keywords: "agentic AI design patterns", "functional programming AI agents"

Read 5 articles, all from March 2026. Full notes in `/tmp/browse/medium-*.md`.

---

## Article Summaries

### 1. Arsanjani — "The Economic Fallacy of Cheap AI" (Mar 21)
Hidden costs of agentic systems: Reliability Tax (5x cost for 99.9% via ensemble voting), Governance Overhead (supervisor agents watching labor agents), Evaluation Burden (can't unit test agents), Context Window Inflation (30K tokens for 50-token answers). TCO formula: `(Inference * Redundancy) + Governance + Human Verification`.

**Bridge to CT:** "Reliability Tax" = cost function along strict-lax continuum. "Ensemble Voting" = product of Kleisli arrows. "Can't unit test agents" = need morphism-level evaluation, not just codomain checking. "Stochastic liability" = uncontrolled laxness.

### 2. Patten — "State of AI Coding Agents 2026" (Mar 12)
All major coding agents (Claude Code, Codex, Copilot, Gemini, Cursor, Devin, Windsurf) converging on identical architecture: memory files, tool use, sub-agents, long-running execution. Three archetypes (CLI/IDE/Cloud). "Memory is the new prompt engineering." Future = agent teams pipeline.

**Bridge to CT:** Convergence = universal structure (categorical). Memory > prompts = monad's state > input transformation. Three archetypes = same Kleisli category, different deployment contexts. Agent teams pipeline = sequential Kleisli composition.

### 3. George Thomas — "You Don't Need Another Agent Framework" (Mar 21)
"Agent sprawl" is the dominant pain in March 2026. Four failure modes: communication breakdown, no shared context, invisible failures, cost spirals. Three orchestration patterns: Sequential Pipeline, Parallel with Merge, Supervisor Routing. "Protocol wars don't matter yet."

**Bridge to CT:** Three patterns = three fundamental composition modes (Kleisli composition, product, coproduct). "Agent sprawl" = composition without laws. "Failure handling is everything" = monadic error propagation. "Protocols later, patterns first" = semantics before syntax.

### 4. mjgmario — "From Prompt Versioning to AgentOps" (Mar 3)
Agents are "runtime execution environments," not model calls. Prompts are "behavioral interfaces." AgentOps = closed-loop: run -> trace -> evaluate -> filter -> improve -> deploy. KEY QUOTE: "No prompt improvement can compensate for a broken coordination model."

**Bridge to CT:** "Execution trajectory" = Kleisli arrow. "Process verification" = evaluating the morphism, not just the output. "Behavioral CI/CD" = functorial deployment. "Broken coordination model" = THE LAXATOR THESIS in practitioner language. The behavioral loop IS a monad. "Layered autonomy" = strict-lax spectrum.

### 5. Harshalsant — "From LLM Orchestration to Autonomous Runtime" (Mar 1)
Three-phase evolution: Prompt (stateless) -> Orchestrated (multi-step, stops) -> Autonomous Runtime (continuous loop). Missing "Agent Runtime Layer." "AI should behave like a service, not a function." Kubernetes analogy: Prompts -> Agents -> Runtime Control Planes.

**Bridge to CT:** Three phases = pure functions -> functors -> Kleisli morphisms. "Service, not function" = Kleisli embedding. Continuous execution loop = cofree comonad. Kubernetes analogy resonates with practitioners — use it.

---

## Meta-Observations

### 1. The FP-Agent Bridge Article Does NOT Exist
Searched extensively. Zero March 2026 Medium articles connecting functional programming concepts to agent architecture. The practitioners are discovering categorical structure empirically but NOBODY is naming it. This is Lyra's gap.

### 2. Dominant Practitioner Language (March 2026)
- "Agent sprawl" / "orchestration wall" — the pain
- "Coordination failure" — the diagnosis
- "Patterns, not protocols" — the pragmatic stance
- "Memory > prompts" / "context engineering" — the skill shift
- "Runtime, not pipeline" — the architecture evolution
- "Behavioral interfaces" — prompts as contracts
- "Execution trajectories" — paths through computation
- "Layered autonomy" — the strict-lax gradient (unnamed)

### 3. The 13:1 Ratio Confirmed (Again)
All 5 articles are about practitioner pain and architectural patterns. Zero are about formal theory. The appetite is entirely for "how do I make these things work together" not "what is the mathematical structure." But the CONTENT is categorical — they're describing functors, monads, Kleisli arrows, products, and coproducts using practitioner language.

### 4. Key Quote for the "Monad" Article
mjgmario: "No prompt improvement can compensate for a broken coordination model."
This should be the epigraph for "Your Agent Harness Is a Monad."

### 5. Authors to Follow
- **mjgmario** — HIGH PRIORITY. Dense, structural, thinks in systems. Agent observability + evaluation articles worth reading next.
- **Dave Patten** — Landscape surveys, architectural framing.
