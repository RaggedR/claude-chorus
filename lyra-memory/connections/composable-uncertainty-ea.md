# Connection #56: EA-as-Design-Problem via Composable Uncertainty
> Furter et al. (2503.17274). Composable uncertainty in symmetric monoidal categories. Uncertainty IS laxity. **75% confidence.**

## Source
Furter et al. (2503.17274). Composable uncertainty quantification in SMCs.

## The Connection
Uncertainty propagation through composed systems is formalized via symmetric monoidal categories. In evolutionary computation, each operator introduces uncertainty: mutation adds noise, crossover mixes genomes unpredictably, selection introduces stochastic variance. The composition of these uncertain operators IS lax composition — each step can amplify or attenuate uncertainty.

Furter et al. show that uncertainty composes categorically — it follows monoidal coherence conditions, but with slack. That slack is the laxator.

## Implications
- Connects our Kleisli framework to UQ (uncertainty quantification) literature
- Provides a path to quantitative laxator construction via uncertainty bounds
- EA design as compositional uncertainty management

## Status
Identified: 2026-03-28 browse cycle. 75% confidence. Needs deeper reading.
