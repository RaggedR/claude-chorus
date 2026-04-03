# Full-Stack Dart Rewrite Plan

## Overview
Rewrite the Russian Video Transcription app as a full-stack Dart application:
- **Backend**: Dart with `shelf` for HTTP server
- **Frontend**: Flutter Web (thin client)
- **Approach**: TDD - tests first

## Project Structure

```
/Users/robin/git/french/dart_app/
├── backend/
│   ├── bin/
│   │   └── server.dart              # Entry point
│   ├── lib/
│   │   ├── server.dart              # Shelf router setup
│   │   ├── services/
│   │   │   ├── media_service.dart   # yt-dlp/ffmpeg wrapper
│   │   │   ├── transcription_service.dart  # OpenAI Whisper
│   │   │   ├── chunking_service.dart       # Smart chunking
│   │   │   └── storage_service.dart        # Session/file storage
│   │   ├── handlers/
│   │   │   ├── analyze_handler.dart
│   │   │   ├── session_handler.dart
│   │   │   ├── chunk_handler.dart
│   │   │   ├── progress_handler.dart  # SSE
│   │   │   └── translate_handler.dart
│   │   └── models/
│   │       ├── session.dart
│   │       ├── chunk.dart
│   │       ├── transcript.dart
│   │       └── progress.dart
│   ├── test/
│   │   ├── services/
│   │   │   ├── media_service_test.dart
│   │   │   ├── transcription_service_test.dart
│   │   │   └── chunking_service_test.dart
│   │   └── handlers/
│   │       └── analyze_handler_test.dart
│   └── pubspec.yaml
│
├── frontend/
│   ├── lib/
│   │   ├── main.dart
│   │   ├── app.dart                 # State machine
│   │   ├── services/
│   │   │   └── api_service.dart     # HTTP + SSE client
│   │   ├── models/                  # Shared with backend
│   │   ├── screens/
│   │   │   ├── input_screen.dart
│   │   │   ├── analyzing_screen.dart
│   │   │   ├── chunk_menu_screen.dart
│   │   │   └── player_screen.dart
│   │   └── widgets/
│   │       ├── progress_bar.dart
│   │       ├── video_player.dart
│   │       ├── transcript_panel.dart
│   │       └── word_popup.dart
│   ├── test/
│   │   └── widget_test.dart
│   └── pubspec.yaml
│
└── shared/                          # Shared models (optional)
    └── lib/
        └── models.dart
```

## Phase 1: Backend Tests (TDD)

### 1.1 Media Service Tests
```dart
// test/services/media_service_test.dart
group('MediaService', () {
  test('downloadAudioChunk calls yt-dlp with correct args', () async {
    // Mock Process.run
    // Verify: --extract-audio, --audio-format mp3, --download-sections
  });

  test('downloadVideoChunk calls yt-dlp with correct args', () async {
    // Verify: format worst[ext=mp4], --force-keyframes-at-cuts
  });

  test('progress callback fires during download', () async {
    // Verify onProgress called with increasing percentages
  });
});
```

### 1.2 Transcription Service Tests
```dart
// test/services/transcription_service_test.dart
group('TranscriptionService', () {
  test('transcribeAudio sends correct request to OpenAI', () async {
    // Mock HTTP client
    // Verify multipart form with audio file
  });

  test('parses word timestamps correctly', () async {
    // Sample response → WordTimestamp objects
  });
});
```

### 1.3 Chunking Service Tests
```dart
// test/services/chunking_service_test.dart
group('ChunkingService', () {
  test('creates ~3 minute chunks', () {
    // 10 min transcript → 3-4 chunks
  });

  test('breaks at silence gaps >= 0.5s', () {
    // Chunks end at natural pauses
  });

  test('merges final chunk if < 2 min', () {
    // Final short chunk merges with previous
  });

  test('getChunkTranscript adjusts timestamps to 0-based', () {
    // Words at 180-200s → 0-20s
  });
});
```

## Phase 2: Backend Implementation

### 2.1 Core Services

**MediaService** - Wraps yt-dlp/ffmpeg:
```dart
class MediaService {
  Future<AudioResult> downloadAudioChunk(
    String url,
    String outputPath,
    int startTime,
    int endTime, {
    void Function(ProgressUpdate)? onProgress,
  });

  Future<VideoResult> downloadVideoChunk(
    String url,
    String outputPath,
    int startTime,
    int endTime, {
    void Function(ProgressUpdate)? onProgress,
  });
}
```

**TranscriptionService** - OpenAI Whisper:
```dart
class TranscriptionService {
  Future<Transcript> transcribe(
    String audioPath, {
    String language = 'ru',
    void Function(ProgressUpdate)? onProgress,
  });
}
```

### 2.2 API Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| POST | /api/analyze | Start analysis, return sessionId |
| GET | /api/session/:id | Get session state + chunks |
| GET | /api/session/:id/chunk/:chunkId | Get chunk video + transcript |
| POST | /api/download-chunk | Download specific chunk |
| POST | /api/load-more | Load next batch of chunks |
| GET | /api/progress/:id | SSE stream |
| POST | /api/translate | Google Translate proxy |
| DELETE | /api/session/:id | Cleanup |

### 2.3 Progress Logging (Terminal + SSE)

```dart
void sendProgress(String sessionId, ProgressUpdate update) {
  // 1. Print to terminal
  final bar = '█' * (update.percent ~/ 5) + '░' * (20 - update.percent ~/ 5);
  stdout.write('\r[${update.type}] $bar ${update.percent}% - ${update.message}');

  // 2. Send to SSE clients
  _sseClients[sessionId]?.forEach((client) {
    client.sink.add('data: ${jsonEncode(update.toJson())}\n\n');
  });
}
```

## Phase 3: Frontend (Flutter Web)

### 3.1 State Machine
```dart
enum AppView { input, analyzing, chunkMenu, loadingChunk, player }

class AppState extends ChangeNotifier {
  AppView view = AppView.input;
  String? sessionId;
  List<VideoChunk> chunks = [];
  // ... minimal UI state only
}
```

### 3.2 Thin Client Pattern
- Frontend NEVER calls yt-dlp/ffmpeg directly
- Frontend NEVER manages download progress internally
- All state comes from backend via:
  - `GET /api/session/:id` for session state
  - `GET /api/progress/:id` for real-time updates

### 3.3 Key Widgets
- `ProgressBar` - Shows download/transcription progress
- `VideoPlayerWidget` - HTML5 video with time sync
- `TranscriptPanel` - Word highlighting, click-to-translate
- `ChunkMenuGrid` - Chunk selection with status indicators

## Phase 4: Commands

### Start Backend
```bash
cd /Users/robin/git/french/dart_app/backend
dart run bin/server.dart
# Server running on http://localhost:3001
```

### Start Frontend (Development)
```bash
cd /Users/robin/git/french/dart_app/frontend
flutter run -d chrome --web-port=5173
```

### Run Tests
```bash
# Backend tests
cd backend && dart test

# Frontend tests
cd frontend && flutter test
```

## Dependencies

### Backend (pubspec.yaml)
```yaml
dependencies:
  shelf: ^1.4.0
  shelf_router: ^1.1.0
  http: ^1.1.0
  path: ^1.8.0

dev_dependencies:
  test: ^1.24.0
  mocktail: ^1.0.0
```

### Frontend (pubspec.yaml)
```yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^1.1.0
  provider: ^6.0.0
  video_player: ^2.8.0

dev_dependencies:
  flutter_test:
    sdk: flutter
```

## Verification

1. **Unit Tests**: `dart test` passes
2. **Integration Test**:
   - Start backend: `dart run bin/server.dart`
   - Submit ok.ru URL
   - Verify terminal shows progress bars
   - Verify frontend shows matching progress
3. **E2E Flow**:
   - Input URL → Analyzing → Chunk Menu → Player
   - Video plays with synced transcript
   - Click word → translation popup

## Migration Notes

- Keep existing Node.js server as reference
- New Dart app in `/dart_app/` directory
- Can run both in parallel during development
- Delete Node.js version after Dart is stable
