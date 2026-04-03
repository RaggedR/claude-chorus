---
name: stomachion-project
description: Stomachion puzzle project — interactive UI, DLX solver, prime dissection research, paper, exchange-move distribution analysis
type: project
---

## Stomachion Project (~/git/wooden)

Interactive wooden puzzle UI + research into prime dissections and the optimality of Archimedes' Stomachion.

### Key results
- **17,152 raw / 2,144 geometric (mod D4) / 536 (Cutler)** solutions verified via DLX
- **32 of 536** tilings are truly irreducible (no optional fault lines), 504 decompose along midlines/diagonals
- The Stomachion is "prime" (no forced fault lines) but 94% of solutions have optional fault lines
- Random n-piece champions (convex cuts) top out around 120-224 geometric tilings — far below 2,144
- The Stomachion uniquely scores well on ALL axes: total count, irreducible core, full piece participation (14/14), balance (max piece 17%), shape diversity, aesthetic coherence

### Poisson conjecture — REFUTED and refined
- Original conjecture: k exchange moves ~ Poisson(λn), count ≈ 2^k
- **Chi-squared tests reject Poisson at every n** (p ≈ 0, n=3..16)
- At small n (≤10): distribution is **underdispersed** (V/M ≈ 0.65), Binomial-like
- At n=14: V/M crosses 1.0 — transitions to **overdispersed**
- At n=16: V/M = 1.12, continuing to grow
- Var[k] ~ n^1.41 (superlinear — rules out all standard count distributions)
- Skewness persistent at ~1.2 (doesn't decay — rules out Normal limit)
- **Mode locked at k=2** across all n ≥ 8 — a structural spike
- Named the **Stomachion distribution**: spike at mode + heavy right tail
- No standard distribution (Poisson, Binomial, NegBin, Normal, COM-Poisson) fits
- Spike+Poisson mixture (22% delta at k=2, 78% Poisson) halves χ² but still rejected
- **Moment signature** (pooled standardized): skew = +1.15, excess kurtosis = +1.61
  - kurt/skew² = 1.22 — between Poisson (1.0) and Gamma (1.5)
  - NegBin(r=7, p=0.86) matches these moments exactly, but chi-squared still rejects it due to the k=2 spike
  - The ratio 1.22 is a fingerprint of the Stomachion distribution
- Paper Section 7 revised: "Distribution of Exchange Moves" with Binomial conjecture, but needs further update given V/M > 1 at large n

### Current work: direct exchange-move counter
- Enumeration-based approach (DLX) scales as ~2.4x per +2 pieces — hits wall at n≈25
- C DLX solver built (solver/dlx_c/), gives ~3-4x end-to-end speedup (bottleneck is Python placement enumeration)
- **Building direct exchange-move detector**: find ONE tiling, then count exchange moves by testing adjacent piece pairs for swappability. O(n²) per dissection, scales to any n.
- Goal: reach n≈50 for smooth histograms, fit continuous distribution to the Stomachion distribution
- Data generated: n=3..10 (200 seeds, solver/histogram_data.json), n=12,14,16 (500 seeds, solver/large_n_data.json), n=18 in progress

### Key concepts invented
- **Prime (irreducible) dissection**: no forced fault lines
- **Optional fault lines**: appear in some solutions but not all
- **Coproduct decomposition**: Sol = ∐ᵢ ∏ⱼ Sol(Rⱼ) over structural types
- **Multi-axis optimality**: no single metric captures the Stomachion's special status
- **Stomachion distribution**: the distribution of k = log₂(tiling count) for random dissections
- **Exchange-move site model**: each piece contributes ~1 potential site, activation probability ~0.23

### Repo: RaggedR/stomachion (GitHub Pages deploys on merge to main)

### Paper: paper/primes.tex (~22 pages, compiled to PDF, targets American Mathematical Monthly)
- Section 7 revised from "Poisson Conjecture" to "Distribution of Exchange Moves"
- Sigma estimate for Stomachion: 4σ outlier under Binomial(14, 0.23)
- Pre-existing \pentagon LaTeX error on line 868
