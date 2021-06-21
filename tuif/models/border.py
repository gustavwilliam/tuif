from dataclasses import dataclass

from tuif.models.color import Color


@dataclass
class Border:
    """Class for managing border objects.

    :param width: Width (in pixels), defaults to 1
    :type width: int, optional
    :param color: Color of the border, defaults to black
    :type color: :class:`tuif.models.color.Color`, optional
    :param border_radius: Border radius (in pixels), defaults to 0
    :type border_radius: int, optional
    """

    width: int = 1
    color: Color = Color("black")
    border_radius: int = 0
