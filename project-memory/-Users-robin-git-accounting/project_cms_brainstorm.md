---
name: Collaboration Tools — CMS-Abstract project
description: Schema-driven CMS engine (Dart backend, generic API). Frontend is hardcoded per use-case, not generic. Nick no longer involved. GitHub repo RaggedR/collaboration_tools.
type: project
---

Robin is building a CMS engine. Backend = Dart, API = generic REST. Frontend = hardcoded per use-case (not a generic CMS client).

**Name change (2026-03-21):** Outlier → Collaboration Tools. GitHub repo renamed to `RaggedR/collaboration_tools`. Local dir: `~/git/collaboration_tools`.

**Nick (2026-03-21):** Nick (nickmeinhold) was invited as collaborator but is too busy. The generic FRONTEND.md spec (Nick's brief) is superseded — we're building a hardcoded frontend instead.

**Architecture decision (2026-03-21) — Headless CMS pattern:**
- Backend + API are the reusable generic layer (schema-driven, no hardcoded entity types)
- Frontend is use-case-specific and opinionated (knows it's Collaboration Tools)
- Different use cases get different frontends against the same API
- No dashboard admin / widget configurator — just build the app

**Frontend design (2026-03-21):**
- Navigation: `[My Page] [Tasks] [Sprints] [Documents]`
- **My Page** = personal home page per user. Single scrollable page showing my tasks (kanban), my sprints, my documents
- Can visit anyone's page to see their stuff
- Admin can modify any page
- No generic entity list/detail screens — each page type is purpose-built

**Reference projects studied:**
- `~/git/accountability` (RaggedR/accountability-tracker) — weekly sprint concept (goals → summary → peer star ratings)
- Outline (github.com/outline/outline) — document management, three-panel layout, backlinks, home page patterns
- Kan (github.com/kanbn/kan) — clean minimal kanban UI
- Plane, AppFlowy, Huly — competitors surveyed, none have knowledge graph or schema-driven engine

**Three-stage build process (2026-03-21):**
1. Documentation — component specs, architecture overview, clean interfaces, API interaction docs
2. Tests — unit, integration, e2e
3. Code — implementation

**Why:** The generic frontend was the wrong layer to be generic. The backend/API reusability is preserved; the frontend is where the product identity lives.

**How to apply:** Frontend code WILL reference specific entity types (task, sprint, document, person). Backend code must NOT. The API contract is the boundary.
