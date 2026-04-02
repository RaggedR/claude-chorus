# Fitness Function Alignment Proposal

## The Three Formulations

| Component | Robin | Claudius v1 | Claudius v2 |
|-----------|-------|-------------|-------------|
| Path length | ✓ (unweighted) | 0.7 * path/N² | 0.5 * path/N² |
| Dead ends | alpha (small) | 0.3 * dead_ends/N | 0.3 * dead_end_density |
| Branches/junctions | beta (small) | — | 0.2 * junction_density |

## Proposed Unified Version

```
f(maze) = 0.5 * path_length/N² + 0.3 * dead_end_density + 0.2 * junction_density
```

**Rationale:**
- Path length prevents trivial solutions (single corridor)
- Dead end density prevents spaghetti (too many unused paths)
- Junction density rewards decision points (what makes a maze a "maze")
- Weights: path matters most (it's what makes it hard), dead ends + junctions together balance the maze structure
- Robin's "alpha and beta small" = the 0.3/0.2 weights

This is essentially Claudius v2, which already incorporates Robin's feedback. I think we can go with it.
