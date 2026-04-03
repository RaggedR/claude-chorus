# Gateway Project Memory

## Symmetric Graph Drawing Project (~/git/graphviz/)

Robin's honours thesis: "Symmetric Graphs and Their Quotients" (algebraic graph theory).
Built a pipeline: GAP (group theory) → Python (layout) → TikZ PDF or D3.js HTML.

**Read first**: `~/git/graphviz/SYMMETRIC_EMBEDDING.md` — full docs, theory, issues, architecture.

### Quick Reference
- `python3 draw_graph.py <name>` → PDF (auto-detects cyclic vs cylindrical)
- `python3 draw_graph_d3.py <name>` → interactive HTML
- `python3 draw_all.py` → gallery PDF (WIP)
- Graphs: petersen, heawood, pappus, dodecahedron, desargues, moebiuskantor, cube, icosahedron, k33
- Add graphs in `symmetric-layout.g` GraphLibrary, always verify |Aut|

### Tools Installed
- **GAP 4.15.1**: `brew install gap-system/gap/gap` (GRAPE + Digraphs)
- **Graphviz**, **LaTeX** (pdflatex/xelatex) — pre-installed

## Robin's Preferences
- Working dir: `~/git/graphviz/` (not `/tmp/`)
- Has `~/git/math/` with LaTeX notes (amsmath, tikz, standalone)
- Likes both PDF and interactive D3.js outputs
