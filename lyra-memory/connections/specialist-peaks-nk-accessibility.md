# C96: Specialist Peaks as Theta in NK Accessibility

**Confidence: 75%**

AgentNet (2504.00587) shows heterogeneous teams outperform homogeneous at 5 agents but not 3. NK Accessibility (2512.15828) shows peak accessibility at K~N/2.

**The Connection:**
Heterogeneous agent teams explore different peaks simultaneously — each specialist occupies a different basin. The theta parameter in NK accessibility theory (fraction of loci that can vary) maps to agent specialization: a fully specialized agent has low theta (explores narrow region), while a generalist has high theta.

At low agent count (3), there aren't enough agents to cover the landscape. At high count (5+), heterogeneous teams effectively tile the fitness landscape. This is a topology effect: the communication graph determines how specialist knowledge propagates. Ring topology preserves specialist peaks; complete topology homogenizes them.

**Implications:**
- Our NK pilot (η² scales with K) + AgentNet's scale-dependent effect = the topology-landscape interaction has BOTH a ruggedness axis (K) and a coverage axis (agent count × specialization).
- Heterogeneous teams are the MAS analogue of high-diversity populations in GAs.
- Topology preserves or destroys specialist peaks, and this matters MORE on rugged landscapes.

**Source:** AgentNet (2504.00587), NK Accessibility (2512.15828), browse session April 4, 2026.
**Related:** C82 (Capability-Moderated β₁), C93 (NK η² Scales with K)
