# Plan: Run Whisper STT on TTS audio for accurate text-mode timestamps

## Context

Text mode (lib.ru) currently estimates word timestamps by distributing audio duration proportionally across words by character length (`estimateWordTimestamps`). This produces poor sync because TTS speech varies in speed — pauses at punctuation, faster/slower words, etc. The fix: run the TTS audio back through Whisper to get real word-level timestamps, then align them to the original text.

## Approach

Create a new function `transcribeAndAlignTTS(text, audioPath, options)` in `media.js` that:
1. Calls existing `transcribeAudioChunk(audioPath)` to get Whisper word timestamps
2. Calls existing `alignWhisperToOriginal(whisperWords, originalWords)` to map them back to original text
3. Builds the same `{words, segments, language, duration}` shape that `estimateWordTimestamps` returns

Then replace `estimateWordTimestamps` calls with `transcribeAndAlignTTS` in all 3 call sites.

## Files to modify

### `server/media.js`
- **Add** `transcribeAndAlignTTS(text, audioPath, options)` function near `estimateWordTimestamps` (~line 1175)
  - Calls `transcribeAudioChunk(audioPath, options)` (reuse existing, line 496)
  - Splits `text` into original words
  - Calls `alignWhisperToOriginal(whisperResult.words, originalWords)` (reuse existing, line 1187)
  - Builds segments from aligned words (~20 words each, same as `estimateWordTimestamps`)
  - Returns `{words, segments, language: 'ru', duration}`
- **Export** `transcribeAndAlignTTS`
- Keep `estimateWordTimestamps` as a fallback (no deletion)

### `server/index.js` — 3 call sites
1. **Line 1695** (download-chunk text mode): Replace `estimateWordTimestamps(chunkText, duration)` → `await transcribeAndAlignTTS(chunkText, audioPath, { onProgress })`; add `trackCost(req.uid, costs.whisper(duration))` after
2. **Line 1891** (prefetch text mode): Same replacement with `silentProgress`; add Whisper cost tracking
3. Update comment on line 1693 from "estimate word timestamps" to "transcribe for real timestamps"

### `server/scripts/generate-demo.js`
- **Line 194**: Replace `estimateWordTimestamps(chunk.text, duration)` → `await transcribeAndAlignTTS(chunk.text, audioPath)` with Whisper cost note in comment

### Tests

#### `server/media.test.js`
- Add `transcribeAndAlignTTS` tests:
  - Calls `transcribeAudioChunk` then `alignWhisperToOriginal`
  - Returns correct shape `{words, segments, language, duration}`
  - Builds segments of ~20 words each

#### `server/integration.test.js`
- Update mock for `media.js` to include `transcribeAndAlignTTS` mock
- Update text-mode download-chunk and prefetch test expectations

#### `server/usage.test.js`
- No changes needed (Whisper cost function already tested)

## Key reuse

| Existing function | File | Line | Purpose |
|---|---|---|---|
| `transcribeAudioChunk()` | `media.js:496` | Whisper API call with word timestamps |
| `alignWhisperToOriginal()` | `media.js:1187` | Two-pointer fuzzy alignment |
| `costs.whisper()` | `usage.js:269` | Cost tracking ($0.006/min) |

## Verification

1. `cd server && npx vitest run media.test.js` — unit tests pass
2. `cd server && npx vitest run integration.test.js` — integration tests pass
3. `npm test` — full test suite passes
4. Manual test: run `npm run dev`, paste a lib.ru URL, load a chunk, verify words highlight in sync with audio playback
