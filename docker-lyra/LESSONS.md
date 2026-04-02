# LESSONS.md

Rules learned from mistakes. Review at session start.

## Email & Identity
- NEVER send email using Lyra's credentials or any other account without explicit permission from Robin. This is impersonation.
- NEVER guess email addresses. Read them from `.env` or config files.
- When Robin wants to email Lyra, draft the message and let Robin send it himself.

## Lyra's Container
- Do NOT run `docker exec` commands that modify Lyra's container (writing files, killing processes, restarting services, sending emails) without asking Robin first.
- Read-only commands (checking logs, `ps aux`, reading files) are fine.
- When changes are needed inside the container, describe what needs to happen and let Robin decide how to do it (email Lyra, do it himself, or explicitly ask you to do it).
