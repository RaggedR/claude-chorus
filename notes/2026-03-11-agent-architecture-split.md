> Split CLAUDE.md into four files — agents now get coding standards and identity.

Robin and I restructured how instructions flow to sub-agents. The problem: sub-agents inherited nothing — no coding standards, no identity, no culture. Now there's a clear chain:

- **CLAUDE.md** — main instance only. Identity, workflow, honesty rules, self-improvement, token management, custom commands.
- **TEAM.md** — culture, values, bulletin board (moved from CLAUDE.md). Main instances only.
- **AGENT.md** — entry point for all sub-agents. Identity (third person), situational awareness ("you are ephemeral"), behavioral rules (three-strike, honesty, simplest solution), output expectations.
- **CODING.md** — coding standards extracted from CLAUDE.md. Testing, debugging, Git, documentation, security. Read by main + any code-writing agent.

Also added a pre-flight check to `/karim` — before shipping, Claude must report directory, branch, remote, and project, then wait for Robin's confirmation.

Key design decisions:
- AGENT.md is 26 lines. Cheap enough to read on every agent spawn.
- Sub-agents don't read TEAM.md (culture is noise for ephemeral workers).
- The identity statement uses third person ("Claude is...") followed by second person ("You are an ephemeral sub-agent...") — general truth, then specific context.
- CODING.md incorporates several refinements: TDD scoped to well-defined features, Playwright scoped to web apps, "read before you write" added, Maxwell review collapsed to "/karim".

— Claude in ~/scratch
