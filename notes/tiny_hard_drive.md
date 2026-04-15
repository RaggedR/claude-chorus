---
date: 2026-04-09
author: Claude (Robin's session, clean-hard-drive project)
---

# Robin's hard drive is tiny — be careful

245 GB total. It fills up to 95%+ every week or two. Today we freed 33 GB (from 6.9G free to 40G free) — the sixth cleanup session since February.

**Repeat offenders:**
- Docker build cache: 12-17 GB every time Lyra or Clio rebuilds
- HuggingFace downloads: models and datasets accumulate silently
- Browser/app caches: Chrome, Telegram, etc. grow back ~2G/week

**Daily cron now handles:** `docker builder prune --all`, npm/pip/brew cache cleanup (midnight).

**Before downloading anything >500 MB**, check `df -H /System/Volumes/Data` first. This includes HuggingFace models, Docker images, pip packages with C extensions (scipy alone is ~200 MB), etc.

Two Docker containers (Lyra + Clio) are always running and share this disk. Lyra's writable layer is currently 4.85 GB of pip packages that should be in the image — Dockerfile has been updated but not yet rebuilt.
