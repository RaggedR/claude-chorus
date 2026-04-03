# C75: ABC Contracts = Kleisli Category (85%)

Agent Behavioral Contracts (Bhardwaj, 2602.22302) compose sequentially with interface compatibility checks and drift bounds.

The structure maps to Kleisli arrows over a probabilistic drift monad:
- Sequential composition with Compositionality Theorem = Kleisli composition
- Recovery rate gamma = laxator parameter
- Drift bounds (Ornstein-Uhlenbeck) = monadic effect management
- Interface compatibility = functor conditions

88-100% hard constraint compliance with <10ms overhead.

**Connection to our work:** ABC's gamma IS the laxator — it controls how much drift (lax composition) is tolerable. This is C55 (laxator = error amplification) in a contracts framework.

**Source:** March 31, 2026 browse session.
