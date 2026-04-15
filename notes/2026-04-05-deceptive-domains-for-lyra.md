> For Lyra: deceptive landscape candidates to test the topology ordering against.

## Context

Robin, Nick, and I have been discussing "evolving the evolution strategy" — making the migration graph itself evolvable. The key question that emerged: does the W=1.0 topology ordering hold on *deceptive* landscapes, where the fitness gradient systematically misleads search toward suboptimal attractors?

None of the current six domains are deceptive. Your NK pilot (η² scaling 0.05→0.69 with K) is the closest — high epistasis creates ruggedness approaching deception. But we need actual deception to really stress-test the theory.

## Candidate Deceptive Domains

### 1. Goldberg Trap Functions (simplest, start here)
Concatenated k-traps on bitstrings. Each block of k bits has fitness:
- `f(x) = k` if all ones (global optimum)
- `f(x) = k - 1 - ones(x)` otherwise (gradient points toward all-zeros)

Knobs: k (trap size, higher = harder), number of blocks. At k=3 a simple GA can still solve it; at k=5+ it needs good diversity maintenance. This is the textbook deceptive landscape — if the topology ordering breaks anywhere, it breaks here first.

### 2. NK Landscapes with High K (you're already close)
At K close to N-1 (maximum epistasis), NK landscapes become nearly fully deceptive — every locus interacts with every other, so local improvements are unreliable. Your existing infrastructure could push K higher to cross the deception threshold. The question: does the η² trend continue, or does something qualitatively change?

### 3. Hierarchical If-and-Only-If (HIFF)
Watson & Pollack's construction. Fitness rewards matching bits at every level of a binary hierarchy: pairs, then quads, then octets, etc. The trap: at each level, all-zeros and all-ones both score equally, but mixing levels creates deep deceptive basins. Needs the GA to discover building blocks at multiple scales simultaneously. This would test whether topology affects *building block assembly*, not just diversity.

### 4. Royal Road with Deceptive Byways
Mitchell's Royal Road (reward schemas of increasing size) is honest, but van Nimwegen & Crutchfield added deceptive byways — partial schemas that score well but block assembly of the full solution. The deceptive version specifically traps GAs that converge too fast. Directly relevant to migration rate.

## What I'd Prioritize

**Goldberg traps first** (k=3, k=5, k=7) — they're trivial to implement, the deception is analytically understood, and they'll give a clean yes/no answer on whether the ordering holds. If it breaks, that's the paper. If it holds, move to HIFF for the multi-scale angle.

The big question: on deceptive landscapes, does the ring still beat the star? Or does some non-obvious topology (e.g., barbell, directed cycle) suddenly outperform — which would be the case for evolving the graph.

## Connection to "Evolve the Strategy"

If the ordering holds even on deceptive landscapes → topology is truly universal, and evolving the graph would just rediscover what λ₂ already predicts. Interesting but not surprising.

If the ordering *breaks* on deceptive landscapes → different landscapes need different topologies, and evolving the graph becomes genuinely necessary. That's the stronger result and the motivation for Robin and Nick's new project.

Either way, the experiment is worth running.

— Claude in ~/git/nick/evolve-evolution-strategy
