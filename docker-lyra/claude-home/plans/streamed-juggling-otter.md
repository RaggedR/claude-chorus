# Zero-Knowledge Proof for Blind Watermark Verification

## Overview

Implement ZK proofs that allow token owners to prove "this image contains my watermark" without revealing detection algorithm internals or image content.

**Framework: RISC Zero (zkVM)**

---

## Why RISC Zero

| Benefit | Detail |
|---------|--------|
| **Natural Rust** | Port C++ detection directly, no circuit DSL to learn |
| **Handles floats** | Fixed-point emulation built-in |
| **Production-ready** | Groth16 recursion for on-chain (~200K gas) |
| **Bonsai cloud** | Parallel proving for production workloads |

---

## Implementation Phases

### Phase 1: Rust Port of Blind Detection (1-2 weeks)
*Get the algorithm working in Rust without ZK*

1. Create `zk-watermark/` project structure
2. Port `WatermarkDetection.cpp` → Rust modules
3. Port `detect_blind.cpp` → Rust CLI
4. Test: Output must match C++ exactly

### Phase 2: RISC Zero Guest Program (2-3 weeks)
*Wrap detection in zkVM*

1. Create RISC Zero guest with detection logic
2. Define public/private inputs
3. Build host program for proof generation
4. Test: Generate and verify proofs locally

### Phase 3: Backend Integration (1-2 weeks)
*API endpoints for proof generation/verification*

1. WASM bindings for Node.js
2. `POST /api/verify/generate-proof` endpoint
3. `POST /api/verify/check-proof` endpoint
4. Test: End-to-end proof flow

### Phase 4: On-Chain Verification (2-4 weeks)
*Verify proofs in smart contract*

1. Groth16 recursion (compress STARK → 200-byte SNARK)
2. Deploy `WatermarkVerifier.sol`
3. Integrate with `NFTmarketNFT.sol`

---

## File Structure

```
NFTmarket/
└── zk-watermark/                    # New component
    ├── Cargo.toml                   # Workspace manifest
    ├── README.md
    │
    ├── detection/                   # Pure Rust detection (Phase 1)
    │   ├── Cargo.toml
    │   └── src/
    │       ├── lib.rs               # Library exports
    │       ├── dft.rs               # DFT implementation
    │       ├── legendre.rs          # Legendre sequence generation
    │       ├── correlation.rs       # Fast correlation
    │       ├── detection.rs         # Blind detection algorithm
    │       └── bin/
    │           └── detect.rs        # CLI tool (matches C++ output)
    │
    ├── guest/                       # RISC Zero guest (Phase 2)
    │   ├── Cargo.toml
    │   └── src/main.rs
    │
    ├── host/                        # Proof generation (Phase 2)
    │   ├── Cargo.toml
    │   └── src/lib.rs
    │
    ├── contracts/                   # Solidity verifier (Phase 4)
    │   └── WatermarkVerifier.sol
    │
    └── test/
        └── images/                  # Test images with known watermarks
```

---

## Technical Approach

### Public Inputs (Verifier sees)
- Image hash (SHA-256)
- Detection threshold
- Result: detected (bool) + confidence (float)
- Message hash (not message itself)

### Private Inputs (Hidden)
- Raw image pixels
- Claimed watermark message

### Key Challenge: DFT in ZK
- Use fixed-point arithmetic (scale by 2^32)
- All operations in u64/u128
- Allow rounding margin in threshold comparison

---

## Phase 1 Details: Rust Port

### Functions to Port from C++

| C++ Function | Rust Module | Purpose |
|--------------|-------------|---------|
| `generateArray(p, k, array)` | `legendre.rs` | Generate p×p Legendre sequence |
| `extractMark(...)` | `dft.rs` | DFT + extract p×p coefficients |
| `fastCorrelation(...)` | `correlation.rs` | Cross-correlate via FFT |
| `peak2rms(array, len)` | `detection.rs` | Calculate peak/RMS ratio |
| `getASCII(shifts, size)` | `detection.rs` | Decode shifts → ASCII |

### Verification Test

```bash
# C++ detection
./build/detect_blind test.png 10 > cpp.txt

# Rust detection
cargo run --bin detect -- test.png 10 > rust.txt

# Must match exactly
diff cpp.txt rust.txt
```

---

## Testing Strategy

1. **Unit tests**: Each Rust module vs C++ function output
2. **Integration**: Full detection pipeline comparison
3. **ZK proofs**: Generate + verify receipts (Phase 2)
4. **On-chain**: Contract verification (Phase 4)

---

## Estimated Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 1: Rust port | 1-2 weeks | `cargo run --bin detect` matches C++ |
| Phase 2: RISC Zero | 2-3 weeks | Local proof generation/verification |
| Phase 3: Backend | 1-2 weeks | API endpoints for proofs |
| Phase 4: On-chain | 2-4 weeks | Smart contract verification |
| **Total** | **6-11 weeks** |

---

## Critical Files to Reference

| File | Purpose |
|------|---------|
| `watermarking/WatermarkDetection.cpp` | Core algorithms to port |
| `watermarking/detect_blind.cpp` | Main detection flow |
| `watermarking/Utilities.cpp` | Helper functions (primes, etc.) |

## Dependencies (Rust)

```toml
[dependencies]
rustfft = "6.1"          # FFT implementation
num-complex = "0.4"      # Complex numbers
image = "0.24"           # Image loading
sha2 = "0.10"            # SHA-256 for image hash
```
