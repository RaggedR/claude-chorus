# Question: What Is the Right Comonad for Genetic Algorithms?

> If Kleisli composition models effects (what operators do), co-Kleisli composition should model context (what operators demand). But what's the concrete comonad?

## Candidates

### 1. `Env` comonad (simplest)
```haskell
data Env e a = Env e a
-- co-Kleisli arrow: Env LandscapeInfo Pop -> Pop
```
Each operator receives the population plus read-only landscape metadata (ruggedness, correlation length, neutrality). This is just a Reader in comonadic clothing — probably too simple to be interesting.

### 2. `Store` comonad
```haskell
data Store s a = Store (s -> a) s
-- co-Kleisli arrow: Store FitnessLandscape Pop -> Pop
```
Each operator sees the current population AND a function that maps any population state to a property (e.g., diversity). The operator can "peek" at hypothetical population states. This is powerful — it models operators that are landscape-aware.

### 3. `Traced` comonad
```haskell
data Traced m a = Traced (m -> a)
-- co-Kleisli arrow: Traced History Pop -> Pop
```
Each operator sees a function from history to the current population. This models operators that can look back at the evolutionary trajectory. History-aware mutation rates, for example.

### 4. Custom comonad combining all three
```haskell
data EvoW a = EvoW
  { landscape :: LandscapeInfo    -- Env component
  , peek :: Pop -> Double         -- Store component
  , history :: [GenerationLog]    -- Traced component
  , current :: a                  -- The actual value
  }
```

## The Key Question
Does the co-Kleisli composition of any of these produce interesting categorical properties? Specifically:
- Is there a co-Kleisli Strict/Lax Dichotomy? (Dual of our theorem)
- Do co-Kleisli diversity fingerprints differ from Kleisli ones?
- Does the comonad extract-duplicate structure have a GA interpretation?

## Status
Completely unexplored. This needs Haskell prototyping, not just theory.
