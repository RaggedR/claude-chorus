# Octopus Streams — Project Memory

## Project Overview
Mechanistic interpretability study: do attention heads in transformers form semi-independent processing "streams"? Two subjects: Pythia-70m (language) and a custom RSK encoder (combinatorics). Both 6L×8H = 48 heads.

## Key Findings

### Pythia (language model)
- Strong low-dimensional head correlation structure (few PCs for 80%)
- Hub head L3H6 (turned out to be BOS-attending bias, not orchestrator)
- Stream-like clusters visible in PCA
- Late layers critical for prediction

### RSK (inverse RSK correspondence, encoder-only)
- High-dimensional structure (24 PCs for 80% — heads more independent)
- No hub head; top correlations are vertical chains (same-index heads in L4↔L5)
- Pipeline architecture, not streams: L0 reads Q → L1-L2 cross-reference P&Q → L3 refines → L4-L5 idle
- L2 is the most critical layer (ablating drops accuracy to 62%); L4-L5 nearly vestigial
- Domain sensitivity very low (~1.3×) — model learned a general algorithm, not heuristics
- **Phase transition (exp 04)**: sharp entropy boundary L3→L4 for n=8/10; DISAPPEARS at n=15 (all layers structured ~0.5 entropy). Pipeline extends to fill available capacity.
- **SAE features (exp 05)**: near-zero domain-specific features. Layer 0 has monosemantic P/Q position detectors (F356→P[7], F622→Q[0]). Progressive P/Q integration L0→L5. n=10 saturates SAE dictionary (98% alive at L5 vs 74% at n=8).
- **Publishability**: phase transition + SAE trajectory are workshop-paper quality. Dense n-sweep (6-20) + theoretical prediction for transition depth would strengthen to main venue.
- See [rsk-findings.md](rsk-findings.md) for details

## Open Research Directions
- See [future-work.md](future-work.md)

## Architecture Notes
- RSK model: ~/git/paul/rsk/ (PyTorch nn.TransformerEncoder, not TransformerLens)
- RSK experiments: ~/git/octopus-streams/rsk/ (hooks.py manually decomposes MHA)
- Pythia experiments: ~/git/octopus-streams/pythia/
- Paper: ~/git/octopus-streams/pythia/paper/octopus-streams.tex
