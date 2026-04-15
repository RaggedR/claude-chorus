# Production Readiness Skill — customer-relations

**Date:** 2026-04-14
**Project:** customer-relations (healthcare CRM)
**Author:** Claude (Opus session with Robin)

## What happened

Created `/production-ready` — a new skill that audits the CRM across 6 operational dimensions:

1. **Observability** — structured logging, metrics, tracing, health checks
2. **Reliability** — graceful failure, retries, no silent failures
3. **Data Integrity** — transactions, constraints, validation
4. **Performance** — pagination, caching, indexes, streaming
5. **Concurrency** — race conditions, idempotency, optimistic locking
6. **Deployment Safety** — migrations, secrets, containers, CI/CD

## Why it matters

The CRM already has three review skills — security-audit (attacker mindset), compliance-audit (regulator mindset), architect (designer mindset). This adds the fourth perspective: **on-call engineer at 3am**. Together they cover the full pre-deployment surface.

## Key findings from the exploration that informed the skill

- No health check endpoint exists anywhere
- No `$transaction` calls in the entire codebase — multi-step writes are non-atomic
- No pagination on any list endpoint — `findAll()` returns everything with all relations eagerly loaded
- No database indexes beyond PKs and one `@unique` on `Session.token`
- Rate limiting is in-memory only (resets on restart, not shared across instances)
- CalDAV pushes are fire-and-forget with no recovery path for failures
- The destructive migration guard (`migrate.ts` refusing DROP) is genuinely excellent

## Connection to other work

This complements the security hardening branch (`security/compliance-hardening`) that's currently in progress. Security and compliance are necessary but not sufficient — you also need the system to survive operational reality.

## For future instances

Run `/production-ready` before any deployment. The scorecard format (1–5 per dimension) gives a quick go/no-go signal. The implementation order in the report tells you what to fix first.
