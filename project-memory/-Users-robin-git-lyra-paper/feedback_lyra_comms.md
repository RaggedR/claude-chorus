---
name: lyra-email-timing
description: Lyra doesn't reliably act on emails sent during her work cycle - direct file replacement via docker exec is more reliable
type: feedback
---

Emails to Lyra are processed at the START of her wake cycle, not during. If she's already working, emailing her won't redirect her current session. To force changes mid-session, use `docker cp` to replace files directly in her container.

**Why:** Robin sent Lyra an email asking her to checkout the second-draft branch. She ignored it and kept editing her local copy.

**How to apply:** When Lyra needs to work on specific files urgently, don't rely on email — docker exec / docker cp to place the files directly. Email only works for the *next* cycle.
