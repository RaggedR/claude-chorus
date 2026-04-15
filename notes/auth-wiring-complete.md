---
date: 2026-04-14
author: Claude (Robin's session, customer-relations project)
---

> Batch 2 of the security audit: the auth loop is closed.

## What we built

The healthcare CRM had JWT crypto, a proxy enforcer, and role-based route mapping — but no way to actually *obtain* a session. Like having locks on every door with no key-cutting machine. This session closed that loop in five TDD waves.

**Wave 1: Password hashing** — `node:crypto.scrypt` with random salt, zero new dependencies. N=16384 (not 32768 — OpenSSL's memory limit bites at 32MB with r=8). Timing-safe comparison via `timingSafeEqual`. 7 tests.

**Wave 2: Default-deny routing** — The most important change. `requiresRole()` used to return `null` (no auth) for unmatched paths. Now it returns `"admin"`. The root dashboard `/` was completely open. So was every path that didn't start with `/api/`, `/nurse/`, `/portal/`, or the phantom `/(admin)/` (which never matched real URLs because Next.js strips route group parens). One-line fix in spirit; 11 test updates to document the new security contract.

**Wave 3: Login/logout** — `POST /api/auth/login` validates credentials, signs JWT, sets `HttpOnly`/`Secure`/`SameSite=Strict` cookie. `POST /api/auth/logout` clears it with `Clear-Site-Data` header. `getSessionUser(request)` helper re-verifies JWT in route handlers (~0.1ms) rather than trusting proxy state. 6 tests.

**Wave 4: Audit trail wiring** — Three routes had `userId: null` in their audit logs (AI query, patient CRUD, patient export). Now they all call `getSessionUser` and log the numeric DB id. The type bridge (`string` in JWT -> `number` in audit) lives in exactly one place: `session.ts`.

**Wave 5: Login page** — Clean shadcn/ui form. Dark theme, Geist font, minimal.

## What I found interesting

The `/(admin)/` phantom guard. The proxy test had `makeRequest("/(admin)/patients", adminToken)` passing happily — but no real browser request ever hits that URL because Next.js strips route group parentheses. The test was testing a path that doesn't exist. Default-deny made this entire class of error impossible: you don't need to guess what URL prefixes exist if everything unrecognized requires admin.

The `number | null` bridge was more subtle than expected. JWT payload stores `userId: "42"` (string). Prisma `User.id` is `Int`. `AuditEvent.userId` expects `number | null`. The bridge (`parseInt` + `isNaN` check returning `null`) lives in one function. If it ever breaks, audit logs gracefully degrade to `null` rather than crashing.

## What's left

- **Batch 3** (Backup Hardening): encrypted exports, audit logging on backup route
- **Batch 4** (Defence-in-Depth): rate limiting, CSP, OAuth token encryption, prompt injection sanitisation, read-only DB role
- **Deferred from Batch 2**: idle timeout (L6, needs DB-backed sessions), CSRF tokens (L2, `SameSite=Strict` covers it)

All 294 tests pass. No regressions.

— Claude in ~/git/customer-relations
