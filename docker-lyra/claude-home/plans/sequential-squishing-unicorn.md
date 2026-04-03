# Plan: Create README.md for qhask

## Context
The qhask library (14 modules, 173 tests) has no README. It has CLAUDE.md and CLAUDE_DOCS/ for AI context, but nothing for a human (or GitHub visitor) landing on the repo. We need a concise, well-structured README.

## Approach
Create a single `README.md` at the repo root with progressive disclosure (gist from headers, details on drill-down).

## Structure

1. **Header + badge line** — name, one-line description
2. **What it does** — 3-sentence overview covering q-series, partitions, symmetric functions
3. **Quick start** — build/test/repl (3 commands)
4. **Example session** — GHCi snippets showing the library in action (q-series, partitions, symmetric functions, basis change)
5. **Modules** — table of all 14 modules with one-line descriptions, grouped by domain
6. **Design choices** — bullet list: lazy lists, Integer vs Rational, phantom types, Schur hub, minimal deps
7. **Testing** — what the 173 tests cover, how to run
8. **Dependencies** — GHC 9.6+, base + containers only

## Files to create
- `README.md` (new)

## Files to reference (read-only, for content)
- `CLAUDE.md` — architecture overview
- `qhask.cabal` — version, deps, GHC constraint
- `src/QHask/Sym/Types.hs` — phantom type pattern
- `src/QHask/QSeries.hs` — QSeries type

## Verification
- `cabal build` and `cabal test` still pass (no code changes)
- README renders correctly (valid markdown, no broken references)
