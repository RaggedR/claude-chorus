---
name: drag-drop-debugging-lessons
description: Hard-won lessons from failing to fix kanban drag-and-drop — context pollution, root cause analysis, and verification
type: feedback
---

After 6+ failed attempts at kanban drag-and-drop across sessions, the fix came from a fresh context with a clear plan.

**Why:** Context pollution from repeated failures caused the model to cycle through variations of the same broken approach (wrapping DragTarget differently) rather than questioning the fundamental assumption (that DragTarget works inside scroll containers on Flutter Web). The plan identified the actual root cause (hitTest top-down traversal breaks with scroll transforms) and designed a bypass (globalToLocal bottom-up traversal).

**How to apply:**
- If a bug has failed 2+ fixes in the same conversation, STOP. Write a plan analyzing WHY each attempt failed before trying again. If the pattern is "same mechanism, different wrapper" — the mechanism is the problem.
- Fresh context + clear technical diagnosis beats iterating in a polluted context. Consider suggesting `/clear` and re-entering via plan.
- Never claim a UI fix works without the user verifying it. Say "this should work because X, but I can't test Flutter Web rendering."
- Use the Dart MCP server (`analyze_files`, `get_widget_tree`, `get_runtime_errors`) for introspection when available.
- Playwright cannot interact with Flutter Web canvas rendering — don't waste time on automated UI tests with it.
