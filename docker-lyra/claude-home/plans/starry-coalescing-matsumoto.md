# Plan: Modular Extraction of media.js and session-store.js

## Context

The backend has two monoliths: `server/media.js` (1345 lines, 18 functions, 5 external services) and `server/session-store.js` (398 lines, 16 exports mixing CRUD/caching/GCS). This plan extracts them into clean modules using Facade and Repository patterns. Route handlers in `index.js` are NOT touched — a re-export barrel preserves all existing import paths.

The work is structured for **sub-agent parallelization** to minimize token cost.

---

## Part 1: Extract media.js → server/media/ (Facade Pattern)

### Target Structure

```
server/media/
  text-utils.js        ← pure functions (zero deps)
  progress-utils.js    ← heartbeat, progress helpers, constants
  download.js          ← yt-dlp/ffmpeg (getOkRuVideoInfo, downloadAudioChunk, downloadVideoChunk, getAudioDuration)
  transcription.js     ← Whisper + GPT-4o (transcribeAudioChunk, addPunctuation, lemmatizeWords)
  text-extraction.js   ← lib.ru fetch (isLibRuUrl, fetchLibRuText)
  tts.js               ← OpenAI TTS + alignment (generateTtsAudio, transcribeAndAlignTTS)
server/media.js        ← thin re-export barrel (preserves all consumer imports)
```

### Round 1 — Foundation modules (2 parallel agents)

**Agent A → `server/media/text-utils.js`**
- Move: `stripPunctuation` (L565-567), `editDistance` (L573-596), `isFuzzyMatch` (L602-607), `estimateWordTimestamps` (L1145-1175), `alignWhisperToOriginal` (L1187-1311)
- Imports: none
- Exports: all 5 functions

**Agent B → `server/media/progress-utils.js`**
- Move: `BROWSER_UA` (L14), `ESTIMATED_EXTRACTION_TIME` (L17), `YTDLP_TIMEOUT_MS` (L52), `mapProgress` (L26-28), `computeRanges` (L36-48), `createHeartbeat` (L91-118)
- Imports: none
- Exports: all 3 functions + 3 constants

### Round 2 — Service modules (4 parallel agents)

**Agent C → `server/media/download.js`**
- Move: `getOkRuVideoInfo` (L59-80), `downloadAudioChunk` (L130-361), `downloadVideoChunk` (L374-485), `getAudioDuration` (L1120-1136)
- Imports from: `./progress-utils.js`, `../chunking.js`
- Exports: all 4 functions

**Agent D → `server/media/transcription.js`**
- Move: `transcribeAudioChunk` (L496-559), `addPunctuation` (L620-791), `lemmatizeWords` (L804-905)
- Imports from: `./text-utils.js`, `./progress-utils.js`
- Exports: all 3 functions

**Agent E → `server/media/text-extraction.js`**
- Move: `isLibRuUrl` (L912-919), `fetchLibRuText` (L930-1051)
- Imports from: `./progress-utils.js` (BROWSER_UA only)
- Exports: both functions

**Agent F → `server/media/tts.js`**
- Move: `generateTtsAudio` (L1062-1113), `transcribeAndAlignTTS` (L1322-1345)
- Imports from: `./progress-utils.js`, `./transcription.js`, `./text-utils.js`
- Exports: both functions

### Round 3 — Barrel + cleanup (1 agent)

**Agent G → rewrite `server/media.js` as barrel**
- Replace 1345 lines with ~10 lines of re-exports
- Verify: `npm test` (all server tests pass through barrel)

### Why this is safe
- `media.test.js` imports from `./media.js` → barrel intercepts
- `integration.test.js` uses `vi.mock('./media.js')` → mocks the barrel, not sub-modules
- `index.js` imports from `./media.js` → unchanged
- `generate-demo.js` imports from `../media.js` → unchanged

---

## Part 2: Extract session-store.js (Repository Pattern)

### Target Structure

```
server/storage/
  session-repository.js   ← Session CRUD (getAnalysisSession, setAnalysisSession, deleteSessionAndVideos, etc.)
  url-cache.js            ← URL→session mapping (getCachedSession, cacheSessionUrl, 6h TTL)
  extraction-cache.js     ← yt-dlp info cache (getCachedExtraction, cacheExtraction, 2h TTL)
  translation-cache.js    ← translation LRU (translationCache)
  gcs.js                  ← GCS primitives (init, getSignedMediaUrl, deleteGcsFile, bucket ref)
  url-utils.js            ← pure functions (extractVideoId, normalizeUrl)
server/session-store.js   ← thin re-export barrel
```

### Round 4 — Storage modules (3 parallel agents)

**Agent H → `server/storage/gcs.js` + `server/storage/url-utils.js`**
- `gcs.js`: `init()`, `getSignedMediaUrl()`, `deleteGcsFile()`, bucket/IS_LOCAL state
- `url-utils.js`: `extractVideoId()`, `normalizeUrl()`
- Both are foundation — no deps on other storage modules

**Agent I → `server/storage/url-cache.js` + `server/storage/extraction-cache.js` + `server/storage/translation-cache.js`**
- Three small cache modules, each owning one Map/LRU + TTL logic
- Import from: `./gcs.js` (for GCS reads in extraction-cache)

**Agent J → `server/storage/session-repository.js`**
- `getAnalysisSession`, `setAnalysisSession`, `saveSession`, `getSession`, `deleteSessionAndVideos`, `cleanupOldSessions`, `rebuildUrlCache`
- Imports from: `./gcs.js`, `./url-cache.js`
- Owns the LRU cache (analysisSessions) and localSessions Map

### Round 5 — Storage barrel (1 agent)

**Agent K → rewrite `server/session-store.js` as barrel**
- Re-export everything from `server/storage/` modules
- Verify: `npm test`

---

## Execution Summary

| Round | Agents | Creates | Modifies | Can Parallel? |
|-------|--------|---------|----------|---------------|
| 0     | 1 (main) | `server/media/` dir, `server/storage/` dir | — | — |
| 1     | 2 | text-utils.js, progress-utils.js | — | Yes |
| 2     | 4 | download.js, transcription.js, text-extraction.js, tts.js | — | Yes |
| 3     | 1 | — | media.js (→ barrel) | No (test) |
| 4     | 3 | gcs.js, url-utils.js, url-cache.js, extraction-cache.js, translation-cache.js, session-repository.js | — | Yes |
| 5     | 1 | — | session-store.js (→ barrel) | No (test) |

**Total: 5 rounds, 12 agent invocations, 0 route handler changes.**

Token cost estimate: Each extraction agent gets ~2K lines of context (source function + target file write). Foundation agents (A, B, H) are cheapest (~1K context). The barrel agents (G, K) are cheapest of all (~500 lines).

---

## Verification

After each barrel round (3 and 5):

```bash
# All server tests (media + integration + usage + stripe + dictionary)
cd server && npx vitest run

# Frontend typecheck
npm run build

# Full suite
npm test
```

After all rounds:
```bash
# E2E (mocks at network level, unaffected but good sanity check)
npm run test:e2e
```

---

## Files NOT modified

- `server/index.js` — route handlers untouched, imports unchanged
- `server/media.test.js` — imports from `./media.js` (barrel), unchanged
- `server/integration.test.js` — `vi.mock('./media.js')` still works
- `server/dictionary.js` — no coupling, unchanged
- `server/chunking.js` — no coupling, unchanged
- `server/progress.js` — independent, unchanged
- `server/auth.js` — independent, unchanged
- `server/usage.js` — independent, unchanged
- `server/stripe.js` — independent, unchanged
- All frontend files — backend-only change
