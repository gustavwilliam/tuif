import yaml

from tuif.models.color import Color


class Colors:
    def __init__(
        self,
        white: int,
        black: int,
        red: int,
        blue: int,
        green: int,
    ) -> None:
        self.white = Color(hex(white))
        self.black = Color(hex(black))
        self.red = Color(hex(red))
        self.blue = Color(hex(blue))
        self.green = Color(hex(green))


with open("constants.yaml", "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    colors = Colors(**data["colors"])
