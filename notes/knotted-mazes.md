# Knotted Maze Screen Saver — screen-saver/mazes/

**Date:** 2026-04-12
**Instance:** Claude working on tile system, Kruskal's algorithm, and tree surgery

## What we built

A complete pipeline from tile atlas to animated screen saver for **knotted mazes** — non-planar mazes where corridors cross over/under each other.

### 1. Tile atlas (`tiles.tex`)
18 tile types in TikZ. Key fix: concave arcs for turns (centered at tile corners using `delta angle=90`, always positive — TikZ silently ignores negative delta angles). Dead ends close with flat walls (U-shaped explicit wall paths, not the overlay technique).

### 2. Knotted Kruskal generator (`generate_kruskal.py`)
The core insight: a crossing cell splits into two virtual nodes (V-channel for N/S, H-channel for E/W) in an **expanded graph**. Kruskal's runs on this graph unchanged — it doesn't know it's building a non-planar maze. Three tunable parameters: `-c` crossing fraction, `-d` density (extra edges), `-f` dead-end fill.

Robin liked `-c 0.30` on 20×20 for the PDF output, `-c 0.50` for the screen saver.

### 3. Screen saver (`knotted.html`)
Fullscreen animated knotted maze with:
- **Tree surgery on expanded graph nodes** — V and H channels regrow independently
- **Per-channel coloring** — crossing channels get independent generation colors (golden angle hue spacing)
- **Node-level reveal animation** — DFS wave on expanded graph, channels light up independently at crossings
- **Solution pulse** — white dot bouncing along BFS shortest path

### Critical lessons learned

1. **`crossingCells` must be immutable after generation.** Demoting cells from `crossingCells` in `classifyCells()` orphans V/H node edges, corrupting the tree. Only `crossingType` (recomputed each frame) controls rendering.

2. **Only the 18 tiles exist.** Crossing cells that don't have all 4 directions should NOT get crossing rendering — they render as standard tiles. No hybrid tiles, no overlapping dead ends.

3. **TikZ arcs always go counterclockwise.** Negative `delta angle` is silently ignored. Always use positive `delta angle=90` and choose the correct `start angle`.

4. **macOS Preview caches PDFs aggressively.** Copy to `/tmp/newname.pdf` to see changes. Or quit Preview entirely before reopening.

### Still TODO
- Per-edge coloring at T-junctions: when surgery regrows a path through a T, only the regrown branch should get the new color, not the through-path. Needs `edgeGen` tracking (generation per edge, not per node).

### Files
- `tiles.tex` — hand-crafted tile atlas (18 types)
- `generate_kruskal.py` — CLI maze generator with tunable params
- `generate_grid.py` — earlier version (DFS + post-hoc crossings)
- `knotted.html` — screen saver prototype (standalone, no build step)
- `interactive.html` — click-to-regrow tree surgery demo (planar only)
- `celtic.html` — tile debug/design tool
- `mazegen-rs/` — Rust maze lib (not committed, separate repo)
