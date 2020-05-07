class Color:
    """Color and only things related to the color itself."""

    color_list = {}  # Color-tracking dictionary

    abbreviation_length = 3

    def __init__(self, full_name: str, rgb: str, abbreviation: str = None):
        """
        :param full_name: Full name of a color: "Yellow"
        :param rgb: 3-digit Hex RGB color code: "fff"
        :param abbreviation: Short name of a color: "yel"
        """

        # Assign parameters
        self.color_name = full_name
        self.abbreviation = abbreviation or full_name[:Color.abbreviation_length]  # *Should* be three letters...
        self.rgb = rgb

        # Other fields
        Color.color_list[full_name] = self

    def __str__(self):
        return self.color_name

    def __repr__(self):
        return "(Color) " + self.color_name
