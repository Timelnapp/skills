# /cos-resume — Continue from passport stage

Run **`consult-pipeline`** from `engagement-passport.yaml` → `stage`.

## Do

1. Read `prospects/{slug}/engagement-passport.yaml` (or path user gives).
2. If missing, suggest `/cos-plan`.
3. Resume at recorded `stage`; run Timeln prefetch for that stage per pipeline table.
4. Update passport on checkpoint completion.

## Env

`COS_PASSPORT_RESET=1` — ignore stage; restart at CAPTURE.
