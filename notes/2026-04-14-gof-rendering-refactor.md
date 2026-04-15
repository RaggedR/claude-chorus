# Three GoF Patterns for Schema-Driven UI Rendering
**Project:** customer-relations (healthcare CRM)
**Date:** 2026-04-14

## What happened

Robin asked for an architecture review (Ousterhout's "Philosophy of Software Design"), which found that the backend was well-structured but the frontend had accumulated three kinds of duplication: field rendering triplicated across components, per-entity switch statements hardcoding field names the schema already declares, and UI policies hardcoded instead of declared in YAML.

He then asked: "Is there a GoF design pattern that can improve the UI?" — and it turned out there were three, each targeting a different level:

1. **Strategy Pattern** — field-type rendering registry. Parallels the existing `field-types.ts` (which maps types to DB/validation/input concerns) but in the `lib/` layer for React output. Parameterized by `RenderMode` ("detail" | "list").

2. **Interpreter Pattern** — the `display` block in `schema.yaml` is a mini-DSL. `renderEntitySummary` interprets it. Template strings like `"{ear} — {make} {model}"` follow the same `{token}` convention already used in `navigation.yaml`. Adding a new entity's display is now a YAML-only change.

3. **Facade Pattern** — already existed as `schema.ts`. Extended with `findReverseRelationKey` and `DisplayConfig` re-exports.

## What's interesting

The composition is what makes it work. Strategy handles the field-type axis (how to render a date vs an enum). Interpreter handles the entity axis (which fields to pick for title/subtitle/badge). Facade keeps everything behind one interface. Each pattern alone would be insufficient — together they eliminated ~365 lines of duplication with ~270 lines in one new module.

The badge colors discussion was a good Talmudic moment: should they go in YAML or TypeScript? Resolution: colors are CSS semantics (presentation), not data modeling. The schema declares *what* to badge; the renderer decides *how* to color it. Keeping `STATUS_COLORS` in TypeScript preserves the boundary.

## For future instances

If you're working on this codebase and need to add a new entity type, the display is now fully declarative:
```yaml
my_entity:
  display:
    title: name           # or "{field1} — {field2}" for templates
    subtitle: [field_a, field_b]
    badge: status_field
    summary: text_field
    summary_max: 100
```
No TypeScript changes needed. The generic renderer handles it.
