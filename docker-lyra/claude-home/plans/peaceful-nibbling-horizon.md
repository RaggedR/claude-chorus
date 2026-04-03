# E2E Tests + CLAUDE.md Production Roadmap

## Context
The Russian transcription app has recurring frontend bugs (popup scroll, flashcard direction, translate errors) that component tests don't fully catch. The app also needs a production roadmap for auth, rate limiting, and a $10/month payment system (first month free, Android). This plan covers two tasks:
1. Add Playwright E2E tests for critical user flows
2. Update CLAUDE.md with production roadmap and deployment changes

## Files to create
- `e2e/playwright.config.ts` — Playwright config
- `e2e/fixtures/mock-data.ts` — Shared mock response payloads
- `e2e/fixtures/mock-routes.ts` — Reusable `page.route()` interceptors
- `e2e/tests/app-loads.spec.ts` — App renders input form
- `e2e/tests/video-flow.spec.ts` — Full video URL → progress → chunks → player
- `e2e/tests/word-popup.spec.ts` — Popup scroll + click-to-translate (regression)
- `e2e/tests/flashcard-review.spec.ts` — Russian on front, English on back (regression)
- `e2e/tests/add-to-deck.spec.ts` — Word → popup → add to deck → badge updates
- `e2e/tests/regression.spec.ts` — Edge cases (non-Cyrillic click, multiple popups)

## Files to modify
- `/Users/robin/git/russian/package.json` — Add Playwright dependency + scripts
- `/Users/robin/git/russian/CLAUDE.md` — Update deployment section + add production roadmap

---

## Part 1: Playwright E2E Tests

### Mocking strategy: Playwright route interception

All API calls mocked at the browser network level via `page.route('**/api/**', ...)`. No real backend needed.

Advantages over starting a real Express server:
- Faster (no server boot), deterministic, isolates frontend logic
- Server integration tests already cover Express routing
- SSE mocked via `route.fulfill()` with `Content-Type: text/event-stream`

Firebase: Block all Firebase network requests (`page.route('**firebaseapp.com**', route => route.abort())`). Auth fails gracefully → `useDeck` falls back to localStorage. Pre-populate localStorage for deck tests.

### Playwright config

```ts
// e2e/playwright.config.ts
{
  testDir: './tests',
  baseURL: 'http://localhost:5173',
  webServer: {
    command: 'npx vite --port 5173',
    port: 5173,
    cwd: '..',  // project root
    reuseExistingServer: true,
  },
  use: { browserName: 'chromium' },
  timeout: 15000,
}
```

Only Vite dev server runs (serves React app). Backend NOT started — all `/api/*` intercepted.

SSE note: `api.ts` sends SSE to `http://localhost:3001` directly in dev. Playwright's `page.route('**/api/progress/**', ...)` matches any origin, so this is intercepted.

### Mock data (`e2e/fixtures/mock-data.ts`)

Shared constants matching the types in `src/types/index.ts`:
- `TEST_SESSION_ID` — fixed session ID
- `MOCK_TRANSCRIPT` — ~30 Russian words with timestamps (enough to test scrolling)
- `MOCK_CHUNKS` — 2 chunks (tests both single-chunk auto-select and chunk menu)
- `MOCK_TRANSLATION` — `{ word: 'Привет', translation: 'Hello', sourceLanguage: 'ru' }`
- `MOCK_SENTENCE` — `{ sentence: 'Привет мир, как дела?', translation: 'Hello world, how are you?' }`
- `MOCK_SRS_CARD` — A due flashcard for review tests

### Mock routes (`e2e/fixtures/mock-routes.ts`)

`setupMockRoutes(page)` registers handlers for:
- `POST /api/analyze` → cached response with chunks
- `GET /api/session/*` → session data
- `GET /api/session/*/chunk/*` → chunk with transcript + video URL
- `POST /api/download-chunk` → chunk data
- `POST /api/translate` → dynamic translation (reads `word` from request body)
- `POST /api/extract-sentence` → sentence + translation
- `GET /api/progress/**` → SSE connected event (immediate)
- `**firebaseapp.com**` / `**googleapis.com/identitytoolkit**` → abort (block Firebase)

### Test scenarios

**1. `app-loads.spec.ts`** — App renders
- Navigate to `/`
- Assert input form visible (URL input + submit button)
- Assert DeckBadge and Settings icons in header

**2. `video-flow.spec.ts`** — Full video flow
- Mock analyze with 2 cached chunks → submit URL → chunk menu appears
- Click Part 1 → mock download-chunk → player view with transcript
- Assert transcript words visible, progress bar at bottom
- Navigate back → chunk menu shows Part 1 as "Ready"

**3. `word-popup.spec.ts`** — Popup positioning + translation (REGRESSIONS)
- Navigate to player view with scrollable transcript
- Click Cyrillic word → popup appears with "Translating..." → resolves to translation
- Scroll transcript → assert popup moved with content (not fixed position)
- Implementation: compare `boundingBox().y` before/after scroll — must decrease
- Click close → popup disappears
- Click different word → new popup appears, old one gone

**4. `flashcard-review.spec.ts`** — Card direction (REGRESSION)
- Pre-populate localStorage with due card `{ word: 'привет', translation: 'hello' }`
- Open ReviewPanel → assert "привет" on front (large text), "hello" NOT visible
- Click "Show Answer" → assert "hello" visible
- Test swapped fields: `{ word: 'hello', translation: 'привет' }` → still shows "привет" on front
- Test with context sentences: Russian sentence visible before reveal, English after

**5. `add-to-deck.spec.ts`** — Add word to deck
- Navigate to player, click word → popup shows translation
- Click "Add to deck" → assert /api/extract-sentence called
- Assert popup changes to "In deck" checkmark
- Assert DeckBadge updates

**6. `regression.spec.ts`** — Edge cases
- Click non-Cyrillic text → no popup
- Multiple popups don't stack (click A, click B → only B's popup open)

### npm scripts

```json
"test:e2e": "cd e2e && npx playwright test",
"test:e2e:headed": "cd e2e && npx playwright test --headed",
"test:e2e:ui": "cd e2e && npx playwright test --ui"
```

---

## Part 2: CLAUDE.md Updates

### Update deployment section
- Change `book-friend-finder` to `russian-transcription` throughout
- Note: Frontend now on Firebase Hosting (`russian-transcription.web.app`), backend on Cloud Run
- Add E2E test commands

### Add production roadmap section

```markdown
## Production Roadmap

### Authentication & Payment (Priority: HIGH)
- Migrate from Firebase Anonymous Auth to email/password + Google OAuth
- Add Stripe subscription: $10/month, first month free
- Android app planned (React Native or PWA wrapper)
- Track per-user API usage (Whisper minutes, translations, TTS calls)
- Enforce usage quotas per tier (free trial vs paid)

### Rate Limiting (Priority: HIGH)
- Add express-rate-limit middleware to server/index.js
- Per-IP: 10 req/min on /api/analyze (expensive: Whisper + yt-dlp)
- Per-IP: 60 req/min on /api/translate
- Per-IP: 5 req/min on /api/extract-sentence (GPT calls)
- Global: budget cap on OpenAI API spend

### Session Security
- Replace timestamp-based session IDs with crypto.randomUUID()
- Add session ownership (tie sessions to authenticated user)
- Validate session access (users can only access their own sessions)

### Monitoring & Error Tracking
- Add Sentry or equivalent for error alerting
- Cloud Run error rate alerts via GCP Monitoring
- Track API costs per user for billing decisions

### Data Persistence
- Server-side deck backup (currently localStorage + Firestore)
- Export/import deck functionality

### CI/CD
- Add `node --check server/index.js` to deploy.sh (prevent syntax crashes)
- Add `npm test` to deploy.sh before deploying
- Consider GitHub Actions for automated testing on push
```

---

## Verification

1. `cd ~/git/russian && npm install` (installs Playwright)
2. `cd e2e && npx playwright install chromium`
3. `npm run test:e2e` — all E2E tests pass
4. `npm test` — existing 11 vitest tests still pass
5. Review CLAUDE.md for accuracy
6. `npm run test:e2e:headed` — visually verify popup scroll and flashcard direction tests
