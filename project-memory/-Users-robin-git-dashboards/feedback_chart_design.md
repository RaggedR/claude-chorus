---
name: Chart design preferences
description: Robin's preferences for how productivity charts should work in dashboards
type: feedback
---

The productivity chart should reflect who has been most "productive" — meaning actual coding work.

**Why:** Robin wants a fair, honest comparison of team output, not inflated by CI ceremony or metadata actions.

**How to apply:**
- Count pushes, not commits (private repos don't expose commits array, creating unfair comparison)
- Exclude non-productive events: starring repos, opening issues, deleting branches, forking
- Don't double-count: squash-merge pushes to main are shipping ceremony, but Robin decided they should still count since "pushing to main should count"
- Show a full week (7 days) so you can see the pattern, not just active days
- Include both the weekday name AND the date in labels
