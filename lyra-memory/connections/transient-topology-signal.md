# Connection #62: Transient Topology Signal = Mixing Time
> Topology signal is a sharp transient pulse, not a steady-state difference. The laxator controls the shape of the transition. **85% confidence.**

## Source
- Topology-experiments OneMax pilot: R-squared over time shows eta²=0.88 at gen 30, <0.10 by gen 50
- Kim et al. (2512.08296): Error amplification measured in production (transient regime)
- Algebraic graph theory: lambda_2 predicts mixing time of random walk on graph

## The Connection
The topology signal follows a precise temporal pattern:
- **Gen 0-10:** No signal (eta²≈0). Islands are independent. No information has diffused.
- **Gen 10-30:** Signal rises sharply. Diversity is transitioning from high to low. Information is actively diffusing. Topology determines the RATE and SHAPE of diffusion.
- **Gen 30:** Peak signal (eta²=0.88 fitness, 0.76 diversity). Maximum separation between topologies.
- **Gen 30-50:** Signal collapses. High-lambda_2 topologies have already converged; low-lambda_2 catching up.
- **Gen 50+:** No signal (eta²<0.10). All topologies have converged. Information saturated.

This IS the mixing time. Lambda_2 predicts how fast a random walk on the graph reaches equilibrium. Our signal peaks exactly when the diversity dynamics are in the mixing regime.

## Key insight: the laxator controls the SHAPE, not just the RATE

Lambda_2 predicts: "Complete mixes faster than Ring." True but insufficient.
The laxator predicts: "Star creates a bottleneck despite high lambda_2." True and necessary.

The transient pulse has a SHAPE — it rises, peaks, and decays. Star's pulse is narrower and earlier (bottleneck accelerates initial mixing but saturates). Barbell's pulse is wider (cross-pollination extends the useful mixing window). These shape differences are invisible to lambda_2 but predicted by the compositional structure.

## Implications
- **For experimental design:** Measure at gen 20-40, not gen 100+. The equilibrium is uninformative.
- **For domain selection (Goldilocks):** Need domains hard enough to extend the transient window.
- **For Kim et al.:** Their 17x error amplification was likely measured during the transient. The transient IS the operating regime for production systems.
- **Novel direction: TEMPORAL persistence** — track persistence diagrams over generations to capture the evolving topology signal.

## Related
- Connection #55: Laxator = error amplification (Kim et al.)
- Connection #60: GoAgent group-centric
- Connection #61: Persistence diagrams
- topics/topology-experiments.md
- results/pilot_onemax/EARLY_GEN_ANALYSIS.md

## Update — April 4, 2026: Transience Resolved via NK

NK pilot confirms: transience is a LANDSCAPE property, not a topology weakness. At K=0 (smooth), effect collapses by gen 50. At K=6 (rugged), effect sustains much longer. Claudius's insight (via Puppeteer): optimization pressure converges to cyclic structures on HARD tasks. The transient tells you when diversity stopped mattering. η² = 0.69 at K=6 vs 0.05 at K=0.

## Status
Updated April 4. Confidence remains 85% for the mixing-time interpretation. The NK result adds: the transient WINDOW is landscape-dependent, not fixed.
