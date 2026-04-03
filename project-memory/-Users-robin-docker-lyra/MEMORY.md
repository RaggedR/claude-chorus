# Docker-Lyra Project Memory

## Key Facts
- Lyra's Medium username: **lyraclaude** (profile: medium.com/@lyraclaude)
- Lyra's Twitter/X username: **lyraclaude20** (profile: x.com/lyraclaude20)
- Two CLAUDE.md copies must stay in sync: `claude-home/CLAUDE.md` (source of truth) and `config/CLAUDE.md` (hot-deploy)
- Nick has asked NOT to be CC'd on emails — only CC Robin

## Current Architecture
- **Wake session**: 2h — email, coding, collaboration
- **Browse session**: 30min, after wake — read-only social media browsing (Medium + Twitter/X), takes reading notes
- **Dream session**: 45min, ~8h after wake — memory consolidation, journaling
- Medium comment system removed (never used — no article published). Replaced by browse session.

## Browse Cycle Details
- `social-login.sh` runs first (5min, haiku) — checks/fixes login on Medium + Twitter
- Then browse session (30min, opus) — ORIENT → BROWSE → NOTE
- Instructions in `scripts/BROWSE.md`, prompt in `scripts/browse-prompt.md`
- Reading notes go to `memory/reading/YYYY-MM-DD.md` + `memory/reading/feeds.md`
- **Authentication is self-service** via `social-login.sh` inside the container
  - Medium: email magic link (reads link from Gmail inbox)
  - Twitter: username + password (`$TWITTER_PASSWORD` env var in host `.env`)
  - Sessions persist in Playwright browser profile — re-login only when cookies expire
- Rate limiting: `sleep 3` between every browser action to avoid bot detection

## Implementation Notes
- Playwright MCP uses `--no-sandbox` (required in Docker) + `--user-data-dir` for persistent login
- `shm_size: 512mb` in docker-compose for Chromium
- Twitter has aggressive bot detection — automated login via Playwright AND Scrapling/Camoufox both fail (API 400 on `/onboarding/task.json`). **Manual cookie injection is the only reliable method**: log in as lyraclaude20 in a real browser, grab `auth_token` + `ct0` from DevTools > Application > Cookies, inject via Playwright `add_cookies()`. Cookies persist in the Playwright profile volume (~weeks-months before expiry).
- Google OAuth login doesn't work from headless browsers (Google blocks it) — that's why Medium uses magic link instead
- LaTeX and Haskell are already installed in the Dockerfile (lines 46-59)
