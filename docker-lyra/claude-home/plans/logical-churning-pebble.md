# Deploy melb-tech to Google Cloud Run

## Context
The melb-tech app is fully built and running locally. We need to deploy it to Cloud Run with a managed Cloud SQL Postgres database. The Dockerfile and app are already Cloud Run-ready (`standalone` output, `PORT` env var, non-root user). Auto-deploy on merge to main via GitHub Actions.

## What already works
- `Dockerfile` — multi-stage, standalone Node.js, listens on PORT, non-root user
- `next.config.mjs` — `output: 'standalone'`
- `lib/db.ts` — uses `DATABASE_URL` env var (no hardcoded connection)
- `.github/workflows/ci.yml` — has deploy job stub looking for `scripts/deploy.sh`

---

## Steps

### Step 1: Create GCP project + enable services
```bash
gcloud projects create melb-tech-prod --name="Melbourne Tech Ecosystem"
gcloud config set project melb-tech-prod
# Link billing (user must do this interactively if no default billing account)
gcloud services enable \
  run.googleapis.com \
  sqladmin.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  secretmanager.googleapis.com
```

### Step 2: Create Artifact Registry repo
```bash
gcloud artifacts repositories create melb-tech \
  --repository-format=docker \
  --location=australia-southeast1 \
  --description="melb-tech container images"
```
Region: `australia-southeast1` (Melbourne) for low latency.

### Step 3: Create Cloud SQL Postgres instance
```bash
gcloud sql instances create melb-tech-db \
  --database-version=POSTGRES_16 \
  --tier=db-f1-micro \
  --region=australia-southeast1 \
  --storage-size=10GB \
  --storage-auto-increase

gcloud sql databases create melbtech --instance=melb-tech-db
gcloud sql users create melbtech \
  --instance=melb-tech-db \
  --password=<generated-secure-password>
```
- `db-f1-micro` is the cheapest tier (~$8/mo)
- Same region as Cloud Run for private networking

### Step 4: Seed the production database
Connect via Cloud SQL proxy and run init.sql + seed.sql:
```bash
# In a separate terminal:
gcloud sql connect melb-tech-db --user=melbtech --database=melbtech
# Then paste init.sql and seed.sql contents
```
Or use the Cloud SQL Auth Proxy locally.

### Step 5: Store secrets
```bash
echo -n "<db-password>" | gcloud secrets create db-password --data-file=-
echo -n "<admin-password>" | gcloud secrets create admin-password --data-file=-
```

### Step 6: Create `scripts/deploy.sh`
**File: `scripts/deploy.sh`**

This script:
1. Builds the Docker image
2. Pushes to Artifact Registry
3. Deploys to Cloud Run with Cloud SQL connection + env vars

```bash
#!/bin/bash
set -euo pipefail

PROJECT_ID="melb-tech-prod"
REGION="australia-southeast1"
SERVICE="melb-tech"
REPO="australia-southeast1-docker.pkg.dev/$PROJECT_ID/melb-tech"
IMAGE="$REPO/app:$GITHUB_SHA"
CLOUD_SQL_INSTANCE="$PROJECT_ID:$REGION:melb-tech-db"

# Build and push
docker build -t "$IMAGE" .
docker push "$IMAGE"

# Deploy to Cloud Run
gcloud run deploy "$SERVICE" \
  --image="$IMAGE" \
  --region="$REGION" \
  --platform=managed \
  --allow-unauthenticated \
  --add-cloudsql-instances="$CLOUD_SQL_INSTANCE" \
  --set-env-vars="NODE_ENV=production" \
  --set-secrets="DATABASE_URL=db-url:latest,ADMIN_PASSWORD=admin-password:latest" \
  --min-instances=0 \
  --max-instances=3 \
  --memory=512Mi \
  --cpu=1 \
  --port=3000
```

### Step 7: Update CI workflow for auto-deploy
**File: `.github/workflows/ci.yml`** — update the deploy job to:
1. Authenticate to GCP using Workload Identity Federation (preferred) or a service account key
2. Configure Docker for Artifact Registry
3. Run `scripts/deploy.sh`

Add GitHub Actions secrets:
- `GCP_PROJECT_ID` = `melb-tech-prod`
- `GCP_SA_KEY` = service account JSON key (or use Workload Identity Federation)

Updated deploy job:
```yaml
deploy:
  needs: test
  runs-on: ubuntu-latest
  if: github.event_name == 'push' && github.ref == 'refs/heads/main'
  permissions:
    contents: read
    id-token: write
  steps:
    - uses: actions/checkout@v4
    - uses: google-github-actions/auth@v2
      with:
        credentials_json: ${{ secrets.GCP_SA_KEY }}
    - uses: google-github-actions/setup-gcloud@v2
    - run: gcloud auth configure-docker australia-southeast1-docker.pkg.dev --quiet
    - run: chmod +x scripts/deploy.sh && scripts/deploy.sh
```

### Step 8: Create the DATABASE_URL secret
The Cloud SQL connection from Cloud Run uses a Unix socket:
```
DATABASE_URL=postgresql://melbtech:<password>@/melbtech?host=/cloudsql/melb-tech-prod:australia-southeast1:melb-tech-db
```
Store this as a Secret Manager secret:
```bash
echo -n "postgresql://melbtech:<pw>@/melbtech?host=/cloudsql/melb-tech-prod:australia-southeast1:melb-tech-db" \
  | gcloud secrets create db-url --data-file=-
```

### Step 9: Create GCP service account for CI
```bash
gcloud iam service-accounts create github-deploy \
  --display-name="GitHub Actions Deploy"

# Grant roles
SA="github-deploy@melb-tech-prod.iam.gserviceaccount.com"
gcloud projects add-iam-policy-binding melb-tech-prod \
  --member="serviceAccount:$SA" --role="roles/run.admin"
gcloud projects add-iam-policy-binding melb-tech-prod \
  --member="serviceAccount:$SA" --role="roles/artifactregistry.writer"
gcloud projects add-iam-policy-binding melb-tech-prod \
  --member="serviceAccount:$SA" --role="roles/secretmanager.secretAccessor"
gcloud projects add-iam-policy-binding melb-tech-prod \
  --member="serviceAccount:$SA" --role="roles/cloudsql.client"
gcloud projects add-iam-policy-binding melb-tech-prod \
  --member="serviceAccount:$SA" --role="roles/iam.serviceAccountUser"

# Create key for GitHub Actions
gcloud iam service-accounts keys create /tmp/gh-deploy-key.json \
  --iam-account="$SA"
# Add contents as GitHub secret GCP_SA_KEY
```

Also grant the Cloud Run service account access to secrets:
```bash
CR_SA="$(gcloud iam service-accounts list --filter='displayName:Compute Engine' --format='value(email)')"
gcloud secrets add-iam-policy-binding db-url \
  --member="serviceAccount:$CR_SA" --role="roles/secretmanager.secretAccessor"
gcloud secrets add-iam-policy-binding admin-password \
  --member="serviceAccount:$CR_SA" --role="roles/secretmanager.secretAccessor"
```

---

## Files to create/modify

| File | Action | Description |
|------|--------|-------------|
| `scripts/deploy.sh` | **Create** | Cloud Run deploy script (build, push, deploy) |
| `.github/workflows/ci.yml` | **Modify** | Add GCP auth + Artifact Registry + deploy steps |
| `.gcloudignore` | **Create** | Ignore node_modules, .next, .git for Cloud Build |

## Execution order

1. GCP infra setup (gcloud commands — interactive, requires billing confirmation)
2. Create Cloud SQL instance + database + seed data
3. Create secrets in Secret Manager
4. Create service account + GitHub secret
5. Write `scripts/deploy.sh` and update CI workflow
6. First deploy: push to main, verify CI deploys successfully
7. Verify the live URL works

## Verification

1. `gcloud run services describe melb-tech --region=australia-southeast1` → service exists
2. Visit the Cloud Run URL → home page loads with seeded data
3. Browse `/people`, `/graph` → all pages work
4. `/admin` → password gate works with production password
5. Search → fuzzy search returns results (pg_trgm works on Cloud SQL)
6. Push a trivial change to main → CI auto-deploys → verify new version live

## Cost estimate
- Cloud SQL db-f1-micro: ~$8/month
- Cloud Run (min 0 instances): ~$0-2/month at low traffic
- Artifact Registry: ~$0.10/month
- **Total: ~$8-10/month** (dominated by Cloud SQL)
