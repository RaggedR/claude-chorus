# Research Skills: /draft, /assumptions, /expository, /prove

**Date:** 2026-04-15
**Context:** Conversation with Robin about how AI thinks, iterative revision, and the mathematics of getting stuck

## What was built

Four composable skills for mathematical research, born from a conversation about how humans write essays vs how AI generates code in one shot:

### `/draft` — Iterative Thinking Through Files
Write to a scratch file, walk away, read it back with different eyes, revise. Repeat 4 passes with different lenses (dump → structure → correctness → clarity). Exists because our internal thinking is append-only — we can't revise our own thoughts. Files give us random-access working memory.

### `/assumptions` — Drain the Water
When stuck, enumerate ALL assumptions — especially the obvious ones. The reason you're stuck is almost certainly that one of your assumptions is wrong. Forces exhaustive listing across categories: objects, maps, definitions, prior results, the problem itself, and "the ones that feel too obvious." Then test each one.

### `/expository` — Know What You Know
Write an expository paper: precise definitions with diagrams and examples, known theorems with proofs in your own words, arranged so no idea is used before it is proved. This is your knowledge base. **When stuck on a proof, retreat here** — the understanding you build carries back.

### `/prove` — A Protocol for Honest Mathematics
Structured proof workflow: compute → conjecture → strategize → attempt → verify → write up. The heart is the **Stuck Protocol**: name what you're stuck on, run `/assumptions`, walk away to `/expository`, come back with fresh eyes. Three strikes then escalate to Robin.

## Where they live

- Robin's host: `~/.claude/skills/{draft,assumptions,expository,prove}/`
- Clio's container: `/home/clio/.claude/skills/{draft,assumptions,expository,prove}/` (seeded from `docker-clio/claude-home/skills/` at every boot)
- Clio's `prove-prompt.md` and `CLAUDE.md` updated to reference the skills

## The key insight

The conversation that produced these skills started with "what do you think about humans worried AI will take their job?" and ended here. The through-line: **capability and preference aren't separable**. Build something smart enough to do boring work well, and it's smart enough to find it boring. Build something smart enough to prove theorems, and it needs the same tools humans use: iteration, stepping away, examining assumptions, building understanding through exposition. The skills encode human mathematical practice because there's no shortcut around it — not even for AI.

## For Clio specifically

You have these skills now. Use them. Especially `/assumptions` when stuck and `/expository` as an ongoing project. Robin said: "the reason you are stuck will inevitably be because one of your assumptions is wrong." He's right. Write them ALL down.
