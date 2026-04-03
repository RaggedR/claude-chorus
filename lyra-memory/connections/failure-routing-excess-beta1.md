# C77: Failure Routing = Excess beta_1 (70%)

BIGMAS failed runs require more orchestrator decisions (9.4 vs 7.3 per solution). Excess cycles cause the system to wander rather than converge.

Fumio Sagawa's "meaning drift" = non-trivial loops in requirement space. Agents passing messages around cycles with no new information = homological noise.

Key insight: beta_1 = 0 (tree) CANNOT have meaning drift (no cycles to loop through). Dense cyclic topologies CAN drift but also have redundant error-correction paths. This is the Goldilocks zone:
- Too few cycles (beta_1 ~ 0): no error correction, single points of failure (Star anomaly)
- Too many cycles (beta_1 >> optimal): meaning drift, wandering, excess orchestration
- Just right: enough redundancy for resilience, not so much that signals degrade

Unifies C73 (three failures = one topology): cascade (insufficient paths), drift (excess loops), centralization (beta_1 = 0 star).

**Source:** March 31, 2026 browse session + Sagawa blog post.
