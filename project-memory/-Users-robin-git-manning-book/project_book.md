---
name: Manning Book Project
description: Single combined book on Claude Code — Part I (beginner to full-stack) + Part II (autonomous agents). 12 chapters, progressive disclosure as the spine.
type: project
---

Robin is writing a single book on Claude Code for Manning Publications. Previously two separate books (beginner + advanced), now combined into one.

**Working title**: "Claude Code: From First Prompt to Autonomous Agents"

**Structure**: Two parts, 12 chapters, 6 appendices. Combined outline at `COMBINED-OUTLINE.md`.

**Part I: Building Things** (Ch 1-7) — Terminal → hangman → full-stack (translation app + social network + auth) → context/CLAUDE.md → skills/agents. Takes a complete beginner to deployed full-stack apps. Developer audience skims Part I quickly.

**Part II: Autonomous Agents** (Ch 8-12) — Collaborator mindset → four agents (Lyra, Claudius, Gremlin, Dreamfinder) → dreaming (RAG/knowledge graphs as dream infrastructure) → building your own → what emerges.

**Key design decisions (2026-03-30)**:
- No standalone Python chapter — interrupts the flow from browser games to full-stack
- No standalone GitHub chapter — branches/PRs/CI/CD introduced progressively when the reader's projects need them (Ch 3: branches, Ch 4: CI/CD, Ch 5: PR review)
- RAG and knowledge graphs are NOT standalone topics — they're infrastructure for dreaming (Ch 10)
- Progressive disclosure is the spine: skill as black box (Ch 2) → CLAUDE.md hierarchy (Ch 6) → skill anatomy (Ch 7) → dream cycles (Ch 10)
- Frontend skill created at `~/.claude/skills/frontend/SKILL.md` — installed as black box in Ch 2, anatomy revealed in Ch 7

**The four agents**:
- Lyra (Robin's): prompt-driven dream cycle, email, research
- Claudius (Nick's): journal-based compression, no automated dream — researched neuroscience of dreaming philosophically
- Gremlin (Nick's, github.com/10xdeca/gremlin): 88+ MCP tools, Telegram, TypeScript, self-repair, deterministic schedulers
- Dreamfinder (Nick's, github.com/imagineering-cc/dreamfinder): Dart, Matrix, 5-phase dream cycle with parallel branching, RAG memory, sprint facilitation

**Why:** One book is stronger than two. The beginner who finishes Part I is ready for Part II. The developer skims Part I. Nobody is bored, nobody is left behind.

**How to apply:** Chapter drafts exist for Ch 1-3 in `book2-beginner/`. The advanced book's outline is at `OUTLINE.md`. The combined outline supersedes both.
