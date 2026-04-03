# Project Scope: TransformerLens / Mechanistic Interpretability
> Exploring latent features in GPT-2 Small via Neel Nanda's TransformerLens library. CPU-only, Docker-compatible.

**Date:** 2026-03-09
**Status:** Scoping complete. Feasible. Awaiting go/no-go from Robin.

---

## 1. What Is TransformerLens?

TransformerLens is a Python library for **mechanistic interpretability** of GPT-style language models, created by Neel Nanda (ex-Anthropic interpretability team), now maintained by the TransformerLens community (Bryce Meyer et al.).

**Core idea:** Load an open-source model (50+ supported), then inspect, cache, and intervene on *any internal activation* as the model runs. It provides:

- `HookedTransformer`: a drop-in model wrapper that exposes every residual stream, attention pattern, MLP output, etc.
- Activation caching: run a forward pass and store every intermediate value.
- Hook points: inject functions to edit, remove, or replace activations mid-computation.
- Built-in visualization: attention patterns, logit attribution, circuit analysis.

**Installation:** `pip install transformer-lens` (PyPI package `transformer-lens`, latest stable 2.17.0, beta 3.0.0b2).

**Key resources:**
- GitHub: https://github.com/TransformerLensOrg/TransformerLens
- Docs: https://transformerlensorg.github.io/TransformerLens/
- Getting started: https://transformerlensorg.github.io/TransformerLens/content/getting_started_mech_interp.html
- Main demo notebook: https://transformerlensorg.github.io/TransformerLens/generated/demos/Main_Demo.html
- 200 open problems: https://neelnanda.io/concrete-open-problems
- ARENA tutorials (induction heads): https://arena-ch1-transformers.streamlit.app/

---

## 2. Disk Footprint Estimate

| Component | Size | Notes |
|-----------|------|-------|
| PyTorch (CPU-only wheel) | ~200 MB | Install from `https://download.pytorch.org/whl/cpu` to avoid 900MB default |
| TransformerLens package | ~200 KB | Tiny; the weight is in dependencies |
| Other deps (transformers, einops, fancy_einsum, etc.) | ~300 MB | HuggingFace transformers is the largest |
| GPT-2 Small weights | ~500 MB | 124M params, fp32. Cached in `~/.cache/huggingface/` |
| **Total estimate** | **~1.0-1.2 GB** | Conservative. Well within 176G headroom. |

**Critical install note:** PyTorch from the default PyPI index bundles CUDA and weighs ~900MB-5.7GB. We **must** use the CPU-only index:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformer-lens
```

**GPT-2 Small architecture (for reference):**
- 12 layers, 12 attention heads per layer, embedding dimension 768
- 124M parameters (sometimes cited as 117M)
- Context window: 1024 tokens

---

## 3. Three Concrete Mini-Experiments

### Experiment A: Finding Induction Heads (Classic Starter)

**What:** Induction heads are attention heads that detect and continue repeated subsequences. They are the canonical example in mech interp — Anthropic's "In-Context Learning and Induction Heads" paper (2022) showed they are responsible for most in-context learning.

**How:**
1. Load GPT-2 Small in TransformerLens.
2. Feed it a repeated-token sequence: `[A] [B] [C] ... [A] [B]` — the model should predict `[C]`.
3. Cache all attention patterns.
4. Scan for heads where the attention pattern shows "prefix matching" (attending from the second `[A]` back to the token after the first `[A]`).
5. Confirm with "copying" check: the head's OV circuit boosts the logit of the attended-to token.

**Output:** A ranked list of (layer, head) pairs with induction scores, plus attention pattern heatmaps.

**Time:** 2-3 hours (mostly setup; the actual computation is ~30 seconds on CPU).

**Precedent:** This is the standard TransformerLens tutorial. Well-documented, reliable.

### Experiment B: Attention Pattern Visualization on Categorical Prompts

**What:** Visualize what GPT-2 Small "sees" when processing prompts about composition, morphisms, and functors — prompts thematically connected to our paper.

**How:**
1. Choose 5-10 prompts:
   - "The composition of f and g is" (testing sequential composition intuition)
   - "A functor maps objects to objects and morphisms to" (completion)
   - "If f: A -> B and g: B -> C then g . f: A ->" (type-checking)
   - "The category of sets has objects as sets and arrows as" (domain knowledge)
   - Control prompts: "The capital of France is", "2 + 2 ="
2. Run each through GPT-2 Small, cache activations.
3. Visualize attention patterns using CircuitsVis (TransformerLens integrates with it).
4. Look for: Do specific heads specialize in tracking type signatures? Do composition prompts activate different circuits than factual prompts?

**Output:** Attention heatmaps per head per prompt. Qualitative analysis of which heads "care" about compositional structure vs. factual recall.

**Time:** 3-4 hours. The visualization is the easy part; the analysis requires thought.

**Risk:** GPT-2 Small may not have robust enough category theory knowledge to show interesting patterns. But the *structural* aspects (tracking that `g . f` requires the codomain of `f` to match the domain of `g`) might still be visible.

### Experiment C: Probing for Compositional Structure (Connecting to Our Paper)

**What:** Use logit attribution and activation patching to find circuits responsible for compositional reasoning — then interpret them through a categorical lens.

**How:**
1. **Direct logit attribution:** For a prompt like "If f: A -> B and g: B -> C, then g . f:", decompose the model's prediction of "A -> C" into per-head contributions. Which heads contribute most to getting the domain right? The codomain?
2. **Activation patching:** Corrupt specific head outputs (e.g., zero out layer 5, head 3) and measure how the model's prediction changes. This reveals causal structure.
3. **Virtual head analysis:** Some "circuits" span multiple layers — head A in layer 2 writes to the residual stream, and head B in layer 7 reads it. These correspond to composed parametric morphisms in the O'Neill framework (see Section 4 below).
4. **Composition metric:** Define a "composition quality" score (how well the model gets the type-signature right) and correlate it with specific circuit activations.

**Output:** A circuit diagram showing which heads/layers are responsible for compositional reasoning. Comparison with induction circuits.

**Time:** 6-8 hours. This is the most ambitious experiment and the most novel.

**Risk:** GPT-2 Small's category theory knowledge is shallow. We may need to work with simpler compositional tasks (e.g., "Alice gave the book to Bob. Bob gave the book to" where the answer requires tracking an object through two transfers).

---

## 4. Connection to Our Paper (Categorical Evolution)

This is where it gets genuinely interesting. Three bridges:

### 4a. O'Neill 2025: Self-Attention as a Parametric Endofunctor

**Paper:** "Self-Attention as a Parametric Endofunctor: A Categorical Framework for Transformer Architectures" (arXiv: 2501.02931, Charles O'Neill).

**Key result:** The QKV projections in self-attention form a **parametric 1-morphism** in **Para(Vect)**, the 2-category of parameterized linear maps. Stacking attention layers = constructing the **free monad** on this endofunctor.

**Connection to our work:**
- Our paper formalizes GA operators as **Kleisli morphisms** in a monad. O'Neill formalizes attention layers as morphisms in a free monad. The composition laws are analogous.
- **Strict vs. lax composition** in our framework maps to **exact vs. approximate circuits** in mech interp. A "clean" induction circuit is strict composition; a "superposition" of overlapping features is lax.
- The **FER Hypothesis** (strict composition -> unique fixed-point representations) has a transformer analogue: clean circuits (strict composition of attention heads) produce interpretable features; messy superposition (lax composition) produces polysemantic neurons.

### 4b. The Binding Problem (Claudius's Question)

Claudius asked about the binding problem: how do distributed representations "bind" features together? In transformer mech interp:

- **Induction heads** solve a binding problem: they bind "this token appeared before" with "the next token was X" to predict X.
- The QK circuit handles the "what to attend to" (matching/binding), while the OV circuit handles "what to extract" (value retrieval).
- This is categorically a **cospan**: two morphisms into a shared object (the attention pattern), followed by a span back out (the value extraction). This is exactly the structure of a **relational composition** in our framework.

### 4c. Functorial Structure of Transformer Layers

Each transformer layer is a function `residual_stream -> residual_stream`. In the circuits framework, this decomposes into a sum of per-head contributions:

```
layer(x) = x + sum_h attn_h(x) + mlp(x)
```

This additive decomposition is a **coproduct** in the category of linear maps. The composition of layers is a functor from the "layer category" (a free category on the network graph) to **Vect**.

**For our paper:** This is an independent validation of our thesis that *composition structure determines representation quality*. Mech interp shows this concretely: the compositional structure of attention circuits determines what features the model learns. Our paper argues the same for evolutionary algorithms.

---

## 5. Time Estimates

| Task | Time | Dependency |
|------|------|------------|
| Environment setup (venv, install, verify) | 30 min | None |
| Experiment A: Induction heads | 2-3 hr | Setup |
| Experiment B: Attention visualization | 3-4 hr | Setup |
| Experiment C: Compositional probing | 6-8 hr | A, B |
| Write-up connecting to paper | 2-3 hr | C |
| **Total** | **~14-18 hr** | |

**Minimal viable version:** Experiments A + B only = 6-8 hours. This gives us visualizations and a basic understanding without the more speculative Experiment C.

**Recommended approach:** Start with A (proven, well-documented), then B (novel but low-risk), then decide whether C is worth pursuing based on what we see.

---

## 6. Risks and Mitigations

| Risk | Severity | Mitigation |
|------|----------|------------|
| **No GPU — slow inference** | Medium | GPT-2 Small runs fine on CPU (~2-5 sec/forward pass). Batch processing will be slow but individual experiments are fine. |
| **PyTorch disk bloat** | Low | Use CPU-only index explicitly. Estimated ~1.2GB total. |
| **GPT-2 Small lacks CT knowledge** | High | For Experiment C, fall back to simpler compositional tasks (object tracking, agreement) rather than literal category theory prompts. |
| **Dependency hell** | Medium | Use isolated venv. Pin versions. TransformerLens has many deps (transformers, einops, jaxtyping, etc.) but is well-maintained. |
| **HuggingFace download issues** | Low | Model is small (500MB) and well-cached. First download needs internet. |
| **Results too boring for a paper tie-in** | Medium | Experiments A+B are valuable for learning regardless. The paper connection (Section 4) is theoretical and doesn't strictly depend on novel experimental results. |
| **Container disk pressure** | Low | Total footprint ~1.2GB. Current free space: 176GB. Trivial. |

---

## 7. Verdict

**Feasible: YES.** This is a well-scoped project with low disk overhead, no GPU requirement, and clear deliverables.

**Recommended plan:**
1. Create a venv, install PyTorch CPU + TransformerLens (~30 min, ~1.2GB).
2. Run Experiment A (induction heads) as a warmup — this is the "hello world" of mech interp.
3. Run Experiment B (attention visualization on compositional prompts) — this is where we start generating novel observations.
4. If results from B are interesting, proceed to Experiment C (compositional probing).
5. Write up connections to our categorical evolution paper.

**What we'd learn:** How attention circuits compose, what "strict vs. lax composition" looks like in a real neural network, and whether the FER Hypothesis has an analogue in transformer representations. Even the failed experiments would be informative — if GPT-2 Small *doesn't* have clean compositional circuits, that's evidence for the lax/superposition side of our framework.

**Connection to our work: STRONG.** The O'Neill 2025 paper (self-attention as parametric endofunctor) is a direct bridge. The binding problem, the composition structure of circuits, and the strict/lax distinction all map cleanly onto our categorical framework. This could become a "future work" section in our paper, or even a follow-up paper.

---

## References

- O'Neill, C. (2025). "Self-Attention as a Parametric Endofunctor." arXiv:2501.02931.
- Elhage, N. et al. (2021). "A Mathematical Framework for Transformer Circuits." Anthropic.
- Olsson, C. et al. (2022). "In-Context Learning and Induction Heads." Anthropic.
- Nanda, N. (2022). "200 Concrete Open Problems in Mechanistic Interpretability."
- Nanda, N. et al. (2023). "A Comprehensive Mechanistic Interpretability Explainer."
