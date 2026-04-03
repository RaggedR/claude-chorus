---
name: Delivery Router project status
description: Flutter web app deployed to Cloud Run — route optimizer for Jenni's warehouse drivers
type: project
---

Delivery Router is live at https://delivery-router-314185672280.australia-southeast1.run.app

**Repo:** https://github.com/RaggedR/delivery-router
**Stack:** Flutter web frontend, Dart HttpServer backend, Cloud Run (australia-southeast1)
**GCP project:** knowledge-graph-app-kg

**Why:** Jenni's warehouse dispatches delivery drivers each morning. This optimizes their routes using Held-Karp TSP (exact, up to 20 stops).

**How to apply:** Future work ideas discussed with Robin:
- Bulk address import (paste from spreadsheet)
- Time windows for deliveries
- Multi-driver route splitting (VRP)
- Theme still needs visual verification — indigo/slate was applied but user couldn't confirm it landed
- GitHub Actions CI/CD is set up but was failing on permissions — may need checking
