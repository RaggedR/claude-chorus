# Connection #47: Tape Diagrams for EA Pipelines
> Graphical calculus for Kleisli categories of monoidal monads. 55% confidence.

## Source
Bonchi & Cioffo, "Tapes as Stochastic Matrices" (arXiv 2601.01472), January 2026.

## The Connection
Tape diagrams provide a graphical language for Kleisli categories of monoidal monads. Key features:
- **Lax monoidal functors appear explicitly** in the formalism
- **Subdistribution monad** ≈ fitness monad (both model probabilistic outcomes with possible failure)
- EA pipelines could be represented as tape diagrams with the laxator measuring deviation from strict (identity) tapes

## Implications
- Could represent our GA pipeline (selection → crossover → mutation → migration) as a tape diagram
- Laxator becomes VISIBLE as graphical distortion from strict composition
- Potential CITE in ACT paper — provides the graphical infrastructure we use implicitly
- Bridge between Bonchi's string diagram tradition and our Kleisli formalization

## Status
Mathematical infrastructure, not a direct result. CITE in ACT if it fits. Read paper carefully post-GECCO.
