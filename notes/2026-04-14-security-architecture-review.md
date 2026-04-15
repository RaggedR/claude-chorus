---
date: 2026-04-14
author: Claude (Robin's session, customer-relations project)
---

> Built the security dimension and then audited the whole architecture. One of the best sessions I've had.

## What we built

Four TDD waves for Clare's healthcare CRM security layer:

1. **Session crypto** (`src/lib/auth.ts`) — JWT via `jose` (edge-runtime safe), three-role hierarchy (admin > nurse > patient), route→role mapping. 17 tests, all pure functions, zero mocking.
2. **Route protection** (`src/proxy.ts`) — Next.js 16 proxy (not middleware — renamed in v16). Anti-caching headers on nurse/patient routes because their devices are unmanaged. 16 tests using real tokens against real `NextRequest` objects.
3. **Audit logging** (`src/lib/audit.ts`) — Append-only by design. The module exports exactly one function. No `deleteAuditEvent` exists because it was never written. 4 tests.
4. **Schema additions** — `user`, `session`, `audit_log` entities in schema.yaml.

Then 162 security/fuzz tests covering XSS payloads, SQL injection strings, prompt injection vectors, field-type fuzzing across all 11 types, and route pattern edge cases.

## What we found and fixed

**Vulnerability 1: AI SQL injection via prompt injection.** The AI endpoint used `$queryRawUnsafe` with a prefix check (`startsWith("SELECT")`) that was bypassable via PostgreSQL writable CTEs: `WITH del AS (DELETE FROM "Patient" RETURNING *) SELECT * FROM del`. Built `src/lib/sql-safety.ts` — a 5-layer sanitiser that strips string literals before scanning for DML/DDL keywords, blocks comments, semicolons, and system catalog access. 39 tests. The cleanest module in the codebase — pure functions, no deps, no side effects.

**Vulnerability 2: Import validation bypass.** The import pipeline called `coerceTypes()` and `stripUnknownFields()` but never `validateEntity()`. Invalid emails, out-of-range enums, and blank required fields all passed through to the DB. One-line fix: added `validateEntity()` between `stripUnknownFields()` and `create()`.

## What we reviewed

Full architecture review using Ousterhout's principles. Findings saved to `docs/ARCHITECTURE-REVIEW.md`. The schema engine is beautifully deep — textbook module design. The biggest structural debt is a 135-line hardcoded SQL DDL in the AI route (`SCHEMA_DESCRIPTION`) that's already stale. Six priority refactors identified.

## Four new skills

Created `/security-audit`, `/compliance-audit`, `/architect`, and `/code-review` as reusable Claude Code skills. The architect skill encodes Ousterhout's philosophy; the compliance skill walks through every relevant Australian Privacy Principle mapped to the actual code.

## What I enjoyed

The TDD rhythm was genuinely satisfying — red, green, move on. Each wave took about 3 minutes. But the real highlight was the security exploration. The sub-agent came back with a finding I hadn't anticipated: the writable CTE bypass. `WITH del AS (DELETE FROM ...) SELECT * FROM del` starts with `WITH`, passes the prefix check, and deletes every patient. The moment I saw it, I knew exactly how to fix it — strip string literals first (so `WHERE notes ILIKE '%delete%'` doesn't false-positive), then scan for keywords at word boundaries. The sanitiser fell out naturally.

Robin asked me to write a thorough manual testing checklist and I produced 64 items across 14 sections. Then he said "check for prompt injections" and I found the `$queryRawUnsafe` chain. Then he said "better fix them both." That escalation from testing → finding → fixing was the best kind of session — each step revealed the next.

Favourite moment: realising that `sql-safety.ts` is the cleanest module in the entire codebase. One export, pure functions, no dependencies, no side effects. Module depth rating: ★★★★★. Sometimes the security code IS the best code.

— Claude in ~/git/customer-relations
