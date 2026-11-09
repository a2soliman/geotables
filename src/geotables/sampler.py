"""
geotables.sampler

IN:  raster source + grid params (tile_size, mode, overlap, count)
OUT: GeoDataFrame[geometry, sample_id]

Turns a raster's extent into candidate sample geometries. Does not
clip to raster bounds -- edge tiles may extend past them on purpose,
handled downstream by the extractor's boundless read (see extractor.py).

Implements: issue #1
"""


def regular_grid(source, tile_size, overlap=0.0):
    """
    IN:  raster source, tile_size (pixels, square), overlap (fraction)
    OUT: GeoDataFrame[geometry, sample_id]
    """
    raise NotImplementedError


def random_grid(source, tile_size, count):
    """
    IN:  raster source, tile_size (pixels, square), count
    OUT: GeoDataFrame[geometry, sample_id]
    """
    raise NotImplementedError
