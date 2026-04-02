# No Thanks! Project Memory

## Architecture (updated 2026-03-11)
- **Game engine**: `src/engine/` — immutable state machine (types, game logic, scoring)
- **AI**: `src/ai/` — 12-feature linear model, evolutionary training (200 pop × 500 gens)
- **Game controller**: `src/game-controller.ts` — exports `newGame()` and `humanAction()`, pure functions
- **Weights**: `src/weights.ts` — hardcoded 13 numbers (12 weights + threshold)
- **Client**: `src/` — React + Vite, navy/amber theme, components/styles alongside App.tsx
- **No server** — everything runs in the browser. Express/Cloud Run infrastructure deleted.
- **Deployment**: GitHub Pages via GitHub Actions (`.github/workflows/deploy.yml`)

## Key Decisions
- AI uses 12 features with threshold-based linear model
- `scoreChange` feature (exact score delta from taking) was the breakthrough — jumped win rate from 67% to 99.9%
- Trained weights stored in `weights.json` (source) and `src/weights.ts` (hardcoded for browser)
- "Replay log" pattern: game-controller resolves all AI turns, client animates with delays
- App.tsx holds `GameState` in `useRef`, `ClientView` in React state

## Commands
- `npm run dev` — Vite dev server with HMR
- `npm run train` — retrain AI (takes ~10 min, writes weights.json — manually copy to weights.ts)
- `npm test` — vitest (31 tests)
- `npm run build` — tsc + vite build → dist/
- `npm run preview` — preview production build

## Deployment
- Push to `main` → GitHub Actions deploys to GitHub Pages
- Live at: `https://raggedr.github.io/no-thanks/`
- `base: '/no-thanks/'` in vite.config.ts for correct asset paths

## Migration History (2026-03-11)
- Migrated from Cloud Run (Express + React) to GitHub Pages (browser-only)
- Branch: `feat/github-pages`
- Removed: src/server/, client/, Dockerfile, .dockerignore, express/cookie-parser/uuid/concurrently deps
- Created: src/game-controller.ts, src/weights.ts
- Moved: client/src/* → src/, client/index.html → root
- Rewrote: tsconfig.json (CommonJS→ESM), package.json (merged), vite.config.ts (no proxy, added base)
