# Data flow

One row per module: what structure goes in, what comes out. This is the project's map — read this before reading implementation code, and check it against a PR before trusting that nothing structural moved.

Every module's docstring carries the same `IN:`/`OUT:` lines shown here. A CI check (`scripts/check_dataflow.py`) fails the build if a module's header and this table disagree — if you change a contract, update both in the same commit.

| Module | IN | OUT |
|---|---|---|
| `sampler.py` | raster source + grid params (tile_size, mode, overlap, count) | `GeoDataFrame[geometry, sample_id]` |
| `maskfilter.py` | candidate GeoDataFrame + mask source (raster class map or vector layer) + target class(es) + coverage rule | filtered GeoDataFrame |
| `extractor.py` | sample geometry + one or more configured sources (each: path, role, resampling_method, optional scales) | `(dict[str, ndarray], metadata: dict)` |
| `writer.py` | iterable of (arrays: dict[str, ndarray], metadata: dict), chunk_id, output_dir | one GeoParquet file per chunk at output_dir/chunk_{id}.parquet |
| `subset.py` | GeoParquet dataset dir + filter query or seeded random selection + name | named subset manifest (+ either a row-reference-only file or a materialized copy) |
| `runner.py` | chunk-processing function + list of chunk ids | side effect -- every chunk processed and written somewhere |
| `hf_export.py` | GeoParquet dataset dir | Hugging Face datasets.Dataset on disk + an auto-generated dataset card (+ optional hub push) |
| `cli.py` | command-line arguments | dispatches to extract / submit / subset / to-hf |

When a module's job genuinely splits into more than one distinct transformation (e.g. `extractor.py` growing single-source, multi-source, and multi-scale variants), function-level `IN:`/`OUT:` comments inside the file carry that detail — this table stays at the module level and isn't meant to capture every function individually.
