"""
Description
-----------
This subpackage contains models and utilities for Earth's atmosphere.
It supports various atmospheric models used in orbital, re-entry, and climate simulations.

Modules
-------
- base: Base functions for atmospheric modeling.
- coesa62: COESA62 atmospheric model.
- coesa76: COESA76 atmospheric model.
- jacchia: Jacchia atmospheric model.
- util: Utility functions for atmospheric data processing.
- _jacchia: Internal routines for the Jacchia model.
- data: Atmospheric data files.
"""

from poliastro2.worldview.earth.atmosphere.coesa62 import COESA62
from poliastro2.worldview.earth.atmosphere.coesa76 import COESA76

__all__ = ["COESA62", "COESA76"]
