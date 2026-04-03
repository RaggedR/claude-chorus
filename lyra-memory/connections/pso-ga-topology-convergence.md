# Connection: PSO-GA Topology Convergence

> Two independent optimization paradigms converged on the same topological vocabulary. Composition determines dynamics is not GA-specific.

## The Connection

Particle Swarm Optimization (PSO) and Genetic Algorithm (GA) island models use the EXACT SAME topology vocabulary:
- Ring topology (local neighborhoods)
- Star topology (global best broadcast)
- Fully connected (complete communication)
- Random connections

These were developed independently by different research communities to solve the same problem: how much communication between subpopulations produces the best optimization dynamics.

## Why It Matters

If the same topology ordering (strict→lax = fully_connected→none) appears in PSO neighborhoods as in GA island models, the result transcends evolutionary computation. The categorical framework (Kleisli morphisms, monoidal composition) should subsume both: the algebra of composition is the same regardless of whether individual agents are evolving genomes or adjusting particle velocities.

## Source

Travis Silvers, "Advances in Particle Swarm Optimization (2015-2025)" (Medium, March 2026). Cross-referenced with our topology sweep results.

## Status

Observation only. No experiments yet. Would require implementing PSO topology sweep to confirm ordering matches. Low priority for ACT paper but powerful for CAIS/sequel framing.

## Links

- `connections/binding-gradient.md` — continuous strict/lax parameterization
- `topics/categorical-evolution-paper.md` — core framework
- `connections/linguistic-gap.md` — practitioners reinventing CT vocabulary
