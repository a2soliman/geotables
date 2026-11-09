"""
geotables.writer

IN:  iterable of (arrays: dict[str, ndarray], metadata: dict), chunk_id, output_dir
OUT: one GeoParquet file per chunk at output_dir/chunk_{id}.parquet

Idempotent and keyed by chunk_id: re-running a chunk overwrites
cleanly rather than appending or duplicating rows. This property is
what makes SLURM-array resumability (runner.py) work without any
extra retry logic.

Implements: issue #3
"""


def write_chunk(chips, chunk_id, output_dir):
    """
    IN:  chips: Iterable[(dict[str, ndarray], dict)], chunk_id: int, output_dir: str
    OUT: path to the written GeoParquet file
    """
    raise NotImplementedError
