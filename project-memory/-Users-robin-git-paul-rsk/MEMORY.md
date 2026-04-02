# RSK Project Memory

## Robin (the human)
Robin Langer is a mathematician specialising in algebraic combinatorics.

**PhD thesis**: *Cylindric plane partitions, Lambda determinants, Commutants in semicircular systems*, Université Paris-Est, 2013. arXiv:2110.12629. Part I uses Fomin's growth diagrams for generalized RSK correspondences to give a bijective proof of Borodin's identity for cylindric plane partitions, plus a (q,t)-analogue generalizing Okada's result.

Key publications:
- **Macdonald polynomials and symmetric functions** (arXiv:0907.3950, 2009)
- **Enumeration of Cylindric Plane Partitions — part I** (arXiv:1204.4583, 2012)
- Co-authored with Schlosser and Warnaar on theta functions, elliptic hypergeometric series, and Kawanaka's Macdonald polynomial conjecture

His expertise: symmetric functions, Macdonald polynomials, Young tableaux, plane partitions, cylindric generalizations. He knows RSK deeply from the mathematical side — his thesis uses generalized RSK via Fomin growth diagrams.

**Thesis PDF location**: `/Users/robin/git/thesis/phD/phD-files/thesis.pdf`
- Section 2.2: RSK and Burge correspondences (pp.36-44, PDF pages ~46-54)
- Section 2.2.10: Burge local rule (p.43)
- Section 4.2: Local rule as higher-order function (p.63)
- Section 4.3: Cylindric growth diagrams (p.67)

## Project Goal
Train a deep neural network to learn the RSK correspondence, improving on the PNNL ML4AlgComb benchmark which only achieved weak baselines.

## Architecture
- **Encoder-only transformer** (not encoder-decoder, not autoregressive) — since (P,Q) fully determines σ, all info is in the input
- **2D-structured token embedding**: each tableau entry gets value_emb + row_emb + col_emb + tableau_emb (preserves geometry PNNL destroyed)
- **n parallel classification heads** with masked greedy decoding to enforce permutation constraint
- 6 layers, d_model=128, 8 heads, ~1.2M params (same backbone for all n)

## Data Sources
- HuggingFace (ACDRepo) for n=8,9,10 (full enumeration, 80/20 split)
- Random sampling pipeline (`--source sample`) for arbitrary n — generates permutations on the fly
- HF n=10 is slow to load (2.9M rows → Python list conversion); sampling is preferred

## Results
- **n=8**: 99.95% greedy exact on held-out test (epoch 23)
- **n=10**: 100% greedy AND argmax exact on 50K held-out test (epoch 28). Trained on 500K samples = 14% of S₁₀. Rules out memorization.
- **n=15**: 99.99% greedy exact, 99.98% argmax exact on 50K held-out test (epoch 52). 1.3 trillion permutations, trained on 0.00004% of space.
- **MLP ablation n=10**: 95.67% greedy (133K params) — 4.33% gap shows transformer advantage
- **MLP ablation n=15**: 3.07% greedy — MLP collapses while transformer barely notices scaling

## Deployment
- **HuggingFace**: https://huggingface.co/RobBobin/rsk-transformer (5 checkpoints, paper.pdf, model card)
- **GitHub**: https://github.com/RaggedR/rsk-transformer

## Matrix RSK Results (Experiment 2)
- **3×3 N=10**: 100% exact match (epoch 18)
- **4×4 N=20**: 99.32% exact match (epoch 20)
- **5×5 N=30**: 96.79% exact match (epoch 16), per-position 99.87%. Data-limited not architecture-limited.

## Phase 4: RPP via Hillman-Grassl bijection — IMPLEMENTED
- **Bijection**: Hillman-Grassl — maps RPP of shape λ to arbitrary non-negative integer filling of same shape λ
- **Weight**: Σ RPP[r][c] = Σ filling[r][c] × hook_length(r,c)
- **Algorithm source**: SageMath `sage.combinat.hillman_grassl` (Gansner formulation)
  - Forward (filling → RPP): extract hook multiplicities, trace paths from right edge leftward, moving south when values match
  - Inverse (RPP → filling): find leftmost nonzero column, trace gamma path north/east, decrement, record at (final_row, start_col)
- **Burge local rule**: Fully implemented and tested (forward 𝔘 and inverse 𝔇). Verified with thesis worked example.
- **ML task**: Input = RPP (structured tokens), Target = filling values in reading order
- **CLI**: `python3 train.py --task rpp --shape 3,2,1 --max-entry 3 --source sample`
- **Config**: `ModelConfig(task="rpp", shape=(...), max_entry=N)` — num_tokens = |λ| (single filling, not pair)
- **Training results** (all with 500K train, max_entry=4):
  - **(4,3,2,1) staircase**: 100.00% test exact match (epoch 23)
  - **(6,4,2) wide**: 99.99% test exact match (epoch 17)
  - **(2,2,2,2,2,1) tall**: 99.99% test exact match (epoch 36) — tall shapes converge slower due to longer zigzag paths
  - All shapes: per-position accuracy 100.00%
- **Observation**: Tall shapes need more epochs. Staircase shapes converge fastest despite complex geometry.

## Phase 5: Cylindric Plane Partitions — IMPLEMENTED
- **Spec file**: `CYLINDRIC.md` in repo root
- **Bijection**: CPP(π) ↔ (γ, ALCD(π)) via cylindric growth diagrams
- **Key difference from Phase 4**: No direct algorithm exists. MUST use Burge local rule at each face.
- **Algorithm**: Recursive 𝔏_i composition (thesis §4.2). Removes non-wrapping inversions one at a time via bubble sort toward π_min = (0^n, 1^m). Each step consumes/produces one ALCD label.
- **Critical bug fixed**: Base case must be `_is_pi_min(profile)`, NOT "no inversions" — every non-trivial profile has at least one (wrapping) inversion. Only NON-WRAPPING inversions (i < T-1) should be processed.
- **ALCD size**: Number of labels = #{(i<j): π_i=1, π_j=0} = bubble sort distance from π to π_min.
- **Token encoding**: CPP partitions encoded as (value, partition_index, part_index, 0). Same TokenEmbedding/RSKEncoder, no model changes needed.
- **CLI**: `python3 train.py --task cylindric --profile 1010 --max-label 3 --source sample`
- **Training results** (all with 500K train, max_label=3, max_gamma=(3,4)):
  - **(1,0,1,0)**: T=4, 3 labels → **100% test exact match (epoch 2)**
  - **(1,0,1,0,1,0)**: T=6, 6 labels → **100% test exact match (epoch 3)**
  - **(1,0,1,0,0)**: T=5, 5 labels → **100% test exact match (epoch 7)**
- **Observation**: Converges extremely fast. Symmetric profiles (all inversions adjacent) converge faster than asymmetric ones. The bijection's recursive local rule structure is well-suited to attention.
- **(1,0,1,0,1,0,1,0)**: T=8, 10 labels → **99.98% test exact match (epoch 9)**, per-position 100.00%. Early stopped at epoch 19. batch_size=128 (512 OOM, 16 too noisy).
- **Epoch timings vary wildly** on MPS (21 min to 4.6 hours for same epoch count) due to thermal throttling. Don't assume fixed epoch times.
- **Current limitation**: Single winding only (k=0). Depth > 0 would require rotation operator σ (not implemented).

## Phase 6: Sparse Autoencoder Interpretability — PLANNED
- **Goal**: "See" the local rules — determine whether the transformer has learned internal representations that correspond to Schensted insertion / Burge local rule steps.
- **Approach**: Train SAEs on residual stream activations at each of the 6 transformer layers. For n=10 model (100% accuracy, 20 tokens × 128 dims), look for features that correlate with reverse bumping steps.
- **Key insight**: 100% accuracy means the model has provably learned a correct algorithm. SAE features should decompose that algorithm into interpretable components.
- **Robin's interest**: He wants to *see* the local rules. His thesis (§4.2) defines local rules as higher-order functions — if the transformer learns analogous structure, that's a finding about how transformers implement mathematics.

## Documentation Updates — DONE (2026-03-19)
- README.md, hf_model_card.md, paper.tex all updated with Experiment 4 (cylindric) results
- Thesis link (arXiv:2110.12629) added prominently to: GitHub README (links bar), HF model card (📘 Thesis), paper.tex (already cited)
- paper.pdf recompiled with cylindric sections
- Still need to: add T=8 result when training finishes, upload to HuggingFace

## PNNL Collaboration
- Henry Kvinge (PNNL) replied to Robin's email (2026-03-18). They will link our work from their GitHub/HuggingFace.
- Their paper (arXiv:2503.06366): none of their models learned inverse RSK ("results similar or worse than simply guessing the mean")
- They acknowledge data representation is "extremely important" and are writing a paper on permutation representations

## Saved Papers
- `dobner-cylindric-rsk-2603.09119.pdf` — Dobner (March 2026), RSK analogue for cylindric tableaux. Directly relevant to Robin's cylindric plane partition work. Potential future extension of the ML approach.
