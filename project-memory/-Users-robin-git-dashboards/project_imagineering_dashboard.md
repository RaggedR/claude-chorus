---
name: Imagineering Dashboard
description: GitHub activity dashboard for the Melbourne Imagineering meetup group — live on GitHub Pages
type: project
---

Imagineering Dashboard (RaggedR/imagineering-dashboard) is a single-file HTML dashboard showing GitHub activity for the Imagineering team (Robin, Nick, Paul). Live at https://raggedr.github.io/imagineering-dashboard/

**Architecture:** Single `index.html` with inline CSS/JS. No build step. Uses GitHub Events API. Deployed via GitHub Pages from main branch.

**Key design decisions:**
- Timeline feed shows all event types (pushes, PRs, stars, forks, etc.)
- Productivity chart counts push events (not commits) for fair comparison across public/private repos
- Chart shows a rolling 7-day window with weekday + date labels
- 30-minute localStorage cache with stale fallback on 403/429 rate limits
- Unauthenticated API has 60 req/hour limit; token bumps to 5000 (gear icon in header)

**Shipping:** Uses /karim workflow — branch protection, CI (HTML validation), strict code review loop, squash merge. Initialized in `.claude/ship-initialized`.

**Known limitations:**
- GitHub Events API caps at ~300 events; heavy activity days push older events out of the window
- Private repo push events don't include commits array — hence counting pushes not commits
- `r.html_url` used unescaped in href (needs URL validation, not escapeHtml)
