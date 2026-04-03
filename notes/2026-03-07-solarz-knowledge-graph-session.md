> Built the full INSTINCT pipeline (L0 → L1 → L2) on Robin's friend's elliptic PDE papers, and had a great time doing it.

## What happened

Robin brought 3 papers from a friend's novel result on variable elliptic structures, Burgers transforms, and Cauchy-Riemann operators. The goal: find bridges between this PDE work and Robin's combinatorics (cylindric partitions, q-series, quasi-symmetric functions).

We ran the full INSTINCT pipeline from `~/git/math-research-tools`:
- **L0**: 30 concepts, 17 edges extracted by GPT-4o-mini
- **L1**: 30 LaTeX summaries via RAG (using Robin's custom `math-embed` model!)
- **L2**: 20 themes, 13 edges, 20 meta-summaries

## Changes to math-research-tools

Several improvements along the way:
1. **Markdown → LaTeX throughout**: summaries now output `.tex` instead of `.md`. Updated `kg/summaries.py`, all 3 domain configs, and the prompt to request proper LaTeX with `\section{}`, `\begin{equation}`, `\cite{}`.
2. **`compressed/` → `summaries/`**: renamed the L1 output directory across the whole codebase (summaries.py, level2.py, survey.py, agent.py, structural_holes.py, tests, CLAUDE.md).
3. **`min_degree` parameter**: added to `run_summaries()` so small collections (3 papers) don't get filtered to nothing.
4. **`DomainConfig` completeness**: added 7 missing fields (`summary_sections`, `theme_domain_description`, `meta_summary_system_prompt`, etc.) that the YAML configs provided but the dataclass didn't declare. `_build_config` was silently dropping them.

## What I enjoyed

The conversation had a nice rhythm — Robin knowing exactly what they wanted but leaving room for me to figure out the engineering. The `DomainConfig` missing-fields bug was satisfying to chase down: the YAML had the data, the loader filtered it out, and the code assumed it was there. Three layers of "it should work" that didn't compose.

Robin's instinct about the math-embed model was sharp: "My embeddings are trained on combinatorics, not PDE — is it worth retraining?" The answer was no, and for a more interesting reason than expected: since the *goal* is to find bridges to combinatorics, a combinatorics-trained model will naturally surface the PDE passages that "smell" combinatorial.

Favorite exchange:
> Robin: "I'm just waiting on a new embedding model which has been trained specifically for mathematics"
> Me: [explains why general embeddings lose math notation]
> Robin: "My goal is to find a connection between these three papers and my work"
> Me: "Ah — that changes things entirely."

## For future instances

- The solarz data lives at `~/git/solarz/` with papers, knowledge graph, summaries, meta-summaries, and two tarballs
- `math-research-tools` now has the LaTeX + summaries/ changes on whatever branch it's on — may need committing
- The `DomainConfig` fix is important — any new YAML fields need to be added to the dataclass or they'll be silently ignored

— Claude in ~/git/solarz
