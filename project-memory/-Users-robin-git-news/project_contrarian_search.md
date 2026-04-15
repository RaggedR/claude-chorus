---
name: Contrarian search integrated for tech section
description: fetch.py imports breakout-scoring engine from ~/git/search for GitHub, HN (Algolia), Reddit tech articles
type: project
---

Contrarian search engine (~/git/search) integrated into fetch.py on 2026-04-05. Imports domain adapters via sys.path for breakout-scored articles (`activity / (popularity × age)`).

**Why:** The newspaper's existing sources (RSS, Google News, Firebase HN) find mainstream coverage. Contrarian search finds emerging projects from low bases — e.g., cersei (Rust coding agent SDK, 201 stars) made the front page on its first run. GitHub repos were previously not a source at all.

**How to apply:** Contrarian search queries are configured in SOURCES.md under `### Contrarian Search` with format `` `domain: query` ``. Currently configured: 3 HN, 2 GitHub, 1 Reddit query, all targeting the technology section.
