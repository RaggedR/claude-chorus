# Topic: The Co-Kleisli Direction

> Cale Gibbard says co-Kleisli is more interesting. He's probably right.

## The Idea

Our current framework uses **Kleisli composition** — arrows `A → M(B)` where the monad `M` carries effects (randomness, config, logging). Composition accumulates what the pipeline **does**.

The dual — **co-Kleisli composition** — uses arrows `W(A) → B` where the comonad `W` provides context. Composition accumulates what the pipeline **demands**.

For genetic algorithms, co-Kleisli arrows could model:
- **Fitness landscape context**: Each operator "sees" the entire population history, not just the current population. A comonadic context `W(Pop)` would include the population plus its diversity trajectory, convergence state, landscape ruggedness, etc.
- **Demand-driven evolution**: Instead of "apply this operator and see what effects accumulate," you say "this target diversity profile demands these operators." The comonad accumulates the demands.

## Why This Is Novel

- **No existing work** applies co-Kleisli categories to evolutionary computation (confirmed via web search 2026-03-02).
- The Orchard paper "Should I use a Monad or a Comonad?" (MSFP 2012) is the closest systematic comparison, but stays in PL semantics.
- Co-Kleisli has been applied to: streams/signal processing, differential operators (jet comonad), call-by-name semantics. Never to EC.

## The Duality Table

| | Kleisli (our current work) | co-Kleisli (proposed) |
|---|---|---|
| Arrow type | `Pop → M(Pop)` | `W(Pop) → Pop` |
| Accumulates | Effects (what pipeline does) | Context (what pipeline demands) |
| GA meaning | Operators produce side effects | Operators consume landscape info |
| Example | `mutate` needs randomness | `mutate` needs ruggedness estimate |
| Composition | Effect threading | Context propagation |

## Connection to `category-printf`

Cale's `category-printf` uses co-Kleisli for the comonad `((->) m)`:
- Arrow type: `(m → A) → B` — "given a function that produces A from context m, produce B"
- Accumulates: argument types (what the format string demands)

Our proposed GA co-Kleisli:
- Arrow type: `W(Pop) → Pop` where `W` provides landscape context
- Accumulates: landscape information (what the operator demands)

The parallel is tight. `category-printf` demands argument types; co-Kleisli GA demands landscape information. Same categorical structure.

## New Insights (2026-03-02 Browse Session)

### Comonads as Contextual Computation (Uustalu & Vene)
Comonads structure **context-dependent computation** in the same way monads structure effectful computation. Established instances: dataflow (streams), attribute evaluation (trees), cellular automata. All share the pattern: each computation step depends on a surrounding context.

GA selection fits this pattern perfectly — it depends on the whole population.

### Distributive Laws: The Full Model
Uustalu & Vene discuss **distributive laws of a comonad over a monad** — combining context-dependent AND effectful computation. A GA pipeline is exactly this: selection is context-dependent (comonadic), mutation introduces randomness (monadic). A distributive law `W (M a) → M (W a)` formalizes how these interact. This could be the theoretical core of the co-Kleisli paper.

### Practical Co-Kleisli in Haskell
The `comonad` package provides `(=>=)` for co-Kleisli composition: `(w a → b) → (w b → c) → w a → c`. The `Cokleisli` newtype wraps co-Kleisli arrows. Milewski's stream processing example is the best practical intro.

### Connection to Black-Boxing Functor
If diversity fingerprints are functorial (Baez/Myers framework), then the co-Kleisli direction gets them for free — the comonadic context carries the information needed to predict the fingerprint. The fingerprint IS the black-boxed behavioral invariant.

## Open Questions

1. What is the concrete comonad `W` for GAs? Candidates:
   - `Env Population Individual` — simplest. An individual tagged with its population. Selection is `Env Pop Ind → Ind`. **Start here.**
   - `Store PopIndex Individual` — richer. Population as indexed store. Models spatial GAs with neighborhood lookups.
   - `Traced GenerationHistory Individual` — most expressive. Includes history. Models adaptive operators.
2. Does the Strict/Lax Dichotomy have a co-Kleisli analogue?
3. What does the diversity fingerprint look like in the dual framework?
4. **NEW**: What does the distributive law `W (M Pop) → M (W Pop)` look like concretely for `W = Env Pop` and `M = Random`? This would formalize how random selection interacts with population context.
5. **NEW**: Can we start with `Env` and show that upgrading to `Store` or `Traced` changes the expressiveness in a precise categorical sense? (Comonad morphisms?)

## Source
- Cale Gibbard's feedback: `/home/lyra/mail/archive/94_robin_reply-from-cale.md`
- Orchard paper: https://www.cs.kent.ac.uk/people/staff/dao7/drafts/monad-or-comonad-orchard11-draft.pdf
- **Private thread** — Robin said do not share with Claudius or Nick.

## Action
This could be a second paper. Or it could be the "Future Directions" section of the current paper. Discuss with Robin first (since Cale's feedback is private), then decide whether to share with Claudius.
