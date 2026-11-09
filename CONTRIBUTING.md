# Contributing

## The data-flow convention

Every module in `src/geotables/` states its contract — what structure goes in, what comes out — in its module docstring, as `IN:` / `OUT:` lines:

```python
"""
geotables.sampler

IN:  raster source + grid params (tile_size, mode, overlap, count)
OUT: GeoDataFrame[geometry, sample_id]

One or two sentences on why, if it's not obvious from the contract alone.
"""
```

That same contract is restated in [`DATAFLOW.md`](DATAFLOW.md), one row per module — the whole project's data flow at a glance, without having to open and read every file. `scripts/check_dataflow.py` runs in CI and fails the build if a module's header and its `DATAFLOW.md` row disagree. If you change what a module takes in or returns, update both in the same commit — the check exists specifically so that doesn't happen silently.

When a single module's job genuinely splits into more than one distinct transformation (e.g. `extractor.py` handling single-source, multi-source, and multi-scale extraction), give each function its own short `IN:`/`OUT:` comment above it too. That's a reviewing convention, not something CI checks line-by-line — the point is that anyone reviewing a PR can read the function's three-line header and know what it does without reading the implementation.

## Pull requests

The PR template asks one direct question: did this change a module's contract? If yes, say what changed and why, and make sure `DATAFLOW.md` reflects it. This is the single most useful thing a reviewer can check quickly, and the thing most likely to get missed when a change is otherwise straightforward.

## Picking up an issue

Issues are filed against one of three milestones (v0.1 local pipeline, v0.2 multi-source/filtering/subsets, v0.3 cluster + HF export) and each one already states its contract and acceptance criteria — that's the spec, not a suggestion. If you think the contract as written is wrong, raise it on the issue before implementing something different; contracts are shared infrastructure other issues depend on.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the reasoning behind the overall design.
