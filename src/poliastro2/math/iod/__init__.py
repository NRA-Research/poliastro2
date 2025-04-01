"""
Description
-----------
This subpackage provides methods on initial orbit determination (IOD). It offers
tools for calculating the initial orbit of a celestial body based on observational data.

Modules
-------
- base_iod: Base functions for initial orbit determination.
- izzo: IOD routines based on Izzo's method.
- vallado: IOD routines based on Vallado's approach.

Notes
-----
The default method solves the Lambert problem using the Izzo algorithm.
"""

# Select default algorithm
from poliastro2.math.iod.izzo import lambert

__all__ = ["lambert"]
