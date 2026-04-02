# Phase 1: User Authentication

## Context

The Melbourne Tech Ecosystem currently has a single-password admin gate (`ADMIN_PASSWORD` env var, `admin_auth=true` cookie). We're adding proper user accounts as the foundation for a 4-phase permissions/collaboration system. Phase 1 covers **only** user registration, login, sessions, and migrating admin auth to the new system.

## Design Decisions

- **Separate `users` table** referencing person entities via `person_id` (1:1)
- **Server-side sessions** stored in `sessions` table (not JWT)
- **bcrypt** for password hashing (12 rounds)
- **HttpOnly + SameSite=Lax cookies** (secure in prod)
- **7-day session duration**, cleanup piggybacks on login
- **No "claim existing person" flow** in Phase 1 — registration always creates a new person entity. The schema supports claiming by design (for Phase 2).
- **Fully replace old admin auth** — use a `create-admin` script to seed the first admin user

## Migration: `db/migrations/003_add_users_sessions.sql`

```sql
CREATE TABLE IF NOT EXISTS users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  person_id UUID NOT NULL UNIQUE REFERENCES entities(id) ON DELETE RESTRICT,
  is_admin BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_expires_at ON sessions(expires_at);
```

`ON DELETE RESTRICT` on `person_id` prevents orphaning accounts. `ON DELETE CASCADE` on sessions cleans up when a user is deleted.

## New Files

| File | Purpose |
|------|---------|
| `db/migrations/003_add_users_sessions.sql` | Schema migration |
| `lib/auth.ts` | Password hashing, session CRUD, cookie helpers, `getCurrentUser()` |
| `middleware.ts` | Lightweight route protection (cookie existence check only, no DB) |
| `app/api/auth/register/route.ts` | POST — create person entity + user in transaction |
| `app/api/auth/login/route.ts` | POST — verify password, create session, set cookie |
| `app/api/auth/logout/route.ts` | POST — delete session, clear cookie |
| `app/api/auth/me/route.ts` | GET — return current user + person entity |
| `app/login/page.tsx` | Login form (email + password) |
| `app/register/page.tsx` | Registration form (name + email + password) |
| `components/UserMenu.tsx` | Navbar auth state: avatar dropdown or "Sign In" link |
| `scripts/create-admin.ts` | CLI script to seed admin user (reads `ADMIN_EMAIL`/`ADMIN_PASSWORD` env vars) |
| `playwright.config.ts` | E2E test configuration |
| `tests/auth.spec.ts` | E2E tests for auth flows |
| `CLAUDE_DOCS/authentication.md` | Feature documentation |

## Modified Files

| File | Change |
|------|--------|
| `package.json` | Add `bcrypt`, `@types/bcrypt`, `@playwright/test`; add `test:e2e`, `db:create-admin` scripts |
| `lib/types.ts` | Add `User`, `SafeUser`, `Session` types |
| `lib/db.ts` | Add `withTransaction()` helper |
| `lib/queries.ts` | Add user CRUD queries (`getUserByEmail`, `createUser`, etc.) |
| `lib/utils.ts` | Add `uniqueSlug()` — appends `-2`, `-3` etc. on collision |
| `components/Navbar.tsx` | Add `<UserMenu />` component |
| `components/InlineAdminControls.tsx` | Accept `isAdmin` prop instead of reading cookie |
| `app/admin/layout.tsx` | Rewrite: fetch `/api/auth/me`, check `is_admin`, redirect to `/login` if not |
| `app/people/[slug]/page.tsx` | Call `getCurrentUser()`, pass `isAdmin` to InlineAdminControls |
| `app/orgs/[slug]/page.tsx` | Same pattern |
| `app/events/[slug]/page.tsx` | Same pattern |
| `app/venues/[slug]/page.tsx` | Same pattern |
| `app/projects/[slug]/page.tsx` | Same pattern |
| `app/topics/[slug]/page.tsx` | Same pattern |
| `app/api/entities/route.ts` | Add admin auth check to POST |
| `app/api/entities/[id]/route.ts` | Add admin auth check to PUT, DELETE |
| `app/api/relationships/route.ts` | Add admin auth check to POST |
| `app/api/relationships/[id]/route.ts` | Add admin auth check to DELETE |
| `app/api/upload/route.ts` | Replace `admin_auth` cookie check with session check |
| `app/api/rel-types/route.ts` | Replace `admin_auth` cookie check with session check |

## Key Architecture

### `lib/auth.ts` — Central auth module
- `hashPassword(password)` / `verifyPassword(password, hash)` — bcrypt wrappers
- `createSession(userId)` — INSERT into sessions, returns Session
- `deleteSession(sessionId)` — DELETE from sessions
- `setSessionCookie(sessionId)` / `clearSessionCookie()` — Next.js `cookies()` API (HttpOnly, Secure in prod, SameSite=Lax, 7-day maxAge)
- `getCurrentUser()` — read cookie → lookup session+user → return `SafeUser | null`

### `middleware.ts` — Lightweight, no DB access
- `/admin/*` — redirect to `/login?redirect=/admin` if no `session_id` cookie
- `/login`, `/register` — redirect to `/` if cookie present
- Cookie existence only, **not** validity — actual validation happens in `getCurrentUser()`

### Server-side auth propagation (no client-side cookie reading)
Entity detail pages (server components) call `getCurrentUser()` and pass `isAdmin` as a prop to `InlineAdminControls`. This eliminates client-side waterfalls.

### Registration flow
1. Validate inputs (email format, password >= 8 chars)
2. Check email uniqueness
3. **Transaction**: create person entity with `uniqueSlug(name)` → create user with `person_id`
4. Create session, set cookie
5. Return user

### Admin API route protection pattern
```typescript
const user = await getCurrentUser();
if (!user?.is_admin) {
  return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
}
```

## Implementation Order

1. Install deps: `bcrypt`, `@types/bcrypt`, `@playwright/test`
2. Write migration `003_add_users_sessions.sql`
3. Add types to `lib/types.ts`
4. Add `withTransaction()` to `lib/db.ts`
5. Create `lib/auth.ts`
6. Add user queries to `lib/queries.ts`
7. Add `uniqueSlug()` to `lib/utils.ts`
8. Write Playwright config + E2E tests (TDD — tests first)
9. Build API routes: register, login, logout, me
10. Create `middleware.ts`
11. Build login + register pages
12. Create `UserMenu` component, update `Navbar`
13. Rewrite `app/admin/layout.tsx` to session auth
14. Update `InlineAdminControls` + all 6 entity detail pages
15. Add admin checks to mutating API routes
16. Create `scripts/create-admin.ts`
17. Run migration, seed admin, run tests
18. Write `CLAUDE_DOCS/authentication.md`

## Verification

1. `npm run db:reset && npm run db:migrate` — migration applies cleanly
2. `npm run db:create-admin` — creates admin user
3. `npm run dev` — app starts without errors
4. `npx tsc --noEmit` — no type errors
5. `npm run test:e2e` — all Playwright tests pass
6. Manual smoke test: register → login → see user menu → visit entity page → logout → admin login → see admin controls
7. `npm run build` — production build succeeds

## Confidence: 85%

Main risks: bcrypt native bindings in Next.js build, `cookies()` async API in route handlers (Next.js 16), slug collisions during concurrent registration. All mitigated in the plan.
