# Plan: GPT-4o-mini Example Sentences for Flashcards

## Context

The batch dictionary enrichment (PR in progress on `feat/enrich-deck`) gave flashcards grammar tables, stress marks, and POS badges. But `RichCardBack.tsx` has an "Example" section (lines 261-268) that renders `entry.example.russian` + `entry.example.english` — and this field is **always empty** because OpenRussian TSVs don't include example sentences. The user wants every card to show a real example sentence alongside the transcript context.

## Approach

Add a `POST /api/generate-examples` endpoint that uses a single GPT-4o-mini call to generate A2-B1 level example sentences for a batch of Russian words. Chain this as a second enrichment pass in `useDeck.ts`, after dictionary enrichment. One-time per card — once `dictionary.example` is populated and saved to Firestore, it's never regenerated.

## Files to Modify

| File | Action |
|------|--------|
| `server/index.js` | Add `POST /api/generate-examples` endpoint |
| `server/integration.test.js` | Add tests for the new endpoint |
| `src/hooks/useDeck.ts` | Add second enrichment pass for example sentences |
| `tests/use-deck.test.tsx` | Add tests for example enrichment flow |
| `e2e/fixtures/mock-routes.ts` | Add mock route for `/api/generate-examples` |
| `CLAUDE.md` | Add endpoint to API table |
| `CLAUDE_DOCS/openrussian-dictionary.md` | Document example generation |

## Step-by-step

### Step 1: Server endpoint (TDD)

**Tests first** in `server/integration.test.js`:
- Returns example sentences keyed by word
- Handles GPT response correctly (JSON mode)
- Validates input (requires `words` array, max 50 items)
- Requires `requireAuth + requireSubscription + requireBudget` (costs money)
- Tracks cost via `costs.gpt4oMini()`

**Then implement** in `server/index.js`:

```javascript
// POST /api/generate-examples — GPT-4o-mini batch example sentence generation
// Accepts: { words: [string] }   (max 50)
// Returns: { examples: { [word]: { russian: string, english: string } | null } }
app.post('/api/generate-examples', requireSubscription, requireBudget, async (req, res) => {
  const { words } = req.body;
  // validate: array, max 50, strings...

  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini',
      messages: [{ role: 'system', content: SYSTEM_PROMPT }, { role: 'user', content: words.join('\n') }],
      response_format: { type: 'json_object' },
      temperature: 0.7,
    }),
  });

  // Parse, track cost, return examples
  trackCost(req.uid, costs.gpt4oMini());
  res.json({ examples });
});
```

**GPT system prompt**: "For each Russian word, generate one simple example sentence (A2-B1 level, 5-12 words). Return JSON object mapping each word to `{ russian, english }`. Use the word in its natural inflected form."

Middleware chain: `requireAuth` (via earlier `app.use`), `requireSubscription`, `requireBudget` — this calls an external API so it costs budget.

**Pattern**: Follows the exact same structure as `POST /api/extract-sentence` (lines 828-862 in `server/index.js`) — direct `fetch` to OpenAI, JSON mode, `costs.gpt4oMini()`.

### Step 2: Frontend — second enrichment pass in `useDeck.ts`

Refactor the current `enrichMissingDictionary` to return the enriched cards, then chain a new `enrichMissingExamples`:

```typescript
async function enrichMissingExamples(loadedCards: SRSCard[]) {
  // Cards that have dictionary data but no example sentence
  const needsExamples = loadedCards.filter(c => c.dictionary && !c.dictionary.example);
  if (needsExamples.length === 0) return;

  const words = needsExamples.map(c => c.word);
  const { examples } = await apiRequest<{ examples: Record<string, { russian: string; english: string } | null> }>(
    '/api/generate-examples',
    { method: 'POST', body: JSON.stringify({ words }) },
  );
  if (cancelled) return;

  const enriched = loadedCards.map(c => {
    if (c.dictionary && !c.dictionary.example && examples[c.word]) {
      return { ...c, dictionary: { ...c.dictionary, example: examples[c.word]! } };
    }
    return c;
  });
  setCards(enriched);
  saveToFirestore(enriched);
}
```

Call order in `load()`:
1. `enrichMissingDictionary(loadedCards)` — free, in-memory
2. `enrichMissingExamples(latestCards)` — costs budget, GPT-4o-mini

Both are fire-and-forget with silent error handling (best-effort).

**Important**: `RichCardBack.tsx` needs **zero changes** — it already renders `entry.example` (lines 261-268).

### Step 3: E2E mock + docs

- `e2e/fixtures/mock-routes.ts` — add route for `/api/generate-examples` returning empty `{ examples: {} }`
- `CLAUDE.md` — add endpoint to API table
- `CLAUDE_DOCS/openrussian-dictionary.md` — document example generation flow

## Verification

1. `cd server && npx vitest run integration.test.js` — new endpoint tests pass
2. `npx vitest run tests/use-deck.test.tsx` — example enrichment tests pass
3. `npm test` — all tests pass
4. `npm run test:e2e` — E2E tests still pass
5. `npm run dev` — flashcards now show GPT-generated example sentences in the blue "Example" box
