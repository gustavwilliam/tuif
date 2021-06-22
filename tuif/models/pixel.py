from typing import Optional

from tuif.models.color import Color


class Pixel:
    def __init__(self, character: str = " ", color: Optional[Color] = None) -> None:
        self.character = character
        self.color = color

    @property
    def ansi_string(self) -> str:
        if not self.color:
            return self.character

        return self.color.ansi + self.character + self.color.colorama_type.RESET
