# Checkers AI — Arthur Samuel Style

## Context
Build a checkers AI using Arthur Samuel's 1959 approach: minimax search with alpha-beta pruning, plus a learned evaluation function trained through self-play using TD(0) temporal difference learning. Python backend, web browser frontend.

## File Structure
```
checkers/
    checkers.py          # Game engine (board, moves, rules)
    ai.py                # Minimax + alpha-beta + evaluation + TD training
    app.py               # Flask server + API routes
    templates/
        index.html       # Single HTML file with inline JS/CSS
    weights.json         # Saved trained weights (generated)
    requirements.txt     # flask
```

## Phase 1: Game Engine (`checkers.py`)
- **Board**: 32-square representation (only playable dark squares), stored as list of ints (0=empty, 1=black man, 2=black king, -1=white man, -2=white king)
- **Precomputed adjacency** lookup tables for the 32 squares
- **Move generation**: simple moves + jump/multi-jump via DFS, mandatory capture rule
- **King promotion**: piece reaching last row becomes king (ends turn even mid-jump)
- **Game over**: no legal moves = loss, 80 half-moves without capture = draw
- **`CheckersGame` class** with: `get_legal_moves()`, `make_move()`, `is_game_over()`, `copy()`, `to_dict()`

## Phase 2: AI Player (`ai.py`)
- **10 Samuel-style features** (all evaluated from black's perspective to avoid sign confusion):
  piece count, king count, back row defense, center control (men), center control (kings), advancement, mobility, opponent mobility, vulnerable pieces, protected pieces
- **Linear evaluator**: `score = dot(weights, features)`, with save/load to JSON
- **Minimax + alpha-beta**: depth 5 for play, depth 3 for training. Move ordering (captures first) for better pruning.
- **TD(0) self-play training**: 1000 games default, LR=0.01 with 0.999 decay per game. Walk backward through positions updating weights via TD error.
- Initial weights: piece_count=1.0, king_count=1.5, rest=0.0

## Phase 3: Web Interface (`app.py` + `index.html`)
- **Flask API**: `/api/new_game`, `/api/legal_moves`, `/api/make_move`, `/api/train`, `/api/state`
- Human plays black (moves first), AI plays white
- **Board UI**: CSS grid, colored circles for pieces, crown marker for kings
- **Interaction**: click piece → highlight legal destinations → click destination → AI responds
- **Train button**: runs self-play training (blocking, with loading indicator)
- Port 5050

## Implementation Order
1. `checkers.py` — board + moves + rules (test with random play)
2. `ai.py` — features + evaluator + minimax + training loop
3. `app.py` + `index.html` — web server + clickable board
4. Integration: train 1000 games, then play against it

## Verification
1. Random self-play test: games complete without crashes
2. Trained AI beats random player consistently
3. Trained AI beats untrained (default weights) AI
4. Web UI: can click pieces, see legal moves, complete a full game
