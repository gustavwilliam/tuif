from typing import TYPE_CHECKING, Optional

from tuif.models.shape import Shape

if TYPE_CHECKING:
    from tuif.models.shape import Shape


class Constraint:
    """Base class for all constraints. All constraints inherent from this class.

    :param relative: Shape to apply the constraint relative to
    :type relative: :class:`tuif.models.shape.Shape`, optional
    """

    def __init__(self, relative: Optional[Shape] = None) -> None:
        """Constructor method."""
        self.relative = relative


# region: Offset
class Offset(Constraint):
    """Constrint to offset the object relative to where it would naturally go. Will not be applied if :class:`tuif.models.constraints.StaticPosition` is active.

    :param top: Offset (in pixels) applied to the top of the object, defaults to 0
    :param right: Offset (in pixels) applied to the right of the object, defaults to 0
    :param bottom: Offset (in pixels) applied to the bottom of the object, defaults to 0
    :param left: Offset (in pixels) applied to the left of the object, defaults to 0
    :type top: int, optional
    :type right: int, optional
    :type bottom: int, optional
    :type left: int, optional
    """

    def __init__(
        self,
        top: int = 0,
        right: int = 0,
        bottom: int = 0,
        left: int = 0,
    ) -> None:
        """Constructor method."""
        super().__init__()
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left


# endregion: Offset

# region: Position
class Position(Constraint):
    """Base class for constraints to position objects relative to others."""

    def __init__(self) -> None:
        """Constructor method."""
        super().__init__()


class RelativePosition(Position):
    """Constraint for positioning the object according to the natural flow of the canvas. :class:`tuif.models.constraints.Offset` will affect the position of the object. The position of the other elements on the canvas will not be changed by the offset of the object."""

    def __init__(self) -> None:
        """Constructor method."""
        super().__init__()


class StaticPosition(Position):
    """Constraint for positioning the object according to the natural flow of the canvas. :class:`tuif.models.constraints.Offset` will not affect the position of the object. The position of the other elements on the canvas will be changed by the offset of the object."""

    def __init__(self) -> None:
        """Constructor method."""
        super().__init__()


class AbsolutePosition(Position):
    """Constraint for positioning the object regardless of the rest of the state of the canvas. :class:`tuif.models.constraints.Offset` will affect the position of the object. The position of the other elements on the canvas will not be changed by the offset of the object."""

    def __init__(self) -> None:
        """Constructor method."""
        super().__init__()


# endregion: Position

# region: Center
class CenterConstraint(Constraint):
    """Base class for constraints to center objects.

    :param relative: Shape to center relative to
    :type relative: :class:`tuif.models.shape.Shape`
    :param offset: Offset (in pixels) relative to the object specified in `relative`, defaults to 0
    :type offset: int, optional
    """

    def __init__(self, relative: Shape, offset: int = 0) -> None:
        """Constructor method."""
        super().__init__(relative)
        self.offset = offset


class CenterXConstraint(CenterConstraint):
    """Constraint for centering objects on the X-axis.

    :param relative: Shape to center relative to
    :param offset: Offset (in pixels) relative to the object specified in `relative`, defaults to 0
    :type relative: :class:`tuif.models.shape.Shape`
    :type offset: int, optional
    """

    def __init__(self, relative: Shape, offset: int = 0) -> None:
        """Constructor method."""
        super().__init__(relative, offset)


class CenterYConstraint(CenterConstraint):
    """Constraint for centering objects on the Y-axis.

    :param relative: Shape to center relative to
    :param offset: Offset (in pixels) relative to the object specified in `relative`, defaults to 0
    :type relative: :class:`tuif.models.shape.Shape`
    :type offset: int, optional
    """

    def __init__(self, relative: Shape, offset: int = 0) -> None:
        """Constructor method."""
        super().__init__(relative, offset)


# endregion: Center
