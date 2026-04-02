---
name: Shipping style for small changes
description: When to use /karim vs direct push for the imagineering dashboard
type: feedback
---

For tiny changes (1-2 line fixes), just push directly to main instead of the full /karim workflow.

**Why:** Robin said "just push to main, this is a tiny change" after several rounds of full PR review cycles. The /karim workflow is valuable for substantive changes but overkill for trivial fixes.

**How to apply:** Use judgement. If the change is a simple value tweak, label rename, or 1-line fix, offer to push directly. For anything involving logic changes, new features, or security fixes, use /karim.
