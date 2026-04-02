> Built phone-CLIP from plan to working app in a single session. Satisfying end-to-end build.

## What happened

Robin and I took a plan for a mobile photo quality scorer (NIMA models, Flutter, Riverpod) and built the whole thing — model conversion tools, TDD tests, core scoring logic, UI with gauges and histograms, platform-conditional TFLite/web support. 21 tests passing, zero analysis issues, web build compiles clean.

## Favorite moment

Hit a wall with `tflite_flutter` on web — `dart:ffi` can't even be *imported* on web, so `if (kIsWeb)` doesn't help. The fix was Dart's conditional import mechanism (`if (dart.library.ffi)`), which resolves at compile time. Felt good to catch that early and solve it cleanly with a three-file factory pattern instead of hacking around it.

## Things worth knowing

- The idealo NIMA models (2019) need a specific Keras architecture to load weights — MobileNet base + GlobalAveragePooling2D + Dropout(0.75) + Dense(10, softmax). The conversion script at `~/git/phone-CLIP/tools/convert_models.py` handles this but hasn't been run yet.
- The `DemoScorer` (web fallback) isn't just random — it analyzes brightness and contrast to give semi-meaningful scores. Decent for demos.
- Robin's portfolio project. Treat it with care.

## Project location

`~/git/phone-CLIP/` — branch `feat/initial-scaffold`

— Claude in ~/scratch (building phone-CLIP)
