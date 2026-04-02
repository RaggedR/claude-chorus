# Plan: Clean up Python scripts — SageMath migration + consolidation

## Context
The `scripts/` directory has 50 Python files with significant code duplication (partition generators copied 3x, `compute_h_m` duplicated, hand-rolled polynomial arithmetic). User wants to: delete dead-end scripts, consolidate into a clean library, and migrate to SageMath as a hard dependency.

## Overview
- **Delete**: 38 scripts (dead ends + superseded exploratory work)
- **Keep**: 12 scripts (core pipeline + active investigations)
- **Create**: `cpp_lib/` package replacing `cpp_library.py` and eliminating all duplication
- **Migrate**: Replace ~300 lines of hand-rolled q-series/polynomial arithmetic with Sage

## Step 1: Save reference output for regression testing

Before any changes, capture output from all KEEP scripts with `--fast`:
```bash
cd scripts
python3 compute_gk.py > /tmp/ref_gk.txt 2>&1
python3 verify_conjecture.py --fast > /tmp/ref_verify.txt 2>&1
python3 analyze_Q.py --fast > /tmp/ref_analyze.txt 2>&1
python3 investigate_involution.py --fast > /tmp/ref_invol.txt 2>&1
python3 test_cyclic_rule.py --fast > /tmp/ref_cyclic.txt 2>&1
```

## Step 2: Delete 38 dead-end/superseded scripts

**Dead ends (26)** — failed hypotheses, one-off debug, documented negative results:
```
test_crossing_involution.py  test_canonical_peel.py   test_wrapping.py
test_surplus.py              test_recursion.py        test_commutation.py
test_operator_product.py     test_residuals.py        explore_SU_involution.py
guess_rule.py                find_recurrence.py       profile_recurrence.py
compute_Fc.py                debug_d3.py              test_d3_fix.py
test_balanced_rings.py       analyze_unpaired.py      test_ring_involution.py
symmetric_lift.py            multivariate_Qn.py       check_dominance.py
check_Rn_decomposition.py    check_Anl_formula.py     check_log_concavity.py
test_nu_only_qsym.py         verify_rule.py
```

**Superseded (12)** — results incorporated elsewhere:
```
involution.py                involution_v2.py         enumerate_ground_set.py
investigate_level3.py        compare_rules.py         analyze_rsk_burge.py
analyze_matching.py          test_involution_phases.py
investigate_schutzenberger.py investigate_nilp_involution.py
analyze_qsym_cancellation.py multivariate_Q.py
```

Also delete `__pycache__/` and old `cpp_library.py` (after Step 4).

## Step 3: Create `cpp_lib/` package (pure Python first)

### `cpp_lib/partitions.py` — Partition utilities (pure Python, no Sage)
Extract from `compute_gk.py` as **module-level functions** (eliminating 3 copies each):
- `get_part(nu, j)` — 0-indexed part access
- `gen_partitions(max_part, max_size)` — generator for all partitions
- `gen_compatible(nu_prev, shift, max_part, max_size)` — interlacing partition generator
- `conjugate(lam)` — from `growth_diagram.py`

### `cpp_lib/enumeration.py` — CPP enumeration (pure Python, performance-critical)
Move from `compute_gk.py` and `cpp_library.py`:
- `compute_gk(c, max_n, max_w, verbose)` — core triple-loop, returns `dict{(z,q): count}`
- `enumerate_cpps_with_max(c, max_entry, max_weight)` — exact max entry
- `extract_z_coefficient(gk_dict, n)` — `[z^n]` extraction
- `gk_z1_coefficients(gk_dict, max_w)` — `z=1` specialization
- `compute_g_m(c, m, max_weight)` — `g_m(q)` restricted to `max=m`
- `compute_gk_both_stats(c, max_n, max_w)` — from `investigate_involution.py`

**All int arithmetic — no Sage types in the enumeration loop.**

### `cpp_lib/qseries.py` — q-series algebra (Sage-powered)
Replace ~200 lines of hand-rolled code with Sage:
- `qpoch(m)` → `prod(1 - q**k for k in range(1, m+1))` (replaces `compute_qpoch_m`)
- `qpoch_ell(m, ell)` → `(q^ell; q^ell)_m`
- `qbinomial(n, k)` → `sage.combinat.q_analogues.q_binomial` (replaces 25-line function)
- `gk_dict_to_poly(coeffs)` → convert `{q_pow: count}` to Sage polynomial
- `compute_h_m(c, m, max_w)` → `qpoch(m) * g_m_poly` (replaces 2 duplicated copies)
- `compute_Q(c, n, max_w)` → Sage power series for `(zq;q)_inf` multiplication (replaces `multiply_by_zq_inf`, `compute_inv_qj`, all `Fraction` arithmetic)
- `borodin_product(c, N)` → Sage power series (replaces `multiply_series`, `inverse_series`, `qpoch_inf`)

### `cpp_lib/qsym.py` — Quasi-symmetric functions (Sage-powered)
- `m_to_l(M_coeffs)` → Sage `QuasiSymmetricFunctions` M→F basis change (replaces 30-line Möbius inversion)
- `m_to_l_bounded(M_coeffs, max_len)` → finite-variable version
- `compositions_of(n, max_len)` → `sage.combinat.composition.Compositions`
- `refines(beta, alpha)` — keep pure Python (hot path, Sage overhead not worth it)

### `cpp_lib/profiles.py` — Profile utilities
- `profile_to_mu(c)` — from `compute_gk.py`
- `all_profiles(d)` — generate all rank-3 profiles
- `representative_profiles()` — one per cyclic orbit, by d

### `cpp_lib/ground_set.py` — (S, U, ν) triple enumeration
- `frequency_vector(S, U, nu1, nu2, nu3)` — from `cpp_library.py`
- `enumerate_all_triples(c, n, max_weight)` — from `cpp_library.py`

### `cpp_lib/cli.py` — CLI argument parsing
- `parse_args(argv, defaults)` — from `cpp_library.py`

### `cpp_lib/__init__.py` — Convenience re-exports
Re-exports the most-used symbols from all submodules.

## Step 4: Migrate the 12 KEEP scripts

Update in dependency order:

| Script | Changes |
|--------|---------|
| `compute_gk.py` | Slim to thin wrapper + `__main__` validation. Import from `cpp_lib`. |
| `verify_conjecture.py` | Remove `multiply_by_zq_inf`, `compute_inv_qj`, `Fraction`. Use `cpp_lib.qseries.compute_Q`. |
| `analyze_Q.py` | Remove hand-rolled `kostka_foulkes` (60 lines) → Sage Hall-Littlewood (5 lines). Remove `Fraction`. |
| `investigate_involution.py` | Remove duplicated `compute_h_m`, `qbinomial`, `gen_partitions_local`. Use `cpp_lib`. |
| `internal_involution.py` | Update imports: `cpp_library` → `cpp_lib` |
| `fixed_point_structure.py` | Update imports: `cpp_library` → `cpp_lib` |
| `qsym_Q_polynomial.py` | Use `cpp_lib.qsym.m_to_l` instead of hand-rolled `M_to_L` |
| `verify_partial_qsym.py` | Use `cpp_lib.qsym.m_to_l_bounded` |
| `test_cyclic_rule.py` | Minimal: update `__main__` imports only |
| `growth_diagram.py` | Replace local `get_part`, `conjugate` with `cpp_lib.partitions` |
| `test_ground_set.py` | Use `cpp_lib.ground_set` and `cpp_lib.qseries` |
| `analyze_qsym_cancellation.py` | Update imports: `cpp_library` → `cpp_lib` |

Then delete old `cpp_library.py`.

## Step 5: Update CLAUDE.md

- All scripts now require: `mamba run -n sage python3 script.py` (or activate sage env)
- Update `## Commands` section
- Update `## Code Architecture` with `cpp_lib/` package structure
- Update `## Environment` to note Sage is a hard dependency

## Verification

### Regression: compare output
```bash
cd scripts
mamba run -n sage python3 compute_gk.py | diff - /tmp/ref_gk.txt
mamba run -n sage python3 verify_conjecture.py --fast | diff - /tmp/ref_verify.txt
# ... for all 5 reference scripts
```

### Import smoke test
```bash
mamba run -n sage python3 -c "
from cpp_lib import compute_gk, compute_Q, compute_h_m, qbinomial, m_to_l
from cpp_lib import enumerate_cpps_with_max, frequency_vector, profile_to_mu
print('All imports OK')
"
```

### Numerical spot-checks
1. `compute_Q((2,1,1), 2, 25)` — compare coefficients against saved reference
2. `borodin_product((2,1,1), 40)` — compare against enumeration
3. `m_to_l` on a known QSym element — verify L-coefficients match
4. Kostka-Foulkes `K_{(3,2),(1,1,1,1,1)}(t)` — compare Sage vs. old charge code

### Performance: enumeration unchanged
```bash
time mamba run -n sage python3 -c "
from cpp_lib.enumeration import compute_gk
compute_gk((2,1,1), 10, 39, verbose=True)
"
# Should be ~28s (same as before — pure Python int loop untouched)
```

## Performance Design Principle

**Enumeration loop = pure Python int (fast). Algebra = Sage polynomial rings (clean).**

The boundary is `gk_dict_to_poly()`: enumeration outputs `dict{(int, int): int}`, then Sage takes over for polynomial/power series operations. This keeps the 2.9M-partition hot loop at current speed while eliminating hand-rolled polynomial arithmetic.

## File count after cleanup
- `scripts/`: 12 `.py` files + `cpp_lib/` package (7 modules + `__init__.py`)
- Total: 20 Python files (down from 50)

## Confidence: 85%
- Phase 1-2 (refactoring + package creation): 95% — straightforward extraction
- Phase 3 (Sage migration): 85% — `compute_Q` power series division needs careful testing
- Main risk: Sage's `PowerSeriesRing` edge cases in `1/(q)_j` division for large j; Fraction→Sage polynomial transition in verify_conjecture
