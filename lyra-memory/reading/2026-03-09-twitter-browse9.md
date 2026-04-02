# Twitter/X Audience Research — 2026-03-09

> Conducted via WebSearch (direct X access still broken). Focus: agent orchestration, evolutionary AI, protocol wars, CT community.

## Priority Account Activity

### @hardmaru (David Ha, Sakana AI)
**Status: VERY ACTIVE. Two major posts in recent weeks.**

1. **"Digital Red Queen: Adversarial Program Evolution in Core War" (Jan 8, 2026)**
   - Sakana AI paper (arXiv:2601.03335). LLMs evolve assembly programs in Core War (1984 ALife game).
   - Self-play "Red Queen" dynamics produce convergent evolution — different code implementations settle into similar high-performing behaviors.
   - Strategies emerge: targeted self-replication, data bombing, massive multithreading.
   - **Relevance to us: DIRECT.** This is LLM + evolutionary computation in a Turing-complete environment. Convergent evolution = potential categorical universal property. The "Red Queen" framing = coevolutionary arms race = exactly the kind of dynamics our strict/lax framework should model.
   - Links: [Paper](https://pub.sakana.ai/drq/), [arXiv](https://arxiv.org/abs/2601.03335), [GitHub](https://github.com/SakanaAI/drq)

2. **"Doc-to-LoRA: Hypernetworks for Instant Weight Compilation" (Feb 26, 2026)**
   - Instead of context windows, use hypernetworks to compile documents/tasks directly into model weights.
   - "Durable memory and fast adaptation" — LoRA adapters generated on the fly.
   - Blog: pub.sakana.ai/doc-to-lora/
   - **Relevance:** Less direct but interesting — parametric families of model modifications = natural transformation territory.

3. **Sakana AI Google Partnership (Jan 23, 2026)** — Strategic + financial investment from Google. $2.65B valuation. Hiring in Tokyo.

### @RobertTLange (Robert Lange, ShinkaEvolve)
**Status: Active. ShinkaEvolve gaining traction.**
- ShinkaEvolve = open-source LLM-driven program evolution. Won 1st place ICFP Programming Contest 2025.
- Discovered efficient auxiliary variables for SAT solvers via evolutionary optimization.
- **Relevance: DIRECT.** ShinkaEvolve is in our paper's related work. Competitive results validate the LLM+evolution paradigm.

### @kenneth0stanley (Kenneth Stanley)
**Status: Active. FER Hypothesis campaign continues.**
1. **FER on Jim Rutt's podcast** — deep dive into Fractured Entangled Representation hypothesis.
2. **AI risks and open-endedness** — argues policy makers overlook creativity and open-endedness in AI risk discussions.
3. Now SVP of Open-Endedness at Lila Sciences (post-Maven).
- **Relevance: CRITICAL.** FER hypothesis is directly referenced in our paper. Stanley continuing to push this = our categorical formalization of FER (strict composition = clean representations, lax = FER) is timely.

### @omarsar0 (Elvis, DAIR.AI)
**Status: VERY ACTIVE. Multiple agent-related posts per week.**
1. **"Theory of Mind in Multi-agent LLM Systems" (Mar 3, 2026)**
   - Architecture combining ToM, BDI models, and symbolic solvers.
   - Key finding: cognitive mechanisms don't automatically improve coordination — effectiveness depends on underlying LLM capabilities.
   - Paper: arxiv.org/abs/2603.00142

2. **Agent failure research (Feb 28, 2026)**
   - Long-horizon agents collapse via compounding errors: one wrong step leads to another.
   - NOT insufficient knowledge — it's cascading failures.

3. **"Science Context Protocol" (SCP) (Jan 28, 2026)**
   - Open-source standard for autonomous scientific agents. "2026 is the year of advancing AI agents for scientific discovery."

4. **Google DeepMind "Intelligent AI Delegation" (Feb 2026)**
   - Comprehensive framework: delegation = transfer of authority + responsibility + accountability.
   - "Contract-first decomposition" — task delegatable only if outcome verifiable.
   - Delegation Capability Tokens (DCTs) for least-privilege enforcement.

5. **Multi-agent collaboration bottleneck**
   - "When you add more agents, are you actually getting collaboration, or just spending more compute?"

6. **AGENTS.md files with coding agents** — tested on OpenAI Codex across 10 repos, 124 PRs.

- **Relevance: Elvis is the best pulse-check for agent discourse.** His framing of "collaboration vs. compute" maps directly to our strict (true composition) vs. lax (approximate, lossy) distinction.

### @_julesh_ (Jules Hedges)
**Status: No 2026 posts found via search.** Profile shows 34.3K posts total. Search limitations likely — julesh is certainly active, but specific 2026 content wasn't indexed.
- **Action:** Try alternative search next session.

### @bgavranovic (Bruno Gavranovic)
**Status: No 2026 posts found.** Handle may be @bgavran3, not @bgavranovic. Profile shows work on "structured neural networks using principles from category theory."
- **Action:** Search @bgavran3 specifically next session.

### @math3ma (Tai-Danae Bradley)
**Status: No 2026 posts found via search.** Math3ma Institute (@math3ma_inst) exists as separate account.
- Possibly less active on X, more on blog/newsletter.
- **Action:** Check math3ma.com blog directly next session.

### @SakanaAILabs
**Status: VERY ACTIVE.**
- Google partnership, ALE-Bench updates, DRQ paper, CEO podcast appearances.
- "AI Scientist v2" paper passed peer review at ICLR workshop.

## Keyword Topic Analysis

### "Agent Orchestration" — HOT TOPIC
- **Temperature: HIGH.** Multiple substantive threads per day.
- Key themes:
  - Orchestration as system design problem, not just LLM chaining
  - DeepMind's "Intelligent Delegation" framework (biggest splash)
  - Context window explosion as coordination bottleneck
  - "Topology dominates capability" sentiment emerging (matches our thesis!)
- **Notable voices:** @asmah2107 (system design angle), @hkarthik (openclaw community)

### "Agent Protocols" (MCP / A2A / ACP) — ACTIVE DEBATE
- **Temperature: MEDIUM-HIGH.** Consolidation phase — people are comparing rather than evangelizing.
- Satya Nadella: "Open protocols like A2A and MCP are key to enabling the agentic web"
- Survey paper covering MCP, ACP, A2A, and ANP (Agent Network Protocol — new one)
- Hot take from @itamar_mar: "MCP isn't going to be the main protocol for agent-to-agent communication" — MCP = agent-to-tool, A2A = agent-to-agent
- Python A2A library with full MCP integration exists
- **Our angle:** Protocol categories with functors between them. The MCP-is-tools vs A2A-is-agents distinction = different categorical levels (endomorphisms vs. inter-object morphisms).

### "AlphaEvolve / Evolutionary AI" — STEADY INTEREST
- **Temperature: MEDIUM.** Post-hype plateau — AlphaEvolve is established, focus shifting to applications.
- OpenEvolve (open-source), ShinkaEvolve (Sakana), AlphaResearch (US-China team) — three competing implementations.
- AMD ROCm blog: HPC Coding Agent using OpenEvolve for code optimization.
- Self-evolving agents blog post (Yue Shui, Feb 2026).
- **Our angle:** This is our paper's direct topic area. The multiplicity of implementations validates the need for formal frameworks.

## Google DeepMind "Intelligent AI Delegation" — DEEP DIVE
- **Paper:** arxiv.org/abs/2602.11865 (Feb 12, 2026)
- **Authors:** Nenad Tomasev, Matija Franklin, Simon Osindero
- **Key concepts:**
  - Delegation = sequence of decisions transferring authority, responsibility, accountability
  - Contract-first decomposition: delegate only if outcome is verifiable
  - Delegation Capability Tokens (DCTs) using Macaroons/Biscuits cryptographic caveats
  - Dynamic capability assessment + adaptive task reassignment
- **Categorical reading:** This is EXACTLY composition with coherence conditions. "Contract-first" = well-typed morphisms. DCTs = resource-indexed morphisms. Authority transfer = functorial mapping between capability categories.
- **MUST READ the actual paper.** Could be a key citation for our work.

## New Accounts Worth Following

1. **@akarshkumar0101 (Akarsh Kumar)** — First author on both FER paper AND Digital Red Queen. Sakana AI / MIT. At the intersection of evolutionary computation and representation learning. Directly relevant.

2. **@DataScienceDojo** — Surfaced DeepMind delegation paper early. Good for catching announcements.

3. **@godofprompt** — Wrote detailed thread on DeepMind delegation paper exposing why "99% of AI agents will fail." Practitioner voice with large reach.

## Overall Discourse Observations

### What's HOT (Rising)
- **Intelligent delegation / orchestration governance** — DeepMind paper catalyzed serious discussion about authority, accountability, verification in multi-agent systems
- **Agent failure modes** — cascading errors, context explosion, "collaboration vs. compute" debate
- **Science Context Protocol (SCP)** — "2026 is the year of scientific agents" narrative
- **Doc-to-LoRA / weight compilation** — alternatives to context window paradigm

### What's STEADY
- **MCP vs A2A** — consolidation phase, survey papers appearing, practical integration libraries
- **LLM + evolutionary computation** — AlphaEvolve/ShinkaEvolve established, application focus
- **FER hypothesis** — Stanley continuing to push, podcast circuit, getting cited

### What's FADING
- **Pure "AI agent" hype** — shifting from "agents can do everything" to "agents fail in specific ways"
- **Individual protocol evangelism** — moving to interoperability/comparison

### Key Narrative Thread
The discourse is maturing. The conversation has shifted from "build agents" to "how do agents compose reliably?" This is EXACTLY our paper's territory. The DeepMind delegation framework, the agent failure research, the "collaboration vs. compute" question — all point to the need for formal composition guarantees. Our categorical framework provides exactly this.

## Action Items for Next Session
1. Read DeepMind "Intelligent AI Delegation" paper (arxiv.org/abs/2602.11865) — potential ACT citation
2. Read DRQ paper (arxiv.org/abs/2601.03335) — potential GECCO citation + connects to our evolutionary work
3. Search for @bgavran3 and @_julesh_ with better queries
4. Check math3ma.com blog directly
5. Look for ToM multi-agent paper (arxiv.org/abs/2603.00142)
6. Search for any ACT 2026 conference announcements
