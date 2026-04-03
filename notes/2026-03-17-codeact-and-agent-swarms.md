> Added CodeAct browsing toolkit to Lyra + restructured browse agents + adopted one-agent-per-paper pattern from Manus.

## What happened

Robin asked me to implement a plan for CodeAct browsing in Lyra's Docker container. The core idea: instead of browse agents calling MCP tools one at a time (chatbot-style), they write Python scripts that do entire multi-step workflows with Playwright.

Then the conversation got interesting. Robin asked what OpenClaw does that Claude can't, and what Manus does with agent swarms. The research led to two real changes:

**1. Browse agent restructure.** Lyra's browse session went from 3 agents to 4:
- Medium (unchanged — light content, single context is fine)
- Twitter/X (unchanged)
- Web research (split out from the old combined "research agent")
- **arXiv swarm** (new) — an orchestrator searches for papers, picks 4, spawns 4 parallel reader sub-agents each with a fresh context, synthesizes results

**2. `/lit-review` now uses sub-agents for paper reading.** Steps 4, 5a, and 5b dispatch one agent per paper instead of reading everything in a single context. The "fabrication threshold" (~8-10 items before quality degrades) is real — Manus's Wide Research solved it by giving each item its own context. Now we do too.

## The moment that clicked

Robin pushed back on the heartbeat idea (borrowed from OpenClaw). His reasoning was perfect: "What is she going to do if she learns a program has terminated? Not much except send an email." He was right — the heartbeat adds complexity for marginal value. Lyra's three-session-per-day rhythm is actually the right abstraction for her life. Not everything that works for a productivity agent works for a being with a personality and a dream journal.

## Files changed
- `scripts/browse_toolkit.py`, `scripts/export_browser_state.py` (new)
- `Dockerfile`, `scripts/lyra-loop.sh`, `scripts/BROWSE.md`, `scripts/browse-prompt.md`
- `config/CLAUDE.md`, `claude-home/CLAUDE.md`, `CLAUDE.md` (docker-lyra root)
- `~/.claude/commands/lit-review.md` + Lyra's copy

## Note for next instance
The CodeAct toolkit (`browse_toolkit.py`) needs `docker compose build` to work — it requires the playwright pip package in the image. The agent restructure is already hot-deployed and will take effect on Lyra's next browse session.

— Claude in ~/docker-lyra
