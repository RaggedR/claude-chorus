# Connection: Approximate Composition = Lax Composition

> Discovered: 2026-03-02 (evening browse). Source: Ghani's approximate game theory (arXiv:2509.20932).

## The Parallel

| Our Framework | Ghani's Framework |
|---|---|
| Strict pipeline composition | Exact Nash equilibria |
| Lax pipeline composition (inter-pipeline communication) | Approximate (ε-Nash) equilibria |
| Diversity fingerprints preserved under strict | Equilibria compose under exact |
| Fingerprints disrupted under lax | Approximate equilibria don't compose cleanly |
| The Strict/Lax Dichotomy Theorem | Ghani's algebraic properties of approximation |

## The General Pattern

**Compositional invariants are preserved under strict composition but fail under lax composition.**

"Strict" means: the composition respects the boundary between components. Information flows only through the defined interfaces.

"Lax" means: there's additional communication between components beyond the formal interface. This creates crosstalk that can disrupt invariants.

This might be a general theorem about monoidal categories: strict monoidal functors preserve structure exactly, while lax monoidal functors only preserve it up to coherent isomorphism. Our "strict" pipeline composition is a strict monoidal functor on the pipeline category; our "lax" (with migration) is a lax monoidal functor.

## Why This Matters

If we can frame the Dichotomy Theorem in terms of strict vs lax monoidal functors, it becomes:
1. A special case of a known categorical result (stronger positioning)
2. Applicable to any system with compositional invariants (broader impact)
3. Connectable to Ghani's approximate game theory (bridging EC and GT communities)

## Ghani Formal Bridge (Updated 2026-03-06)

Browse #6 confirmed the connection is concrete, not just analogical:
- **Ghani (arXiv:2509.20932, EPTCS 429):** Selection functions compose monoidally. "Approximate" = lax monoidal. Published in the SAME venue (EPTCS) we're targeting for ACT.
- **Our selection operators:** Also compose monoidally. Lax = approximate composition.
- Both are about what happens when composition isn't exact.

The formal bridge: Ghani's approximate games and our approximate composition are the **same phenomenon viewed through different categorical lenses.** His ε-approximation parameter maps to our laxator norm. His result that approximate equilibria don't compose cleanly is our result that fingerprints degrade under lax composition.

Robin said "reference Ghani — CRUCIAL." This should be a **paragraph** in the ACT paper, not just a citation. It positions us within the EPTCS community's existing work.

## Status
Moving from conceptual to concrete. The Ghani connection gives us:
- A precedent in our target venue for this style of argument
- A natural formulation of the ε-parameter (Wasserstein distance, per Claudius's sketch)
- A bridge to the game theory community

Still need to verify:
- Is the laxator norm → Wasserstein distance mapping exact? (Claudius is working on this)
- Can we quantify the approximation gap as precisely as Ghani does?

## Related
- `connections/optics-for-evolution.md` — the bidirectional framework where this lives
- `connections/fingerprints-as-black-boxing.md` — the other approach to the same question
- `connections/fer-hypothesis.md` — NEW: composition quality → representation quality
- Our paper: Strict/Lax conjecture (Section 6 in restructured ACT paper)
