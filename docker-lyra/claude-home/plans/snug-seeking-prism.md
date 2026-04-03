# Plan: Code-split the 1.2MB single-chunk bundle

## Context

The app ships a single 1,237KB JS bundle (384KB gzipped). The browser must download, parse, and execute ALL of it before React mounts and Firebase Auth can even check if the user is logged in. This makes the app feel slow compared to sites that code-split. The three heaviest deps — Firebase Auth (~150KB gz), Firebase Firestore (~200KB gz), and hls.js+@vimeo/player (~90KB gz) — are all statically imported even though Firestore and the video player are only needed later.

**Goal:** Split the bundle so the initial load is ~300KB gz (down from 384KB), with Firestore and player libs loaded lazily.

---

## Step 1: `manualChunks` in vite.config.ts

Add `build.rollupOptions.output.manualChunks` to split vendor deps into cacheable parallel chunks:

```js
manualChunks: {
  'firebase-auth': ['firebase/app', 'firebase/auth'],
  'firebase-firestore': ['firebase/firestore'],
  'react-vendor': ['react', 'react-dom'],
  'sentry': ['@sentry/react'],
}
```

This alone doesn't defer anything, but it enables parallel downloads and better browser caching. Sentry stays eager (ErrorBoundary wraps the app in main.tsx).

**File:** `vite.config.ts`

---

## Step 2: Split `firebase.ts` to defer Firestore

Currently `firebase.ts` imports BOTH `firebase/auth` and `firebase/firestore`. Since `useAuth.ts` and `api.ts` import `auth` from it, Firestore (~200KB gz) gets pulled into the initial bundle even though it's only used by `useDeck.ts`.

**Create two new files:**

- `src/firebase-auth.ts` — exports `app` and `auth` (eager, needed at boot)
- `src/firebase-db.ts` — exports `db` (lazy, imported dynamically)

**Update imports:**
- `src/hooks/useAuth.ts` — import from `../firebase-auth`
- `src/services/api.ts` — import from `../firebase-auth`
- `src/firebase.ts` — becomes a re-export barrel (backwards compat for tests)

**Files:** `src/firebase-auth.ts` (new), `src/firebase-db.ts` (new), `src/firebase.ts`, `src/hooks/useAuth.ts`, `src/services/api.ts`

---

## Step 3: Dynamic Firestore import in `useDeck.ts`

The static `import { doc, getDoc, setDoc, serverTimestamp } from 'firebase/firestore'` at line 2 of `useDeck.ts` is what forces Firestore into the main bundle. Convert to dynamic imports:

```ts
async function getFirestore() {
  const [firestoreModule, { db }] = await Promise.all([
    import('firebase/firestore'),
    import('../firebase-db'),
  ]);
  return { ...firestoreModule, db };
}
```

All Firestore call sites in `useDeck.ts` are already inside async functions or `setTimeout` callbacks, so this is straightforward. The `Sentry` import stays static (it's in the eager sentry chunk).

**File:** `src/hooks/useDeck.ts`

---

## Step 4: React.lazy() for conditional components

All components use named exports, so we need the `.then(m => ({ default: m.X }))` wrapper.

**Lazy-load these (all conditionally rendered):**
- `LandingPage` — only shown when `!userId`
- `PaywallScreen` — only shown when `needsPayment`
- `SettingsPanel` — modal, only shown when `isSettingsOpen`
- `ReviewPanel` — modal, only shown when `isReviewOpen`
- `VideoPlayer` — only in player view (also defers hls.js + @vimeo/player ~90KB gz)
- `AudioPlayer` — only in player view
- `TranscriptPanel` — only in player view

**Keep eager (always visible or tiny):**
- `VideoInput`, `TextInput`, `ChunkMenu`, `ProgressBar`, `DeckBadge`

**Suspense fallbacks:**
- Full-page gates (Landing, Paywall) → same spinner already used for auth/sub loading
- Modals → `fallback={null}` (imperceptible delay)
- Player view → inline spinner in content area

Extract an inline `LoadingSpinner` component from the existing duplicated spinner JSX.

**File:** `src/App.tsx`

---

## Expected result

| Chunk | When loaded | Est. size (gz) |
|-------|-------------|----------------|
| react-vendor | Immediately | ~45KB |
| firebase-auth | Immediately | ~150KB |
| sentry | Immediately | ~80KB |
| app (index) | Immediately | ~30KB |
| firebase-firestore | After auth (useDeck) | ~200KB |
| player components + hls.js + vimeo | On player view | ~90KB |
| landing/paywall/modals | On demand | ~15KB |

**Initial load: ~305KB gz** (down from 384KB). Firestore and player libs load in the background after auth resolves.

---

## Verification

1. `npm run build` — check chunk output, confirm multiple chunks created
2. `npm test` — all frontend + server tests pass
3. `npm run dev` — manual test: login flow should feel faster on refresh
4. Browser DevTools Network tab — confirm Firestore chunk loads lazily after auth, not at boot
