#!/usr/bin/env python3
"""
Gmail MCP Server for Lyra
=========================
Exposes email_client.py functions as native MCP tools so Claude Code
can call them directly instead of constructing bash commands.

Start: python3 email_mcp_server.py  (runs on stdio transport)
"""

from mcp.server.fastmcp import FastMCP

import email_client

mcp = FastMCP("gmail")


@mcp.tool()
def check_inbox(unread_only: bool = True, limit: int = 10) -> list:
    """Check Gmail inbox for recent messages.

    Args:
        unread_only: If True, only return unread messages. Default True.
        limit: Maximum number of messages to return (most recent first). Default 10.

    Returns a list of message summaries with uid, from, subject, date, unread status,
    and message_id. Use the uid with read_email or download_attachments.
    """
    return email_client.check_inbox(unread_only=unread_only, limit=limit)


@mcp.tool()
def read_email(uid: int) -> dict:
    """Read the full content of an email by its UID.

    Does NOT mark the email as read (uses IMAP PEEK). Call mark_as_read
    separately after processing.

    Args:
        uid: The IMAP UID of the message (from check_inbox results).

    Returns the email with uid, from, subject, body, date, message_id,
    attachment_count, attachments metadata, and total_attachment_size_human.
    """
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
    """Send an email via Gmail SMTP, optionally with file attachments.

    Args:
        to: Recipient email address.
        subject: Email subject line.
        body: Plain text email body.
        cc: Optional CC address(es), comma-separated.
        reply_to: Optional Message-ID to reply to (sets In-Reply-To header).
        attachments: Optional list of absolute file paths to attach (e.g. ["/home/lyra/projects/paper.pdf"]).
                     Each file must exist and be under 25MB.

    Returns status dict with 'sent' or 'error'. If attachments were sent,
    includes an 'attachments' list with filename and size_human for each.
    """
    return email_client.send_email(to, subject, body, reply_to_id=reply_to, cc=cc, attachments=attachments)


@mcp.tool()
def download_attachments(uid: int) -> dict:
    """Download all attachments from an email to /home/lyra/mail/attachments/<uid>/.

    Args:
        uid: The IMAP UID of the message.

    Returns dict with status, attachment_count, total_size_human, saved_to directory,
    and list of files with filename, path, content_type, size, and size_human.
    """
    return email_client.download_attachments(uid)


@mcp.tool()
def mark_as_read(uid: int) -> dict:
    """Mark an email as read (sets the IMAP \\Seen flag).

    Call this after successfully processing/replying to an email.

    Args:
        uid: The IMAP UID of the message.

    Returns status dict with 'ok' or 'error'.
    """
    return email_client.mark_as_read(uid)


if __name__ == "__main__":
    mcp.run()
