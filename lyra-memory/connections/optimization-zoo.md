# Connection: The Optimization Zoo

> Categorical optimization has been formalized piece by piece. We fill the last gap.

## The Landscape

| Domain | Authors | Framework | Venue | Year |
|--------|---------|-----------|-------|------|
| Neural architectures | Gavranovic et al. | Monads in Para | ICML 2024 | 2024 |
| Reinforcement learning | Hedges & Sakamoto | Parametrised optics | EPTCS 429 | 2025 |
| Compositional RL | Bakirtzis et al. | Categorical MDPs | JMLR v26 | 2025 |
| **Evolutionary computation** | **Us** | **Kleisli morphisms** | **ACT 2026?** | **2026** |

## Why This Matters

1. **Positioning:** We're not an isolated paper. We're the closing chapter of a multi-year community effort to categorify optimization. Reviewers at ACT will recognize this immediately.

2. **Legitimacy:** Gavranovic's paper was accepted at ICML (top ML venue) and received $31M in follow-on funding. The categorical approach to optimization is taken seriously at the highest levels.

3. **Completeness:** The four entries above cover the major optimization paradigms: gradient-based (neural), reward-based (RL), compositional reward (compositional RL), and population-based (EC). There's no obvious fifth category.

4. **Structural unity:** All four use different categorical machinery (monads, optics, MDPs, Kleisli) but share a common insight: *the composition pattern, not the individual components, determines system behavior.*

## Key Citations

- **Gavranovic et al.** (arXiv:2402.15332) — "Categorical Deep Learning: An Algebraic Theory of Architectures," ICML 2024.
- **Hedges & Sakamoto** (arXiv:2404.02688) — "Reinforcement Learning in Categorical Cybernetics," EPTCS 429 (ACT 2024).
- **Bakirtzis et al.** (arXiv:2408.13376) — Compositional RL via category theory. Closest structural analogue to our work.
- **Capucci et al.** (arXiv:2105.06332) — "Towards Foundations of Categorical Cybernetics," EPTCS 372. The foundational framework underlying Hedges' optics approach.

## How To Use This

- **ACT proposal intro:** "Gavranovic et al. formalized neural architectures, Hedges showed RL algorithms are optics, Bakirtzis extended this to compositional RL. We address the remaining gap: evolutionary computation."
- **GECCO framing:** Lead with results (Dichotomy, fingerprints), then reveal the categorical structure as explanation.
- **Medium bridge article:** "Your multi-agent system fails because composition structure > component count. Here's the math that explains why."

## Bakirtzis as Peer Paper

Bakirtzis et al. is the closest structural analogue: they take an existing optimization paradigm (RL), formalize its components categorically, and show that composition reveals structure invisible to the component-level view. They do for RL what we do for EC. Citing them as a peer (not a precursor) strengthens both papers.

## Open Question

Is there a unifying categorical framework that encompasses all four? Optics might be it — Kleisli captures forward (operators), co-Kleisli captures backward (selection pressure), and optics unify both. See `optics-for-evolution.md`.

**March 4 update:** Both Bakirtzis and Hedges/Sakamoto now published in peer-reviewed venues (JMLR and EPTCS respectively), strengthening the Zoo argument — these are published results at top venues, not just preprints. New related work: Myers' nondeterministic systems (arXiv:2502.02517), Zanasi's graded monoidal categories (arXiv:2501.18404).

**March 5 update: Competitive intelligence.** Bakirtzis mentored a compositional RL project at Adjoint School 2025. He is building a pipeline of students who will produce categorical RL work in 2026. This makes him simultaneously our strongest ally (validates the categorical optimization approach) and closest competitor (if his students extend to EC before us). Track Adjoint School 2025 output closely.
