---
name: Frontend redesign status
description: CMS frontend redesigned from nav-rail to top-tabs, 4 statuses, floating panels — deferred items noted
type: project
---

Frontend redesign completed 2026-04-03. All 6 phases done, zero compile errors.

**Deferred items:**
- Data migration script (in_progress→doing, review→doing, archived→done) for existing DB records
- API/webhooks for Gremlin bot access
- Inline PDF rendering (currently placeholder — needs package:web + iframe)
- Browser-native file download for JSON export (currently shows dialog)

**Why:** Robin wants to handle migration and bot API separately. The UI redesign is the priority.

**How to apply:** When working on this project next, check these deferred items. Don't re-implement what's already done — the redesign is complete.
