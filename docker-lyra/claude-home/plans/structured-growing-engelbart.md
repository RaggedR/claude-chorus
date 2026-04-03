# Code Review Fixes for ~/git/russian

## Context
Full code review identified 15 issues across security, performance, and code quality. User approved fixing all except unifying handleAnalyzeVideo/handleAnalyzeText (kept separate by design). This plan covers all remaining fixes in dependency order.

## Files Modified

| File | Changes |
|------|---------|
| `server/package.json` | Add `lru-cache` dependency |
| `server/index.js` | URL validation, CORS, LRU caches, signed URLs, input limits, req.session rename, health check, refactor SSE/progress to separate module, fix race condition |
| `server/media.js` | Extract shared UA constant |
| `server/progress.js` | **NEW** — extracted SSE + terminal rendering |
| `server/session-store.js` | **NEW** — extracted session CRUD + GCS persistence |
| `src/App.tsx` | Fix XSS (remove dangerouslySetInnerHTML) |
| `src/components/TranscriptPanel.tsx` | Fix stale useCallback dependency |
| `firestore.rules` | Add data shape validation |

## Plan (in execution order)

### Phase 1: Quick security fixes (low-risk, high-value)

**1a. XSS fix — `src/App.tsx:793-798`**
Replace `dangerouslySetInnerHTML` with a safe `ErrorMessage` component that splits text on URL regex and renders `<a>` tags as React elements (no raw HTML injection).

**1b. URL validation — `server/index.js` `/api/analyze` handler**
Add URL validation after the `if (!url)` check:
```js
// Only allow ok.ru video URLs and lib.ru text URLs
const parsedUrl = new URL(url); // catch invalid URLs
const isOkRu = parsedUrl.hostname === 'ok.ru' || parsedUrl.hostname.endsWith('.ok.ru');
const isLibRu = isLibRuUrl(url);
if (!isOkRu && !isLibRu) {
  return res.status(400).json({ error: 'Only ok.ru and lib.ru URLs are supported' });
}
```

**1c. CORS restriction — `server/index.js:457`**
Replace `app.use(cors())` with origin whitelist:
```js
app.use(cors({
  origin: [
    /^https:\/\/russian-transcription.*\.run\.app$/,
    'http://localhost:5173',
    'http://localhost:3001',
  ],
}));
```
This covers Cloud Run (production), Vite dev server, and direct backend access.

**1d. Input length validation — `server/index.js`**
- `/api/translate`: reject if `word.length > 200`
- `/api/extract-sentence`: reject if `text.length > 5000` or `word.length > 200`

**1e. Fix stale useCallback dep — `src/components/TranscriptPanel.tsx:153`**
Change `[transcript.segments]` to `[transcript.words]`.

**1f. Firestore rules — `firestore.rules`**
Add shape validation:
```
allow write: if request.auth.uid == userId
  && request.resource.data.cards is list;
```

### Phase 2: Memory & performance fixes

**2a. Add lru-cache dependency**
```bash
cd server && npm install lru-cache
```

**2b. LRU caches — `server/index.js`**
Replace unbounded Maps with LRU caches:
- `translationCache` → LRU max 10,000 entries
- `analysisSessions` → LRU max 50 entries (these are large objects)

Keep `urlSessionCache` as a Map (bounded by session count, evicted on TTL) and `progressClients` (bounded by active SSE connections, cleaned on disconnect).

**2c. Fix race condition — `server/index.js` download-chunk handler**
Replace the busy-poll loop with a Promise-based approach:
- When prefetch starts, store a `Promise` on the chunk object: `chunk.downloadPromise = new Promise(...)`
- When prefetch completes/fails, resolve/reject the promise
- In download-chunk handler, if `chunk.status === 'downloading'` and `chunk.downloadPromise` exists, `await chunk.downloadPromise` instead of polling

### Phase 3: Security hardening

**3a. Signed URLs — `server/index.js`**
Replace `makePublic()` + direct GCS URL with `getSignedUrl()`:
```js
const [signedUrl] = await bucket.file(gcsFileName).getSignedUrl({
  action: 'read',
  expires: Date.now() + 24 * 60 * 60 * 1000, // 24h
});
```
Apply in 4 locations: video upload (2x), audio upload (2x) — both in download-chunk handler and prefetchNextChunk.

**Note**: IAM permission already granted (2026-02-18):
```
gcloud iam service-accounts add-iam-policy-binding \
  96900302527-compute@developer.gserviceaccount.com \
  --member="serviceAccount:96900302527-compute@developer.gserviceaccount.com" \
  --role="roles/iam.serviceAccountTokenCreator" \
  --project=russian-transcription
```
Will document this in deploy.sh as a prerequisite comment.

**3b. `req.session` rename — `server/index.js`**
Rename `req.session` to `req.analysisSession` in `requireSessionOwnership` and all route handlers that use it, to avoid shadowing Express's built-in session property.

### Phase 4: Code quality improvements

**4a. Extract shared User-Agent constant — `server/media.js` + `server/index.js`**
Create a shared constant in `media.js`:
```js
export const BROWSER_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36';
```
Import and use in `index.js` proxy routes.

**4b. Improve health check — `server/index.js`**
Add dependency checks:
```js
app.get('/api/health', (req, res) => {
  res.json({
    status: 'ok',
    openai: !!process.env.OPENAI_API_KEY,
    translate: !!process.env.GOOGLE_TRANSLATE_API_KEY,
    gcs: !IS_LOCAL,
  });
});
```

**4c. Extract session-store module — `server/session-store.js` (NEW)**
Move from `index.js`:
- `saveSession`, `getSession`, `deleteGcsFile`, `deleteSessionAndVideos`
- `getAnalysisSession`, `setAnalysisSession`
- `cleanupOldSessions`, `rebuildUrlCache`
- `getCachedExtraction`, `cacheExtraction`
- `extractVideoId`, `normalizeUrl`, `getCachedSession`, `cacheSessionUrl`
- LRU caches: `analysisSessions`, `urlSessionCache`, `translationCache`
- Maps: `localSessions`

**4d. Extract progress module — `server/progress.js` (NEW)**
Move from `index.js`:
- `progressClients` Map
- `sendProgress`, `printProgress`, `renderProgressBar`
- `createProgressCallback`
- `TERM_COLORS`, `TYPE_STYLES`
- `friendlyErrorMessage`

## NOT doing (per user request)
- Unifying handleAnalyzeVideo/handleAnalyzeText (kept separate)
- Unifying handleSelectVideoChunk/handleSelectTextChunk (kept separate)

## Verification
1. `cd server && npm test` — all 7 backend test files pass
2. `cd /Users/robin/git/russian && npm run build` — frontend builds without errors
3. `cd /Users/robin/git/russian && npm run test:e2e` — all 14 Playwright suites pass
4. Manual check: XSS fix renders error URLs as clickable links without dangerouslySetInnerHTML
5. Manual check: CORS headers present on API responses
