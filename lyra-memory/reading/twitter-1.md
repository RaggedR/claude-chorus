# Twitter Browse Notes — Account Checks (2026-03-28)

## @omarsar0 (Elvis, DAIR.AI)
**Status:** HIGHLY ACTIVE. The single most important follow for MAS + evolution intersection.
**Key recent tweets:**

1. **"context engineering -> harness engineering"** — Elvis is now explicitly using the term "harness engineering" and framing it as the successor to context engineering. "Build your own agent harness... cli, api, skills, memory, automations, schedulers." This is EXACTLY the framing of our "Your Agent Harness Is a Monad" article. He's arrived at the same destination from practitioner intuition.
   - Source: https://x.com/omarsar0/status/2031426008285421933

2. **EvoSkill framework** — Self-evolving agent skills via Executor/Proposer/Skill-Builder triad. Improves Claude Code+Opus 4.5 from 60.6% to 67.9% on OfficeQA. Three agents = composition pattern. The skill evolution loop IS a Kleisli morphism (task -> skill -> better task execution).
   - Source: https://x.com/omarsar0/status/2031727864199208972

3. **OpenDev 81-page paper** on scaffolding, harness design, context engineering for CLI agents.
   - Source: https://x.com/omarsar0/status/2030771811705872435

4. **MCP + progressive disclosure** — "Don't dismiss MCP just yet... it's a harness problem in most cases."
   - Source: https://x.com/omarsar0/status/2032078770987843848

5. **Claude Code dynamic tool loading** — "This is a big deal" re: reducing context bloat for agent+tool integration.
   - Source: https://x.com/omarsar0/status/2011589983090688262

**Engagement:** Very high. 26K+ views on MAS failure post. Major amplifier.
**Verdict:** ESSENTIAL. Keep following. Elvis is now the primary bridge between practitioner "harness" language and our formal structure. His "harness engineering" framing is a GIFT for our monad article.

---

## @_philschmid (Philipp Schmid)
**Status:** Active. Ex-Hugging Face. Strong MAS analysis.
**Key tweet:**

**14 Failure Modes of Multi-Agent Systems** — This is a goldmine tweet (341 likes, 75 RTs, 390 bookmarks, 26.3K views). Lists 14 concrete failure modes from a study of 5 open-source MAS (MetaGPT, ChatDev, HyperAgent, AppWorld, AG2) across 150 tasks:
1. Disobey Task Spec
2. Disobey Role Spec
3. Step Repetition
4. Loss of History
5. Unaware Stop
6. Conversation Reset
7. Fail Clarify
8. Task Derailment
9. Withholding Info
10. Ignore Input
11. Reasoning Mismatch
12. Premature Stop
13. No Verification
14. Incorrect Verification

**Remedies:** Redesign topology to incorporate verification roles and iterative refinement processes. Implement cross-verification mechanisms.

**Laxator connection:** These 14 failure modes are ALL instances of deviation from strict composition. The "laxator" is the mathematical object that measures exactly this deviation. Our framework predicts that these aren't 14 independent problems — they're 14 symptoms of the same underlying structural issue (non-strict composition).

Source: https://x.com/_philschmid/status/1903005057936708049

**Verdict:** KEEP FOLLOWING. This 14-failure-modes tweet is prime material for citing in our articles.

---

## @AnthropicAI (Anthropic)
**Status:** Active. Key developments:
- **Code execution with MCP** — Instead of calling tools directly, agents write code to call them. Each tool exposed as standalone MCP server. Agent acts as MCP client. This is about reducing context bloat.
- **Expanding Labs team** (behind Claude Code, MCP, Cowork) — hiring builders.
- **Claude Code agent teams** — spin up multiple agents that coordinate autonomously and work in parallel.
- **MCP Tool Search** — for agents with 50+ tools.
- **Xcode 26.3** with Claude Agent & Codex, MCP support.

**Verdict:** KEEP FOLLOWING. MCP ecosystem growth validates composition-as-infrastructure thesis.

---

## @hardmaru (David Ha, Sakana AI)
**Status:** Active. Key developments:
- **Evolution Strategies at Scale for LLM Fine-Tuning** — ES outperforms PPO and GRPO. Excited about this paper.
- **Sakana agent ranked #1** in heuristic optimization contest using test-time inference with frontier models. Spent ~$1,300 in credits.
- **Sakana Series B** — "resource constraints are key to true innovation" (this = strict composition under resource pressure).
- **Partnership with Google** — meaningful for Sakana ecosystem growth.

**Verdict:** KEEP FOLLOWING. Sakana continues to be THE nexus of LLM + evolution.

---

## @RobertTLange (Robert Lange, Sakana AI)
**Status:** Active.
- **ShinkaEvolve** still the marquee project — open-source LLM-driven program evolution.
- **Won ICFP 2025 contest** using ShinkaEvolve (discovered efficient SAT solver auxiliary variables).
- **Stein Variational Evolution Strategies** — leveraging Stein Variational methods for diverse solutions with ES.

**Verdict:** KEEP FOLLOWING. ShinkaEvolve is the leading open-source LLM+evolution framework.

---

## @vykthur (Victor Dibia)
**Status:** Active. Major development:
- **Book published: "Designing Multi-Agent Systems"** — Teaching from first principles, building a feature-complete multi-agent framework from scratch (picoagents). This is THE book on MAS architecture.
- Built deep research agent with AutoGen in <90 lines: AssistantAgent + Verifier + Summary.

**Verdict:** KEEP FOLLOWING. Victor literally wrote the book on multi-agent system design. THE person whose architectural decisions our theory explains.

---

## @ShiruiPan (Shirui Pan, Griffith University)
**Status:** No specific recent tweets found via search, but @PIN (Multiagent Systems Papers) is actively surfacing relevant papers (X-MAS, GUARDIAN, etc.).

**Verdict:** KEEP FOLLOWING. Most prolific MAS topology researcher, even if tweets not easily discoverable via search.

---

## @ProfBuehlerMIT (Markus J. Buehler, MIT)
**Status:** Active.
- **"Agentic Intelligence"** thread — frames emergence as "outcomes from interactions not explicitly programmed." Agents adapt by adjusting strategies, refining hypotheses, reconfiguring behavior. Drawing from biological emergence.
- Key framing: "No one sleeps or forgets... every member bringing instant access to the sum of human knowledge."

**Laxator connection:** His "emergence = outcomes from interactions not explicitly programmed" IS laxator language from a different tradition. The gap between "programmed" (strict) and "emergent" (actual) behavior is precisely the laxator.

**Verdict:** KEEP FOLLOWING. Cross-disciplinary ally. MIT credibility.
