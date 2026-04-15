---
name: Newspaper overhaul April 2026
description: Major refactor of The Morning Dispatch — pure tech focus, keyword scoring from INTERESTS.md, human kindness swarm, editorial curation
type: project
---

Major overhaul completed 2026-04-03:

- **Dropped sections**: Iran, Africa removed from SOURCES.md and build.py
- **Kept**: Technology, Startups, Human Kindness, Science, Spiritual, Horoscope, Art images
- **Keywords**: 116 keywords in INTERESTS.md parsed by fetch.py (was 13 hardcoded)
- **Content fetching**: fetch.py now fetches intro+conclusion from article URLs for deeper keyword matching
- **Human Kindness Swarm**: 3 parallel agents search the web every edition for genuine kindness stories. RSS alone produces garbage Reddit titles.
- **Editorial curation**: /newspaper skill now has Claude review all articles and curate rather than accepting algorithmic picks
- **NPR My Unsung Hero** added as permanent kindness source

**Why:** The algorithmic front page was selecting irrelevant articles. Human kindness in particular needs editorial judgment, not keyword matching.

**How to apply:** When running /newspaper, always follow the full 6-step pipeline including the kindness swarm.
