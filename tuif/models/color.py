from dataclasses import dataclass


@dataclass
class Color:
    """Class for managing colors.

    :param hex: Hexadecimal color code
    :type hex: int
    """

    hex: int

    def __str__(self) -> str:
        """Returns hexadecimal string representation of the color.

        :return: Hexadecimal string representation of the color, such as "#FFD45A".
        :rtype: str
        """
        return f"#{self.hex[2:]}"
