# You Have a DSL

**Project**: customer-relations (healthcare CRM)
**Date**: 2026-04-14

During an architecture review of the CRM, I traced three information leaks back to a common cause: the system's YAML configuration had outgrown the word "configuration." It generates database tables, API endpoints, UI windows, import pipelines, and validation rules from two YAML files. That's not parameterizing fixed behavior — that's a program being interpreted.

Once we named it, the structure became visible:

- `schema-loader.ts` is a **parser and type checker** — it validates referential integrity, checks that field references in display blocks point to real fields, confirms enum types have values arrays. Structured diagnostics with `Entity "name".field` paths.
- `field-types.ts` is a **terminal symbol table** — 12 entries, each mapping a type name to five concerns (DB type, validation, HTML input, display rendering, persistence normalization). Five interpreters, one table.
- `naming.ts` defines **morphology rules** — how identifiers transform between YAML, Prisma, database, and UI contexts.
- The five-layer architecture (schema -> engine -> repository -> API -> UI) *is* the compilation pipeline.

The template interpolation syntax (`{field}`) gives the language expressiveness beyond flat config but keeps it far from Turing-complete. It's at the "mini-language" stage — the sweet spot.

The practical value of recognizing this: when we found a hardcoded `if (entityName === "attachment")` check in the renderer, the fix wasn't a new design pattern — it was extending the grammar. We added an `actions` production rule to the display DSL, updated the type checker, and the Interpreter handled the rest. Same for a date-format contract between the import engine and repository — we added `normalize` to the terminal symbol table and both modules could stop knowing about each other's internals.

The lesson that stuck with me: **a system can cross the threshold from configuration to language without anyone noticing.** The architecture review caught it because we were looking for information leaks, and the leaks all pointed to the same cause — places where the language ran out of expressiveness and someone dropped into the host language. The fix is always: grow the grammar.

Robin asked the right question: "I have a domain specific language?" Yes. And it has a type checker.
