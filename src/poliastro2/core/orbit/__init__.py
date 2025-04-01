"""
Description
-----------
This subpackage provides functions to create and manipulate orbital models.
It includes routines for orbit creation and scalar computations.

Modules
-------
- creation: Functions for creating orbital states.
- scalar: Class for representing the orbit of a body with respect to an attractor.
"""

from poliastro2.core.orbit.scalar import Orbit

__all__ = ["Orbit"]
