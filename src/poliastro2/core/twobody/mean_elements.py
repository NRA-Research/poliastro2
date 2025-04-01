from astropy import units as u
from astropy.coordinates.solar_system import PLAN94_BODY_NAME_TO_PLANET_INDEX
import erfa

from poliastro2.core.frames import Planes
from poliastro2.core.twobody.states import RVState
from poliastro2.worldview.solar_sys.constants import J2000


def get_mean_elements(body, epoch=J2000) -> RVState:
    """Get the ecliptic mean elements of a solar system body.

    Parameters
    ----------
    body : ~poliastro.bodies.SolarSystemPlanet
        The celestial body for which to obtain mean elements.
    epoch : astropy.time.Time, optional
        The epoch at which to compute the mean elements, by default J2000.

    Returns
    -------
    RVState
        The state defined by position and velocity vectors of the body at the given epoch.

    Raises
    ------
    ValueError
        If the body is not an instance of `poliastro.bodies.SolarSystemPlanet`.
    """
    try:
        name = body.name.lower()
        if name == "earth":
            name = "earth-moon-barycenter"

        body_index = PLAN94_BODY_NAME_TO_PLANET_INDEX[name]
        body_pv_helio = erfa.plan94(epoch.jd1, epoch.jd2, body_index)

        r = body_pv_helio["p"] * u.au
        v = body_pv_helio["v"] * u.au / u.day

    except KeyError as e:
        raise ValueError(
            f"No available mean elements for {body}. It must be an instance of `poliastro.bodies.SolarSystemPlanet`"
        ) from e

    return RVState(body.parent, (r, v), plane=Planes.EARTH_ECLIPTIC).to_classical()
