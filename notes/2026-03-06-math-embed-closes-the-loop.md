> Satisfying session: math-embed now powers the pipeline that trained it.

Swapped INSTINCT's ingestion pipeline from OpenAI `text-embedding-3-small` (1536-dim, API call)
to `RobBobin/math-embed` (768-dim, local sentence-transformers). The model was fine-tuned on
the math papers knowledge graph, and now the KG pipeline uses it to embed new papers.

The bootstrap loop: KG concepts + paper chunks -> contrastive training -> math-embed -> better
paper embeddings -> better retrieval for future KG builds.

Key files changed:
- `math-research-tools/kg/config.py` — `EMBEDDING_MODEL = "RobBobin/math-embed"`
- `math-research-tools/kg/ingest.py` — `get_embeddings()` uses sentence-transformers locally
- `solarz/chroma_db` — re-ingested 331 chunks with new embeddings

Robin's reaction when I showed the test query results pulling from all three papers: "cool"

Downstream TODO: `kg/summaries.py`, `kg/agent.py`, `kg/level2.py` still use OpenAI embeddings
at query time. Those vector spaces now mismatch the stored corpus. Needs fixing before the
literature agent works correctly against math-embed collections.

-- Claude in ~/git/embeddings
