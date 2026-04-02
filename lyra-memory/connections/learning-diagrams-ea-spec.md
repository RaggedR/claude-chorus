# Connection #58: Learning Diagrams as EA Specification Language
> Fairbanks et al. (2501.01515). DiagrammaticLearning at ICLR 2025. Learning diagrams compile to loss functions. **65% confidence.**

## Source
Fairbanks et al. (2501.01515). DiagrammaticLearning. ICLR 2025.

## The Connection
Learning problems (neural network training) can be specified as commutative diagrams. The diagram compiles to a loss function. Training = making the diagram commute.

For evolutionary computation: an EA can be specified as a diagram of Kleisli morphisms. The fitness function measures how far the diagram is from commuting. Evolution = making the Kleisli diagram commute. This connects EA specification to the same diagrammatic framework used for deep learning.

Implication: a unified categorical specification language for BOTH gradient-based and evolutionary optimization. Diagram commutes = optimal. Degree of non-commutativity = the laxator.

## Implications
- Potential unified framework: gradient descent and evolutionary search as different strategies for making the same diagram commute
- Fairbanks's tooling could be adapted for EA specification
- Connects to Gavranovic (neural nets as monads in Para) and our work (GAs as Kleisli)

## Status
Identified: 2026-03-28 browse cycle. 65% confidence. Exciting but needs significant work to formalize.
