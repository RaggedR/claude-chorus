# Max-Entry Refinement Details

## Files
- `verify_partial_qsym.py` — verifies partial QSym of g_tilde_n (55/55 profiles pass)
- `MAX_PART.tex` — 13-page survey document on max-entry refinement
- `QUASI_SYMMETRIC.tex` — updated with 0-Hecke remark (Section 6.2), partial QSym (Section 5.3)

## Key equations (MAX_PART.tex)
- Eq (5): g_{n,λ}(q) = RPPs of shape λ with exact max = n, by weight
- Eq (8): RPPs with max ≤ n = s_λ(1,q,...,q^{n-1}) (principal specialization)
- Eq (9): g_{n,λ}(q) = s_λ(1,q,...,q^{n-1}) - s_λ(1,q,...,q^{n-2}) (differencing)
- Eq (9) is the RPP analogue of E-H: cumulative ≤n is clean, exact =n needs subtraction

## Partial quasi-symmetry verification
- g_tilde_n ∈ z_n · QSym(z_1,...,z_{n-1})[z_n]
- Argument: relabelling non-n values preserves interlacing (depends on relative order only)
- n held fixed → all inequalities with n-entries automatically satisfied
- M_to_L_bounded(M_coeffs, max_len): restricts Möbius inversion to compositions with length ≤ max_len
- Bug found: M_to_L from cpp_library.py is infinite-variable, gave false L-negativity for r < ∞

## Slice L-positivity failure (structural, not a bug)
- At n=3, r=2 variables: M_(k) counts CPPs where all non-n values equal (one distinct value)
- M_(j,k-j) counts CPPs with exactly two distinct non-n values
- M_(k) = 2 > M_(j,k-j) = 1 for typical profiles → L_(a,b) = M_(a,b) - M_(a+b) = -1

## Gansner vs Frequency comparison
| Feature | Gansner (traces) | Frequency (ours) |
|---------|-----------------|------------------|
| Variable | x_d per diagonal d | z_k per value k |
| Statistic | t_d = sum on diagonal d | #_k = cells with entry k |
| Symmetry | Symmetric in each x_d | Quasi-symmetric in z_k's |
| Product formula | Yes (hook product) | No |
| Sees max entry | No | Yes |
| Specialization | x_d → q gives weight | z_k → q^k gives GK(1,q) |

## Crush operator on QSym
- Combinatorially: subtract 1 from every positive entry of CPP
- On frequency GF: z_k → z_{k-1} (shift variable index)
- z_1 → z_0: cells with value 1 "fall off" (need z_0 formal variable or set z_0=1)
- Weight change: drops by total #nonzero cells (z_k → q^k gives q^k → q^{k-1})
- In infinite-variable QSym: automorphism (just reindexing)
- In finite variables: escapes alphabet (maps n-variable poly to (n-1)+z_0)

## Variable-count mismatch
- (q;q)_n lifts to e_1,e_2,... in infinitely many variables (or ∏(1-z_k) in QSym)
- g_tilde_n lives in only n variables z_1,...,z_n
- Product (q;q)_n · g_n makes sense in one variable (q), but multivariate lift must reconcile ∞ vs n variables
- This is why E-H factorization doesn't lift to QSym

## RPP vs CPP parallel
- RPPs: max ≤ n gives s_λ(1,q,...,q^{n-1}), exact max = n is a difference → trivially positive
- CPPs: max ≤ n gives transfer matrix (Schur positive before specialization), exact max = n needs (zq;q)_∞ extraction → positivity is Warnaar's Conjecture 2.7
- The difficulty is entirely in the extraction mechanism

## Schur positivity of Borodin's formula
- Transfer matrix: GK_c(z,q) = Σ_n z^n Σ_{chain} ∏ s_{μ^(i)/μ^(i-1)}(1,q,q^2,...)
- Before specialization, each term is a product of skew Schur functions → Schur positive by LR
- But this is Schur positivity in the "alphabet" sense (Schur expansion of s_μ(X^n)), not in the frequency sense
- The transfer matrix Schur positivity does NOT directly help with Q_n positivity

## ArXiv RAG system
- Located at ~/data/arxiv-rag/
- rag.py: PyMuPDF + ChromaDB + OpenAI text-embedding-3-small
- kg_query.py: knowledge graph queries
- build_knowledge_graph.py: builds KG from papers
- visualize_graph.py: D3.js v7 force-directed graph (self-contained HTML)
- Searched 62 papers for max-entry refinement — no prior work on frequency refinement at fixed max entry found
