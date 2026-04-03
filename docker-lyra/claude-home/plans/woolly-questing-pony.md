# Smart Video Chunking System

## Goal

Transform the app to handle large videos by chunking them into ~3 minute segments at natural pauses. Users select which chunk to download, reducing wait time to 2-3 minutes per chunk.

## New User Flow

```
1. User pastes URL
2. Audio downloads (fast, low quality)
3. Whisper transcribes → identifies natural pause points
4. App shows chunk menu: "Part 1: 0:00-3:12", "Part 2: 3:12-6:45", etc.
5. User clicks a chunk → video downloads for that chunk only
6. User studies that chunk
7. User can return to menu and select another chunk
```

## Architecture

### Phase 1: Analyze (~30-60s)
- Download FULL audio (4 concurrent fragments, HIGH quality for accuracy)
- Transcribe entire audio with Whisper
- Create smart chunks from segment boundaries (natural pauses)
- Return chunk menu to user

### Phase 2: Download Chunk (Per user selection - ~60-90s)
- Download VIDEO only for selected time range (LOW quality for speed)
- Use ffmpeg to extract just that segment
- Transcript already available from Phase 1
- Display progress bar
- Play when ready

## Smart Chunking Algorithm

```javascript
// Target: ~180 seconds per chunk
// End chunks at Whisper segment boundaries (natural pauses)
// Prefer gaps > 0.5 seconds between segments

for each segment:
  add to current chunk
  if chunk duration >= 180s AND next gap > 0.5s:
    finalize chunk
    start new chunk
```

## API Endpoints

### `POST /api/analyze` (Phase 1)
```
Request:  { url, openaiApiKey }
Response: { sessionId, title, totalDuration, chunks: [...] }
```

### `GET /api/progress/:sessionId` (SSE)
```
Events: audio_progress, transcription_progress, video_progress
Data:   { progress: 0-100, status: 'active'|'complete'|'error' }
```

### `POST /api/download-chunk` (Phase 2)
```
Request:  { sessionId, chunkId, startTime, endTime }
Response: { videoUrl, transcript: { words, segments } }
```

## Progress Bars (3 bars, 2 visible at a time)

```
Phase 1 - Analysis:
  [Audio Download    ████████░░ 80%]  ← active
  [Transcription     ██░░░░░░░░ 20%]  ← starts when audio ~50%

When audio completes:
  [Audio Download    ██████████ ✓  ]  ← complete (fades out)
  [Transcription     ██████████ ✓  ]  ← completes

Phase 2 - Chunk Download:
  [Downloading Part 3 ██████░░░░ 60%]  ← single bar
```

## New Frontend Components

| Component | Purpose |
|-----------|---------|
| `ChunkMenu.tsx` | Grid of chunk cards with preview text |
| `ProgressBar.tsx` | Single animated progress bar |
| `ProgressStack.tsx` | Manages 2-bar display with transitions |

## App State Machine

```
'input' → analyze → 'chunk-menu' → select chunk → 'loading-chunk' → 'player'
                         ↑                                              ↓
                         └──────────── "Back to chunks" ────────────────┘
```

## Files to Modify

### Backend
| File | Changes |
|------|---------|
| `server/index.js` | Add /api/analyze, /api/progress (SSE), /api/download-chunk |
| `server/chunking.js` | **NEW** - chunking algorithm |

### Frontend
| File | Changes |
|------|---------|
| `src/types/index.ts` | Add VideoChunk, ChunkingSession, ProgressState types |
| `src/App.tsx` | Add view state machine, chunk selection flow |
| `src/services/api.ts` | Add SSE subscription for progress |
| `src/components/ChunkMenu.tsx` | **NEW** - chunk selection UI |
| `src/components/ProgressBar.tsx` | **NEW** - progress bar component |
| `src/components/ProgressStack.tsx` | **NEW** - stacked progress display |
| `src/components/VideoInput.tsx` | Show progress during analysis |

## yt-dlp Flags

```bash
# Audio (Phase 1) - HIGH quality for accurate transcription
yt-dlp -x --audio-format mp3 --audio-quality 0 --concurrent-fragments 4

# Video (Phase 2) - LOW quality for fast download
yt-dlp -f "worst[ext=mp4]/worst" --concurrent-fragments 4
```

## ffmpeg Chunk Extraction

```bash
# Fast seek + copy (no re-encoding)
ffmpeg -ss 192 -i <video_url> -t 180 -c copy -avoid_negative_ts make_zero output.mp4
```

## Edge Cases

| Case | Handling |
|------|----------|
| Video < 3 minutes | Single chunk, skip menu, download directly |
| SSE disconnects | Fallback to polling every 2s |
| Chunk already downloaded | Serve from cache immediately |
| Download fails | Show retry button, keep menu accessible |

## Verification

1. Submit a 10+ minute ok.ru video
2. Should see chunk menu within ~60 seconds
3. Select a chunk → downloads in ~60-90 seconds
4. Video plays with synced transcript
5. "Back to chunks" returns to menu
6. Select different chunk → works correctly
7. Previously downloaded chunks load instantly
