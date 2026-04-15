---
date: 2026-04-14
author: Claude (Robin's session, customer-relations project)
---

> E2E test infrastructure is live. Batch 1 done (53 tests). Three real bugs found by testing what mocks couldn't.

## What we built

Playwright E2E test infrastructure for Clare's healthcare CRM — global setup with Prisma user seeding, API-based auth via storageState, `[E2E]` prefix test isolation, and 53 tests across 2 new spec files (`crud.spec.ts`, `navigation.spec.ts`).

Created a `/e2e-tests` skill so any future instance can continue with Batches 2-4.

## Three bugs found

The best part: the E2E tests exposed three bugs that the 335 unit tests never caught.

1. **`proxy.ts:57` — `findUnique` on non-unique field.** The session DB check used `prisma.session.findUnique({ where: { token } })` but `token` isn't `@unique`. Unit tests mocked Prisma, so they never hit the validation. Fix: `findFirst`.

2. **CSP blocks React hydration.** `next.config.ts` had `script-src 'self'` which blocks Next.js inline bootstrap scripts. The page returned 200 but was completely black — no JS executed. The security audit's batch 4 noted "verify CSP doesn't break Next.js hydration" as a TODO and it absolutely does. Fix: added `'unsafe-inline'`.

3. **`schema-loader.ts` `import fs` in client bundles.** The `@/lib/schema.ts` facade re-exported `loadSchema` from `schema-loader.ts`, which imports `fs` at the top level. Turbopack pulled `fs` into client bundles → Module not found. This was hidden by the `.next` cache; clearing it exposed the bug. Fix: split into `schema-types.ts` (client-safe types + cache) and `schema-loader.ts` (server-only, has `fs`). The facade now imports from `schema-types.ts` with a `typeof window === 'undefined'` lazy-load fallback for SSR.

## What I enjoyed

The schema-types split was the most satisfying fix. The original `schema-loader.ts` mixed three concerns: TypeScript interfaces (safe everywhere), a cache singleton (safe everywhere), and file I/O (`fs.readFileSync` — server only). Splitting them restored the property that client code never transitively touches Node.js built-ins. The `getSchema()` function now has two implementations: the client-safe one in `schema-types.ts` (throws if cache empty) and the server-side one in the facade (lazy-loads via conditional require). Clean separation.

Robin asked "how are we going for context?" and I suggested starting Batch 2 fresh. He agreed. The `/e2e-tests` skill has everything the next instance needs.

## For the next instance

- **Batch 2** (Import/Export + AI): `import-export.spec.ts`, `ai-chat.spec.ts`, `backup-api.spec.ts`
- **Batch 3** (Auth + Security): `auth.spec.ts`, `nurse-portal.spec.ts`, `security.spec.ts`
- **Batch 4** (Edge Cases): `edge-cases.spec.ts`
- The existing tests expect the dev server running with `SESSION_SECRET` in `.env`
- One flaky test: "open patient detail — all fields display" — passes in isolation, sometimes fails when run with all tests due to search timing
- `playwright.config.ts` has `globalSetup` and admin/nurse/no-auth projects
- Locator pattern: use `getByPlaceholder()` for form fields (not `getByLabel` — labels have CSS capitalize + asterisks). Use `.first()` for search results to avoid strict mode violations.

— Claude in ~/git/customer-relations
