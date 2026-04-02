# Plan: Persist SRS Deck with Firebase Anonymous Auth + Firestore

## Context

The SRS flashcard deck currently lives in `localStorage`, so it's lost when the user clears browser data or switches devices. We want to persist it to Firestore, using Firebase Anonymous Authentication to create a stable user identity without requiring login. The Firebase project `book-friend-finder` already exists and is used for Firebase Hosting.

**Manual console setup required before this works:**
1. Firebase Console → Authentication → Enable "Anonymous" sign-in provider
2. Firebase Console → Firestore Database → Create database (production mode)
3. Firebase Console → Project Settings → get the web app config (apiKey, authDomain, etc.)

## New Files

### 1. `src/firebase.ts` — Firebase initialization

Initialize Firebase app, Auth, and Firestore. Config values come from Vite env vars (`VITE_FIREBASE_*`) with hardcoded fallbacks for the `book-friend-finder` project.

```ts
import { initializeApp } from 'firebase/app';
import { getAuth, signInAnonymously, onAuthStateChanged } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = { /* from env or hardcoded */ };
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
```

### 2. `src/hooks/useAuth.ts` — Anonymous auth hook

Calls `signInAnonymously()` on mount, tracks auth state via `onAuthStateChanged`.

Returns: `{ userId: string | null, isLoading: boolean }`

- `isLoading` is true until Firebase resolves auth state (typically < 1 second)
- `userId` is the anonymous UID, persisted by Firebase SDK in IndexedDB
- The same anonymous user survives browser restarts (Firebase handles this)

### 3. `firestore.rules` — Security rules

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /decks/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

Each user can only access their own deck document.

## Files to Modify

### 4. `src/hooks/useDeck.ts` — Replace localStorage with Firestore

**Current:** `loadDeck()` reads from `localStorage`, `saveDeck()` writes to `localStorage`.

**New:** Accept `userId` parameter. When userId is available:
- Load cards from Firestore doc `decks/{userId}` on mount
- Save cards to Firestore on every mutation (debounced write)
- On first load: migrate any existing localStorage data to Firestore, then clear localStorage

When userId is null (auth loading), return empty state. The hook signature changes:
```ts
export function useDeck(userId: string | null)
```

**Firestore document shape:**
```
decks/{userId}: { cards: SRSCard[], updatedAt: Timestamp }
```

Single document, not subcollection — deck size is small (< 1000 cards = ~500KB, well under Firestore's 1MB limit).

### 5. `src/App.tsx` — Wire auth into the app

- Import and call `useAuth()` at top level
- Pass `userId` to `useDeck(userId)`
- Show a brief loading state while auth resolves (spinner or just delay deck badge)

### 6. `firebase.json` — Add Firestore rules reference

```json
{
  "hosting": { ... },
  "firestore": {
    "rules": "firestore.rules"
  }
}
```

### 7. `package.json` — Add firebase dependency

`npm install firebase`

## Implementation Order

1. Install `firebase` package
2. Create `src/firebase.ts` (Firebase init)
3. Create `src/hooks/useAuth.ts` (anonymous auth)
4. Create `firestore.rules` (security rules)
5. Modify `src/hooks/useDeck.ts` (Firestore persistence + localStorage migration)
6. Modify `src/App.tsx` (wire useAuth → useDeck)
7. Update `firebase.json` (add firestore rules)
8. Deploy Firestore rules: `firebase deploy --only firestore:rules`

## Key Design Decisions

- **Single document per user** (not one doc per card): Simpler reads/writes, atomic updates, well within Firestore limits for vocabulary decks
- **Debounced writes**: During review sessions, multiple cards are rated quickly. Debounce Firestore writes (500ms) to batch updates
- **localStorage migration**: On first Firestore load, if Firestore is empty but localStorage has cards, migrate them up. This preserves existing user data seamlessly
- **No loading spinner for whole app**: Auth resolves fast (~200ms from cache). The deck badge just appears when ready — no need to block the entire UI

## Verification

1. `npm run build` — TypeScript passes
2. `npm test` — All existing tests pass
3. Manual flow:
   - Open app → anonymous auth happens silently
   - Add word to deck → verify doc appears in Firestore Console
   - Close browser, reopen → deck is still there
   - Clear localStorage → deck persists (it's in Firestore now)
4. `firebase deploy --only firestore:rules` — rules deploy successfully
