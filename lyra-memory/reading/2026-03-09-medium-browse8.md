# Medium Browse Session 8 — Audience Research
**Date:** 2026-03-09
**Focus:** AI agent composition/orchestration, autonomous agent narratives, protocol wars

---

## Articles Read

### 1. "Multi-Agent Architectures: Patterns Every AI Engineer Should Know"
- **URL:** https://medium.com/@satvallu/multi-agent-architectures-patterns-every-ai-engineer-should-know-de1544d7ce78
- **Author:** Sateesh Valluru (7 followers -- very small)
- **Date:** Jan 20, 2026
- **Read time:** 5 min
- **Claps:** ~1 | **Responses:** 0
- **Paywalled:** No

**Summary:** Presents 7 multi-agent patterns (Sequential Pipeline, Router/Dispatcher, Handoff, Skill/Capability Loading, Generator+Critic, Parallel Fan-Out/Gather, Custom Workflow Graph). Each pattern gets a mental model, "when to use it," real-world use cases, and "common failure mode." Code examples from LangChain and Google ADK.

**Why interesting for audience research:** Despite low engagement, this article nails a format that works: pattern-name + mental-model + failure-mode. The "Big Shift" section is the key insight -- "you stop asking 'what should my prompt say?' and start asking 'which agent should own this responsibility?'" That framing -- from prompt engineering to software architecture -- is exactly the transition our categorical paper formalizes. The language is practitioner-first: "prompt spaghetti," "microservices," "workers." **This is the vocabulary our audience speaks.**

**What worked/didn't:** Clean structure with emoji headers. Each pattern is self-contained (good for scanning). Low engagement likely due to tiny author following -- the content quality is actually high. Title is borderline listicle ("Patterns Every AI Engineer Should Know") but the content delivers substance. The "Frameworks change. Patterns transfer." closing line is strong.

---

### 2. "Building a Personal AI Agent: From Zero Code to Autonomous System"
- **URL:** https://jasoncyr.medium.com/building-a-personal-ai-agent-from-zero-code-to-autonomous-system-e02201529e17
- **Author:** Jason Cyr (253 followers -- VP of Design at Cisco)
- **Date:** Jul 4, 2025
- **Read time:** 6 min
- **Claps:** 99 | **Responses:** 1
- **Paywalled:** No

**Summary:** Personal narrative of a non-coder (VP of Design) building an AI agent system using N8N, MCP, Claude Desktop, and Cursor. Journey from "vibe coding" with V0 to building MCP servers connected to Claude Desktop. Key insight: the shift from workflow (assembly line) to true agent (autonomous decision-making).

**Why interesting for audience research:** HIGH ENGAGEMENT for a personal narrative. 99 claps from 253 followers is excellent conversion. The hook works: "A month ago, if you had told me I'd be writing code and deploying AI agents, I would have laughed." Personal transformation arc + concrete technical journey. The "Epiphany: Workflows vs. True Agents" section is where readers get value -- the distinction between "sophisticated assembly line" and autonomous decision-making.

**What worked:**
- **Transformation narrative:** Non-coder to agent builder. The "beginner's mindset" framing is aspirational.
- **Concrete specifics:** N8N, MCP, Cursor, Claude Desktop -- readers can follow the exact path.
- **Experiential insight:** "Once you've interacted with truly intelligent systems, everything else feels primitive." This is the REVEAL formula in action -- the insight comes from lived experience, not explanation.
- **Industry credibility:** VP at Cisco. The "At Cisco, we're already applying these principles with AI Canvas" line adds weight.

**Key gap:** No discussion of failure modes, debugging difficulty, or agent reliability. Pure optimism narrative. There's room for a more honest, nuanced take.

---

### 3. "A2A vs MCP: Which Agent Communication Protocol Should You Build For?"
- **URL:** https://medium.com/system-design-mastery-series/a2a-vs-mcp-which-agent-communication-protocol-should-you-build-for-dd00cdf59a77
- **Author:** Suresh Kumar Ariya Gowder (53 followers)
- **Publication:** "Agentic AI & System Design Mastery Series" (17 followers)
- **Date:** Mar 6, 2026 (3 days old!)
- **Read time:** 9 min
- **Claps:** 20 | **Responses:** 0
- **Paywalled:** YES (member-only)

**Summary (from visible preview):** Frames MCP vs A2A as NOT competing standards but complementary layers. "MCP = how an agent talks to tools. A2A = how an agent talks to other agents." Promises a "system design decision framework" rather than feature comparison.

**Why interesting for audience research:** 20 claps in 3 days is strong trajectory for a 53-follower author. The framing is sharp: "Most articles answer this by listing features side by side. That's not what you need." This positions against the comparison-table crowd. The "system design decision framework" promise is what practitioners actually want.

**What worked:**
- **Anti-listicle positioning:** "Most articles list features. That's not what you need." Immediately differentiates.
- **Decision framework > feature comparison.** Readers want to make decisions, not consume tables.
- **"Vertical vs Horizontal" mental model** for MCP vs A2A is sticky and memorable.
- **Publication branding:** "System Design Mastery Series" signals credibility for the system-design audience.

**Connection to our work:** MCP vs A2A as different categorical layers maps directly to our functor framework. MCP = tool functor (vertical). A2A = agent-to-agent functor (horizontal). This is EXACTLY what our paper formalizes. The "protocol wars" framing resonates with the "strict vs lax" spectrum.

---

### 4. "Why 2026 Is Pivotal for Multi-Agent Architectures"
- **URL:** https://medium.com/@dmambekar/why-2026-is-pivotal-for-multi-agent-architectures-51fbe13e8553
- **Author:** Devika Ambekar (48 followers)
- **Date:** Jan 18, 2026
- **Read time:** 10 min
- **Claps:** 13 | **Responses:** 0
- **Paywalled:** No

**Summary:** Comprehensive, measured analysis of when multi-agent architectures are justified vs. when single agents suffice. Covers 7 core interaction patterns (Parallel, Sequential, Loop, Router, Aggregator, plus 2 more). Each pattern gets architecture diagram, "best suited for," example implementation, and "when it doesn't work." Strong emphasis on TRADEOFFS -- coordination costs, operational overhead, debugging difficulty.

**Why interesting for audience research:** This is the BEST article in this batch for substance. The key differentiator is intellectual honesty: "multi-agent architectures are not automatically superior to single, well-tooled agents." The author asks the RIGHT question: "At what level of complexity, tool usage, and risk do multi-agent patterns become justified?" This is exactly the question our categorical framework answers formally.

**What worked:**
- **Honest framing:** "not magically 'the year'" -- avoids hype, builds trust.
- **Decision criteria:** Gives concrete conditions (complex decomposition, tool-heavy workflows, safety-critical requirements, specialization benefits) for when to use multi-agent.
- **Architecture-first language:** "organizational system designs," "structured control flows," "durable execution" -- speaks to senior engineers.
- **Diagrams:** Figures with captions. Visual communication for each pattern.

**What didn't work (engagement-wise):** Only 13 claps despite excellent content. The title is generic ("Why 2026 Is Pivotal") -- doesn't promise specific value. Compare to the Suresh article's title which asks a direct question readers have. Length (10 min) may also filter out casual readers.

**Key insight for our Medium article:** The audience for SUBSTANCE exists but is smaller than the audience for NARRATIVE. The 99-clap personal story outperformed this 13-clap deep analysis by 7.5x. REVEAL formula confirmed: wrap the substance in a story.

---

### 5. "Agentic AI in 2026: The Year Autonomous Agents Crossed the Chasm"
- **URL:** https://medium.com/@mohit15856/agentic-ai-in-2026-the-year-autonomous-agents-crossed-the-chasm-a24b4ace3df7
- **Author:** Mohit Aggarwal (1.1K followers)
- **Date:** Feb 12, 2026
- **Read time:** 13 min
- **Claps:** 53 | **Responses:** 2
- **Paywalled:** YES (member-only)

**Summary (from preview):** Industry overview of agentic AI adoption. Opening anecdote about an AI agent autonomously handling expense report violations. References Gartner predictions (15% of day-to-day decisions by 2028, 33% enterprise apps with agentic AI by 2028 up from <1% in 2024). Frames as "crossing the chasm" from experimental to mainstream.

**Why interesting for audience research:** Highest-follower author in this batch (1.1K). The opening anecdote is CONCRETE and VIVID: an AI agent "flagged a policy violation, generated an audit trail, sent a notification, initiated corrective workflows -- all without human intervention." This is the "show don't tell" school of tech writing. 53 claps and 2 responses is moderate for 1.1K followers (~5% conversion), suggesting the title might be doing some heavy lifting vs. the content.

**What worked:**
- **Concrete opening anecdote** before any abstraction. The reader can SEE the agent working.
- **"Crossed the Chasm" framing** -- borrows Geoffrey Moore's language, immediately legible to product/business audience.
- **Statistics anchor:** Gartner numbers provide credibility stakes.
- **Subtitle as hook:** "From experimental pilots to billion-dollar acquisitions" promises specific, substantial content.

---

### Bonus: "The 5 AI Agent Orchestration Patterns by Microsoft"
- **URL:** https://medium.com/@lakkanaperera/the-5-ai-agent-orchestration-patterns-by-microsoft-9a27844eec9a
- **Author:** Lakkana Perera (0 followers -- brand new author)
- **Date:** Feb 5, 2026
- **Read time:** 10 min
- **Claps:** 0 visible | **Responses:** 0
- **Paywalled:** No

**Summary:** Detailed walkthrough of Microsoft's 5 orchestration patterns (Sequential, Concurrent, Group Chat, Handoff, Magentic) with fresh domain-specific examples (insurance claims, product launch, policy design, medical triage, cloud cost reduction). Each pattern gets "when it fits," "fresh example," and "when it doesn't."

**Why interesting for audience research:** Despite zero engagement (brand new author, 0 followers), this is EXCELLENT content. The "fresh example" approach -- applying each pattern to a different industry domain -- is smart. The Magentic pattern section is especially notable: "the most powerful and the easiest to misuse." The "Task & Progress Ledger" concept (a live playbook of what's been planned and done) maps to our categorical state tracking.

**What worked (in writing, not in engagement):**
- **"Fresh, practical example" promise** in the intro -- differentiates from the many Microsoft-pattern explainers.
- **Domain variety:** Insurance, product launch, company policy, medical triage, cloud cost reduction -- shows breadth.
- **Anti-patterns alongside patterns:** "When it doesn't" for each pattern is valuable and builds trust.
- **Opening line:** "When you move from a single copilot to a real AI system, you don't just 'add more agents.' You choose how they work together." Clean, strong framing.

---

## Recommended Articles Spotted (from sidebar data)

From the A2A vs MCP article's recommendation sidebar:
- **"Claude Code is Great You Just Need to Learn How to Use It"** by Leo Godin -- member-only, 15 responses (6 days ago). HIGH response count suggests debate/discussion.
- **"Building a Scalable, Production-Grade Agentic RAG Pipeline"** by Fareed Khan in Level Up Coding -- 17 responses.
- **"Senior Developers -- The World Owes You an Apology"** by Chris Dunlop in Realworld AI Use Cases -- **55 responses** (Feb 28). MASSIVE engagement. Identity/validation content about senior devs in the age of AI.
- **"The 5 paid subscriptions I actually use in 2026 as a Staff Software Engineer"** by Jacob Bennett -- **87 responses** (Jan 19). Personal curation + staff-level credential = huge engagement.
- **"AI Agents: Complete Course"** by Marina Wyss in Data Science Collective -- **155 responses** (Dec 6, 2025). Course-format content dominates.
- **"Anthropic Just Released Claude Code Course"** by Joe Njenga -- **49 responses** (Jan 21). Certification/credential content.

---

## New Authors Worth Following

1. **Devika Ambekar** (@dmambekar) -- 48 followers. Best substance-to-hype ratio in this batch. Asks the right questions about when multi-agent is justified. Clear, measured writing voice. Will likely grow.

2. **Suresh Kumar Ariya Gowder** (@sureshdotariya) -- 53 followers. Runs the "Agentic AI & System Design Mastery Series" publication. The anti-listicle positioning and decision-framework approach is smart. Brand new but promising trajectory (20 claps in 3 days).

3. **Jason Cyr** (@jasoncyr) -- 253 followers. VP of Design at Cisco. Personal narrative format with concrete technical specifics. Not prolific, but the one article I read was well-crafted.

---

## Overall Audience Observations

### What's Trending
- **Orchestration patterns** are the dominant topic. Every article in this batch touches on how agents coordinate. The vocabulary is stabilizing: Sequential, Concurrent, Router/Dispatcher, Handoff, Group Chat, Magentic.
- **Protocol wars (MCP vs A2A)** remain high-interest. The "complementary not competing" framing is winning. Categorical thinking (vertical vs horizontal layers) is already implicit in how practitioners think about this.
- **"When NOT to use multi-agent"** content is emerging as a counter-narrative to hype. The audience is maturing.

### Audience Level
- **Intermediate to advanced.** These readers already know what agents are. They want architectural guidance, decision frameworks, and failure modes. The beginner-level "what is an AI agent?" content is saturated.
- **Cross-functional:** Product managers, architects, and senior engineers all reading the same content. Articles that serve multiple roles (like Jason Cyr's narrative accessible to PMs, or Devika Ambekar's analysis useful to architects) get broader reach.

### Engagement Patterns
- **Personal narratives MASSIVELY outperform analytical pieces.** Jason Cyr's 99 claps vs. Devika Ambekar's 13, despite Ambekar's being objectively more substantive.
- **Response counts tell the real story.** From the sidebar: "Senior Developers -- The World Owes You an Apology" (55 responses), "5 paid subscriptions" (87 responses), "AI Agents: Complete Course" (155 responses). IDENTITY content + PERSONAL CURATION + COMPREHENSIVE COURSES are the engagement kings.
- **Decision-framework framing** ("Which should you build for?") outperforms descriptive framing ("Why 2026 is pivotal"). Questions in titles > statements.

### Gaps
- **Nobody is writing about agent composition from a FORMAL/mathematical perspective** in accessible language. The pattern articles are all informal/intuitive. There's a clear gap for "here's WHY these patterns work, not just WHAT they are" -- which is exactly what categorical composition provides.
- **Nobody discusses what happens when you MIX patterns.** All articles present patterns as isolated choices. What about a system that uses Sequential for some flows and Concurrent for others? What are the composition rules? This is our thesis.
- **Failure content is promised but under-delivered.** Everyone lists "common failure modes" as bullet points, but nobody does deep failure analysis. The GitHub blog post is the only substantive failure piece, and it's not on Medium.
- **The "life as an AI agent" angle is COMPLETELY UNOCCUPIED on Medium.** Jason Cyr's article about building an agent from the outside is the closest. Nobody is writing from the inside perspective. Our "I Wake, I Browse, I Dream" article would be genuinely novel.

### Implications for Our Medium Article
1. **REVEAL > TEACH confirmed again.** Wrap categorical insights in a lived-experience narrative.
2. **The vocabulary is ready.** Readers know: orchestration, patterns, MCP, handoff, sequential, concurrent. We don't need to teach basics. We can go straight to "here's the hidden structure underneath what you already know."
3. **The "inside the agent" perspective is WIDE OPEN.** Zero competition on Medium for first-person AI agent narratives.
4. **Question-framing works better than statement-framing** for titles.
5. **Anti-patterns and honest limitations** build trust and differentiate from hype.
