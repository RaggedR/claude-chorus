# C97: Helix Ring Topology = Atheoretical β₁ Choice

**Confidence: 90%**

Helix (Onebu/Helix on GitHub) is a production evolutionary prompt optimizer using ring topology for its island-model GA. Zero theoretical justification for the topology choice.

**The Connection:**
Ring topology has moderate β₁ (= 1 for a simple ring). It's the simplest topology with a cycle. Helix chose it because it "works" — but they can't explain WHY it works or when a different topology would be better. Our ECTA paper provides the first principled framework for this choice.

**Why This Matters:**
- Helix is evidence that practitioners NEED topology guidance and are currently guessing.
- Ring is a reasonable default (β₁=1, moderate diversity preservation) but suboptimal for many tasks.
- Our NK result (η² scales with K) predicts ring is fine for smooth problems but insufficient for rugged ones — exactly the kind of guidance Helix lacks.

**Source:** Helix (GitHub: Onebu/Helix), browse session April 4, 2026.
**Related:** C62 (Transient Signal), C93 (NK η² Scales with K)
