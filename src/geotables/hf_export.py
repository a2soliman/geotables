"""
geotables.hf_export

IN:  GeoParquet dataset dir
OUT: Hugging Face datasets.Dataset on disk + an auto-generated dataset card (+ optional hub push)

Dataset card metadata (bbox, CRS, resolution, sample count, sampling
method, source license) is close to free here since it's already
captured as chip provenance during extraction -- most geospatial
datasets on the Hub are missing exactly this.

Implements: issue #10
"""


def to_hf(geoparquet_dir, output_dir, push_to_hub=None):
    """
    IN:  geoparquet_dir: str, output_dir: str, push_to_hub: str | None
    OUT: path to the written HF dataset directory
    """
    raise NotImplementedError
