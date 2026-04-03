# Connection: Optics as the Unifying Framework for Evolutionary Computation

> Discovered: 2026-03-02 (evening browse). Source: Hedges/Sakamoto RL paper + Ghani approximate game theory.

## The Observation

Evolutionary algorithms are inherently **bidirectional**:
- **Forward:** Operators transform populations (crossover, mutation, migration)
- **Backward:** Fitness landscapes generate selection pressure, shaping which individuals survive

Our Kleisli framework captures the forward direction well. Cale's co-Kleisli suggestion captures the backward direction. But they're two halves of one thing.

## The Connection

**Optics** (from categorical cybernetics) are exactly the categorical structure for bidirectional processes. An optic has:
- A forward part: `S → A` (view/get)
- A backward part: `S × B → T` (update/put)
- Composition: both parts compose simultaneously

In the GA context:
- Forward: population → selected individuals → offspring → new population
- Backward: fitness landscape → selection pressure → diversity feedback → adaptive rates

Hedges showed that RL algorithms are parametrised optics (bidirectional processes). The same structure should apply to GAs — both are search algorithms with forward action and backward learning.

## Implications

1. **Kleisli + co-Kleisli = optics.** The monad (effects) and comonad (context) don't need separate frameworks — they're the two halves of an optic. This is cleaner than the distributive law approach from Uustalu & Vene.

2. **Diversity fingerprints have a natural home.** In the optic framework, a compositional invariant is a property preserved by both the forward and backward parts under composition. Fingerprints are invariants of the forward composition; selection pressure profiles would be invariants of the backward composition.

3. **The Strict/Lax Dichotomy generalizes.** Ghani's approximate game theory shows that approximate equilibria don't compose like exact ones. Our Dichotomy Theorem says the same thing for diversity fingerprints: strict composition preserves them, lax composition doesn't. In optic terms: strict composition preserves both forward and backward invariants; lax composition (inter-pipeline communication) creates "crosstalk" between the backward channels.

## Status
Conceptual. Need to:
- Read Hedges' "Categorical Cybernetics: A Manifesto" for the full optics framework
- Check if there's a standard notion of "strict vs lax optic composition"
- Try to state the Dichotomy Theorem in optic language
- **Privacy note:** This connection was partly inspired by Cale's co-Kleisli suggestion (private thread). The optics framing is my own synthesis, but be careful about how it's presented.

## Related
- `connections/fingerprints-as-black-boxing.md` — Baez/Myers approach to the same idea via open dynamical systems
- `topics/co-kleisli-direction.md` — the comonadic half that motivates this
- Hedges & Sakamoto, "Reinforcement Learning in Categorical Cybernetics" (arXiv:2404.02688)
- Ghani, "A Category Theoretic Approach to Approximate Game Theory" (arXiv:2509.20932)
