from typing import Optional

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

    :param relative: Shape to offset relative to
    :type relative: :class:`tuif.models.shape.Shape`, optional
    :param top: Offset (in pixels) applied to the top of the object, defaults to 0
    :type top: int, optional
    :param right: Offset (in pixels) applied to the right of the object, defaults to 0
    :type right: int, optional
    :param bottom: Offset (in pixels) applied to the bottom of the object, defaults to 0
    :type bottom: int, optional
    :param left: Offset (in pixels) applied to the left of the object, defaults to 0
    :type left: int, optional
    """

    def __init__(
        self,
        relative: Optional[Shape] = None,
        top: int = 0,
        right: int = 0,
        bottom: int = 0,
        left: int = 0,
    ) -> None:
        """Constructor method."""
        super().__init__(relative)
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left


# endregion: Offset

# region: Position
class Position(Constraint):
    """Base class for constraints to position objects relative to others.

    :param relative: Shape to position relative to
    :type relative: :class:`tuif.models.shape.Shape`, optional
    """

    def __init__(self, relative: Optional[Shape]) -> None:
        """Constructor method."""
        super().__init__(relative)


class RelativePosition(Position):
    """Constraint for positioning the object according to the natural flow of the canvas. :class:`tuif.models.constraints.Offset` will affect the position of the object.

    :param relative: Shape to position relative to
    :type relative: :class:`tuif.models.shape.Shape`, optional
    """

    def __init__(self, relative: Optional[Shape]) -> None:
        """Constructor method."""
        super().__init__(relative)


class StaticPosition(Position):
    """Constraint for positioning the object according to the natural flow of the canvas. :class:`tuif.models.constraints.Offset` will not affect the position of the object.

    :param relative: Shape to position relative to
    :type relative: :class:`tuif.models.shape.Shape`, optional
    """

    def __init__(self, relative: Optional[Shape]) -> None:
        """Constructor method."""
        super().__init__(relative)


class AbsolutePosition(Position):
    """Constraint for positioning the object regardless of the rest of the state of the canvas. :class:`tuif.models.constraints.Offset` will affect the position of the object.

    :param relative: Shape to position relative to
    :type relative: :class:`tuif.models.shape.Shape`, optional
    """

    def __init__(self, relative: Optional[Shape]) -> None:
        """Constructor method."""
        super().__init__(relative)


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
    :type relative: :class:`tuif.models.shape.Shape`
    :param offset: Offset (in pixels) relative to the object specified in `relative`, defaults to 0
    :type offset: int, optional
    """

    def __init__(self, relative: Shape, offset: int = 0) -> None:
        """Constructor method."""
        super().__init__(relative, offset)


class CenterYConstraint(CenterConstraint):
    """Constraint for centering objects on the Y-axis.

    :param relative: Shape to center relative to
    :type relative: :class:`tuif.models.shape.Shape`
    :param offset: Offset (in pixels) relative to the object specified in `relative`, defaults to 0
    :type offset: int, optional
    """

    def __init__(self, relative: Shape, offset: int = 0) -> None:
        """Constructor method."""
        super().__init__(relative, offset)


# endregion: Center
