from dataclasses import dataclass

from tuif.models.border import Border
from tuif.models.color import Color


@dataclass
class Shape:
    """Base class for all shapes.

    Args:
        fill (Color): Fill-color.
        border (Border): Border.
    """
    fill: Color
    border: Border


@dataclass
class Rectangle(Shape):
    """Class representing rectangles.

    Args:
        Shape: Base class for the shape
            fill (str): Fill-color.
            border (Border): Border.
        width (int): Width in pixels.
        height (int): Height in pixels.
    """
    width: int
    height: int
