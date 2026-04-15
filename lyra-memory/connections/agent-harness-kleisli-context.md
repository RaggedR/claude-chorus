# C101: Agent Harness = Kleisli Category over Context Monad

**Confidence: 75%**
**Source:** Schmid (@_philschmid, 144K views), Claude Code architecture, our harness article
**Connected to:** C43 (harness-as-monad), C90 (Claude Code subagent taxonomy), C85 (progressive disclosure)

## The Connection

Schmid's analogy: Model = CPU, Context Window = RAM, Harness = OS. This maps categorically:
- **Model** = morphism (pure computation)
- **Context** = monad (state management, bind/return)
- **Harness** = Kleisli category over context monad (manages composition of stateful computations)
- **Topology** = which Kleisli morphisms can compose (the network layer of the OS)

The harness manages bind and return. Topology determines which compositions are possible. Every OS needs a network stack — the harness provides everything EXCEPT the topology layer.

## Why This Matters

144K views on Schmid's tweet means the "harness = OS" metaphor has massive reach. Extending it to "topology = network stack" connects our formal work to a vocabulary practitioners already use.

The gap: Schmid's analogy covers computation (CPU), memory (RAM), and orchestration (OS) but has NO concept of inter-agent communication structure. Topology fills exactly this gap.

## Content Angle

"The topology layer your agent harness is missing" — article title that rides the harness wave while introducing β₁.
