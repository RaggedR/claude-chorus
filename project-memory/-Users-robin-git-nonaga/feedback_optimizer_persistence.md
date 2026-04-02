---
name: Always use persistent optimizers in iterative training
description: Creating fresh Adam optimizer per iteration destroys momentum — a recurring bug across Nonaga and Connect Four
type: feedback
---

Never create a fresh optimizer inside a per-iteration training function. Pass the optimizer in and keep it alive across iterations.

**Why:** Adam's first-moment (m) and second-moment (v) estimates take ~1000 steps to warm up. Destroying them every iteration effectively degrades Adam to near-SGD for the first portion of each pass. This was independently discovered as a bug in both Nonaga (`train_from_ga.py`) and Connect Four (`train.py`). In Connect Four, fixing this single issue (plus removing arena gating) took the NN from 0-20 vs GA to 10-0.

**How to apply:** When reviewing any training loop that calls a `train_network()` function repeatedly, check whether the optimizer is created inside that function or passed in. If created inside, it's a bug. The optimizer should be created once in `main()` and passed to every training call.
