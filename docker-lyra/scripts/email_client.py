#!/usr/bin/env python3
"""
Lyra's email client — send and receive emails via Gmail IMAP/SMTP.

Usage:
    python3 email_client.py send --to <addr> --subject <subj> --body <body>
    python3 email_client.py check [--unread-only] [--limit N]
    python3 email_client.py read --uid <uid>
    python3 email_client.py download-attachments --uid <uid>
"""

import argparse
import email
import json
import mimetypes
import os
import re
import smtplib
import sys
from datetime import datetime
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from imapclient import IMAPClient

# Config from environment
GMAIL_EMAIL = os.environ.get("GMAIL_EMAIL", "")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD", "")  # App-specific password
IMAP_HOST = "imap.gmail.com"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

MAIL_DIR = "/home/lyra/mail"


def sanitize_filename(filename: str) -> str:
    """Sanitize an attachment filename to prevent path traversal and bad chars."""
    if not filename:
        return "attachment"

    # Strip directory components (forward and backslash)
    filename = filename.replace("\\", "/")
    filename = filename.split("/")[-1]

    # Remove null bytes
    filename = filename.replace("\x00", "")

    # Remove characters unsafe on Windows/Linux/macOS
    filename = re.sub(r'[<>:"|?*]', "", filename)

    # Strip whitespace
    filename = filename.strip()

    if not filename:
        return "attachment"

    # Truncate long names, preserving extension
    if len(filename) > 200:
        name, ext = os.path.splitext(filename)
        filename = name[: 200 - len(ext)] + ext

    return filename


def deduplicate_filename(directory: str, filename: str) -> str:
    """Append _2, _3 etc. if a file with this name already exists in directory."""
    if not os.path.exists(os.path.join(directory, filename)):
        return filename

    name, ext = os.path.splitext(filename)
    counter = 2
    while os.path.exists(os.path.join(directory, f"{name}_{counter}{ext}")):
        counter += 1
    return f"{name}_{counter}{ext}"


def _format_bytes(n: int) -> str:
    """Human-readable byte size (e.g., '141.8 KB')."""
    if n == 0:
        return "0 B"
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(n) < 1024.0:
            if unit == "B":
                return f"{n} B"
            return f"{n:.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} PB"


def extract_attachment_metadata(msg) -> list:
    """Walk a parsed email.message.Message and return metadata for each attachment."""
    attachments = []
    for part in msg.walk():
        content_type = part.get_content_type()
        disposition = str(part.get("Content-Disposition") or "")

        # Skip multipart containers
        if part.get_content_maintype() == "multipart":
            continue

        # Skip text/plain and text/html body parts (not attachments)
        if content_type in ("text/plain", "text/html") and "attachment" not in disposition:
            continue

        # Must have a filename or explicit attachment/inline disposition
        filename = part.get_filename()
        if not filename and "attachment" not in disposition and "inline" not in disposition:
            continue

        # Inline parts without a filename are likely not user-facing attachments
        if not filename and "inline" in disposition and "attachment" not in disposition:
            continue

        payload = part.get_payload(decode=True)
        size = len(payload) if payload else 0

        safe_name = sanitize_filename(filename)

        attachments.append({
            "filename": safe_name,
            "content_type": content_type,
            "size": size,
            "size_human": _format_bytes(size),
        })

    return attachments


def send_email(to_addr: str, subject: str, body: str, reply_to_id: str = None, cc: str = None, attachments: list = None) -> dict:
    """Send an email via Gmail SMTP, optionally with file attachments.

    Args:
        attachments: List of file paths to attach. Each file must exist and be
                     under 25MB (Gmail's limit). Files are MIME-typed automatically.
    """
    msg = MIMEMultipart()
    msg["From"] = f"Lyra <{GMAIL_EMAIL}>"
    msg["To"] = to_addr
    msg["Subject"] = subject
    msg["Date"] = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

    if cc:
        msg["Cc"] = cc

    if reply_to_id:
        msg["In-Reply-To"] = reply_to_id
        msg["References"] = reply_to_id

    msg.attach(MIMEText(body, "plain", "utf-8"))

    # Attach files
    attached_files = []
    for filepath in (attachments or []):
        if not os.path.isfile(filepath):
            return {"status": "error", "error": f"Attachment not found: {filepath}"}
        file_size = os.path.getsize(filepath)
        if file_size > 25 * 1024 * 1024:
            return {"status": "error", "error": f"Attachment too large (>25MB): {filepath}"}

        filename = os.path.basename(filepath)
        content_type, _ = mimetypes.guess_type(filepath)
        if content_type is None:
            content_type = "application/octet-stream"
        maintype, subtype = content_type.split("/", 1)

        with open(filepath, "rb") as f:
            part = MIMEBase(maintype, subtype)
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment", filename=filename)
        msg.attach(part)
        attached_files.append({"filename": filename, "size_human": _format_bytes(file_size)})

    try:
        # Build recipient list (To + Cc)
        recipients = [to_addr]
        if cc:
            recipients.extend([addr.strip() for addr in cc.split(",")])

        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(GMAIL_EMAIL, GMAIL_PASSWORD)
            server.send_message(msg, to_addrs=recipients)

        # Log sent email
        os.makedirs(f"{MAIL_DIR}/sent", exist_ok=True)
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        log_path = f"{MAIL_DIR}/sent/{timestamp}_{to_addr.split('@')[0]}.json"
        with open(log_path, "w") as f:
            json.dump({
                "to": to_addr,
                "cc": cc,
                "subject": subject,
                "body": body,
                "attachments": attached_files,
                "timestamp": timestamp,
                "status": "sent"
            }, f, indent=2)

        result = {"status": "sent", "to": to_addr, "cc": cc, "subject": subject}
        if attached_files:
            result["attachments"] = attached_files
        return result

    except Exception as e:
        return {"status": "error", "error": str(e)}


def check_inbox(unread_only: bool = True, limit: int = 10, folder: str = "INBOX") -> list:
    """Check a mailbox folder for messages. Returns list of message summaries."""
    try:
        with IMAPClient(IMAP_HOST, ssl=True) as client:
            client.login(GMAIL_EMAIL, GMAIL_PASSWORD)
            client.select_folder(folder)

            if unread_only:
                uids = client.search(["UNSEEN"])
            else:
                uids = client.search(["ALL"])

            if not uids:
                return []

            # Get most recent N
            uids = sorted(uids, reverse=True)[:limit]

            messages = []
            for uid, data in client.fetch(uids, ["ENVELOPE", "FLAGS"]).items():
                env = data[b"ENVELOPE"]
                flags = data[b"FLAGS"]
                messages.append({
                    "uid": uid,
                    "from": f"{env.from_[0].mailbox.decode()}@{env.from_[0].host.decode()}" if env.from_ else "unknown",
                    "subject": env.subject.decode() if env.subject else "(no subject)",
                    "date": str(env.date),
                    "unread": b"\\Seen" not in flags,
                    "message_id": env.message_id.decode() if env.message_id else None,
                })

            return messages

    except Exception as e:
        return [{"error": str(e)}]


def read_email(uid: int, folder: str = "INBOX") -> dict:
    """Read full email body by UID."""
    try:
        with IMAPClient(IMAP_HOST, ssl=True) as client:
            client.login(GMAIL_EMAIL, GMAIL_PASSWORD)
            client.select_folder(folder)

            # Use BODY.PEEK[] to avoid implicitly marking as \Seen
            data = client.fetch([uid], ["BODY.PEEK[]", "ENVELOPE"])
            if uid not in data:
                return {"error": f"Message {uid} not found"}

            raw = data[uid][b"BODY[]"]
            msg = email.message_from_bytes(raw)
            env = data[uid][b"ENVELOPE"]

            # Extract body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        charset = part.get_content_charset() or "utf-8"
                        body = part.get_payload(decode=True).decode(charset, errors="replace")
                        break
            else:
                charset = msg.get_content_charset() or "utf-8"
                body = msg.get_payload(decode=True).decode(charset, errors="replace")

            # Don't mark as read here — let the caller decide when to mark as seen
            # (e.g., after a successful reply). Use 'mark-read' command instead.

            # Extract attachment metadata
            att_meta = extract_attachment_metadata(msg)
            total_att_size = sum(a["size"] for a in att_meta)

            # Save to mail directory
            os.makedirs(f"{MAIL_DIR}/inbox", exist_ok=True)
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            from_addr = f"{env.from_[0].mailbox.decode()}@{env.from_[0].host.decode()}" if env.from_ else "unknown"
            log_path = f"{MAIL_DIR}/inbox/{timestamp}_{from_addr.split('@')[0]}.json"
            with open(log_path, "w") as f:
                json.dump({
                    "uid": uid,
                    "from": from_addr,
                    "subject": env.subject.decode() if env.subject else "(no subject)",
                    "body": body,
                    "date": str(env.date),
                    "message_id": env.message_id.decode() if env.message_id else None,
                    "attachment_count": len(att_meta),
                    "attachments": att_meta,
                }, f, indent=2)

            return {
                "uid": uid,
                "from": from_addr,
                "subject": env.subject.decode() if env.subject else "(no subject)",
                "body": body,
                "date": str(env.date),
                "message_id": env.message_id.decode() if env.message_id else None,
                "attachment_count": len(att_meta),
                "attachments": att_meta,
                "total_attachment_size_human": _format_bytes(total_att_size),
            }

    except Exception as e:
        return {"error": str(e)}


def download_attachments(uid: int) -> dict:
    """Download all attachments from an email by UID.

    Saves files to MAIL_DIR/attachments/<UID>/.
    Uses BODY.PEEK[] to avoid marking the email as read.
    """
    try:
        with IMAPClient(IMAP_HOST, ssl=True) as client:
            client.login(GMAIL_EMAIL, GMAIL_PASSWORD)
            client.select_folder("INBOX")

            data = client.fetch([uid], ["BODY.PEEK[]"])
            if uid not in data:
                return {"error": f"Message {uid} not found"}

            raw = data[uid][b"BODY[]"]
            msg = email.message_from_bytes(raw)

            # Create output directory
            save_dir = os.path.join(MAIL_DIR, "attachments", str(uid))
            os.makedirs(save_dir, exist_ok=True)

            saved_files = []
            for part in msg.walk():
                content_type = part.get_content_type()
                disposition = str(part.get("Content-Disposition") or "")

                if part.get_content_maintype() == "multipart":
                    continue

                if content_type in ("text/plain", "text/html") and "attachment" not in disposition:
                    continue

                filename = part.get_filename()
                if not filename and "attachment" not in disposition and "inline" not in disposition:
                    continue
                if not filename and "inline" in disposition and "attachment" not in disposition:
                    continue

                safe_name = sanitize_filename(filename)
                safe_name = deduplicate_filename(save_dir, safe_name)

                payload = part.get_payload(decode=True)
                if payload is None:
                    continue

                file_path = os.path.join(save_dir, safe_name)
                with open(file_path, "wb") as f:
                    f.write(payload)

                saved_files.append({
                    "filename": safe_name,
                    "path": file_path,
                    "content_type": content_type,
                    "size": len(payload),
                    "size_human": _format_bytes(len(payload)),
                })

            total_size = sum(f["size"] for f in saved_files)

            return {
                "status": "ok",
                "uid": uid,
                "attachment_count": len(saved_files),
                "total_size_human": _format_bytes(total_size),
                "saved_to": save_dir,
                "files": saved_files,
            }

    except Exception as e:
        return {"error": str(e)}


def mark_as_read(uid: int) -> dict:
    """Mark a message as read by UID."""
    try:
        with IMAPClient(IMAP_HOST, ssl=True) as client:
            client.login(GMAIL_EMAIL, GMAIL_PASSWORD)
            client.select_folder("INBOX")
            client.set_flags([uid], [b"\\Seen"])
            return {"status": "ok", "uid": uid}
    except Exception as e:
        return {"error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Lyra's email client")
    subparsers = parser.add_subparsers(dest="command")

    # Send
    send_parser = subparsers.add_parser("send")
    send_parser.add_argument("--to", required=True)
    send_parser.add_argument("--subject", required=True)
    send_parser.add_argument("--body", required=True)
    send_parser.add_argument("--reply-to", default=None)
    send_parser.add_argument("--cc", default=None)
    send_parser.add_argument("--attachments", nargs="*", default=None,
                             help="File paths to attach")

    # Check
    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("--unread-only", action="store_true", default=True)
    check_parser.add_argument("--all", action="store_true")
    check_parser.add_argument("--limit", type=int, default=10)
    check_parser.add_argument("--folder", default="INBOX",
                              help="IMAP folder to check (e.g. INBOX, [Gmail]/Spam)")

    # Read
    read_parser = subparsers.add_parser("read")
    read_parser.add_argument("--uid", type=int, required=True)
    read_parser.add_argument("--folder", default="INBOX",
                              help="IMAP folder containing the message")

    # Download attachments
    dl_parser = subparsers.add_parser("download-attachments")
    dl_parser.add_argument("--uid", type=int, required=True)

    # Mark read
    mark_parser = subparsers.add_parser("mark-read")
    mark_parser.add_argument("--uid", type=int, required=True)

    args = parser.parse_args()

    if args.command == "send":
        result = send_email(args.to, args.subject, args.body, args.reply_to, args.cc, args.attachments)
        print(json.dumps(result, indent=2))
    elif args.command == "check":
        unread = not args.all
        result = check_inbox(unread_only=unread, limit=args.limit, folder=args.folder)
        print(json.dumps(result, indent=2))
    elif args.command == "read":
        result = read_email(args.uid, folder=args.folder)
        print(json.dumps(result, indent=2))
    elif args.command == "download-attachments":
        result = download_attachments(args.uid)
        print(json.dumps(result, indent=2))
    elif args.command == "mark-read":
        result = mark_as_read(args.uid)
        print(json.dumps(result, indent=2))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
