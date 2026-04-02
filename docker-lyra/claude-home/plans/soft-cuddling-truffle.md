# Plan: Citation-Aware Structural Hole Detector

## Context

The user's thesis proof depended on van Leeuwen's 1987 paper — a "bridge paper" connecting q-series/growth diagrams (Cluster A) to symmetric functions/tableaux (Cluster B). No keyword search from either side would have found it. The user discovered it through a chance conversation with Viennot on a cliff.

**Goal**: Build a tool that systematically detects these structural holes and finds bridge papers, using citation network analysis overlaid on the existing concept knowledge graph.

**Target corpus**: Math research at `~/data/arxiv-rag/` (76 papers, 559 concepts, 486 edges, 6 thematic subdirectories). No Semantic Scholar API key — use unauthenticated access with conservative rate limiting.

## File to create

### `/Users/robin/git/knowledge-graphs/detect_structural_holes.py`

A single standalone script with 8 steps:

### Step 1: Extract paper metadata
- Scan `~/data/arxiv-rag/` subdirectories for PDFs
- Extract arXiv IDs from filenames via regex: `r'(\d{4}\.\d{4,5})'` (modern) + `r'(\d{7})'` (old format)
- 58/76 papers have arXiv IDs; 18 pre-arXiv papers skipped for citation fetch
- Map papers → concepts using `knowledge_graph.json`

### Step 2: Fetch citations from Semantic Scholar
- Endpoint: `GET https://api.semanticscholar.org/graph/v1/paper/arXiv:{id}?fields=title,year,references.paperId,references.externalIds,references.title,references.year`
- Rate limit: `time.sleep(3)` between calls (conservative for unauthenticated)
- Cache to `<dir>/citation_cache.json` after each fetch (crash-resilient)
- Skip papers already in cache
- Handle 404 (not in S2), 429 (rate limit → exponential backoff), timeouts
- ~58 calls × 3s = ~3 minutes

### Step 3: Build citation graph (NetworkX DiGraph)
- Nodes: 76 internal papers + all external references
- Edges: directed `cites` relationships
- Tag nodes as `internal=True/False`
- Log stats: total nodes, edges, internal→internal vs internal→external

### Step 4: Cluster papers by subdirectory
- Use the 6 subdirectories as natural clusters (deliberate thematic grouping):
  `core` (9), `crystal-bases` (5), `cylindric-partitions` (7), `hall-littlewood-macdonald` (4), `q-series-positivity` (34), `qsym-p-partitions` (18)
- Build concept sets per cluster from KG concept→papers mapping
- Generate 1-sentence cluster descriptions via GPT-4o-mini

### Step 5: Detect structural holes
- For each of 15 cluster pairs (6 choose 2):
  - **Concept similarity**: Jaccard index on concept sets
  - **Citation density**: cross-cluster citation edges / (|A| × |B| × 2)
  - **Hole score**: `concept_similarity / (citation_density + 0.01)`
- High hole score = concepts overlap but papers don't cite each other
- Sort by hole score descending

### Step 6: Find bridge papers
- For each structural hole: find external papers cited by papers in **both** clusters
- **Bridge score**: `citations_from_A × citations_from_B` (captures pathway density)
- Compute betweenness centrality on relevant subgraph
- These are the "van Leeuwens" — papers connecting worlds that our searches missed

### Step 7: Generate cross-cluster queries (GPT-4o)
- For each top structural hole, prompt GPT-4o with:
  - Key concepts from both clusters
  - Known bridge papers (if any)
  - Shared concepts
- Output: 3-5 targeted search queries for Semantic Scholar + arXiv
- Focus on mathematical intersection terms

### Step 8: Generate report
- `<dir>/structural_holes_report.json` — structured data
- `<dir>/structural_holes.md` — human-readable report with bridge papers, queries, reasoning
- Console summary

## CLI interface

```bash
python3 detect_structural_holes.py --dir ~/data/arxiv-rag/
python3 detect_structural_holes.py --dir ~/data/arxiv-rag/ --skip-fetch  # use cached citations
python3 detect_structural_holes.py --dir ~/data/arxiv-rag/ --top-k 5    # top 5 holes only
```

## Key files read

- `/Users/robin/data/arxiv-rag/knowledge_graph.json` — concept→paper mapping, edges
- `/Users/robin/data/arxiv-rag/extraction_cache.json` — paper titles for non-arXiv papers
- `/Users/robin/data/arxiv-rag/**/*.pdf` — filenames for arXiv ID extraction

## Dependencies

- `networkx` (already installed, v3.6.1) — graph construction, Louvain, betweenness
- `requests` (already installed) — Semantic Scholar API calls
- `openai` (already installed) — GPT-4o for query generation
- No new dependencies needed

## Cost estimate

- Semantic Scholar: free, ~58 API calls
- GPT-4o: ~15 cluster pairs × 1 call = ~$0.15-0.30
- GPT-4o-mini: 6 cluster descriptions = ~$0.01
- **Total: ~$0.20-0.35**

## Verification

1. Check `citation_cache.json` has ~58 entries with reference lists
2. Console output shows citation graph stats (expect 300-500 external papers)
3. `structural_holes.md` lists top 15 holes with bridge papers
4. Spot-check: do the bridge papers between `core` and `qsym-p-partitions` include anything related to growth diagrams or local rules?
5. Search queries should be specific enough to find relevant papers on Semantic Scholar

## Confidence: 80%

The architecture is straightforward (API calls + graph analysis + LLM prompts). Main risks:
- Semantic Scholar may not have all 58 arXiv papers (older math papers less covered)
- Unauthenticated rate limit may be tighter than expected
- Some structural holes may be real gaps (no bridge papers exist) vs. just unexplored connections

Both risks are handled by caching and graceful degradation.
