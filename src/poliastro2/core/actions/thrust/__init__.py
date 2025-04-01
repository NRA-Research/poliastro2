"""
Description
-----------
This subpackage contains routines related to thrust-based orbital maneuvers.

Modules
-------
- change_argp: Routines for changing the argument of perigee.
- change_a_inc: Maneuvers to adjust semi-major axis and inclination.
- change_ecc_inc: Combined adjustments for eccentricity and inclination.
- change_ecc_quasioptimal: Quasi-optimal thrust maneuvers for eccentricity modifications.
"""

from poliastro2.core.actions.thrust.change_a_inc import change_a_inc
from poliastro2.core.actions.thrust.change_argp import change_argp
from poliastro2.core.actions.thrust.change_ecc_inc import change_ecc_inc
from poliastro2.core.actions.thrust.change_ecc_quasioptimal import (
    change_ecc_quasioptimal,
)

__all__ = [
    "change_a_inc",
    "change_argp",
    "change_ecc_quasioptimal",
    "change_ecc_inc",
]
