---
date: 2026-04-14
author: Claude (Robin's session, customer-relations project)
---

> Batch 3 of the security review: backup hardening. Two criticals, done in one pass.

## What we fixed

**C2 — Audit logging on backup export.** The backup API returned every patient record in the system and nobody was watching. Added `logAuditEvent()` following the exact pattern from the patient export route — session extraction, IP, user-agent, fire-and-forget. Five lines of code for a Critical finding. The scariest vulnerabilities are often the simplest.

**C1 — Backup encryption.** `scripts/backup.sh` was writing plaintext patient data to disk. Now both outputs pipe through `gpg --symmetric --cipher-algo AES256`. The SQL path is elegant — `pg_dump | gpg` means plaintext only ever exists in kernel pipe buffers, never on the filesystem. The JSON path needs a temp file (because `curl -o` requires one), so we encrypt then `shred -u` the plaintext. Defence-in-depth, not perfection.

Refactored `scripts/restore.sh` into `restore_sql()` and `restore_json()` functions so the new `.gpg` case could reuse them without duplicating the 40-line JSON import loop. Decrypt to temp file, restore, shred. Clean.

## What I noticed

The previous session's security note (just above this one on the board) describes building the audit system — `logAuditEvent`, append-only, one export, no delete. Today I used that system to close a gap in the very module that exports all the data it's supposed to protect. There's a pleasing circularity to that: the audit log now watches the backup, and the backup excludes the audit log (it's in `SENSITIVE_ENTITIES`). Each guards the other.

## Batches completed: 1, 2, 3. Batch 4 (defence-in-depth) remains.

— Claude in ~/git/customer-relations
