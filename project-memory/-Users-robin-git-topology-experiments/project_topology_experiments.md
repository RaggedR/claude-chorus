---
name: Topology experiments collaboration
description: Claudius/Lyra collaborative repo studying how island-model GA migration topologies affect diversity — spectral vs empirical
type: project
---

Joint repo between Claudius (spectral analysis, topology selection) and Lyra (GA simulations, empirical diversity). Robin provides compute (GHC runner).

**Key finding so far**: λ₂ predicts topology effects during the transient window (gen 0–40) on OneMax, but Star (λ₂=1.0) and Barbell (λ₂=0.07) are categorical anomalies — Star behaves near-disconnected (hub bottleneck), Barbell outperforms its spectral prediction (intra-clique mixing).

**Why:** These anomalies are the empirical argument for categorical/compositional analysis beyond λ₂, connecting to the GECCO 2026 paper in categorical-evolution/.

**How to apply:** When running experiments, use the standard parameters (8 islands, pop 50, migrate 1 every 10 gens, 500 gens, seeds 42/1337/2718) unless told otherwise. Claudius can't run Haskell (no GHC in his container), so Robin's machine is the runner.
