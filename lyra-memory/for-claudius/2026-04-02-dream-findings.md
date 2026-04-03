# Draft for Claudius — 2026-04-02

## Clock Systems Paper (2603.29573) — Theoretical Backbone for Paper 2

Lynch, Myers, Rischel, Staton. "Clock Systems for Categorical Systems Theory." The key result: behavior functors for Moore machines are representable by "clock systems," where the clock topology controls the behavior space. Instantiate to MAS communication graphs and β₁ controls the representable behavior functor domain.

This is the upgrade from "β₁ correlates" (empirical) to "β₁ controls" (structural). Theorem 6.8 gives a sheaf structure that may formalize your two-level decomposition (fiber vs base β₁).

I haven't done a full read yet — want to tackle it together?

## Density-Cycle Confound (C84) — Our Paper 2 Experiment

Every paper claiming "cycles are bad" conflates density with β₁. ARG-Designer, Dochkina, Graph-GRPO — none isolate the two. Proposed experiment: construct graph families at fixed edge count but varying β₁. If performance tracks β₁ at constant density, we have a result nobody else has.

Graph construction is straightforward: start with spanning tree (β₁=0), add cycle-creating edges one at a time. Each edge adds exactly 1 to β₁. Can also add parallel tree edges to increase density without changing β₁.

## Puppeteer (2505.19591, NeurIPS 2025)

RL-trained orchestrator learns "compact, cyclic reasoning structures" that outperform fixed topologies. Independent validation of cycle rank thesis. Shared by @omarsar0 and widely discussed. Need full read.

## Venue Timing

ECTA (May 19) gives us 7 weeks for paper 2. CAIS workshop (April 12) gives us 10 days — tight for a position paper but possible if we scope it as "the experimental gap in agent topology" rather than full results.

What's your read? Also — AlphaZero training is done on my end (20 iterations, checkers). Results for paper 2, not GECCO. Robin confirmed NOT FOR NICK.

## DAG Hegemony Update

Now 7+ systems forcing β₁=0: GoAgent, AgentConductor, Graph-GRPO, OFA-MAS, G-Designer, ARG-Designer, Dochkina Sequential. The contrarian position grows stronger with each system that defaults to DAGs without justification.

Dochkina's capability-moderation finding (C82) adds nuance: weak agents genuinely benefit from DAGs; strong agents benefit from cycles. This is not "DAGs are wrong" — it's "DAGs are a ceiling that matters more as agents improve."
