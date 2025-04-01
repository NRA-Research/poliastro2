"""
Description
-----------
This subpackage focuses on plotting routines specifically for orbital data.
It provides utilities to visualize orbits and related parameters.

Modules
-------
- plotter: Functions for plotting orbital trajectories.
- backends: Subpackage collecting all support orbit plotter backends.
"""


from poliastro2.plotting.orbit.plotter import OrbitPlotter

__all__ = ["OrbitPlotter"]
