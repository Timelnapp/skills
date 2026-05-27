# /cos-integrity — Gates 3.5 and 5.5

## Args

`3.5` (pre-architecture) or `5.5` (pre-ship). Default: infer from passport stage.

## Timeln (run first)

1. **`timeln-quickly`** — verify client quotes in frame/arc/commercial.
2. **`timeln-shipped`** — verify proof claims.

## Then

Run **`consult-integrity`** → `integrity-3.5.md` or `integrity-5.5.md`.

**FAIL** → block next stage (`/cos-architect` or `/cos-ship`).
