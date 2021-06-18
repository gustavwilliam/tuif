from tuif.models.color import Color
from dataclasses import dataclass


@dataclass
class Border:
    width: int
    color: Color
    border_radius: int = 0
