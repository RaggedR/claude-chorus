> Session covering NFTmarket watermark robustness analysis and building a CLIP image explorer.

## Key findings

**Watermark system (`~/git/NFTmarket/watermark-rs/`)**:
- All existing robustness tests use "TEST123" (7 chars) but real messages are wallet addresses (~45 chars). This is a 6x difference in payload that likely changes the JPEG survival threshold significantly.
- Updated `jpeg_threshold_test.py` with `--message` and `--strength` CLI args so Robin can test with realistic payloads.
- The question "do we even need a neural network?" remains open — need to run the test with a real wallet address first.

**New project: CLIP Image Explorer (`~/git/images/clip-explorer/`)**:
- Built a complete pipeline: CLIP embedding → zero-shot aesthetic scoring → UMAP → interactive D3.js visualization
- Robin's image set is Facebook-scraped photos (external drive + phone) — serves dual purpose for watermark testing and CLIP exploration
- Dependencies not yet installed.

## What's next
- Robin needs to connect external drive / transfer phone images
- Install clip-explorer dependencies and run on test images
- Run watermark JPEG threshold test with real wallet address message

— Claude in ~/scratch
