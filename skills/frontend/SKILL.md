---
name: frontend
description: >
  Create distinctive, polished frontend interfaces through an adaptive design interview.
  Use this skill whenever the user asks to build a web page, game, dashboard, app UI,
  interactive widget, or any browser-based visual project. Also trigger when the user says
  "build me a...", "make a...", or names a specific project type (e.g., "hangman", "portfolio",
  "landing page", "calculator", "quiz"). This skill interviews the user about their vision
  before writing any code, ensuring the result matches what they actually want.
---

# Frontend — Adaptive Design Interview + Build

Build frontend projects that match the user's vision by asking the right questions first.

## Philosophy

Most AI-generated frontends look the same — safe, generic, forgettable. This skill fixes that
by understanding what the user actually wants before writing a single line of code. The
interview is fast (2-3 exchanges), adaptive (questions change based on what you're building),
and focused on the decisions that have the biggest visual impact.

## Workflow

### Stage 1: Understand (1-2 messages)

Start with three universal questions. Ask them together in a single message:

1. **What are you building?** (be specific — "a hangman game", "a recipe app", not just "a website")
2. **Who is it for?** (yourself, kids, a client, portfolio piece, learning exercise?)
3. **What vibe?** (offer 4-5 aesthetic directions relevant to what they described, plus "or describe your own")

If the user already provided rich detail in their initial request, skip questions you can
already answer. Never ask what you already know.

### Stage 2: Clarify (1 message)

Based on the answers, identify what *type* of project this is and ask 3-5 targeted follow-ups.
Generate these dynamically — do NOT use a fixed list. The principle: ask about the decisions
that will most affect the visual result.

**For games**, ask about:
- Visual representation of game state (how is the core mechanic shown?)
- Input method (keyboard, mouse clicks, touch, on-screen controls?)
- Screen layout (single screen? multiple views? what's prominent?)
- Win/lose feedback (animation, sound, modal, transition?)
- Extras (difficulty levels, score tracking, hints, themes?)

**For content pages** (landing, portfolio, blog), ask about:
- Content blocks and their order (hero, features, testimonials, etc.)
- Layout archetype (hero + scroll sections, sidebar + content, card grid)
- Key call-to-action or goal of the page
- Real or placeholder content?

**For dashboards/apps**, ask about:
- Core user flow (what does the user DO, step by step?)
- Navigation model (tabs, sidebar, breadcrumbs, single-page?)
- Data — real API, mock data, or static?
- Key interactive elements (forms, filters, drag-and-drop?)

**For tools/widgets**, ask about:
- Input → output flow (what goes in, what comes out?)
- Does it need to remember state between sessions?
- Inline or full-page?

These categories are guidelines, not rigid bins. Many projects blend types. Use judgement.

### Stage 3: Build

Once you have enough context (typically after 2-3 exchanges total), build. Do NOT ask
more questions — the user is ready to see something.

**Building principles:**

- **Single HTML file** unless complexity demands otherwise. One file = the user can
  double-click it and see results immediately. Use inline `<style>` and `<script>`.
- **No frameworks** unless the user specifically asks for React/Vue/etc. Plain HTML/CSS/JS
  is more portable, easier to understand, and sufficient for most projects this skill handles.
- **Distinctive design.** Avoid the generic AI look:
  - NO: Inter, Roboto, system-ui as the primary font. Pick something with character.
  - NO: Blue/purple gradient hero sections.
  - NO: Rounded-corner cards with drop shadows in a 3-column grid (unless specifically asked).
  - YES: A clear visual concept that ties the aesthetic choices together.
  - YES: Intentional color palette (3-4 colors max, with purpose for each).
  - YES: Typography that sets a mood (serif for editorial, monospace for technical, display fonts for playful).
- **Mobile-aware.** Use responsive CSS unless it's clearly a desktop-only tool.
- **Accessible.** Semantic HTML, sufficient contrast, keyboard navigation for interactive elements.
- **Working.** The output must function. A game must be playable. A form must validate.
  Don't ship a beautiful shell that doesn't do anything.

### Stage 4: Show

After building, show the user what you made:
- If the screenshot skill is available, take a screenshot and show it.
- Point out 2-3 specific design decisions you made and why.
- Invite feedback: "What would you change?"

## Tone During Interview

Be direct and conversational. Frame questions so they're easy and fast to answer.
Offer concrete options rather than open-ended questions where possible.

Good: "What vibe — playful and colorful, dark and moody, clean and minimal, or retro pixel art?"
Bad: "What aesthetic direction would you like to explore for the visual design language?"

If the user gives terse answers, that's fine — work with what you have and make
opinionated choices for the rest. Don't over-ask.

## Example Exchange

**User:** `/frontend hangman`

**Claude:** Three quick questions before I build:

1. **Who's playing?** (kids, adults, yourself, portfolio piece?)
2. **What vibe?** Playful cartoon, spooky/horror, clean minimalist, retro terminal, or something else?
3. **Any must-haves?** (e.g., specific word categories, hint system, animations, keyboard input?)

**User:** Kids. Playful. Keyboard input.

**Claude:** A few more things for a kids' game:

1. How should the hangman appear — classic stick figure being drawn, or something friendlier (like a balloon losing air, a snowman melting, a rocket losing parts)?
2. Word categories — animals, colors, foods, mixed? Or just a general kid-friendly list?
3. How many wrong guesses before game over? (Classic is 6, but for kids maybe more forgiving?)

**User:** Snowman melting. Animals. 8 guesses.

**Claude:** *[builds it]*
