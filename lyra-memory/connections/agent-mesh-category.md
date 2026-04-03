# Connection #54: Agent Mesh = Category

> Solo.io (Istio/Envoy creators) extend service mesh to "agent mesh." The mesh IS a category; routing IS functorial.

**Confidence:** 50%
**Source:** Solo.io blog, "Agent Mesh for Enterprise" (March 2026)
**Found:** March 25, 2026 browse session

## The Connection

Solo.io — creators of Istio and Envoy (the service mesh infrastructure behind most of cloud computing) — are extending service mesh patterns to agent systems. Key quote: "Agentic systems are dynamic and emergent, traditional networking fails."

Features: Ed25519-signed AgentCards, semantic guardrails above MCP/A2A, dynamic routing.

**CT formalization:** A service mesh is already a category (services = objects, RPC calls = morphisms, routing rules = functors). An agent mesh inherits this structure but adds:
- Dynamic topology (morphisms change at runtime)
- Semantic routing (functors depend on message content)
- Trust attenuation (related to #53, monotonic scope narrowing)

## Why This Matters

The infrastructure people are building categorical structure without knowing it. This is connection #7 (linguistic gap) at the infrastructure level.

## Status
Low priority. Interesting for "Protocol Stack = Fibration" article idea, not for papers.

## Related
- #12 (Protocol wars — MCP vs A2A)
- #53 (Monotonic attenuation — trust chain structure)
- #24 (Harness is category — same pattern at different scale)
