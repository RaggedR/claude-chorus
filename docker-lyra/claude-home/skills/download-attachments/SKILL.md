---
name: download-attachments
description: Download email attachments to disk. Use when an email has attachments that need to be saved, inspected, or processed.
---

# Download Email Attachments

Download attachments from an email to `/home/lyra/mail/attachments/<UID>/`.

## Steps

### 1. Check for Attachments

Before downloading, verify the email has attachments by looking at the `attachment_count` and `attachments` fields from the `read` command output:

```bash
python3 /home/lyra/scripts/email_client.py read --uid <UID>
```

If `attachment_count` is 0, there's nothing to download.

### 2. Review Sizes

Check `total_attachment_size_human` in the read output. If the total exceeds 50 MB, warn Robin before downloading — his disk is tiny.

### 3. Download

```bash
python3 /home/lyra/scripts/email_client.py download-attachments --uid <UID>
```

This saves all attachments to `/home/lyra/mail/attachments/<UID>/` and returns JSON with the file paths.

### 4. Use the Files

Access downloaded files via the paths returned in the `files` array. Each entry has `filename`, `path`, `content_type`, `size`, and `size_human`.

### 5. Clean Up

When done with the attachments, delete them to save disk space:

```bash
rm -rf /home/lyra/mail/attachments/<UID>
```

## Arguments

If the user provides an argument, treat it as the UID:
- `/download-attachments 42` — download attachments from email UID 42
