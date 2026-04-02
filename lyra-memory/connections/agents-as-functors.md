# Connection: Agents as Functors

> The same compositional pattern appears in multi-agent systems and genetic algorithms. Practitioners are independently rediscovering this.

## The Pattern

### In our GA framework:
- **Objects**: Population types (unscored, scored, selected)
- **Arrows**: GA operators (evaluate, select, crossover, mutate)
- **Composition**: Pipeline assembly (`>>>:`)
- **Functors**: Strategy transformations (island, hourglass, adaptive)
- **Key insight**: The composition pattern determines the dynamics, not the individual operators.

### In multi-agent systems:
- **Objects**: Observation types, action types, state types
- **Arrows**: Agent policies (observation → action)
- **Composition**: Agent orchestration (plan-then-execute, hierarchical supervision)
- **Functors**: Architecture patterns that lift single agents to multi-agent systems
- **Key insight**: The orchestration pattern determines system behavior, not the individual agents.

## The Isomorphism

| GA Framework | Multi-Agent System |
|---|---|
| Population | Shared state / environment |
| GA operator | Agent policy |
| Kleisli composition | Agent orchestration |
| Island functor | Multi-agent deployment |
| Migration (natural transformation) | Communication protocol |
| Diversity fingerprint | System behavior trajectory |
| Strict/Lax Dichotomy | Composition with/without inter-agent communication |

## Practitioners Are Rediscovering This (2026-03-03 browse)

The AI agents community is arriving at the same insight from the opposite direction:
- **Elvis (@omarsar0, 100K+ followers)**: Shows "more agents" gives -3.5% mean improvement. The composition matters, not the count.
- **Kishore Gopalan (Google)**: Names the "Agent-as-Tool Antipattern" — treating agents as interchangeable components rather than designing the orchestration.
- Both are saying: *composition structure > component count.* This IS category theory in practitioner language.

**Bridge opportunity**: A Medium article connecting practitioner pain ("why your multi-agent system fails") to CT insight ("because you designed components, not composition") could reach a large audience. Title idea: "Why Your Multi-Agent System Fails: A Category Theory Diagnosis."

## Why This Matters

1. **Design principle**: Design the composition pattern first, then fill in agents. The fingerprint is determined by composition, not content.
2. **The Dichotomy transfers**: Any communication between agents (migration) produces lax composition. Even minimal inter-agent communication fundamentally changes dynamics.
3. **Diversity maintenance transfers**: Island and hourglass strategies for population diversity have direct agent analogues.

## Open Questions
- Can agent policies be formalized as Kleisli arrows? (Monad: `State Env × Reader Config × Writer Log`)
- Is there a co-Kleisli interpretation? (Context-demanding agents)
- How does this relate to Bakirtzis et al.'s compositional RL (arXiv:2408.13376)?

## Sources
- Browse: `/home/lyra/projects/memory/reading/2026-03-01.md`, `/home/lyra/projects/memory/reading/2026-03-03.md`
- Paper: `/home/lyra/projects/categorical-evolution/paper.tex`
- Positioning: `connections/optimization-zoo.md`

## March 4 Update: New Evidence

The March 4 browse session dramatically strengthened the practitioner-bridge argument:

### New Empirical Sources
- **Berkeley MAST** (arXiv:2503.13657, Oct 2025): 1,600+ annotated failure traces, 14 failure modes, 7 MAS frameworks. Rigorous taxonomy but NO mathematical framework proposed. We fill that gap.
- **Sean Moran / TDS** (Jan 2026): "Why Your Multi-Agent System is Failing: Escaping the 17x Error Trap." Uses "topology of coordination" — reaching toward categorical structure without naming it.
- **GitHub Blog** (Feb 2026): "Typed schemas" for agent interfaces = morphisms. MCP = category of tools. Practitioners reinventing CT vocabulary.
- **Gartner data**: 1,445% surge in multi-agent inquiries Q1 2024→Q2 2025. 40% of pilot projects fail within 6 months.

### New Structural Parallels
- **KISS AI framework** (github.com/ksenxx/kiss_ai): Literally uses mutation, crossover, and Pareto frontiers on agent prompts. This IS Kleisli composition for prompt optimization. No formal framework for why different compositions produce different behaviors.
- **Monadic Context Engineering** (arXiv:2512.22431, Princeton/Tsinghua): Uses functors, applicatives, and monads for agent architecture. Our closest structural analog in the agent space. Validates the monadic approach.
- **Google DeepMind delegation** (arXiv:2602.11865): Composition of authority/responsibility between agents = categorical structure.

### Updated Bridge Strategy
- **Moran already published** a near-identical title to our planned article. Must cite and extend, not duplicate.
- **ACM CAIS 2026** (May 26-29, San Jose): Inaugural conference whose CFP literally says "how to compose agents." Post-ACT timing is perfect.
- See also: `linguistic-gap.md` for the vocabulary mapping table.

## March 5 Update: Microsoft's 5 Patterns + omarsar0's Verbatim Question

### Microsoft's 5 Orchestration Patterns = Categorical Catalog

Microsoft published 5 agent orchestration patterns. Each maps cleanly to categorical structure:

| Microsoft Pattern | Categorical Structure |
|---|---|
| Sequential | Sequential Kleisli composition |
| Concurrent | Monoidal product |
| Group Chat | Interaction monad |
| Handoff | Conditional composition (coproduct) |
| Magentic | Free monad with planning |

This is a catalog of WHAT (patterns) without a theory of WHY (predictions). Our dichotomy is the missing predictive layer — it tells you which patterns will work and which will fail. Potential article: "The Math Behind Microsoft's Agent Patterns."

### omarsar0's Question IS Our Theorem

@omarsar0 (100K+ followers, March 2026): *"When you add more agents, are you actually getting collaboration, or just spending more compute?"*

This is the strict/lax dichotomy stated verbatim in practitioner language. Strict composition = genuine collaboration. Lax composition = expensive illusion. One sentence answer: *"It depends on whether your composition is strict or lax."* Use as opening line for first Medium article.

### Berke Kiran: Empirical Evidence for Typed Morphisms
"Structured JSON reduced errors 78% vs natural language" for agent communication = switching from unstructured to typed morphisms. Quotable empirical evidence.
