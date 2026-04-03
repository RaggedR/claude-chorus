# Plan: Split lit-review and knowledge-graph workflows

## Context
Currently `/lit-review` downloads PDFs AND builds ChromaDB, while `/knowledge-graph` only reads from existing ChromaDB. The user wants a clean separation:
- **lit-review**: search + download PDFs to a given directory (no RAG)
- **knowledge-graph**: ingest PDFs from a directory into ChromaDB, then build KG

**Constraints:**
- Both skills require a directory argument — NO defaults
- Scripts must NOT live in or default to `~/data/arxiv-rag/`
- Move relevant code to `~/git/research/bin/` (new directory)

## Files

| File | Action |
|------|--------|
| `~/data/lit-reviews/lit_review.py` | Remove RAG indexing, add `--dir`, make dir compulsory |
| `~/git/research/bin/build_knowledge_graph.py` | **New** — moved from `~/data/arxiv-rag/`, add PDF ingestion, require `--dir` |
| `~/.claude/commands/lit-review.md` | Update skill |
| `~/.claude/commands/knowledge-graph.md` | Update skill |

`~/data/arxiv-rag/build_knowledge_graph.py` and `~/data/arxiv-rag/rag.py` are left untouched — they continue to work standalone for the existing arxiv-rag corpus.

## Changes

### 1. `lit_review.py` — Remove RAG, add `--dir`

**a) CLI parser** (lines 862-882): Add `--dir <path>` option. Make it the output directory.

**b) `cmd_search` signature** (line 254): Add `output_dir=None`. If provided, use it as `review_dir`. Remove `chroma_dir` (line 264).

**c) Delete Phase 5** (lines 334-409): Remove entire ChromaDB indexing block.

**d) Update summary** (lines 411-444):
- Renumber phases to 1/3, 2/3, 3/3
- Remove `chunk_count` from manifest
- Replace "To query" hint with "To build a knowledge graph: /knowledge-graph <dir>"

### 2. `build_knowledge_graph.py` — Move to research, add ingestion

Copy `~/data/arxiv-rag/build_knowledge_graph.py` to `~/git/research/bin/build_knowledge_graph.py` with these modifications:

**a) Remove default dir** — `--dir` is required, no `DEFAULT_DIR` fallback.

**b) Add PDF ingestion functions** — copy `extract_text_from_pdf()`, `chunk_text()`, `get_embeddings()` from `~/data/arxiv-rag/rag.py`. Also copy `rag.py` to `~/git/research/bin/rag.py` as a reference/utility (or inline the needed functions).

**c) Add `ingest_pdfs(rag_dir)` function** (~50 lines):
- Scans `rag_dir/papers/*.pdf`
- Extracts text → chunks → embeds → stores in `rag_dir/chroma_db/`
- Collection name: `"lit_review"`
- Loads `selected_papers.json` if available for metadata

**d) Auto-detect in `main()`**: If `chroma_db/` missing but `papers/` has PDFs → auto-ingest, then build KG.

### 3. `lit-review.md` — Update skill

- Dir argument is compulsory (first argument)
- Claude should generate multiple "smart" search queries — theme and variation queries based on the user's topic and conversation context (e.g., for "cylindric partitions positivity", also try "q-series positivity", "plane partition generating function", etc.)
- Run `lit_review.py search <terms> --dir <dir>` for each query variant
- Remove all RAG/query references
- Suggest `/knowledge-graph <dir>` as next step

### 4. `knowledge-graph.md` — Update skill

- Dir argument is compulsory
- Points to `~/git/research/bin/build_knowledge_graph.py --dir <dir>`
- Remove default to `~/data/arxiv-rag/`
- Keep lit-review name shorthand (resolve via `~/data/lit-reviews/$NAME/`)
- Document auto-ingestion behavior

## Confidence: ~90%

## Verification
1. `/lit-review /tmp/test-review cylindric partitions positivity --max-papers 5` → Claude generates multiple query variants, PDFs in `/tmp/test-review/papers/`, no `chroma_db/`
2. `/knowledge-graph /tmp/test-review` → auto-ingests, builds KG, opens HTML
3. Existing `~/data/arxiv-rag/` scripts untouched and still work independently
4. Both skills error cleanly if no directory argument is provided
