"""
geotables.subset

IN:  GeoParquet dataset dir + filter query or seeded random selection + name
OUT: named subset manifest (+ either a row-reference-only file or a materialized copy)

The actual differentiator of this project: a subset is a reproducible,
inspectable object, not a one-off query someone forgot the parameters
of. See ARCHITECTURE.md.

Implements: issue #8
"""


def create_subset(dataset_dir, query=None, seed=None, name=None, materialize=False):
    """
    IN:  dataset_dir: str, query: str | None, seed: int | None, name: str, materialize: bool
    OUT: subset manifest dict, written alongside the dataset
    """
    raise NotImplementedError
