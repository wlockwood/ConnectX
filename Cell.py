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
        if self.contents is None:
            return False
        else:
            return True

    def get_board_representation(self) -> str:
        # If empty return what an empty cell looks like

        # Otherwise, have the occupant decide how it wants to be displayed
        if self.is_occupied():
            return self.contents.get_board_representation()
        else:
            return "___"

    def __repr__(self) -> str:
        return f"Cell({self.x_pos},{self.y_pos}: {self.contents})"



if __name__ == "__main__":
    test_cell = Cell(0,0)
    print(type(test_cell))
    print(type(test_cell.is_occupied))
