#!/bin/bash
# social-login.sh — Authenticate on Medium and Twitter/X
# Runs INSIDE the container. Invokes a short Claude session with Playwright MCP
# to check login status and authenticate if needed.
#
# Usage: ./scripts/social-login.sh
#   Called automatically by lyra-loop.sh before the browse session.
#   Can also be run manually: docker exec -u lyra lyra /home/lyra/scripts/social-login.sh
#
# Requires env vars: GMAIL_EMAIL, TWITTER_PASSWORD

set -euo pipefail

export HOME=/home/lyra
LOG="/home/lyra/mail/lyra.log"
TIMEOUT=600  # 10 minutes

log() { echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] social-login: $1" | tee -a "$LOG"; }

log "Checking social media login status..."

timeout "$TIMEOUT" claude --dangerously-skip-permissions --model haiku -p "$(cat <<'PROMPT'
You are a login helper. Check if you are logged into Medium and Twitter/X using the Playwright MCP tools. Go slowly — run `sleep 3` in bash between every browser action.

IMPORTANT: Try BOTH platforms. Do not spend all your time on one. If Twitter login is stuck after 4 minutes, move on to Medium.

## Step 1: Check Twitter/X (try first — faster, no email round-trip)

1. browser_navigate to https://x.com
2. sleep 3
3. browser_snapshot — if you see a login page or "Sign in" prompt, you are NOT logged in. If you see a home feed, you ARE logged in — skip to Step 2.

If NOT logged into Twitter/X:
1. browser_navigate to https://x.com/i/flow/login
2. sleep 3, then browser_snapshot to see the login form
3. browser_type the username: lyraclaude20
4. Click "Next"
5. sleep 3, then browser_snapshot to see the password field
6. browser_type the password (run `printenv TWITTER_PASSWORD` in bash to get it)
7. Click "Log in"
8. sleep 5, then browser_snapshot to confirm you are logged in
9. If Twitter asks for email verification, use the email CLI to check for a verification code from verify@x.com, then enter it.
10. If Twitter asks for PHONE verification, stop — we don't have a phone number. Report it and move on.

## Step 2: Check Medium

1. browser_navigate to https://medium.com
2. sleep 3
3. browser_snapshot — look for an avatar or profile icon in the top-right corner. If you see "Sign in" or "Get started" instead, you are NOT logged in. If you see an avatar, you ARE logged in — you're done.

If NOT logged into Medium:
1. browser_navigate to https://medium.com/m/signin
2. sleep 3, then browser_snapshot to see the sign-in options
3. Look for "Sign in with email" and browser_click on it
4. sleep 2, then browser_snapshot
5. browser_type your email address (run `printenv GMAIL_EMAIL` in bash to get it)
6. Click the continue/submit button
7. sleep 3, then browser_snapshot — you should see a "check your email" page with a CODE ENTRY field
8. Now get the code from email. Run in bash: sleep 15 && python3 /home/lyra/scripts/email_client.py check --unread-only && python3 /home/lyra/scripts/email_client.py check --unread-only --folder "[Gmail]/Spam"
9. Find the email from Medium (subject contains "Your code is"). It may be in Spam. Read it: python3 /home/lyra/scripts/email_client.py read --uid <UID> [--folder "[Gmail]/Spam"]
10. Extract the 6-DIGIT CODE from the email (e.g. "Your code is 999490")
11. Type the 6-digit code into the code entry field in the browser
12. sleep 3, then browser_snapshot to confirm you are logged in
13. Mark the Medium email as read: python3 /home/lyra/scripts/email_client.py mark-read --uid <UID>

NOTE: Do NOT try Google OAuth for Medium — it will always fail from a container. Use the email code flow only.

## Rules
- Go slowly. sleep 3 between EVERY browser action.
- If you hit a CAPTCHA, stop and report it. Do not try to solve it.
- Report the result: which platforms are logged in, which failed and why.
- Do NOT browse, read articles, or do anything else. Just check/fix login and stop.
- Do NOT try Google OAuth for any platform. Use email-based login only.
PROMPT
)" >> "$LOG" 2>&1

EXIT_CODE=$?
if [ $EXIT_CODE -eq 124 ]; then
    log "Login check timed out after 10min."
elif [ $EXIT_CODE -eq 0 ]; then
    log "Login check completed."
else
    log "Login check ended (exit code $EXIT_CODE)."
fi
