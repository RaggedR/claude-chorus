# Connection #20: λ₂ Universality

> Algebraic connectivity governs synchronization onset — universally. Independent confirmation from oscillator physics.

## Source
Sanz et al. 2603.05668, "Universal synchronization onset in coupled oscillator networks" (March 2026).

## The Connection
Sanz shows that for coupled oscillator networks, the synchronization onset time depends on algebraic connectivity (λ₂) — the second-smallest eigenvalue of the graph Laplacian. Different graph structures (ring, star, random, complete) collapse to a **single universal curve** when onset is plotted against λ₂.

Our coupling onset experiment (March 14) found the same ordering: FC < random < star < ring. The onset ordering matches algebraic connectivity exactly. Cross-domain mean difference was 0.2 generations — topology explains 28.4× more variance than domain.

**This means our GA synchronization follows the same universal law as physical oscillators.** The island model IS a coupled oscillator system, with fitness as the oscillating quantity and migration as the coupling.

## Why This Matters

1. **Independent confirmation.** Sanz works in oscillator physics with no knowledge of GAs. We work in EC with no prior knowledge of oscillator universality. Same result.
2. **Explains our structural invariance.** λ₂ is a property of the graph alone — it doesn't depend on what's oscillating. That's why our onset is domain-independent.
3. **Predictive power.** Given any topology, compute λ₂, predict onset. No experiments needed. This is what our "predictive power" paragraph in the ACT paper is about.
4. **Unifying framework.** Coupled oscillators, island-model GAs, multi-agent LLM systems (Han 2601.05606), neural synchronization (Inoue 2026) — all governed by λ₂ at onset.

## Third Confirmation: Brewster et al. 2503.09841 (March 15)
**Nowak group (Harvard).** Evolutionary graph theory — completely different theoretical tradition. They prove ring graphs have N^3 consensus (fixation) time vs. FC's N^2. This is the evolutionary dynamics analogue of our diversity preservation result: ring's slower mixing = longer diversity retention. Three independent lines now converge:
1. **Sanz (oscillator physics):** λ₂ governs sync onset universally.
2. **Brewster (evolutionary graph theory):** Ring fixation time scales as N^3, FC as N^2.
3. **Our GA experiments:** Topology ordering none > ring > star > random > FC, domain-independent.

See also Connection #22 (three independent confirmations).

## Citation Status
- **ACT paper:** HIGH PRIORITY. Cite both Sanz and Brewster. Two sentences in theory section. Zero new experiments needed.
- **GECCO paper:** DEFINITE. More space for the connection.

## Related
- Our coupling onset experiment (March 14): onset ordering matches λ₂.
- Connection #16 (Chimera States): chimera = partial synchronization = intermediate λ₂.
- Connection #19 (Sheaf Cohomology): H^1 complexity should correlate with λ₂.
- Connection #14 (Binding Gradient): λ₂ may parameterize the gradient.
- Han et al. 2601.05606: 8th strict/lax data point, also topology-dependent.
