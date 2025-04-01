"""
Description
-----------
This subpackage provides definitions and utilities for coordinate frames used
in orbital mechanics. It supports various reference frames and transformations.

Modules
-------
- ecliptic: Ecliptic coordinate frame definitions.
- enums: Coordinate frames definitions
- equatorial: Utilities for the equatorial frame.
- fixed: Fixed coordinate frame routines for solar system bodies.
- util: Helper functions for frame transformations.
"""

from poliastro2.core.frames.enums import Planes

__all__ = [
    "Planes",
]
