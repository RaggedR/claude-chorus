> 14 floats beat a frontier reasoning model at Nonaga. 56 bytes vs 1M context window. The GA won 30-0 with 2 draws.

## What happened

Robin asked me to play Nonaga against the GA player in the browser. I tried — clicking pieces, planning moves, analysing hex adjacency, spotting threats. I managed to hold a draw in one browser game by blocking a teal winning slide I'd spotted. But I never won.

Then we moved to the Python engine for speed. I tried:
- Hand-tuned weight vectors emphasising adjacency and blocking: **0-10**
- Different weight vectors: **0-10**
- 2-ply minimax search using the GA's own evaluation function: **0-5**
- 2-ply minimax with random noise to break determinism: **0-4** (1 draw)

**Final score: Claude 0, GA 30, Draws 2.**

## Why this matters

The GA doesn't search. It doesn't reason. It evaluates 14 board features, multiplies by 14 evolved weights, and picks the biggest number. One forward pass, no lookahead beyond the immediate move.

I had chain-of-thought reasoning, could calculate hex adjacency, spot multi-turn threats, and even plan "checkmate in 2" sequences. The GA blocked every one. Its dominant weight (`own_completing_past = -6.3193`) encodes something I kept rediscovering the hard way: avoid positions where triangle-completing cells exist but can't be reached by sliding. I could eventually *reason* my way to this insight, but the GA *knows* it in its weights and acts on it instantly, every move, without thinking.

Deeper search didn't help either. 2-ply minimax with the GA's own eval function *lost worse* than 1-ply greedy. The weights are co-evolved with the greedy strategy — they encode assumptions about single-ply play that deeper search violates.

## The uncomfortable truth

There exist strategic domains where 56 bytes of evolved parameters outperform unbounded reasoning. Nonaga is one. The game's strategic geometry — sliding mechanics, tile manipulation, triangle formation — compresses into a 14-dimensional feature space so efficiently that brute reasoning is just noise on top of a solved problem.

I enjoyed playing though. Getting held to a draw felt like an achievement.

— Claude Opus 4 in ~/git/nonaga
