#!/usr/bin/env python3
"""
Verify directed cycle counts for the proposed graph families.
Confirms that graphs with same (n, m) have different directed cycle structure.
"""

import networkx as nx


def count_directed_cycles(G):
    """Count simple directed cycles in G."""
    cycles = list(nx.simple_cycles(G))
    return len(cycles), cycles


def directed_cycle_rank(G):
    """Sum of (|E_scc| - |V_scc| + 1) over non-trivial SCCs."""
    total = 0
    scc_info = []
    for scc in nx.strongly_connected_components(G):
        if len(scc) < 2:
            continue
        subG = G.subgraph(scc)
        rank = subG.number_of_edges() - len(scc) + 1
        total += rank
        scc_info.append((len(scc), subG.number_of_edges(), rank))
    return total, scc_info


def summarize(name, G):
    n_cycles, cycles = count_directed_cycles(G)
    d_rank, scc_info = directed_cycle_rank(G)
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"  n={G.number_of_nodes()}, m={G.number_of_edges()}")
    print(f"  Directed cycles: {n_cycles}")
    print(f"  Directed cycle rank: {d_rank}")
    print(f"  SCCs (|V|, |E|, rank): {scc_info}")
    print(f"  Strongly connected: {nx.is_strongly_connected(G)}")
    cycle_lengths = [len(c) for c in cycles]
    if cycle_lengths:
        print(f"  Cycle length distribution: min={min(cycle_lengths)}, "
              f"max={max(cycle_lengths)}, avg={sum(cycle_lengths)/len(cycle_lengths):.1f}")
    print(f"{'='*60}")


# ---- DAG Family (0 directed cycles) ----

def dag_layer():
    """DAG-Layer: {0,1} -> {2,3,4} -> {5,6,7}, plus 0->1."""
    G = nx.DiGraph()
    G.add_nodes_from(range(8))
    # Layer 1 -> Layer 2
    for s in [0, 1]:
        for t in [2, 3, 4]:
            G.add_edge(s, t)
    # Layer 2 -> Layer 3
    for s in [2, 3, 4]:
        for t in [5, 6, 7]:
            G.add_edge(s, t)
    # Intra-layer
    G.add_edge(0, 1)
    return G


def dag_wide():
    """DAG-Wide: 0 broadcasts to all, then layered fan-out."""
    G = nx.DiGraph()
    G.add_nodes_from(range(8))
    # Node 0 to all
    for t in range(1, 8):
        G.add_edge(0, t)
    # Nodes 1,2,3 each to 5,6
    for s in [1, 2, 3]:
        for t in [5, 6]:
            G.add_edge(s, t)
    # Node 4 to 6,7
    G.add_edge(4, 6)
    G.add_edge(4, 7)
    # Node 5 to 7
    G.add_edge(5, 7)
    return G


# ---- Low-Cycle Family ----

def lowcyc_1():
    """DAG-Layer with one edge reversed: 5->2 creates a 2-step feedback."""
    G = dag_layer()
    G.remove_edge(2, 5)
    G.add_edge(5, 2)
    # Now 2->5 is gone, we have 5->2. But we need 2->5 path too.
    # Actually: layer1 sends to 2, and 5->2 creates feedback.
    # Path: 0->2->3...no, 2 sends to {5,6,7} minus 5. So 2->6, 2->7.
    # And 5->2 creates: any path to 5 then 5->2 then 2->6 or 2->7.
    # Cycle: need path from 2 to 5 to 2. But we removed 2->5.
    # Path 2->5: only via layer 2->layer 3. But 2 sends to {6,7} (not 5 anymore).
    # Hmm, we need to be more careful.
    # Let's just reverse one edge that creates a cycle.
    # Better: keep 2->5, add 5->0 (reverse of the flow).
    G = dag_layer()
    G.remove_edge(0, 1)  # free up an edge
    G.add_edge(5, 0)     # feedback: 0->2->5->0 is a 3-cycle
    return G


def lowcyc_3():
    """DAG-Layer with three feedback edges creating independent cycles."""
    G = dag_layer()
    # Remove 3 intra-layer edges to free up
    # Actually dag_layer only has 1 intra edge (0->1).
    # Total is 6+9+1 = 16. We need to swap edges.
    # Remove 3 forward edges, add 3 backward edges.
    G.remove_edge(0, 1)
    G.remove_edge(0, 3)
    G.remove_edge(1, 4)
    G.add_edge(5, 0)  # cycle: 0->2->5->0
    G.add_edge(6, 1)  # cycle: 1->3->6->1... wait 1->3 was removed? No, 1->{2,3,4}
    G.add_edge(7, 0)  # cycle: 0->4->7->0... 0->4 exists? Yes.
    return G


# ---- Medium-Cycle Family ----

def medcyc_ring():
    """Two interleaved directed rings: ring + skip-2 ring."""
    G = nx.DiGraph()
    G.add_nodes_from(range(8))
    # Base ring
    for i in range(8):
        G.add_edge(i, (i + 1) % 8)
    # Skip-2 ring
    for i in range(8):
        G.add_edge(i, (i + 2) % 8)
    return G


def medcyc_skip3():
    """Ring + skip-3 ring."""
    G = nx.DiGraph()
    G.add_nodes_from(range(8))
    for i in range(8):
        G.add_edge(i, (i + 1) % 8)
    for i in range(8):
        G.add_edge(i, (i + 3) % 8)
    return G


# ---- High-Cycle Family ----

def highcyc_tournament():
    """Ring + skip-2 + skip-3 (selecting 16 edges)."""
    G = nx.DiGraph()
    G.add_nodes_from(range(8))
    # Ring (8)
    for i in range(8):
        G.add_edge(i, (i + 1) % 8)
    # Skip-3 (8)
    for i in range(8):
        G.add_edge(i, (i + 3) % 8)
    # Already 16
    return G


def highcyc_bidir():
    """Bidirectional ring + 8 extra cross edges."""
    G = nx.DiGraph()
    G.add_nodes_from(range(8))
    # Forward ring
    for i in range(8):
        G.add_edge(i, (i + 1) % 8)
    # Backward ring (opposite direction)
    for i in range(8):
        G.add_edge((i + 1) % 8, i)
    return G


# ---- Run all ----

if __name__ == "__main__":
    families = [
        ("DAG-Layer", dag_layer()),
        ("DAG-Wide", dag_wide()),
        ("LowCyc-1 (one feedback)", lowcyc_1()),
        ("LowCyc-3 (three feedback)", lowcyc_3()),
        ("MedCyc-Ring (ring + skip-2)", medcyc_ring()),
        ("MedCyc-Skip3 (ring + skip-3)", medcyc_skip3()),
        ("HighCyc-Tournament (ring + skip-3)", highcyc_tournament()),
        ("HighCyc-Bidir (bidirectional ring)", highcyc_bidir()),
    ]

    print("DIRECTED CYCLE STRUCTURE VERIFICATION")
    print("=" * 60)

    for name, G in families:
        summarize(name, G)

    # Summary table
    print("\n\nSUMMARY TABLE")
    print(f"{'Name':<40} {'n':>3} {'m':>3} {'#Cycles':>8} {'DirRank':>8}")
    print("-" * 70)
    for name, G in families:
        n_cyc, _ = count_directed_cycles(G)
        d_rank, _ = directed_cycle_rank(G)
        print(f"{name:<40} {G.number_of_nodes():>3} {G.number_of_edges():>3} "
              f"{n_cyc:>8} {d_rank:>8}")
