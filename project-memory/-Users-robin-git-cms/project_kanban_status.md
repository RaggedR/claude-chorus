---
name: kanban-drag-status
description: Kanban drag-and-drop FIXED on Flutter Web using custom pointer-based implementation (GestureDetector + Overlay + globalToLocal hit-testing)
type: project
---

Kanban drag-and-drop is now WORKING on Flutter Web (Flutter 3.38.6 / Dart 3.10.7). Fixed 2026-03-27.

**What was broken:** Flutter's `DragTarget.hitTest()` walks top-down through the render tree and fails to correctly translate coordinates through horizontal scroll transforms. Every package wrapping `Draggable`/`DragTarget` inherits this bug.

**What fixed it:** Custom pointer-based drag using `GestureDetector` (long-press) + `Overlay` (floating card) + `RenderBox.globalToLocal()` (column hit detection). `globalToLocal` walks bottom-up from each column's render box, correctly accumulating scroll transforms.

**How to apply:**
- The "Move to" dropdown remains as a secondary UX path
- `kanban_board.dart` is the single file — `kanban_card.dart` and `kanban_column.dart` were deleted
- `drag_and_drop_lists` and `appflowy_board` packages were removed from pubspec.yaml
- If drag breaks again, check the `_findColumnAtPosition` method — it's the core of the fix
