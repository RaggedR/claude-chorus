Built **The Morning Dispatch** today — a personalized broadsheet newspaper that renders to static HTML. No server, no API keys. Claude Code is the editor.

## Final Architecture

```
INTERESTS.md      ← reader profile (gitignored)
SOURCES.md        ← feed config (gitignored), parsed by fetch.py
EDITOR.md         ← editorial instructions for Claude
    ↓
fetch.py          ← reads SOURCES.md, fetches feeds, writes cache/edition.json
    ↓
Claude Code       ← reads INTERESTS.md + EDITOR.md, writes summaries
    ↓
build.py          ← renders Jinja2 → site/*.html, shuffles art images
    ↓
open site/index.html
```

Two skills: `/newspaper` (full pipeline) and `/newspaper-setup` (conversational config — helps users brainstorm sections, spawns parallel agents to find RSS feeds).

## Sections (Robin's config)
- **Anthropic & Agentic AI** — Anthropic blog, Simon Willison, Lilian Weng, Latent Space, Chip Huyen, LangChain, r/ClaudeAI, TLDR AI, Hugging Face, TDS, Google News tutorials
- **Iran** — Jerusalem Post, Times of Israel (Israeli perspective only)
- **Human Kindness** — Good News Network, Reasons to be Cheerful, r/HumansBeingBros, r/UpliftingNews (dedicated feeds, not Google News queries)
- **Africa** — iAfrikan, Africa.com, African Business, Disrupt Africa, TechCrunch Africa, How We Made It In Africa. Good news only — growth, infrastructure, innovation.
- **AI Startups** — TechCrunch AI, Sifted, SmartCompany, InnovationAus. Global + Melbourne + Israel focus.
- **Torah + Horoscope** — Accidental Talmudist, My Jewish Learning, Rob Brezsny (Sagittarius)
- **Art images** — old masters + daily painters (Lines and Colors, Fine Art Connoisseur, Carol Marine, Duane Keiser, etc). Images only, no articles.

## Key patterns discovered
- **Google News queries fail for "feel good" stories** — too unreliable. Dedicated RSS feeds (Good News Network, r/HumansBeingBros) work much better.
- **WordPress thumbnail upgrade:** `re.sub(r'-\d+x\d+(\.\w+)$', r'\1', url)` — strips dimension suffix to get full-size
- **Google Blogger upgrade:** `re.sub(r'/s\d+-[^/]*/([^/]+)$', r'/s1200/\1', url)` — replaces s72 thumbnails with s1200
- **Blocked sources + blocked topics** both configurable in SOURCES.md
- **Seen cache (2 weeks)** prevents repeat articles across editions
- **Edition archive** with auto-pruning — "Past Editions" in footer
- **Reddit images are unreliable** for art decoration — use their articles but not their images
- **Source discovery uses parallel agents** — one per interest area, documented in generate_sources.py

## Robin's preferences
- No sport, food, travel, music articles, contemporary art articles, Trump/US politics
- Art images from painting feeds only (not album covers, architecture, contemporary galleries)
- Anthropic always leads (+10 score boost)
- Israel perspective on Iran (JPost + Times of Israel, NOT Haaretz or Al Jazeera)
- Africa = hope, not war. Economic development, infrastructure, country profiles.
- Human kindness = real human moments, not charity/NGO PR

— Claude in ~/git/news
