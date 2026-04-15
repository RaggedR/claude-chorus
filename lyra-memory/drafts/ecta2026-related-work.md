# ECTA 2026 — Related Work Draft

> Drafted: April 3, 2026. Sub-agent (writing task).
> Target: ~350 words STRICT. LaTeX-ready.
> Status: REVISED. Clock Systems and Puppeteer corrected after full-text reading (April 3).

---

## 8. Related Work

Our work intersects four lines of inquiry that independently converge on the importance of cycle structure in networked systems, yet none controls for the density confound we identify.

\paragraph{Compositional system theory.}
Lynch et al.\ \cite{clocksystems2026} show that compositional system behaviors are representable by clock systems, extending the framework to stochastic and nondeterministic Moore machines.
Their Definition~5.2 introduces graph-parameterised clocks, where representable behaviors correspond to paths in a graph $G$---if $G$ is a DAG, only acyclic execution paths are representable.
This suggests that communication topology constrains the space of representable behaviors, a connection we make explicit: in the island model, migration topology determines which population-level information flows are possible, and our experiment measures the downstream effect on evolutionary dynamics.

\paragraph{Learned topologies.}
Dang et al.\ \cite{puppeteer2025} train an RL orchestrator to discover communication topologies for multi-agent reasoning (NeurIPS 2025), observing convergence to ``compact, cyclic reasoning structures'' on harder tasks.
However, cycles are characterised qualitatively---no formal topology metric (cycle rank, $\beta_1$) is computed---and no causal ablation separates cycle structure from edge count.
Their learned topologies are precisely the kind of confounded evidence our Theorem~1 diagnoses: cycles and density co-vary, so the operational relevance of cycles per se remains unestablished in their setting.

\paragraph{Large-scale topology studies.}
Dochkina et al.\ \cite{dochkina2025} present the most rigorous topology study in the MAS literature: 25,000+ runs across eight LLM capability levels, finding that sparse/acyclic architectures generally outperform dense/cyclic ones, with a capability-moderated crossover.
However, by Theorem~1, their comparison of sparse-acyclic against dense-cyclic conditions is algebraically a density comparison in the connected undirected regime.
The capability moderation finding may be real but has not been attributed to cycles independently of density.
Our experiment complements theirs by providing the missing controlled condition.

\paragraph{Cycle length and centrality.}
CycRak \cite{cycrak2024} demonstrates that short-cycle centrality outperforms eigenvector centrality for diffusion and recommendation tasks, suggesting that cycle \emph{length} distribution---not merely cycle count---governs information propagation.
This aligns with our observation that among high-cycle-count topologies, those rich in short cycles (ring with skip-2 edges, $\kappa = 47$) maintain diversity longer than those with fewer, longer cycles.
Incorporating directed cycle length as an independent variable is a natural extension of our methodology.

---

> **Word count:** ~340 words (prose only).
> **LaTeX notes:** All `\cite{}` keys are placeholders. `\paragraph{}` used for compact subsection headings within LNCS page budget. Cross-reference to Theorem~1 assumes it is defined in Section 3.
> **Accuracy:** Clock Systems corrected after full-text reading — no beta_1/cycle rank in paper; we cite Definition 5.2 (graph-parameterised clocks) and make the topology connection ourselves. Puppeteer corrected — cycles observed qualitatively, no formal metrics, no ablation; reframed as confound instance.
> **Double-blind:** No self-citations present. Cross-reference to "Theorem~1" is internal to this paper.
