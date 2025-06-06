import sys

from astropy import units as u

from poliastro2.core.actions.propagate.enums import PropagatorKind
from poliastro2.core.twobody.states import ClassicalState
from poliastro2.math.propagation import recseries_coe as recseries_fast

from ._compat import OldPropagatorModule

sys.modules[__name__].__class__ = OldPropagatorModule


class RecseriesPropagator:
    """Kepler solver for elliptical orbits with recursive series approximation method.

    The order of the series is a user defined parameter.

    Notes
    -----
    This algorithm uses series discussed in the paper *Recursive solution to
    Kepler's problem for elliptical orbits - application in robust
    Newton-Raphson and co-planar closest approach estimation*
    with DOI: http://dx.doi.org/10.13140/RG.2.2.18578.58563/1
    """

    kind = PropagatorKind.ELLIPTIC

    def __init__(
        self,
        method="rtol",
        order=8,
        numiter=100,
        rtol=1e-8,
    ):
        self._method = method
        self._order = order
        self._numiter = numiter
        self._rtol = rtol

    def propagate(self, state, tof):
        state = state.to_classical()

        nu = (
            recseries_fast(
                state.attractor.k.to_value(u.km**3 / u.s**2),
                *state.to_value(),
                tof.to_value(u.s),
                method=self._method,
                order=self._order,
                numiter=self._numiter,
                rtol=self._rtol,
            )
            << u.rad
        )

        new_state = ClassicalState(
            state.attractor, state.to_tuple()[:5] + (nu,), state.plane
        )
        return new_state
