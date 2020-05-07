from Color import *
from typing import Dict, List


class Player:
    default_player_names: List = ["Chrono", "Lucca", "Marle", "Magus", "Robo", "Ayla", "Frog"]
    current_players: Dict = {}
    _next_player_id: int = 1

    def __init__(self, name: str = None, color_name: str = None):
        # Parameters
        self.plid: int = Player.get_next_id()
        self.name: str = name or self.get_next_default_player_name()
        self.color: Color = PlayerColor.acquire_color(self, color_name)

        # Player tracking
        Player.current_players[name] = self

    def __str__(self):
        return f"{self.name} ({self.color})"

    def __repr__(self):
        return f"[Player {self.plid}, {str(self)}]"

    @classmethod
    def get_next_default_player_name(cls):
        if len(cls.default_player_names) == 0:
            raise Exception("No more player names available.")  # TODO: Find a more appropriate exception class
        return cls.default_player_names.pop()

    @classmethod
    def get_next_id(cls):
        this_id = cls._next_player_id
        cls._next_player_id += 1
        return this_id

    def list_players(self):
        print("--------------------------------------------")
        print(f"|  {self.plid}  |  {self.name}  |  {self.color}  |")


class PlayerColor(Color):
    """Extension/wrapper for Color that handles game-specific functionality."""
    all_colors: Dict = {}

    def __init__(self, full_name: str, rgb: str, abbreviation: str = ""):
        super().__init__(full_name, rgb, abbreviation)
        PlayerColor.all_colors[full_name] = self

        # Tracks whether the color is available vs already in use
        self.assigned_to_player = None  # As a backward reference, may cause problems with serialization

    def is_available(self) -> bool:
        """Is this color available for use now?"""
        return self.assigned_to_player is None

    @classmethod
    def get_available_colors(cls) -> List:
        """Returns a list of names of available colors."""
        return [k for k, v in cls.all_colors.items() if v.is_available()]

    @classmethod
    def acquire_color(cls, player: Player, color_name: str = None) -> "PlayerColor":
        """
        Gets an unused player color and marks it as used.
        :param player: The Player the color will be assigned to.
        :param color_name: Optional, the name of the color: "yellow"
        :return: A PlayerColor reference
        """
        avail_c = cls.get_available_colors()

        if len(avail_c) == 0:
            raise Exception(f"All {len(cls.all_colors)} colors are in use and none available.")

        # Default to next available if no color is specified
        if color_name is None:
            color_name = avail_c.pop()

        # Check if color exists and is available
        if color_name not in cls.all_colors:
            raise Exception(f"The color '{color_name}' has not been defined yet.")

        found_color = cls.all_colors[color_name]

        if not found_color.is_available():
            raise Exception(f"The color '{color_name}' is already in use by {found_color.assigned_to_player.name}.")

        # Mark color as used and return
        found_color.assigned_to_player = player
        return found_color

    @classmethod
    def build_player_colors(cls):
        cls("red", "d22")
        cls("blue", "22d")
        cls("yellow", "ff5", "ylw")
        cls("green", "2d2", "grn")
        cls("orange", "e80", "org")

