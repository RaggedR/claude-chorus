---
name: CRDT Workspace Project for Imagineering
description: Local-first collaborative workspace with cards, links, filesystem, and compaction protocol — designed for the Imagineering meetup group
type: project
---

## Project: Local-First Imagineering Workspace

A collaborative knowledge workspace for the Imagineering group (10 people, Melbourne build & share meetup). Cards on a canvas, links between them, organized in a tree/filesystem. Syncs at meetups, works offline between them.

**Why:** The group has no shared persistent space for ideas, project connections, and meetup notes. The dashboard tracks velocity but not substance.

**How to apply:** This is Robin's new "software-engineery" project. It bridges his lattice theory background (Davey & Priestley school) with real distributed systems engineering.

## Key Design Decisions (from 2026-04-04 conversation)

### Data model
- Cards (create, edit, delete)
- Links between cards (create, delete)
- Tree/filesystem for organization (create collection, move card, move collection)
- Move operations are the mathematically interesting part (tree constraint, concurrent move = potential cycle)

### CRDT approach
- Operation lattice = lattice of ideals of the causal poset (always distributive, by Birkhoff)
- Observable state = rendering function from ideals to what the user sees (NOT a lattice homomorphism)
- No valid LATTICE congruences preserve observations (every join-irreducible collapse identifies visually-distinct states)
- But JOIN-SEMILATTICE congruences can work, and "partial observation" (knowing peer positions) enables compaction

### Compaction protocol
- Compaction = discarding operations everyone has seen
- Bottleneck = slowest/most absent peer
- System actively nudges slow peers: "sync up so we can compact"
- Maps to Imagineering social rhythm: sync at Tuesday meetups, email stragglers Wednesday morning
- Policy decision: how long to wait before removing an absent peer

### Lattice theory connections
- Operation poset → ideal lattice (Birkhoff) → always distributive
- Congruences of distributive lattice = 2^n (Boolean, indexed by join-irreducibles = operations)
- Observation restricts to filter ↑s, enabling congruences that the full lattice doesn't admit
- Undo ↔ relative complements (distributivity gives unique complements)
- Schema evolution ↔ Galois connections
- Composition ↔ universal algebra (Davey's field)
- Linear extensions of causal poset ↔ quasisymmetric functions (connects to Robin's RSK / partition combinatorics work)

### Stack (tentative)
- Automerge for CRDT layer (learn the library first, then consider improvements)
- Web frontend (canvas with draggable cards, SVG links)
- Sync server for cloud relay
- Peer discovery on local network for meetup sync

### Robin's background
- Studied lattice theory under Brian Davey at La Trobe (Davey & Priestley textbook)
- Deep knowledge of quotient lattices, ideals, congruences, distributivity, Galois connections
- Existing work in partition combinatorics, RSK, q-series (connects via linear extensions / QSym)
