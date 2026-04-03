# Feature: Email Attachment Downloading
> Download and save email attachments to disk via the email client CLI.

## Overview

Lyra's `email_client.py` can now detect, report, and download email attachments. When reading an email (`read --uid`), the response includes attachment metadata: count, filenames, sizes, and content types. A separate `download-attachments` command saves all attachments to `/home/lyra/mail/attachments/<UID>/`.

### How it works

1. **Reading an email** now returns attachment metadata:
   ```json
   {
     "uid": 42,
     "body": "See attached report.",
     "attachment_count": 2,
     "attachments": [
       {"filename": "report.pdf", "content_type": "application/pdf", "size": 145234, "size_human": "141.8 KB"},
       {"filename": "data.csv", "content_type": "text/csv", "size": 8921, "size_human": "8.7 KB"}
     ],
     "total_attachment_size_human": "150.5 KB"
   }
   ```

2. **Downloading attachments** saves files and returns paths:
   ```bash
   python3 /home/lyra/scripts/email_client.py download-attachments --uid 42
   ```
   ```json
   {
     "status": "ok",
     "uid": 42,
     "attachment_count": 2,
     "total_size_human": "150.5 KB",
     "saved_to": "/home/lyra/mail/attachments/42",
     "files": [
       {"filename": "report.pdf", "path": "/home/lyra/mail/attachments/42/report.pdf", "size_human": "141.8 KB"},
       {"filename": "data.csv", "path": "/home/lyra/mail/attachments/42/data.csv", "size_human": "8.7 KB"}
     ]
   }
   ```

### Security

- **Filename sanitization**: Path traversal (`../../etc/passwd`), null bytes, and special characters are stripped. Filenames are truncated to 200 chars max.
- **Deduplication**: If two attachments share a name, the second gets `_2` appended (e.g., `data_2.csv`).
- **BODY.PEEK[]**: Downloads use IMAP PEEK to avoid marking emails as read.

### Disk space

Robin's host has limited disk space. The `/download-attachments` skill warns Robin if total attachment size exceeds 50 MB. Always clean up downloaded attachments when done:
```bash
rm -rf /home/lyra/mail/attachments/<UID>
```

## Resources

- [Architecture overview](architecture.md)

## Assets

| File | Role |
|------|------|
| `scripts/email_client.py` | Implementation (helpers + download function) |
| `scripts/test_email_client.py` | Test suite (31 tests) |
| `claude-home/skills/download-attachments/SKILL.md` | Claude Code skill definition |
| `scripts/boot-prompt.md` | Session boot prompt (references the command) |
