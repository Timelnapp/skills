# /cos-market — Lookalike target list (post-win)

Find the next 5 companies who'd buy the same use case. Runs `consult-market`.

## Inputs (ask if missing)

- **Industry / vertical**, **company size band**, **use case** (one line) — required
- Region, exclusions — optional

## Timeln (run first)

1. **`timeln-find`** — analogous accounts/engagements for the vertical + use case.

## Then

Run **`consult-market`**:

- Web/Exa for firmographics + buying signals; Apollo/Clay if connected.
- Score top 5 on industry + size + use-case fit + signal recency.
- Contacts: verified-source only, else `not verified — enrich`. Never guess emails.
- Write MD table + CSV (offer XLSX) to the path you name (default `./lookalikes/{use-case-slug}-targets.*`).

**Next step:** `/cos-pursue {company} for {use case}` to draft outreach.
