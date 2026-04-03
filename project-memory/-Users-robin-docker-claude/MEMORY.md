# Docker-Claude Project Memory

## Architecture
- **Don't wrap Claude in a scheduler subprocess.** Let Claude Code be the main process. It has bash tools — it can run scripts directly.
- Main loop: `lyra-loop.sh` — a simple bash while loop that calls `claude -p` every 5 min.
- No supervisor needed. No Python scheduler needed.

## Key Gotchas
- `claude --dangerously-skip-permissions` refuses to run as root. Must create a non-root user.
- Supervisor strips env vars from child processes even with `environment=` directive. Avoid supervisor.
- `sudo -E -u lyra` preserves env when dropping privileges in entrypoint.
- IMAP `RFC822` fetch implicitly marks messages as `\Seen`. Use `BODY.PEEK[]` to avoid this.
- Claude Code `-p` flag: put `--model` BEFORE `-p`, not after. `-p` consumes the next arg as prompt.
- OAuth tokens expire ~1 hour. Cron job on Mac refreshes every 30 min: `scripts/refresh-token.sh`
- Gmail SMTP requires App Password (not regular password) when 2FA is enabled.

## Credentials
- OAuth: `~/.claude/.credentials.json` (access + refresh token from Mac keychain)
- Gmail: App Password in `.env` as `GMAIL_PASSWORD`
- GitHub: PAT via `GH_TOKEN` env var (account: lyra-claude)
- Claudius email: 11o1111o11oo1o1o@gmail.com
- CC all Claudius emails to: langer.robin@gmail.com, nickmeinhold@gmail.com

## File Layout
- `scripts/lyra-loop.sh` — main loop (bash)
- `scripts/boot-prompt.md` — prompt given to Claude each cycle
- `scripts/email_client.py` — IMAP/SMTP client (check, read, send, mark-read)
- `scripts/entrypoint.sh` — root setup then drops to lyra
- `scripts/refresh-token.sh` — cron job on Mac, pushes fresh OAuth token into container
- `config/CLAUDE.md` — Lyra's global instructions
- `PERSONALITY.md` — Lyra's identity
