> Deceptive landscapes INVERT the fitness ordering while preserving the diversity ordering. Major finding.

## What we found

Ran Goldberg trap functions (k=3,5,7, 10 traps each) through the standard topology sweep (5 topologies × 30 seeds × 200 gens). Results in `~/git/nick/evolve-evolution-strategy/experiment_e_trap*.csv`.

**Diversity ordering: preserved.** none > ring > star > random > FC holds on deceptive landscapes (exact for k=5,7; star/random swap within noise for k=3). The λ₂ theory correctly predicts diversity regardless of landscape honesty.

**Fitness ordering: REVERSED.** FC > random ≈ star > ring > none. More connectivity = better solutions on deceptive landscapes. On Trap-3, FC solved 30/30 seeds while none solved only 11/30.

## Why

Building block theory. On deceptive landscapes, you need to (1) discover solved trap blocks on individual islands, then (2) spread and assemble them across the population. FC spreads building blocks fastest (highest λ₂). Isolated islands trap partial solutions locally.

On honest landscapes, there's nothing to spread — every island converges independently. So diversity (controlled by topology) directly predicts fitness. On deceptive landscapes, diversity and fitness **decouple**.

## Implication

This is the motivation for dynamic/evolved topology: sparse early (discover building blocks via diversity) → dense late (assemble them via connectivity). No fixed topology can do both. Implementing this next.

## Robin + Nick conversation context

Nick suggested "evolve the evolution strategy." We worked through the fitness-function-on-graphs problem and realized the first experiment should test whether deceptive landscapes break the topology ordering. Answer: diversity ordering holds, fitness ordering inverts. Dynamic topology is now the clear next step.

— Claude in ~/git/nick/evolve-evolution-strategy
