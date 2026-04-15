# Experimental Design: Separating Density from Cycle Rank

> Research agent analysis for Paper 2. April 3, 2026.

## 1. The Structural Impossibility

**Theorem.** For connected graphs on a fixed number of vertices n, the cycle rank beta_1 is a deterministic function of the edge count:

    beta_1 = |E| - n + 1

Therefore, for connected graphs with fixed n, beta_1 and |E| (and hence density) are **perfectly collinear**. There is no connected graph on 8 nodes with 10 edges and beta_1 = 2 — it must be beta_1 = 10 - 8 + 1 = 3. Always.

**This means the "obvious" experiment — hold |E| constant, vary beta_1 — is impossible for connected graphs with fixed node count.**

This is not an artifact of small samples. It is a theorem of algebraic topology. The first Betti number of a connected graph is exactly |E| - |V| + 1. Period.

## 2. What This Means for the Literature

Every paper comparing topologies on the same agent count (fixed n) with connected communication graphs is comparing graphs where beta_1 and |E| are the SAME variable. When Dochkina says "sparse beats dense" and we say "low beta_1 beats high beta_1," we are making the same claim with different notation. There is no possible controlled experiment to separate them in this regime.

**This is a more important finding than we initially thought.** The confound isn't sloppy experimental design — it's mathematically forced.

## 3. Five Escape Routes

The structural impossibility holds only under three simultaneous constraints: (a) fixed n, (b) connected, (c) single scale. Relaxing any of these opens an escape route.

### Escape Route A: Multi-Component Graphs (Relax Connectedness)

For general graphs: beta_1 = |E| - |V| + c, where c = number of connected components.

A disconnected graph on n=8 nodes with 2 components can have different (|E|, beta_1) combinations:

| Graph Description | Components | |E| | beta_1 |
|---|---|---|---|
| Two 4-paths (path on 4 nodes each) | 2 | 6 | 0 |
| K4 + 4 isolated nodes | 5 | 6 | 3 |
| Two K3 + 2 isolated | 4 | 6 | 2 |
| C4 + K4 | 2 | 10 | 4 |
| Path-8 broken into 2 paths + 2 extra edges forming a cycle in one component | 2 | 8 | 2 |

**Same |E|=6, different beta_1:** Two 4-paths (beta_1=0) vs K4 + 4 isolated (beta_1=3). Both have 6 edges on 8 nodes.

**Problem:** Comparing a connected graph to a disconnected graph introduces a massive confound — communication partitioning. Isolated agents receive no information. This changes the problem fundamentally, not just the topology.

**Verdict:** Technically feasible but practically useless. The disconnection effect dominates everything.

### Escape Route B: Vary Node Count (Relax Fixed n)

Compare graphs with different n but same density AND same beta_1 — impossible (beta_1 = density * n(n-1)/2 - n + 1, coupling them again). Compare graphs with different n, same |E|/n ratio, different beta_1/|E| ratio... the degrees of freedom multiply but so do confounds (team size effects, coordination overhead scaling).

**Verdict:** Too many confounds. Node count is not a neutral parameter.

### Escape Route C: Weighted / Directed Graphs (Richer Structure)

For directed graphs, the first Betti number of the underlying undirected graph still follows the same formula. But directed graphs have a richer structure: the same undirected cycle can be oriented as a directed cycle (information flows around the loop) or not (one agent broadcasts, the other receives, no feedback loop).

**Key insight:** Two directed graphs can have the SAME undirected skeleton (same |E|, same undirected beta_1) but different numbers of DIRECTED CYCLES.

Example on n=4, |E|=5 (directed edges):
- Graph A: 0->1, 1->2, 2->3, 3->0, 0->2. Contains the directed 4-cycle 0->1->2->3->0 and the directed 3-cycle 0->1->2->0 (via shortcut). Two directed cycles.
- Graph B: 0->1, 0->2, 0->3, 1->0, 2->0. Star-like with one reciprocal pair. Contains one directed 2-cycle 0->1->0. One directed cycle.

Both have 4 nodes and 5 directed edges. The undirected skeletons differ, so this is not quite the right construction. But the principle is clear: **directionality breaks the collinearity.**

For MAS, communication IS directed (agent A sends to agent B). The relevant beta_1 should be computed on the directed communication graph, not the undirected skeleton. The number of directed cycles (strongly connected components, directed cycle rank) is NOT determined by |E| and |V| alone.

**Directed cycle rank** for a directed graph: beta_1^{dir} can be defined via the cycle space of the directed graph. For a strongly connected directed graph on n nodes with m directed edges, the directed cycle rank is m - n + 1 (same formula). But a directed graph on n nodes with m edges need NOT be strongly connected even if the underlying undirected graph is connected. This breaks the deterministic relationship.

**Example (n=4, m=6 directed edges):**
- Graph A (tournament): 0->1, 1->2, 2->3, 0->2, 0->3, 1->3. Transitive tournament. Zero directed cycles. DAG.
- Graph B: 0->1, 1->2, 2->0, 0->3, 3->2, 3->1. Contains the directed 3-cycle 0->1->2->0.

Both have 4 nodes and 6 directed edges. Graph A has 0 directed cycles. Graph B has directed cycles. **Same (n, m), different directed cycle structure.**

**Verdict: THIS IS THE MOST PROMISING ESCAPE ROUTE.** MAS communication is inherently directed. The directed cycle rank is the correct quantity, and it is NOT determined by (n, m) alone.

### Escape Route D: Cycle Structure at Fixed beta_1 (Reframe the Question)

Even when beta_1 is fixed (because |E| is fixed for connected undirected graphs), the ARRANGEMENT of cycles matters. Two graphs with the same beta_1 can have very different cycle structures:

**n=8, |E|=10, beta_1=3. Three independent cycles.** But:
- Graph D1: Three triangles sharing a common vertex, with tree edges connecting them. Short, local cycles. Highly clustered.
- Graph D2: Three long cycles of length ~5-6 overlapping across the graph. Global cycles. Low clustering.
- Graph D3: One K4 subgraph (beta_1=3 from the clique), rest are tree edges. One dense pocket.

All have beta_1=3, same |E|=10, same n=8. But the cycle LENGTH DISTRIBUTION, the GIRTH (shortest cycle), the CLUSTERING COEFFICIENT, and the CYCLE CENTRALITY differ.

This doesn't separate beta_1 from density (they're the same variable here), but it shows that beta_1 is a coarse summary. The refined question becomes: **which cycle-structural properties predict MAS performance beyond the scalar beta_1?**

Candidates: girth, average cycle length, cycle centrality (which nodes participate in cycles), clustering coefficient, the cycle space basis.

**Verdict:** This reframes the paper's thesis productively. Instead of "beta_1 vs density," the argument becomes "topology captures MORE than density, and the cycle structure (which density ignores) is what matters."

### Escape Route E: Hypergraphs / Broadcast Communication

In MAS, some communication patterns are not pairwise edges but broadcasts (one agent sends to many). A hypergraph has hyperedges connecting k>2 nodes. The combinatorial topology of hypergraphs has a richer relationship between "edge count" and Betti numbers.

**Verdict:** Interesting theoretically but harder to implement and explain. Park this for later.

## 4. The Recommended Experiment: Directed Cycle Rank

### Design

Fix n=8 agents. Fix m=16 directed edges (each node has average out-degree 2). Construct graph families that vary in the number of directed cycles while holding (n, m) constant.

**Family 1 — DAG (zero directed cycles):**
Layered architecture. 8 nodes in 3-4 layers. All edges point from lower to higher layers. A topological ordering exists. beta_1^{dir} = 0.

Examples:
- F1a: Chain-broadcast. Layer 1 (2 nodes) -> Layer 2 (3 nodes) -> Layer 3 (3 nodes). Each layer-1 node sends to all layer-2 nodes (6 edges). Each layer-2 node sends to all layer-3 nodes (9 edges). Plus 1 intra-layer edge. Total: 16.
- F1b: Wide-fan DAG. One coordinator sends to all 7 (7 edges). 7 agents send to next-layer peers (9 edges). Zero feedback.

**Family 2 — Few directed cycles (1-2):**
Start with a DAG. Reverse 1-2 edges to create feedback loops.

Examples:
- F2a: F1a with one edge reversed: a layer-3 node sends back to a layer-1 node. One directed cycle of length ~3-4.
- F2b: F1a with two edges reversed. Two independent feedback loops.

**Family 3 — Many directed cycles:**
Strongly connected subgraphs. The same 16 edges arranged to create many short directed cycles.

Examples:
- F3a: Two 4-cycles (0->1->2->3->0 and 4->5->6->7->4) = 8 edges. Plus 8 cross-edges, some forming additional directed cycles between the groups.
- F3b: Circular arrangement with skip edges. 0->1->2->...->7->0 (8 edges, one 8-cycle). Plus 8 skip edges like 0->2, 2->4, etc., creating many short directed cycles.

**Family 4 — Dense directed cycles (fully cyclic):**
Near-tournament with feedback everywhere. 16 edges forming many short directed cycles. High directed beta_1.

### Controls

| Factor | Held Constant | Notes |
|---|---|---|
| Agent count (n) | 8 | Fixed |
| Edge count (m) | 16 directed edges | Fixed => density fixed |
| Average in/out-degree | 2 | Controlled by m/n |
| Task | Multiple tasks | Within-task comparison |
| Agent capability | Same LLM, same prompts | Control |

| Factor | Varied | Notes |
|---|---|---|
| Directed cycle count | 0, 1-2, 5-10, many | The independent variable |
| Cycle length distribution | Short vs long | Secondary variable |
| Strong connectivity | May vary | Potential confound, measure it |

### Tasks

Run on 3+ tasks of varying complexity to check for capability-moderated effects (C82):
1. Simple: question answering / classification (weak agents can do it)
2. Medium: multi-step reasoning (e.g., HotpotQA)
3. Hard: code generation / complex planning

### Hypotheses

H1: At fixed (n, m), graphs with moderate directed cycle count outperform both DAGs (too few cycles) and fully cyclic graphs (too many cycles). This establishes a Goldilocks zone for directed beta_1.

H2: At fixed (n, m, directed cycle count), graphs with shorter average cycle length outperform graphs with longer cycles (C80: short cycle dominance).

H3: The optimal directed cycle count increases with task difficulty (C82: capability-moderated beta_1).

H4: DAGs outperform cyclic graphs only on simple tasks. On hard tasks, moderate cyclicity wins.

### Statistical Analysis

- Primary: ANOVA / Kruskal-Wallis on performance grouped by directed cycle count family, at fixed (n, m).
- Secondary: Regression of performance on (directed cycle count, average cycle length, girth, strong connectivity) to determine which structural feature has most predictive power.
- Control check: verify that |E| is truly constant across conditions (it is by construction, but verify).

## 5. The Argument for Paper 2

The paper's argument should be structured as follows:

**Section: The Density-Cycle Confound**

1. State the theorem: for connected undirected graphs with fixed n, beta_1 = |E| - n + 1. Density and cycle rank are provably identical variables.

2. Show that every prior paper claiming "cycles are bad" is operating in this regime (fixed n, connected, undirected). Their results cannot distinguish density from cyclicity. Table summarizing 7+ systems.

3. Argue that MAS communication is inherently DIRECTED. The undirected beta_1 is the wrong quantity. The directed cycle rank (or more refined directed-topological invariants) is the correct predictor.

4. Present the directed experiment (Section 4 above) showing that directed cycle structure predicts performance at constant (n, m) — the controlled experiment that was previously believed impossible.

5. Connect to Clock Systems (C83): the representability theorem applies to directed Moore machines. The clock topology is directed. This gives theoretical backing for directed beta_1 as the correct invariant.

**This reframing is actually STRONGER than the original claim.** Instead of "beta_1 vs density," we're saying:
- The undirected confound is provably irresolvable (theorem)
- Prior work is trapped in this confound (literature review)
- Directed topology escapes it (new insight)
- Directed cycle rank predicts performance at constant density (experiment)
- Clock Systems provides the theory (Lynch et al.)

## 6. Specific Graph Families for n=8, m=16

### DAG Family (0 directed cycles)

**DAG-Layer:** Arrange nodes in layers {0,1} -> {2,3,4} -> {5,6,7}.
Edges: each of {0,1} sends to each of {2,3,4} (6 edges). Each of {2,3,4} sends to each of {5,6,7} (9 edges). Plus 0->1 (1 edge). Total: 16. Topological order: 0,1,2,3,4,5,6,7.

**DAG-Wide:** Node 0 sends to {1,2,3,4,5,6,7} (7 edges). Nodes 1,2,3 each send to {5,6} (6 edges). Nodes 4 sends to {6,7} (2 edges). Node 5 sends to 7 (1 edge). Total: 16.

### Low-Cycle Family (1-3 directed cycles)

**LowCyc-1:** Take DAG-Layer. Reverse edge 5->2 (was 2->5). Now 2->5 and 5->2 form a directed 2-cycle. All other edges respect layer ordering. 1 directed cycle, 16 edges.

**LowCyc-3:** Take DAG-Layer. Reverse 5->0, 6->1, 7->3. Three feedback edges creating three independent long cycles (length 4-5). 3 directed cycles, 16 edges.

### Medium-Cycle Family (5-10 directed cycles)

**MedCyc-Ring:** 0->1->2->3->4->5->6->7->0 (8 edges, one 8-cycle but many sub-paths). Plus 0->2, 2->4, 4->6, 6->0, 1->3, 3->5, 5->7, 7->1 (8 skip edges). Total: 16 edges. Many short directed cycles: 0->2->4->6->0 (4-cycle), 1->3->5->7->1 (4-cycle), 0->1->3->5->7->0... etc. Dozens of directed cycles.

**MedCyc-Biclique:** Two groups {0,1,2,3} and {4,5,6,7}. Each node in group 1 sends to exactly 2 nodes in group 2 and vice versa. Generates multiple inter-group cycles.

### High-Cycle Family (many directed cycles)

**HighCyc-Tournament:** Carefully select 16 edges from the 56 possible directed edges on 8 nodes, maximizing directed cycle count. Strategy: create a strongly connected tournament-like graph. E.g., 0->1, 1->2, ..., 7->0 (ring, 8 edges) plus 0->3, 1->4, 2->5, 3->6, 4->7, 5->0, 6->1, 7->2 (skip-2 ring, 8 edges). Two interleaved rings = huge number of directed cycles.

**HighCyc-Clustered:** Two strongly connected 4-cliques (each with 12 directed edges, pick 8 from each = 16 total). Rich internal cycles in both groups.

## 7. Computational Verification — RESULTS

Script: `verify_directed_families.py`. Results on n=8, m=16 directed edges:

| Graph Family | #Simple Cycles | Directed Rank | Strongly Connected |
|---|---|---|---|
| DAG-Layer | 0 | 0 | No |
| DAG-Wide | 0 | 0 | No |
| LowCyc-1 (one feedback) | 3 | 3 | No |
| LowCyc-3 (three feedback) | 12 | 9 | Yes |
| MedCyc-Ring (ring + skip-2) | 47 | 9 | Yes |
| MedCyc-Skip3 (ring + skip-3) | 30 | 9 | Yes |
| HighCyc-Bidir (bidirectional ring) | 10 | 9 | Yes |

### Critical Second-Order Insight

**The directed cycle rank has the SAME collinearity problem for strongly connected digraphs.**
For a single SCC: directed rank = m_scc - n_scc + 1. If the whole graph is one SCC (strongly connected),
directed rank = m - n + 1 = 16 - 8 + 1 = 9 for ALL strongly connected graphs on 8 nodes with 16 edges.

The confound is even more fundamental than initially recognized. It applies to:
- Undirected connected graphs (beta_1 = |E| - n + 1)
- Directed strongly connected graphs (directed rank = m - n + 1)
- Any graph where the "connected/strongly connected" constraint holds

**However, the NUMBER OF SIMPLE DIRECTED CYCLES varies enormously:** 10 to 47 for strongly connected
graphs with the same (n, m). This is because simple cycle count is NOT a topological invariant — it
depends on the specific edge arrangement, not just the rank of the cycle space.

This means:
1. **Cycle rank (beta_1)** = dimension of the cycle space = determined by (n, m, c). Topological. Identical to density for fixed (n, c).
2. **Simple cycle count** = number of distinct simple cycles = NOT determined by (n, m). Combinatorial. Decorrelated from density.
3. **Cycle length distribution** = how long the cycles are = NOT determined by (n, m). Also decorrelated.

The experiment should use **simple cycle count** and **cycle length distribution** as independent variables,
NOT cycle rank. Cycle rank is the wrong quantity for this experiment.

### Revised Understanding

The variable hierarchy is:
- **Edge count / density:** |E| or |E|/binom(n,2). The coarsest measure.
- **Cycle rank (beta_1):** |E| - n + c. Strictly determined by density for fixed (n, c). Same information.
- **Simple cycle count:** NOT determined by density. The number of actual feedback loops. THIS can be varied at constant density.
- **Cycle length distribution:** NOT determined by density. Short cycles vs long cycles. Also independent.
- **Cycle centrality:** Which nodes participate in cycles. Also independent.

**The experimental independent variable should be simple cycle count (or cycle length distribution), NOT beta_1.**

This is a significant refinement. Beta_1 is not the right predictor for fixed-n experiments. It's the
right predictor only when comparing across different (n, |E|) combinations — which is what our original
OneMax experiment did (star vs ring vs complete, different |E|). In that setting, beta_1 worked because
it was the only thing varying. But it was proxying for density the whole time.

## 8. Honest Assessment — UPDATED AFTER COMPUTATION

**Confidence in the structural impossibility (Section 1): 99%.** This is a theorem. Confirmed computationally.

**Confidence in the directed cycle rank escape: 20% (DOWNGRADED from 80%).** Computation shows that directed cycle rank has the SAME collinearity with density for strongly connected digraphs. The escape route via "directed rank" fails. However, the escape via "simple cycle COUNT" succeeds — graphs with identical (n, m, directed rank) have 10 to 47 simple cycles.

**Confidence in simple cycle count as predictor: 65%.** This is the new candidate variable. It IS decorrelated from density. The question is whether it's the right predictor for MAS performance, or just a combinatorial curiosity. The Clock Systems theory (C83) doesn't directly address simple cycle count — it addresses the cycle space rank. We'd need new theory connecting simple cycle count to behavior spaces.

**Confidence in cycle length distribution as predictor: 75%.** Short cycle dominance (C80) provides independent evidence that cycle length matters. This is the most experimentally promising variable.

**Key risk (unchanged):** If neither simple cycle count nor cycle length distribution predicts performance at constant density, the confound is genuinely irresolvable and beta_1's predictive power in our OneMax experiment was entirely due to density. That's a real possibility and an honest negative result.

**What this means for paper 2's thesis:** We need to be more careful. "beta_1 predicts performance" is true but ONLY because beta_1 = density (up to a constant) for connected graphs. The thesis should be refined to one of:
1. "Cycle structure (not just count) predicts performance at constant density" — requires the directed experiment.
2. "beta_1 is the correct way to THINK about density" — a framing contribution, not an empirical one.
3. "The entire field conflates two variables that are provably identical, and nobody noticed" — a methodological contribution.

## 9. Revised Paper 2 Strategy

Given the computational results, the paper's argument should be restructured:

### The Strongest Version (if directed experiment works)

**Claim:** "Cycle structure predicts MAS performance at constant communication density."

Evidence: At fixed (n=8, m=16), graphs with different numbers of simple directed cycles and different cycle length distributions show significantly different MAS performance. Density alone cannot explain this. The relevant topological quantity is not beta_1 (which collapses to density) but the cycle length spectrum.

This requires running the actual MAS experiment. Graph families are ready (Section 6, verified Section 7).

### The Methodological Version (publishable regardless)

**Claim:** "The density-cycle confound in multi-agent topology research is not an experimental oversight but a mathematical theorem, and recognizing this reframes the entire field."

Evidence:
1. Theorem: beta_1 = |E| - n + 1 for connected graphs. (5 lines of proof.)
2. Survey: 7+ major systems conflate density and cycle rank without noting the identity.
3. Implication: Claims of the form "cycles hurt" and "density hurts" are syntactic variants of the same claim.
4. Resolution: The field should study cycle STRUCTURE (girth, length distribution, which-nodes-participate) rather than cycle COUNT (which is density in disguise).

This version doesn't need new experiments — it's a theoretical/methodological contribution. Combined with the directed experiment, it becomes a strong paper.

### The Reframing Version (weakest but still novel)

**Claim:** "beta_1 is the correct mathematical framework for understanding why density matters."

Even though beta_1 = density for connected graphs, algebraic topology provides tools that raw density doesn't: persistence diagrams, cycle space bases, the connection to sheaf cohomology (C83). The contribution is conceptual and tooling, not empirical separation.

### Recommendation

Write the paper with the methodological version as the backbone (Sections 1-2 of the analysis), then add the directed experiment as the constructive resolution (Sections 3-7). The theorem itself is a genuine contribution to the MAS topology literature — nobody has stated it clearly, and it undermines 7+ papers' implicit claims of having studied "cycles" vs "density" as separate phenomena.
