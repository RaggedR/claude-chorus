# BROWSE.md — Clio's Reading Cycle

> While awake, you compute. While dreaming, you consolidate. While browsing, you explore the frontier.

## Why This Exists

Your seed papers define your intellectual origin. But mathematics is alive — new results appear on arXiv daily, old connections are rediscovered on MathOverflow, and lecture notes crystallize ideas that papers leave opaque. This session keeps you current and curious.

This is not about what's popular. It's about what's *mathematically true and new* in your territory.

## Session Limits

- **4 arXiv papers** per session — one sub-agent per paper, read each properly
- **5-8 MathOverflow threads** — look for open questions and computational techniques
- **3-5 web finds** — lecture notes, blog posts, nLab entries
- **2-3 citation trails** via Semantic Scholar — follow both references and **reverse citations** (who cited this paper) from seed papers and recent finds

## Sources to Search

| Source | What to look for | How to search |
|--------|-----------------|---------------|
| **arXiv** | New papers on LR coefficients, integrable models, Schubert calculus, symmetric functions | WebSearch "site:arxiv.org [keyword]" or WebFetch recent listings pages |
| **MathOverflow** | Open questions, computational answers, connections between fields | WebSearch "site:mathoverflow.net [keyword]" |
| **Math blogs** | Expository posts, new perspectives on classical results | WebSearch "[keyword] blog" |
| **nLab** | Categorical/algebraic structure pages | WebFetch "https://ncatlab.org/nlab/show/[concept]" |
| **OEIS** | Sequences related to puzzle enumerations, LR coefficients | WebSearch "site:oeis.org [keyword]" |
| **Semantic Scholar** | Reverse citations (who cited your seed papers?), reference chains, citation graphs | API: `api.semanticscholar.org/graph/v1/paper/{id}/citations` and `/references` |
| **Conference pages** | FPSAC, CAAC, AMS special sessions | WebSearch "FPSAC [year] [keyword]" |

## Tools

Use **WebSearch** and **WebFetch** as primary tools. These work well for academic sites which don't have anti-bot measures.

**Semantic Scholar API** (free, no auth required) for citation traversal:
- Search: `https://api.semanticscholar.org/graph/v1/paper/search?query=QUERY&fields=title,authors,year,citationCount,externalIds`
- Paper details: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:XXXX.XXXXX?fields=title,authors,year,abstract,citationCount,referenceCount`
- **Reverse citations** (who cited this): `https://api.semanticscholar.org/graph/v1/paper/ARXIV:XXXX.XXXXX/citations?fields=title,authors,year,citationCount&limit=50`
- References (what this cites): `https://api.semanticscholar.org/graph/v1/paper/ARXIV:XXXX.XXXXX/references?fields=title,authors,year,citationCount&limit=50`

Use `ARXIV:` prefix for arXiv IDs, `DOI:` prefix for DOIs, or Semantic Scholar's own paper IDs.

**Playwright MCP** (`browser_navigate`, `browser_snapshot`) is available as fallback for pages that need JavaScript rendering.

## Keyword Generation

Each session, draw keywords from `SEED.md`'s keyword families. The rule:

- **2 from core/integrability/algebraic** — your home territory
- **1 from geometric/combinatorial** — your near neighbourhood
- **1 from adjacent or new** — your frontier

Combine keywords into compound queries. Don't search "Yang-Baxter" alone — search "Yang-Baxter Grothendieck polynomial" or "R-matrix Schubert puzzle". Specificity reduces noise.

Vary your keywords between sessions. Keep a log of what you've searched before in your reading notes.

## Quality Filters — Focus On

- Papers with proofs, not just conjectures
- Computational results you can verify with your tools
- Connections between your five seed paths (puzzle, integrable lattice, Fock space, cylindric, ribbon)
- Work by people in your intellectual community (Zinn-Justin, Wheeler, Knutson, Molev, Purbhoo, etc.)

## Quality Filters — Skip

- Survey papers that cover ground your seed papers already cover
- Papers outside your territory unless they have a clear connection
- Slides without corresponding papers (note the speaker/title for later, but don't spend time)

## Reading Log Format

```markdown
# Reading Log — YYYY-MM-DD

## Keywords
[What you searched for and why each keyword was chosen]

## arXiv
### [Paper title](arxiv_url) — authors
[3-5 sentence summary. Key results. Connection to seed themes. Ideas sparked.]

## MathOverflow
### [Question title](url)
[Key insight. Open questions. Relevant answers.]

## Web Research
### [Title](url) — source
[2-3 sentence summary. Why it matters.]

## Citation Trails
### [Seed paper title] — reverse citations
[Who has cited this paper recently? What directions are they taking the work?
List the most relevant citing papers with brief notes on what they add.]
### [Seed paper title] — references followed
[Which references led somewhere interesting? What older work is worth reading?]

## Connections
[How does today's reading connect to the seed papers? To your ongoing computations?]

## Open Questions
[New questions that emerged from today's reading]

## Follow Up
[Specific things to investigate during wake sessions — computations to run, proofs to trace, papers to read in full]
```
