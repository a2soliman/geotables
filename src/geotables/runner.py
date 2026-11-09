"""
geotables.runner

IN:  chunk-processing function + list of chunk ids
OUT: side effect -- every chunk processed and written somewhere

The chunk-processing core doesn't know or care how it gets invoked.
That's what makes this a thin, swappable layer: LocalRunner for
dev/CI, SLURMArrayRunner for the actual production target. See the
Orchestration section of ARCHITECTURE.md for why SLURM and not Dask.

Implements: issues #4 (LocalRunner), #9 (SLURMArrayRunner)
"""


class LocalRunner:
    """
    IN:  chunk_fn: Callable[[int], None], chunk_ids: list[int]
    OUT: None (runs chunk_fn over chunk_ids via multiprocessing)
    """

    def run(self, chunk_fn, chunk_ids):
        raise NotImplementedError


class SLURMArrayRunner:
    """
    IN:  chunk_fn: Callable[[int], None], chunk_ids: list[int], slurm config
    OUT: None (submits a SLURM job array, one task per chunk id)
    """

    def run(self, chunk_fn, chunk_ids):
        raise NotImplementedError
