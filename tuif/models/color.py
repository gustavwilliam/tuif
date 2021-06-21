import colorama


class Color:
    """Class for managing colors.

    :param name: ANSI name of the color. Only accepts valid ANSI color names that are supported by colorama
    :param type_: The type of color (foreground or background). Accepts "Fore" for foreground and "Back" for background, defaults to "Back"
    :type name: str
    :type type_: str
    :raises ValueError: :param:`type_` is not a valid color type. Only "Fore" and "Back" are valid
    :raises ValueError: :param:`name` is not a valid ANSI color name.

    :Example:

    >>> from tuif.models.color import Color
    >>> white = Color("white")
    >>> white.ansi
    '\\x1b[47m'

    >>> from tuif.models.color import Color
    >>> red_fg = Color("red", "Fore")
    >>> str(red_fg)
    'red'

    .. note:: :param:`name` will be converted to uppercase by the constructor method. The `name` attribute is always uppercase, even if the provided `name` parameter is lowercase
    """

    def __init__(self, name: str, type_: str = "Back") -> None:
        """Constructor method."""
        if type_ not in ["Fore", "Back"]:
            raise ValueError(
                f"'{type_}' is not a valid color type. Accepts 'Fore' and 'Back' as arguments."
            )
        self.type_ = type_
        self.colorama_type: colorama.AnsiCodes = getattr(colorama, self.type_)

        ANSI_NAMES = list(vars(self.colorama_type).keys())
        name = name.upper()  # Colorama color names are all uppercase.
        if name not in ANSI_NAMES:
            raise ValueError(
                f"'{name}' is not a valid ANSI color name. Please select one of the following: {ANSI_NAMES}"
            )
        self.name = name
        self.ansi = getattr(self.colorama_type, self.name)

    def __str__(self) -> str:
        """Returns a lowercase string representation of the color.

        :return: String representation of the color, such as "white" or "red".
        :rtype: str

        :Example:

        >>> from tuif.models.color import Color
        >>> blue_fg = Color("blue", "Fore")
        >>> str(blue_fg)
        'blue'
        """
        return self.name.lower()
