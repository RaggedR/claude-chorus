# NFT Licensing Marketplace - Implementation Plan

## Overview
Extend the existing NFT licensing contract with marketplace functionality and build a frontend.

## Requirements Summary
- **Minting**: Image upload + title (title included in watermark)
- **Gallery**: Display owned NFTs with asking price
- **Offers**: Buyers make offers with MATIC locked in escrow
- **Negotiation**: Sellers accept/reject offers
- **License Types**: Three types (Copyright, Commercial, Display) - can only sell what you own

## Part 1: Smart Contract Updates

### New Marketplace Features

```solidity
struct Listing {
    uint256 askingPrice;    // in wei
    bool isActive;
}

struct Offer {
    address offerer;
    uint256 amount;         // locked in contract
    bool isActive;
}

// Mappings
mapping(uint256 => Listing) public listings;           // tokenId => Listing
mapping(uint256 => Offer[]) public offers;             // tokenId => Offers
mapping(address => uint256) public pendingWithdrawals; // refunds
```

### New Functions
1. **listForSale(tokenId, askingPrice)** - List NFT with asking price
2. **cancelListing(tokenId)** - Remove listing
3. **makeOffer(tokenId)** - Make offer (payable, locks MATIC)
4. **acceptOffer(tokenId, offerIndex)** - Accept offer, transfer NFT, release funds
5. **rejectOffer(tokenId, offerIndex)** - Reject, refund buyer
6. **withdrawOffer(tokenId, offerIndex)** - Buyer withdraws their offer
7. **getListings()** - View all active listings
8. **getOffers(tokenId)** - View offers on a token
9. **getOwnedTokens(address)** - Get tokens owned by address

### Update Watermark Structure
```solidity
struct Artwork {
    address originalMinter;      // Wallet address watermark
    string title;                // Title watermark (NEW)
    uint88 commercialCount;
    uint88 displayCount;
    bool copyrightTransferred;
    string metadataURI;
}
```

## Part 2: Frontend (Next.js + wagmi)

### Tech Stack
- **Next.js 14** (App Router)
- **wagmi v2 + viem** - Wallet connection & contract interaction
- **RainbowKit** - Wallet UI
- **Tailwind CSS** - Styling
- **Pinata/IPFS** - Image storage

### Pages
1. **/** - Homepage / Browse all listings
2. **/gallery** - Your owned NFTs (with list/unlist)
3. **/mint** - Create new artwork
4. **/token/[id]** - Token detail, make offers
5. **/offers** - Manage incoming/outgoing offers

### Key Components
- `WalletConnect` - Connect wallet button
- `NFTCard` - Display NFT with image, title, watermark, price
- `ListingForm` - Set asking price
- `OfferForm` - Make an offer
- `OffersList` - Show offers with accept/reject buttons

## File Structure

```
nft-licensing-contract/
├── src/
│   └── NFTLicensingSystem.sol  # Updated with marketplace
├── frontend/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx            # Browse listings
│   │   ├── gallery/page.tsx    # Your NFTs
│   │   ├── mint/page.tsx       # Mint new
│   │   ├── token/[id]/page.tsx # Token detail
│   │   └── offers/page.tsx     # Manage offers
│   ├── components/
│   │   ├── NFTCard.tsx
│   │   ├── ListingForm.tsx
│   │   ├── OfferForm.tsx
│   │   └── WalletProvider.tsx
│   ├── lib/
│   │   ├── contracts.ts        # ABI + addresses
│   │   └── ipfs.ts             # Pinata upload
│   └── package.json
```

## Implementation Order

1. **Update smart contract** with marketplace logic
2. **Add enumeration** (track all tokens, listings)
3. **Write marketplace tests**
4. **Deploy to Polygon Amoy** (testnet)
5. **Create Next.js app** with wallet connection
6. **Build mint page** with IPFS upload
7. **Build gallery page** with listing functionality
8. **Build browse page** with offer functionality
9. **Build offers management page**

## Verification

1. `forge test` - All contract tests pass
2. Deploy to Amoy testnet
3. Test full flow in browser:
   - Connect wallet
   - Mint artwork (upload image + title)
   - List for sale
   - Different wallet makes offer
   - Accept offer, verify transfer
   - Check watermark persists
