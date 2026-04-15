# Security Audit Complete — customer-relations

**Date:** 2026-04-14
**Project:** ~/git/customer-relations

All four batches of the security audit are done. SECURITY_REVIEW.md is fully implemented.

## What shipped
- **Batch 1**: sortBy validation, case-insensitive route matching, upload size/MIME limits, nosniff header, error message sanitisation, Infinity rejection
- **Batch 2**: Login/logout routes, default-deny routing, session cookies (HttpOnly/Secure/SameSite), audit logging with userId, CSRF via SameSite=Strict
- **Batch 3**: GPG-encrypted backups (AES256), audit logging on backup export
- **Batch 4**: Rate limiting (AI 30/min, login 5/min), prompt injection sanitisation, AES-256-GCM token encryption, import file size limit (10MB), CSP/HSTS/security headers, read-only DB role for AI queries

## Deployment steps still needed
Three one-time actions before production deploy — documented in `docs/SECURITY.md` under "Defence-in-Depth (Batch 4)":
1. Run `scripts/create-readonly-role.sql` against production DB + set `DATABASE_URL_READONLY`
2. Set `TOKEN_ENCRYPTION_KEY` env var (64 hex chars)
3. Verify CSP doesn't break Next.js hydration (check browser console)

All three have graceful fallbacks if not set, but the full security posture requires them.

## Test coverage
335 unit tests across 18 files, all passing. New test files for rate limiting, name sanitisation, token crypto, parsers, and CSP config.
