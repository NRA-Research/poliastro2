"""Circular Restricted 3-Body Problem (CR3BP).

Includes the computation of Lagrange points
"""

from astropy import units as u
import numpy as np

from poliastro2.math.optimize import brentq
from poliastro2.util import norm
from poliastro2.math.threebody import restricted

@u.quantity_input(r12=u.km, m1=u.kg, m2=u.kg)
def lagrange_points(r12, m1, m2):
    """Computes the Lagrangian points of CR3BP.

    Computes the Lagrangian points of CR3BP given the distance between two
    bodies and their masses.
    It uses the formulation found in Eq. (2.204) of Curtis, Howard. 'Orbital
    mechanics for engineering students'. Elsevier, 3rd Edition.

    Parameters
    ----------
    r12 : ~astropy.units.Quantity
        Distance between the two bodies
    m1 : ~astropy.units.Quantity
        Mass of the main body
    m2 : ~astropy.units.Quantity
        Mass of the secondary body

    Returns
    -------
    ~astropy.units.Quantity
        Distance of the Lagrangian points to the main body,
        projected on the axis main body - secondary body
    """

    return restricted.lagrange_points(r12, m1, m2)


@u.quantity_input(m1=u.kg, r1=u.km, m2=u.kg, r2=u.km, n=u.one)
def lagrange_points_vec(m1, r1, m2, r2, n):
    """Computes the five Lagrange points in the CR3BP.

    Returns the positions in the same frame of reference as `r1` and `r2`
    for the five Lagrangian points.

    Parameters
    ----------
    m1 : ~astropy.units.Quantity
        Mass of the main body. This body is the one with the biggest mass.
    r1 : ~astropy.units.Quantity
        Position of the main body.
    m2 : ~astropy.units.Quantity
        Mass of the secondary body.
    r2 : ~astropy.units.Quantity
        Position of the secondary body.
    n : ~astropy.units.Quantity
        Normal vector to the orbital plane.

    Returns
    -------
    list:
        Position of the Lagrange points: [L1, L2, L3, L4, L5]
        The positions are of type ~astropy.units.Quantity
    """

    return restricted.lagrange_points_vec(m1, r1, m2, r2, n)
