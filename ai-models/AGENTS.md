# AI Models

This user-authorized top-level folder owns model comparisons and the entire
working collection procedure. Root Agents workspace rules still apply.

## Read only what the task needs

- Choosing a model to delegate to: `delegation-briefing.md` (the only place
  that chooses models; rules in `specs/model-delegation/spec.md`).
- Reading numbers: `README.md`, `STATE.md`, then the selected `data/<date>/`
  snapshot or table (raw data not published). Do not load raw payloads, full catalogues or old research
  reports into model context.
- Adding models/metrics or collecting: `collection/README.md`, then only the
  needed section of `collection/LEARNINGS.md` or `collection/API.md`.
- Resume after compaction: `STATE.md` owns the exact next action.

## Data rules

- Resolve UUID + exact slug + effort. Honor `favorites.json` defaults. Never
  assume an unsuffixed slug means medium; these families use it for max.
- Keep API and website measurements separate, with versions, units, timestamps
  and source hashes. Null/missing is unavailable, not zero.
- Decode time is not wall-clock completion. Prompt-length settings are not
  reasoning settings. Claude fallback settings are part of model identity.
- Read from this folder, not Downloads. Do not edit generated table values;
  rebuild from source data. Preserve dated evidence when adding a newer snapshot.
- Unknown metrics may be kept in raw source objects, but do not label them
  supported until their meaning, unit and configuration are checked.

## Collection rules

Start offline. Reuse the whole catalogue/payload once per batch. Never launch an
LLM reader merely to parse JSON or look up a model already present. Native readers
are targeted checks, not the numeric ingestion source. Do not open a visible
browser without the owner agreeing. Stop on access controls or throttling; no paid
upgrade, export bypass or credential persistence. Keys belong only in the process
environment or the private credential system, never this folder or Git.

Any durable change here updates `STATE.md`. External skill/capability files may
be thin discovery pointers; substantive data/procedure stays here.
