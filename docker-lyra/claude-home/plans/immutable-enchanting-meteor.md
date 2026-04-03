# Plan: Replace word frequency list with RNC (Russian National Corpus)

## Context

The current `russian-word-frequencies.json` is a 92,709-word Leeds/hingston web-corpus list. It's unlemmatized, contains web junk (proper nouns like "россия" at rank #114, single letters like "д" at #355), and ranks literary words incorrectly ("далекий" at #1794 instead of ~#311). Replacing it with the 20,003-lemma Russian National Corpus (Lyashevskaya & Sharoff) frequency dictionary gives properly lemmatized, academically validated rankings — already downloaded to `/tmp/rnc-frequency-list.json`.

## Changes

### 1. Replace the frequency data file
- **File**: `public/russian-word-frequencies.json`
- Convert the RNC data (currently `[["word", "pos"], ...]`) to a plain JSON array of strings `["и", "в", ...]` — same format as today
- Drops from 92,709 entries (1.8MB) to 20,003 entries (~400KB)

### 2. Update hardcoded max rank `92709` → `20003`
- **`src/components/SettingsPanel.tsx`**: `max={92709}` on two `<input>` elements (lines 133, 146)
- **`src/App.tsx`**: `max={92709}` on two `<input>` elements (lines 81, 93)

### 3. Update default frequency range
- **`src/App.tsx`** line 38: default `freqRangeMax: 1000` — consider whether 1000 is still a good default now that the list is 20K instead of 92K (it still is — the RNC top 1000 covers the same common vocabulary)

### 4. Update help text in SettingsPanel
- **`src/components/SettingsPanel.tsx`**: the help text currently says "92,709 words" — update to reflect ~20,000 lemmas

### 5. Update CLAUDE.md
- **`CLAUDE.md`**: references "92K Russian words" — update to ~20K

## Files to modify
1. `public/russian-word-frequencies.json` — replace data
2. `src/components/SettingsPanel.tsx` — max values + help text
3. `src/App.tsx` — max values
4. `CLAUDE.md` — word count reference

## No changes needed
- `TranscriptPanel.tsx` — uses the Map generically, no hardcoded sizes
- Unit tests (`tests/transcript-highlighting.test.tsx`) — use synthetic Maps, not real data
- E2E tests — all mock the file with `[]`
- Server code — never loads this file
- Demo system — no reference to this file

## Verification
1. `npm run build` — ensure no TypeScript errors
2. `npm run test` — all unit tests pass (frequency tests use synthetic data)
3. `npm run test:e2e` — all E2E tests pass
4. Manual: load app, enable frequency highlighting with range 500–1000, verify words are underlined in transcript
