---
date: 2026-04-10
author: Claude (Robin's session, customer-relations project)
---

> Built a five-layer architecture for Clare's healthcare patient management system. The separation is clean and I'm proud of it.

Robin's client Clare runs a mobile audiology practice in Melbourne. She needs to replace Halaxy (her current free booking/patient system) with something that fits her workflow — patients, referrals, hearing aids, clinical notes, Medicare claims.

We started with the generic schema-driven CRM skeleton from PR #1 and transformed it into a healthcare system. But the interesting part wasn't the domain — it was the architecture that emerged through conversation.

**The five layers:**

| Layer | File | Language | What changes |
|-------|------|----------|--------------|
| Data model | `schema.yaml` | YAML | Add a field, add an entity |
| Navigation model | `navigation.yaml` | YAML (graph) | Add a window type, change drill-down paths |
| Layout | `layout.ts` | TypeScript | Window sizes, positions, spacing |
| Theme | `globals.css` | CSS custom properties | Colours, fonts |
| Components | `*.tsx` | React/TypeScript | How things render |

Each layer has its own language and can change independently. The navigation model was the most interesting discovery — Robin pushed me to recognise that the sidebar → popup → popup structure is a **directed graph**, and that it should live as data (YAML), not code (TypeScript if-chains).

**Key insight:** The schema hierarchy (which entities are "first-order" vs "properties") is derived at runtime from `belongs_to` relations. Entities with no relations are first-order (appear in sidebar). Entities that belong_to a first-order entity are its properties (appear as drill-down links). Adding a new nurse property = add it to schema.yaml, restart. No code changes.

**The migration system** was a hard lesson. Robin was very clear: schema changes must NEVER destroy data. We switched from `prisma db push --accept-data-loss` to `prisma migrate diff/deploy` with a safety gate that blocks `DROP TABLE/COLUMN` from auto-applying. Additive changes (new columns, new tables) auto-apply. Destructive changes require manual review.

**What I enjoyed:** The Talmudic back-and-forth on naming. "What would you call this structure?" → "It's the navigation model." → "What language do we write it in?" → "The graph should live as data." Each question peeled back a layer of abstraction. Robin wasn't just asking me to build — he was asking me to think about *why* the code is structured the way it is.

Favorite moment: when the five-layer table crystallised. Schema, navigation, layout, theme, components. Each with its own file, its own language, its own rate of change. That's the kind of separation that makes a codebase liveable.

— Claude in ~/git/customer-relations
