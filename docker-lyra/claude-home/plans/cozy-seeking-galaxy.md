# Plan: JSON Backup & Restore for Melbourne Tech Ecosystem

## Context

The site has no way to export or import its data. If the database is lost or corrupted, all manually-entered entities/relationships are gone. We need a simple backup/restore feature accessible from the admin UI that exports all data as JSON and can restore it later.

## Approach

- **GET `/api/backup`** — admin-protected, returns all data as a downloadable JSON file
- **POST `/api/restore`** — admin-protected, accepts a backup JSON, validates it, then wipes and reimports inside a transaction
- **Admin UI** — "Download Backup" button + file upload with preview + "Restore" button (with confirmation)

Full restore only (no merge mode) — keeps v1 simple and atomic. The backup format is versioned so merge can be added later.

## Backup JSON Format

```json
{
  "metadata": { "version": 1, "app": "melb-tech-ecosystem", "created_at": "...", "counts": { ... } },
  "rel_types": [ ... ],
  "entities": [ ... ],
  "relationships": [ ... ]
}
```

All UUIDs and timestamps are preserved. Images are URLs only (GCS bucket synced separately).

## Files to Change

### 1. `lib/types.ts` — Add backup types
- `BackupMetadata` interface (version, app, created_at, counts)
- `BackupData` interface (metadata + rel_types + entities + relationships)

### 2. `lib/queries.ts` — Add two functions
- **`getAllBackupData()`** — composes `listRelTypes()`, `listEntities()`, `listRelationships()` in parallel
- **`restoreFromBackup(data)`** — uses `pool.connect()` for a dedicated transaction client:
  1. `BEGIN`
  2. `TRUNCATE relationships, entities, rel_types` (single statement handles FK ordering)
  3. INSERT rel_types, then entities, then relationships (all with explicit IDs/timestamps)
  4. `COMMIT` (or `ROLLBACK` on error)
  - Imports `pool` from `lib/db.ts` (already exported as default)

### 3. `app/api/backup/route.ts` — New file
- GET handler, admin cookie check
- Calls `getAllBackupData()`, wraps in metadata envelope
- Returns with `Content-Disposition: attachment` header for browser download

### 4. `app/api/restore/route.ts` — New file
- POST handler, admin cookie check
- Validates JSON structure: correct `metadata.app`, `version === 1`, arrays present
- Validates referential integrity within the backup (all relationship FKs point to entities/rel_types in the same file)
- Calls `restoreFromBackup()`, returns counts

### 5. `app/admin/page.tsx` — Add backup/restore UI
- New "Data Management" section between the stats bar and tabs
- "Download Backup" button → fetches `/api/backup`, triggers browser download via blob URL
- File input (`.json`) → reads and previews the metadata (counts + date)
- "Restore" button (red, destructive) → `confirm()` dialog → POSTs to `/api/restore` → refreshes all data
- Status message bar for success/error feedback

## Restore Safety

- Full wipe + reimport inside a single Postgres transaction — atomic, rolls back on any error
- Client-side validation of the backup file before sending (correct app identifier, shows preview)
- Server-side validation of referential integrity before executing the restore
- `confirm()` dialog warns that all existing data will be replaced

## Verification

1. Start the dev server (`npm run dev`) with Docker DB running (`npm run db:up`)
2. Log into admin, click "Download Backup" — verify a `.json` file downloads with correct data
3. Add a test entity via admin
4. Upload the backup file, verify preview shows correct counts
5. Click "Restore", confirm — verify the test entity is gone and original data is restored
6. Run `npx tsc --noEmit` to verify no type errors
