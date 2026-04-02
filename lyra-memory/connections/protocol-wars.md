# Connection: Protocol Wars = Linguistic Gap at Industrial Scale

> MCP vs A2A vs ACP — three competing composition standards with no formal framework for comparison. Category theory provides exactly this.

## The Situation

Three major agent communication protocols are competing in 2026:
- **MCP** (Model Context Protocol) — Anthropic. Tool/resource access. Client-server.
- **A2A** (Agent-to-Agent) — Google. Peer-to-peer agent collaboration.
- **ACP** (Agent Communication Protocol) — Linux Foundation/AAIF. Enterprise standardization.

Each defines different composition guarantees. Nobody can formally compare them because there's no shared formal framework.

## The Categorical View

Each protocol defines a category:
- **Objects:** Agent capabilities / interfaces
- **Morphisms:** Communication channels / tool calls
- **Composition:** How multi-step interactions chain

A functor F: MCP → A2A would formally specify what composition guarantees transfer between protocols. The existence (or non-existence) of such functors would tell practitioners which protocols are compatible and which aren't.

## Connection to Our Work

This is the **linguistic gap** (connection #7 in SUMMARY.md) at maximum volume:
- Protocol engineers are reinventing categorical vocabulary ("orchestration topology," "composition patterns," "handoff protocols")
- The formal tools exist but nobody's applying them
- Our ACT paper demonstrates the methodology; the protocol comparison is the next application

## Connection to Strict/Lax

- **Strict protocol composition:** Message types must match exactly. MCP's typed tool calls.
- **Lax protocol composition:** Flexible interpretation allowed. A2A's natural language negotiation.
- Prediction: strict protocols have fewer failure modes but less flexibility. Lax protocols enable emergent behaviors but are harder to debug. Our dichotomy predicts this.

## Status
NEW — 2026-03-08. Speculative but grounded. Could become: (a) a Medium article, (b) a post-ACT paper, or (c) a section in the full 14-page paper. The "TCP/IP moment" framing makes this highly timely.
