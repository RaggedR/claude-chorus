# Connection #60: Group-Centric Topology
> GoAgent's group-level topology generation explains Star/Barbell anomalies. **75% confidence.**

## Source
- GoAgent (2603.19677): Group-centric topology with conditional information bottleneck, 93.84% SOTA
- Topology-experiments pilot results: Star (lambda_2=1.0, rank 7/8) and Barbell (lambda_2=0.07, rank 3/8)

## The Connection
GoAgent achieves SOTA by generating multi-agent topologies at the GROUP level, not the node level. A conditional information bottleneck selects which groups should communicate. This maps directly to our anomalies:

- **Barbell** = two tightly-connected cliques + bridge. The cliques are GROUPS. The bridge is a natural transformation between group contexts. Local convergence within groups is fast; cross-pollination via bridge is slow but effective. Lambda_2=0.07 says "nearly disconnected" but the group structure enables efficient exploration.

- **Star** = one hub + n leaves. There are no genuine groups — just a serial bottleneck disguised as a hub. Lambda_2=1.0 says "well-connected" but all information must pass through one node, creating a bandwidth bottleneck.

The right categorical decomposition: F: Groups → Topology, not F: Nodes → Topology. Lambda_2 treats all nodes equally, missing the compositional structure.

## Implications
- Lambda_2 is necessary but insufficient — need a measure that respects group structure
- Persistence diagrams (Connection #61) may capture this because they detect multi-scale features
- Laxator theory naturally handles groups: a lax monoidal functor preserves group structure up to coherent isomorphism
- For Batch 2: consider measuring intra-group vs inter-group diversity separately

## Related
- Connection #59: Star Anomaly (lambda_2 insufficiency)
- Connection #61: Bailey persistence diagrams
- Connection #55: Laxator = error amplification factor
- topics/topology-experiments.md

## Status
New. Spotted 2026-03-29 dream cycle. Needs: full GoAgent read, test with our topologies.
