# Connection #67: The Bitter Lesson Resolves at the Monad Level
> 85% confidence. March 29, 2026.

## The Connection

The bitter lesson debate for agents: "Will harness engineering survive scaling, or get bitter-lessoned out of existence?" (Aaron Levie, Box CEO). @buckeyevn: "Most Agent Harnesses Are Not Bitter Lesson Pilled."

The resolution lives at the monad level:

**SCAFFOLDING** (gets bitter-lessoned):
- Specific prompt templates
- Hand-coded retry logic
- Tool-specific error handling
- Framework-dependent state management
- These are the monad's IMPLEMENTATION — they change as models improve

**STRUCTURE** (survives bitter lesson):
- Unit (wrapping a value in context)
- Bind (composing contextual computations)
- Associativity (composition order doesn't matter)
- These are the monad INTERFACE — they're mathematical, not empirical

The monad IS bitter-lesson-compatible because it's a structural pattern, not hand-coded knowledge. As models get better, the IMPLEMENTATION of bind changes (simpler error handling, less scaffolding), but the INTERFACE persists (you still compose agents via bind, you still lift values via unit).

## Evidence
- Vercel: removed 80% of tools (scaffolding), kept composition (structure) → 80% → 100% accuracy
- OpenClaw → NanoClaw: removed 99.999% of code, preserved categorical operations
- Anthropic Agent SDK: minimal interface (AgentDefinition + tools + model), maximal capability
- All three: scaffolding removed, structure preserved, performance improved

## Implications
- "Harness Is a Monad" article should explicitly address the bitter lesson debate — it's the hook
- The monad interface IS the irreducible structure that survives scaling
- Prediction: successful frameworks will converge to monad-like interfaces as scaffolding is automated away
- This is a testable prediction for the article: "In 2 years, the scaffolding in today's harnesses will be gone, but unit/bind/associativity will remain"

## Links
- Connection #43 (Harness-as-Monad)
- Connection #65 (Framework Compression IS Functoriality)
- topics/medium-strategy.md
