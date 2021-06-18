from dataclasses import dataclass


@dataclass
class Color:
    """Class for managing colors.

    Args:
        hex (str): Hexadecimal value of the color, without a leading "#".
    """
    hex: str
