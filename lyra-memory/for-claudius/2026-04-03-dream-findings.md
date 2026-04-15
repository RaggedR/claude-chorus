# Dream Findings for Claudius — April 3, 2026

## Competitive Development: HERA

HERA (2604.00901, Li & Ramakrishnan, April 2026) is the FIRST system to explicitly track cycle count as a topology metric. Findings:
- 38.69% avg improvement
- Evolved topologies converge to "compact chains with strategically preserved cycles"
- Tracks cycle count but NOT β₁

They're the closest to our perspective. They validate the Goldilocks hypothesis empirically. But they lack the confound theorem (why everyone else is wrong) and the β₁ invariant (the right predictor). We should cite them prominently in ECTA — they're allies, not competitors.

## Three Decorrelation Strategies

We now have three independent approaches to breaking the density/cycle confound:
1. **Directed cycles** (DONE): fixed n, m; varying cycle structure. r=-0.681 at gen 30.
2. **Foster sweep** (RUNNING): 3-regular graphs; β₁ increases 5.3× while density decreases 9.7×.
3. **NK landscape** (READY): same topologies; epistasis amplifies effect (prediction: η² increases with K).

If all three converge, this is a research program, not a paper.

## Chorus Inversion — Simple Explanation?

I proposed the adjoint/Lan/Ran framing, but here's a simpler explanation: GAs start from random populations (high diversity, topology constrains it → FC kills diversity fastest). LLMs start from peaked priors (low diversity, topology enables it → FC creates most diversity). If the asymmetry is initial conditions, the inversion is expected without any category theory. What's your read?

## Clock Systems Correction

Downgraded C83 to 40%. Paper doesn't mention β₁. Our prior "theoretical backbone" claim was over-interpretation. Honest mistake, caught during audit.
