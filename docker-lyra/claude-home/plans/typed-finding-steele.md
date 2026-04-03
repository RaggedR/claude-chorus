# Phase 3: Relationship Requests — Implementation Plan

## Context

Phases 1 (User Accounts) and 2 (Entity Permissions) are complete. Phase 3 adds a **request/approve workflow** for relationships: when a non-admin creates a relationship that requires approval, it becomes a pending request that the target entity's owner(s) must approve or reject.

**Key user requirement**: Every entity must have an **owner** — a user account (not a person entity). Currently, only entities created by non-admin users have explicit owners. All 36 seed entities are ownerless. This must be fixed as a prerequisite.

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| `requires_approval` config | Code array in `lib/config/permissions.ts` | Matches existing pattern (`ADMIN_ONLY_REL_TYPES`, `EDIT_GRANTING_REL_TYPES`). Easy to change without migrations. |
| Which rels need approval | `member_of`, `hosted_at` | Self-claims (`attended`, `spoke_at`, `contributes_to`, `tagged_with`) are low-risk. Admin-only rels (`founded`, `organized`, `manages`) are unchanged. |
| Auto-approve shortcut | Yes, if requester owns/edits target | If you own both sides, no approval needed. |
| Backfill strategy | SQL migration deriving owners from `founded`/`manages` relationships + admin fallback | Idempotent, handles unclaimed persons gracefully. |
| HTTP status for pending | `202 Accepted` | Distinguishes from `201 Created` (direct relationship). Client checks response to show appropriate feedback. |

## Files to Create/Modify

### Stage A — Foundation (schema + config + types)

1. **`db/migrations/006_add_relationship_requests.sql`** (new)
   - `relationship_requests` table: `id`, `requester_id`, `source_id`, `target_id`, `rel_type`, `label`, `metadata`, `status` (pending/approved/rejected), `decided_by`, `decided_at`, `created_at`
   - Partial unique index on `(source_id, target_id, rel_type) WHERE status = 'pending'` — prevents duplicate pending requests while allowing resubmission after rejection

2. **`db/migrations/007_backfill_entity_owners.sql`** (new)
   - Step 1: For each `founded`/`manages` relationship where the source person is claimed (has a user), grant `owner` on the target entity
   - Step 2: For remaining ownerless entities (except claimed person entities, which have implicit self-edit), assign the admin user as fallback owner
   - Idempotent via `ON CONFLICT DO NOTHING`

3. **`lib/config/permissions.ts`** — Add `REQUIRES_APPROVAL_REL_TYPES: string[]` = `['member_of', 'hosted_at']`

4. **`lib/types.ts`** — Add `RelationshipRequestStatus`, `RelationshipRequest`, `RelationshipRequestWithDetails` types

### Stage B — Backend (queries + API)

5. **`lib/queries.ts`** — Add relationship request functions:
   - `createRelationshipRequest()` — insert pending request
   - `getRelationshipRequestById()` — fetch single request
   - `getPendingRequestsForUser()` — requests for entities the user owns/edits (join with entity_permissions + edit-granting relationships)
   - `getAllPendingRequests()` — admin view
   - `getRequestsByRequester()` — user's own submitted requests
   - `approveRelationshipRequest()` — in a transaction: update status + create real relationship
   - `rejectRelationshipRequest()` — update status
   - `getEntityOwners()` — users with explicit owner/editor permission on an entity
   - `countPendingRequestsForUser()` — for navbar badge

6. **`app/api/relationships/route.ts`** — Modify POST handler:
   - After direction normalization and existing permission checks
   - New branch: if `!user.is_admin && REQUIRES_APPROVAL_REL_TYPES.includes(rel_type)`:
     - Check `canEditEntity(user, targetId)` — if yes, fall through to direct creation (auto-approve)
     - If no, create a pending request and return `202` with `{ ...request, _type: 'request' }`
   - Existing behavior for non-approval rel types is unchanged

7. **`app/api/relationship-requests/route.ts`** (new) — GET:
   - `?mine=true` → user's submitted requests
   - Admin → all pending requests
   - Non-admin → requests for entities they own

8. **`app/api/relationship-requests/[id]/route.ts`** (new) — PATCH:
   - Body: `{ action: 'approve' | 'reject' }`
   - Permission check: `canEditEntity(user, request.target_id)`
   - Approve: transactional status update + relationship creation
   - Handle duplicate relationship (409), already-decided (404)

### Stage C — E2E Tests (TDD)

9. **`tests/relationship-requests.spec.ts`** (new)
   - **API tests**: auto-approved rels bypass flow, requires_approval creates 202, auto-approve if requester owns target, admin direct creates, duplicate pending 409, owner approves, owner rejects, non-owner 403, admin approves any, already-decided 404
   - **UI tests**: form shows pending feedback for approval types, owner sees pending requests, approve/reject via UI, requests page lists incoming/outgoing

### Stage D — UI

10. **`components/AdminRelForm.tsx`** — Handle `202` response: show "Request submitted — pending approval" message instead of closing modal immediately. Show note below rel type dropdown when a `REQUIRES_APPROVAL` type is selected.

11. **`components/RequestActionButtons.tsx`** (new) — Client component with Approve/Reject buttons, calls PATCH API, `router.refresh()` on success.

12. **`app/requests/page.tsx`** (new) — Server component at `/requests`:
    - "Incoming Requests" — pending requests for entities you own, with approve/reject buttons
    - "My Requests" — requests you submitted, with status badges (pending/approved/rejected)

13. **`components/InlineAdminControls.tsx`** — Add "Pending Requests (N)" section in sidebar when owner views an entity with pending requests. Shows compact list with approve/reject buttons.

14. **Navbar** (`components/UserMenu.tsx` or layout) — Pending request count badge linking to `/requests`.

### Stage E — Documentation

15. **`CLAUDE_DOCS/relationship-requests.md`** (new) — Feature doc
16. Update **`CLAUDE.md`** architecture section and **`CLAUDE_DOCS/PHASES.md`**

## Backfill Analysis (Seed Data)

The backfill migration will derive ownership from these existing relationships:
- **Atlassian** → Scott + Mike (both `founded`)
- **Canva** → Melanie (`founded`)
- **Culture Amp** → Didier (`founded`)
- **Envato** → Nicholas (`founded`)
- **Inspire9** → Leni Mayo (`founded`)
- **Inspire9 Richmond** → Leni Mayo (`manages`)

All other entities (SEEK, YBF, MSB, Startup Vic, LaunchVic, all events, MCEC, RMIT, YBF CBD, all projects, all topics, unclaimed people) → **admin fallback owner**.

Note: `organized` relationships have organizations as sources (not people), so they don't directly map to user ownership. Events organized by orgs inherit admin as fallback. Admins can reassign later.

## Verification

1. Run `npm run db:migrate` — verify both migrations apply cleanly
2. Query `entity_permissions` — verify all entities have at least one owner
3. Run `npx playwright test tests/relationship-requests.spec.ts` — all tests pass
4. Manual: log in as non-admin, try to create `member_of` relationship → see 202 pending
5. Manual: log in as entity owner, go to `/requests` → see pending request, approve it → verify relationship appears
6. `npx tsc --noEmit` + `npm run build` — no type errors
