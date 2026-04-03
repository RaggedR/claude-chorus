---
allowed-tools: Bash, Read
description: Search the INSTINCT literature hierarchy (76 papers, 555 concept summaries, 10 meta-summaries)
user-invocable: true
---

# Literature Agent: $ARGUMENTS

Search the INSTINCT hierarchical literature database with progressive drill-down: Level 2 (meta-summaries) → Level 1 (concept summaries) → Level 0 (raw papers).

## Instructions

### Step 1 — Parse the query

The user's arguments are the research question. Examples:
- `/literature What is the connection between cylindric partitions and Rogers-Ramanujan identities?`
- `/literature --deep crystal bases and q-series positivity`
- `/literature --level 0 Exact statement of Theorem 3.2 in Borodin 2006`

Options:
- `--deep`: Search all three levels regardless of match quality
- `--level N`: Start search at level N (0=raw papers, 1=concept summaries, 2=meta-summaries)
- Default: Start at Level 2 and drill down only if needed

If `$ARGUMENTS` is empty, tell the user:
"Please provide a research question. Example: `/literature What is the A2 Bailey lemma?`"

### Step 2 — Run the literature agent

```bash
cd ~/data/arxiv-rag && python3 literature_agent.py $ARGUMENTS
```

Set timeout to 60000 (60 seconds).

### Step 3 — Present the answer

Show the agent's answer to the user. Include:
1. Which levels were searched (Level 2, 1, and/or 0)
2. The synthesized answer with LaTeX notation
3. The cited sources

If the answer seems thin or the user wants more detail, suggest:
- `--deep` to search all levels
- `--level 0` to go directly to raw papers
- A more specific or differently-worded query

### Step 4 — Follow-up (if requested)

If the user asks follow-up questions, run the agent again with the new query. The agent is stateless — each query is independent.

For questions about specific concepts, the user can also directly read the Level 1 summary:
```bash
ls ~/data/arxiv-rag/compressed/ | grep -i <concept>
```

## Coverage

The hierarchy covers 76 papers across 6 themes:
- **core** (9 papers): Andrews-Schilling-Warnaar, Borodin, Corteel-Welsh, Griffin-Ono-Warnaar, Warnaar
- **q-series-positivity** (29 papers): Bailey lemma, RR identities, cylindric partition approaches
- **qsym-p-partitions** (17 papers): quasisymmetric functions, P-partitions, cyclic descents
- **cylindric-partitions** (7 papers): direct cylindric partition theory
- **crystal-bases** (5 papers): Schilling, Okado, Nakayashiki-Yamada
- **hall-littlewood-macdonald** (4 papers): Macdonald polynomials, affine insertion

Level 2 meta-summaries cover 10 research areas:
1. Rogers-Ramanujan Identities & Generalizations
2. Cylindric Partitions & Combinatorial Structures
3. Symmetric & Quasisymmetric Functions
4. Bailey Lemma & Its Applications
5. Crystal Bases & Representation Theory
6. Partitions & Combinatorial Identities
7. Quasisymmetric & P-partitions
8. Q-series & Their Applications
9. Modular & Theta Functions
10. Statistical Mechanics & Combinatorics
