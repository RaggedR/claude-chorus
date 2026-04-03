# Plan: Generate Example Sentences at Card Creation Time

## Context

Flashcard example sentences (GPT-4o-mini) are the ONLY card data not set at creation time. They rely on a background enrichment pipeline (`enrichMissingExamples` in useDeck.ts) that silently fails when subscription, budget, or network issues occur — causing the "sometimes works, sometimes doesn't" behavior.

Meanwhile, the user no longer wants the "From transcript" context sentence (already removed from UI). The `/api/extract-sentence` call that generates it is now wasted work.

**Fix:** Replace the `extract-sentence` GPT call with a `generate-examples` GPT call in `handleAddToDeck`. Same cost, same latency, but the card is born complete.

## Changes

### 1. WordPopup.tsx — Replace extract-sentence with generate-examples
- `handleAddToDeck`: Call `/api/generate-examples` with `{ words: [translation.word] }` instead of `/api/extract-sentence`
- Merge the generated example into `translation.dictionary` before passing to `onAddToDeck`
- Remove `context` prop from interface and destructuring
- Simplify `onAddToDeck` callback signature: drop `context`, `contextTranslation` params → `(word, translation, sourceLanguage, dictionary?)`
- On failure: still add card without example (graceful degradation)

### 2. TranscriptPanel.tsx — Remove context state
- Remove `selectedContext` state and `setSelectedContext`
- Remove the 30-word context window computation in `handleWordClick` (lines 115-130)
- Remove `context={selectedContext}` from `<WordPopup>` props

### 3. sm2.ts — Simplify createCard
- Remove `context` and `contextTranslation` parameters from `createCard()`
- New signature: `createCard(word, translation, sourceLanguage, dictionary?)`

### 4. useDeck.ts — Simplify addCard
- Update `addCard` callback to match new 4-param signature
- Keep `enrichMissingExamples` as fallback for old cards

### 5. ReviewPanel.tsx — Clean up dead code
- Remove `russianSentence`/`englishSentence` from `getCardSides()` (no longer rendered)

### 6. types/index.ts
- Remove `context`/`contextTranslation` from `DictionaryEntry` (never populated server-side)
- Keep `context`/`contextTranslation` on `SRSCard` for backward compat with existing Firestore data

### 7. Tests — Update to match new API call

**Unit tests:**
- `tests/word-popup.test.tsx`: Rewrite 3 extract-sentence tests → test generate-examples call, failure fallback
- `tests/sm2.test.ts`: Update createCard tests (remove context params)
- `tests/use-deck.test.tsx`: Update addCard call signatures

**E2E tests:**
- `e2e/fixtures/mock-routes.ts`: Update `generate-examples` mock to return example data; remove `extract-sentence` mock
- `e2e/fixtures/mock-data.ts`: Replace `MOCK_SENTENCE` with `MOCK_EXAMPLE`
- `e2e/tests/add-to-deck.spec.ts`: Verify generate-examples instead of extract-sentence
- `e2e/tests/api-interactions.spec.ts`: Same
- `e2e/tests/demo-flow.spec.ts`: Update mock
- `e2e/tests/text-flow.spec.ts`: Update mock

### No backend changes needed
`/api/generate-examples` already handles batches of 1. `/api/extract-sentence` remains available (not deleted).

## Verification
1. `npm test` — all vitest (frontend + server)
2. `npm run test:e2e` — all Playwright E2E tests
3. `npm run build` — TypeScript check + production build
