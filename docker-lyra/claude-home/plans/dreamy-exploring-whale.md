# Thin Client Refactor Plan

## Goal
Make frontend a thin client. Backend owns all session state. Frontend only manages view state and playback.

## Current Problems
1. Frontend stores `ChunkingSession` with chunks, transcript, title - duplicates backend
2. Frontend tracks `downloadedChunks` Set - backend should know this
3. Frontend caches chunk videos in `cachedChunkVideos` Map - should be backend
4. API keys passed per-request from localStorage - security risk
5. Complex SSE cleanup logic in frontend

## Architecture After Refactor

### Frontend State (thin)
```typescript
// View state
view: 'input' | 'analyzing' | 'chunk-menu' | 'loading-chunk' | 'player'
sessionId: string | null  // Reference only

// Current playback (for active chunk)
videoUrl: string | null
transcript: Transcript | null
currentTime: number
seekTo: number | null

// UI
progress: ProgressState[]
error: string | null
```

### Backend State (complete)
```javascript
analysisSessions.get(sessionId) = {
  status: 'analyzing' | 'ready' | 'error',
  title, totalDuration, originalUrl,
  chunks: [{
    id, index, startTime, endTime, duration, previewText,
    status: 'pending' | 'downloading' | 'ready',  // NEW
    videoUrl: string | null  // NEW - set when ready
  }],
  chunkTranscripts: Map<chunkId, Transcript>  // NEW
}
```

## Changes

### 1. Backend: Enhance GET /api/session/:sessionId
Return full session state including chunk download status.
```javascript
// Response when status='ready'
{
  status: 'ready',
  title: string,
  totalDuration: number,
  chunks: [{ id, index, startTime, endTime, status, videoUrl? }]
}
```

### 2. Backend: Add GET /api/session/:sessionId/chunk/:chunkId
Get chunk video URL and transcript (if ready).
```javascript
// Response
{ videoUrl, transcript, title }
```

### 3. Backend: Update POST /api/download-chunk
After download completes, update session:
```javascript
chunk.status = 'ready';
chunk.videoUrl = videoUrl;
session.chunkTranscripts.set(chunkId, transcript);
```

### 4. Backend: Remove API key from request
Use only `process.env.OPENAI_API_KEY`. Remove from /api/analyze body.

### 5. Frontend: Simplify App.tsx
Remove:
- `chunkingSession` state
- `downloadedChunks` state
- `cachedChunkVideos` state
- `selectedChunk` state

Add:
- `sessionId` (string only)
- Fetch session data from backend when needed

### 6. Frontend: Update handleSelectChunk
```typescript
const handleSelectChunk = async (chunkId: string) => {
  // Fetch current session state
  const session = await apiRequest(`/api/session/${sessionId}`);
  const chunk = session.chunks.find(c => c.id === chunkId);

  if (chunk.status === 'ready') {
    // Fetch chunk data
    const data = await apiRequest(`/api/session/${sessionId}/chunk/${chunkId}`);
    setVideoUrl(data.videoUrl);
    setTranscript(data.transcript);
    setView('player');
  } else {
    // Trigger download, SSE will notify when ready
    setView('loading-chunk');
    await apiRequest('/api/download-chunk', { sessionId, chunkId });
  }
};
```

### 7. Frontend: ChunkMenu uses server chunk status
Pass `chunks` from session response directly. Show checkmarks based on `chunk.status === 'ready'`.

## Files to Modify

| File | Changes |
|------|---------|
| `server/index.js` | Add chunk status tracking, new endpoint, persist to GCS |
| `src/App.tsx` | Remove fat state, fetch from backend |
| `src/types/index.ts` | Remove ChunkingSession, add SessionResponse |
| `src/services/api.ts` | Add getSession, getChunk functions |
| `src/components/ChunkMenu.tsx` | Use chunk.status from props |
| `src/components/SettingsPanel.tsx` | Remove OpenAI key input |

## Verification
1. Start server: `npm run dev`
2. Enter ok.ru URL
3. Verify progress shows during analysis
4. Verify chunk menu shows all chunks
5. Click chunk - verify it downloads and plays
6. Refresh page - verify session recovers (chunk-menu shows)
7. Click same chunk - verify instant playback (cached on server)
8. Click different chunk - verify download starts
