---
name: Foster Sweep Decorrelation Insight
description: 3-regular graphs naturally decorrelate β₁ from density — key analytical insight for paper
type: project
---

# Foster Sweep: Natural Decorrelation of β₁ and Density

## Key Insight
For the Foster census of cubic symmetric graphs (all 3-regular):
- **Edges:** m = 3n/2 (constant degree)
- **β₁ = n/2 + 1** (grows linearly with n)
- **Density = 3/(n-1)** (DECREASES with n)

As n goes from 4 to 30:
- β₁ goes from 3 to 16 (5.3× increase)
- Density goes from 1.0 to 0.103 (9.7× decrease)

**β₁ and density are NEGATIVELY correlated across this family.**

## Why This Matters
If we observe diversity INCREASING with n across the Foster census, it means:
- Diversity increases WITH β₁ (positive correlation)
- Diversity increases AGAINST density (negative correlation with density)
- This is evidence for β₁ over density as the causal variable

This is a DIFFERENT decorrelation strategy than the directed cycle experiment:
- Directed experiment: fixed n, fixed m, varying cycle structure
- Foster sweep: fixed degree, varying n, β₁ and density naturally anticorrelated

**Two independent decorrelation strategies, same prediction.** If both show cycle-related effects, that's convergent evidence.

## Caveat
These graphs also vary in n (number of islands) and other structural properties (diameter, girth, automorphism group). So we can't attribute effects purely to β₁. But the density confound runs in the WRONG direction — if density were the driver, diversity should DECREASE with n. Any increase must come from something else.

## How to Apply
- In the paper, present Foster sweep as "natural experiment" alongside directed experiment
- Emphasize the anticorrelation: "density decreases while β₁ increases"
- Any positive diversity-n relationship is evidence against density-as-confounder
- Regression: regress diversity on both β₁ and density to see which coefficient dominates
