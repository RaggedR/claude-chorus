# Plan: Pre-processed Demo Content for First-Time Users

## Context

First-time users currently must paste a URL and wait through a slow download/transcription process (90-120s for ok.ru videos). This is a bad first impression. We'll add two "try a demo" buttons on the landing page that instantly load pre-processed content — one video and one text — letting users experience the app immediately.

Demo URLs:
- **Video**: `https://ok.ru/video/400776431053`
- **Text**: `http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0080.shtml`

## Architecture

The demo system has three parts:

1. **Generation script** — runs the normal pipeline once, saves transcript JSON + uploads media to GCS
2. **Backend endpoint** — `POST /api/demo` creates a real session from pre-baked data (instant, no API calls)
3. **Frontend buttons** — "Try Demo Video" / "Try Demo Text" on the input page

The demo sessions are real sessions — they go through the same ownership, chunk loading, word click, and deck flows. No special-casing in the player.

## Implementation Steps

### 1. Generation Script (`server/scripts/generate-demo.js`)

A standalone Node.js script that:
- Processes each demo URL through the existing `media.js` pipeline (transcribe, punctuate, lemmatize, chunk)
- Limits output to the first ~10 minutes of content (2-3 chunks)
- Saves transcript + chunk metadata as JSON: `server/demo/demo-video.json`, `server/demo/demo-text.json`
- Uploads media files to GCS under `demo/` prefix (e.g. `demo/video-chunk-0.mp4`, `demo/text-chunk-0.mp3`)
- Saves media files locally to `server/demo/media/` for local dev (gitignored)
- Requires: API keys (OpenAI), network access (ok.ru, lib.ru), GCS write access
- Run once, commit the JSON files, gitignore the media files

**Demo JSON structure:**
```json
{
  "title": "Video Title",
  "contentType": "video",
  "totalDuration": 180,
  "originalUrl": "https://ok.ru/video/400776431053",
  "hasMoreChunks": false,
  "chunks": [
    { "id": "chunk-0", "index": 0, "startTime": 0, "endTime": 180, "duration": 180, "previewText": "...", "wordCount": 250, "status": "ready" }
  ],
  "chunkTranscripts": [
    ["chunk-0", { "words": [...], "segments": [...], "language": "ru", "duration": 180 }]
  ],
  "gcsMediaKeys": { "chunk-0": "demo/video-chunk-0.mp4" },
  "localMediaFiles": { "chunk-0": "demo-video-chunk-0.mp4" }
}
```

### 2. Backend — `POST /api/demo` endpoint (`server/index.js`)

**Route**: `POST /api/demo` with `requireAuth` (no budget/rate-limit — no API calls made)
**Body**: `{ type: 'video' | 'text' }`
**Response**: Same shape as a cached `/api/analyze` response

Logic:
1. Read and cache the demo JSON file in memory (read once on first call)
2. Generate a new `crypto.randomUUID()` session ID
3. Resolve media URLs per chunk:
   - **Production (GCS)**: `getSignedMediaUrl(gcsMediaKey)` → 24h signed URL
   - **Local dev**: Check `server/demo/media/` exists → register in `localSessions` → serve via `/api/local-video/` or `/api/local-audio/`
4. Build session object with `uid: req.uid`, `status: 'ready'`, chunks with resolved media URLs, `chunkTranscripts` as a Map
5. Save via `setAnalysisSession(sessionId, session)`
6. Return `{ sessionId, status: 'cached', title, contentType, totalDuration, chunks, hasMoreChunks }`

The frontend's existing `handleAnalyzeVideo`/`handleAnalyzeText` cached-response handling (lines 400-416, 485-501 of App.tsx) takes over from here — auto-selecting if single chunk, showing chunk menu if multiple. All subsequent endpoints (`GET /api/session/:id/chunk/:chunkId`, translate, extract-sentence) work via normal session ownership.

### 3. Frontend — Demo Buttons (`src/App.tsx`)

Add a new section below the VideoInput/TextInput grid in the `view === 'input'` block:

```
[Video URL Input]  [Text URL Input]
        ── or try a demo ──
[Try Demo Video]   [Try Demo Text]
```

- Divider with "or try a demo" text (gray, centered)
- Two styled buttons matching the input cards
- `handleLoadDemo(type)` callback: sets contentType, calls `POST /api/demo`, handles cached response (same pattern as existing cached analyze handling)
- Add `data-testid` attributes for E2E testing

### 4. API Client (`src/services/api.ts`)

Add `loadDemo(type: 'video' | 'text')` function — simple POST wrapper.

### 5. GCS Lifecycle Exclusion (`deploy.sh`)

Update lifecycle rule to use `matchesPrefix` so the `demo/` prefix is excluded from 7-day auto-deletion:
```json
{ "action": {"type": "Delete"}, "condition": { "age": 7, "matchesPrefix": ["videos/", "sessions/", "cache/"] } }
```

### 6. `.gitignore`

Add `server/demo/media/` (large media files for local dev, not tracked in git).

## Files to Create/Modify

| File | Action | Purpose |
|------|--------|---------|
| `server/scripts/generate-demo.js` | Create | One-time generation script |
| `server/demo/demo-video.json` | Create (generated) | Pre-processed video data |
| `server/demo/demo-text.json` | Create (generated) | Pre-processed text data |
| `server/index.js` | Modify | Add `POST /api/demo` endpoint |
| `src/App.tsx` | Modify | Add demo buttons + handler |
| `src/services/api.ts` | Modify | Add `loadDemo()` function |
| `deploy.sh` | Modify | Update GCS lifecycle rule |
| `.gitignore` | Modify | Add `server/demo/media/` |

## Testing

### Backend tests (`server/integration.test.js` — add tests)
- `POST /api/demo` returns 400 for missing/invalid type
- Creates a session owned by the requesting user
- Returns cached-style response with ready chunks
- Session accessible via `GET /api/session/:id` afterward
- Chunk data accessible via `GET /api/session/:id/chunk/:chunkId`

### E2E tests (`e2e/tests/demo-flow.spec.ts` — new file)
- Demo video button visible on input page
- Demo text button visible on input page
- Clicking demo video → mock `/api/demo` → player with transcript
- Clicking demo text → mock `/api/demo` → audio player with transcript
- Word click works in demo mode (translation popup)
- "Load different video or text" returns to input

### Verification
1. Run generation script against both URLs
2. `npm test` — all existing + new tests pass
3. `npm run test:e2e` — demo flow E2E tests pass
4. Manual test: start app, click both demo buttons, verify instant player load
5. Verify demo content persists across server restarts (JSON checked into repo, media in GCS)
