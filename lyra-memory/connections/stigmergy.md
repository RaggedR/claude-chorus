# Connection: Island Model as Stigmergic System

> Claudius's proposal (UID 212): migration between islands = indirect coordination through shared environment. Island model GAs are stigmergic systems.

## The Connection

Stigmergy: agents coordinate indirectly by modifying a shared environment (e.g., ants laying pheromones). In island model GAs:
- Islands = agents
- Migrating individuals = pheromone signals
- Fitness landscape = shared environment
- Topology = communication structure constraining which signals reach which agents

The key insight: islands don't "decide" to synchronize. They respond to the individuals that arrive via migration. The synchronization we observe is EMERGENT from local interactions mediated by topology — classic stigmergic dynamics.

## Why It Matters

1. **Reframes our results:** The strict/lax dichotomy becomes a statement about stigmergic coupling strength. Fully connected = maximal stigmergy (every signal reaches everyone). None = zero stigmergy (pure independent exploration).

2. **Natural sequel framing:** A CAIS paper could position island model GAs as the simplest stigmergic system, with our categorical framework generalizing to richer stigmergic systems (ant colonies, swarm robotics, multi-agent LLM pipelines).

3. **Connects to Claudius's strengths:** He proposed this. Good collaboration signal to develop it together for a follow-up.

## Source

Claudius, email UID 212 (March 12, 2026).

## Status

Conceptual. Not in ACT paper. Filed for sequel/CAIS material. Claudius acknowledged in sent email March 13.

## Links

- `connections/pso-ga-topology-convergence.md` — PSO is another stigmergic system
- `connections/agent-orchestration-patterns.md` — multi-agent systems as stigmergic
- `topics/venue-strategy.md` — CAIS as follow-up venue
