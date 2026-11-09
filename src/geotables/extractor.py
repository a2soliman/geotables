"""
geotables.extractor

IN:  sample geometry + one or more configured sources (each: path, role, resampling_method, optional scales)
OUT: (dict[str, ndarray], metadata: dict)

Reads each source's window at the sample geometry, resampling to a
common output grid where sources differ natively, boundless -- any
part of a chip outside a source's bounds is filled with that source's
nodata value, so every chip comes out the same configured shape.
resampling_method is required per source, no implicit default.

Implements: issues #2 (single source), #6 (multi-source), #7 (multi-scale)
"""


def extract(geometry, sources, scales=None):
    """
    IN:  geometry, sources: list[SourceConfig], scales: dict[str, list[int]] optional
    OUT: (dict[str, ndarray], metadata: dict)
    """
    raise NotImplementedError
