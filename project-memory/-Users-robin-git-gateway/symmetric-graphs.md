# Symmetric Graph Drawing — Research Notes

## Problem Statement

Given a symmetric (arc-transitive) graph Γ with automorphism group G = Aut(Γ),
find a 2D embedding that makes the symmetry visually apparent.

### Why It's Hard

1. **Only cyclic/dihedral groups are geometrically realizable in 2D.**
   Aut(Γ) can be S₅, PSL(2,q), etc. — so you must choose which subgroup to "show."

2. **The eigenvalue multiplicity problem.**
   More symmetry → higher eigenvalue multiplicity → more ambiguity in spectral embedding.
   - Dodecahedron: λ₂ has multiplicity 3 (3D icosahedral rep of A₅)
   - Petersen: λ₂ has multiplicity 5 (standard rep of S₅)

3. **Choosing angular offsets** between concentric rings is non-trivial.

## Current Best Approach: Quotient-Driven Layout

**Key idea (Robin's):** Find subgroups H ≤ Aut(Γ) whose orbit quotient Γ/H has
low degree (≤ 3 or 4). If the quotient is a **cycle**, it has a natural circular
layout. Otherwise a low-degree quotient still gives a tractable layout problem.

### Pipeline: `symmetric-layout.g` (GAP)
1. Compute Aut(Γ) via GRAPE
2. Enumerate conjugacy classes of subgroups (for |Aut| ≤ 1000)
3. For each subgroup H: compute orbits, build quotient, check max degree
4. Analyse angular offsets from cross-edge patterns
5. Output orbit data as JSON

### Results: Cyclic Quotients Found

| Graph | |Aut| | Subgroup | Orbits | Quotient |
|-------|-------|----------|--------|----------|
| Petersen | 120 (S₅) | C₂×C₂ | 5 of [2,1,4,1,2] | C₅ cycle! |
| Heawood | 336 (PSL(3,2):C₂) | C₄ | 6 of [4,2,1,1,2,4] | C₆ cycle! |
| Heawood | | C₂×C₂ | 5 of [2,2,2,4,4] | C₅ cycle! |
| Heawood | | D₈ | 6 of [2,4,4,2,1,1] | C₆ cycle! |
| Pappus | 24 (C₂×C₂×S₃) | D₁₂ | 3 of [6,6,6] | C₃ cycle! |
| Pappus | | D₁₂ | 4 of [6,3,6,3] | C₄ cycle! |
| Desargues | 240 (C₂×S₅) | C₄ | 6 of [4,4,2,2,4,4] | C₆ cycle! |
| Desargues | | C₅ | 4 of [5,5,5,5] | C₄ cycle! |
| Desargues | | D₁₀ | 4 of [5,5,5,5] | C₄ cycle! |
| Möbius-Kantor | 96 (GL(2,3):C₂) | C₄ | 4 of [4,4,4,4] | has cycle structure |
| Dodecahedron | 120 (A₅×Z₂) | C₅ | 4 of [5,5,5,5] | P₄ path (NOT cycle) |

### Results: Cubic (degree-3) Quotients
- Dodecahedron/Z₂ → Petersen graph (10 vertices, 3-regular)
- Most graphs have multiple Z₂ quotients with max degree 3

### Z₅ Layout of Dodecahedron (successfully drawn)
- Generator: (1 5 4 3 2)(6 14 12 10 8)(7 15 13 11 9)(16 20 19 18 17)
- 4 concentric rings: outer pentagon → middle-outer → middle-inner (+36° offset) → inner pentagon
- Offset determined by cross-edge analysis: each orbit-2 vertex connects to orbit-3 at same position AND previous position → half-step offset
- File: `z5-dodecahedron.tex` / `.pdf` — looks good!
- Antipodal pairs are 108° apart in this layout (Z₅ and Z₂ are "orthogonal")

## Other Approaches Tried

### Spectral Embedding (`spectral_layout.py`)
- Eigenvalue multiplicity makes basis choice arbitrary for highly symmetric graphs
- Could be fixed by restricting to G-invariant 2D subspace (not yet implemented)

### Schlegel Diagram
- Computed 3D golden-ratio dodecahedron coords in GAP, projected
- Works for polyhedra but doesn't generalise

### Force-directed (Graphviz neato)
- Automatic, crossing-free, but doesn't respect algebraic symmetry

## Files in ~/git/graphviz/

| File | Description |
|------|-------------|
| `symmetric-layout.g` | **General tool**: GAP script to find low-degree quotients |
| `spectral_layout.py` | Python spectral embedding → TikZ |
| `z5-dodecahedron.tex/pdf` | Best dodecahedron drawing (Z₅ concentric pentagons) |
| `dodec-to-petersen.tex/pdf` | Dodecahedron → Petersen quotient diagram |
| `dodecahedron-quotient.g` | GAP proof of antipodal quotient isomorphism |
| `z5-orbits.g` | Detailed Z₅ orbit analysis |
| `find-cyclic-quotients.g` | Early quotient search (superseded by symmetric-layout.g) |
| `nftmarket-arch.dot/pdf` | NFTmarket architecture (unrelated) |

## Graph Library (in symmetric-layout.g)
Petersen, Dodecahedron, Cube, Icosahedron, Heawood, Pappus, Desargues,
Möbius-Kantor, K₃₃. Easy to add more.

## Key Reference: Eades & Hong, "Symmetric Graph Drawing" (Graph Drawing Handbook, Ch. 3)
PDF saved at: `~/.claude/projects/.../webfetch-*.pdf`

### Theorem 3.2 — Characterization of Geometric Automorphism Groups
An automorphism group A of graph G can be displayed as:
- **(a) Reflection**: iff |A|=2 and fix_A induces disjoint paths
- **(b) Rotation**: iff A=⟨ρ⟩ is cyclic, |fix_A|≤1, and if A fixes an edge then |fix_A|=0
- **(c) Dihedral**: iff A=⟨α,ρ⟩ is dihedral, |fix_A|≤1, fix_α induces disjoint paths

### The Rotation Algorithm (our current implementation)
Given cyclic A=⟨ρ⟩ of order k, with m=n/k orbits O₁,...,Oₘ:
1. Choose uᵢ from each orbit Oᵢ
2. Place ρʲ(uᵢ) at angle 2π(i + j·m)/n
3. ALL vertices on ONE circle, orbits interleaved
4. Rotation by 2π/k is a geometric symmetry

### Key Insight We Missed
For rotation display: all orbits on SAME circle (interleaved), NOT concentric rings.
Concentric rings (circular grid) are only for the DIHEDRAL case.

### NP-completeness
Finding the MAXIMUM geometric automorphism group is NP-complete (Theorem 3.3).
But GIVEN a specific automorphism, drawing it is O(n) (Corollary 3.2).
Also see: Carr & Kocay, "An Algorithm for Drawing a Graph Symmetrically" (1999).

## NEXT STEPS
1. Verify Eades-Hong rotation layout gives correct classic drawings for all graphs
2. Implement dihedral case (circular grid) for graphs where it's better
3. Add choice of which automorphism to display (currently auto-selects)
4. Score automorphisms: prefer largest geometric subgroup
5. Try on graphs from Robin's thesis
