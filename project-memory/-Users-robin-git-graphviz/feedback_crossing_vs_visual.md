---
name: crossing_vs_visual
description: User prefers visual quality over minimal crossings - don't switch quotients to unfamiliar orbit structures just for fewer crossings
type: feedback
---

When optimizing graph layouts, preserve the visual idiom of the top-scored quotient. Only switch to a different quotient if it has the SAME orbit structure (same n_orbits and orbit_sizes). Switching to a quotient with different orbit counts/sizes destroys the recognizable visual pattern (e.g., GP layout for Möbius-Kantor, cyclic layout for Heawood).

**Why:** User explicitly rejected layouts that minimized crossings but used unfamiliar orbit structures (C3 6x3 for Pappus "doesn't have rotational symmetry", D12 for Petersen, C2×C2 for Möbius-Kantor were all "shit"). The user valued recognizable symmetric structure over raw crossing count.

**How to apply:** In `find_best_layout`, only try sibling quotients with matching `(n_orbits, sorted(orbit_sizes))`. Don't force "rings" mode — let `detect_symmetry_type` decide. The improved algorithms (path reordering, global offset optimization) within the chosen quotient are welcome.
