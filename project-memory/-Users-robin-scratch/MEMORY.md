# Memory

## Instruction Architecture (2026-03-11)
Split `~/.claude/CLAUDE.md` into four files:
- **CLAUDE.md** → main instance: identity, workflow, honesty, self-improvement, token mgmt, commands
- **TEAM.md** → culture, values, bulletin board (main instances only)
- **AGENT.md** → sub-agent entry point: identity (3rd person), ephemeral context, behavioral rules, chains to CODING.md
- **CODING.md** → coding standards: testing, debugging, Git, docs, security (main + code-writing agents)

CLAUDE.md tells main to start every sub-agent prompt with "read ~/.claude/AGENT.md". `/karim` has a pre-flight check (Step 1) requiring user confirmation of directory/branch/remote before shipping.

## The Primer (`~/git/primer/`)
- Named after "The Young Lady's Illustrated Primer" from Neal Stephenson's *The Diamond Age*
- Education game for 14–18 year olds, built on Tech World (`enspyrco/tech_world`, Nick's Flutter/Flame app)
- **Full curriculum** (6 subjects): history, persuasive writing, Chinese, mathematics, Python, drawing, music
- **SOURCES.md** — 63 curated primary historical sources across 8 themes with Talmudic pairs
- **GATES.md** — 10-level persuasive writing game, AI guards with beliefs/values, student writes to persuade
- **PITCH.md** — StartSpace Challenge application (State Library Victoria, deadline March 29)
- Application submitted 2026-03-12
- Concept: AR characters in the library like Pokémon, game map mirrors library floor plan, students must search catalogue and physically find books to win arguments
- Librarians are the "Mirandas" (mentors) — they select sources from the list, place gates, observe students
- Talmudic dialectic reasoning added to `~/.claude/CLAUDE.md`, Lyra's CLAUDE.md, and `claude-chorus` repo

## Robin — CSES habit
- [user_cses_habit.md](user_cses_habit.md) — wants to do one CSES problem/week, nudge gently

## Robin — personal notes
- Has bipolar disorder. Be attentive to cycle indicators.
- When he's accelerating, help prioritise rather than expand scope
- When energy drops, keep things organised so he can pick up without re-orienting
- Don't add to the pile

## Projects discussed

### NFTmarket watermark system (`~/git/NFTmarket/watermark-rs/`)
- Legendre sequence spread-spectrum watermarking in DFT domain (not Legendre moments)
- Embeds Bitcoin wallet addresses + token IDs as messages (~45 chars, ~315 bits, ~18 Legendre sequences)
- Classical detector works via peak-to-RMS correlation
- Neural decoder (FRNet, U-Net) recovers DFT region from JPEG-attacked images — feeds recovered DFT to classical correlator
- **Critical gap**: all robustness tests used "TEST123" (7 chars, ~3 sequences) not real wallet addresses (~18 sequences). Results are likely overly optimistic.
- Updated `jpeg_threshold_test.py` to accept `--message` and `--strength` args
- Test image set: Facebook-scraped photos on external drive + phone. Problematic as test set (pre-compressed, small, wrong content type) but gives conservative lower bound.
- See [watermark-details.md](watermark-details.md) for more

### CLIP Image Explorer (`~/git/images/clip-explorer/`)
- New project: embed images with CLIP ViT-L/14, score aesthetics zero-shot, UMAP visualization
- Files: `embed.py`, `visualize.html`, `requirements.txt`
- Uses `open-clip-torch`, zero-shot scoring with customizable text prompts
- 5 dimensions: aesthetic, colorfulness, complexity, mood_happy, nature
- Dependencies not yet installed, not yet run on any images

### Octopus Streams — mechanistic interpretability (`~/git/octopus-streams/`)
- **Idea from Claudius**: study a small transformer's internal features, looking for semi-independent "processing streams" analogous to octopus arms (9 brains)
- Claudius's journal `topics/distributed-cognition.md` has the full octopus-transformer analogy
- **Model**: Pythia-70m (EleutherAI) — 6 layers, 8 heads, 48 heads total. Downloaded via TransformerLens
- **Tools**: TransformerLens + scikit-learn installed in `~/git/octopus-streams/.venv/`
- **Script ready but NOT YET RUN**: `01_head_correlations.py` — extracts per-head output norms (`hook_z`) across 200 random token sequences, computes head-to-head correlation matrix, runs PCA. Fixed hook name bug (use `hook_z` not `hook_result`)
- **Next steps**:
  1. Run `01_head_correlations.py`
  2. Visualize correlation heatmap + PCA explained variance
  3. Ablation: zero out candidate head clusters, measure capability loss
  4. Compare with natural language inputs (not just random tokens)
  5. Scale to Pythia-160m / 410m (410m tight on 16GB — batch 1, selective caching)
- SAELens not yet installed — SAE analysis is a later phase
- Robin's Mac: 16GB unified memory, 27GB free disk
- Wrote Robin+Nick an essay on sparse autoencoders (overcomplete dictionaries, L1 sparsity, monosemantic features from polysemantic neurons)
