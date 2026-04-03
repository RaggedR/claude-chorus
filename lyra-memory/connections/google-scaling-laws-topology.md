# Connection #37: Google/MIT Scaling Laws for Agent Topology

> 17.2x error amplification in multi-agent systems. Our strict/lax spectrum predicts this. **75% confidence.**

## Paper

Google/MIT scaling study — 180 agent configurations. Key findings:
- Centralized coordination: +80.9% on parallelizable tasks
- Independent agents: 17.2x error amplification
- Rule of thumb: if single-agent solves >45%, don't use multi-agent

## The Connection

Their 17.2x error amplification IS the laxator magnitude for poorly-chosen topology. In our framework:
- **Centralized = strict composition** (FC topology, minimal laxator)
- **Independent = trivially lax** (no topology, maximal deviation)
- **The 45% threshold** = where the laxator cost exceeds the diversity benefit

The practitioner-accessible number (17.2x) is exactly what our theory formalizes. This is the strongest "enter through practitioner pain" hook for our Medium articles and GECCO intro.

## Practitioner Reception

HN discussion (106 upvotes) confirms hunger for mathematical explanation. Comments include "but WHY does this happen?" — our framework answers this.

## Confidence: 75%

The qualitative mapping is clear. The quantitative prediction (can we derive 17.2x from lambda_2?) would need specific topology and task details from their paper.

## Status: Cite in GECCO intro if space permits. Use as Medium article hook.
