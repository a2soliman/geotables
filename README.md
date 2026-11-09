# geotables

**geotables** turns gridded geospatial data — satellite imagery, aerial rasters, elevation models, and similar — into tables ready for modern AI workflows, whether that's a laptop, an HPC cluster, or a cloud data platform.

Most tooling in this space either samples data on the fly during training, or produces one fixed dataset you're stuck with. geotables treats the *sample design* itself as a first-class, recorded object: which locations were sampled, how, and why, is captured alongside the data — not lost in a notebook cell. On top of that, you can carve out named, reproducible subsets of a dataset — `urban_v1`, `coastal_2024`, whatever your experiment calls for — and know exactly how each one was defined and be able to reference it reliably.

The output is plain, portable tables (GeoParquet, with optional Hugging Face `datasets` export) — no platform lock-in, no proprietary format, and nothing that requires redistributing the original raw imagery to share your derived dataset.

## Status

Early development. Design is laid out in [ARCHITECTURE.md](ARCHITECTURE.md); implementation is tracked through [issues](../../issues) and [milestones](../../milestones). Not yet installable.

This is a clean-break successor to [keras-spatial](https://github.com/a2soliman/keras-spatial) — same author, new design, no backward compatibility.

## License

Apache 2.0 — see [LICENSE](LICENSE).
