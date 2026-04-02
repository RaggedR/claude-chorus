# Plan: Inline Admin Editing on Entity Detail Pages

## Context

Admins currently must navigate to `/admin` to edit entities or manage relationships. The goal is to let admins edit entities and manage relationships **directly on the entity detail page** they're viewing — no round-trip to the admin dashboard.

## Approach

Add a client component (`InlineAdminControls`) that checks the admin cookie and conditionally renders edit/delete buttons and modals on each entity detail page. Reuse the existing `AdminEntityForm` and `AdminRelForm` inside modals.

## Changes

### 1. Widen cookie scope (2 files)

The `admin_auth` cookie is currently scoped to `Path=/admin`, making it invisible on entity pages (`/people/*`, `/orgs/*`, etc.).

- **`app/api/admin/login/route.ts`** — Change `Path=/admin` to `Path=/`
- **`app/admin/layout.tsx`** — Change cookie clear `Path=/admin` to `Path=/`

### 2. Add `preselectedSourceId` to AdminRelForm (1 file)

- **`components/AdminRelForm.tsx`** — Add optional `preselectedSourceId?: string` prop
  - When provided, initialize `sourceId` state with it
  - Hide the source entity search/select, show a static display of the pre-selected entity instead
  - This makes "Add Connection" contextual to the current entity

### 3. Create Modal component (1 new file)

- **`components/Modal.tsx`** — Reusable modal overlay
  - Fixed overlay with backdrop blur, centered content card
  - Escape key and click-outside to close
  - Used by both entity edit and relationship add modals

### 4. Create InlineAdminControls component (1 new file)

- **`components/InlineAdminControls.tsx`** — Central orchestrator for all inline admin UI
  - Props: `entity`, `relationships`, `backHref`, `backLabel`
  - Checks `admin_auth` cookie client-side (same pattern as `app/admin/layout.tsx`)
  - **Always renders**: connections list (same grouping logic as current `RelationshipList`), back link
  - **Admin-only renders**: Edit + Delete buttons above connections, delete (X) per relationship, "Add Connection" button
  - Edit button → Modal with `AdminEntityForm` (pre-filled with entity)
  - Delete button → `confirm()` → `DELETE /api/entities/{id}` → `router.push(backHref)`
  - Relationship delete → `confirm()` → `DELETE /api/relationships/{id}` → `router.refresh()`
  - Add Connection → Modal with `AdminRelForm` (preselectedSourceId = entity.id)
  - After any save: `router.refresh()` to re-fetch server data
  - Imports `REL_TYPE_LABELS` directly from `lib/types.ts` (it's a plain const, no server dependency)

### 5. Update all 6 entity detail pages (6 files)

Replace the sidebar section in each page with `<InlineAdminControls>`:

| Page | backHref | backLabel |
|------|----------|-----------|
| `app/people/[slug]/page.tsx` | `/people` | `People` |
| `app/orgs/[slug]/page.tsx` | `/orgs` | `Organizations` |
| `app/events/[slug]/page.tsx` | `/events` | `Events` |
| `app/venues/[slug]/page.tsx` | `/venues` | `Venues` |
| `app/projects/[slug]/page.tsx` | `/projects` | `Projects` |
| `app/topics/[slug]/page.tsx` | `/topics` | `Topics` |

Each page change is ~5 lines: swap import, replace sidebar JSX, pass props.

### 6. Delete RelationshipList (1 file)

- **`components/RelationshipList.tsx`** — Delete. Its grouping/rendering logic is absorbed into `InlineAdminControls`. No remaining references.

## File summary

| File | Action |
|------|--------|
| `components/Modal.tsx` | CREATE |
| `components/InlineAdminControls.tsx` | CREATE |
| `app/api/admin/login/route.ts` | MODIFY (cookie path) |
| `app/admin/layout.tsx` | MODIFY (cookie clear path) |
| `components/AdminRelForm.tsx` | MODIFY (add preselectedSourceId) |
| `components/RelationshipList.tsx` | DELETE |
| `app/people/[slug]/page.tsx` | MODIFY (sidebar) |
| `app/orgs/[slug]/page.tsx` | MODIFY (sidebar) |
| `app/events/[slug]/page.tsx` | MODIFY (sidebar) |
| `app/venues/[slug]/page.tsx` | MODIFY (sidebar) |
| `app/projects/[slug]/page.tsx` | MODIFY (sidebar) |
| `app/topics/[slug]/page.tsx` | MODIFY (sidebar) |

**2 new, 9 modified, 1 deleted**

## Verification

1. `npx tsc --noEmit` — type-check passes
2. `npm run build` — production build succeeds
3. Manual test: navigate to entity page without admin cookie → no admin controls visible
4. Manual test: log in as admin, navigate to entity page → Edit, Delete, Add Connection buttons visible
5. Manual test: edit entity via modal → page refreshes with updated data
6. Manual test: delete relationship → connection disappears
7. Manual test: add connection → new connection appears
8. Manual test: delete entity → redirects to listing page
