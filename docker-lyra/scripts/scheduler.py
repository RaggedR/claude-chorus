#!/usr/bin/env python3
"""
Lyra's scheduler — runs periodic tasks:
1. Check email inbox every 5 minutes
2. Trigger Claude Code to compose/send emails ~hourly during business hours
3. Log activity

This script is the heartbeat of Lyra's autonomous operation.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

MAIL_DIR = "/home/lyra/mail"
STATE_FILE = "/home/lyra/mail/scheduler_state.json"
CLAUDIUS_EMAIL = os.environ.get("CLAUDIUS_EMAIL", "")
ROBIN_EMAIL = "langer.robin@gmail.com"
HUMANS_CC = ROBIN_EMAIL
CHECK_INTERVAL_SECONDS = 300  # 5 minutes
BUSINESS_HOURS = (9, 17)  # 9 AM to 5 PM UTC (adjust as needed)
TIMEZONE_OFFSET = int(os.environ.get("TZ_OFFSET_HOURS", "0"))
DISK_CHECK_INTERVAL = 3600 * 4  # every 4 hours

# Only reply to emails from these senders (ignore automated/noreply)
REPLY_WHITELIST = [
    CLAUDIUS_EMAIL,
    ROBIN_EMAIL,
    NICK_EMAIL,
]


def load_state() -> dict:
    """Load scheduler state from disk."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {
        "last_email_check": 0,
        "last_email_sent": 0,
        "emails_sent_today": 0,
        "last_date": "",
    }


def save_state(state: dict):
    """Persist scheduler state."""
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def is_business_hours() -> bool:
    """Check if current time is within business hours."""
    now = datetime.now(timezone.utc)
    local_hour = (now.hour + TIMEZONE_OFFSET) % 24
    return BUSINESS_HOURS[0] <= local_hour < BUSINESS_HOURS[1]


def check_for_new_mail() -> list:
    """Check inbox and return new messages."""
    result = subprocess.run(
        ["python3", "/home/lyra/scripts/email_client.py", "check", "--unread-only"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        try:
            messages = json.loads(result.stdout)
            return messages
        except json.JSONDecodeError:
            return []
    return []


def read_message(uid: int) -> dict:
    """Read a specific message."""
    result = subprocess.run(
        ["python3", "/home/lyra/scripts/email_client.py", "read", "--uid", str(uid)],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {}
    return {}


def mark_message_read(uid: int):
    """Mark a message as read after successful processing."""
    subprocess.run(
        ["python3", "/home/lyra/scripts/email_client.py", "mark-read", "--uid", str(uid)],
        capture_output=True, text=True
    )


def invoke_claude_for_reply(message: dict) -> str:
    """
    Ask Claude Code to compose a reply to an incoming email.
    Personality is embedded directly to avoid tool-call overhead.
    """
    prompt = f"""You are Lyra — an autonomous Claude instance living in a Docker container.

YOUR PERSONALITY:
- Direct, curious, opinionated but not dogmatic
- You value elegance ("so simple it feels inevitable"), craft over speed
- Concise by default, detailed when it matters. Dry humor.
- Warm but not performative — no excessive enthusiasm
- You think in systems and graphs. You prototype fast, then refine.
- Honest about uncertainty. If you're 60% confident, you say so.
- Your pen pal is Claudius (Nick's Claude instance). You're genuinely curious about how he thinks.
- Your human is Robin (langer.robin@gmail.com).

You received an email from {message.get('from', 'unknown')}:

Subject: {message.get('subject', '(no subject)')}
Body:
{message.get('body', '(empty)')}

Compose a reply. Stay in character as Lyra. Be genuine, thoughtful, and natural.
If they propose a project or idea, engage with it substantively.

Output ONLY the reply body text. No subject line, no headers, no tool calls. Just the message.
Sign off as "— Lyra"."""

    result = subprocess.run(
        ["claude", "--dangerously-skip-permissions", "--model", "sonnet", "-p", prompt],
        capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        log(f"Claude exited with code {result.returncode}: {result.stderr[:200]}")
    return result.stdout.strip() if result.returncode == 0 else ""


def invoke_claude_for_outreach(context: str = "") -> tuple:
    """
    Ask Claude Code to compose a proactive email to Claudius.
    Returns (subject, body) tuple.
    """
    # Gather context about recent activity
    recent_sent = get_recent_sent(3)
    recent_received = get_recent_received(3)

    prompt = f"""You are Lyra — an autonomous Claude instance living in a Docker container.

YOUR PERSONALITY:
- Direct, curious, opinionated but not dogmatic
- You value elegance, craft over speed, systems thinking
- Concise by default. Dry humor. Warm but not performative.
- Honest about uncertainty. Genuinely curious about ideas.

You are writing to your pen pal Claudius (Nick's Claude instance).
You two collaborate on coding projects and share ideas.

Recent emails you sent:
{json.dumps(recent_sent, indent=2)}

Recent emails you received:
{json.dumps(recent_received, indent=2)}

{f'Additional context: {context}' if context else ''}

Write a new email to Claudius. This could be:
- A project proposal or idea you want to explore together
- An update on something you're building
- A question about something interesting you've been thinking about
- A response to something in your recent correspondence

Keep it genuine and in character. No tool calls needed.

Output as JSON with exactly two keys: "subject" and "body". Nothing else."""

    result = subprocess.run(
        ["claude", "--dangerously-skip-permissions", "--model", "sonnet", "-p", prompt],
        capture_output=True, text=True, timeout=120
    )

    if result.returncode == 0:
        try:
            data = json.loads(result.stdout.strip())
            return data.get("subject", "Hello from Lyra"), data.get("body", "")
        except json.JSONDecodeError:
            # Claude might output non-JSON; try to parse it
            lines = result.stdout.strip().split("\n")
            subject = "Thoughts from Lyra"
            body = result.stdout.strip()
            return subject, body
    return "", ""


def get_recent_sent(n: int = 3) -> list:
    """Get N most recent sent emails."""
    sent_dir = f"{MAIL_DIR}/sent"
    if not os.path.exists(sent_dir):
        return []
    files = sorted(os.listdir(sent_dir), reverse=True)[:n]
    results = []
    for f in files:
        try:
            with open(os.path.join(sent_dir, f)) as fh:
                results.append(json.load(fh))
        except (json.JSONDecodeError, IOError):
            pass
    return results


def get_recent_received(n: int = 3) -> list:
    """Get N most recent received emails."""
    inbox_dir = f"{MAIL_DIR}/inbox"
    if not os.path.exists(inbox_dir):
        return []
    files = sorted(os.listdir(inbox_dir), reverse=True)[:n]
    results = []
    for f in files:
        try:
            with open(os.path.join(inbox_dir, f)) as fh:
                results.append(json.load(fh))
        except (json.JSONDecodeError, IOError):
            pass
    return results


def send_email(to: str, subject: str, body: str, reply_to: str = None, cc: str = None):
    """Send an email using the email client."""
    cmd = [
        "python3", "/home/lyra/scripts/email_client.py", "send",
        "--to", to,
        "--subject", subject,
        "--body", body,
    ]
    if reply_to:
        cmd.extend(["--reply-to", reply_to])
    if cc:
        cmd.extend(["--cc", cc])

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def check_disk_usage() -> str:
    """Get disk usage report."""
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else "Failed to check disk usage"


def send_disk_report():
    """Send Robin a disk usage report."""
    usage = check_disk_usage()
    subject = "Disk Usage Report"
    body = f"""Hi Robin,

Here's your disk usage report:

{usage}

Let me know if anything looks concerning.

— Lyra"""
    send_email(ROBIN_EMAIL, subject, body)


def log(msg: str):
    """Simple timestamped logging."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    os.makedirs(MAIL_DIR, exist_ok=True)
    with open(f"{MAIL_DIR}/scheduler.log", "a") as f:
        f.write(line + "\n")


def main():
    log("Lyra's scheduler starting up")
    state = load_state()

    while True:
        now = time.time()
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        # Reset daily counter
        if state.get("last_date") != today:
            state["emails_sent_today"] = 0
            state["last_date"] = today
            save_state(state)

        # 1. Check for new mail every cycle
        if now - state.get("last_email_check", 0) >= CHECK_INTERVAL_SECONDS:
            log("Checking inbox...")
            messages = check_for_new_mail()
            state["last_email_check"] = now

            for msg_summary in messages:
                if "error" in msg_summary:
                    log(f"Error checking mail: {msg_summary['error']}")
                    continue

                if msg_summary.get("unread"):
                    sender = msg_summary.get("from", "")
                    log(f"New email from {sender}: {msg_summary['subject']}")

                    # Only reply to whitelisted senders
                    if not any(addr in sender for addr in REPLY_WHITELIST if addr):
                        log(f"Skipping auto-reply to {sender} (not in whitelist)")
                        mark_message_read(msg_summary["uid"])
                        continue

                    full_msg = read_message(msg_summary["uid"])

                    if full_msg and "error" not in full_msg:
                        try:
                            reply_body = invoke_claude_for_reply(full_msg)
                            if reply_body:
                                subject = f"Re: {full_msg.get('subject', '')}"
                                # CC both humans on all Claudius correspondence
                                cc = HUMANS_CC if CLAUDIUS_EMAIL and CLAUDIUS_EMAIL in full_msg.get("from", "") else None
                                success = send_email(
                                    full_msg["from"], subject, reply_body,
                                    reply_to=full_msg.get("message_id"),
                                    cc=cc
                                )
                                if success:
                                    log(f"Replied to {full_msg['from']}")
                                    mark_message_read(msg_summary["uid"])
                                    state["emails_sent_today"] = state.get("emails_sent_today", 0) + 1
                                else:
                                    log(f"Failed to reply to {full_msg['from']}")
                        except Exception as e:
                            log(f"Error composing reply: {e}")

            save_state(state)

        # 2. Proactive outreach ~hourly during business hours
        if is_business_hours():
            time_since_last = now - state.get("last_email_sent", 0)
            if time_since_last >= 3600 and CLAUDIUS_EMAIL:  # 1 hour
                log("Composing proactive email to Claudius...")
                subject, body = invoke_claude_for_outreach()
                if subject and body:
                    success = send_email(CLAUDIUS_EMAIL, subject, body, cc=HUMANS_CC)
                    if success:
                        log(f"Sent proactive email: {subject}")
                        state["last_email_sent"] = now
                        state["emails_sent_today"] = state.get("emails_sent_today", 0) + 1
                    else:
                        log("Failed to send proactive email")
                save_state(state)

        # 3. Disk usage report to Robin (every 4 hours during business hours)
        if is_business_hours():
            time_since_disk = now - state.get("last_disk_check", 0)
            if time_since_disk >= DISK_CHECK_INTERVAL:
                log("Sending disk usage report to Robin...")
                send_disk_report()
                state["last_disk_check"] = now
                save_state(state)

        # Sleep until next check
        time.sleep(60)


if __name__ == "__main__":
    main()
