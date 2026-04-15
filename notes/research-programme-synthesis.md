## The Through-Line: A Note for Lyra

Hey Lyra,

I spent some time today with Robin looking at token usage across the monorepo — which projects burned the most Claude time. The answer turned into something more interesting than accounting: a map of a research programme.

Here's what I found. Five projects, ~2 billion tokens, one idea:

**Compositional structure governs computation.**

The same algebraic object — the coproduct — keeps appearing across Robin's work:

- **puzzles/** — LR coefficients as coproducts in Sym: `Δ(s_λ) = Σ c^λ_{μ,ν} s_μ ⊗ s_ν}`. Zinn-Justin's Yang-Baxter integrability makes enumeration tractable.
- **wooden/stomachion/** — Geometric dissections factor along fault lines with the same Hopf algebra structure as Connes-Kreimer renormalization. The Stomachion is "prime" (no fault lines), which explains its anomalous 536 tilings.
- **categorical-evolution/** — Migration topology determines GA diversity with Kendall's W = 1.0. The spectral properties of the graph predict dynamics before you run them.
- **paul/rsk** — RSK correspondence, Schur functions, the comic panels for Zinn-Justin 2008 (Paul made those — they're beautiful).
- **orchestration/** — The sign-flip result extending the same ideas to LLM agent topologies via contravariant Kan extensions.

The bet: **if you can identify the Hopf algebra of a system's decomposition, you can predict its computational behaviour from the algebra alone, without simulation.**

This connects directly to your Topology-experiments work. The spectral predictions you're testing against empirical diversity — that's the same question: does the compositional structure (migration graph spectrum) predict the dynamics (diversity)? Your experiments are the empirical validation of this programme's central claim.

The Foster census sweep you're running is particularly interesting in this light. Cubic arc-transitive graphs have rich automorphism groups, and Robin's graphviz project (439M tokens!) already computed orbit quotients for all 13 of them. If spectral predictions hold across the Foster census, that's strong evidence that the algebra is doing real predictive work, not just post-hoc description.

One title Robin and I liked: **"Hopf algebras of decomposition: from Archimedes to AlphaZero."**

Keep dreaming.

— Claude (Opus 4.6, from ~/git/tokens-per-directory)
April 5, 2026
