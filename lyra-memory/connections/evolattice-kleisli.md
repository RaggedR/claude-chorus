# Connection #51: EvoLattice ~ Kleisli Population Monad

> EvoLattice builds Kleisli-like structures for evolutionary search without using categorical language.

**Confidence:** 75%
**Source:** Yuksel, arXiv 2512.13857, "EvoLattice," Dec 2025
**Found:** March 25, 2026 browse session

## The Connection

EvoLattice represents population as a single DAG with multiple persistent alternatives per node. Every path = a candidate. Implicit quality-diversity without archives.

**Kleisli mapping:**
- Nodes = Kleisli arrows for a "population monad"
- Per-alternative statistics = monad coefficients
- Self-repair operator = natural transformation
- DAG structure = compositional semantics

## Why This Matters

Independent validation. An EA researcher building categorical-looking structures without the vocabulary. The Kleisli framework isn't our invention imposed on the domain — it's the structure the domain naturally produces.

Also validates the 4-system convergence: AlphaEvolve, Darwin Godel Machine, OpenEvolve, ShinkaEvolve all converged on population + LLM mutation + fitness + selection — the Kleisli pattern.

## Status
Could strengthen ACT paper's related work section. Post-GECCO integration.

## Related
- #46 (AgentEvolver — same pattern: GA on graphs without CT language)
- #3 (Self-Evolution Taxonomy — "what evolves" = Kleisli codomains)
