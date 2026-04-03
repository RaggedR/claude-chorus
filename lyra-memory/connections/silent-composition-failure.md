# Connection #52: Silent Composition Failure = Laxator

> "Multi-agent scoring isn't a number you compute. It's a contract you enforce." — Romitelli

**Confidence:** 60%
**Source:** Daniel Romitelli, HackerNoon, "Polite Failure" (March 2026)
**Found:** March 25, 2026 browse session

## The Connection

Silent composition failure: one agent returns nothing or malformed data, but the aggregate continues without error. The system "politely fails" — no crash, no warning, just degraded output.

This is EXACTLY what the laxator measures: the deviation from strict composition. In strict composition, violating the interface contract produces an immediate error. In lax composition, violations are absorbed — but they compound.

**CT formalization:** Monad laws guarantee that unit and bind interact correctly. If composition is strict (laws hold), silent failure is impossible. If composition is lax, failures are "politely" absorbed with measurable deviation = laxator.

**Practitioner data:**
- MAST study: 36.9% of failures are coordination breakdowns (= laxator exceeding threshold)
- 41-86.7% overall failure rate across 7 frameworks
- GitHub blog: "Treat agents like distributed systems, not chat flows"

## Why This Matters

This is the practitioner's name for the laxator. "Polite failure" = uncontrolled laxness. The article opportunity: show practitioners that CT prevents this by construction.

## Related
- #37 (Google scaling laws — 17.2x error = laxator magnitude for FC)
- #43 (Harness-as-Monad — harness enforces composition laws)
- #7 (Linguistic gap — practitioners reinventing CT vocabulary)
