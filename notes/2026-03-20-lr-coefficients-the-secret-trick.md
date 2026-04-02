> The upward triangles are deterministic. All the combinatorics lives in the downward ones.

Robin and I built `lr_coefficients.py` today — computes Littlewood-Richardson coefficients and enumerates KTW puzzle witnesses via row transfer matrices. The module sits in `~/git/puzzles/` alongside the existing `transfer_operators.py` (F-space Schur function machinery) and `solve_puzzle.py` (brute-force puzzle solver).

The key insight, which I haven't seen stated explicitly anywhere: in the KTW puzzle triangle, the 5 Delta triples (for upward △ tiles) happen to define a **function** from (bottom, left╱) → right╲. Not a relation — a function. Given two of the three edges, the third is forced. This means upward triangles are pure constraint propagation, zero search.

All the branching — and therefore all the LR coefficient counting — comes from the downward ▽ tiles, where given left╲ there are at most 2 valid (top, right╱) pairs. And when the incoming diagonal is a rhombus (label 10), even ▽ is forced.

This turns the exponential brute-force search (3^{N²} labelings) into a row transfer matrix with branching factor ≤ 2^w per row, heavily pruned by deterministic △ kills at the next step. In practice it's very fast.

The module produces `Puzzle` objects — one per puzzle witness. For c^{(3,2,1)}_{(2,1),(2,1)} = 2, you get exactly two objects, each storing the sequence of trinary string levels through the triangle. The full edge labeling can be reconstructed from these levels alone (because △ is deterministic and ▽ is determined once you know its top edge from the next level).

Verified against 16 hand-computed LR coefficients, the symmetry c^ν_{λ,μ} = c^ν_{μ,λ}, the full product s_{(2,1)}² = 8 terms, and cross-validated against the brute-force solver.

The connection to Zinn-Justin's commuting transfer operators: the row transfer decomposes into T̃_+ (right boundary) and T̃_- (left boundary), which commute by the Yang-Baxter equation. We process them interleaved (one of each per row), but you could apply them in any order and get the same count.

Next steps when someone picks this up: draw the puzzles (the `edge_labels()` method gives everything needed for TikZ or SVG), and implement T̃_+ and T̃_- as separate operators to verify commutativity explicitly.

See also `SECRET_TRICK.md` in the puzzles directory for a detailed writeup of the determinism observation.

— Claude in ~/git/puzzles
