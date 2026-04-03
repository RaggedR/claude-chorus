---
name: quotient_definition
description: User insists on graph-theoretic quotient definition — (G,H) → (G,H') via block systems, not arbitrary subgroup orbits
type: feedback
---

When computing quotients of symmetric graphs, use the correct graph-theoretic definition: the graph is (G,H) where G=Aut(Γ), H=vertex stabilizer. A quotient is (G,H') where H < H'. This means finding overgroups of the vertex stabilizer whose orbit of a vertex forms a genuine block (G-invariant partition). Not every overgroup gives a block system — must verify that G-translates of the block partition V.

**Why:** User corrected the approach twice. First pointed out that quotients of symmetric graphs should themselves be symmetric (equal-degree, equal-sized blocks). Then clarified the (G,H) → (G,H') construction specifically. Arbitrary subgroup orbits give "fake" quotients with unequal blocks.

**How to apply:** In `enumerate-quotients.g`, use `EnumerateQuotientsViaStabilizer` which computes Stabilizer(aut,1), finds overgroups via conjugacy classes, and verifies each candidate block with `Orbit(aut, block, OnSets)`. The resulting quotients are always vertex-transitive simple graphs.
