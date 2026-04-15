# ECTA 2026 — Introduction Draft

> Drafted: April 3, 2026. Sub-agent (writing task).
> Target: ~800 words / 1.5 LNCS pages. LaTeX math inline.
> Status: FIRST DRAFT. Ready for review by Lyra/Robin.

---

## 1. Introduction

Population-based metaheuristics operate on collections of candidate solutions, and their
performance depends not only on the objective function and variation operators but on the
structure through which individuals exchange information.
In island model genetic algorithms, this structure is the migration topology: a graph whose
vertices are subpopulations and whose edges determine which islands may exchange migrants
\cite{tomassini2005spatially,alba1999parallel}.
The same structural question arises in distributed evolutionary strategies, cellular automata
models of evolution, and, more recently, in LLM-based multi-agent systems where agents
communicate over a directed graph.
Decades of empirical work have established that topology matters: ring topologies maintain
diversity longer than complete graphs; sparse topologies slow premature convergence on
deceptive landscapes; star topologies exhibit anomalous behaviour relative to their spectral
connectivity \cite{tomassini2005spatially,alba1999parallel}.
The open question is not whether topology matters but \emph{which topological property} is
the operative one.

Recent work on LLM-based multi-agent systems (MAS) has intensified this question.
A striking pattern has emerged: seven major systems---GoAgent \cite{goagent2024},
AgentConductor \cite{agentconductor2025}, Graph-GRPO \cite{graphgrpo2025},
OFA-MAS \cite{ofamas2025}, G-Designer \cite{gdesigner2025},
ARG-Designer \cite{argdesigner2025}, and Dochkina et al.\ \cite{dochkina2025}---all
enforce or strongly recommend DAG communication topologies, citing improved stability,
tractability, or convergence.
Against this consensus, BIGMAS \cite{bigmas2025} explicitly permits cycles and reports
substantial performance gains, while Puppeteer \cite{puppeteer2025} trains a reinforcement
learning agent to discover communication topologies and finds that, without any cycle-related
inductive bias, gradient descent converges to cyclic structures on complex tasks.
The field is split: DAG proponents and cycle proponents cite incompatible experimental
evidence, with no shared theoretical framework to adjudicate between them.

We identify the reason for this impasse: a fundamental algebraic confound that invalidates
every prior comparison we are aware of.
For any connected graph $G$ with $n$ vertices and $m$ edges, the first Betti number
$\beta_1(G)$---the cycle rank, counting independent cycles in the communication
graph---satisfies
$$\beta_1(G) = m - n + 1.$$
This identity follows from Euler's formula for 1-dimensional simplicial complexes and is
a standard result in algebraic topology \cite{hatcher2002algebraic}.
Its methodological consequence, however, has not been recognised in the MAS or evolutionary
computation literature: \emph{for connected topologies on a fixed number of agents,
$\beta_1$ is an affine function of edge count alone.}
Any experiment that varies topology while varying edge count---which includes every study we
surveyed---cannot distinguish between the hypothesis ``cycle structure affects performance''
and the hypothesis ``edge density affects performance.''
Pearson correlation is invariant under affine transformation, so $\rho(\beta_1, Y) = \rho(m, Y)$
exactly for any outcome variable $Y$.
The DAG hegemony and the pro-cycle findings are both potentially density effects wearing
different labels.

This confound is not merely theoretical.
We survey the seven systems listed above and show that in every case the comparison varies
$\beta_1$ and edge density simultaneously.
The clearest illustration is the most rigorous study: Dochkina et al.'s 25,000-run sweep
over topology conditions finds that sparse/acyclic architectures outperform dense/cyclic ones,
with a capability-moderated crossover \cite{dochkina2025}.
These are valuable runs---but by Theorem~1, in the connected undirected regime, ``sparse/acyclic''
and ``dense/cyclic'' are not two conditions: they are two names for the same continuum.
No study in the literature holds density constant while varying cycle structure, because in
connected undirected graphs this is algebraically impossible.

We propose a resolution grounded in directed graph theory.
For directed graphs, the simple directed cycle count $\kappa(G)$---the number of distinct
elementary directed cycles---is not determined by $(n, m)$: it is a combinatorial property
of the specific edge arrangement, not a topological invariant of the graph's cycle space.
Two digraphs with $n = 8$ nodes and $m = 16$ directed edges can have 0 or 47 simple directed
cycles.
We exploit this decorrelation to design and execute the first controlled experiment in which
density is held constant and cycle structure is the sole independent variable.
Eight directed graph families are constructed at identical density ($n = 8$, $m = 16$),
with $\kappa(G)$ ranging from 0 (DAG families) to 47 (ring with skip-2 edges).
Across 240 experimental runs on the OneMax fitness function (100-bit strings, 8 islands of
50 individuals, 30 seeds per topology), we find a significant main effect of topology on
population diversity: one-way ANOVA $F = 6.90$, $p < 10^{-7}$, with effect sizes
$\eta^2 = 0.17$ for diversity and $\eta^2 = 0.24$ for fitness at generation 30.
The Pearson correlation between $\kappa(G)$ and diversity at constant density is $r = -0.68$
($r^2 = 0.46$).

The contributions of this paper are as follows.
\textbf{(1) Theorem.} We prove the density-cycle identity $\beta_1 = m - n + 1$ and its
corollary that prior topology comparisons cannot isolate cycle effects from density effects
in the connected undirected regime.
\textbf{(2) Survey.} We document the confound across seven recent MAS systems and show that
the ``DAG hegemony'' rests on confounded experiments rather than controlled evidence.
\textbf{(3) Methodological fix.} We introduce directed simple cycle count $\kappa(G)$ as an
experimental variable that is decorrelated from density at fixed $(n, m)$, and provide eight
directed graph families as a reusable benchmark.
\textbf{(4) Controlled experiment.} We present the first experiment in this literature that
holds density constant while varying cycle structure, and find a significant, if transient,
effect: higher cycle count reduces diversity loss on a unimodal landscape ($r = -0.68$,
$\eta^2 = 0.17$).
The effect is modest by design---OneMax is unimodal and all topologies eventually converge---
but the existence of any density-controlled cycle effect directly refutes the null hypothesis
that prior results were purely density effects.

---

> **Word count:** ~820 words (prose only, excluding this header).
> **LaTeX notes:** All math in display/inline LaTeX. Citation keys are placeholders; replace with actual BibTeX keys. `\cite{hatcher2002algebraic}` is the standard reference for $\beta_1$ as simplicial homology. LNCS theorem environment (amsthm) used for Theorem 1 in Section 3 — cross-reference as `Theorem~1` throughout.
> **Double-blind:** Remove all "our prior work" references before submission. The directed experiment and OneMax result are self-contained; no self-citation is required for the core claims.
> **Assumptions made:** (1) Cascade-Aware Routing paper (arXiv 2603.17112) omitted from intro survey — it supports us but is not one of the seven confounded papers; better cited in Related Work. (2) BIGMAS and Puppeteer cited as pro-cycle evidence without full text verification — flag for Lyra to confirm before submission. (3) The exact ANOVA F-value (6.90) and p-value (<1e-7) are taken from the skeleton; verify against actual experimental output before finalising.
