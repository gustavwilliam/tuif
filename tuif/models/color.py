from dataclasses import dataclass


@dataclass
class Color:
    """Class for managing colors.

    Args:
        hex (int): Hexadecimal value of the color.
    """
    hex: int
