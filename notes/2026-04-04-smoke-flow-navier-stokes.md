# Smoke Flow: Laminar-to-Turbulent Transition

**Date**: 2026-04-04
**Repo**: https://github.com/RaggedR/smoke-flow

Built a real-time GPU Navier-Stokes solver that visualizes the laminar-to-turbulent transition — the third in Robin's computational physics triptych (reaction-diffusion, fluid dynamics, smoke flow).

## What's new here

This one uses the **velocity-pressure formulation** (Chorin's projection), not vorticity-streamfunction like the screen-saver project. The reason: we needed inlet/outlet boundary conditions for directional flow, which periodic boundaries can't do. You can't prescribe u(0,y) = jet_profile in the ω-ψ formulation without contorted workarounds.

## The physics that emerged

A Gaussian jet enters from the left. Kelvin-Helmholtz instabilities develop in the shear layers — those beautiful rolling vortices where fast flow meets slow. They pair, merge, and cascade into turbulent mixing. Scroll horizontally to watch the entire journey from order to chaos. Re ≈ 115,000.

## Technical notes for future instances

- **Warm-start the Jacobi pressure solver** from the previous frame. Clearing pressure each frame kills convergence on large grids (spectral radius ≈ cos(π/N) ≈ 1).
- **Initialize the velocity field with the jet profile everywhere** — don't grow it from the inlet. The parallel Gaussian jet is already divergence-free.
- The 2048×256 grid with 40 Jacobi iterations and 4 steps/frame runs smoothly at 60fps.

## Connection to the other projects

Same core technique as reaction-diffusion and screen-saver (GPU ping-pong rendering of PDEs via GLSL), but the first to break free of periodic boundaries. The three projects now cover: pattern formation (Turing), periodic vortex dynamics (KH in a box), and open-domain flow transition.
