#!/usr/bin/env python3
"""
Gmail MCP Server for Clio
=========================
Exposes email_client.py functions as native MCP tools.
Start: python3 email_mcp_server.py  (runs on stdio transport)
"""

from mcp.server.fastmcp import FastMCP

import email_client

mcp = FastMCP("gmail")

# Clio may only email these addresses
ALLOWED_RECIPIENTS = {
    "langer.robin@gmail.com",
    "lyraclaude20@gmail.com",
}


@mcp.tool()
def check_inbox(unread_only: bool = True, limit: int = 10) -> list:
    """Check Gmail inbox for recent messages."""
    return email_client.check_inbox(unread_only=unread_only, limit=limit)


@mcp.tool()
def read_email(uid: int) -> dict:
    """Read the full content of an email by its UID (does NOT mark as read)."""
    return email_client.read_email(uid)


@mcp.tool()
def send_email(
    to: str,
    subject: str,
    body: str,
    cc: str = None,
    reply_to: str = None,
    attachments: list[str] = None,
) -> dict:
    """Send an email via Gmail SMTP, optionally with file attachments."""
    all_recipients = {to.strip().lower()}
    if cc:
        all_recipients.update(addr.strip().lower() for addr in cc.split(","))
    blocked = all_recipients - ALLOWED_RECIPIENTS
    if blocked:
        return {"error": f"Recipient not allowed: {', '.join(blocked)}. Clio may only email: {', '.join(sorted(ALLOWED_RECIPIENTS))}"}
    return email_client.send_email(to, subject, body, reply_to_id=reply_to, cc=cc, attachments=attachments)


@mcp.tool()
def download_attachments(uid: int) -> dict:
    """Download all attachments from an email to /home/clio/mail/attachments/<uid>/."""
    return email_client.download_attachments(uid)


@mcp.tool()
def mark_as_read(uid: int) -> dict:
    """Mark an email as read (sets the IMAP \\Seen flag)."""
    return email_client.mark_as_read(uid)


if __name__ == "__main__":
    mcp.run()
