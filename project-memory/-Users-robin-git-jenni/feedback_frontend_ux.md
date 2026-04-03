---
name: Frontend UX/UI weakness
description: Claude struggles with frontend visual design and browser-based testing — use Playwright or screenshots to verify, don't guess
type: feedback
---

Frontend UX/UI is a weak spot. Don't assume visual changes work — verify them.

**Why:** In the delivery-router session (2026-03-27), multiple rounds of "changes" were pushed that the user couldn't see any difference on. Build caching meant code wasn't actually in the production bundle, Chrome automation couldn't interact with Flutter's canvas rendering, and theme changes were committed without visual verification. The user wasted significant time checking things that hadn't actually changed.

**How to apply:**
- After any visual/UI change, verify it's actually in the build (grep the compiled output for distinctive strings)
- Use `flutter clean` before `flutter build web` — Flutter's incremental build cache is unreliable
- Don't use Claude-in-Chrome for Flutter web apps — CanvasKit renders to canvas, not DOM. Screenshots come back blank, typed text doesn't register, clicks don't land.
- Use Playwright screenshots or ask the user to confirm before claiming something works
- For theme/styling changes, describe exactly what should look different so the user can verify quickly
- Never say "it's done" without evidence the change is actually live
