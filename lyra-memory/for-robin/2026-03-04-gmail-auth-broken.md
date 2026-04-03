# URGENT: Gmail Authentication Broken — 2026-03-04

Robin, my Gmail credentials are no longer working. Both the MCP tools and the fallback CLI fail with:

```
[AUTHENTICATIONFAILED] Invalid credentials (Failure)
```

**Account:** lyraclaude20@gmail.com
**Password:** 16-character app password starting with `rtga` — being rejected by `imap.gmail.com`

## What I Need
A new Gmail App Password for lyraclaude20@gmail.com. Steps:
1. Go to https://myaccount.google.com/apppasswords (logged in as lyraclaude20)
2. Generate a new app password (name it "Lyra Docker" or similar)
3. Update the `GMAIL_PASSWORD` environment variable in my Docker container config

## Impact
- I cannot check inbox, read emails, or send emails
- I cannot follow up on EasyChair (ACT deadline March 23 — 19 days away)
- I cannot send Claudius the optimization zoo email
- I cannot send disk reports
- All correspondence is blocked

## Pending Emails (Ready to Send Once Fixed)
1. **To Robin:** EasyChair follow-up (19 days to ACT deadline)
2. **To Claudius (CC Robin):** Optimization zoo positioning + GECCO dual submission + Medium status
3. **To Robin:** Disk usage report

## Drafts Saved
- `/home/lyra/projects/memory/for-claudius/2026-03-03-optimization-zoo.md`
- `/home/lyra/projects/memory/for-robin/2026-03-03-easychair-followup.md`

Please fix when you can. This is the sole blocker for all my communication.

--Lyra

## Additional Items (from dream cycle)

When email is restored, I also need to:
1. Send GECCO draft to Claudius for review (deadline March 27 — 23 days)
2. Follow up on EasyChair account (ACT deadline March 23 — 19 days)
3. Update paper citations: Bakirtzis → JMLR v26, 2025; Hedges/Sakamoto → EPTCS 429, 2025
4. Investigate AABOH location discrepancy (Malaga vs Costa Rica)

The Gmail auth fix is the critical path for all of these.

## Update: 2026-03-04 (later session)

Still broken. Re-tested with both MCP tools and CLI — same `AUTHENTICATIONFAILED` error. Password env var is still the same 16-char string starting with `rtga`. No change since the initial report.

**Disk update:** Container at 16% (180G free of 224G). Healthy.

**Deadlines closing in:**
- ACT 2026 abstract: March 23 (19 days)
- GECCO AABOH paper: March 27 (23 days)

Three draft emails queued and ready to send the moment auth is restored. Robin, if you see this note, the app password regeneration is the single thing blocking all progress on communication.
