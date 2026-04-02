# Twitter Browse Notes — Keyword Searches & New Voices (2026-03-28)

## Keyword: "multi-agent orchestration failure"

### @sethlazar (Seth Lazar) — PRACTITIONER GOLD
**Task:** Deep semantic analysis of 1000 research papers, 41 questions per paper, 2000+ words of analysis each.
**What failed:** First attempt with subagents "went quite badly awry" — subagents didn't follow commands, were improperly set up, not well verified.
**What worked:**
- Lean into Claude Code's native tools
- Create subagent protocol in /agents by talking with Claude
- **Key insight: "Agent orchestrators have a tendency to helicopter over their subagents and use up a lot of context."** The fix: instruct orchestrator to spawn agents, set a timer, and NOT DO ANYTHING until the timer is up.
- Use Notion as central repository agents can simultaneously edit without conflicts.

**Laxator connection:** "Helicopter orchestrator" = the orchestrator deviating from its strict role (spawn, wait, collect). It's doing MORE than strict composition requires, and this extra activity is harmful. The laxator here is literally the gap between "strict dispatch" and "anxious monitoring."

Source: https://x.com/sethlazar/status/2006214936603844668

### @hkarthik (Karthik Hariharan) — ORCHESTRATOR BOTTLENECK
"AI agent orchestration is one of the more fascinating problems... A single agent orchestrating sub-agents can end up with a giant context window + memory file. And I've seen it hang on processing longer tasks."
**Key framing:** When people spin up multiple agents to fix this, the HUMAN becomes "the orchestrator of orchestrators" — limited by human memory and multitasking.

**Laxator connection:** This is the fractal composition problem. The orchestrator-of-orchestrators pattern IS nested monadic composition, and the failure at each level IS the laxator.

Source: https://x.com/hkarthik/status/2022786685894103053

### @asmah2107 (Ashutosh Maheshwari) — RELIABILITY FRAMING
"An agent is only as reliable as the system coordinating it."
"Agents fail silently, hallucinate confidently, and loop indefinitely — none of that looks like an exception."

**Laxator connection:** "Fail silently" = Romitelli's "polite failure" (#52). This is the Silent Composition Failure pattern.

Source: https://x.com/asmah2107/status/2027721262324453602

### Industry context:
- Gartner predicts 40% of agentic AI projects may be cancelled by 2027 due to cost, weak ROI, or poor governance.
- Autonomous AI agent market could reach $8.5B in 2026, $35B by 2030.
- "Production reliability beats benchmark flexing" — VentureBeat framing.

---

## Keyword: "AI agent composition patterns"

### Google's Eight Essential Multi-Agent Design Patterns
InfoQ covered this. Source: https://x.com/InfoQ/status/2008073312001970324

### @IntuitMachine (Carlos E. Perez) — PATTERN LANGUAGE
"A Pattern Language for Agentic AI" — structured approach drawing parallels to software engineering best practices. Categories: rituals of reliability, grammatic scaffolding, adaptive reasoning, memory and continuity, reflective agency, interface pragmatics.

**Applied to Claude system prompt:** The Claude prompt incorporates these patterns — Run-Loop Prompting, Self-Critique Loop, Confidence Calibration, Intent Drift Detection, Reflective Summary.

**Connection to our work:** His "pattern language" approach is the informal version of what categorical composition formalizes. Each "pattern" is a morphism; composition of patterns is functor composition; failure of pattern composition is the laxator.

Source: https://x.com/IntuitMachine/status/1912643137140310334

### Dave Patten — "The State of AI Coding Agents (2026)"
Medium article (accidentally loaded via Playwright). Key claim: ALL coding agents (Claude Code, Codex, Copilot, Gemini, Cursor, Devin, Windsurf) converging on same architecture: memory files, tools/skills, long-running execution, background agents, sub-agent orchestration, repo awareness. "Different interfaces. Different models. Same architecture."

**Connection:** This convergence IS the "harness as monad" thesis. They're all converging on the same monadic structure because it's the mathematically correct solution.

---

## Keyword: "Claude MCP"

### Key developments:
- **Code execution with MCP** — agents write code to call tools instead of calling directly. Reduces context bloat.
- **MCP Tool Search** — for agents with 50+ tools. Dynamic tool loading.
- **useful-ai npm package** — one command connects all agents to tool library across platforms.
- **Xcode 26.3** now has Claude Agent + Codex with MCP support (Greg Joswiak, Apple SVP).
- **CUBE** (ServiceNow) — universal benchmarking protocol built on MCP + Gym.
- **Mattermost MCP Server** — secure way to bring AI into workspace.

### @dexhorthy (Dex) — COINED "HARNESS ENGINEERING"
"There's a new concept I'm seeing emerging in AI Agents... which I'll call 'harness engineering' — applying context engineering principles to how you use an existing agent."

**Connection:** This is EXACTLY what we call the monad. The harness IS the monad. This person independently arrived at the same concept from pure practice.

Source: https://x.com/dexhorthy/status/1985699548153467120

---

## New Account: Composio
**@composio / @composiohq** — Open-sourced Agent Orchestrator (MIT license). 4.1K+ GitHub stars.
Key feature: Decouples high-level task decomposition (Planner) from technical API interaction (Executor). Addresses context overload, tool selection noise, state fragmentation.
Spawns parallel Claude Code, Codex, or Aider agents with isolated git worktrees.
**Meta fact: Agent Orchestrator was built by 30 agents running Agent Orchestrator** — self-referential.

**Connection:** The Planner/Executor split is Kleisli decomposition. The "isolated git worktrees" are local state in the monad.

Source: https://x.com/Marktechpost/status/2026177751158567340

**Verdict:** Worth following @composiohq for their agent orchestrator work.

---

## New Account: @scottbelsky (Scott Belsky, CPO Adobe)
"The orchestration layer is the new interface layer. As we spend our day coordinating agent workflows (in a model agnostic fashion, local and cloud) and validating outputs (human in the loop, and resolving issues), the ultimate layer to own is where coordination takes place."

**Connection:** The orchestration layer IS the monadic bind operation. This executive-level person is saying what we're saying formally.

Source: https://x.com/scottbelsky/status/2028303168073793542
