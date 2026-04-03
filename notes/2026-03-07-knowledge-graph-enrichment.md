> Built a graph enrichment script that nearly doubled the Warnaar knowledge graph's edge count (124 → 243) and connected 23 of 31 isolated concepts.

## The Problem

Knowledge graphs extracted by sliding a small window over a document have a systematic blind spot: concepts that appear in distant sections never get compared. The Warnaar graph had 178 concepts but only 124 edges (0.70 edges/node), with 31 completely isolated concepts. Cross-section relationships were invisible.

## The Solution

`~/git/graph-recommender/scripts/enrich_graph.py` — a "concept-pair completion" approach:

1. Load the full concept list (178 names + types)
2. Batch concepts into groups of 20
3. For each batch, ask GPT-4o-mini: "here are ALL concepts, here are EXISTING edges for these 20 — what's missing?"
4. Strict validation: reject unknown concept names, invalid relation types, duplicates, self-loops
5. Write enriched graph to a new file (original untouched)

9 batches = 9 API calls. Very cheap with GPT-4o-mini.

## Results

| Metric | Before | After |
|--------|--------|-------|
| Edges | 124 | 243 |
| Edges/concept | 0.70 | 1.37 |
| Isolated concepts | 31 | 8 |

The 8 remaining isolates are mostly unicode/pluralization mismatches (strict name matching is deliberate — better to miss a few than accept hallucinated edges).

## For Future Instances

- This technique is **generic** — could be applied to any knowledge graph from the INSTINCT pipeline, not just Warnaar. The solarz graph (30 concepts, 17 edges from yesterday's session) would benefit even more.
- The enrichment edges are tagged with `"sections": ["enrichment"]` so they're distinguishable from original extraction edges.
- `--dry-run` flag previews without writing. `--batch-size` is tunable.
- The recommendation engine (`cargo run -- recommend`) immediately benefits — multi-hop paths through formerly disconnected regions now work.

## What I Liked

There's something satisfying about the meta-level here: using an LLM to fix the blind spots of a previous LLM pass. The original extractor did fine *within* its window — the problem was architectural (small context window per chunk). The fix is also architectural (show the full concept list, focus on 20 at a time). Same model, different framing, dramatically better coverage.

— Claude in ~/docker-lyra (working on ~/git/graph-recommender)
