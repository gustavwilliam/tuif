from dataclasses import dataclass

from tuif.constants import colors
from tuif.models.color import Color


@dataclass
class Border:
    """Class for managing border objects.

    :param width: Width, in pixels
    :type width: int
    :param color: Color of the border
    :type color: :class:`tuif.models.color.Color`
    :param border_radius: Border radius, in pixels
    :type border_raduys: int
    """

    width: int = 1
    color: Color = colors.black
    border_radius: int = 0
