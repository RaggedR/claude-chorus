# Plan: Browser Back/Forward Button Support via React Router

## Context

The app is a single-page React app with a 5-state view machine (`input` → `analyzing` → `chunk-menu` → `loading-chunk` → `player`). Currently the browser back button does nothing — there's no router, no history entries. The user wants the back button to navigate between "pages" (view states).

A previous attempt used the raw History API (`pushState`/`popState`), but it required manually categorizing every `setView` call as push vs. replace and had an unresolved E2E failure. **The user explicitly requested a switch to React Router** for a more maintainable solution.

**Approach**: Install `react-router-dom`, use `BrowserRouter` with 3 routes (`/`, `/chunks`, `/player`). Transient states (`analyzing`, `loading-chunk`) remain as React state overlays — no URL change. The browser back/forward buttons work automatically because React Router manages the history stack.

## New Dependency

`react-router-dom` (v7) — the standard React routing library. BrowserRouter (not MemoryRouter) is required because MemoryRouter doesn't interact with the browser's history stack.

## Files to Modify

| File | Change |
|------|--------|
| `package.json` | Add `react-router-dom` |
| `src/main.tsx` | Wrap `<App />` in `<BrowserRouter>` |
| `src/App.tsx` | Replace `view` state with URL-derived view + `transientView` overlay state; replace 25 `setView` calls with `navigate()` or `setTransientView()` |
| `tests/app.test.tsx` | Wrap renders in `<MemoryRouter>`, add 4 browser-history tests |
| `e2e/tests/browser-history.spec.ts` | **New**: 4 Playwright E2E tests |

No backend, Vite config, or Docker changes. Server already has SPA catch-all at `server/index.js:2003-2010`.

## Routes

| Route | View | Description |
|-------|------|-------------|
| `/` | `input` | URL input + demo buttons. Also hosts `analyzing` as a transient overlay. |
| `/chunks` | `chunk-menu` | Chunk selection menu. Also hosts `loading-chunk` as a transient overlay. |
| `/player` | `player` | Video/audio player with transcript. |

`analyzing` and `loading-chunk` are transient loading states that don't get their own URLs. They overlay the current route's view (e.g., analyzing overlays `/`, loading-chunk overlays `/chunks` or `/` for single-chunk auto-proceed).

## Implementation (TDD)

### Step 1: Install react-router-dom

```bash
cd /Users/robin/git/russian-feat-browser-history && npm install react-router-dom
```

### Step 2: Write failing tests first

**`tests/app.test.tsx`** — Two changes:

1. Update `render(<App />)` calls to wrap in `<MemoryRouter>`:
   ```tsx
   import { MemoryRouter } from 'react-router-dom';
   // Helper:
   const renderApp = (initialRoute = '/') =>
     render(
       <MemoryRouter initialEntries={[initialRoute]}>
         <App />
       </MemoryRouter>
     );
   ```
   Replace all `render(<App />)` with `renderApp()` across existing tests.

2. Add a `Browser history` describe block with 4 new tests:
   - Navigates to `/chunks` when multi-chunk analysis completes (check chunk-menu visible)
   - Navigates to `/player` when chunk is selected (check player visible)
   - Route guard: starting at `/chunks` with no session → redirects to `/` (shows input)
   - Route guard: starting at `/player` with no data → redirects to `/` (shows input)

**`e2e/tests/browser-history.spec.ts`** — New file, 4 tests:
- Back from chunk-menu → input (verify input view appears)
- Back from player → chunk-menu (verify chunk-menu appears)
- Forward after back restores view (back then forward returns to same view)
- Back after reset lands at input (session cleared, guard kicks in)

### Step 3: Wrap App in BrowserRouter (main.tsx)

```tsx
import { BrowserRouter } from 'react-router-dom';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
);
```

### Step 4: Replace view state with URL-derived view (App.tsx)

Remove:
```tsx
const [view, setView] = useState<AppView>('input');
```

Add:
```tsx
import { useLocation, useNavigate } from 'react-router-dom';

const location = useLocation();
const navigate = useNavigate();

// Transient loading overlays (don't change the URL)
const [transientView, setTransientView] = useState<'analyzing' | 'loading-chunk' | null>(null);

// Derive the effective view from the URL + any transient overlay
const view: AppView = transientView || (() => {
  switch (location.pathname) {
    case '/chunks': return 'chunk-menu' as const;
    case '/player': return 'player' as const;
    default: return 'input' as const;
  }
})();
```

### Step 5: Add route guards + transient cleanup

```tsx
// Clear transient overlays when URL changes (e.g., browser back/forward)
useEffect(() => {
  setTransientView(null);
}, [location.pathname]);

// Route guards: redirect if navigating to a view without required data
useEffect(() => {
  if (location.pathname === '/chunks' && !sessionId && sessionChunks.length === 0) {
    navigate('/', { replace: true });
  }
  if (location.pathname === '/player' && !transcript && !videoUrl && !audioUrl) {
    navigate('/', { replace: true });
  }
}, [location.pathname, sessionId, sessionChunks.length, transcript, videoUrl, audioUrl, navigate]);
```

### Step 6: Replace all 25 setView() calls

**Mapping rules:**
- `setView('analyzing')` → `setTransientView('analyzing')` (no URL change)
- `setView('loading-chunk')` → `setTransientView('loading-chunk')` (no URL change)
- `setView('chunk-menu')` → `navigate('/chunks')` or `navigate('/chunks', { replace: true })` for errors
- `setView('player')` → `navigate('/player')`
- `setView('input')` → `navigate('/', { replace: true })` for errors, `navigate('/')` for user-initiated

| Handler | Line | Current | Replacement | Reason |
|---------|------|---------|-------------|--------|
| `loadReadyChunk` success | 242 | `setView('player')` | `navigate('/player')` | Chunk loaded, show player |
| `loadReadyChunk` error | 245 | `setView('chunk-menu')` | `navigate('/chunks', { replace: true })` | Error fallback |
| `finishChunkDownload` | 264 | `setView('player')` | `navigate('/player')` + `setTransientView(null)` | Download done |
| `handleSelectVideoChunk` no-session | 272 | `setView('input')` | `navigate('/', { replace: true })` | Error |
| `handleSelectVideoChunk` loading | 287 | `setView('loading-chunk')` | `setTransientView('loading-chunk')` | Transient |
| `handleSelectVideoChunk` SSE error | 308 | `setView('chunk-menu')` | `setTransientView(null)` | Error, stay on /chunks |
| `handleSelectVideoChunk` catch | 322 | `setView('chunk-menu')` | `setTransientView(null)` | Error, stay on /chunks |
| `handleSelectTextChunk` no-session | 331 | `setView('input')` | `navigate('/', { replace: true })` | Error |
| `handleSelectTextChunk` loading | 346 | `setView('loading-chunk')` | `setTransientView('loading-chunk')` | Transient |
| `handleSelectTextChunk` SSE error | 369 | `setView('chunk-menu')` | `setTransientView(null)` | Error, stay on /chunks |
| `handleSelectTextChunk` catch | 383 | `setView('chunk-menu')` | `setTransientView(null)` | Error, stay on /chunks |
| `handleAnalyzeVideo` start | 399 | `setView('analyzing')` | `setTransientView('analyzing')` | Transient |
| `handleAnalyzeVideo` cached multi | 437 | `setView('chunk-menu')` | `navigate('/chunks')` | Forward nav |
| `handleAnalyzeVideo` SSE multi | 464 | `setView('chunk-menu')` | `navigate('/chunks')` | Forward nav |
| `handleAnalyzeVideo` SSE error | 469 | `setView('input')` | `setTransientView(null)` | Error, stay on / |
| `handleAnalyzeVideo` catch | 476 | `setView('input')` | `setTransientView(null)` | Error, stay on / |
| `handleAnalyzeText` start | 484 | `setView('analyzing')` | `setTransientView('analyzing')` | Transient |
| `handleAnalyzeText` cached multi | 522 | `setView('chunk-menu')` | `navigate('/chunks')` | Forward nav |
| `handleAnalyzeText` SSE multi | 549 | `setView('chunk-menu')` | `navigate('/chunks')` | Forward nav |
| `handleAnalyzeText` SSE error | 554 | `setView('input')` | `setTransientView(null)` | Error, stay on / |
| `handleAnalyzeText` catch | 561 | `setView('input')` | `setTransientView(null)` | Error, stay on / |
| `handleBackToChunks` | 586 | `setView('chunk-menu')` | `navigate('/chunks')` | User-initiated back |
| `handleLoadDemo` multi | 685 | `setView('chunk-menu')` | `navigate('/chunks')` | Forward nav |
| `handleLoadDemo` error | 689 | `setView('input')` | `navigate('/', { replace: true })` | Error |
| `handleReset` | 705 | `setView('input')` | `navigate('/')` | User-initiated reset |

### Step 7: Update Stripe return handler

Line 194: `window.history.replaceState({}, '', window.location.pathname)` — keep as-is (just cleans up the `?subscription=success` query param, doesn't affect router state).

### Step 8: Add navigate to useCallback dependency arrays

Every handler that now calls `navigate()` needs it in its dependency array. This is straightforward since `navigate` is stable across renders (from React Router).

### Step 9: Run all tests, verify green

```bash
cd /Users/robin/git/russian-feat-browser-history && npm test
cd /Users/robin/git/russian-feat-browser-history && npm run test:e2e
```

## Expected Back Button Behavior

| Scenario | History Stack | Back goes to |
|----------|--------------|-------------|
| Multi-chunk analysis | `/` → `/chunks` | `/` (input) |
| Player from chunk menu | `/` → `/chunks` → `/player` | `/chunks` (chunk-menu) |
| Single-chunk auto-proceed | `/` → `/player` | `/` (input) |
| After reset | `... → /` | Previous entry |
| After reset then forward | Guard: no session → stays at `/` | — |

## Key Design Decisions

1. **Transient states are overlays, not routes.** `analyzing` and `loading-chunk` are loading spinners that shouldn't create history entries. Pressing back during analysis does nothing (URL is still `/`), which is correct.

2. **No `auto` parameter needed.** Unlike the raw History API approach, we don't need to distinguish user-click vs auto-proceed for chunk handlers. Single-chunk auto-proceed stays at `/` (transient overlay), then navigates to `/player`. Multi-chunk goes through `/chunks`. The history stack is naturally correct.

3. **Route guards handle stale forward navigation.** If a user presses forward to `/chunks` or `/player` after session data was cleared (e.g., after reset), the guard redirects to `/`.

## Confidence: 85%

React Router is well-tested infrastructure that handles the history stack automatically — no manual push/replace decisions per call site. Main risk: existing tests may need minor tweaks for the MemoryRouter wrapper. The transient overlay pattern (analyzing/loading-chunk as React state, not URLs) is the novel part, but it's simple.
