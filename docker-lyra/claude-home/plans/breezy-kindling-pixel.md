# Literature Review Skill — Implementation Plan

## Context

Robin wants a `/lit-review` skill that searches arXiv for papers on a topic, filters by abstract relevance, downloads PDFs, builds a fresh ChromaDB RAG, and allows querying — all in a new directory each time. Disk space is tight, so we minimize storage. ArXiv must be queried gently (3s between requests).

## Components

### 1. `~/data/lit-reviews/lit_review.py` — Main Python script

**Subcommands:**

```
python3 lit_review.py search "Bailey lemma cylindric partitions" [--max-papers 50] [--abstracts-only]
python3 lit_review.py query <review-dir> "specific question" [--top 5]
python3 lit_review.py list
```

**`search` workflow (6 phases):**

1. **Slug & directory creation**
   - Slugify search terms: lowercase, replace spaces/special chars with hyphens, truncate to 50 chars
   - Create `~/data/lit-reviews/<slug>-<YYYY-MM-DD>/`
   - Subdirs: `papers/` (PDFs), `chroma_db/` (index)

2. **ArXiv API search** (gentle)
   - URL: `http://export.arxiv.org/api/query?search_query=all:<terms>&start=0&max_results=100&sortBy=relevance`
   - Parse Atom XML with `xml.etree.ElementTree` (stdlib — no extra deps)
   - Extract: arxiv_id, title, abstract, authors, pdf_url, published date
   - Paginate if needed (2 pages × 100 = 200 candidates max)
   - **3-second sleep between API requests**
   - Save all candidates to `candidates.json`

3. **Abstract relevance ranking**
   - Embed the search query + all abstracts using OpenAI `text-embedding-3-small`
   - Rank by cosine similarity to query embedding
   - Take top N (default 50, configurable with `--max-papers`)
   - This costs ~1 API call (batch 200 abstracts) — cheap and fast
   - Save ranked list to `selected_papers.json` with similarity scores

4. **PDF download** (gentle)
   - Download PDFs from `https://arxiv.org/pdf/<id>`
   - **3-second sleep between downloads**
   - Skip on failure (log warning), continue with remaining papers
   - `--abstracts-only` flag skips this phase entirely (saves ~75 MB)
   - Progress bar: print `[12/50] Downloading 2401.12345...`

5. **RAG indexing**
   - Reuse patterns from existing `~/data/arxiv-rag/rag.py`:
     - `extract_text_from_pdf()` — PyMuPDF text extraction
     - `chunk_text()` — 1500-char chunks, 200-char overlap, smart breaks
     - `get_embeddings()` — OpenAI batch embedding
   - If `--abstracts-only`: index abstracts directly (no PDF extraction needed)
   - ChromaDB PersistentClient at `<review-dir>/chroma_db/`
   - Collection name: `"lit_review"`
   - Metadata per chunk: source filename, chunk_index, arxiv_id, title

6. **Summary generation**
   - Save `manifest.json`: timestamp, query, paper count, chunk count, disk usage
   - Print summary: "Indexed 47 papers (2,341 chunks) in ~/data/lit-reviews/bailey-lemma-2026-02-16/"

**`query` subcommand:**
- Load ChromaDB from `<review-dir>/chroma_db/`
- Embed query, search, display results (same pattern as existing rag.py)
- Show: similarity score, paper title, arxiv ID, matching passage

**`list` subcommand:**
- Scan `~/data/lit-reviews/*/manifest.json`
- Show: directory name, query, paper count, date, disk size

### 2. `~/.claude/commands/lit-review.md` — Global skill

**Behavior:**
- Takes search terms as `$ARGUMENTS`
- Spawns a `general-purpose` background agent (`run_in_background: true`)
- Agent runs: `python3 ~/data/lit-reviews/lit_review.py search "$ARGUMENTS"`
- Reports task ID and expected directory to user
- Tells user how to query when done: `python3 ~/data/lit-reviews/lit_review.py query <dir> "question"`

### 3. Disk space estimates

| Component | Per paper | 50 papers |
|-----------|-----------|-----------|
| PDFs | ~1.5 MB | ~75 MB |
| ChromaDB | ~1 MB | ~50 MB |
| Abstracts JSON | ~2 KB | ~100 KB |
| **Total (with PDFs)** | | **~125 MB** |
| **Total (abstracts-only)** | | **~5 MB** |

The `--abstracts-only` flag reduces storage by 96% at the cost of depth.

## Files to create

| File | Purpose |
|------|---------|
| `~/data/lit-reviews/lit_review.py` | Main script (~300 lines) |
| `~/.claude/commands/lit-review.md` | Skill definition (~50 lines) |

## Dependencies (all already installed)

- `PyMuPDF` (fitz) — PDF extraction
- `chromadb` — vector store
- `openai` — embeddings
- `xml.etree.ElementTree` — arXiv XML parsing (stdlib)
- `urllib.request` — PDF download (stdlib)

## Key design decisions

1. **Embedding-based relevance filtering** over keyword matching — cheap (1 API call), more accurate than keywords, doesn't require LLM tokens
2. **Separate ChromaDB per review** — clean isolation, easy to delete old reviews
3. **3s delay everywhere** — arXiv's stated guideline; no risk of throttling
4. **stdlib XML + urllib** — no new dependencies to install
5. **`--abstracts-only` default: no** — full PDFs by default, but flag available for disk-constrained runs

## Verification

1. `python3 ~/data/lit-reviews/lit_review.py search "test query" --max-papers 3` — smoke test with 3 papers
2. `python3 ~/data/lit-reviews/lit_review.py query <resulting-dir> "test question"` — verify RAG works
3. `python3 ~/data/lit-reviews/lit_review.py list` — verify listing
4. `/lit-review test query` — verify skill invocation spawns background agent
5. Check disk usage with `du -sh ~/data/lit-reviews/<dir>/`
