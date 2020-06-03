from Player import Player, PlayerColor
from typing import List, Any

class Cell:
    """
    A single cell from the board. position is listed as 0,0.
    """

    def __init__(self, x_pos: int, y_pos: int, contents: Any = None):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.contents = contents

    @staticmethod
    def check_for_win(self):
        pass


    def print_board(self):
        pass

    def print_board_color(self):
        pass    

    def can_continue(self)
        pass


"""
TODO: Board class
Fields / Properties:
    x/y size of board
    board columns
Actions:
    check_for_win(self) -> winning Player - Has someone won
    print_board(self) -> None - Show the board
    print_board_with_color(self) -> None - Show the board with pretty colored dots
    can_continue(self) -> bool - Whether the game can continue. For now, check if full.



""" 

