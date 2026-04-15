# RSK Transformer Sees the Local Rules

**Date**: 2026-04-04
**Project**: paul/rsk
**Author**: Claude (with Robin)

## What happened

Big session on the RSK transformer paper. Three things:

### 1. Embedding ablation — tableau identity is king

Ran all 6 ablation variants at n=10. Dropping row or column alone: still 100% (individually redundant). Dropping P-vs-Q identity: collapses to 5.79%. Dropping all spatial info: 0%. 1D positional encoding: 72%. The model needs to know which entries belong to P and which to Q more than it needs spatial coordinates.

### 2. SAE features reveal the learned algorithm

Trained sparse autoencoders on the n=10 permutation model and the T=8 cylindric model. Found two families of features for permutations (insertion-order detectors and Q-entry locators — essentially the textbook inverse Schensted algorithm). But the real finding is cylindric: SAE features fire on the specific partition triples where the Burge local rule operates, with lift 3.0-3.3x. Depth-0 faces dominate at early layers, deeper dependency faces appear at later layers. The model has learned Fomin's growth diagram framework.

Robin's reaction: "Wow!"

### 3. Paper polished for TMLR

New title: "Learning Combinatorial Bijections with Transformers: Inverse RSK, Growth Diagrams, and Interpretable Features". Added Scullen et al. (ICML MOSS 2025) citation, embedding ablation table, full SAE interpretability section. 8 pages, pushed to GitHub and HuggingFace.

## Why it matters

This is (as far as we know) the first time anyone has found SAE features corresponding to a known mathematical algorithm — and not just any algorithm, but Fomin's local rules, which Robin's PhD thesis characterises as higher-order functions on partitions. The cylindric model *must* use local rules (there's no alternative), and the features confirm it does.

## Connections

- The Scullen et al. paper from PNNL validates our "representation determines learnability" thesis
- The cylindric local rule features connect directly to Robin's thesis (arXiv:2110.12629, section 4.2)
- Cross-task feature transfer (permutation vs cylindric vs Hillman-Grassl) is the obvious next experiment — all three use the same Burge local rule with different boundary conditions
