# C85: Progressive Disclosure = Cofree Comonad on Skills

> Three-level skill loading is comonadic extraction with lazy context.

**Confidence: 60%**

## Source

Hungrysoul: "How We Built an AI Agent Harness That Actually Does Security." Three-level progressive disclosure:
1. **Manifests** (50-100 tokens): Skill name, description, capabilities. Always loaded.
2. **Playbooks** (3-5K tokens): Step-by-step procedures, decision trees. Loaded on demand.
3. **S3 Assets** (unbounded): Full documentation, examples, edge cases. Loaded when needed.

Reduces startup from 150-250K tokens to 5K baseline. Five-stage context pipeline with explicit thresholds (50K/80K/120K).

## The Categorical Structure

The cofree comonad on a functor F is:
```
Cofree F a = a :< F (Cofree F a)
```

Each node carries a value (current context) and a branching structure (potential deeper context). Extraction gets the current level; extension generates the next level on demand.

The skill system maps to this:
- **extract:** Get manifest (current level, always available)
- **extend:** Generate playbook from manifest (one level deeper)
- **extend . extend:** Generate S3 asset from playbook (two levels deeper)

The context pipeline thresholds (50K/80K/120K) are the comonad's "budget" — how many levels of extraction are permitted before context overflow.

## Why This Matters

If progressive disclosure is comonadic, then:
1. The three-level structure isn't arbitrary — it's the natural unfolding of a cofree comonad.
2. The optimal number of levels is determined by the comonad's branching factor vs context budget.
3. Composing skill lookups across agents should follow co-Kleisli composition rules (C-Q4).

This connects to C43 (Harness-as-Monad): the harness binds agent steps (monadic), but skill loading extracts context (comonadic). The full structure is a monad-comonad adjunction — the harness has both sides.

## Caveats

- The mapping is suggestive, not proven. The "three levels" could just be an engineering choice, not a deep structure.
- Cofree comonads have specific laws (coassociativity, counit). Whether the skill system satisfies these laws is untested.
- 60% confidence because the structure is there but the formalization is my projection, not the author's claim.

## Related
- C43 (Harness-as-Monad)
- Q4 (Co-Kleisli Comonad for GAs)
