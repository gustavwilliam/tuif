from typing import List, Optional, Tuple

from tuif.models.color import Color
from tuif.models.shape import Shape


class Canvas:
    def __init__(
        self, *objects: Tuple[Shape], bg_color: Optional[Color] = None
    ) -> None:
        self.bg_color = bg_color
        self.objects: List[Shape] = list(objects)

    def add(self, object_: Shape) -> None:
        """Adds the provided object to the top of the canvas.

        :param object_: Object/shape to add to the canvas
        :type object_: :class:`tuif.models.shape.Shape`
        """
        self.objects.append(object_)

    def insert(self, object_: Shape, index: int) -> None:
        """Adds the provided object to the specified index of the canvas.

        :param object_: Object/shape to add to the canvas
        :param index: Index for where in the canvas the object should be inserted. 0 is the very top of the canvas
        :type object_: :class:`tuif.models.shape.Shape`
        :type index: int
        """
        self.objects.insert(index, object_)

    # @property
    # def frame(self) -> List[List[Optional[Color]]]:
    #     """
    #     [
    #         [None, Color, Color, Color, Color, Color, Color],
    #         [None, Color, None, None, Color, None, Color],
    #         [Color, Color, Color, Color, Color, Color, Color],
    #         [None, Color, None, None, Color, None, Color],
    #     ]
    #     """
