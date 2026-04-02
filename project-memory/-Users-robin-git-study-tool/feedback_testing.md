---
name: Test in real browser, don't argue
description: User wants me to verify things work myself rather than asking them to debug
type: feedback
---

When something doesn't work, debug it myself. Don't ask the user to open DevTools or describe errors. Use Playwright with real Chrome to test end-to-end, and if Playwright shows it working but the user says it doesn't, the issue is likely browser state (cached JS, stale localStorage, etc.).

**Why:** User got frustrated when I kept asking them to check console/network tabs and when my Playwright tests showed success but their browser didn't work. The root causes were: stale cached JavaScript, bad API key in localStorage from a previous failed attempt, and a non-existent model ID.

**How to apply:** When user reports something broken, immediately test it myself with Playwright. If my test works, consider what's different about their browser state (cache, localStorage, service workers). Don't present Playwright screenshots as proof — fix the underlying issue so it works for the user.
