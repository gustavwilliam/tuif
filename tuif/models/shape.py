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
