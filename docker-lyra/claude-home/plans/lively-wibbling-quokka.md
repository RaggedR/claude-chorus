# Plan: GitHub Actions CI + Cloud Run CD

## Context

PR #1 (Knowledge Graph Web App) was merged to main with 54 passing tests, but there's no CI/CD pipeline. Tests only run locally, meaning future PRs could break security-critical behavior (path traversal prevention, upload size limits, XSS escaping) without anyone noticing. The app is already deployed to Cloud Run at `https://kg-web-bb6sfpptkq-ts.a.run.app/` but deployment is manual.

**Goal:** Add automated test gating on every push/PR and auto-deploy to Cloud Run on merge to main.

## GCP Configuration

| Setting | Value |
|---------|-------|
| Project ID | `knowledge-graph-app-kg` |
| Project Number | `314185672280` |
| Service | `kg-web` |
| Region | `australia-southeast1` |

## Files to Create

| File | Purpose |
|------|---------|
| `.github/workflows/ci.yml` | Run unit + API tests, then E2E tests on every push/PR |
| `.github/workflows/deploy.yml` | Build Docker image, push to Artifact Registry, deploy to Cloud Run on merge to main |
| `scripts/setup-gcp-wif.sh` | One-time GCP Workload Identity Federation setup (run manually, kept for documentation) |

## 1. CI Workflow (`.github/workflows/ci.yml`)

**Triggers:** push to any branch, PRs to main

**Job 1: `test`** (unit + API tests)
- Ubuntu latest, Python 3.12
- `apt-get install libmupdf-dev` (required by PyMuPDF)
- `pip install -e . && pip install -r requirements-dev.txt`
- `pytest tests/ -v --ignore=tests/test_e2e.py --junitxml=test-results.xml`
- Upload JUnit XML as artifact
- No API keys needed — all tests are mocked via `tests/conftest.py`

**Job 2: `e2e`** (Playwright browser tests, depends on Job 1)
- Same Python/system setup
- `playwright install chromium --with-deps`
- `pytest tests/test_e2e.py -v --junitxml=e2e-results.xml`
- Upload JUnit XML as artifact

**Extras:**
- `concurrency` group cancels in-progress CI runs on same branch (saves runner minutes)
- `pip` cache via `setup-python` cache option

## 2. CD Workflow (`.github/workflows/deploy.yml`)

**Triggers:** push to main only

**Authentication:** Workload Identity Federation (keyless OIDC)
- Uses `google-github-actions/auth@v2` with OIDC token
- Requires `permissions: id-token: write`

**Steps:**
1. Checkout
2. Authenticate to GCP via WIF
3. Configure Docker for Artifact Registry
4. `docker build` + `docker push` (tagged with `${{ github.sha }}` and `latest`)
5. Deploy to Cloud Run via `google-github-actions/deploy-cloudrun@v2`

**Image path:** `australia-southeast1-docker.pkg.dev/knowledge-graph-app-kg/kg-web/kg-web`

**Secrets required (2):**
| Secret | Value |
|--------|-------|
| `WORKLOAD_IDENTITY_PROVIDER` | `projects/314185672280/locations/global/workloadIdentityPools/github-actions-pool/providers/github-oidc` |
| `GCP_SERVICE_ACCOUNT` | `github-actions-deploy@knowledge-graph-app-kg.iam.gserviceaccount.com` |

**Concurrency:** `cancel-in-progress: false` — don't cancel mid-deploy

## 3. GCP Setup Script (`scripts/setup-gcp-wif.sh`)

One-time script (run locally with `gcloud` as project owner):

1. Enable APIs: `iam`, `iamcredentials`, `run`, `artifactregistry`
2. Create Artifact Registry repo `kg-web` in `australia-southeast1`
3. Create Workload Identity Pool `github-actions-pool`
4. Create OIDC Provider `github-oidc` with attribute condition restricting to `RaggedR/math-research-tools`
5. Create Service Account `github-actions-deploy` with roles:
   - `roles/run.admin` — deploy Cloud Run services
   - `roles/artifactregistry.writer` — push Docker images
   - `roles/iam.serviceAccountUser` — act as runtime SA
6. Bind WIF pool to SA (scoped to this repo only)
7. Print the two GitHub secrets to configure

## Implementation Sequence

1. **Run GCP setup script** — create WIF infrastructure, Artifact Registry repo
2. **Add GitHub secrets** — `WORKLOAD_IDENTITY_PROVIDER` and `GCP_SERVICE_ACCOUNT`
3. **Create branch** `ci/github-actions`
4. **Write** `.github/workflows/ci.yml`
5. **Write** `.github/workflows/deploy.yml`
6. **Save** `scripts/setup-gcp-wif.sh` for documentation
7. **Push branch** — verify CI workflow triggers and all tests pass
8. **Open PR** to main, get MaxwellMergeSlam review
9. **After merge** — verify deploy workflow triggers and Cloud Run updates
10. **Enable branch protection** — require `test` and `e2e` status checks on main

## Verification

1. Push to branch → CI triggers, `test` job passes (54 tests minus E2E), `e2e` job passes
2. JUnit XML artifacts uploaded and downloadable
3. PR to main shows required status checks
4. Merge to main → deploy workflow triggers
5. Auth step succeeds (WIF OIDC)
6. Image appears in Artifact Registry: `gcloud artifacts docker images list australia-southeast1-docker.pkg.dev/knowledge-graph-app-kg/kg-web`
7. Cloud Run service updated: `gcloud run services describe kg-web --region=australia-southeast1`
8. App loads at service URL

## Confidence: 90%

Main risk: WIF setup has many moving parts (pool, provider, SA, bindings). If any step is misconfigured, the deploy workflow will fail with an auth error. The setup script handles this deterministically, and errors will be clear and fixable.

## Critical Existing Files (read-only context)

- `Dockerfile` — already Cloud Run-ready (python:3.12-slim, libmupdf-dev, `pip install .`, uvicorn on $PORT)
- `pyproject.toml` — package definition used by `pip install -e .` in CI
- `requirements-dev.txt` — test dependencies (pytest, pytest-asyncio, httpx, playwright)
- `tests/conftest.py` — mock fixtures proving no API keys needed
- `tests/test_e2e.py` — Playwright tests using random port via `_find_free_port()`
