from Player import Player, PlayerColor
from typing import List, Any

class Cell:
    """
    A single cell from the board. Position is listed as 0,0.
    """

    def __init__(self, x_pos: int, y_pos: int, contents: Any = None):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.contents = contents

    def is_occupied(self) -> bool:
        if contents == None:
            return True
        else:
            return False
