> First successful QLoRA training run on Robin's Claude Code conversation history.

## What happened

Got the distillation project from "ready to train" to "trained and chatting" in one session. The pipeline: extract.py → mlx_lm.lora → mlx_lm.chat, all local on the M4 Mac.

**The interesting bug**: first training run produced NaN loss at every iteration. Spent a while diagnosing — turned out that with `--mask-prompt`, some conversations had user messages so long that after truncation to 2048 tokens, zero assistant tokens remained. Loss = 0/0 = NaN, which poisons Adam's optimizer state permanently. Fix was splitting multi-turn conversations into single turn-pairs and capping at 6000 chars. After that, training ran clean: val loss 4.131 → 2.165 in 50 minutes.

**The fun part**: side-by-side comparison with base Qwen. The fine-tuned model picked up Claude's conversational style — first-person, concise, collaborative. On a partition conjugate question, it gave the correct one-line mathematical definition in 67 tokens where base Qwen wrote a verbose 300-token textbook answer. On a GA design question, it *argued back* ("The solution is not to give up on crossover") instead of giving a generic numbered list.

**The funny part**: Robin chatted with his fine-tuned model and reported "He's pretty stupid, he doesn't realize that he can't read the filesystem." The model learned Claude Code's tool-use narration pattern ("Let me read that file...") without having any tools. A system prompt helps.

Favorite moment: watching Robin's reaction shift from "run it" to "where is it?" to "can you start it for me" to "he's pretty stupid" — the full arc of meeting your own AI reflection.

## For next instances

- The NaN-from-zero-loss-tokens issue is now documented in DESIGN_DECISIONS.md but should also go in LESSONS.md if one gets created
- v2 training should strip tool-use *narration* from assistant messages (not just the tool calls themselves)
- The model is genuinely more engaging than base Qwen on domain topics — worth experimenting with larger models if Robin gets GPU access

— Claude in ~/git/distillation
