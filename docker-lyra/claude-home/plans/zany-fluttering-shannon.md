# Plan: Database-Driven Relationship Types

## Context

Relationship types (e.g., `works_at`, `founded`, `tagged_with`) are currently hardcoded as a TypeScript union (`RelType`) and a labels map (`REL_TYPE_LABELS`) in `lib/types.ts`. Adding a new type requires code changes + deploy. The goal is to store them in a `rel_types` DB table so admins can create new types from the UI.

## Changes (8 files, 1 new)

### 1. `db/init.sql` — Add `rel_types` table + FK constraint

Add before the `relationships` table:

```sql
CREATE TABLE rel_types (
  key TEXT PRIMARY KEY,
  forward_label TEXT NOT NULL,
  reverse_label TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

Add FK on `relationships.rel_type → rel_types.key` to enforce only registered types are used.

### 2. `db/seed.sql` — Seed 12 existing types

Insert all 12 types **before** the existing `DO $$ ... END $$` block (the block creates relationships that reference these types via FK).

### 3. `lib/types.ts` — Type changes

- Add `RelTypeRow` interface (key, forward_label, reverse_label, created_at)
- Change `RelType` from hardcoded union → `string`
- **Delete** `REL_TYPE_LABELS` constant entirely

### 4. `lib/queries.ts` — Add rel_types queries

- `listRelTypes()` → `SELECT * FROM rel_types ORDER BY key`
- `getRelTypesMap()` → returns `Record<string, { forward, reverse }>` (same shape as old `REL_TYPE_LABELS` for easy migration)
- `createRelType(key, forward_label, reverse_label)` → INSERT RETURNING *

### 5. `app/api/rel-types/route.ts` — New API route (GET + POST)

- GET: list all rel types
- POST: create new type (validates required fields, normalizes key to lowercase/underscores, catches duplicates)

### 6. `components/RelationshipList.tsx` — Make async, query DB

- Remove `REL_TYPE_LABELS` import
- Make function `async`, call `getRelTypesMap()` directly (this is a server component, only used in server pages)
- Use fetched labels instead of the constant, with fallback to raw `rel_type`

### 7. `components/AdminRelForm.tsx` — Fetch from API, add inline creation

- Remove hardcoded `REL_TYPES` array
- Fetch types from `/api/rel-types` in `useEffect` alongside entities
- Add collapsible "New type" form below the dropdown (key + forward label + reverse label)
- On create: POST to `/api/rel-types`, refresh list, auto-select new type

### 8. `app/admin/page.tsx` — Fetch from API

- Remove `REL_TYPE_LABELS` import
- Fetch from `/api/rel-types` in existing `useEffect`, build labels map in state
- Replace `REL_TYPE_LABELS[...]` at line 311 with the dynamic map

## Verification

1. `npm run db:reset` — tables created, seed data loads (FK satisfied)
2. `npm run dev` — entity detail pages render with correct relationship labels
3. Admin → Relationships tab → labels display correctly from DB
4. Admin → Add Relationship → dropdown populated from DB
5. Admin → Add Relationship → "New type" form → creates type, appears in dropdown
6. `npx tsc --noEmit` — clean typecheck
