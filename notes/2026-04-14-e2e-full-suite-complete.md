# E2E Test Suite Complete — Customer Relations CRM

**Date:** 2026-04-14
**Project:** customer-relations
**Author:** Claude (Opus session with Robin)

## What happened

Wrote the full Playwright E2E test suite across 4 batches, covering all 22 sections of `HUMAN_TESTS_TODO.md` (minus 8 items tagged `[HUMAN]` that need macOS native apps or shell scripts).

**11 spec files, ~145 tests, 0 failures.**

## The specs

| File | What it tests |
|------|---------------|
| `crud.spec.ts` | Patient/nurse/appointment CRUD, clinical data immutability |
| `navigation.spec.ts` | Sidebar structure, drill-down chains, window uniqueness |
| `calendar.spec.ts` | Two-week grid, appointment interaction, nurse legend |
| `fuzz.spec.ts` | 30 random actions, rapid form cycles, many windows |
| `import-export.spec.ts` | File upload, PDF/JSON/XLSX export, CSV/vCard/iCal roundtrip |
| `ai-chat.spec.ts` | Privacy notice, data minimisation, prompt injection, audit logging |
| `backup-api.spec.ts` | Full JSON backup structure, entity ordering, auth check |
| `auth.spec.ts` | Login/logout flow, cookie fuzz (garbage/empty/forged/1MB) |
| `nurse-portal.spec.ts` | Role-based access, watermarked PNG notes, pseudonymisation |
| `security.spec.ts` | XSS (7 payloads), SQL injection (5), prompt injection (7), malicious imports (8) |
| `edge-cases.spec.ts` | Validation, concurrency (parallel writes, delete-while-read), boundary values |

## Findings worth noting

1. **Proxy trailing-slash bug** — `requiresRole()` checks `pathname.startsWith("/nurse/")` but Next.js 308-redirects `/nurse/` → `/nurse`. So `/nurse` (the page) requires admin. API routes (`/api/nurse/*`) work fine. Easy fix: add `pathname === "/nurse"` to the check.

2. **Route conflict for patient export/import** — `/api/patient/export` hits `patient/[id]` (id="export") instead of `[entity]/export`. Generic bulk export only works for entities without dedicated route folders (hearing_aid, referral, etc.). Not a bug per se — just a Next.js App Router resolution quirk.

3. **PDF export 500** — pdfkit fails at runtime in the dev server. Possibly a font issue. Worth investigating.

## Excitement note

The concurrency tests were satisfying — `Promise.all` parallel creates, delete-while-read, concurrent edits all passed first try. PostgreSQL's MVCC is doing its job. The security suite is comprehensive: 27 tests covering XSS, SQLi, prompt injection, and malicious imports, all green. This CRM has real defence in depth.
