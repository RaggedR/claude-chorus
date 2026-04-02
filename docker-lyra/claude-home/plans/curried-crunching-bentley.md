# Declarative Config Refactor: Entity/Relationship Schema + Permissions

## Context

Entity types, relationship types, and permission rules are hardcoded in ~30 locations. Changing a relationship type means editing 5+ files. The user wants **two master config files** — change one file, and the whole system adapts.

Also: prune relationship types (remove 5, add `manages`, update `organized`), and remove the "Create new type" UI entirely.

## Master File #1: `lib/config/schema.ts`

Source of truth for entity types, relationship types, route mapping, and auto-relationship logic.

```typescript
export const ENTITY_TYPES = ['person', 'organization', 'event', 'venue', 'project', 'topic'] as const;
export type EntityType = typeof ENTITY_TYPES[number];

export const ENTITY_TYPE_CONFIG: Record<EntityType, {
  label: string; plural: string; icon: string; color: string; routeSegment: string;
}> = {
  person:       { ..., routeSegment: 'people' },
  organization: { ..., routeSegment: 'orgs' },
  // etc.
};

export const REL_TYPE_DEFINITIONS = [
  { key: 'founded',        forwardLabel: 'Founded',        reverseLabel: 'Founded by',    sourceTypes: ['person'],                          targetTypes: ['organization', 'project'] },
  { key: 'organized',      forwardLabel: 'Organized',      reverseLabel: 'Organized by',  sourceTypes: ['person', 'organization', 'project'], targetTypes: ['event'] },
  { key: 'attended',       ... },
  { key: 'member_of',      ... },
  { key: 'contributes_to', ... },
  { key: 'hosted_at',      ... },
  { key: 'tagged_with',    ... },
  { key: 'spoke_at',       ... },
  { key: 'manages',        forwardLabel: 'Manages',        reverseLabel: 'Managed by',    sourceTypes: ['person'],                          targetTypes: ['venue'] },
];

// When a user creates an entity, auto-create this relationship from their person
export const AUTO_RELATIONSHIP_MAP: Partial<Record<EntityType, string>> = {
  organization: 'founded',
  project:      'founded',
  event:        'organized',
  venue:        'manages',
};
```

Changes from current: removes `works_at`, `based_at`, `invested_in`, `mentors`, `sponsors`. Adds `manages`. Updates `organized` to include `project` in sourceTypes. Adds `routeSegment` to entity config (absorbs `entityPath` mapping).

## Master File #2: `lib/config/permissions.ts`

Source of truth for permission rules that reference the schema.

```typescript
import type { EntityType } from './schema';

// Entity types that only admins can create
export const ADMIN_ONLY_ENTITY_TYPES: EntityType[] = ['person', 'topic'];

// Rel types that grant derived edit permission (source person can edit target entity)
export const EDIT_GRANTING_REL_TYPES: string[] = ['founded', 'organized', 'manages'];

// Rel types that only admins can create (prevents privilege escalation)
// Currently same as EDIT_GRANTING_REL_TYPES — split if needed later
export const ADMIN_ONLY_REL_TYPES: string[] = EDIT_GRANTING_REL_TYPES;
```

## File Changes

### Create (3)

| File | Purpose |
|------|---------|
| `lib/config/schema.ts` | Master schema: entity types, rel types, auto-rel map |
| `lib/config/permissions.ts` | Master permissions: admin-only types, edit-granting rels |
| `db/migrations/005_prune_rel_types_add_manages.sql` | Prune 5 rel types, add `manages`, update `organized` |

### Modify (11)

| File | Change |
|------|--------|
| `lib/types.ts` | Remove `EntityType` union + `ENTITY_TYPE_CONFIG`. Re-export both from `lib/config/schema` (preserves import paths for all consumers) |
| `lib/utils.ts` | `entityPath()`: replace hardcoded `typeToRoute` map with `ENTITY_TYPE_CONFIG[type].routeSegment` |
| `lib/queries.ts` | `hasEditRelationship()`: replace hardcoded `IN ('founded','organized')` with parameterized query from `EDIT_GRANTING_REL_TYPES` |
| `app/api/entities/route.ts` | Replace hardcoded admin-only check + `autoRelType` map with imports from config |
| `app/api/relationships/route.ts` | Replace local `ADMIN_ONLY_REL_TYPES` constant with import from permissions config |
| `components/AdminRelForm.tsx` | Import `ADMIN_ONLY_REL_TYPES` from config. **Remove entire "Create new type" UI** (state, handler, form section) |
| `components/AdminEntityForm.tsx` | Replace local `ENTITY_TYPES` array with import from config |
| `components/GraphView.tsx` | Replace `Object.keys(ENTITY_TYPE_CONFIG) as EntityType[]` with imported `ENTITY_TYPES` |
| `app/page.tsx` | Replace inline ternary URL builder with `ENTITY_TYPE_CONFIG[type].routeSegment` |
| `db/seed.sql` | Update rel_types INSERT: remove 5 pruned types, add `manages`, update `organized`. Remove ~14 seed relationships using pruned types |
| `tests/entity-permissions.spec.ts` | Update auto-relationship test to also verify venue → `manages` |

### No changes needed (confirmed)

- All `app/*/page.tsx` listing pages — import path for `ENTITY_TYPE_CONFIG` unchanged via re-export
- All `app/*/[slug]/page.tsx` detail pages — same
- `components/InlineAdminControls.tsx`, `EntityCard.tsx`, `SearchBar.tsx`, `CreateEntityButton.tsx` — unchanged imports
- `lib/permissions.ts` — already delegates to `hasEditRelationship()`
- `middleware.ts`, `lib/auth.ts`, `lib/db.ts` — no type references
- `db/init.sql` — entity type CHECK constraint unchanged (entity types aren't changing)

## Order of Operations

1. Create `lib/config/schema.ts` and `lib/config/permissions.ts`
2. Update `lib/types.ts` (re-export) → run `npx tsc --noEmit` immediately (riskiest step, 25+ consumers)
3. Update remaining consumers (`lib/utils.ts`, `lib/queries.ts`, API routes, components, `app/page.tsx`)
4. Remove "Create new type" UI from `AdminRelForm.tsx`
5. `npx tsc --noEmit` + `npm run build`
6. Create migration `005_prune_rel_types_add_manages.sql`
7. Update `db/seed.sql`
8. `npm run db:reset` to verify clean DB
9. Update tests
10. `npm run test:e2e` — all pass
11. Update docs (`CLAUDE.md` key files, `CLAUDE_DOCS/entity-permissions.md`)

## Verification

1. `npx tsc --noEmit` — passes
2. `npm run build` — succeeds
3. `npm run db:reset` — clean seed works
4. `npm run test:e2e` — all tests pass
5. Manual: create venue as regular user → verify `manages` relationship auto-created
