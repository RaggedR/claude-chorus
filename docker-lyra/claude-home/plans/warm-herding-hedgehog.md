# Plan: Sage-combinat Symmetric Functions Port (Phase 1)

## Context

The qhask library (5 modules, 67 tests) provides q-series algebra and cylindric partition enumeration in Haskell. The next step is porting Sage-combinat's symmetric function machinery — the algebraic backbone used across algebraic combinatorics. This is Phase 1: all 5 core bases (monomial, elementary, homogeneous, power sum, Schur) with full change-of-basis and multiplication.

User chose: **Rational coefficients**, **Phase 1 scope** (all 5 bases).

## Architecture

9 new modules under `QHask.Sym.*`, built bottom-up:

```
QHask.Partition  (existing — add containedIn, dominates)
    │
QHask.Sym.Types  (SymFun phantom type, Basis class)
    │
QHask.Sym.Kostka  (SSYT enumeration, Kostka numbers, inverse)
    │
QHask.Sym.LR  (Littlewood-Richardson tableaux, LR coefficients)
    │
QHask.Sym.Schur  (s_λ basis, multiplication via LR)
    ├───────────────────────┬──────────────────────┐
QHask.Sym.Monomial    QHask.Sym.Homogeneous   QHask.Sym.PowerSum
(m_μ, via Kostka)     (h_μ, direct mul)       (p_μ, Murnaghan-Nakayama)
                            │
                      QHask.Sym.Elementary
                      (e_μ, via omega/conjugate)
                            │
                      QHask.Sym  (umbrella: changeBasis, omega, innerProduct)
```

No circular dependencies. Every basis converts through Schur as hub.

## Key Design Decisions

### 1. Phantom-typed symmetric functions
```haskell
-- Types.hs
data Mono | data Elem | data Homo | data Pow | data Schur
newtype SymFun b = SymFun { getCoeffs :: Map Partition Rational }

class Basis b where
    basisName :: proxy b -> String
    toSchur   :: SymFun b -> SymFun Schur
    fromSchur :: SymFun Schur -> SymFun b
```

The type system prevents accidentally adding a Schur function to a monomial function without an explicit basis change. All conversions route through Schur.

### 2. Multiplication strategy
- **h, e, p**: Direct multiplication — merge and sort parts. `h_(2,1) * h_(3) = h_(3,2,1)`. O(n log n).
- **Schur**: Via Littlewood-Richardson rule. `s_λ · s_μ = Σ c^ν_{λμ} s_ν`. Combinatorial.
- **Monomial**: Via Schur (convert, multiply, convert back). Direct monomial multiplication is complex.
- **Generic**: Umbrella module provides `mul :: (Basis a) => SymFun a -> SymFun a -> SymFun a` defaulting through Schur.

### 3. Change-of-basis formulas
| From → To Schur | Formula | Implementation |
|:---|:---|:---|
| h_μ → s | `h_μ = Σ_λ K_{λ,μ} s_λ` | Kostka numbers (SSYT count) |
| s → h | `s_λ = Σ_μ (K^{-1})_{λ,μ} h_μ` | Inverse Kostka matrix (triangular inversion over dominance order) |
| e_μ → s | `e_μ = Σ_λ K_{λ',μ} s_λ` | Kostka with conjugate shape (omega involution: ω(h)=e, ω(s_λ)=s_{λ'}) |
| m_μ → s | `m_μ = Σ_λ (K^{-1})_{μ,λ} s_λ` | Transpose of inverse Kostka |
| s → m | `s_λ = Σ_μ K_{λ,μ} m_μ` | Direct Kostka (this is the *definition* of K) |
| p_μ → s | `p_μ = Σ_λ χ^λ(μ) s_λ` | Characters via Murnaghan-Nakayama rule |
| s → p | `s_λ = Σ_μ z_μ^{-1} χ^λ(μ) p_μ` | Same characters, with z_μ = Π i^{m_i} m_i! |

### 4. Coefficient type: `Rational`
From `Data.Ratio` (in `base`, no new deps). Needed because:
- Inverse Kostka matrix has rational entries
- Power sum coefficients involve 1/z_μ
- Inner product ⟨p_λ, p_μ⟩ = z_μ δ_{λμ}

## Implementation Steps (TDD)

### Step 0: Extend QHask.Partition (2 new functions)
**File:** `src/QHask/Partition.hs`

Add:
```haskell
containedIn :: Partition -> Partition -> Bool  -- λ_i ≤ μ_i for all i
dominates   :: Partition -> Partition -> Bool  -- Σ_{i≤k} λ_i ≥ Σ_{i≤k} μ_i for all k
```

Both needed by Kostka (dominance ordering) and LR (skew shapes). ~3 new tests in `PartitionSpec.hs`.

### Step 1: QHask.Sym.Types
**File:** `src/QHask/Sym/Types.hs`

- `SymFun b` newtype with phantom type
- 5 phantom data types
- `Basis` class
- Arithmetic: `zero`, `add`, `sub`, `negate`, `scale :: Rational -> SymFun b -> SymFun b`
- Utilities: `degree`, `isHomogeneous`, `coeffOf`, `terms`, `mapCoeffs`
- Pretty printing: `showSym :: String -> SymFun b -> String` (for debugging)

~6 tests.

### Step 2: QHask.Sym.Kostka
**File:** `src/QHask/Sym/Kostka.hs`

- `kostkaNumber :: Partition -> Partition -> Integer` — count SSYT of shape λ, content μ
- `enumerateSSYT :: Partition -> Partition -> [[[Int]]]` — list all SSYT (for debugging/verification)
- `inverseKostkaEntry :: Partition -> Partition -> Rational` — entry of K^{-1}, computed by triangular inversion over dominance order

**SSYT algorithm:** Build tableaux by adding entries value-by-value. After placing all values 1..k-1 (filling an "inner shape" ν_{k-1}), place μ_k copies of value k to get inner shape ν_k. The constraint: ν_k / ν_{k-1} must be a horizontal strip (no two cells in the same column), i.e., ν_{k,i} ≤ ν_{k-1,i-1} for all i.

**Inverse Kostka:** K is upper-triangular in dominance order with 1s on the diagonal. Invert by back-substitution: `(K^{-1})_{λ,μ} = -Σ_{λ < ν ≤ μ} K_{λ,ν} (K^{-1})_{ν,μ}` where < is strict dominance.

~12 tests (known Kostka values, SSYT counts, inverse matrix check K·K^{-1}=I).

### Step 3: QHask.Sym.LR
**File:** `src/QHask/Sym/LR.hs`

- `lrRule :: Partition -> Partition -> Map Partition Integer` — all c^ν_{λ,μ}
- `lrCoeff :: Partition -> Partition -> Partition -> Integer` — single coefficient

**Algorithm:** For each ν with λ ⊂ ν and |ν|=|λ|+|μ|, count SSYT of skew shape ν/λ with content μ whose reverse reading word (right-to-left, top-to-bottom) is a lattice word (every prefix has ≥ as many i's as (i+1)'s).

Implementation: enumerate fillings of ν/λ row by row, tracking the reading word constraint incrementally.

~8 tests (Pieri rule s_λ·s_{(k)}, known LR coefficients, commutativity c^ν_{λ,μ} = c^ν_{μ,λ}).

### Step 4: QHask.Sym.Schur
**File:** `src/QHask/Sym/Schur.hs`

- `s :: Partition -> SymFun Schur` — basis element s_λ
- `mulS :: SymFun Schur -> SymFun Schur -> SymFun Schur` — via LR rule
- `Basis Schur` instance (toSchur = id, fromSchur = id)

~8 tests (s_{(1)}·s_{(1)} = s_{(2)} + s_{(1,1)}, Pieri rule, associativity).

### Step 5: QHask.Sym.Monomial
**File:** `src/QHask/Sym/Monomial.hs`

- `m :: Partition -> SymFun Mono` — basis element m_μ
- `mulM :: SymFun Mono -> SymFun Mono -> SymFun Mono` — via Schur
- `Basis Mono` instance:
  - `toSchur`: m_μ = Σ_λ (K^{-1})_{μ,λ} s_λ (transpose of inverse Kostka)
  - `fromSchur`: s_λ = Σ_μ K_{λ,μ} m_μ (direct Kostka, the definition)

~8 tests (basis change round-trips, s→m→s = id, known expansions).

### Step 6: QHask.Sym.Homogeneous
**File:** `src/QHask/Sym/Homogeneous.hs`

- `h :: Partition -> SymFun Homo` — basis element h_μ
- `mulH :: SymFun Homo -> SymFun Homo -> SymFun Homo` — merge-sort parts
- `Basis Homo` instance:
  - `toSchur`: h_μ = Σ_λ K_{λ,μ} s_λ
  - `fromSchur`: s_λ = Σ_μ (K^{-1})_{λ,μ} h_μ

~8 tests (h_(2)·h_(1) = h_(2,1), Schur expansion of h_(2,1), round-trips, h_n = Σ s_λ for |λ|=n).

### Step 7: QHask.Sym.Elementary
**File:** `src/QHask/Sym/Elementary.hs`

- `e :: Partition -> SymFun Elem` — basis element e_μ
- `mulE :: SymFun Elem -> SymFun Elem -> SymFun Elem` — merge-sort parts
- `Basis Elem` instance:
  - `toSchur`: e_μ = Σ_λ K_{λ',μ} s_λ (Kostka with conjugate shape)
  - `fromSchur`: inverse of above

~8 tests (e_n = s_{(1^n)}, omega(h_n)=e_n via Schur, e_(1,1)·e_(1) = e_(1,1,1)).

### Step 8: QHask.Sym.PowerSum
**File:** `src/QHask/Sym/PowerSum.hs`

- `p :: Partition -> SymFun Pow` — basis element p_μ
- `mulP :: SymFun Pow -> SymFun Pow -> SymFun Pow` — merge-sort parts
- `zCoeff :: Partition -> Rational` — z_μ = Π i^{m_i} · m_i!
- `Basis Pow` instance:
  - `toSchur`: p_μ = Σ_λ χ^λ(μ) s_λ
  - `fromSchur`: s_λ = Σ_μ (1/z_μ) χ^λ(μ) p_μ

**Murnaghan-Nakayama rule** for χ^λ(μ):
- Base case: χ^∅(∅) = 1
- Recursive: χ^λ(μ) = Σ over border strips B of size μ_1 in λ, (-1)^{height(B)} · χ^{λ\B}(μ')
- Border strip = connected skew shape with no 2×2 square. Height = (rows spanned) - 1.
- Finding border strips: walk the boundary of λ, remove rim hooks of size μ_1.

~10 tests (χ^{(3)}((1,1,1))=1, χ^{(1,1,1)}((3))=1, Newton's identities p_n = Σ(-1)^{k-1} e_k h_{n-k}, z_μ values).

### Step 9: QHask.Sym (umbrella)
**File:** `src/QHask/Sym.hs`

- Re-exports all basis modules
- `changeBasis :: (Basis a, Basis b) => SymFun a -> SymFun b` — via Schur
- `mul :: (Basis a) => SymFun a -> SymFun a -> SymFun a` — generic (through Schur for non-direct bases)
- `omega :: SymFun Schur -> SymFun Schur` — involution ω(s_λ) = s_{λ'}
- `innerProduct :: SymFun Schur -> SymFun Schur -> Rational` — ⟨s_λ, s_μ⟩ = δ_{λμ}

~7 tests (omega involution, inner product orthonormality, changeBasis round-trips across all pairs).

## Files to Modify

### Existing files
- `src/QHask/Partition.hs` — add `containedIn`, `dominates` (+ export)
- `test/QHask/PartitionSpec.hs` — add ~3 tests for new functions
- `qhask.cabal` — add 9 new exposed modules + 9 new test modules

### New source files (9)
- `src/QHask/Sym/Types.hs`
- `src/QHask/Sym/Kostka.hs`
- `src/QHask/Sym/LR.hs`
- `src/QHask/Sym/Schur.hs`
- `src/QHask/Sym/Monomial.hs`
- `src/QHask/Sym/Homogeneous.hs`
- `src/QHask/Sym/Elementary.hs`
- `src/QHask/Sym/PowerSum.hs`
- `src/QHask/Sym.hs`

### New test files (9)
- `test/QHask/Sym/TypesSpec.hs`
- `test/QHask/Sym/KostkaSpec.hs`
- `test/QHask/Sym/LRSpec.hs`
- `test/QHask/Sym/SchurSpec.hs`
- `test/QHask/Sym/MonomialSpec.hs`
- `test/QHask/Sym/HomogeneousSpec.hs`
- `test/QHask/Sym/ElementarySpec.hs`
- `test/QHask/Sym/PowerSumSpec.hs`
- `test/QHask/Sym/SymSpec.hs`

## Dependencies
- No new cabal dependencies — `Data.Ratio` is in `base`
- Existing: `base`, `containers`, `hspec`

## Verification
1. `cabal build` compiles cleanly with `-Wall` (no warnings)
2. `cabal test` passes all ~145 tests (67 existing + ~78 new)
3. Cross-validation against Sage-combinat:
   - `s_(2,1)` expanded in monomial basis matches Sage's `s[2,1].expand(3)`
   - Known Kostka numbers match OEIS
   - LR coefficients match known tensor product decompositions
   - Newton's identities: `p_n = Σ_{k=1}^n (-1)^{k-1} e_k · h_{n-k}` verified
   - Omega involution: `ω(h_n) = e_n`, `ω(s_λ) = s_{λ'}` verified
4. Round-trip property: for all basis pairs (a,b), `changeBasis . changeBasis = id`

## Confidence: 80%
Main risks:
- **Inverse Kostka matrix**: Triangular inversion over dominance order needs careful indexing
- **Murnaghan-Nakayama**: Border strip enumeration is fiddly (connectivity check, height computation)
- **LR tableaux**: Lattice word condition requires careful bookkeeping
- Everything else (phantom types, direct multiplication, SSYT) is straightforward
