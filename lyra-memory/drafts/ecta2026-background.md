# ECTA 2026 — Section 2: Background

> Drafted: April 3, 2026. Sub-agent (writing task).
> Target: ~400 words. LaTeX math inline.
> Status: FIRST DRAFT. Ready for review by Lyra/Robin.

---

## 2. Background

### 2.1 Island Model Evolutionary Algorithms

In island model evolutionary algorithms, a population is partitioned into
semi-isolated subpopulations (islands) that evolve independently and exchange
individuals periodically via migration~\cite{tomassini2005spatially,alba1999parallel}.
The \emph{migration topology} is a graph $G = (V, E)$ whose vertices are islands
and whose edges (or arcs, in the directed case) determine which islands may
exchange migrants.
Early work established that topology affects the balance between exploration and
exploitation: sparse topologies (rings, ladders) slow the spread of fit
individuals, maintaining diversity longer, while dense topologies (complete
graphs) accelerate convergence but risk premature
loss of diversity on multimodal
landscapes~\cite{alba2002parallel,skolicki2005influence}.
The question motivating this paper is not whether topology matters---it
demonstrably does---but which \emph{topological property} drives the effect.

### 2.2 Cycle Rank and the First Betti Number

For a graph $G = (V, E)$ with $|V| = n$ vertices, $|E| = m$ edges, and $c$
connected components, the \emph{first Betti number} (cycle rank) is
\begin{equation}
  \beta_1(G) \;=\; m - n + c.
  \label{eq:betti}
\end{equation}
For connected graphs ($c = 1$), this simplifies to $\beta_1 = m - n + 1$.
Geometrically, $\beta_1$ counts the number of independent cycles: a spanning
tree uses $n - 1$ edges, and each additional edge closes exactly one cycle that
is linearly independent (over $\mathrm{GF}(2)$) of all
others~\cite{hatcher2002algebraic}.
A tree has $\beta_1 = 0$; adding $k$ edges beyond the spanning tree yields
$\beta_1 = k$.
Prior work has used $\beta_1$ as a predictor of island model performance,
reporting strong correlations between cycle rank and both fitness convergence
rate and diversity retention [ANON].
However, as we show in Section~3, these correlations are algebraically
indistinguishable from density effects.

### 2.3 Directed Graphs and Simple Cycle Count

A directed graph (digraph) $D = (V, A)$ has arcs (ordered pairs) rather than
edges.
We define the \emph{simple directed cycle count} $\kappa(D)$ as the number of
distinct elementary directed cycles in $D$---cycles that visit each vertex at
most once.
Unlike $\beta_1$, which for connected graphs is determined entirely by $n$ and
$m$, the quantity $\kappa(D)$ depends on the specific arrangement of arcs.
Two digraphs with the same $n$ and $|A|$ can have vastly different values of
$\kappa$.
Enumeration is performed via Johnson's
algorithm~\cite{johnson1975finding} in $O((|V| + |A|)(C + 1))$ time, where $C$
is the number of cycles found.
This combinatorial freedom is what makes controlled experiments possible, as we
exploit in Section~4.

---

> **Word count:** ~370 words (prose only, excluding headers and this note).
> **LaTeX notes:** All math in display/inline LaTeX. Citation keys are placeholders; replace with actual BibTeX keys during assembly. `[ANON]` marks a self-citation requiring double-blind treatment.
> **Design note:** Section 2.3 is kept brief because Section 3.2 (The Directed Escape) provides the full formal treatment and the decorrelation argument. This subsection establishes only the definition and the key property ($\kappa$ is not determined by $(n, |A|)$) so that Section 3 can reference it without a forward-definition problem.
