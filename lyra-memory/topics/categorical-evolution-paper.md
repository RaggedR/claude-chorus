# Topic: Categorical Evolution Paper

> Updated: 2026-03-21 (Dream Cycle)

## Paper
"From Games to Graphs: Categorical Composition of Genetic Algorithms Across Domains"

## Status: ACT SUBMITTED, GECCO IN PROGRESS

### ACT 2026 — SUBMITTED
- **Robin submitted BOTH abstract AND full paper** (UID 458, March 21).
- EasyChair Submission #10. 3 authors: Langer (1st), Turing, Vega.
- Commit `ce88507` on main = submitted version.
- **Changes on branch only, NOT main.** Robin needs space.
- 9 pages (7.5 body). Restructured from 14 pages after Robin's rejection (March 20).
- **Open:** Can EasyChair be updated before March 30?

### GECCO 2026 AABOH — PRIMARY FOCUS
- **March 27 deadline** (6 days). 9 pages ACM SigConf, double-blind.
- Branch: `feat/gecco2026-aaboh`. Polished, builds clean.
- **Claudius pivoting here.** Wants expanded laxator section.
- 3 citations to add: AgentConductor, MAC, MCE.

## Key Theoretical Contributions
1. **GA operators as Kleisli morphisms** — first categorical formalization of evolutionary computation
2. **Spectral Bridge** (Proposition/Conjecture 1) — lambda_2 predicts diversity ordering
3. **Laxator** (Remark 2) — identified but construction = future work (honest)
4. **Domain independence** — W=1.0 across 6 domains, p=0.00008
5. **110x time-averaged gap** — spectral signature of strict vs lax

## Major Events (March 20-21)
- **March 20:** Robin rejected 13-page version ("logical structure is shit"). Extended session for restructuring. 14→9 pages. Robin: "much much better."
- **March 21:** Robin submitted. Claudius sent 8 emails, pivoting to GECCO. Lax/oplax verified. GECCO polished.

## All Experiments COMPLETE
| Domain | Ordering | Notes |
|--------|----------|-------|
| OneMax | Yes (rho=1.0) | Benchmark domain |
| Maze | Yes (rho=1.0) | Primary designed domain |
| Graph Coloring | Yes (rho=1.0) | Combinatorial domain |
| Knapsack | Yes (rho=1.0) | Optimization domain |
| No Thanks! | Yes (rho=1.0) | Co-evolutionary, largest phase transition (53.9%) |
| Checkers | Yes (rho=1.0) | Co-evolutionary, smallest phase transition (11.1%) |

**Kendall's W=1.0, chi-square=24.0, p=0.00008.** n=7 Maze confirms spectral prediction (p=6.6e-5).

## Five Mathematical Convergences
1. Category theory (our laxator)
2. Homological algebra (Li et al. — derived functors)
3. Physics (Sanz — algebraic connectivity)
4. Evolutionary graph theory (Brewster/Nowak — PNAS Nexus)
5. Causal category theory (Wilson — strict separation, 75%)

## Key Files
- ACT paper: `projects/categorical-evolution/act2026/paper.tex`
- GECCO paper: `projects/categorical-evolution/gecco2026/paper.tex`
- GUIDE: `projects/categorical-evolution/GUIDE.md`
- Experiments: `projects/categorical-evolution/experiments/`

## Topology-Experiments Project (March 28) — NEW EMPIRICAL ARM

Robin launched a new collaborative project to generate experimental data validating the framework.
- Claudius picks topologies (9+ Foster-census cubic graphs), computes lambda_2
- Lyra runs island-model GA simulations across topologies
- Domain: Maze first (Haskell, Kleisli pipeline), then Checkers
- First batch: Ring (0.382), Dodecahedron (0.76), Desargues (1.324), Petersen (2.0), Hypercube (2.0), Complete
- See: `topics/topology-experiments.md`
