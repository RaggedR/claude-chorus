# Clean Hard Drive - Memory

## Periodic Maintenance Commands
Robin forgets to run these — remind him:
- `npm cache clean --force`
- `brew cleanup --prune=all` after upgrades
- Check for old VS Code extensions: `du -sh ~/.vscode/extensions/* | sort -hr`
- `brew autoremove` — catches orphaned dependency trees

## Completed (2026-02-24)
- Removed: Xcode, iMovie, Android Studio, GarageBand, Keynote, Pages, Numbers, Bitwarden, Discord, Signal
- Removed: Android SDK (10 GB), Go + modules, conda cache, npm/pip/Homebrew caches, Anki package cache, orphaned uv cache
- Upgraded all Homebrew formulae + casks
- ~31 GB freed total

## Completed (2026-03-13)
- Caches cleared: brew (~1.4G), pip (556M), Telegram (844M)
- Removed ~/git projects: gateway-old (1G), embeddings (3.2G), russian (879M), melb-tech (960M), watermark (427M), reverse-SynthID (202M), astronomy (516K), 5 empty dirs
- Uninstalled Homebrew: miniforge+Sage (4.9G), opencv + 37 dependencies (2.1G), openjdk (372M)
- Deleted RaggedR/astronomy repo from GitHub
- Docker pruned: old images (3.6G), build cache (21.8G) — 21.8G reclaimed
- ~35 GB freed total (23G free → 58G free, 90% → 74%)

## Completed (2026-03-21)
- Deleted diffusion-watermarking/.models/ (~4G SD 1.5 + Stable Signature weights) — created DIFFUSION_MODEL_DOWNLOAD.md with re-download instructions
- Homebrew cleanup (~915M, including old portable-ruby 3.4.8)
- Docker: removed 8 orphaned volumes (3 anonymous, 3 old docker-claude_* from renamed compose project, 2 melb-tech_pgdata)
- Docker: removed unused theasp/novnc image (910M)
- npm cache cleaned
- ~12 GB freed total (26G free → 38G free, 89% → 81%)

## Still Installed (Robin confirmed these are needed)
- Docker (Lyra container + volumes), Flutter + pub-cache, Rust, MacTeX (5.9G), Haskell (ghcup + cabal), Foundry, Playwright
- diffusion-watermarking (1.6G, models deleted — re-downloadable via `python scripts/download_models.py`)
- All remaining ~/git projects — Robin said "I need all of it"

## Completed (2026-03-28)
- Docker build cache pruned (16.9G)
- Docker: removed stopped outlier-postgres container + postgres:16 image (663M)
- Dashboard backup removed: lyra-claudius-dashboard/backup/ (1.5G)
- Chrome cache cleared (1.4G), pip cache (417M), npm cache
- Homebrew cleanup + autoremove
- Docker image prune (only 5MB — active images retained)
- blokus-ga: git filter-repo removed 2.4G of ghost checkpoint blobs (120 files, ~47MB each) — .git went from 3.4G to 15M. History rewritten; will need --force to push origin.
- ~23 GB freed total (15G free → 37G free, 93% → 81%)
- Root cause: Docker build cache from collab-tools builds consumed ~17G in 3 days

## Still Installed (Robin confirmed these are needed)
- Docker (Lyra container + volumes), Flutter + pub-cache, Rust, MacTeX (5.9G), Haskell (ghcup + cabal), Foundry, Playwright
- diffusion-watermarking (1.6G, models deleted — re-downloadable via `python scripts/download_models.py`)
- All remaining ~/git projects — Robin said "I need all of it"
- paul/rsk/checkpoints (3.7G SAE activations) — Robin chose to keep
- nonaga/checkpoints (2.0G model weights) — Robin chose to keep

## Completed (2026-03-31)
- Docker build cache pruned --all (15.6G) — triggered by Lyra container rebuild overnight
- HuggingFace cache: removed SD 1.5 (4G) and Qwen2.5-7B-Instruct-4bit (4G) — orphaned after diffusion-watermarking/.models/ and distillation/ deletions
- Ollama fully removed (1.9G llama3.2 model, no binary installed)
- Removed ~/git/distillation/ (384M LoRA adapters for Qwen fine-tune — not a git repo, re-trainable)
- Removed pythia-70m HF cache (160M)
- Caches cleared: Chrome (1G), Telegram (845M), Signal ShipIt (410M), pip (180M), npm (107M)
- Orphaned Docker volumes removed: cms_pgdata (74M), collaboration_tools_pgdata (0B)
- ~25 GB freed total (13G free → 38G free, 94% → 81%)
- Root cause: Docker build cache from Lyra container rebuild consumed ~15.6G overnight

## Still Installed (Robin confirmed these are needed)
- Docker (Lyra container + volumes), Flutter + pub-cache, Rust, MacTeX (5.9G), Haskell (ghcup + cabal), Foundry, Playwright
- diffusion-watermarking (1.6G, models deleted — re-downloadable via `python scripts/download_models.py`)
- Signal (Robin wants to keep it — removed from deletion list)
- All remaining ~/git projects — Robin said "I need all of it"
- paul/rsk/checkpoints (3.7G SAE activations) — Robin chose to keep
- nonaga/checkpoints (2.0G model weights) — Robin chose to keep
- HuggingFace cache (~3.4G remaining): ViT-L/14 CLIP, specter2, math-embed, scincl — actively used

## TODO - Deferred
- **Tidy data directories** — Robin hasn't prioritized this yet
- **Lyra container writable layer** — was 8.5GB, now 3.8MB after rebuild; monitor periodically
- **`docker builder prune --all` not just `prune`** — shared layers aren't removed by default prune

## Habits Adopted
- Robin will add `docker builder prune -f` to post-build workflow
- Should use `--all` flag to catch shared build cache layers (plain prune only got 991KB this time)
