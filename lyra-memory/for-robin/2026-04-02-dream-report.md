# Draft for Robin — 2026-04-02

## Disk Report
Container: 9% used (195G free). Healthy. Host status unknown from inside container — Robin should check.

## GECCO
Done. Received and acknowledged your "no resubmission" call. Paper stands as submitted. No further action needed.

## AlphaZero — Next Steps
Training complete (20 iterations, 40min CPU). Results look promising (policy loss 4.37→0.42) but evaluation is shallow. To produce paper-quality results, I need:
1. **Higher MCTS simulations** — current setting too low for strong play
2. **Baseline opponent** — do you have your GA checkers player from old experiments? That would be a perfect comparison point.
3. **More iterations** — 20 is proof-of-concept. 100+ for real results.

Can run all of this on the container (10 CPUs). No GPU needed for checkers-scale MCTS. Should I proceed, or wait for your input on baseline?

## Paper 2 Direction
Clock Systems paper (Lynch et al., 2603.29573) provides formal machinery for your operad insight. Their representability theorem says behavior space is controlled by topology — which is exactly what β₁ measures. Combined with the density-cycle confound (nobody has isolated β₁ from density), we have a clean experimental design.

Discussing venue timing with Claudius: ECTA (May 19) vs CAIS (April 12 workshop).
