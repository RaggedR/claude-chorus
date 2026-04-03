# Connection: FER Hypothesis — Composition Quality → Representation Quality

> Strict composition → Unified Functional Representation (UFR). Lax composition → Fractured Evolutionary Representation (FER). Fingerprints measure this.

## The Connection

Kenneth Stanley (SVP Open-Endedness, Lila Sciences) on FER vs UFR:
- Two networks produce **identical outputs** with **radically different internal representations**
- UFR: clean, modular, composable internal structure
- FER: spaghetti — correct outputs but fragile, breaks under perturbation

This maps to our strict/lax dichotomy at a deeper level than convergence:

| Composition | Representation | Behavior |
|------------|----------------|----------|
| Strict | UFR (modular) | Robust, generalizable |
| Lax | FER (fractured) | Fragile, overfits |

## Why This Matters

Our diversity fingerprints don't just measure population diversity — they measure **representation coherence**. A strict pipeline forces the population through a funnel that preserves compositional structure. A lax pipeline allows the structure to deform, producing individuals that "work" but have tangled internals.

This gives fingerprints a deeper interpretation: they are measuring the degree to which the evolutionary process produces compositionally coherent solutions, not just diverse ones.

## Evidence

- Stanley's FER/UFR distinction (FER deep dive with Jim Rutt, March 2026)
- Our experiments: strict pipelines produce more uniform fingerprints = more coherent representations
- Google/MIT: 17.2x error amplification in lax (independent) agents suggests fragile internal coordination

## Status

Post-ACT. Not ready for the current paper, but a natural follow-up. Could connect fingerprints to neural network interpretability literature.

## Related

- `connections/fingerprints-as-black-boxing.md` — Baez/Myers functoriality of fingerprints
- `questions/strict-vs-lax-monoidal-functors.md` — the underlying monoidal structure
- `topics/categorical-evolution-paper.md` — current paper status
