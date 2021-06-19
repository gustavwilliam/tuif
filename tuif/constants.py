from dataclasses import dataclass
import yaml


@dataclass
class Colors:
    white: int
    black: int
    red: int
    blue: int
    green: int


with open("constants.yaml", "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    colors = Colors(**data["colors"])
