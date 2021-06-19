from dataclasses import dataclass
from typing import List, Optional

from tuif.models.border import Border
from tuif.models.color import Color
from tuif.models.constraints import Constraint, Offset, RelativePosition


class Shape:
    """Base class for all shapes.

    :param fill: Fill-color of the shape
    :type fill: :class:`tuif.models.color.Color`
    :param border: Border of the shape
    :type border: :class:`tuif.models.border.Border`
    """

    def __init__(self, fill: Color, border: Border) -> None:
        self.fill = fill
        self.border = border

        # Default constraints
        self.constraints: List[Constraint] = [
            Offset(),
            RelativePosition(),
        ]


class Rectangle(Shape):
    """Class representing rectangles.

    :param width: Width in pixels
    :type width: int
    :param height: Height in pixels
    :type height: int
    :param fill: Fill-color of the shape
    :type fill: :class:`tuif.models.color.Color`, optional
    :param border: Border of the shape
    :type border: :class:`tuif.models.border.Border`, optional
    """

    def __init__(
        self,
        width: int,
        height: int,
        fill: Optional[Color],
        border: Optional[Border],
    ) -> None:
        """Constructor method."""
        super().__init__(fill, border)
        self.width = width
        self.height = height
