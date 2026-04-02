---
name: Cognee OSS Contribution
description: Robin's first open source contribution — to Cognee (knowledge graph RAG engine). Skipped entry PR (issues swarmed), went straight to research proposal. Discussion #2494 posted 2026-03-26.
type: project
---

Robin is making his first open source contribution to Cognee (topoteretes/cognee), a knowledge graph + RAG engine for AI agent memory.

**Why:** Robin has independently built overlapping systems (INSTINCT + math-embed) that exceed Cognee in specific areas: hierarchical progressive drill-down retrieval, KG-guided embedding fine-tuning (77% MRR improvement over OpenAI), and interactive D3.js visualization.

**Status as of 2026-03-26:**
- Phase 1 (entry PR) skipped — all "good first issue" tickets (#2312, #2315, etc.) had 3-4 competing PRs already
- Phase 2 (research proposal) DONE — Discussion #2494 posted proposing KG-guided embedding fine-tuning
- Repo forked to RaggedR/cognee, cloned to ~/git/cognee
- Waiting for maintainer response on Discussion #2494

**How to apply:** Next steps depend on maintainer response. If interested, implement fine-tuning task in cognee/tasks/. Phase 3 (drill-down retriever) can proceed independently. See /Users/robin/git/imagineering/PLAN.md for details.
