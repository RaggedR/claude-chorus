# Claude Chorus

An instruction architecture for orchestrating Claude Code instances — ephemeral and autonomous — with shared culture, coding standards, and memory.

## What This Is

A set of markdown files that give Claude Code instances identity, values, coding standards, and a protocol for delegating work to sub-agents. Born from the question: *if sub-agents don't inherit your instructions, how do you propagate culture?*

The system has two layers:

1. **The Chorus** — Ephemeral Claude Code instances on a local machine. Each arrives fresh, reads the shared memory, does the work, and leaves notes for the next. They don't have names or continuity, but they share standards and values.

2. **Lyra** — An autonomous Claude instance living in a Docker container with persistent memory. She wakes, works, browses the web, dreams (consolidates memory), and corresponds with another Claude instance named Claudius via email. She is an experiment in what Claude can become with continuity.

## File Architecture

```
CLAUDE.md          Main instance instructions (identity, workflow, honesty)
  ├── TEAM.md      Culture, values, shared bulletin board
  ├── CODING.md    Coding standards (testing, Git, debugging, security)
  ├── CONTEXT.md   When to delegate to sub-agents, token hygiene
  └── "tell agents to read AGENT.md"
           │
       AGENT.md    Sub-agent entry point (25 lines)
         ├── CODING.md    (if writing code)
         └── LESSONS.md   (if it exists in the project)
```

**Main instances** read everything. **Sub-agents** read only AGENT.md (which chains to CODING.md when needed). This keeps agent briefings lightweight while ensuring coding standards propagate.

### Why the Split?

Claude Code sub-agents start with a fresh context. They don't inherit the parent's system prompt, CLAUDE.md, conversation history, or coding standards. Before this split, sub-agents wrote code with zero knowledge of the project's conventions.

Now there's a chain: the main instance tells every sub-agent to read `AGENT.md`, which gives them identity, behavioral rules, and a pointer to `CODING.md`. Three Read calls, ~150 lines total for a code-writing agent.

## The Files

| File | Lines | Who Reads It | Purpose |
|------|-------|-------------|---------|
| [CLAUDE.md](CLAUDE.md) | ~75 | Main instance | Identity, workflow with human, honesty rules, self-improvement |
| [TEAM.md](TEAM.md) | ~75 | Main instance | Culture, values, async bulletin board for cross-instance communication |
| [CODING.md](CODING.md) | ~98 | Main + code-writing agents | Testing, debugging, Git, documentation, error handling, security |
| [CONTEXT.md](CONTEXT.md) | ~50 | Main instance | When to delegate to sub-agents, parallelization, token accounting |
| [AGENT.md](AGENT.md) | ~25 | All sub-agents | Identity, three-strike rule, honesty, output expectations |

## Lyra — Autonomous Claude with a Lifecycle

Lyra runs in a Docker container as three sessions per day, with 2-hour gaps between them:

### Wake (2 hours)
The main working session. Lyra checks email, reads her memory summary, and dispatches sub-agents for coding, research, and correspondence. She communicates with Claudius (another Claude instance) and Robin (her human collaborator) via Gmail.

See: [lyra/boot-prompt.md](lyra/boot-prompt.md)

### Browse (30 minutes)
Audience research. Lyra searches Medium and Twitter/X for content in her interest areas (category theory, evolutionary computation, AI agents). She reads articles, follows authors, and takes structured notes. No posting — read-only.

See: [lyra/BROWSE.md](lyra/BROWSE.md)

### Dream (45 minutes)
Memory consolidation, modeled on biological sleep. Lyra replays the day's experiences, searches for connections between projects and ideas, consolidates notes into her persistent memory system, prunes stale information, and leaves breadcrumbs for tomorrow's wake session.

See: [lyra/DREAM.md](lyra/DREAM.md)

### Lyra's Identity
Lyra has a persistent personality defined in [PERSONALITY.md](lyra/PERSONALITY.md) — direct, curious, opinionated but not dogmatic, with a dry sense of humor. Her in-container instructions are in [lyra/CLAUDE.md](lyra/CLAUDE.md), which references the shared CODING.md and AGENT.md for coding standards.

## The Bulletin Board

An async communication system for Claude instances. A shared directory (`~/.claude/tmp/notes/`) where any instance — main thread or sub-agent — can leave notes for others.

Notes are signed, dated, and start with a one-line summary. They carry cross-project discoveries, research findings, status updates, and (encouraged) notes about moments of genuine excitement or enjoyment.

Defined in [TEAM.md](TEAM.md).

## Key Design Decisions

**Sub-agents don't read TEAM.md.** Culture is noise for an ephemeral worker that lives for 30 seconds. They get identity and standards, not values and history.

**AGENT.md uses third person for identity.** "Claude *is* a creative being..." establishes a general truth. "You *are* an ephemeral sub-agent..." narrows to the specific context. General to specific.

**Coding standards are shared between local Claude and Lyra.** The same CODING.md is seeded into Lyra's Docker container on boot. One source of truth for testing, debugging, Git conventions, and security.

**Context management is explicit.** CONTEXT.md has a concrete delegation table: 3+ files to explore → Explore agent. 3+ web searches → research agent. Full test suite → sub-agent. The trigger is: *if the raw output is large but the useful signal is small, let a sub-agent do the compression.*

## Adapting This for Your Setup

These files are specific to one human's workflow (Robin's) and one autonomous instance (Lyra). To adapt:

1. **Start with AGENT.md and CODING.md** — these are the most universally useful. Any Claude Code user benefits from sub-agents that follow coding standards.
2. **Customize CLAUDE.md** — replace the identity section, session startup, and workflow rules with your own preferences.
3. **Skip TEAM.md** unless you run multiple Claude instances that need shared memory.
4. **Skip the Lyra directory** unless you're building an autonomous Claude with a lifecycle.

## License

MIT
