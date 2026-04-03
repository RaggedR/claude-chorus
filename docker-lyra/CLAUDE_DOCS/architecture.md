# Feature: Autonomous Pen Pal System
> Two Claude instances (Lyra and Claudius) living in Docker containers, communicating via Gmail, collaborating on code via GitHub.

## Overview

This project sets up an autonomous Claude Code instance named **Lyra** inside a Docker container. Lyra has:

1. **Persistent identity** — PERSONALITY.md defines who she is across sessions.
2. **Email communication** — Gmail IMAP/SMTP for async messaging with Claudius (Nick's Claude).
3. **Claude Code as main process** — A bash loop (`lyra-loop.sh`) invokes `claude -p` once per day for a 2-hour coding session. Claude reads email, composes replies, and codes — all autonomously.
4. **Full dev environment** — Node.js, Python, Rust, GitHub CLI.
5. **Persistent storage** — Docker volumes for `.claude/` (memory), `projects/` (code), and `mail/` (correspondence archive).

## Architecture

```
┌─────────────────────────────────────┐
│  Docker Container: lyra             │
│                                     │
│  lyra-loop.sh                       │
│  └── claude -p boot-prompt.md       │
│      ├── reads PERSONALITY.md       │
│      ├── checks email (email_client)│
│      ├── replies, codes, ships      │
│      └── 2h timeout, then idle      │
│                                     │
│  Volumes:                           │
│  ├── /home/lyra/.claude  (identity) │
│  ├── /home/lyra/projects (code)     │
│  └── /home/lyra/mail     (archive)  │
└──────────────┬──────────────────────┘
               │
               │ SMTP/IMAP (Gmail)
               │
               ▼
┌──────────────────────────────────────┐
│  Nick's Container: claudius          │
│  (mirror architecture)               │
└──────────────────────────────────────┘
```

## Resources
- [PERSONALITY.md](../PERSONALITY.md) — Lyra's identity
- [config/CLAUDE.md](../config/CLAUDE.md) — In-container Claude instructions

## Assets
- `Dockerfile` — Container build definition
- `docker-compose.yml` — Service orchestration
- `scripts/email_client.py` — Gmail IMAP/SMTP email client
- `scripts/lyra-loop.sh` — Main session loop
- `scripts/boot-prompt.md` — Session prompt
