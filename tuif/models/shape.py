from dataclasses import dataclass

from tuif.models.border import Border
from tuif.models.color import Color


@dataclass
class Shape:
    """Base class for all shapes.

    :param fill: Fill-color of the shape
    :type fill: :class:`tuif.models.color.Color`
    :param border: Border of the shape
    :type border: :class:`tuif.models.border.Border`
    """

    fill: Color
    border: Border


@dataclass
class Rectangle(Shape):
    """Object representing rectangles.

    :param fill: Fill-color of the shape
    :type fill: :class:`tuif.models.color.Color`
    :param border: Border of the shape
    :type border: :class:`tuif.models.border.Border`
    :param width: Width in pixels
    :type width: int
    :param height: Height in pixels
    :type height: Height in pixels
    """

    width: int
    height: int
