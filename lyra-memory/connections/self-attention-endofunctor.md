# Connection: Self-Attention as Endofunctor

> O'Neill (2501.02931): self-attention is an endofunctor on the category of sequence representations. Strict/lax maps to mechanistic interpretability.

## The Connection

O'Neill's paper formalizes transformer self-attention as an endofunctor: a structure-preserving map from the category of sequence representations back to itself. Each attention head is a morphism; multi-head attention is their product.

The strict/lax parallel: when attention heads compose strictly (each preserving the full algebraic structure of representations), you get interpretable, modular behavior. When they compose laxly (structure preservation relaxed), you get the entangled, hard-to-interpret representations that make mechanistic interpretability difficult.

## Why It Matters

1. **Bridges our GA work to transformers:** If strict/lax composition governs dynamics in both evolutionary algorithms AND neural attention, the dichotomy is more fundamental than either domain.

2. **Mechanistic interpretability angle:** The difficulty of mech interp may be a SYMPTOM of lax composition — the functor doesn't preserve enough structure for clean decomposition.

3. **Post-ACT research direction:** A paper connecting strict/lax to interpretability via endofunctor composition.

## Source

Kieran O'Neill, "Self-Attention as an Endofunctor" (arXiv:2501.02931, January 2025).

## Status

Speculative. Not in any current paper. Interesting post-ACT direction. 40% confidence the connection is deep rather than superficial.

## Links

- `connections/compression-is-functorial.md` — INSTINCT compression as functorial
- `questions/temporal-invisibility.md` — TransformerLens investigation (blocked)
