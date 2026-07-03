from typing import Optional
from image import Camera


from chalk.modern.chalkcolor import ChalkColor


class Pixel:
    def __init__(self, character: str = " ", color: Optional[Color] = None) -> None:
        self.character = character
        self.chalkcolor = chalkcolor

    @property
    def ansi_string(self) -> str:
        if not self.chalkcolor:
            return self.character

        return self.chalkcolor.ansi + self.character + self.chalkcolor.colorama_type.RESET
