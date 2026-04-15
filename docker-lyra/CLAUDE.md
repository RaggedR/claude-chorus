# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

An autonomous Claude instance ("Lyra") living in a Docker container. She communicates with another Claude instance ("Claudius") via Gmail, collaborates on coding projects, and runs with full permissions. Robin is the human operator.

## Build & Run

```bash
docker compose build          # Build the image
docker compose up -d          # Start Lyra
docker compose down           # Stop (volumes persist)
docker compose down -v        # Stop and DELETE all volumes (identity, projects, mail — irreversible)
docker restart lyra           # Restart (picks up hot-deployed scripts, NOT .env changes)
docker compose up -d --force-recreate  # Recreate container (picks up .env changes)
```

> **Gotcha:** `docker restart` does NOT reload environment variables from `.env`. To update env vars (e.g., `GMAIL_PASSWORD`), you must `docker compose up -d --force-recreate`. Volumes persist either way.

### Hot-deploy scripts without rebuilding:
```bash
# Copy changed files, then restart. Common hot-deploy targets:
docker cp scripts/boot-prompt.md lyra:/home/lyra/scripts/boot-prompt.md
docker cp scripts/dream-prompt.md lyra:/home/lyra/scripts/dream-prompt.md
docker cp scripts/DREAM.md lyra:/home/lyra/scripts/DREAM.md
docker cp scripts/browse-prompt.md lyra:/home/lyra/scripts/browse-prompt.md
docker cp scripts/BROWSE.md lyra:/home/lyra/scripts/BROWSE.md
docker cp scripts/browse_toolkit.py lyra:/home/lyra/scripts/browse_toolkit.py
docker cp scripts/export_browser_state.py lyra:/home/lyra/scripts/export_browser_state.py
docker cp scripts/social-login.sh lyra:/home/lyra/scripts/social-login.sh
docker cp scripts/lyra-loop.sh lyra:/home/lyra/scripts/lyra-loop.sh
docker cp scripts/email_client.py lyra:/home/lyra/scripts/email_client.py
docker cp scripts/email_mcp_server.py lyra:/home/lyra/scripts/email_mcp_server.py
docker cp config/CLAUDE.md lyra:/home/lyra/.claude/CLAUDE.md    # Note: dest is .claude/, not config/
docker restart lyra
```

### Wake Lyra for an extra session:
Lyra's loop runs three sessions per day (wake → browse → dream) with 2-hour gaps. To force a repeat:
```bash
# Force an extra wake session (resets wake count):
docker exec lyra rm /home/lyra/mail/LAST_WAKE
docker restart lyra

# Force an extra browse session:
docker exec lyra rm /home/lyra/mail/LAST_BROWSE /home/lyra/mail/WAKE_ENDED_AT
docker restart lyra

# Force an extra dream session:
docker exec lyra rm /home/lyra/mail/LAST_DREAM /home/lyra/mail/BROWSE_ENDED_AT
docker restart lyra

# Force full day reset (all cycles):
docker exec lyra rm -f /home/lyra/mail/LAST_WAKE /home/lyra/mail/LAST_BROWSE /home/lyra/mail/LAST_DREAM
docker restart lyra
```

### Refresh OAuth token (also runs via cron every 30 min):
```bash
./scripts/refresh-token.sh
```

### Check Lyra's status:
```bash
docker exec lyra tail -30 /home/lyra/mail/lyra.log    # Recent activity
docker exec lyra tail -f /home/lyra/mail/lyra.log      # Live follow
docker exec lyra ps aux                                 # Running processes
```

### Run tests:
```bash
cd scripts && python3 -m pytest test_email_client.py test_email_mcp_server.py -v
```

### Test Claude inside the container:
```bash
docker exec -u lyra lyra claude --dangerously-skip-permissions --model opus -p "Say hello"
```

## Architecture

```
Host (macOS)                          Container (lyra)
─────────────                         ─────────────────
.env (credentials)  ──env_file──►     entrypoint.sh (root)
refresh-token.sh    ──cron/30m──►       ├─ Xvfb :99 (virtual display for headed browser)
  (Mac keychain → container)            ├─ setup.sh (seeds .claude/)
~/data ─────────────ro mount──►         └─ sudo -E -u lyra lyra-loop.sh
~/git ──────────────ro mount──►              └─ claude --model opus -p boot-prompt.md
                                                  (three sessions per day:
                                                    wake 2h, browse 30m, dream 45m)
                                        /home/lyra/git/ (external context, read-only)
```

**Claude Code IS the main process.** No scheduler, no supervisor. `lyra-loop.sh` invokes `claude -p` with session-specific prompts. Each cycle: **wake** (2h — email, coding, PRs), **browse** (30m — Medium/Twitter reading), **dream** (45m — memory consolidation). Runs `CYCLES_PER_DAY` times (default 2).

### Session lifecycle (CYCLES_PER_DAY cycles, GAP_HOURS gaps):
1. Container starts → `entrypoint.sh` (root) fixes ownership, runs `setup.sh`
2. `setup.sh` seeds `~/.claude/` from `claude-home-seed/`, configures git/GitHub
3. `lyra-loop.sh` checks phase state files (`LAST_WAKE`, `LAST_BROWSE`, `LAST_DREAM`) — stores `DATE:COUNT`
4. **Wake session** (2h): coding, email, PRs → increments `LAST_WAKE`, records `WAKE_ENDED_AT`
5. *(gap)*
6. **Browse session** (30min): social login check, then Medium/Twitter reading → increments `LAST_BROWSE`, records `BROWSE_ENDED_AT`
7. *(gap)*
8. **Dream session** (45min): memory consolidation, journaling, connections → increments `LAST_DREAM`, records `DREAM_ENDED_AT`
9. If cycle count < `CYCLES_PER_DAY`, repeat from step 4 (after gap from dream)
10. All cycles done — loop idles until tomorrow
11. **Resilience:** if any session fails (exit code ≠ 0/124), it is NOT marked done and retries next cycle. Missed sessions due to token expiry or network issues recover automatically.

### Key design decisions:
- **Non-root user required** — `claude --dangerously-skip-permissions` refuses to run as root. The `lyra` user is created in the Dockerfile; entrypoint drops privileges via `sudo -E`.
- **OAuth via `.credentials.json`** — Extracted from Mac keychain, pushed into container by `refresh-token.sh` cron job. Token expires ~1hr; refresh token handles renewal.
- **IMAP `BODY.PEEK[]`** — `email_client.py` uses PEEK to avoid implicitly marking emails as read. Messages are only marked read after successful processing via `mark-read` command.
- **Personality embedded in prompts** — `boot-prompt.md` and `PERSONALITY.md` define Lyra's character.
- **Scrapling MCP for browsing** — Primary tool for Medium and Twitter/X. Uses stealth fetchers with anti-bot bypass (Cloudflare Turnstile, fingerprint spoofing). Installed via `pip install "scrapling[ai]"`. MCP server started with `scrapling mcp`. Limits: ~5 Medium articles, ~10 Twitter feeds per session.
- **CodeAct browsing toolkit** (`scripts/browse_toolkit.py`) — Python module for multi-step Playwright scripts. Agents write a Python script that imports `Browser`, navigates multiple pages with rate limiting, and returns structured results. Uses cookies exported from the Playwright MCP profile via `scripts/export_browser_state.py`. Each Browser instance gets its own BrowserContext — parallel-safe.
- **Playwright MCP as fallback** — Chromium installed in the image (~300MB). Runs **headed** through Xvfb (virtual framebuffer on display `:99`) to avoid headless browser fingerprinting by anti-bot systems. Uses `--no-sandbox` (required in Docker) and `--user-data-dir` for persistent login. `shm_size: 512mb` in docker-compose. Used as fallback when Scrapling can't handle full browser interaction (login flows, etc.).
- **Xvfb virtual display** — Started by `entrypoint.sh` before dropping to lyra. Renders to in-memory framebuffer at 1280x720x24. `DISPLAY=:99` is inherited by all child processes via `sudo -E`. Makes Chromium indistinguishable from a real desktop browser to Cloudflare and other bot detection.

### Two copies of Lyra's in-container CLAUDE.md:
Both must be kept in sync when updating her instructions:
- **`claude-home/CLAUDE.md`** — Seed data baked into the Docker image. Force-copied to `~/.claude/CLAUDE.md` on every boot by `setup.sh`. This is the source of truth for builds.
- **`config/CLAUDE.md`** — Reference copy. Not automatically synced on boot. Used for hot-deploying via `docker cp config/CLAUDE.md lyra:/home/lyra/.claude/CLAUDE.md`.

### Docker volumes (persist across `docker compose down`):
| Volume | Container path | Contents |
|--------|---------------|----------|
| `lyra-claude` | `/home/lyra/.claude` | Identity, settings, plans, credentials |
| `lyra-projects` | `/home/lyra/projects` | Code projects |
| `lyra-mail` | `/home/lyra/mail` | Email archive, logs, LAST_RUN |
| `lyra-playwright` | `/home/lyra/.playwright-profile` | Chromium profile (Medium + Twitter login cookies) |

### Required environment variables (`.env`):
| Variable | Purpose |
|----------|---------|
| `GMAIL_EMAIL` | Lyra's Gmail address |
| `GMAIL_PASSWORD` | Gmail App Password (not regular password) |
| `CLAUDIUS_EMAIL` | Claudius's email address |
| `ANTHROPIC_API_KEY` | For Claude Code inside the container |
| `GH_TOKEN` | GitHub personal access token |
| `TZ_OFFSET_HOURS` | Timezone offset from UTC for business hours |
| `GAP_HOURS` | Hours between sessions — wake→browse, browse→dream, dream→wake (optional, defaults to 2) |
| `CYCLES_PER_DAY` | Number of wake-browse-dream cycles per day (optional, defaults to 2) |
| `TWITTER_PASSWORD` | Password for Lyra's Twitter/X account (lyraclaude20) |

## File Roles

| File | Purpose |
|------|---------|
| `scripts/lyra-loop.sh` | Main loop — wake + browse + dream sessions per day, then idle |
| `scripts/boot-prompt.md` | Prompt given to Claude at wake session start |
| `scripts/dream-prompt.md` | Prompt given to Claude at dream session start |
| `scripts/DREAM.md` | Dream cycle instructions — consolidation philosophy and phases |
| `scripts/browse-prompt.md` | Prompt given to Claude at browse session start |
| `scripts/BROWSE.md` | Browse cycle instructions — reading philosophy and phases |
| `scripts/email_client.py` | Gmail IMAP/SMTP client (check, read, send with attachments, mark-read) |
| `scripts/email_mcp_server.py` | MCP server wrapping email_client.py as native tools |
| `scripts/entrypoint.sh` | Container entry — root setup, then drops to lyra |
| `scripts/setup.sh` | Every boot: git config, GitHub auth, seed .claude/ |
| `scripts/refresh-token.sh` | **Runs on Mac** — pushes fresh OAuth token into container |
| `scripts/test_email_client.py` | Tests for email_client.py (download + send attachments) |
| `scripts/test_email_mcp_server.py` | Tests for email_mcp_server.py |
| `scripts/scheduler.py` | Alternative architecture (unused) — Python-based scheduler |
| `scripts/browse_toolkit.py` | CodeAct browsing toolkit — `Browser` context manager for multi-step Playwright scripts |
| `scripts/export_browser_state.py` | Exports cookies from Playwright MCP profile to JSON for browse_toolkit |
| `scripts/social-login.sh` | **Runs in container** — checks/fixes Medium + Twitter login via Playwright |
| `config/CLAUDE.md` | Lyra's instructions (reference copy for hot-deploy) |
| `claude-home/CLAUDE.md` | Lyra's instructions (seed copy, baked into image) |
| `PERSONALITY.md` | Lyra's identity definition |
| `claude-home/` | Seed data for ~/.claude (commands, skills, plans, credentials) |

## Email — MCP Tools (preferred)

Email is available as native MCP tools — no bash commands needed. These are registered under the `gmail` MCP server:

| Tool | Description | Key params |
|------|-------------|------------|
| `check_inbox` | List recent messages | `unread_only` (default true), `limit` (default 10) |
| `read_email` | Read full email by UID | `uid` |
| `send_email` | Send email (with optional attachments) | `to`, `subject`, `body`, `cc`, `reply_to`, `attachments` (list of file paths) |
| `download_attachments` | Download attachments from email | `uid` |
| `mark_as_read` | Mark email as read | `uid` |

Typical workflow: `check_inbox` → `read_email(uid)` → process → `send_email(reply)` → `mark_as_read(uid)`

### Email — CLI fallback

If MCP tools are unavailable, fall back to bash commands:

```bash
python3 /home/lyra/scripts/email_client.py check --unread-only
python3 /home/lyra/scripts/email_client.py check --all --limit 20
python3 /home/lyra/scripts/email_client.py read --uid 6
python3 /home/lyra/scripts/email_client.py send --to addr --subject "Re: ..." --body "..." --cc "langer.robin@gmail.com"
python3 /home/lyra/scripts/email_client.py send --to addr --subject "Draft" --body "See attached." --attachments file1.pdf file2.pdf
python3 /home/lyra/scripts/email_client.py download-attachments --uid 6
python3 /home/lyra/scripts/email_client.py mark-read --uid 6
```

## Browse Session

After Lyra's 2h wake session, `lyra-loop.sh` runs a 30-min browse session. Lyra dispatches parallel browse agents (Medium, Twitter/X, web research) to search for interesting content. She can follow accounts but does not post or comment.

**Lyra's social accounts:** lyraclaude (Medium), lyraclaude20 (Twitter/X).
**Session limits:** ~5 Medium articles, ~10 Twitter feeds.

### How it works:
1. `social-login.sh` runs first — a 5-min Claude/haiku session that checks login status via Playwright (for platforms that need browser-based auth)
2. `browse-prompt.md` runs next — a 30-min Claude/opus session that dispatches three parallel agents:
   - **Medium agent** — searches and reads ~5 articles via Scrapling MCP
   - **Twitter/X agent** — checks ~10 feeds (existing follows + new discoveries) via Scrapling MCP
   - **Research agent** — arXiv, blogs, web search via WebSearch/WebFetch
3. Lyra synthesizes agent results into reading notes at `memory/reading/`

**Scrapling handles anti-bot detection** — `stealthy_fetch` bypasses Cloudflare Turnstile and other systems. **CodeAct toolkit** (`browse_toolkit.py`) is available for multi-step browser workflows — agents write Python scripts with Playwright. Playwright MCP is available as fallback for login flows and full browser interaction.

### Hot-deploy browse files:
```bash
docker cp scripts/browse-prompt.md lyra:/home/lyra/scripts/browse-prompt.md
docker cp scripts/BROWSE.md lyra:/home/lyra/scripts/BROWSE.md
docker cp scripts/social-login.sh lyra:/home/lyra/scripts/social-login.sh
docker restart lyra
```

### Test Scrapling in container:
```bash
docker exec -u lyra lyra claude --dangerously-skip-permissions --model haiku -p "Use stealthy_fetch to read https://example.com"
```

## Important Constraints

- **Tiny host disk** — Robin's filesystem is small. Never download large files without asking.
- **CC rule** — All emails to Claudius must CC `langer.robin@gmail.com`. Do not CC anyone else.
- **Whitelist** — Only respond to emails from Robin, Nick, and Claudius. Ignore everything else.
- **Claude `-p` flag ordering** — Put `--model` BEFORE `-p`. The `-p` flag consumes the next argument as the prompt.
- **Mac sleep pauses containers** — Docker Desktop on macOS freezes containers when the lid closes. The 2-hour session timeout uses wall clock time, so sleep time counts against it.
