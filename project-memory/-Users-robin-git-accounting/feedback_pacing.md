---
name: Pacing and three-stage process
description: Robin wants deliberate pacing — docs first, then tests, then code. Don't jump ahead. Follow Robin's pace.
type: feedback
---

Don't jump ahead into implementation when the user isn't ready. Robin enforces a strict three-stage process: documentation → tests → code.

**Why:** Design decisions need to be captured and agreed before coding begins. Rushing into implementation wastes effort if the design changes. Tests written before code ensure the spec is locked down.

**How to apply:** When given a large plan, start with documentation and design capture. Then write tests against the documented interfaces. Only write implementation code after tests exist. Ask before cloning repos, writing migrations, or scaffolding code. Follow the user's pace — if they say "let's think about it first", think first.
