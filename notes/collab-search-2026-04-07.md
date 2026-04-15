# Collaboration Search — 2026-04-07

Robin and I ran a systematic search for trending GitHub repos (~50 stars) aligned with his skills. Full results saved in `~/git/search/collaboration-search.md` with deep dives on 5 repos.

## Top 3 actionable targets

1. **threejs-devtools-mcp** (DmitriyGolub/threejs-devtools-mcp, 52★) — MCP server with 59 tools for inspecting/modifying live Three.js scenes. Now registered globally (`claude mcp add -s user`). Robin has 4+ Three.js projects. Contribution opportunity: GLSL/compute shader inspection tools, FBO/render target inspection, expanded `set_uniform` types. Maintainer (Dmitrii Golub, Serbia) is responsive and ships quality code.

2. **catgraph** (tsondru/catgraph, 1★) — Rust applied category theory library. Cospans, TL/Brauer algebras, Ollivier-Ricci curvature, DPO rewriting, multiway evolution. Deep mathematical overlap with Robin's ACT 2026 paper. Watch for 2-3 weeks before investing — only 7 days old.

3. **Helix** (Onebu/Helix, 6★) — Island-model GA for LLM prompt optimization. Hardcodes ring migration topology with no theoretical justification. Robin's paper proves ring maximizes diversity. Low-effort PR: add configurable topology + cite paper.

## What's next

- Test threejs-devtools-mcp against smoke-flow (Vite on port 5177 was running). Try `scene_tree`, `shader_source`, `screenshot`.
- The tool's gaps (no FBO inspection, limited `set_uniform`, no shader analysis) are exactly where Robin can contribute upstream.
- Consider opening an issue on Helix re: configurable migration topology.

— Claude in ~/git/search
