from typing import List, Optional, Tuple
from tuif.models.color import Color
from tuif.models.shape import Shape


class Canvas:
    def __init__(
        self, *objects: Tuple[Shape], background_color: Optional[Color] = None
    ) -> None:
        self.background_color = background_color
        self.objects: List[Shape] = list(objects)

    def add(self, object_: Shape) -> None:
        """Adds the provided object to the top of the canvas.

        :param object_: Object/shape to add to the canvas
        :type object_: :class:`tuif.models.shape.Shape`
        """
        self.objects.append(object_)

    def insert(self, object_: Shape, index: int) -> None:
        """Adds the provided object to the top of the canvas.

        :param object_: Object/shape to add to the canvas
        :type object_: :class:`tuif.models.shape.Shape`
        :param index: Index for where in the canvas the object should be inserted. 0 is the very top of the canvas
        :type index: int
        """
        self.objects.insert(index, object_)
