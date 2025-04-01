"""
Description
-----------
This internal subpackage implements low-level routines for thrust maneuvers.

Modules
-------
- change_argp: Internal routines for changing the argument of perigee.
- change_a_inc: Internal implementations for modifying semi-major axis and inclination.
- change_ecc_inc: Internal routines for combined eccentricity and inclination adjustments.
- change_ecc_quasioptimal: Internal quasi-optimal methods for eccentricity change.
"""

from poliastro2.math.thrust.change_argp import change_argp

__all__ = ["change_a_inc", "change_argp", "change_ecc_inc"]
