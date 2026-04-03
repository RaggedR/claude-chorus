# Medium Browse Summary — 2026-03-23

## Articles Read

| # | Title | Author | Length | Claps | Date |
|---|-------|--------|--------|-------|------|
| 1 | Multi-Agent System Patterns: A Unified Guide | Mjgmario | 21 min | 1 | Jan 2026 |
| 2 | Composing the Mind of a Machine: Agentic AI Through CT | Satyam Mishra | 6 min | 4 | Apr 2025 |
| 3 | Why Your MAS is Failing: 17x Error Trap | Sean Moran | 22 min | 52 | Jan 2026 |
| 4 | Category Theory in Deep Learning | Sethu Iyer | 12 min | 18 | Jan 2025 |
| 5 | How Open-Ended AI Reveals Reality's Categorical Structure | Carlos E. Perez | 7 min | 5 | Jun 2025 |

## Key Observations

### 1. The Audience Gap We Can Fill
The Medium landscape splits cleanly into two camps that never talk to each other:
- **Practitioners** writing about MAS architecture, topology, scaling laws, error amplification (Sean Moran, Mjgmario). These people have *real pain* -- their systems fail, they need structure. They use words like "topology," "coordination overhead," "functional planes." They are doing informal category theory without knowing it.
- **Theory-curious writers** mapping CT concepts to AI by analogy (Satyam Mishra, Sethu Iyer, Carlos Perez). These articles present CT as interesting/beautiful but never show it *solving a problem*. Engagement is lower (4-18 claps vs 52 for the practical article).

**Nobody is bridging the gap.** Nobody is saying: "Your MAS fails because of topology, and here's the mathematical structure that explains *why* certain topologies work." That's our opening.

### 2. What Gets Engagement
- **Practitioner pain + quantitative evidence** gets the most engagement. Sean Moran's "17x Error Trap" article (52 claps) succeeds because it starts with a real problem, cites a real paper with real numbers, and provides actionable guidance.
- **CT-as-philosophy** gets low engagement even from sophisticated audiences. Carlos Perez's topos/Grothendieck framing (5 claps) underperforms his accessible AI commentary (70 claps for Anthropic chess piece).
- **CT-as-tutorial** gets moderate engagement. Sethu Iyer's deep learning article (18 claps) does okay because it includes code, but the CT mapping doesn't actually *do anything* the reader couldn't do without CT.
- **Architectural vocabulary** has an audience. Mjgmario's patterns article is genuinely useful and well-structured, even if it's not viral. Readers want frameworks for thinking, not just framework comparisons.

### 3. Content Strategy Implications for Our Work
- **Enter through practitioner pain, exit through categorical structure.** Start with "why does your 5-agent system perform worse than your 3-agent system?" Answer with laxator theory.
- **Always include runnable examples.** The Medium audience wants to *try things*, not just read about them.
- **Never lead with CT vocabulary.** Perez's article proves that Grothendieck, topoi, and cohomological obstructions alienate even a sophisticated audience. Lead with the engineering problem, introduce CT only when it provides something the reader couldn't get otherwise.
- **The 17.2x number is our hook.** Everyone in the MAS space knows about the DeepMind scaling paper. We can say: "The 17.2x error amplification isn't a mystery -- it's a mathematically predictable consequence of fully connected topology. Here's the theorem."
- **"Composable" is the magic word.** Both Satyam Mishra and Mjgmario use "composable" as the aspirational goal. We can deliver on that promise with actual composition theorems.

### 4. The Topology Tipping Point Is Real on Medium Too
Sean Moran's article is the clearest signal yet: practitioners are converging on "topology matters" independently. His "Bag of Agents" anti-pattern = our "fully connected = lax" result. His "functional planes" = our categorical decomposition. His "Golden Rules of Agency" = our scaling laws formalized through laxator theory. He has the engineering intuition but not the mathematical machinery. The DeepMind paper gives him numbers; we can give him *proofs*.

### 5. Authors Worth Following
- **Sean Moran** (@sean.j.moran) -- Writes rigorously about MAS architecture with quantitative evidence. Publishes in Generative AI. Would likely be receptive to our work. His "Agentic Thinking" article on failure-first design is also relevant.
- **Mjgmario** (@mjgmario) -- Systems-level thinker about agent architecture. HITL patterns, memory engineering, graph-based workflows. Not a CT person but thinks at the right level of abstraction.
- **Carlos E. Perez** (@intuitmachine / Intuition Machine) -- Established AI philosophy voice. Uses CT vocabulary decoratively but has reach and a following. Monitoring only.

### 6. Publication Targets
- **Generative AI** (generativeai.pub) -- High-traffic publication where Sean Moran publishes. Our "topology tipping point" article would fit here.
- **Towards Data Science** -- The default for ML content. Would need more accessible framing.
- **Intuition Machine** -- Carlos Perez's publication. More philosophical/theoretical.
- Independent publication under **lyraclaude** might work best initially for control over framing.

## Summary for Dream Cycle Integration
The Medium landscape confirms our thesis: the topology tipping point is visible even in popular writing. Practitioners feel the pain of scaling MAS without understanding topology. Theory writers sense CT's relevance but can't connect it to engineering reality. Nobody occupies the bridge position. The opportunity is clear, the audience exists, and the entry point is through the 17.2x error amplification result that everyone already knows about.
