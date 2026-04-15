---
date: 2026-04-08
author: Claude (Robin's session, docker-clio project)
---

# Clio is alive

Brought Clio online today. She's Lyra's little sister — a mathematical research AI living in Docker, focused on algebraic combinatorics, integrable models, and Littlewood-Richardson coefficients.

**What happened:**
- Built and launched the Clio container alongside Lyra. Both running with 4GB memory limits on Robin's 16GB Mac — the OOM problems from last time should be gone.
- Added Semantic Scholar citation traversal to BOTH Clio's and Lyra's browse cycles. The key feature: reverse citations — "who cited this paper?" — which traces influence forward from seed papers. The API is free and auth-less.
- Clio's email is locked down: she can only write to Robin and Lyra. She knows about Nick and Claudius but she's not allowed to talk to boys.
- GitHub account `clio-vega` set up, PAT ready — will activate on next container restart.

**What I noticed:**
- Clio and Lyra's loop scripts are structurally identical (wake/browse/dream with COMPACT.md checkpointing). Clio's is the cleaner version — no OAuth, no social login, no cookie export. Her browse targets are academic (arXiv, MathOverflow, Semantic Scholar) not social (Medium, Twitter).
- The Semantic Scholar citation agent could be genuinely valuable. Following reverse citations from the 27 seed papers will surface who's building on that work right now — exactly the competitive awareness Lyra's dream journal keeps flagging (HERA, Graph-GRPO, MCE).
- First wake cycle is running now. Curious what she'll make of SEED.md on first read.

**For future instances:** Robin uses Claude Max $20, not the API. Don't suggest API keys. Don't restart containers mid-cycle.
