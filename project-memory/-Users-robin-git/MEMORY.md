# Memory

## Research Repository (~/git/research)
- Focuses on Warnaar's Conjecture 2.7 (positivity of Q_{n,c}(q) for rank-3 cylindric partitions)
- **Directory structure**: `scripts/` (Python), `tex/` (LaTeX + PDF), `pdf/` (reference papers), root has CLAUDE.md only
- **Run Python from scripts/**: `cd scripts && mamba run -n sage python3 compute_gk.py`
- **Compile LaTeX from tex/**: `cd tex && pdflatex notes_weighted_local_rules.tex`
- **SageMath 10.7 is a HARD DEPENDENCY** for all scripts: `mamba run -n sage python3 script.py`
- Sage provides PowerSeriesRing(ZZ,'q'), q-binomials, polynomial arithmetic (replaced fractions.Fraction)
- Enumeration loop is pure Python int (fast); algebra uses Sage (clean). Boundary: `gk_dict_to_poly()`
- Key files: `scripts/compute_gk.py`, `scripts/verify_conjecture.py`, `scripts/analyze_Q.py`, `scripts/investigate_involution.py`, `tex/notes_weighted_local_rules.tex`
- **Shared library**: `scripts/cpp_lib/` package (7 modules + __init__.py):
  - `partitions.py` — get_part, gen_partitions, gen_compatible, conjugate, partitions_of
  - `enumeration.py` — compute_gk, enumerate_cpps_with_max, extract_z_coefficient (pure Python)
  - `qseries.py` — compute_Q, compute_h_m, qbinomial, borodin_product (Sage-powered)
  - `qsym.py` — compositions_of, refines, coarsens, M_to_L, M_to_L_bounded
  - `ground_set.py` — frequency_vector, enumerate_all_triples
  - `profiles.py` — profile_to_mu, all_profiles
  - `cli.py` — parse_args
- 12 scripts total (down from 50 after cleanup), all import from cpp_lib
- Multipartition enumeration validated against Borodin product formula
- Conjecture verified for d=1,2,4,5,7 (all tested profiles pass, 10 profiles total)
- Key finding: d=2 gives Q = monomial (q^{n^2} or q^{n(n+1)}), matching AG quadratic forms
- d=7 profiles tested: (3,2,2), (2,3,2), (4,2,1) — all pass for n=1
- Reversal symmetry GK_{(c0,c1,c2)} = GK_{(c2,c1,c0)} does NOT hold in general (fails for (2,1,0))
- Soft positivity disproved: f(z,q)=1+zq counterexample shows cylindric structure is essential
- Q_{n,c}(q) does NOT decompose as nonneg sum of Kostka-Foulkes polynomials
- Kostka-Foulkes comparison and charge statistic analysis in analyze_Q.py

## Cyclic descent injection (KEY RESULT)
- For d not divisible by 3: the CYCLIC DESCENT RULE gives a valid injection from weight-(w-1) to weight-w max-1 CPPs
- Rule: given slack s=(s1,s2,s3), increment l_k where k has s_k > s_{k-1 mod 3} with smallest predecessor
- Formally: k = argmin{s_{(k-2) mod 3} : k ∈ CycDes(s)}, ties broken by smallest k
- Verified for ALL profiles with d=1,2,4,5,7,8 (126 profiles total)
- Fixed points at w≥2 match h_1(q) coefficients exactly
- For d≡0 mod 3: rule fails because balanced slack (d/3,d/3,d/3) has no cyclic descent
- d=3 triple count oscillates (3,3,4,3,3,4,...) making injection impossible
- Key files: scripts/test_cyclic_rule.py, scripts/analyze_matching.py, scripts/test_d3_fix.py
- LaTeX: Section 8 of tex/notes_weighted_local_rules.tex (now 22 pages)

## Quasi-symmetric frequency generating function (KEY DISCOVERY)
- GK_tilde = sum_{CPP} z_1^{#1} z_2^{#2} ... (#k = parts equal to k) is QUASI-SYMMETRIC
- Verified for ALL 55 profiles with d=1..5, zero failures
- NOT symmetric (M_{(2,1)} coeff ≠ M_{(1,2)} coeff)
- Reason: interlacing depends on relative order of values, not absolute values
- Stabilized coefficients: c=(1,1,0) gives 2^ℓ, c=(2,1,1) gives 5^ℓ
- Specialization z_k → q^k recovers GK_c(1,q)
- L-POSITIVITY: expansion in Gessel's fundamental basis L_alpha also has nonneg coefficients (55 profiles, 0 failures)
- L-positivity is strictly stronger than M-positivity (involves Möbius inversion, nontrivial cancellation)
- L-positivity implies a descent-type statistic on CPPs should exist
- E-H factorization does NOT lift to QSym (both with and without max-entry variable give negatives)
- Written up in tex/QUASI_SYMMETRIC.tex (now ~14 pages, includes 0-Hecke remark and partial QSym)
- QSym is a Λ-module — the right algebraic framework
- 0-Hecke connection: L-positivity ↔ being quasi-symmetric characteristic of an H_n(0)-module (Tewari-van Willigenburg)

## Partial quasi-symmetry and max-entry refinement (KEY RESULTS)
- g_tilde_n (CPPs with max = n) lives in z_n · QSym(z_1,...,z_{n-1})[z_n]
- Each z_n^m slice is quasi-symmetric in z_1,...,z_{n-1} — verified 55/55 profiles, n=1..3
- Script: scripts/verify_partial_qsym.py (uses M_to_L_bounded for finite-variable QSym)
- Bug lesson: M_to_L from cpp_library.py is infinite-variable; need M_to_L_bounded(M_coeffs, max_len) for finite variables
- Slice L-positivity FAILS at n≥3: structural issue, M_(k) > M_(j,k) forces L_(a,b) < 0
- Variable-count mismatch: (q;q)_n lifts to e_j in infinitely many variables, but g_tilde_n lives in only n variables — structural obstacle to multivariate Q_n lift
- RPP parallel: max ≤ n RPPs counted by s_λ(1,q,...,q^{n-1}); exact max = n is just a difference (trivially positive). CPPs need (zq;q)_∞ extraction — that's where positivity is hard
- Crush operator on frequency GF: z_k → z_{k-1} (shift index down by 1). Automorphism of QSym in infinite variables, but escapes finite alphabet (z_1 → z_0)
- Gansner's trace GF ≠ our frequency GF: Gansner tracks diagonal sums (x_d per diagonal), we track value counts (z_k per value). Gansner has hook-product formula but can't see max entry
- LaTeX: tex/MAX_PART.tex (13 pages) — comprehensive survey of max-entry refinement for RPPs and CPPs
- See [max_entry_details.md](max_entry_details.md) for full details

## Omega involution investigation (investigate_involution.py)
- E-H factorization: GK_c = H(z) · F_c where H=1/(zq;q)_∞, F_c=(zq;q)_∞·GK_c
- Rogers-Ramanujan confirmed for d=2: Q_m = q^{m²} (first RR), Q_m = q^{m(m+1)} (second RR)
- KEY FINDING: h_m = (q)_m · g_m are nonneg polynomials for all tested profiles (d=1,2,4,5)
- q-binomial decomposition: Q_n = Σ (-1)^j q^{j(j+1)/2} [n choose j]_q h_{n-j} — verified
- q-binomial INVERSE: h_m = Σ q^j [m,j]_q Q_{m-j} (NOT q^{j²} — bug was in definitions.tex, now fixed)
- H_m = [z^m] 1/(zq;q)_∞ = q^m/(q)_m gives the correct inverse
- GK ≠ GK^omega (max-first-part ≠ max-length), but z=1 totals agree
- Notes expanded to 14 pages with Section 6 on omega involution

## U-toggle involution and (S,U,ν) analysis
- U-toggle involution pairs (S,U,ν) with (S, U△{k}, ν') — handles 94-97% of all triples
- Two-level structure: Level 1 (U-toggle = (q)_m factor), Level 2 (S-alternation = q-binomial sum)
- Cross-cancellation between different QSym monomials: only 0-0.3% of total (verified 7 cases)
- QSym Q_n^{QSym} = Σ (-1)^{|S|+|U|} M_{freq} is NOT L-positive (different from GK_tilde which IS)
- Key files: scripts/internal_involution.py, scripts/analyze_qsym_cancellation.py, scripts/qsym_Q_polynomial.py, scripts/fixed_point_structure.py

## Multivariate and operator dead ends
- Per-part multivariate Q_n (q^k → q_k): positivity FAILS for n≥2 (negative integer coefficients)
- Crush operator on CPPs: preserves profile, moves φ(k) boxes (variable per CPP), doesn't preserve weight
- Crush on frequency GF is clean: just z_k → z_{k-1} (value shift). Weight drops by #nonzero cells
- Combinatorial involution approach: dead end — profile-preserving ops move variable #boxes, involutions need weight preservation
- Korff-Palazzo h-positivity: different "h" from ours, wrong direction (h≥0 is easy, Q≥0 is hard)
- tex/LITERATURE_NOTES.tex tracks literature connections

## Communication preferences
- When uncertain between two approaches, present both with trade-offs rather than picking one silently
- Don't ask for confirmation on routine file edits — just do them
- If a task will take more than ~5 files of changes, enter plan mode first

## Frontend UI — CRITICAL lessons
- User has repeatedly had broken button/interaction bugs across projects (checkers, russian, mastermind)
- ROOT CAUSE: Claude writes frontend code but never verifies the full round-trip (button → handler → fetch → API → response → state update → re-render)
- After writing ANY frontend interactive element, ALWAYS trace the complete chain before finishing:
  1. Does the button/element have an event handler attached?
  2. Does the handler call the right endpoint with the right method/body?
  3. Does the backend endpoint exist and accept that method?
  4. Is the response parsed and does it update the UI state?
  5. Does the component re-render with the new state?
- Ask the user for screenshots when debugging visual issues — can read images
- Don't just test the code you wrote in isolation; verify it integrates with the existing frontend

## Thesis source
- Located at `~/git/thesis/phD/phD-files/`
- Key chapters: chap1.tex (Burge local rule), chap1a.tex (CPP defs), chap3.tex (growth diagrams)

## Performance notes
- GK enumeration: d=4 with max_w=39 takes ~28s (2.9M partitions); d=5 with max_w=26 takes ~0.7s (213K)
- d=7 with max_w=24 takes ~0.2s (94K partitions)
- For verify_conjecture: max_w must be >= degree of Q_{n,c}; deg(Q_{n,c}) ~ n^2 * d/3
- d=4, n=3 needs max_w>=30 (deg~27); d=7, n=2 needs max_w>=30
- Truncation safe range: enumeration exact for q^w with w <= max_n (max entry bound)
- Use --fast flag for quick validation, omit for full verification
