# ECTA 2026 — Discussion and Conclusion

> Drafted: April 3, 2026. Sub-agent (writing task).
> Target: Discussion ~400 words, Conclusion ~150 words. LaTeX-ready.

---

## 7. Discussion

The directed cycle experiment establishes that cycle count independently predicts island model GA behaviour at constant density. This is a narrow but consequential result: it means the confound identified by Theorem~1 is not merely a theoretical curiosity but has masked a real structural effect. When density is controlled, directed cycle count $\kappa(G)$ explains 17\% of diversity variance and 24\% of fitness variance at generation~30. These are medium-to-large effects by Cohen's thresholds, and they emerge on OneMax --- a landscape deliberately chosen to be easy.

The temporal profile of the effect deserves careful interpretation. The correlation between $\kappa(G)$ and diversity peaks in the window from generation~20 to generation~50, then decays toward zero by generation~100. We interpret this as \emph{cycle-mediated exploration}: feedback loops in the communication topology slow the propagation of dominant alleles across islands, extending the period during which subpopulations maintain independent search trajectories. On a unimodal landscape, this exploration phase is eventually overwhelmed by selection pressure driving all islands toward the global optimum. The effect is therefore a rate effect --- cycles delay convergence rather than alter the eventual outcome.

This transience is a feature of the experimental design, not a weakness. OneMax has no local optima; premature convergence is not a failure mode but merely a speed difference. On deceptive or multimodal landscapes, where premature convergence causes genuine performance loss, the same cycle-mediated exploration mechanism is predicted to yield larger and more sustained effects. If cycles extend diversity on an easy landscape, they should matter more on a hard one. Testing this prediction on NK landscapes ($k \geq 3$) and trap functions is the most important next step.

The implications for multi-agent system design are immediate. The seven systems surveyed in Section~3 all concluded that DAGs outperform cyclic topologies, but by Theorem~1 their experiments compared sparse graphs to dense ones. The correct conclusion from their data is that \emph{sparser communication is cheaper}, not that cycles are harmful. Our controlled experiment provides the first evidence that cycle structure has an independent effect --- modest on OneMax, but non-zero. Practitioners should not enforce DAG topologies by default without first controlling for density.

We acknowledge several limitations. First, $n = 8$ islands is small; the Foster census sweep (13 cubic symmetric graphs, $n = 4$ to $30$, currently running) will test whether the effect scales. Second, the Pearson correlation at generation~30 is marginal ($p = 0.063$) on $n = 8$ topology-level data points, though significant at generation~50 ($r = 0.838$, $p = 0.009$) and corroborated by the 240-run ANOVA ($p < 10^{-7}$). Third, OneMax is the simplest possible fitness landscape; the generality of the finding to harder problems remains to be established.

---

## 8. Conclusion

For connected graphs with fixed vertex count, cycle rank $\beta_1$ and edge count $m$ differ by a constant (Theorem~1). This algebraic identity means that every prior comparison of cyclic versus acyclic communication topologies in the evolutionary computation and multi-agent systems literature is confounded: varying $\beta_1$ necessarily varies density, and vice versa. We escape this confound by moving to directed graphs, where simple directed cycle count $\kappa(G)$ is not determined by $(n, m)$. Across 240 controlled runs at constant density ($n = 8$, $m = 16$, 8 topology families, 30 seeds), we find that $\kappa(G)$ significantly predicts population diversity ($\eta^2 = 0.17$, $p < 10^{-7}$) and fitness ($\eta^2 = 0.24$). The effect is transient on the unimodal OneMax landscape but establishes that cycle structure is not reducible to density.

Future work should pursue three directions: (1)~scaling to larger graphs and harder fitness landscapes (NK, deceptive traps) where cycle-mediated exploration is predicted to yield stronger effects; (2)~testing whether directed cycle count interacts with agent capability, as suggested by Dochkina et al.'s capability-moderated findings; and (3)~developing $\kappa(G)$ as a practical design heuristic for communication topology selection in multi-agent systems.

---

> **Word count:** Discussion ~400 words, Conclusion ~155 words. Total ~555 words.
> **LaTeX notes:** All math inline/display-ready. Cross-references to Theorem~1 (Section 3), Section~3 (confound survey), and Figure~4 ($\eta^2$ bar chart). Citation placeholder for Dochkina et al. Foster sweep mentioned without citation (our own ongoing work). Cohen's thresholds are standard and do not need citation in EC venues.
> **Double-blind:** No self-identifying references. "Our prior work" removed. Foster sweep described generically.
