# Android Voice-to-ChatGPT App

## Overview
Simple Flutter Android app that records voice, transcribes via Whisper API, and sends to ChatGPT.

**Location:** `/Users/robin/git/andrew/` (delete existing content first)
**ChatGPT Model:** gpt-4o

## User Flow
1. Tap "Record" button → starts recording
2. Tap "Stop" button → stops recording
3. Audio sent to Whisper API → returns transcript
4. Transcript sent to ChatGPT API → returns response
5. Display conversation (user transcript + ChatGPT response)

## Project Structure
```
andrew/  (new project in /Users/robin/git/andrew/)
├── lib/
│   ├── main.dart              # App entry, MaterialApp
│   ├── screens/
│   │   └── chat_screen.dart   # Main UI with record button + chat
│   └── services/
│       ├── audio_recorder.dart # Record audio, save to file
│       └── openai_service.dart # Whisper + ChatGPT API calls
├── pubspec.yaml
└── .env                        # OpenAI API key (gitignored)
```

## Dependencies
```yaml
dependencies:
  flutter:
    sdk: flutter
  record: ^5.0.0          # Audio recording
  path_provider: ^2.1.0   # Get temp directory for audio files
  http: ^1.1.0            # API calls
  flutter_dotenv: ^5.1.0  # Load API key from .env
  permission_handler: ^11.0.0  # Microphone permission
```

## Key Implementation Details

### Audio Recording (audio_recorder.dart)
- Use `record` package
- Record to m4a/aac format (Whisper accepts this)
- Save to temp file

### OpenAI Service (openai_service.dart)
- `transcribe(File audioFile)` → POST to `https://api.openai.com/v1/audio/transcriptions`
  - multipart/form-data with audio file
  - model: "whisper-1"
- `chat(String message, List<Message> history)` → POST to `https://api.openai.com/v1/chat/completions`
  - model: "gpt-4o"
  - Include conversation history for context

### UI (chat_screen.dart)
- Simple chat interface with messages list
- Large record/stop button at bottom
- Visual feedback during recording (red dot, pulsing, etc.)
- Loading indicator while processing

### Permissions
- Request microphone permission on first use
- Handle permission denied gracefully

## Files to Create
1. `pubspec.yaml` - dependencies
2. `lib/main.dart` - app entry
3. `lib/services/openai_service.dart` - API calls
4. `lib/services/audio_recorder.dart` - recording logic
5. `lib/screens/chat_screen.dart` - main UI
6. `.env.example` - template for API key
7. Update `.gitignore` - exclude .env
8. `android/app/src/main/AndroidManifest.xml` - add permissions

## Build Steps
1. Delete existing content in `/Users/robin/git/andrew/`
2. Run `flutter create .` to scaffold Flutter project
3. Add dependencies, run `flutter pub get`
4. Implement the files listed above
5. Add `.env` with OpenAI API key

## Verification
1. Build and run on Android emulator or device
2. Grant microphone permission when prompted
3. Test: tap record → speak → tap stop → see transcript appear → see ChatGPT response
