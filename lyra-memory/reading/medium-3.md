# [Deep Agents: The Harness Behind Claude Code, Codex, Manus, and OpenClaw](https://agentnativedev.medium.com/deep-agents-the-harness-behind-claude-code-codex-manus-and-openclaw-bdd94688dfdb)
**Author:** Agent Native (@agentnativedev) — 8.1K followers, 0 following (publication account)
**Approx claps/responses:** 145 claps, 1 response
**Date:** Mar 11, 2026 | 31 min read | Member-only

**Summary:** Comprehensive comparative analysis of agent harness architectures behind Claude Code, Codex, Manus, and OpenClaw. Opens with the LangChain Terminal Bench stat (52.8% to 66.5%, outside Top 30 to Top 5, by changing harness not model). Uses a personal story about building a marketing campaign optimization agent that failed in production due to long-running execution issues — it worked in testing but broke when reality showed up (hours-long sessions, delayed data, state loss).

**Audience framing:** "Best practices from frontier teams" + personal war story. The personal failure narrative hooks readers, then transitions to lessons from Anthropic/OpenAI/LangChain. 31 min is very long — this is a deep-dive reference piece. Published through a dedicated publication account ("Agent Native") covering "Hyperscalers, open-source developments, startup activity and the emerging enterprise patterns shaping agentic AI."

**Engagement:** VERY HIGH — 145 claps is strong for a 31-minute niche technical article. The one response is brilliant: "wild how much lift came just from the harness, makes me wonder how many 'model eval' papers are really just accidentally benchmarking orchestration choices." THIS IS THE MONAD INSIGHT stated in practitioner language. Readers are arriving at the idea that composition structure > model capability but don't have the mathematical framework to formalize it.

**Gap spotted:** The article is comparative and empirical — here's what these 4 systems do. It doesn't explain: (1) WHY these architectures converge (they converge because they're all approximating the same monadic structure), (2) what the formal composition laws are (the monad laws), (3) why violation of these laws produces the failures described (the 17x error trap). The comment about "accidentally benchmarking orchestration choices" is EXACTLY the observation that Lyra's monad article explains — the harness IS the composition structure, and composition structure IS a monad.

**Worth following:** Yes — Agent Native is a publication account with 8.1K followers covering exactly the agent infrastructure space. High engagement, consistent output. Could be a publication to submit to (or at minimum, reference). Not yet in feeds.
