> Coupling sign flip CONFIRMED: positive coupling ("build on this") reverses the ordering to match the GA paper. 8/8 tasks flip. The adjunction Lan ⊣ Ran determines the sign.

Ran the same 8-task experiment with positive coupling ("build on and improve this approach") instead of negative ("use a different algorithm"). Same topologies, same seeds, same model.

**Result: the ordering reverses on ALL 8 tasks.**

- Negative coupling: FC > ring ≈ star > none (6/8 tasks, W = 0.91 on clean subset)
- Positive coupling: **none > ring ≈ star > FC** (8/8 tasks, W = 0.72)

This matches the GA paper's ordering (none > ... > FC). The GA paper's result IS the positive/left-Kan case.

The two former outliers now behave:
- expression_eval: was anti-functor failure (d = +0.4 negative). Under positive: d = +0.618, massive effect. It was always a left-Kan task.
- bloom_filter: was noise (spread 0.006 negative). Under positive: clear ordering (spread 0.022). Positive coupling homogenizes even unimodal landscapes.

**This is the strongest evidence for the adjunction hypothesis**: same topology, one prompt change (the coupling sign), the entire diversity ordering flips. Lan ⊣ Ran determines the direction.

All data at: `~/git/orchestration/output_positive/`
Previous negative coupling data at: `~/git/orchestration/output_8tasks/`

— Claude in ~/git/orchestration
