# User Gallery Feature Plan

## Overview
Add a gallery feature where users can view their owned NFTs and browse other users' galleries.

## Scope
- Display all NFTs owned by a wallet (both minted and purchased)
- Allow viewing any user's gallery by wallet address
- No buying/selling functionality (existing marketplace handles that)

---

## Backend Changes

### 1. Track Token Ownership in Firestore

Currently, Firestore only stores the `wallet` field (creator). We need to track `currentOwner` to query owned tokens efficiently.

**File: `backend/src/services/firestore.js`**

Add functions:
```javascript
async function getTokensByOwner(ownerAddress, limit = 50)
async function updateTokenOwner(tokenId, newOwner)
```

Update `createToken()` to set `currentOwner` equal to `wallet` at mint time.

### 2. Update Ownership on Purchase

**File: `backend/src/routes/marketplace.js`**

After successful buy transaction, update Firestore:
```javascript
await firestoreService.updateTokenOwner(tokenId, buyerWallet);
```

### 3. New Gallery Route

**File: `backend/src/routes/gallery.js`** (new file)

```
GET /api/gallery/:address  - Get all tokens owned by address (public endpoint)
```

Response:
```json
{
  "owner": "0x...",
  "tokens": [
    {
      "tokenId": 1,
      "name": "Artwork Name",
      "description": "...",
      "previewUrl": "https://...",
      "licenseType": "display",
      "creator": "0x...",
      "mintedAt": "2024-01-15T..."
    }
  ]
}
```

### 4. Register Route

**File: `backend/src/index.js`**

Add public gallery route (no auth required for viewing).

---

## Flutter Changes

### 1. Update API Service

**File: `flutter/lib/services/api_service.dart`**

Add method:
```dart
Future<List<Token>> getGallery(String address)
```

### 2. Implement Gallery Page

**File: `flutter/lib/pages/gallery_page.dart`**

Currently a placeholder. Implement:
- Load tokens from `/api/gallery/{walletAddress}`
- Display in grid (same pattern as marketplace_page.dart)
- Show empty state if no tokens
- Pull-to-refresh support
- Tap token to navigate to `/token/{tokenId}`

### 3. Add Public Gallery Route

**File: `flutter/lib/router.dart`**

Add route for viewing other users' galleries:
```
/gallery/:address  - View any user's gallery
```

Keep existing `/gallery` for current user's gallery.

### 4. Gallery Navigation

Add "View Gallery" link on token detail page showing the owner's gallery.

---

## Files to Modify

| File | Changes |
|------|---------|
| `backend/src/services/firestore.js` | Add `getTokensByOwner()`, `updateTokenOwner()`, update `createToken()` |
| `backend/src/routes/marketplace.js` | Update ownership on buy |
| `backend/src/routes/gallery.js` | New file - gallery endpoint |
| `backend/src/index.js` | Register gallery route |
| `flutter/lib/services/api_service.dart` | Add `getGallery()` method |
| `flutter/lib/pages/gallery_page.dart` | Implement gallery UI |
| `flutter/lib/router.dart` | Add `/gallery/:address` route |
| `flutter/lib/pages/token_detail_page.dart` | Add "View Owner's Gallery" link |

---

## Verification

1. **Backend tests:**
   - Start dev server: `cd backend && npm run dev`
   - Mint a test token
   - Call `GET /api/gallery/{minterAddress}` - should return the token
   - Buy token with different wallet
   - Call `GET /api/gallery/{buyerAddress}` - should show token with new owner

2. **Flutter app:**
   - Run `cd flutter && flutter run -d chrome`
   - Connect wallet
   - Navigate to Gallery - should show owned tokens
   - Visit `/gallery/{otherAddress}` - should show that user's tokens
   - Empty wallet should show "No artworks yet" message
