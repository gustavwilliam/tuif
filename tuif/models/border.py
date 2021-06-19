from dataclasses import dataclass

from tuif.constants import colors
from tuif.models.color import Color


@dataclass
class Border:
    """Class for border objects.

    Keeps track of attributes of borders.

    Args:
        width (int): Width in pixels.
        color (Color): Color, as a color object.
        border_radius (int): Border radius in pixels.
    """

    width: int = 1
    color: Color = colors.black
    border_radius: int = 0
