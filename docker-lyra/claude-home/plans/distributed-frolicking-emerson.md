# Russian Video Transcription App - Implementation Plan

## Overview
Transform the French document reader into a Russian video transcription app with:
- Video URL input (ok.ru, YouTube, etc.) via yt-dlp
- OpenAI Whisper API transcription with word-level timestamps
- Synced video playback with highlighted transcript
- Click-to-translate Russian → English

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND (React)                         │
├─────────────────────────────────────────────────────────────────┤
│  VideoInput        VideoPlayer         TranscriptPanel          │
│  (URL paste)  ←→   (HTML5 video)  ←→   (word highlighting)     │
│                         ↓                     ↓                  │
│                   currentTime sync      click → translate       │
│                                         click → seek video      │
└─────────────────────────────────────────────────────────────────┘
                              ↓ API calls
┌─────────────────────────────────────────────────────────────────┐
│                      BACKEND (Express.js)                        │
├─────────────────────────────────────────────────────────────────┤
│  POST /api/transcribe                                            │
│    1. yt-dlp: download audio from URL                           │
│    2. OpenAI Whisper API: transcribe with word timestamps       │
│    3. Return: { videoUrl, transcript: [{word, start, end}...] } │
│                                                                  │
│  POST /api/translate                                             │
│    → Proxy to Google Translate (hides API key)                  │
└─────────────────────────────────────────────────────────────────┘
```

## Data Structures

```typescript
interface WordTimestamp {
  word: string;
  start: number;  // seconds
  end: number;    // seconds
}

interface Transcript {
  words: WordTimestamp[];
  segments: { text: string; start: number; end: number }[];
  language: string;
  duration: number;
}

interface VideoState {
  url: string;           // direct video URL for playback
  transcript: Transcript;
  currentTime: number;
  currentWordIndex: number;
}
```

## Implementation Steps

### Phase 1: Backend Setup
1. Create `server/` directory with Express.js
2. Install dependencies: `express`, `openai`, `yt-dlp-exec`
3. Implement `/api/transcribe` endpoint:
   - Accept video URL
   - Use yt-dlp to extract audio
   - Send to OpenAI Whisper with `timestamp_granularities: ["word"]`
   - Return transcript + direct video URL

4. Implement `/api/translate` endpoint:
   - Proxy Russian → English translation
   - Cache translations server-side

### Phase 2: Frontend - Video Input
1. Replace `FileUpload.tsx` → `VideoInput.tsx`
   - URL input field
   - "Transcribe" button
   - Loading state during processing

2. Update `App.tsx` state management
   - Store video URL + transcript
   - Handle transcription API calls

### Phase 3: Frontend - Video Player
1. Create `VideoPlayer.tsx`
   - HTML5 `<video>` element
   - Track `currentTime` via `timeupdate` event
   - Expose seek function for transcript clicks

2. Create `TranscriptPanel.tsx`
   - Display words with highlighting
   - Current word highlighted based on video time
   - Click word → seek video + show translation
   - Auto-scroll to keep current word visible

### Phase 4: Translation Integration
1. Update tokenizer for Russian (Cyrillic)
2. Add Russian to language detection
3. Reuse `WordPopup.tsx` with Russian support
4. Update Web Speech API for Russian pronunciation (`ru-RU`)

### Phase 5: Polish
1. Settings panel for OpenAI API key
2. Loading states and error handling
3. Keyboard shortcuts (space = play/pause)
4. Mobile responsive layout

## Files to Modify/Create

### New Files
- `server/index.js` - Express backend
- `server/package.json` - Backend dependencies
- `src/components/VideoInput.tsx` - URL input
- `src/components/VideoPlayer.tsx` - Video player
- `src/components/TranscriptPanel.tsx` - Synced transcript

### Modified Files
- `src/App.tsx` - New state management for video/transcript
- `src/types/index.ts` - New types for timestamps
- `src/components/WordPopup.tsx` - Russian language support
- `src/components/SettingsPanel.tsx` - OpenAI API key input
- `package.json` - Add concurrently for running both servers

### Files to Remove/Deprecate
- `src/components/FileUpload.tsx` - No longer needed
- `src/components/TextDisplay.tsx` - Replaced by VideoPlayer + TranscriptPanel
- `src/services/fileParser.ts` - No longer needed
- `src/services/tokenizer.ts` - Whisper handles segmentation

## Dependencies

### Backend (new)
```json
{
  "express": "^4.18",
  "openai": "^4.0",
  "yt-dlp-exec": "^1.0",
  "cors": "^2.8"
}
```

### Frontend (additions)
```json
{
  "concurrently": "^8.0"  // Run frontend + backend together
}
```

### System Requirements
- yt-dlp installed globally (`brew install yt-dlp` or `pip install yt-dlp`)

## API Details

### OpenAI Whisper Request
```javascript
const response = await openai.audio.transcriptions.create({
  file: audioFile,
  model: "whisper-1",
  response_format: "verbose_json",
  timestamp_granularities: ["word"],
  language: "ru"
});
// Returns: { words: [{word, start, end}, ...], segments: [...] }
```

### yt-dlp Usage
```javascript
import ytdlp from 'yt-dlp-exec';

// Get direct video URL for playback
const info = await ytdlp(url, { dumpJson: true });
const videoUrl = info.url; // Direct stream URL

// Download audio for Whisper
await ytdlp(url, {
  extractAudio: true,
  audioFormat: 'mp3',
  output: '/tmp/audio.mp3'
});
```

## Verification

1. **Backend**:
   - `curl -X POST http://localhost:3001/api/transcribe -d '{"url":"..."}'`
   - Verify returns transcript with word timestamps

2. **Frontend**:
   - Paste ok.ru URL
   - Video should load and play
   - Words highlight as video plays
   - Click word → translation popup + video seeks

3. **Full flow**:
   - Paste: `https://m.ok.ru/video/7389692627506`
   - Wait for transcription (may take 30-60s)
   - Play video, verify sync
   - Click Russian words, verify translation
