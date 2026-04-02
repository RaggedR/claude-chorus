# Plan: Progressive Subgraph Exploration for Knowledge Graph (Accepted)

## Context

The graph currently shows all nodes and links at once, and clicking any node immediately navigates away. The user wants an **exploration mode**: click a node to reveal its neighborhood, click another to grow the visible subgraph, and only navigate on a second click of the same node. The force simulation must only act on visible nodes (hidden nodes shouldn't pull visible ones). Edges are also too faint against the black background.

## Approach: Single ForceGraph2D with fx/fy Pinning

All nodes stay in the ForceGraph2D instance. Background (non-visible) nodes are pinned at deterministic positions via `fx`/`fy` (standard d3-force pinning). Visible nodes have `fx`/`fy` cleared so they participate in the force simulation. Only links between visible nodes are included. This gives us a single canvas, single coordinate space, and native click handling — no dual-canvas complexity.

## State Model

| State | Type | Purpose |
|-------|------|---------|
| `expandedNodes` | `Set<string>` | Nodes the user has clicked to reveal |
| `adjacencyMap` | `Map<string, Set<string>>` (memo) | Pre-computed neighbor lookup |
| `visibleNodeIds` | `Set<string>` (memo) | expandedNodes + all their neighbors |
| `backgroundPositions` | `Map<string, {x,y}>` (memo) | Deterministic scatter layout for pinned nodes |

Removes: `selectedNodeId`, `neighborSet`

## Click Behavior

| Scenario | Action |
|----------|--------|
| Click a **non-expanded** node (background or revealed neighbor) | Add to `expandedNodes` → reveals its neighborhood |
| Click an **already-expanded** node | `router.push(entityPath(...))` → navigate to detail page |
| Click **background** (empty space) | Clear `expandedNodes` → reset to initial state |

## Visual States (paintNode)

| State | Alpha | Radius | Border | Label |
|-------|-------|--------|--------|-------|
| **Initial** (nothing expanded) | 0.4 | normal | faint | at zoom > 0.8 |
| **Expanded** | 1.0 | 1.3x | thick white + glow ring | at zoom > 0.5 |
| **Revealed neighbor** | 1.0 | normal | subtle white | at zoom > 0.6 |
| **Background** (during exploration) | 0.06 | 0.6x | none | never |

## Edge Visibility Fix

- `linkWidth`: `0.5` → `1.5`–`2` (callback: thicker for links touching expanded nodes)
- `linkColor`: `rgba(255,255,255,0.15)` → `rgba(255,255,255,0.55)` for expanded-node links, `0.25` for neighbor-to-neighbor

## Files to Modify

1. **`components/GraphView.tsx`** — Full rework of state, memos, click handlers, rendering callbacks, ForceGraph2D props (~310 lines, most lines change)
2. **`app/graph/page.tsx`** — Update instruction text: "Click a node to explore connections. Click again to view details."

No API, query, or type changes needed.

## Implementation Steps

1. Add `adjacencyMap` memo (pre-computed from `graphData.links`)
2. Replace `selectedNodeId` with `expandedNodes` state
3. Add `backgroundPositions` memo (golden-angle spiral scatter)
4. Add `visibleNodeIds` memo (expanded + their neighbors)
5. Rewrite `filteredGraphData` → `simulationGraphData` memo (fx/fy pinning, link filtering, type filtering)
6. Rewrite `handleNodeClick` (expand-or-navigate logic)
7. Update `handleBackgroundClick` (clear expandedNodes)
8. Rewrite `paintNode` (four visual states)
9. Update `paintNodePointerArea` (match new radius logic)
10. Rewrite `linkColor` + add `linkWidth` callback
11. Update ForceGraph2D props
12. Update tooltip (add "click to explore" / "click to view details" hint)
13. Update `app/graph/page.tsx` instruction text

## Verification

- `npm run dev` → visit `/graph`
- Initial load: all nodes visible as faint dots, no edges
- Click a node: it + neighbors appear at full opacity, edges visible between them
- Click a revealed neighbor: its connections added to visible set
- Click an already-expanded node: navigates to its detail page
- Click background: resets to initial state
- Type toggles still filter correctly
- `npx tsc --noEmit` passes
