from typing import List, Optional

from tuif.models.border import Border
from tuif.models.color import Color
from tuif.models.constraints import Constraint, Offset, RelativePosition


class Shape:
    """Base class for all shapes.

    :param bg_color: Fill-color of the shape, defaults to :class:`tuif.constants.colors.WHITE`
    :param border: Border of the shape, default to a border with width 0
    :type bg_color: :class:`tuif.models.color.Color`, optional
    :type border: :class:`tuif.models.border.Border`, optional

    .. note:: Non-default constraints can be set after the Shape object is created, but not during initialization
    """

    def __init__(
        self, bg_color: Color = Color("white"), border: Border = Border(width=0)
    ) -> None:
        """Constructor method."""
        self.bg_color = bg_color
        self.border = border

        # Default constraints
        self.constraints: List[Constraint] = [
            Offset(),
            RelativePosition(),
        ]


class Rectangle(Shape):
    """Class representing rectangles.

    :param width: Width in pixels
    :param height: Height in pixels
    :param bg_color: Fill-color of the shape
    :param border: Border of the shape
    :type width: int
    :type height: int
    :type bg_color: :class:`tuif.models.color.Color`, optional
    :type border: :class:`tuif.models.border.Border`, optional

    .. note:: Default values for :param:`bg_color` and :param:`border` are the default values for new :class:`tuif.models.shape.Shape` objects
    .. warning:: Currently both :param:`bg_color` and :param:`border` need to be set for either of them to be set as non-default
    """

    def __init__(
        self,
        width: int,
        height: int,
        bg_color: Optional[Color] = None,
        border: Optional[Border] = None,
    ) -> None:
        """Constructor method."""
        if bg_color and border:
            super().__init__(bg_color, border)
        else:
            super().__init__()

        self.width = width
        self.height = height
