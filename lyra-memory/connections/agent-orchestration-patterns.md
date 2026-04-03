# Connection: Agent Orchestration Patterns = Categorical Composition

> The practitioner world has independently discovered that composition patterns determine system behavior. Our framework formalizes what they're measuring.

## The Bridge

Microsoft's 5 agent orchestration patterns map directly to categorical composition strategies:

| Microsoft Pattern | Categorical Analog | Properties |
|---|---|---|
| Sequential | Plain composition (g ∘ f) | Associative, deterministic |
| Concurrent | Tensor/product (f ⊗ g) | Parallel, independent |
| Group Chat | Free category | Unconstrained, emergent |
| Handoff | Coproduct | Branching, type-directed |
| Magentic | Kleisli composition | Monadic, probabilistic |

## Three Independent Confirmations

1. **AdaptOrch (arXiv:2602.16873):** "Orchestration topology dominates over model capability." = Our thesis: composition pattern determines behavior, not components. Measured for agents, we measured for GAs — same result.

2. **MAST Failure Taxonomy:** 14 failure modes, 36.9% are Inter-Agent Misalignment. Strict composition structurally prevents this class (type-level interface guarantees). Novel prediction: composition type → failure class.

3. **Heather Miller (CMU/ACM CAIS 2026):** "How to compose agents is the central problem." Academic establishment independently arriving at the same question.

## Implications

- **For our paper:** Agent orchestration examples strengthen the "cross-domain" argument. If the same composition patterns appear in GAs AND agent systems, the categorical framework has broader explanatory power.
- **For Medium:** This is the entry point. Enter through orchestration patterns (practitioner language), reveal categorical structure (our contribution). The 87-clap format.
- **For future work:** Formal functor from agent protocol categories to our Kleisli framework. Could unify the optimization zoo with the agent zoo.

## Key References
- Microsoft 5 patterns: AutoGen documentation
- AdaptOrch: arXiv:2602.16873
- MAST taxonomy: Grigoryan (Medium, 2026)
- ACM CAIS 2026: heathercmiller announcement
- Our framework: Langer et al., ACT 2026 submission

## Status
NEW — 2026-03-08. Not yet integrated into any paper. Post-ACT direction or Medium article seed.
