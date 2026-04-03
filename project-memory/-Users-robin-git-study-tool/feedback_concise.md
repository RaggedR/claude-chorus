---
name: Be direct, don't waste time
description: User wants efficiency - stop over-explaining, stop running redundant tests
type: feedback
---

Don't run the same test multiple times with slight variations. Don't over-explain insights when the user is waiting for a fix. When told to do something, do it — don't reinterpret or add unnecessary steps.

Don't over-engineer simple requests. If the user says "scroll to the bottom", use `window.scrollTo` — don't build a ref-and-callback architecture. First attempt should be the simplest possible implementation.

**Why:** User had to repeat themselves 3 times for an auto-scroll feature because the first attempt over-engineered it with refs, callbacks, and wrapper divs instead of a single `window.scrollTo` line. User got frustrated by repeated Playwright tests that didn't address the actual problem, and by being asked to do debugging work themselves.

**How to apply:** Fix first, explain later. One line of code beats an architecture. One test, not five. If it fails, change approach rather than tweaking parameters.
