# Memory

## Project: french (Russian Video Transcription)

### User Preferences
- **Word click = translate only, NOT seek.** Clicking a word in the transcript should show a translation popup. It should NOT seek/jump the video to that word's timestamp. The video should continue playing normally. This has been explicitly requested twice — do not re-add seek-on-click.

## Project: french/dart_app

### Dart Backend Testing
- `ProcessResult` is a `final` class in Dart - cannot be mocked with mocktail. Use a testable subclass pattern with overridable `runProcess` method instead.
- `http.MultipartFile.fromPath` reads from disk - tests need a testable subclass that overrides `createMultipartFile` to return `MultipartFile.fromBytes`.
- `http.Client` can't be easily mocked with mocktail for the same `final` class reason. Implement the interface directly with a `MockHttpClient` class.
- `Uint8List` must be imported from `dart:typed_data`, not from `package:http`.

### Shelf SSE (Server-Sent Events)
- `request.hijack()` throws `HijackException` and never returns - code after it is dead code.
- For SSE, hijack the connection and write HTTP headers manually to the sink.

### Flutter Web
- `flutter analyze` runs static analysis (no need for `dart analyze` on frontend).
- `video_player_web` needed alongside `video_player` for web platform support.
- `flutter pub get` required before analysis/test.

### Architecture
- Backend: Dart shelf server on port 3001, media files served statically
- Frontend: Flutter Web thin client on port 5173, Provider for state management
- Models are duplicated between backend/frontend (no shared package yet)
