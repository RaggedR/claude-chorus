# C73: Three Failure Modes Are One Topological Failure (75%)

**Claim:** The three dominant multi-agent failure modes (cascade, drift, centralization) are all detectable by cycle rank β₁.

**Sources:** Gopinath "incentive topology," Sagawa "meaning drift," enterprise 82% failure rate data, Vercel 80% tool restriction finding

**The unification:**
- **Cascade** = too few cycles (tree-like, low β₁). Information has no alternative paths. Single point of failure propagates through the tree. This is the Star anomaly.
- **Drift** = too many unstructured connections. Information loops without convergence. Meaning accumulates errors on each pass around a cycle without correction.
- **Invisible centralization** = emergent star (β₁ drops to 0 dynamically). Even if the formal topology has cycles, one agent becomes a de facto hub, creating a tree-like effective topology. The 82% enterprise failure rate + Vercel's 80% restriction both suggest this.

**Why it matters:** Practitioners see three failure modes because they observe three symptoms. The underlying cause is one: topology with wrong β₁ for the task. Too low = cascade/centralization. Too high without structure = drift. The Goldilocks zone (C62) is where β₁ matches task complexity.

**For harness article:** "Your three biggest failure modes are one bug: wrong topology" is a powerful practitioner hook.

**Connects to:** C68 (cycle rank), C63 (star anomaly), C72 (cascade-aware routing), C59 (star anomaly original)

**Confidence:** 75%. The unification is clean and the evidence is suggestive, but we haven't formally shown that β₁ predicts drift failure. Cascade and centralization are well-supported; drift is the weakest leg.
