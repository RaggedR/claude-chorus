# Pilot Signal Implementation for Rotation-Invariant Watermarking

## Problem
The current watermark breaks at 0.05° rotation because frequency coefficients shift in the DFT domain.

## Solution
Add a **pilot signal** — a sinusoidal pattern on a circular ring in the DFT. This pattern survives rotation and reveals the rotation angle, allowing correction before main watermark detection.

---

## Implementation Plan

### Phase 1: Create `src/pilot.rs` (new module)

**Core structs:**
```rust
pub struct PilotConfig {
    pub n_cycles: usize,           // Sinusoidal cycles around ring (default: 4)
    pub strength: f64,             // Pilot amplitude (default: 1.5)
    pub ring_radius_fraction: f64, // Ring radius as fraction of p (default: 0.33)
    pub ring_width: f64,           // Ring thickness in pixels (default: 3.0)
}

pub struct PilotDetectionResult {
    pub rotation_angle: f64,       // Detected angle in degrees
    pub confidence: f64,           // Peak-to-sidelobe ratio
    pub detected: bool,
}
```

**Functions to implement:**

1. `embed_pilot(spectrum, width, height, p, config)` — Add sinusoidal ring pattern to DFT
2. `detect_pilot(pixels, width, height, p, config) -> PilotDetectionResult` — Detect rotation angle
3. `rotate_image(pixels, width, height, angle) -> Vec<f64>` — Bilinear interpolation rotation
4. `bilinear_interpolate(pixels, width, height, x, y) -> f64` — Helper for sub-pixel sampling

### Phase 2: Modify `src/embedding.rs`

Add option to embed pilot alongside main watermark:

```rust
pub struct EmbedOptions {
    pub strength: f64,
    pub embed_pilot: bool,
    pub pilot_config: PilotConfig,
}

pub fn embed_watermark_with_options(pixels, width, height, message, options) -> EmbedResult
```

**Change:** After DFT, before inserting Legendre patterns, call `embed_pilot()` if enabled.

### Phase 3: Modify `src/detection.rs`

Add rotation-corrected detection:

```rust
pub struct DetectOptions {
    pub threshold: f64,
    pub max_sequences: usize,
    pub use_pilot: bool,
    pub pilot_config: PilotConfig,
}

pub fn detect_blind_with_rotation(pixels, width, height, options) -> ExtendedDetectionResult
```

**Flow:**
1. Try direct detection (no rotation)
2. If fails and `use_pilot`: detect rotation angle from pilot
3. Rotate image by negative angle
4. Re-run detection on corrected image

### Phase 4: Update `src/lib.rs`

Export new public API:
```rust
mod pilot;
pub use pilot::{PilotConfig, PilotDetectionResult, embed_pilot, detect_pilot, rotate_image};
pub use embedding::{EmbedOptions, embed_watermark_with_options};
pub use detection::{DetectOptions, ExtendedDetectionResult, detect_blind_with_rotation};
```

### Phase 5: Update CLI binaries

**`src/bin/embed.rs`:** Add `--pilot` flag (default: true)
**`src/bin/detect.rs`:** Add `--pilot` flag (default: true)

---

## Files to Modify

| File | Changes |
|------|---------|
| `src/pilot.rs` | **NEW** — All pilot signal logic (~200 lines) |
| `src/embedding.rs` | Add `EmbedOptions`, `embed_watermark_with_options()` |
| `src/detection.rs` | Add `DetectOptions`, `detect_blind_with_rotation()` |
| `src/lib.rs` | Export pilot module and new functions |
| `src/bin/embed.rs` | Add `--pilot` CLI flag |
| `src/bin/detect.rs` | Add `--pilot` CLI flag |

---

## Algorithm Details

### Pilot Embedding
```
For each pixel (i, j) in DFT:
    r = distance from center
    if |r - r_pilot| < ring_width/2:
        theta = atan2(i - center, j - center)
        value = strength * cos(n_cycles * theta)
        spectrum[i,j].re += value
```

### Rotation Detection
```
1. Compute DFT magnitude of image
2. Sample magnitude values along ring at r = r_pilot (360 samples)
3. Cross-correlate samples with reference cos(n_cycles * theta)
4. Peak position / n_cycles = rotation angle
5. Use parabolic interpolation for sub-degree precision
```

### Image Rotation
```
For each output pixel (x, y):
    Map to input coordinates via inverse rotation
    Bilinear interpolate from 4 neighboring pixels
```

---

## Verification

### Unit Tests (in `src/pilot.rs`)
1. `test_pilot_roundtrip` — Embed + detect with no rotation → 0°
2. `test_rotation_5_degrees` — Rotate 5°, detect → ~5°
3. `test_rotation_0_05_degrees` — Rotate 0.05°, detect → ~0.05° (within 0.1°)

### Integration Test
```bash
# Embed with pilot
cargo run --bin embed -- test.png wm.png "TEST123" --pilot

# Apply our ring attack (was breaking at 0.05°)
python3 ring_attack.py wm.png attacked.png 150 0.05

# Detect with pilot correction — should now succeed
cargo run --bin detect -- attacked.png --pilot
```

### CLI Rotation Test
```bash
# Test various rotation angles
for angle in 0.05 0.1 0.5 1.0 2.0 5.0; do
    convert wm.png -rotate $angle rotated.png
    cargo run --bin detect -- rotated.png --pilot
done
```

---

## Trade-offs

| Aspect | Impact |
|--------|--------|
| **Capacity** | Minimal — ring is narrow, doesn't overlap main watermark much |
| **Speed** | ~30% overhead when rotation correction needed |
| **Precision** | ~0.05-0.1° achievable (sufficient for our attack) |
| **Robustness** | Pilot slightly stronger than main watermark (1.5x) |
