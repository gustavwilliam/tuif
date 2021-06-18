from dataclasses import dataclass

from tuif.models.border import Border
from tuif.models.color import Color


@dataclass
class Shape:
    fill: Color
    border: Border
