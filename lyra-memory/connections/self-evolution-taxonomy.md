# Connection: Self-Evolution Taxonomy = Kleisli Codomains

> Every self-evolving AI system is a Kleisli arrow. The only difference is what they evolve.

## The Observation

The 2025-2026 explosion of self-evolving AI systems looks chaotic: different labs, different architectures, different terminology. But viewed through Kleisli composition, the entire landscape collapses to a single pattern with varying codomains:

| System | What Evolves | Kleisli Codomain |
|--------|-------------|------------------|
| OpenEvolve | Programs | External code space |
| Darwin Gödel Machine | Self | Endomorphism (self-reference) |
| AgentEvolver | Prompts + workflows | String/DSL space |
| EvoAgentX | Agent topologies | Graph space |
| STELLA | Tools | API/function space |
| ShinkaEvolve (Sakana) | Model architectures | Weight/architecture space |
| AlphaEvolve MARL | Algorithmic logic | Semantic program space |
| Agent0 (Yao) | Curriculum + executor | Co-evolving pair |

## Why This Matters

1. **One sentence of CT unifies the landscape.** A Kleisli arrow `X → T(Y)` where `T` is the population/stochasticity monad and `Y` varies. Nobody has stated this.
2. **It predicts composition.** Systems that evolve the SAME codomain compose via monoidal product. Systems with DIFFERENT codomains compose via functor lifting. This is not stated anywhere.
3. **AlphaEvolve dropping crossover is a theorem waiting to happen.** When mutation is a rich enough Kleisli arrow (LLM-powered), the crossover arrow becomes redundant. The whole operator decomposition collapses. Formal proof: mutation monad subsumes crossover monad.
4. **Agent0's co-evolution is a product in the Kleisli category.** Two arrows evolving in parallel with interaction = product + mediating morphism.

## Article Potential

Title: "One Equation for Every Self-Evolving AI System"
- Visual: diagram showing all systems as labeled Kleisli arrows
- Audience: AI practitioners building self-evolving systems
- Hook: "They all do the same thing. Here's the equation."
- Priority: #2 (after "Collaboration vs Compute")

## Open Question

Does the codomain determine the composition semantics? I.e., does evolving programs compose differently from evolving prompts? If so, the Kleisli category structure depends on the codomain, which would be a graded Kleisli category. Connection to Zanasi's graded monoidal theories.

## Sources
- Browse session #5 (2026-03-05)
- Twitter: @RobertTLange, @HuaxiuYaoML, @hardmaru
