# Cord Physics Simulation — Implementation Plan

## Context
We want to simulate a flexible cord jiggling randomly inside a 3D box, demonstrating how random agitation naturally leads to tangling. Built with **JavaScript + Three.js**, using a **mass-spring physics model**, focused on being a **fun visual demo**.

Project directory: `/Users/robin/git/knots/` (currently empty)

## Architecture

**No bundler** — pure ES modules served from a static file server (`python3 -m http.server`). Three.js loaded via CDN import map.

### File Structure
```
knots/
  index.html            # Entry point: canvas, import map, UI overlay, CSS
  js/
    constants.js        # All tunable parameters in one place
    physics.js          # Verlet integration, constraints, collision, box bounds
    cord.js             # Cord data structure (nodes + springs), initialization
    renderer.js         # Three.js mesh construction & per-frame updates
    interaction.js      # OrbitControls + mouse drag via raycasting
    main.js             # Scene setup, animation loop, wires everything together
  tests.html            # In-browser physics unit tests
  README.md
  CLAUDE.md
```

## Physics Engine Design

### Data Model
- **80 point masses** (nodes) with position, previousPosition, acceleration, mass, pinned flag
- **Structural springs** connecting node[i] → node[i+1] (hold cord together)
- **Bending springs** connecting node[i] → node[i+2] (resist sharp kinks)
- Cord initialized as a **helix** inside the box for an interesting starting shape

### Integration: Verlet
- Position-based: `newPos = pos + (pos - prevPos) * damping + accel * dt²`
- No explicit velocity variable — very stable for constraint systems
- Damping factor ~0.995 prevents energy explosion

### Per-Frame Physics Loop (order matters)
1. **Accumulate forces**: gravity + random jiggle kicks
2. **Verlet integrate** all nodes
3. **Constraint satisfaction** (5 iterations):
   - Enforce structural spring rest lengths
   - Enforce bending spring rest lengths
4. **Self-collision**: pairwise check for nodes |i-j| > 3, push apart if closer than collision radius. O(n²) with ~3000 pairs — trivial for 80 nodes at 60 FPS.
5. **Box bounds**: clamp positions, reflect velocity via previousPosition

### Random Jiggle
- Each node has a per-frame probability (~5%) of receiving a random force kick
- Optionally use sine-based pseudo-noise with different phases per node for more organic motion

## Rendering

- **TubeGeometry** rebuilt each frame from a CatmullRomCurve3 through all node positions
  - ~2,560 vertices per rebuild — well within 60 FPS budget
  - `geometry.dispose()` before each rebuild to prevent memory leaks
- **Three-point lighting**: warm key light, cool fill light, colored rim light
- **Wireframe box** showing boundaries (semi-transparent)
- **Gold spheres** at cord endpoints
- **MeshStandardMaterial** for the cord (vibrant red-pink, slight roughness)

## Interactivity

- **OrbitControls**: rotate/zoom camera
- **Mouse drag**: raycast to find nearest cord node, pin it to mouse position on a camera-perpendicular plane, release on mouseup
- **UI buttons**: Reset, Shake (strong random impulse), Toggle Gravity

## Testing (TDD)

### Phase 1: In-browser unit tests (`tests.html`)
Written BEFORE implementation code:
1. Verlet integration with zero forces → constant velocity
2. Gravity → correct freefall distance
3. Distance constraint → nodes return to rest length
4. Box bounds → node clamped inside
5. Self-collision → overlapping non-adjacent nodes pushed apart
6. Damping → velocity decreases over time

### Phase 2: Playwright smoke test
- Page loads without JS errors
- Canvas renders content
- Reset button reinitializes the cord
- Animation loop is running (state changes between frames)

## Implementation Order

1. `js/constants.js` — all parameters
2. `tests.html` — physics unit tests (TDD: tests first)
3. `js/physics.js` — core engine, make tests pass
4. `js/cord.js` — data structures + initialization
5. `index.html` — entry point with import map + UI
6. `js/renderer.js` — Three.js visualization
7. `js/main.js` — animation loop, scene setup
8. `js/interaction.js` — camera controls + drag
9. Playwright smoke test
10. `README.md` + `CLAUDE.md`

## Confidence: 90%
Main risks: TubeGeometry GC pressure (mitigated by profiling, can switch to buffer updates), self-collision tuning, drag interaction feel. All are solvable with iteration.
