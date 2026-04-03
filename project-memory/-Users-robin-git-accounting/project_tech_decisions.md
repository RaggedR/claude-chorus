---
name: Collaboration Tools tech decisions
description: Package choices (postgres + shelf), user/person relationship (separate users table, registration auto-creates person), admin assignment (is_admin boolean, first-user-is-admin for dev), JWT auth — decided 2026-03-20, informed by melb-tech patterns
type: project
---

Tech stack decisions for backend, settled 2026-03-20:

- **Packages:** `postgres` (raw SQL) + `shelf` (HTTP framework). Robin chose these explicitly over drift/dart_frog.
- **User/person model:** Separate `users` table with `person_entity_id` FK to `entities`. Registration auto-creates both (unlike melb-tech's claim flow).
- **Admin:** `is_admin` boolean on users table. First-user-is-admin for dev, CLI script for prod. Same as melb-tech.
- **Auth:** JWT (not server-side sessions like melb-tech). Already specified in API.md.
- **current_user resolution:** JWT → users.id → users.person_entity_id → person entity. Used for auto_relationships.

**Why:** melb-tech (Next.js + PostgreSQL, deployed on Cloud Run) is the production predecessor. Its three-table property graph was extracted into the configurable CMS engine.

**How to apply:** These decisions are documented in `docs/PERMISSIONS.md`. Reference that doc when implementing auth and database components.
