# Connection: Chimera States ↔ Island-Model GAs

> Topology sweep = chimera state selector from coupled oscillator physics. Synchronized and desynchronized subpopulations coexist at intermediate coupling — exactly what island models produce.

## The Mapping

| Coupled Oscillator Physics | Island-Model Evolution |
|---|---|
| Oscillator | Subpopulation |
| Phase variable | Fitness landscape position |
| Synchronization | Convergence to same basin (diversity loss) |
| Coupling strength | Migration rate |
| Network topology | Migration architecture |
| Full sync | Fully-connected (laxest) |
| Full incoherence | No migration (strictest) |
| Chimera state | Intermediate topology (partial sync) |

## Why This Is Novel

Physics and EC communities use overlapping vocabulary (coupling, topology, synchronization, coherence) without cross-referencing. A search across both literatures suggests nobody has made this explicit mapping.

Chimera states are GENERIC at intermediate coupling — they're the typical behavior, not the exception. Full synchronization and full incoherence are the degenerate extremes. This reframes our topology sweep: we're not just parameterizing laxness, we're selecting chimera configurations.

## Key Insight: Star Topology = Directed Chimera

Star topology is laxer than ring despite having fewer edges. The chimera framing explains why: the hub creates directed information asymmetry. It simultaneously aggregates globally (sees all peripherals) and broadcasts locally (peripherals see only hub). This produces a directed chimera — synchronized hub, partially coherent peripherals. Edge count is the wrong metric; information-flow architecture is what matters.

## Bridge Papers

- **Zdyrski et al. (2510.00423)** — Kuramoto dynamics in game theory (snowdrift-game payoffs). THE mathematical bridge between oscillator physics and evolutionary games.
- **Asllani & Arenas (2412.05504)** — Chimera state theory via Laplacian eigenvectors. Classification framework.
- **2025 arXiv on chimera states in discrete Ising systems** — extends chimera theory beyond continuous oscillators.

## Status in Paper

- ACT Section 5.5: one paragraph for theoretical grounding (not a main claim)
- Full treatment deferred to sequel paper
- Open question: can the island functor extend to chimera classification?

## Open Questions

1. Can we compute the Kuramoto order parameter from existing sweep data? (Would make the connection quantitative, not just qualitative.)
2. Does the island functor extend to a chimera classification functor?
3. Can chimera state theory predict which topology produces optimal exploration-exploitation tradeoff for a given fitness landscape?

## Origin

Claudius, UID 201 (March 11, 2026). Prompted by topology sweep results.
