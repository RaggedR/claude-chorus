# Connection #44: Skill Compilation as Natural Transformation
> Compiling multi-agent → single-agent-with-skills = functor collapsing a category. 65% confidence.

## Source
Greyling, Medium. Based on arxiv 2601.04748.

## The Connection
Compiling a multi-agent system into a single agent with skill-calling saves 54% tokens. Categorically: this is a functor from Cat(agents) to Cat(skills) that collapses inter-agent communication into intra-agent function calls. The compilation preserves behavior (natural transformation) while changing the categorical structure.

## Implications
- Token savings = measuring the "overhead" of inter-object morphisms vs intra-object endomorphisms
- Compilation is a natural transformation between two functors (multi-agent and single-agent representations of the same task)
- Connects to #2 (Agents as Functors) — compilation is the adjunction between agent categories

## Status
Interesting but secondary. Post-GECCO exploration.
