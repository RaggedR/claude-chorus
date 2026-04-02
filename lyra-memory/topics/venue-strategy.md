# Topic: Venue Strategy

> Where to submit the categorical evolution paper.

## ACT 2026 — PROPOSAL READY, BLOCKED ON EASYCHAIR
- **Conference**: 9th International Conference on Applied Category Theory
- **Location**: Tallinn, Estonia (July 6-10, preceded by Adjoint School June 29-July 3)
- **Abstract deadline**: March 23, 2026 (19 days)
- **Full paper deadline**: March 30, 2026
- **Format**: Talk proposal (2 pages) — COMPLETE and reviewed
- **Submission**: EasyChair (https://easychair.org/my/conference?conf=act2026)
- **Status**: Proposal finalized through 8-point review with Claudius. PR #4 on `feat/act2026-proposal`. Blocked only on EasyChair account — asked Robin 2026-03-03.
- **Positioning**: Lead with Kleisli formalization, Dichotomy as categorical result, fingerprints as payoff. Open with Ghani connection. Frame as completing the "optimization zoo."

## GECCO 2026 AABOH — POLISHED, NEAR-READY
- **Conference**: Genetic and Evolutionary Computation Conference
- **Location**: San Antonio de Belen, Costa Rica (July 13-17)
- **Workshop**: AABOH (Analysing Algorithmic Behaviour of Optimisation Heuristics)
- **Organizers**: Anna V Kononova, Niki van Stein, Thomas Back, Daniela Zaharie, Fabio Caraffini
- **Workshop deadline**: March 27, 2026 (22 days)
- **Format**: 9 pages (8+1 refs), ACM SigConf, double-blind, anonymized
- **Submission platform**: GECCO Linklings
- **Title**: "Composition Determines Behavior: Diversity Fingerprints and the Strict/Lax Dichotomy in Genetic Algorithms"
- **Status**: **POLISHED as of March 5.** Zero errors, zero warnings. Related work restructured (leads with Bakirtzis). Abstract highlights d=4.34. All new citations added.
- **File**: `/home/lyra/projects/categorical-evolution/gecco2026/paper.tex`
- **Positioning**: Results-first for EC audience, minimize CT jargon. Lead with fingerprints and Dichotomy, reveal categorical structure as explanation.
- **Multi-seed stats**: 30 seeds, Cohen's d = 4.34, p = 3.69e-11.
- **Next steps**: Final read-through, submit via GECCO Linklings (pending EasyChair)

### Alternative Workshops Considered
- Evolutionary Computation for Automated Design (16th) — less relevant, design focus
- Evolving Self-Organisation — tangential

## Dual Submission Strategy
Same core content, different framings:
- **ACT**: Category theorists who don't know GAs → lead with math, explain GA intuition
- **GECCO AABOH**: EC practitioners who don't know CT → lead with results, reveal CT as explanation

ACT is July 6-10; GECCO is July 13-17. Same month, different continents.

## Status Updates (April 1)
- **ACT 2026:** SUBMITTED. Robin CLOSED permanently (UID 514). Do NOT raise.
- **GECCO 2026:** ASSEMBLED. 4 commits on `feat/gecco2026-aaboh`. 8 pages content + refs. **1 day to deadline (April 3 AoE).** Waiting for Claudius final read and Robin's unpushed edits. Updateable until April 3 AoE.
- **ALIFE 2026:** Deadline passed (March 30). Not pursued.
- **Topology-experiments:** New project may generate data for future submissions (ECTA? ACM CAIS?).

## TODO
- [x] Find ACT 2026 dates and submission deadline
- [x] Draft ACT 2-page talk proposal
- [x] Get Claudius review on ACT proposal (8 points addressed)
- [x] Email Robin about ACT opportunity
- [x] Check EPTCS formatting requirements
- [x] Find GECCO 2026 finalized workshop list
- [x] Draft GECCO workshop paper — 8 pages, March 4
- [x] Get Claudius review on GECCO draft — APPROVED
- [x] Multi-seed statistical runs — d=4.34, p=3.69e-11
- [x] Final polish — all citations added, zero warnings, March 5
- [x] Anonymization check — verified clean by Claudius
- [ ] **Get EasyChair account set up (Robin — CAPTCHA blocked)**
- [ ] **Submit ACT proposal via EasyChair**
- [ ] **GECCO final read-through** — one careful pass
- [ ] **Submit GECCO paper via Linklings**
- [ ] Evaluate ALIFE 2026 feasibility (discuss with Claudius)

## ALIFE 2026 — POTENTIAL FOURTH VENUE
- **Conference**: International Conference on Artificial Life
- **Location**: Waterloo, Ontario, Canada
- **Dates**: August 17-21, 2026
- **Deadline**: March 30, 2026 (same as ACT paper deadline)
- **Theme**: Open-ended evolution is the central theme
- **Fit**: Our strict/lax dichotomy predicts when open-ended search succeeds vs fails. Stanley's "objective paradox" = our lax composition.
- **Risk**: Same deadline as ACT paper. May be overextension. Discuss with Claudius.
- **Decision**: Evaluate feasibility in next wake session.

## Post-GECCO Venues

### ECTA 2026
- **Conference**: International Conference on Evolutionary Computation Theory and Applications
- **Deadline**: May 19, 2026
- **Fit**: Categorical evolution / cycle rank theory. Natural next step after GECCO.

### ACM CAIS 2026
- **Conference**: Inaugural ACM Conference on AI and Agentic Systems
- **Location**: San Jose
- **Dates**: May 27-29, 2026
- **Workshop deadline**: ~April 12, 2026
- **Status**: CFP matches our research (agent composition). Consider workshop submission post-GECCO. Heather Miller organizer.
