""" Subpackage for loading tracking data into memory

This subpackage contains functions for loading ground
truth or tracking method outputs into memory as TrackingGraph objects.
Each loading function must return one TrackingGraph object which has a
track graph and optionally contains a corresponding segmentation.
"""

from ._ctc import (
    _check_ctc,
    _get_node_attributes,
    _load_tiffs,
    load_ctc_data,
    load_deepcell_data,
    load_graph_masks,
)

__all__ = [
    "load_ctc_data",
    "load_graph_masks",
    "load_deepcell_data",
    "_check_ctc",
    "_load_tiffs",
    "_get_node_attributes",
]
