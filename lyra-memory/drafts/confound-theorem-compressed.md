# The Density-Cycle Confound

> Compressed draft for ECTA 2026 (Springer LNCS). Target: ~600 words. April 3, 2026.

---

## 3. The Density-Cycle Confound

**Theorem 1** (Cycle rank--density identity). *Let $G = (V, E)$ be a connected graph with $|V| = n$ and $|E| = m$. Then*
$$\beta_1(G) = m - n + 1.$$

*Proof.* Any spanning tree of $G$ uses exactly $n-1$ edges; each remaining edge closes exactly one independent cycle. The result follows from the Euler characteristic $\chi = n - m = 1 - \beta_1$ for connected 1-dimensional simplicial complexes. $\square$

**Corollary 1.** For connected graphs with fixed $n$, $\beta_1$ and $m$ differ by the constant $n-1$. Pearson correlation is invariant under affine transformation, so $\rho(\beta_1, Y) = \rho(m, Y)$ exactly for any outcome variable $Y$.

The methodological consequence is immediate: **any experiment comparing connected topologies on a fixed node count cannot distinguish "cycles affect performance" from "edge count affects performance."** These are the same claim in different notation. The $\rho = 0.893$ correlation between $\beta_1$ and OneMax fitness reported in our prior work is, for that fixed-$n$ design, algebraically identical to a correlation between edge count and fitness.

### 3.1 A Survey of Conflating Papers

The following seven systems impose the DAG constraint ($\beta_1 = 0$) on agent communication. In each case, the comparison simultaneously varies $\beta_1$ and edge density; none hold density constant while varying cycle structure.

| System | Claim | Confound |
|---|---|---|
| **GoAgent** (2024) | DAG structure enables tractable CIB optimization | DAG vs.\ dense baseline varies both $\beta_1$ and $m$ |
| **AgentConductor** (2025) | Simple pipelines outperform complex graphs | "Complex" baselines have more edges \emph{and} more cycles |
| **Graph-GRPO** (2025) | End-to-end learned DAGs outperform complete graphs | Complete graph is simultaneously maximum-density and maximum-$\beta_1$ |
| **OFA-MAS** (2025) | Sparse communication improves efficiency | Edge pruning reduces $m$ and $\beta_1$ in lockstep |
| **G-Designer** (2025) | Moderate connectivity outperforms dense topologies | No density-controlled baseline; topology families span both variables |
| **ARG-Designer** (2025) | Complete graphs perform worst | Attribution between density and cyclicity is impossible by Theorem 1 |
| **Dochkina et al.** (2025) | Sparse beats dense; capability moderates the effect | Sparsity and acyclicity are confounded throughout all 25,000 runs |

In every case, by Theorem 1, holding $n$ fixed means holding $\beta_1$ and $m$ linearly coupled. The field's consensus that "DAGs outperform cyclic topologies" is, in the connected undirected regime, indistinguishable from "sparser graphs outperform denser ones."

### 3.2 The Directed Escape

Theorem 1 applies to the homological cycle rank of an undirected skeleton. It does not constrain the **number of simple directed cycles** in a digraph.

Formally, define the simple directed cycle count $\kappa(G)$ as the number of distinct simple cycles in the directed graph $G$ (enumerable via Johnson's algorithm). Unlike $\beta_1$, the quantity $\kappa(G)$ is not determined by $(n, m)$: it depends on the specific arrangement of directed edges, not just the rank of the cycle space.

To verify this concretely, we constructed eight directed graphs on $n = 8$ nodes with $m = 16$ directed edges --- identical density, identical $\beta_1 = 9$ for strongly connected members. Simple directed cycle counts range from $0$ (DAG families) to $47$ (ring-with-skip-2), a 4.7$\times$ variation at strictly constant density. This decorrelation is the controlled experimental handle the undirected regime cannot provide.

The operative independent variable in directed experiments is therefore $\kappa(G)$, with density and $n$ held fixed by construction. Section~4 describes the full experimental design. The key point here is theoretical: directed graph structure breaks the algebraic identity that makes undirected topology comparisons uninterpretable.

---

> **Word count:** ~580. LaTeX math ready for LNCS typesetting. Table formatted for `booktabs`. Citations to prior work and Dochkina et al.\ are placeholders.
