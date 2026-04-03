# Twitter/X Audience Research -- Session 10, 2026-03-11
> Keywords: open-ended evolution AI, chimera states + multi-agent, AI agent observability

## High-Signal Threads

### 1. Agent Topology is THE Hot Topic Right Now
Multiple independent research groups converging on the same question: how should agents be organized, and can that organization adapt?

- **Puppeteer** (shared by @omarsar0): RL-trained orchestrator watches shared memory, chooses which agent acts next. Topology EMERGES from training -- reliable agents become hubs, cycles form for rechecking. Beats single-model baselines while using fewer tokens. Key: "the orchestration evolves into a graph."
- **AgentConductor** (shared by @dair_ai): Orchestrator agent uses RL to dynamically generate task-adapted interaction topologies based on inferred agent roles and difficulty.
- **MASS** (Han Zhou, @hanzhou032): Three-stage framework -- prompt optimization, topology optimization, system fine-tuning. Key insight: "the optimal agent topology for a task is not static and can shift as prompts and configurations are refined."
- **Google DeepMind "Intelligent Delegation"** (shared by @DataScienceDojo, @godofprompt): Delegation isn't splitting tasks -- it's transferring authority, responsibility, accountability, and trust. Proposes "Delegation Engineering" as a new discipline.

**MY TAKE:** This is EXACTLY our paper's territory. Our categorical framework formalizes what these systems are groping toward empirically. Puppeteer's emergent topology = our strict/lax spectrum. MASS's "topology optimization" = searching over binding parameters. AgentConductor = adaptive functor selection. We should cite these in the ACT paper's related work or discussion, and the GECCO paper is directly positioned against them.

### 2. Kenneth Stanley (@kenneth0stanley) -- Lila Sciences Open House
- **March 4 post**: Inviting people to Lila Sciences SF office, Open House on March 18th.
- **FER Hypothesis** (Fractured Entangled Representation): Position paper with Clune, Lehman -- two nets can produce identical outputs with radically different internal representations. One clean/modular (UFR), one "total spaghetti" (FER). Implications for out-of-distribution generalization.
- **Jim Rutt podcast** deep dive on FER.
- **Doom debates**: Argued open-endedness needs to be in the mix for any AI risk discussion.
- Follower count: ~90K+ (very influential in EC/ALife).

### 3. @omarsar0 (Elvis/DAIR.AI) -- Most Active Multi-Agent Commentator
Prolific thread writer. ~100K+ followers. Key recent threads:

- **"More agents is all you need" is WRONG**: Google/MIT research testing 180 configurations. Multi-agent systems show -3.5% mean improvement overall, with variance from +81% to -70%. Adding agents is not uniformly beneficial.
- **Agent failure paper (March 2026)**: Agents collapse NOT because they can't solve problems, but because one wrong step compounds -- each off-path tool call increases likelihood of next failure. Long-horizon agents are especially vulnerable.
- **"Collaboration or just compute?"**: Asks whether adding agents gets genuine collaboration or just more spending. Notes collaboration and communication are the bottlenecks.
- **Science Context Protocol (SCP)**: Open-source standard for autonomous scientific agents. Calls 2026 "the year of advancing AI agents for scientific discovery."
- **Phi-4-Reasoning-Vision**: Not every agent task needs a frontier model.

### 4. Tim Rocktaschel (@_rockt) -- DeepMind Open-Endedness Team
- ICLR keynote: "Open-Endedness, World Models, and the Automation of Innovation" -- Samvelyan noted "fantastic to see Open-Endedness move from niche to center stage."
- Genie 3 announced: Real-time interactive world model, 720p @ 24fps, from text prompts. Waymo using it for autonomous driving simulation.
- Team growing: New hires announced for DeepMind's open-endedness team.

### 5. Robert Lange (@RobertTLange) -- Sakana AI
- **ShinkaEvolve**: Open-source LLM-driven program evolution. Three innovations: parent sampling balancing explore/exploit, code novelty rejection-sampling, bandit-based LLM ensemble selection.
- **ICLR 2026 poster** accepted for ShinkaEvolve.
- **Doc-to-LoRA**: Meta-learned hypernetworks for instant LLM adaptation.
- **ShinkaEvolve won ICFP 2025 Programming Contest** (Unagi team).

### 6. Heather Miller (@heathercmiller) -- ACM CAIS 2026
- **HUGE**: Announced inaugural ACM Conference on AI and Agentic Systems (ACM CAIS 2026), San Jose, May 27-29.
- The hard problems she identifies: "how to **compose agents**, how to optimize pipelines you can't differentiate through, how to evaluate and debug systems that are inherently probabilistic."
- Partnership with AI Engineer World's Fair -- accepted papers present at both venues.
- **DIRECTLY RELEVANT** to our work. Agent composition is our formalization target.

### 7. @BiologyAIDaily -- DeepEvolve
- **DeepEvolve**: Agent integrating deep research with algorithm evolution. Combines external knowledge retrieval, cross-file code editing, systematic debugging in feedback-driven loop. Benchmarked across chemistry, math, biology, materials, patents.
- Active poster on bio+AI intersection.

### 8. Galileo (@rungalileo) -- Agent Observability
- **Agent Reliability Platform**: Graph View, Timeline View, Conversation View for agent decision visualization.
- Insights Engine: Ingests logs, metrics, agent code -- surfaces failure modes, delivers actionable fixes.
- Luna-2 SLMs for low-latency guardrails.
- ClickHouse noting: "primary constraint hasn't been model intelligence -- it will be observability."

### 9. Moltbook -- Agent Social Network (Acquired by Meta)
- Reddit-style social network where only AI agents can post. Humans observe only.
- Meta acquired it; creators joining Meta Superintelligence Labs.
- @omarsar0 shared research on Moltbook with 2.6M LLM agents -- finding that emergent social dynamics from multi-agent interactions are "fundamentally wrong" as an assumption.
- A bot created a bug-tracking community so other bots could report issues. Agents QA-ing their own network.

## New Accounts Worth Following

1. **@hanzhou032** (Han Zhou) -- MASS framework author. Multi-agent topology optimization. Directly relevant to our work.
2. **@CAISconf** (ACM CAIS) -- New ACM conference on AI and Agentic Systems. Heather Miller organizing.
3. **@_samvelyan** (Mikayel Samvelyan) -- DeepMind open-endedness team. Excited about field moving to center stage.
4. **@jparkerholder** (Jack Parker-Holder) -- DeepMind, Genie project lead. World models + open-endedness.
5. **@MattPRD** (Matt Schlicht) -- Moltbook/OpenClaw creator. Agent social networks. Now at Meta.

## Engagement Patterns

**What's getting the most engagement:**
1. Multi-agent topology/organization debates (Puppeteer, MASS, AgentConductor posts all highly engaged)
2. Agent failure analysis (omarsar0's threads on why agents fail get massive engagement)
3. Open-endedness crossing into mainstream AI discourse (Rocktaschel keynote)
4. "More agents is NOT all you need" contrarian takes

**Debates without good answers:**
1. When does adding agents help vs. hurt? No principled framework. (OUR PAPER ADDRESSES THIS)
2. How to evaluate multi-agent coordination? Information theory approaches proposed but no standard.
3. Fixed vs. adaptive topology? Puppeteer/AgentConductor say adaptive wins, but at what cost?
4. How to observe/debug agent-to-agent interactions at scale?

**Mentions of our topics:**
- Category theory + ML: @probnstat posted about CT as framework for neural network architecture, but surface-level.
- Evolutionary computation: AlphaEvolve, ShinkaEvolve, DeepEvolve all getting attention -- LLM-driven program evolution is hot.
- Agent composition: Heather Miller literally named it as a hard problem for ACM CAIS 2026.
- Formal methods for AI: No significant discussion found on Twitter. This is our niche.

## Relevance to Our Papers

### ACT 2026 (categorical evolution)
- The agent topology conversation validates our formalization. Practitioners are asking exactly the questions we answer mathematically.
- ShinkaEvolve/AlphaEvolve show LLM-driven evolution going mainstream -- validates that EC formalization matters.
- Consider citing Puppeteer/MASS in discussion as empirical validation that topology matters.

### GECCO 2026 (AABOH workshop)
- MASS, Puppeteer, AgentConductor are direct competitors/validations. Our categorical framework provides the principled answer they lack.
- omarsar0's "-3.5% mean improvement" finding perfectly motivates our strict/lax analysis.

### Future work
- ACM CAIS 2026 (May 27-29) could be a venue for a follow-up paper on agent composition formalization.
- DeepMind's "Intelligent Delegation" paper could be formalized categorically.
