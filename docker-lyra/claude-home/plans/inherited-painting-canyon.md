# Plan: Frontend-Backend Integration Test Suite

## Context

The Russian Video Transcription app has a backend (Express.js) and frontend (React thin client) that communicate over HTTP and SSE. Currently, only the `createHeartbeat` function has unit tests. There are no tests verifying the API contract — the shapes of requests/responses, SSE event formats, error handling, or multi-step flows like analyze → progress → session → chunk download. A comprehensive integration test suite will catch regressions when either side changes.

## Approach

Spin up the **real Express server** on a random port but **mock the external dependencies** (yt-dlp, ffmpeg, OpenAI) at the module boundary (`server/media.js`). This tests the actual HTTP contract, session management, chunking logic, and SSE streaming — everything except the slow/expensive external calls.

## Files to Modify

| File | Change |
|------|--------|
| `server/index.js` | Export `app` and guard `app.listen()` so tests can import the server |
| `server/integration.test.js` | **New file** — the full integration test suite |
| `server/vitest.config.js` | Add `integration.test.js` timeout override (these tests are slower) |

## Step 1: Make server importable (`server/index.js`)

Replace the bottom of `index.js` (lines 1670-1679):

```js
// Before:
app.listen(PORT, () => { ... });

// After:
export { app };

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`OpenAI API key: ${process.env.OPENAI_API_KEY ? 'loaded from .env' : 'not set'}`);
    console.log(`Google API key: ${process.env.GOOGLE_TRANSLATE_API_KEY ? 'loaded from .env' : 'not set'}`);
    cleanupOldSessions().catch(err => {
      console.error('[Startup] Cleanup failed:', err.message);
    });
  });
}
```

This preserves the existing `npm run dev:backend` behavior while letting tests `import { app } from './index.js'`.

Also export the in-memory Maps for test cleanup:
```js
export { app, analysisSessions, localSessions, progressClients };
```

## Step 2: Create `server/integration.test.js`

### Mock Setup (top of file)

Use `vi.mock('./media.js')` to replace all 5 external-facing functions:
- `getOkRuVideoInfo` — returns `{ title, duration }`
- `downloadAudioChunk` — writes a dummy file at `outputPath`, returns `{ size, info }`
- `downloadVideoChunk` — writes a dummy file at `outputPath`, returns `{ size }`
- `transcribeAudioChunk` — returns a mock transcript
- `addPunctuation` — passes transcript through unchanged
- `createHeartbeat` — returns a no-op `{ stop, isStopped, getSeconds }`

### Server Lifecycle

```
beforeAll:  app.listen(0) → capture random port as baseUrl
afterAll:   server.close()
beforeEach: vi.clearAllMocks(), clear analysisSessions/localSessions/progressClients Maps
```

Clearing the Maps between tests ensures isolation — no leaked sessions between tests.

### Helper Utilities

1. **`createMockTranscript(wordCount, durationSec)`** — generates evenly-spaced words + segments (realistic enough for `createChunks()` to produce proper chunks)

2. **`createSSEClient(url)`** — uses Node `http.get` to consume SSE events, returns `{ events[], waitForEvent(type, timeoutMs), close() }`. Cannot use browser `EventSource` in Node.

3. **`analyzeAndWait(baseUrl, url, opts)`** — POSTs to /api/analyze, subscribes to SSE, waits for 'complete' event, returns `{ sessionId, completeEvent }`. Used by most test suites as setup.

### Test Suites (31 tests)

#### A. Health Check (1 test)
- `GET /api/health` → `{ status: 'ok' }`

#### B. POST /api/analyze — Happy Path (2 tests)
- **New analysis**: POST with mocked media → verify `{ sessionId, status: 'started' }`, then SSE `complete` event has `{ title, totalDuration, chunks[], hasMoreChunks }`. Verify `GET /api/session/:id` returns `status: 'ready'`.
- **Cached session**: POST same URL again → `{ status: 'cached', chunks }` returned immediately.

#### C. POST /api/analyze — Error Cases (3 tests)
- Missing URL → 400 `'URL is required'`
- Missing OPENAI_API_KEY → 400 `'API key not configured'`
- Media download failure (mock rejects) → SSE `error` event, session status `'error'`

#### D. GET /api/session/:sessionId (4 tests)
- Non-existent session → 404
- Ready session → `{ status: 'ready', title, totalDuration, chunks[], hasMoreChunks }`
- Error session → `{ status: 'error', error: string }`
- Downloading session (in-progress) → `{ status: 'downloading', progress }`

#### E. POST /api/download-chunk (5 tests)
- Pending chunk → 200 with `{ videoUrl, transcript, title }`, chunk becomes `status: 'ready'`
- Already-ready chunk → returns cached data, `downloadVideoChunk` NOT called again
- Invalid session → 404
- Invalid chunk ID → 404
- Download failure → 500, chunk reset to `'pending'`

#### F. GET /api/session/:sessionId/chunk/:chunkId (4 tests)
- Pending chunk → 400 `'Chunk not ready'`
- Ready chunk → 200 `{ videoUrl, transcript, title }` with adjusted timestamps
- Non-existent session → 404
- Non-existent chunk → 404

#### G. POST /api/load-more-chunks (3 tests)
- Happy path (long video with `hasMoreChunks: true`) → new chunks with sequential IDs, adjusted timestamps
- Non-existent session → 404
- No more chunks (`hasMoreChunks: false`) → 400

#### H. POST /api/translate (4 tests)
- Valid translation (mock `globalThis.fetch` for Google API) → `{ word, translation, sourceLanguage }`
- Cache hit (translate same word twice) → fetch called only once
- Missing word → 400
- Missing API key → 400

#### I. DELETE /api/session/:sessionId (2 tests)
- Existing session → `{ success: true }`, subsequent GET returns 404
- Non-existent session → still 200 (cleanup is idempotent)

#### J. SSE Progress Format (3 tests)
- Connected event on subscribe → `{ type: 'connected', sessionId }`
- Error session sends error event on connect → `{ type: 'error', message }`
- Client disconnect cleanup → no crash when sendProgress called after disconnect

## Step 3: Update vitest config

Add a test timeout for integration tests (they need time for setTimeout-based background processing):

```js
test: {
  globals: true,
  environment: 'node',
  include: ['**/*.test.js'],
  testTimeout: 15000,  // Integration tests need more time
  // ... existing coverage config
}
```

## Key Design Decisions

1. **Mock at the media.js boundary** — not at `fetch`/`spawn` level. This tests Express routing, session management, chunking, and SSE for real while avoiding network/API calls.

2. **Real `fs` operations** — The mock `downloadAudioChunk`/`downloadVideoChunk` write tiny files at `outputPath` so that `fs.unlinkSync()` in `index.js` works naturally. No need to mock `fs`.

3. **SSE via raw HTTP** — Use Node's `http.get` to consume SSE, not `EventSource` (browser-only). Parse `data: {...}\n\n` lines manually.

4. **Session isolation** — Clear all in-memory Maps in `beforeEach` so tests don't leak state.

5. **`globalThis.fetch` spy** — Only needed for translate tests. Since `media.js` is fully mocked, `fetch` is only called by the translate endpoint. Use `vi.spyOn(globalThis, 'fetch')` scoped to translate tests.

## Verification

```bash
# Run only integration tests
cd server && npx vitest run integration.test.js

# Run all server tests (unit + integration)
cd server && npm test

# Verbose output for debugging
cd server && npx vitest run integration.test.js --reporter=verbose
```

Expected: 31 passing tests, no network calls, completes in <10s.
