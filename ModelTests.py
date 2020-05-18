import Color
from Player import Player, PlayerColor
from Board import Board

"""
This file is a throwaway intended for doing standalone testing of other modules.


PlayerColor.build_player_colors()
print("Available colors: ", PlayerColor.get_available_colors())

print()
print("A player")
a_player = Player()
print(a_player)

print()
print("B player")
b_player = Player("Will")
print(b_player)

print()
c_player_chosen_color = PlayerColor.get_available_colors()[0]
print("C player")
c_player = Player(color_name=c_player_chosen_color)
print(c_player)

print()
d_player_chosen_color = PlayerColor.get_available_colors()[0]
print("D player")
d_player = Player("Fred", color_name=d_player_chosen_color)
print(d_player)

print()
print("Available colors: ", PlayerColor.get_available_colors())
"""
b = Board.create_board(8,8)
Board.print_board(b)
Board.update_board(b,"chrono", 3)