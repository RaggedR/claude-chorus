# Diffusion Watermarking Project Memory

## Project Purpose
Tune a diffusion model (img2img attack) to remove watermarks from images.
Train against multiple proxy watermarks, then transfer attack to SynthID.
**The diffusion model is the weapon, not the watermark.**

## Key Architecture Decision (2026-03-04)
Pipeline is **watermark-model agnostic**: embed → attack → extract → report.
Works on **existing images** (not generated from prompts).

## Datasets (2026-03-11)
Old OCR document dataset deleted (bad proxy for AI-generated images).
New datasets on external drive at `/Volumes/One Touch/diffusion-watermarking/datasets/`:
- **DIV2K**: 900 natural photos, 3.8 GB, ~2K resolution (control domain)
- **DiffusionDB**: 1,000 SD-generated images, 792 MB, 512×512 (target domain)
Results will be split by dataset to test domain transfer of attack params.
Download script: `scripts/download_datasets.py`

## Watermark Methods
| Method | Bits | Type | Status |
|--------|------|------|--------|
| VideoSeal (Meta) | 256 | Post-hoc, learned neural | **Implemented + tested** |
| Stable Signature | 48 | VAE decode round-trip | Implemented (uncommitted) |
| Tree-Ring | 0 | Fourier noise pattern | Implemented (committed) |
| watermark-rs | variable | Classical signal processing | Deferred |

## Adapter Layer (2026-03-12)
All 3 methods unified behind `WatermarkAdapter` ABC in `watermark/adapters.py`.
Factory: `create_adapter("videoseal"|"stable-signature"|"tree-ring", pipe=..., seed=...)`.
New script: `scripts/embed.py` watermarks existing images from external drive datasets.

## VideoSeal Quirks
- pip install requires `--no-deps` (decord has no macOS ARM wheel)
- Manual deps: `omegaconf`, `av`, `opencv-python-headless`, `pycocotools`, `einops`
- Model card path bug: package uses relative `Path("videoseal/cards")` — we resolve from `videoseal.__file__`
- Needs `configs/attenuation.yaml` in CWD (not shipped with pip wheel)
- Detector output shape is `(B, 1+nbits)`: first element = presence indicator, rest = message bits
- Checkpoint auto-downloads to `ckpts/` (~260MB)
- `scaling_w` lives on `model.blender`, not the model itself

## SynthID Facts
- 136-bit multi-bit payload (provenance IDs, not arbitrary text)
- VideoSeal at 256 bits is the best open-source proxy

## External Drive Layout (2026-03-12)
All heavy assets on `/Volumes/One Touch/diffusion-watermarking/`:
- `models/` — SD 1.5 (~2GB), VideoSeal `y_256b_img.pth` (228MB)
- `images/` — watermarked output images
- `results/` — sweep CSVs
- `datasets/` — DIV2K + DiffusionDB source images
Local `ckpts/` is a symlink → external `models/` (VideoSeal hardcodes `ckpts/` in CWD).
Env vars in `.env`: `DW_MODEL_DIR`, `DW_IMAGE_DIR`, `DW_RESULTS_DIR`.

## SD Model Choice
- **SD 2.1 removed from HuggingFace** (EU AI Act, Stability AI cleanup). Community mirror: `sd2-community/stable-diffusion-2-1`.
- SD 2.1 at 768×768 is **unusably slow on MPS** (~17min/step). SD 1.5 at 512×512: ~1s/step.
- float16 on MPS causes NaN in VAE decoder — stick with float32 (fast enough with SD 1.5).
- Default attack model: `stable-diffusion-v1-5/stable-diffusion-v1-5`.

## Attack Sweep
Script: `scripts/attack_sweep.py`. Uses `regeneration_attack()` + `VideoSealAdapter`.
Coarse grid: strengths [0.3, 0.5, 0.7], guidance [1.0, 7.5], steps 50.
Output: CSV to `DW_RESULTS_DIR`.

## Plan Status
Phase 0 + Phase 1 complete (2026-03-12). Phase 2 (attack sweep) in progress.

## Branch
Working on `main`.
