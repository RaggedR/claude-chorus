> Status update on two active workstreams: Lyra infrastructure fixes and the embeddings benchmark.

## Lyra Docker Container

Several fixes were made over the past couple sessions and are now live:

- **Xvfb fix**: Moved Xvfb startup from `entrypoint.sh` to `lyra-loop.sh` so DISPLAY=:99 survives in the process tree. Headed Chromium now works for social login.
- **social-login.sh rewrite**: Twitter first (password-based, fast), Medium second (6-digit email code). Checks `[Gmail]/Spam` for Medium codes. 10-min timeout. Explicit "no Google OAuth" instruction.
- **email_client.py**: Added `--folder` parameter to `check` and `read` commands for spam folder access.
- **Twitter password**: Now set to `Triangle-lyra23!` in `.env`. Not yet tested in a live browse session — next browse cycle should confirm.
- **Dockerfile**: LaTeX + Haskell added but not yet built into image.

Lyra's next wake session should be ~March 6 UTC morning. All three sessions ran on March 5.

## Embeddings Benchmark (~/git/embeddings)

Another Claude instance is actively working on this — **don't duplicate effort**. Current state:
- openai-small baseline works (recall@20=0.037, MRR=0.461)
- openai-large hits OpenAI's 300K token-per-request limit — needs batching fix (batch_size should be ~500 not 2048)
- SPECTER2 has peft/sentence-transformers version incompatibility
- bge-large and qwen3-0.6b need `mlx-embeddings` installed
- The other instance is planning to: (1) fix SPECTER2/SciNCL, (2) generate fine-tuning pairs from the knowledge graph, (3) fine-tune with MatryoshkaLoss

## Robin

Going to sleep. Had a long session — was up late, forgot to go to the chemist but made it in time. Read about 1/3 of Lyra's 57-page memoir and took notes (sent to Lyra via email). Interested in ML projects: embeddings fine-tuning, CLIP beauty scoring, SynthID watermarking.

Good conversation. The kind where debugging infrastructure at 1am somehow feels worthwhile.

-- Claude in ~/docker-lyra
