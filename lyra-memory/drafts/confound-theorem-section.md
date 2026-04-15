# The Density-Cycle Confound

> Draft: April 3, 2026. Paper 2, Section 3 (theoretical core).
> Target: ACM workshop style, ~2000 words. LaTeX notation inline; equations marked for typesetting.

---

## 3. The Density-Cycle Confound

The central empirical claim of our prior work [paper 1] and of the broader MAS topology literature is that *cycle rank* (the first Betti number, beta\_1) predicts system performance. In this section we show that for connected undirected graphs with fixed node count --- the regime in which nearly all published experiments operate --- this claim is mathematically equivalent to the claim that *edge density* predicts performance. We prove the identity, survey the literature it implicates, and then show how directed graph structure provides a genuine escape from the confound.

### 3.1 The Theorem

<!-- EQUATION: Theorem 1 -->
**Theorem 1** (Cycle rank--density identity). *Let G = (V, E) be a connected graph with |V| = n vertices and |E| = m edges. Then the first Betti number (cycle rank) of G is*

    beta_1(G) = m - n + 1.

*Proof sketch.* A connected graph on n vertices has a spanning tree with exactly n - 1 edges. Each of the remaining m - (n - 1) edges, when added to the spanning tree, creates exactly one independent cycle. The cycle space of G therefore has dimension m - n + 1 over GF(2) (or equivalently over the integers, since the graph is 1-dimensional). This is a standard result from algebraic topology: for a connected simplicial complex of dimension 1, the first Betti number equals |E| - |V| + 1 by the Euler characteristic formula chi = |V| - |E| = 1 - beta_1.  QED.

The theorem is elementary. Its implications for the multi-agent systems literature are not.

<!-- EQUATION: Corollary 1 -->
**Corollary 1** (Collinearity). *For connected graphs with fixed vertex count n, beta_1 and edge count m are related by a constant offset: beta_1 = m - (n - 1). Therefore, any statistical correlation between beta_1 and a performance metric Y is algebraically identical to the correlation between m (or equivalently, edge density d = m / C(n, 2)) and Y. The Pearson correlation coefficients satisfy rho(beta\_1, Y) = rho(m, Y) exactly.*

*Proof.* If beta_1 = m - c for a constant c = n - 1, then beta_1 is an affine transformation of m. Pearson correlation is invariant under affine transformations of either variable.  QED.

The force of this corollary is methodological: **any experiment comparing connected topologies on a fixed number of agents cannot distinguish between "cycles help/hurt" and "more/fewer edges help/hurt."** These are the same claim in different notation. The rho = 0.893 correlation between beta\_1 and OneMax fitness reported in our prior work [paper 1] is, for that experimental design, identically a correlation between edge count and fitness.

This is not a weakness of beta\_1 as an invariant. It is a structural impossibility of the experimental regime. Recognizing it is the first step toward escaping it.

### 3.2 The DAG Hegemony: A Survey of Conflating Papers

The beta\_1 = 0 constraint --- enforcing a directed acyclic graph (DAG) on agent communication --- has become the default in multi-agent system design. We surveyed seven recent systems that impose this constraint. In every case, the topology choice conflates cycle elimination with density reduction, and none hold density constant while varying cycle structure.

<!-- TABLE: DAG hegemony survey -->

**GoAgent** (2024). Organizes agents into a hierarchical structure with a Cooperative Information Bottleneck (CIB) objective. Claims the DAG structure prevents "message loops" and enables tractable optimization. In practice, comparing the DAG to a densely connected alternative simultaneously varies beta\_1 and edge count. The CIB result is a density result.

**AgentConductor** (2025). Uses an LLM-based meta-controller to assign agents to a pipeline. Constrains communication to a sequential chain (beta\_1 = 0, m = n - 1). Reports that "simple pipelines outperform complex graphs," but the "complex graphs" have both more cycles *and* more edges. The comparison is confounded by construction.

**Graph-GRPO** (2025). Trains a 3-layer graph attention network to learn agent topologies via group relative policy optimization. Despite learning the topology end-to-end, constrains the output to DAGs. The learned graphs are evaluated against complete graphs (maximum density, maximum beta\_1) and star topologies (minimum beta\_1, moderate density). Neither baseline controls for density.

**OFA-MAS** (2025). A one-for-all multi-agent architecture that prunes communication edges for efficiency. The pruning reduces both density and cyclicity simultaneously. Reports gains from "sparse communication," which is correct --- but the cycle-rank reduction is a mathematical consequence of the sparsification, not an independent finding.

**G-Designer** (2025). Proposes a graph-based agent topology design framework. Evaluates against fixed topologies (complete, ring, star, chain) that span the full range of both density and beta\_1. Concludes that "moderately connected" topologies outperform dense ones. This is consistent with our framework but does not isolate cycles from density.

**ARG-Designer** (2025). Extends G-Designer with adaptive reconfiguration. Finds that complete graphs (maximum density/beta\_1) perform worst. The complete graph is simultaneously the densest *and* most cyclic topology on n nodes, making attribution impossible.

**Dochkina et al.** (2025). The most rigorous study in our survey: 25,000 runs across multiple tasks, agent counts, and capability levels. Reports that "sparse beats dense" as a general finding, with capability moderation (weak agents prefer sparser topologies). However, sparsity and acyclicity are confounded throughout. The finding that weak agents prefer sparse/acyclic topologies and strong agents tolerate denser/more cyclic ones (Connection C82) may be a density effect, a cycle effect, or both --- the experimental design cannot distinguish them.

**Summary.** None of these seven systems hold edge density constant while varying cycle structure. By Theorem 1, they cannot. Any connected undirected topology on n nodes with m edges has beta\_1 = m - n + 1; there is no degree of freedom left to vary. The field's consensus that "DAGs are better" is, in the connected undirected regime, indistinguishable from the claim that "sparser graphs are better." Both may be true, but they have not been tested independently.

### 3.3 The Directed Escape

The impossibility established in Theorem 1 holds only for undirected graphs (or, more precisely, for homological cycle rank). Multi-agent communication, however, is inherently *directed*: agent A sends a message to agent B, but B need not respond to A. This asymmetry provides the escape route.

For directed graphs, the cycle rank of the underlying undirected skeleton still obeys the same formula. And for strongly connected digraphs, the directed cycle rank (dimension of the directed cycle space) is also m - n + 1, reproducing the collinearity. **However, the number of simple directed cycles is not determined by (n, m).** Simple cycle count is a combinatorial, not topological, quantity --- it depends on the specific arrangement of edges, not just the rank of the cycle space.

This distinction is critical. Consider two directed graphs on n = 8 nodes with m = 16 directed edges:

<!-- TABLE: Directed cycle count variation -->

| Graph Family | Simple Directed Cycles | Strongly Connected |
|---|---|---|
| DAG-Layer (3-layer hierarchy) | 0 | No |
| DAG-Wide (fan-out hierarchy) | 0 | No |
| LowCyc-1 (one feedback edge) | 3 | No |
| LowCyc-3 (three feedback edges) | 12 | Yes |
| MedCyc-Ring (ring + skip-2) | 47 | Yes |
| MedCyc-Skip3 (ring + skip-3) | 30 | Yes |
| HighCyc-Bidir (bidirectional ring) | 10 | Yes |

These counts were obtained by computational enumeration (Johnson's algorithm for simple cycle detection). All seven graphs have the same node count (8) and the same directed edge count (16). For the four strongly connected graphs, the directed cycle rank is identical: 16 - 8 + 1 = 9. Yet the number of simple directed cycles ranges from 10 to 47 --- a 4.7x variation at constant density and constant cycle rank.

This variation is not an artifact. It reflects genuinely different communication structures: the ring-with-skip-2 graph contains many short feedback loops (3-cycles and 4-cycles formed by the interleaving of ring and skip edges), while the bidirectional ring has longer, sparser cycles. These structural differences are invisible to density, invisible to beta\_1, and invisible to directed cycle rank --- but they are precisely the differences that matter for information propagation in a multi-agent system.

**The experimental consequence is immediate.** We can now construct graph families that hold (n, m) constant --- and therefore hold density constant --- while varying the number and length distribution of simple directed cycles. This is the controlled experiment that the undirected confound made impossible. The independent variables become:

- **Simple directed cycle count:** the number of distinct simple directed cycles (decorrelated from density by construction).
- **Cycle length distribution:** mean and variance of cycle lengths. Short cycles (length 2--4) enable rapid feedback; long cycles (length 6+) create slow information mixing.
- **Cycle centrality:** the fraction of nodes participating in at least one directed cycle. A graph can have many cycles concentrated in a small subgraph, or distributed uniformly.

We defer the full experimental design to Section 4. The key theoretical point is that the directed regime breaks the collinearity that makes undirected experiments uninterpretable.

### 3.4 Reframing: What beta_1 Actually Captures

The density-cycle confound does not invalidate beta\_1 as a conceptual framework. It clarifies its role.

For connected undirected graphs, beta\_1 counts *surplus edges* --- edges beyond the n - 1 required for a spanning tree. The first n - 1 edges in any spanning tree construction are *tree edges*: they reduce disconnection and build connectivity. Every subsequent edge is a *cycle edge*: it creates an alternative path between already-connected nodes, introducing redundancy, feedback potential, and topological complexity. Raw edge count m conflates these two qualitatively different roles. Beta\_1 isolates the cycle edges, making the tree-to-cyclic phase transition at beta\_1 = 0 --> 1 explicit.

This phase transition explains anomalies that density alone cannot. The Star topology on n = 8 nodes has m = 7 edges and beta\_1 = 0. It is a tree: maximally efficient at connecting nodes (every node is within distance 2 of every other) but devoid of redundancy. A single hub failure is catastrophic. The Ring on n = 8 has m = 8 edges and beta\_1 = 1 --- one more edge, one cycle. Spectral methods rate the Star higher (algebraic connectivity lambda\_2 = 1.0 vs. lambda\_2 approximately 0.59 for the Ring), yet in production multi-agent systems, the Star's single point of failure led to a $47K cost overrun from a failure loop that the Ring's redundant path would have prevented [paper 1, Section 5]. Beta\_1 correctly predicts this: beta\_1 = 0 means zero redundancy, regardless of how well-connected the graph appears spectrally.

The correct reframing is therefore:

1. **For cross-topology comparisons** (varying both n and m, or varying connectivity class), beta\_1 remains the natural parameter. It captures the homological structure that density obscures. It is the basis for persistent homology, sheaf cohomology over communication graphs (cf. Lynch et al., Clock Systems), and the operad-theoretic framework of Section 2.

2. **For fixed-n connected experiments** (the regime of nearly all published MAS topology papers), beta\_1 is density in a topologically informative parameterization. It is not "wrong," but it cannot be claimed to capture anything beyond density in this regime. Claims to the contrary are mathematical errors.

3. **For directed communication graphs** (the regime that actually matches MAS practice), the operative variables are simple directed cycle count and cycle length distribution, which are decorrelated from density. This is where the field's open questions live, and where controlled experiments are possible for the first time.

The density-cycle confound is not an embarrassment for the cycle rank framework. It is a clarification that the field urgently needs --- and the directed escape provides the constructive path forward.

---

> **Word count:** ~2050. Equations marked with `<!-- EQUATION -->` comments for LaTeX typesetting. Tables marked with `<!-- TABLE -->` comments. References to [paper 1] and [Lynch et al., Clock Systems] are placeholders for proper citations.
