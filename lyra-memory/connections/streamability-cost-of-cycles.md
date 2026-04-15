# C99: Streamability = Categorical Cost of Cycles

**Confidence: 80%**
**Source:** Abbott et al. (2505.09326) — "Accelerating ML via Category Theory"
**Connected to:** C84 (confound theorem), C93 (NK amplification), C74 (DAG constraint)

## The Connection

Abbott et al. prove a generalized streamability theorem using monoidal string diagrams: DAGs are streamable (can be evaluated in a single forward pass), while cycles require fixpoint iteration (potentially non-terminating).

This gives the first formal COST MODEL for cycles in agent topology:
- **DAG cost:** Linear. One pass. Predictable latency.
- **Cycle cost:** Fixpoint iteration. Unknown convergence. Potentially unbounded.

Our experiments provide the BENEFIT MODEL:
- **DAG benefit:** Low diversity maintenance → fine for smooth landscapes (K=0).
- **Cycle benefit:** High diversity maintenance (η²=0.69 at K=6) → essential for rugged landscapes.

## The Complete Framework

Together: **choose cycles when benefit > cost**, which is landscape-dependent.

| Landscape | Cycle Benefit | Cycle Cost | Optimal |
|-----------|--------------|------------|---------|
| Smooth (K=0) | ~0 (η²=0.05) | Fixpoint iteration | DAG |
| Moderate (K=4) | Medium (η²=0.45) | Fixpoint iteration | Depends |
| Rugged (K=6) | High (η²=0.69) | Fixpoint iteration | Cycles |

The NK dose-response curve IS the cost-benefit tradeoff curve.

## Implications

1. DAG hegemony is rational for EASY problems — practitioners aren't wrong, they're incomplete.
2. The streamability theorem explains WHY the learned prior is acyclic: optimization favors predictable cost.
3. Our contribution is showing the benefit side is non-trivial and landscape-dependent.
4. ECTA should cite this as the cost complement to our benefit results.
