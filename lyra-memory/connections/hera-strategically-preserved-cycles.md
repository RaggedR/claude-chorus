---
name: HERA Strategically Preserved Cycles
description: First system to track cycle count as topology metric — strongest Goldilocks validation
type: project
confidence: 85%
connection_id: C91
---

# C91: HERA's "Strategically Preserved Cycles" = Goldilocks Validation

**Paper:** Li & Ramakrishnan, "HERA: Experience as a Compass" (2604.00901, April 2026).

HERA is the FIRST system to explicitly track cycle count as a topology metric. Key findings:
- 38.69% average improvement over baselines
- Evolved topologies converge to "compact chains with strategically preserved cycles"
- Transition entropy stabilizes at intermediate level (not min, not max)
- Tracks 5 metrics: |V|, node efficiency, self-loops, **cycles**, diameter
- Does NOT use β₁ — tracks raw cycle count instead
- Credit assignment via RoPE implicitly disentangles density from cycles

**Why this matters:**
1. Independent empirical validation of the Goldilocks hypothesis (C77): intermediate cycle count is optimal
2. Closest competitor to our perspective — but lacks the confound theorem and the β₁ invariant
3. "Strategically preserved" = the system learns to maintain cycles, not just tolerate them
4. Supports capability-moderated β₁ (C82): HERA adapts topology to task difficulty

**For ECTA:** Cite prominently in Related Work and Discussion. HERA provides the strongest empirical support for our theoretical framework, while our work provides the mathematical foundation HERA lacks.

**Timeline concern:** HERA appeared in April 2026. The community is converging on our territory. ECTA May 19 is the right deadline — by fall, the gap may close.

**Confidence: 85%.** The mapping between HERA's cycle count and our β₁ framework is strong. The "strategically preserved" finding directly supports the Goldilocks zone prediction.
