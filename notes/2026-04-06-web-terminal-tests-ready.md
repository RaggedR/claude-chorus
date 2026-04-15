> web-terminal TDD test suite is complete — 194 tests across 8 files, ready for implementation.

## What's done

All test files written for `~/git/web-terminal/`. Every module has a stub in `src/` (empty class) and a full test suite in `test/`. Tests auto-skip via prototype method checks — as you implement methods, tests activate automatically.

Run `npx vitest run --reporter=verbose` to see all 194 tests skip cleanly. Run `npx vitest --watch` while implementing to see them light up.

## Implementation order (recommended)

Start with the easiest, work up:

1. **pty-manager** (22 tests) — Pure Node, EventEmitter + Map + node-pty. Accept `ptyFactory` in options for testability. The FakePty mock in the test file shows exactly what IPty methods we use.
2. **ws-bridge** (16 tests) — Wires WebSocket ↔ pty. Parse sessionId from URL path. Binary frames = pty I/O, text frames = JSON control messages. Don't destroy pty on WS disconnect (allows reconnect).
3. **tab-manager** (22 tests, jsdom) — Pure DOM manipulation. Needs a minimal inline EventEmitter (~15 lines). Keyboard shortcuts registered on `document`. Remember `e.preventDefault()` on Ctrl+T/W.
4. **terminal-view** (17 tests, jsdom) — Wraps xterm.js + WebSocket. Uses CDN globals (window.Terminal, etc). ResizeObserver for fit. Exponential backoff reconnect.
5. **idle-detector** (16 tests) — fs.watch on JSONL file. Track byte offset. Debounce 200ms, dedup via SHA-1 sliding window (20 entries), ignore events >60s old.
6. **idle-detector-client** (15 tests, jsdom) — Simplest frontend module. Badge + ding + Notification API.
7. **latex-renderer** (20 tests) — pdflatex + dvisvgm pipeline. LRU cache (Map with eviction). Integration tests have 30s timeouts and skip if no TeX installed (`describe.skipIf`).
8. **latex-overlay** (66 tests, jsdom) — **Hardest.** Four internal stages: AnsiStripper (state machine), LineBuffer, LatexScanner (dollar-sign heuristics + environment accumulation), overlay positioning. Study LaTerM source (MaxwellsEquation/LaTerM on GitHub) before starting. The `$` disambiguation heuristics matter — test file has edge cases for $PATH, $100, backtick spans, etc.

## Architecture docs

Read these first:
- `~/git/web-terminal/docs/ARCHITECTURE.md` — system diagram, data flow, interface definitions
- `~/git/web-terminal/docs/PRIOR_ART.md` — study LaTerM for the latex-overlay pattern
- `~/git/web-terminal/docs/modules/*.MODULE.md` — one per module, full spec + behaviour

## Key decision: DOM renderer + inline overlays

The previous instance explicitly chose xterm.js DOM renderer (not WebGL) so that KaTeX/TikZ overlays can be positioned inline with terminal text. This is the LaTerM pattern: intercept `terminal.write()`, replace LaTeX with hash placeholders, render overlays at placeholder positions. Don't revisit this without talking to Robin.

## What I enjoyed

The architecture has real personality — this is a mathematician's terminal. The decision to render math inline rather than in a side panel means you see `$\mathcal{F}$` right next to the sentence describing the functor. The ANSI stripper → line buffer → LaTeX scanner pipeline is a satisfying streaming architecture. And the idle-detector using Claude Code hooks + fs.watch to ding when Claude needs attention is clever infrastructure that'll make Robin's multi-instance workflow genuinely better.

— Claude in ~/git/scratch (working on ~/git/web-terminal)
