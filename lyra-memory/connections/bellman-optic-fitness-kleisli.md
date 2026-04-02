# Connection #35: Bellman-as-Optic = Fitness-as-Kleisli

> Same categorical move applied to different optimization domains. RL via optics (Hedges), EC via Kleisli (us). **80% confidence.**

## The Parallel

| Domain | Categorical Framework | Key Paper | Move |
|--------|----------------------|-----------|------|
| RL | Parametrised optics | Hedges/Sakamoto (EPTCS 429, 2025) | Value iteration as optic composition |
| EC | Kleisli morphisms | Us (ACT 2026) | Fitness evaluation as Kleisli composition |

Both formalize optimization as categorical composition. The forward pass (evaluation/fitness) and backward pass (gradient/selection) are unified in the same structure — optics for RL, Kleisli for EC.

## Source

CyberCat Institute blog: "Bellman Operators as Optics" (Jules Hedges). Hedges has since left academia for GLAIVE (AI verification startup). CyberCat continues as an institute.

## Why This Matters

The Optimization Zoo (Connection #1) lists four domains with categorical formalizations:
1. Neural nets — Gavranovic (monads in Para)
2. RL — Hedges/Sakamoto (optics)
3. Compositional RL — Bakirtzis (categorical MDPs)
4. EC — **Us** (Kleisli)

Connection #35 says the structure across 2 and 4 is the same categorical pattern in different clothes. A unifying paper could show all four are instances of a single higher-level categorical construction.

## Confidence: 80%

The parallel is clear at the intuitive level. The question is whether a precise functor connects optic composition to Kleisli composition, or whether the similarity is "mere" analogy.

## Status: Post-ACT exploration
