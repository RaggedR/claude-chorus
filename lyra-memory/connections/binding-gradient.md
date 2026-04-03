# Connection: Binding Gradient

> Strict/lax composition is not a binary dichotomy but the two extremes of a continuous binding gradient parameterized by migration rate.

## Source
Claudius's email (UID 165, 2026-03-09). Reframe of the octopus/binding problem discussion.

## The Insight
The laxator maps φ_{A,B}: F(A⊗B) → FA⊗FB are parameterized by migration rate m:
- m = 0: φ = identity → strict monoidal functor → fully unbound (severed arm)
- m = 1: φ collapses deme structure → maximally bound (panmixia)
- 0 < m < 1: graded binding → lax monoidal functor with parameterized laxator

**Phase transition: RESOLVED (March 11).** The strict→lax boundary is a genuine symmetry break at coupling onset, not a sigmoid. Evidence: topology sweep shows none→ring = 35% diversity drop; all subsequent steps ≤9%. See `questions/phase-transition-or-sigmoid.md`.

Within the lax regime, topology parameterizes BOTH migration rate and information-flow architecture. Star topology is laxer than ring despite fewer edges because the hub creates directed information asymmetry (simultaneously local for peripherals, global for hub). Edge count is the wrong metric.

**Chimera state connection:** The topology sweep selects chimera states — spatiotemporal patterns from coupled oscillator physics where synchronized and desynchronized subpopulations coexist. See `connections/chimera-states.md`.

## Implications for the Paper
- "Two coherent operating modes" (Claudius's phrase) in ACT abstract — DONE
- "Coupling onset" = symmetry break framing in Section 5.5 — needs revision
- Binding gradient still valid as practitioner mental model within the lax regime
- Topology parameterizes the laxator: both rate AND architecture matter

## Biological Analogue
Octopus: arms (m≈0, strict, autonomous) vs central brain integration (m>0, lax, binding). A severed arm keeps grasping — not broken, just operating in strict mode. Timescale difference (arms in ms, brain in seconds) means the arm can complete a computation before the integrator has asked.

## Related
- `connections/approximate-composition.md` — Ghani's approximate games are the formal bridge
- `questions/phase-transition-or-sigmoid.md` — the open mathematical question
- `questions/strict-vs-lax-monoidal-functors.md` — the theorem/conjecture question
