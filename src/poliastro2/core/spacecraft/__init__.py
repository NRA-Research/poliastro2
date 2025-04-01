"""
Description
-----------
A module to represent a spacecraft with properties, and manipulation/calculation methods.

"""

from astropy import units as u


class Spacecraft:
    """A class to represent a spacecraft with properties for area, drag coefficient, and
    mass. It includes methods to access these properties and calculate the ballistic
    coefficient, which is a measure of the spacecraft's aerodynamic efficiency.

    Attributes
    ----------
    A : ~astropy.units.Quantity
        Area of the spacecraft (km^2).
    C_D : ~astropy.units.Quantity
        Dimensionless drag coefficient.
    m : ~astropy.units.Quantity
        Mass of the spacecraft (kg).
    metadata : dict
        Optional metadata for the spacecraft.
    """

    @u.quantity_input(A=u.km**2, C_D=u.one, m=u.kg)
    def __init__(self, A, C_D, m, **metadata):
        """Initialize a Spacecraft instance.

        Parameters
        ----------
        A : ~astropy.units.Quantity
            Area of the spacecraft (km^2).
        C_D : ~astropy.units.Quantity
            Dimensionless drag coefficient.
        m : ~astropy.units.Quantity
            Mass of the spacecraft (kg).
        **metadata : dict, optional
            Additional metadata for the spacecraft.
        """
        self._A = A
        self._C_D = C_D
        self._m = m
        self._metadata = metadata

    @property
    def A(self):
        """Area of the spacecraft (km^2)."""
        return self._A

    @property
    def C_D(self):
        """Drag coefficient (dimensionless)."""
        return self._C_D

    @property
    def m(self):
        """Mass of the spacecraft (kg)."""
        return self._m

    @property
    def ballistic_coefficient(self):
        r"""Calculate the ballistic coefficient (km^2/kg).

        Returns
        -------
        ~astropy.units.Quantity
            Ballistic coefficient (km^2/kg).

        Notes
        -----
        Be aware that you may encounter alternative definitions of the ballistic
        coefficient, such as the reciprocal:

        .. math::

            \frac{m}{C_D A}
        """
        return self._C_D * (self._A / self._m)
