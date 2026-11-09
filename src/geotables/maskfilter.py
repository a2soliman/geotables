"""
geotables.maskfilter

IN:  candidate GeoDataFrame + mask source (raster class map or vector layer) + target class(es) + coverage rule
OUT: filtered GeoDataFrame

Cheap pre-pass: reads only the mask for each candidate, drops samples
that don't meet the class/coverage criterion, before the much more
expensive multi-source extraction runs on what's left.

Implements: issue #5
"""


def filter_by_class(candidates, mask_source, target_classes, coverage_rule="majority"):
    """
    IN:  candidates: GeoDataFrame, mask_source, target_classes: list, coverage_rule: str
    OUT: GeoDataFrame (filtered subset of candidates)
    """
    raise NotImplementedError
