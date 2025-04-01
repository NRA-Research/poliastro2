"""
Description
-----------
This subpackage provides plotting utilities specifically for Earth-based visualizations,
including ground tracks and atmospheric data representations.

Modules
-------
- groundtrack: Functions for plotting ground track diagrams.
- utils: Helper functions for Earth plotting.
"""


from poliastro2.worldview.earth.plotting.groundtrack import GroundtrackPlotter

__all__ = ["GroundtrackPlotter"]
