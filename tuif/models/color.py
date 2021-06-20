import colorama


class Color:
    """Class for managing colors.

    :param name: ANSI name of the color. Only accepts valid ANSI color names that are supported by colorama
    :type name: str
    :param type_: The type of color (foreground or background). Accepts "Fore" for foreground and "Back" for background, defaults to "Back"
    :type type_: str
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
        """
        return self.name.lower()
