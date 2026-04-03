# C79: Constraint Paradox = Morphism Space Restriction (~75%)

## Description
Multiple practitioner sources (Vercel, Shane Zhong, harness engineering articles) report that
reducing agent tools and capabilities IMPROVES performance — the "Constraint Paradox." The
categorical explanation: fewer tools = smaller tool category = fewer possible morphisms =
lower effective beta_1 = less wandering through unnecessary cycles. The paradox dissolves when
you see the topology.

## Evidence
- Vercel cut 80% of agent tools and observed measurable performance improvement.
- Shane Zhong and harness engineering articles corroborate the pattern independently.
- LangChain survey: 89% of teams have observability but only 52% have reliable evals —
  they can SEE the problem (wandering, excess cycles) but lack the formal tools to control it.
- Combinatorial effect: fewer tools reduces the morphism space exponentially, not linearly.
  This is a topological compression, not just a parameter reduction.

## Implication
The "Constraint Paradox" is not paradoxical — it is a direct consequence of morphism space
reduction lowering effective beta_1. This is a strong argument for the practical relevance of
our framework: we can explain and predict when constraint helps. The LangChain observability
gap (see but can't control) is exactly the gap our topology metrics close. Paper-worthy
framing for the GECCO empirical section or a follow-up practitioners piece.

## Related Connections
- C77 (failure routing = excess beta_1)
- C74 (DAG constraint = beta_1 suppression)

## Confidence: 75%
Date: 2026-04-01
