# NFTmarket Dark & Premium UI Redesign

## Design Direction

**Style:** Dark & Premium - High-end gallery aesthetic with dark backgrounds, subtle gradients, and refined accents.

**Inspiration:** Luxury art galleries, premium crypto platforms (Foundation, SuperRare), high-end e-commerce

---

## Color Palette

### Primary Colors
```dart
// Background layers (darkest to lightest)
background:     #0D0D0F   // Near black
surface:        #141418   // Card backgrounds
surfaceLight:   #1C1C22   // Elevated surfaces

// Accent colors
accent:         #C9A962   // Gold - primary accent
accentLight:    #E5D4A1   // Light gold - highlights
primary:        #6366F1   // Indigo - interactive elements

// Text
textPrimary:    #FFFFFF   // White
textSecondary:  #9CA3AF   // Gray 400
textMuted:      #6B7280   // Gray 500

// Status colors (refined for dark bg)
success:        #34D399   // Emerald 400
warning:        #FBBF24   // Amber 400
error:          #F87171   // Red 400
info:           #60A5FA   // Blue 400

// License badges (darker, premium)
displayBlue:    #3B82F6   // Blue 500
commercialOrange: #F59E0B // Amber 500
transferPurple: #A855F7   // Purple 500
```

---

## Design System

### Cards
- **Background:** Subtle gradient from `#141418` to `#1A1A20`
- **Border:** 1px `rgba(255,255,255,0.06)`
- **Border radius:** 16px
- **Hover:** Slight elevation + border glow `rgba(201,169,98,0.2)`

### Typography
- **Headings:** White, bold weight
- **Body:** `#E5E7EB` (Gray 200)
- **Captions/metadata:** `#9CA3AF` (Gray 400)
- **Accent text:** Gold `#C9A962`

### Buttons
- **Primary:** Gradient indigo or solid with glow
- **Secondary:** Outlined with gold accent
- **Ghost:** Transparent with hover state

### Badges
- Semi-transparent backgrounds with colored borders
- Subtle glow effect

---

## Files to Modify

### 1. Theme (`flutter/lib/theme.dart`)
- Complete dark theme overhaul
- New color scheme with gold accent
- Card themes with gradients
- Typography refinements
- Input decoration themes

### 2. Gallery Page (`flutter/lib/pages/gallery_page.dart`)
- `_TokenCard` - premium card styling
- `_GalleryCard` - refined discovery cards
- Search bar styling
- Section headers with accent

### 3. Marketplace Page (`flutter/lib/pages/marketplace_page.dart`)
- `_ListingCard` - premium listing cards
- Price display with gold accent
- Empty state styling

### 4. Home Page (`flutter/lib/pages/home_page.dart`)
- Hero section with gradient
- Feature cards refinement
- Step cards premium styling

### 5. Wallet Button (`flutter/lib/widgets/wallet_button.dart`)
- Premium connected state
- Refined dropdown menu

### 6. Token Detail Page (`flutter/lib/pages/token_detail_page.dart`)
- Image showcase styling
- Metadata cards
- Action buttons

---

## Implementation Order

### Phase 1: Foundation
1. **theme.dart** - New dark color scheme, card themes, typography

### Phase 2: Core Pages
2. **gallery_page.dart** - Token cards, gallery cards
3. **marketplace_page.dart** - Listing cards

### Phase 3: Supporting Pages
4. **home_page.dart** - Hero, features
5. **wallet_button.dart** - Premium styling

### Phase 4: Polish
6. **token_detail_page.dart** - Detail view
7. Other pages as needed

---

## Key Visual Elements

### Token Card Design
```
┌─────────────────────────────────┐  ← 1px border rgba(255,255,255,0.06)
│  ┌─────────────────────────┐    │
│  │                         │    │  ← Image area
│  │        [IMAGE]          │    │
│  │                         │ ⬤  │  ← Badge (Original/License)
│  └─────────────────────────┘    │
│                                 │
│  Artwork Title                  │  ← White, semibold
│  ┌──────────────┐               │
│  │ Display      │               │  ← License badge (semi-transparent)
│  └──────────────┘               │
│  Creator: Alice                 │  ← Gray 400, small
│  Copyright: Alice               │
└─────────────────────────────────┘
   ↑ Gradient bg: #141418 → #1A1A20
```

### Listing Card (Marketplace)
```
┌─────────────────────────────────┐
│  ┌─────────────────────────┐    │
│  │                         │    │
│  │        [IMAGE]          │    │
│  │                         │ ⬤  │  ← License type badge
│  └─────────────────────────┘    │
│                                 │
│  Artwork Title                  │
│  ┌──────────┐                   │
│  │ 1.5 ETH  │  ← Gold accent    │  ← Price highlight
│  └──────────┘                   │
│  Seller: 0x3C44...93BC          │
└─────────────────────────────────┘
```

---

## Verification

1. Run Flutter app: `cd flutter && flutter run -d chrome`
2. Check Gallery page - cards should have dark gradient backgrounds
3. Check Marketplace page - pricing should have gold accent
4. Verify contrast and readability
5. Test hover states on web
6. Ensure images display correctly on dark backgrounds
