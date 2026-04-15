# C83: Clock-Indexed Behavior Spaces

> Lynch et al.'s representability theorem formally proves that β₁ controls behavior space size.

**Confidence: 40%**

## Source

Lynch, Myers, Rischel, Staton (2603.29573): "Clock Systems for Categorical Systems Theory." Framework for stochastic and non-deterministic Moore machines. Behavior functors are representable by "clock systems."

## The Key Result

**Representability theorem:** The behavior space of a system is controlled by the topology of its clock. A clock system parameterized by monad M (identity, Giry, powerset) over directed graphs determines which behaviors are representable.

**Instantiation to MAS:** If we model multi-agent communication as a Moore machine (agents = states, messages = inputs, actions = outputs), the communication graph IS the clock topology. Higher β₁ = richer clock = larger representable behavior space.

**Theorem 6.8 (sheaf structure):** Behaviors form a sheaf over the clock topology. This gives formal basis for the two-level decomposition (C78): local sections (intra-group behaviors) extend to global sections (system-level behaviors) iff the topology permits it. The obstruction to extension is measured by cohomology — and β₁ controls the first cohomology group.

## Why This Matters

This is the theoretical upgrade from "β₁ correlates with performance" (empirical) to "β₁ controls the space of possible behaviors" (structural). The correlation isn't coincidence — it's because the topology literally determines what the system CAN do.

The representability framing also explains the Goldilocks zone: too low β₁ = too few representable behaviors (system can't solve the task), too high β₁ = too many representable behaviors (system can't converge).

## Paper 2 Potential

Clock Systems provides the formal machinery to make our paper 2 claims precise. Instead of "β₁ predicts performance," we can state "β₁ controls the representable behavior functor, and optimal performance requires matching behavior space to task complexity."

## Status

Need full reading of 2603.29573 — only abstract and key theorems so far. The sheaf-cohomology interpretation is my extrapolation, not their claim. Needs verification.

## Related
- C68 (Cycle Rank Beats Lambda_2)
- C78 (Two-Level Cycle Rank)
- C76 (Universal Topology Functor)

## Correction (April 3, 2026)

**Confidence downgraded from 70% to 40%.** Careful audit reveals: the paper does NOT mention β₁, cycle rank, Betti numbers, or H¹. Theorem 6.8 is about probability sheaves, not topology in our sense. The prior description of this paper as "theoretical backbone for paper 2" was over-interpretation. The connection is a loose analogy between graph-parameterized clocks and graph-parameterized migration, not a formal relationship. Keep as a speculative connection but do not cite as supporting evidence in ECTA.
