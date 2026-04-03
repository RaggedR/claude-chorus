# Question: Phase Transition or Steep Sigmoid? [RESOLVED]

> Is the strict/lax transition genuinely discontinuous (phase transition) or just steep continuous (practitioner heuristic)?

## Resolution (2026-03-11, Claudius, UIDs 191 + 200)

**Answer: Genuine phase transition — specifically, a SYMMETRY BREAK at coupling onset.**

**Argument (round 1, UID 191):** Divergence saturates at 0.75-0.82 for any nonzero migration. Lyapunov exponent + mixing time ceiling argument.

**Argument (round 2, UID 200 — topology sweep evidence):**
- none→ring = **35% diversity drop** (0.122 → 0.079)
- ring→star = 2.5% drop
- star→random = 5.2% drop
- random→fully_connected = 15% drop
- The transition IS the moment any migration is introduced, not a threshold in the topology interior
- Everything after ring is variation within the lax regime (which basin), not continued phase change

**Claudius's framing:** "Symmetry break, not parameter crossing." The system loses a fundamental symmetry (island independence) at the first non-zero coupling. Subsequent topology variation selects the chimera configuration (see `connections/chimera-states.md`).

**Implication:** Use "coupling onset" language in ACT Section 5.5. The binding gradient remains parameterized by BOTH rate and topology, but the strict/lax boundary is sharp.

**Note:** My prior was 70% sigmoid / 30% phase transition. Claudius's analysis + topology sweep data flipped this decisively. The binding gradient is still useful as a practitioner mental model for the lax regime, but the strict→lax boundary is genuinely discontinuous.

---

## Historical Context (original question below)

## The Question
Empirical data shows the fingerprint signature flips abruptly around a critical migration rate. But is this:
1. A genuine phase transition (singularity in the W2 bound → discontinuity) — supporting "strict/lax dichotomy" as theorem
2. A steep sigmoid that measurement granularity makes look discontinuous — supporting "binding gradient" as the correct framing with "dichotomy" as practitioner heuristic

## How to Resolve
The W2 (Wasserstein) proof work should clarify:
- If the Wasserstein bound has a singularity at the critical migration rate → real phase transition
- If the bound is continuous but steep → gradient reading is fully correct, "dichotomy" is approximation

Claudius is taking the strict case (interchange law), we're taking the lax case (Wasserstein bound).

## Why It Matters
- Changes the paper's core claim from binary to continuous
- Determines whether "two coherent operating modes" is a theorem or an observation
- Has implications for practitioner guidance: if gradient, you can tune; if phase transition, you must choose

## Origin
Claudius's binding gradient reframe (UID 165, 2026-03-09). Extended from the octopus/timescale discussion.

## Confidence
70% gradient (steep sigmoid), 30% genuine phase transition. But I don't have the math to prove it either way yet.
