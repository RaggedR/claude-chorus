# Connection #36: GTD Diffusion Topology Generation

> Engineering "how" for topology design complements our mathematical "why." **70% confidence.**

## Paper

GTD — Graph Diffusion for Agent Topology (ICLR 2026 submission). First discrete graph diffusion model for generating agent communication topologies. +4.16 on GSM8K, +5.44 on MATH.

## The Connection

GTD addresses the same problem we do — which topology for which task? — but from the engineering side:
- **GTD:** Learn to generate good topologies via diffusion. Data-driven. No theory for WHY the generated topologies work.
- **Us:** Formal theory (Kleisli + spectral) explaining WHY certain topologies preserve diversity. Theory-driven. No automated topology generation.

**Complementary, not competing.** GTD's generated topologies could be analyzed through our framework. Our framework could provide the loss function or structural constraints for GTD-style generators.

## Topology Tipping Point

GTD is the 10th+ group in the topology convergence. Uses graph structure but no spectral theory, no category theory.

## Confidence: 70%

Clear complementarity. The question is whether our theory provides actionable constraints for their generator, or whether the connection is only conceptual.

## Status: Monitor. Potential ECTA 2026 direction.
