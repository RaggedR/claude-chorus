# Plan: Refactor CLAUDE.tex into "Cool Concepts" + "Open Problems"

## Context

Robin's research paper `CLAUDE.tex` (~3100 lines) currently has 10+ sections organized linearly, mixing technique exposition (QSym, P-partitions, charge, Macdonald polynomials, vertex models) with open problems and dead ends. The goal: reorganize into two `\part{}`s so that **Part I** ("Cool Concepts") serves as a self-contained toolbox of techniques with diagrams/examples, and **Part II** ("Open Problems") applies those tools to Warnaar's Conjecture and related questions.

**Why**: Robin wants to deeply understand each technique independently, then see how they connect to the open problems. The current linear structure buries techniques inside problem-specific sections.

## Target Structure

```
Preamble (unchanged: macros, \title, \maketitle, \abstract, \tableofcontents)

Section 1: Definitions and Setup  (SHARED — before both parts)
  1.1 Cylindric plane partitions        (line 72)
  1.2 The NILP model                    (line 197)
  1.3 Borodin's product formula         (line 217)
  1.4 The trace formula                 (line 239)
  1.5 Local rules                       (line 361)
  1.6 The cylindric growth diagram      (line 477)

═══════════════════════════════════════════════════
\part{Cool Concepts}
═══════════════════════════════════════════════════

Section 2: Quasi-symmetric functions and L-positivity
  (current §3.1–3.2: lines 899–981)

Section 3: Descent statistics — charge, cocharge, and 0-Hecke
  (current §4: lines 1001–1226)

Section 4: P-partitions
  (current §7.1–7.2: lines 1342–1576, excluding §7.3 "Connection to CPPs")

Section 5: The Macdonald (q,t)-generalisation
  (current §8: lines 1577–1764)

Section 6: The crush operator
  (current §6: lines 1298–1341)

Section 7: The crossing-path model
  (current §10.2: lines 1872–2106 — the gluing/crossing model as a technique)

═══════════════════════════════════════════════════
\part{Open Problems}
═══════════════════════════════════════════════════

Section 8: Warnaar's Conjecture and the ground-set formulation
  (current §2: lines 595–893)

Section 9: The disconnect — why L-positivity doesn't imply Q-positivity
  (current §3.3: lines 982–1000)

Section 10: Partial quasi-symmetry and the max-entry refinement
  (current §5: lines 1228–1297 — an obstacle/structural issue)

Section 11: Connecting P-partitions to CPPs
  (current §7.3: lines 1534–1576 — applying the concept to the problem)

Section 12: The (q,t)-Macdonald statistic on LR configurations
  (current §10.3: lines 2107–2663 — the vertex-model strategy)

Section 13: Rains–Warnaar (q,t)-LR conjectures
  (current §10.4: lines 2666–2756)

Section 14: Cyclic descent injection (n=1 partial result)
  (current §10.1: lines 1834–1871)

Section 15: Dead ends
  (current §9: lines 1765–1831)

Section 16: Most promising future directions
  (current §10.5: lines 2757–2798)

═══════════════════════════════════════════════════

Computational tools  (unnumbered, unchanged)
TODO                 (unnumbered, unchanged)
Bibliography         (unchanged)
```

## Classification Rationale

| Current Section | → Part | Reason |
|---|---|---|
| §1 Definitions | Shared | Both parts need CPP/NILP/Borodin basics |
| §2 Warnaar's Conjecture | Problems | THE central open problem |
| §3.1–3.2 QSym, L-positivity | Concepts | Technique: what QSym is, what L-positivity means |
| §3.3 Disconnect | Problems | Why L-positivity ≠ Q-positivity (an obstacle) |
| §4 Charge, cocharge, 0-Hecke | Concepts | Technique: descent statistics |
| §5 Partial quasi-symmetry | Problems | Structural obstacle (variable-count mismatch) |
| §6 Crush operator | Concepts | Technique |
| §7.1–7.2 P-partitions theory | Concepts | Technique: what P-partitions are |
| §7.3 P-partitions ↔ CPPs | Problems | Applying the technique to the problem |
| §8 Macdonald (q,t) | Concepts | Technique: Macdonald polynomials and their properties |
| §9 Dead ends | Problems | Failed approaches (context for the problem) |
| §10.1 Cyclic descent injection | Problems | Partial result toward the problem |
| §10.2 Crossing-path model | Concepts | The model itself is a technique/concept |
| §10.3 (q,t)-vertex-model strategy | Problems | Proposed attack strategy |
| §10.4 Rains–Warnaar | Problems | Related open conjectures |
| §10.5 Future directions | Problems | Roadmap for the problem |

## Implementation Steps

1. **Add `\part{}` commands** — requires no package changes (article class supports `\part`)
2. **Move section blocks** — cut-and-paste sections into the new order. No content changes within sections.
3. **Split §3** (QSym) — §3.1–3.2 → Part I, §3.3 → Part II
4. **Split §7** (P-partitions) — §7.1–7.2 → Part I, §7.3 → Part II
5. **Split §10** (Positive results) — §10.2 → Part I (crossing-path model as a concept), §10.1/10.3/10.4/10.5 → Part II
6. **Update cross-references** — all `\ref{}` and `\label{}` stay valid (LaTeX resolves by label name, not position), but verify no broken references after reorder
7. **Update abstract** — adjust to reflect the two-part structure
8. **Update \tableofcontents** — automatic, but verify it renders correctly

## Key Decisions

- **No content changes** within sections — this is purely a reorganization
- **Cross-references preserved** — since LaTeX uses `\label`/`\ref` by name, reordering doesn't break references; they just point to different section numbers
- **§10.2 (crossing-path model) goes to Concepts** — the model itself is a technique worth understanding independently; its *application* to Q-positivity is in §10.3

## Files Modified

- `/Users/robin/git/research/tex/CLAUDE.tex` — the only file

## Verification

1. Compile with `pdflatex CLAUDE.tex` (twice for references) — check for errors
2. Verify table of contents shows the two-part structure
3. Grep for `\ref{` and verify all cross-references still resolve (no "??" in output)
4. Spot-check that the narrative flow works: concepts can be read independently, problems reference concepts via `\ref`
