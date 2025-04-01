"""
Description
-----------
This subpackage implements various orbit propagation algorithms. It contains
different numerical methods for propagating orbits under various assumptions.

Modules
-------
- cowell: Implementation of the Cowell propagation method.
- danby: Danby's propagation method.
- enums: Enumerations for propagation options.
- farnocchia: Farnocchia propagation routine.
- gooding: Gooding's method for orbit propagation.
- markley: Markley's propagation technique.
- mikkola: Mikkola's method.
- pimienta: Pimienta's propagation routines.
- recseries: Recursive series propagation.
- vallado: Propagation method based on Vallad's work.
- _compat: Compatibility routines.

Propagators capabilities available at poliastro2:

+-------------+------------+-----------------+-----------------+
|  Propagator | Elliptical |    Parabolic    |    Hyperbolic   |
+-------------+------------+-----------------+-----------------+
|  farnocchia |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|   vallado   |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|   mikkola   |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|   markley   |      ✓     |        x        |        x        |
+-------------+------------+-----------------+-----------------+
|   pimienta  |      ✓     |        ✓        |        x        |
+-------------+------------+-----------------+-----------------+
|   gooding   |      ✓     |        x        |        x        |
+-------------+------------+-----------------+-----------------+
|    danby    |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|    cowell   |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|  recseries  |      ✓     |        x        |        x        |
+-------------+------------+-----------------+-----------------+

"""

from poliastro2.core.actions.propagate.cowell import CowellPropagator
from poliastro2.core.actions.propagate.danby import DanbyPropagator
from poliastro2.core.actions.propagate.enums import PropagatorKind
from poliastro2.core.actions.propagate.farnocchia import FarnocchiaPropagator
from poliastro2.core.actions.propagate.gooding import GoodingPropagator
from poliastro2.core.actions.propagate.markley import MarkleyPropagator
from poliastro2.core.actions.propagate.mikkola import MikkolaPropagator
from poliastro2.core.actions.propagate.pimienta import PimientaPropagator
from poliastro2.core.actions.propagate.recseries import RecseriesPropagator
from poliastro2.core.actions.propagate.vallado import ValladoPropagator

from ._compat import propagate

ALL_PROPAGATORS = [
    CowellPropagator,
    DanbyPropagator,
    FarnocchiaPropagator,
    GoodingPropagator,
    MarkleyPropagator,
    MikkolaPropagator,
    PimientaPropagator,
    RecseriesPropagator,
    ValladoPropagator,
]
ELLIPTIC_PROPAGATORS = [
    propagator
    for propagator in ALL_PROPAGATORS
    if propagator.kind & PropagatorKind.ELLIPTIC
]
PARABOLIC_PROPAGATORS = [
    propagator
    for propagator in ALL_PROPAGATORS
    if propagator.kind & PropagatorKind.PARABOLIC
]
HYPERBOLIC_PROPAGATORS = [
    propagator
    for propagator in ALL_PROPAGATORS
    if propagator.kind & PropagatorKind.HYPERBOLIC
]


__all__ = [item.__name__ for item in ALL_PROPAGATORS] + ["propagate"]
