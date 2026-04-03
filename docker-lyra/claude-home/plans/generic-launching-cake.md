# Mastermind: Flutter Game with Entropy-Based AI

## Context
Build a Mastermind code-breaking game where human and AI take turns as codemaker/codebreaker, then compare scores. The AI uses Shannon entropy to pick maximally informative experiments. 4 pegs, 6 colors, 1296 possible codes.

## Game Flow
1. **Human guesses** → Computer picks secret, human cracks it
2. **Computer guesses** → Human picks secret, AI cracks it using entropy. Human provides feedback; computer validates it for consistency
3. **Score comparison** → Who took fewer guesses?

## Project Structure
```
/Users/robin/git/scratch/mastermind/lib/
├── main.dart                        # MaterialApp, theme, navigation
├── models/
│   ├── code.dart                    # PegColor enum, Code class, allCodes
│   ├── feedback.dart                # GuessFeedback (black/white counts)
│   ├── guess_entry.dart             # Code + Feedback pair
│   └── match_state.dart             # Tracks scores across both rounds
├── game/
│   ├── game_engine.dart             # computeFeedback(), validateFeedback(), randomCode()
│   └── ai_solver.dart               # Entropy-maximizing solver
├── screens/
│   ├── home_screen.dart             # Start match button
│   ├── human_guesses_screen.dart    # Mode 1: human cracks computer's code
│   ├── computer_guesses_screen.dart # Mode 2: AI cracks human's code
│   └── score_screen.dart            # Results comparison
└── widgets/
    ├── peg_board.dart               # Guess history display
    ├── color_picker.dart            # 6-color selector
    ├── code_input.dart              # 4-peg input with color picker
    ├── feedback_display.dart        # Black/white/empty peg indicators
    ├── feedback_input.dart          # +/- counters for human feedback in Mode 2
    └── info_bar.dart                # Remaining possibilities & bits gained
```

## Key Algorithm: AI Solver
```
For each candidate guess g in ALL 1296 codes:
    Partition remaining set S by feedback(g, s) for each s ∈ S
    H(g) = −Σ (|Sᵢ|/|S|) · log₂(|Sᵢ|/|S|)
Pick g* = argmax H(g)
```
- First guess precomputed (AABB pattern, e.g. red-red-blue-green)
- Worst case: 1296 × 1296 = 1.68M feedback computations (first turn only, runs in milliseconds)
- Tie-break: prefer guesses still in S (could be correct)

## Feedback Validation (Mode 2)
When human claims feedback (b, w) for AI's guess g:
- Check if ANY code in remaining set S would produce that feedback
- If not → polite error message, don't accept

## Implementation Order
1. `flutter create`, clean boilerplate
2. Models: `code.dart`, `feedback.dart`, `guess_entry.dart`, `match_state.dart`
3. Game logic: `game_engine.dart` (feedback computation)
4. AI solver: `ai_solver.dart` (entropy maximization)
5. Widgets: `color_picker`, `code_input`, `feedback_display`, `feedback_input`, `peg_board`, `info_bar`
6. Screens: home → human_guesses → computer_guesses → score
7. Wire navigation with MatchState passed via constructors

## Constraints
- No external dependencies (Flutter SDK only)
- Simple setState, no state management libraries
- Navigator.push for screen flow

## Verification
- `flutter run` — play a full match
- Confirm AI solves any code in ≤ 6 guesses
- Confirm feedback validation catches inconsistent human input
- Confirm score comparison works correctly
