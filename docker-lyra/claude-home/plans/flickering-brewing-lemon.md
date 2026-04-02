# Plan: Public Landing Page

## Context

Stripe onboarding requires a publicly-visible (non-password-protected) website. Currently, the app immediately shows a login gate (`LoginScreen`) for unauthenticated visitors. We'll replace `LoginScreen` with a full marketing `LandingPage` that describes the product, shows features and pricing, and has a "Get Started" CTA that triggers Google Sign-In. Authenticated users skip straight to the app.

## Approach

Replace `LoginScreen` with a new `LandingPage` component at the same position in the auth gate render tree (App.tsx line 726). Same props interface (`onSignIn`, `error`). No React Router needed — the existing conditional rendering handles it.

## File Changes

### 1. Create `src/components/LandingPage.tsx` (NEW)

Full-width marketing page with these sections:

- **Hero**: App name, tagline, "Get Started" button (with Google icon SVG), auth error display
- **Features**: 2x2 responsive grid (1-col mobile, 2-col desktop) with inline SVG icons:
  1. Synced Transcripts — word-by-word highlighting synced to video playback
  2. Text Reading with TTS — AI-generated audio for lib.ru texts
  3. Click-to-Translate — instant word translation + sentence extraction
  4. SRS Flashcards — spaced repetition deck with keyboard shortcuts
- **Pricing**: $5/month, 30-day free trial (no card required), second "Get Started" CTA
- **Footer**: Legal agreement text with expandable ToS/Privacy (reuse `legal.ts` constants, keep existing `data-testid` IDs: `legal-agreement`, `login-tos-link`, `login-privacy-link`, `login-tos-content`, `login-privacy-content`)

Props: `{ onSignIn: () => void; error?: string | null }`
Primary CTA button: `data-testid="get-started-btn"`, text "Get Started" with Google icon

### 2. Edit `src/App.tsx` (2 lines)

- Change import: `LoginScreen` → `LandingPage`
- Change render at line 728: `<LoginScreen ...>` → `<LandingPage ...>`

### 3. Delete `src/components/LoginScreen.tsx`

Fully replaced by LandingPage — no other imports.

### 4. Tests (TDD — write before component)

**Replace `tests/login-screen.test.tsx` → `tests/landing-page.test.tsx`**
- Renders app title ("Russian Video & Text")
- Renders feature sections (synced transcripts, TTS, translate, flashcards)
- Renders pricing ("$5" and "30-day free trial")
- Renders "Get Started" button with `data-testid="get-started-btn"`
- Clicking "Get Started" calls `onSignIn`
- No error shown when `error` is null/undefined
- Shows error message when `error` prop is set
- Renders Google logo SVG
- Legal links expand/collapse ToS and Privacy Policy

**Update `tests/app.test.tsx`**
- Mock `../src/components/LandingPage` instead of `LoginScreen`
- Update test IDs: `login-screen` → `landing-page`, `sign-in-btn` → `get-started-btn`
- Update test descriptions accordingly

**Update `e2e/tests/settings-features.spec.ts`**
- Line 174: `text=Sign in with Google` → `getByTestId('get-started-btn')`
- Lines 82-113: Update describe block title to "Legal agreement on landing page" (test IDs stay the same)

**Update `e2e/tests/subscription.spec.ts`**
- Line 82: `text=Sign in with Google` → `getByTestId('get-started-btn')`

### 5. Update `CLAUDE.md`

Add `LandingPage.tsx` to frontend component documentation.

## Verification

1. `npm test` — all vitest tests pass (frontend + server)
2. `npm run test:e2e` — all Playwright E2E tests pass
3. `npm run build` — TypeScript check + production build succeeds
4. Manual: visit localhost:5173 unauthenticated → see landing page with features/pricing
5. Manual: click "Get Started" → Google Sign-In flow → lands in app
6. Manual: refresh while authenticated → skips landing page, goes to app
