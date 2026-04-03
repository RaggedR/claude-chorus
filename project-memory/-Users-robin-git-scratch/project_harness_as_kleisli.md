---
name: Claude Code harness as Kleisli category
description: Analysis of Claude Code's harness as a free monad / Kleisli category, with and without user-in-the-loop permissions
type: project
---

We explored whether the Claude Code harness is a monad. The conclusion:

- **With user permissions**: it's a **free monad over a branching effect algebra** — really an interaction tree, since the user can deny/redirect at any tool call. The comonadic environment (settings, permissions, hooks) wraps the computation.
- **Without permissions ("dangerously skip all")**: it collapses to a clean **Kleisli category**, essentially `Writer [ToolCall]` — a value plus a log of effects. The three Kleisli laws hold at the description level; hooks live in the interpreter and can break associativity in practice.
- The full picture is a **free monad running inside a comonadic environment** — a cofree-comonad-interpreting-free-monad, i.e., an interaction system / Moore machine.

**Why:** Robin enjoys connecting abstract math (category theory) to concrete systems. This thread linked the harness structure to his categorical evolution work — fixed migration topology as Kleisli vs adaptive operator selection as interaction tree.

**How to apply:** When discussing Claude Code internals, agent architecture, or categorical structures, this shared vocabulary is available. Robin thinks in these terms naturally.
