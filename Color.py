class Color:
    """Color and only things related to the color itself."""

    color_list = {}  # Color-tracking dictionary

    abbreviation_length = 3

    def __init__(self, full_name: str, color_code: str, abbreviation: str = None):
        """
        :param full_name: Full name of a color: "Yellow"
        :param color_code: ANSI control code for this color
        :param abbreviation: Short name of a color: "yel"
        """

        # Assign parameters
        self.color_name = full_name
        self.abbreviation = abbreviation or full_name[:Color.abbreviation_length]
        self.color_code = color_code

        # Other fields
        Color.color_list[full_name] = self

    def __str__(self):
        return self.color_name

    def __repr__(self):
        return "(Color) " + self.color_name

