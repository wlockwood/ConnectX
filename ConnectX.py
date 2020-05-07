from Player import Player, PlayerColor
from InterfaceHelpers import *

def get_players():
    """
    Get player 
    """
    debug = 1
    players = {}

    if debug == 1:
        # Debug values
        return Player() * 3

    else:

        try:
            player_num = int(input("How many players are going to play (1-10)?\n"))
            if player_num > 10:
                print(f"{player_num} is too large. Please try again")
                exit()

        except:
            print("Please enter a valid number, not whatever that was.")
            exit()

    # player id - used for color and identification
    play_id = 0

    while player_num != 0:
        cur_col = PlayerColor.get_available_colors()[play_id]
        if debug == 0:
            cur_player = input(f"Player {play_id + 1} , What is your name?\n")
        else:
            cur_player = Player.default_player_names[play_id]  # debug val.
        players.update({cur_player: Player(play_id, cur_player, cur_col)})
        play_id += 1
        player_num -= 1

    return (players)


def get_board_size():
    size = input("How many columns would you like to play with (2-???)? (Standard is 7. 12+ is playable, but weird)")

    try:
        size = int(size)
    except:
        print("Try a number please.")
        exit()
    if size == 1:
        print("You must be lonely. This is not a single player game. ")
        exit()

    return (size)


def print_table(players):
    print("This is the current list of players.")
    print("    ID     |    Name       |    color ")
    for pl in players:
        Player.list_players(players[pl])


# TODO: Create a method to ask user for a number
# TODO: Create a method to print a sweet text representation of the board
# TODO: Figure out colored text output
# TODO: create a size of board question/logic
# TODO: Save/load
# TODO: Multiplayer across network?

"""
|_|_|_|_|_|
|_|_|_|_|_|
|_|_|_|_|_|
|_|_|_|_|_|
|_|_|_|●|_|
|_|●|_|_|_|
 1 2 3 4 5 

Ryan (green player), it's your turn. Input the column you'd like to place into (1-8):
 - Validate that there are open spaces on that column
 - Find a way to find the lowest row in that column
"""


def turn_order(players_list, size):
    # size = 8 # debug we'll set this up differently later
    board_line = ["|_____"] * size
    board_key = ["A", "B", "C", "D", "E", "F"]
    board_matrix = {'A': board_line.copy(), 'B': board_line.copy(), 'C': board_line.copy(), 'D': board_line.copy(),
                    'E': board_line.copy(), 'F': board_line.copy()}

    while True:
        for p in players_list:
            x = players_list[p]
            move = input(
                f"{x.name} ({x.color} player), it's your turn. Input the column you'd like to place into (1-{size}) \n")
            try:
                move = int(move)
            except:
                print("not a valid input. Next player's turn.")
                continue

            if move <= size:
                move -= 1
                for c in board_key[::-1]:
                    # print(c)
                    if board_matrix[c][move] == "|_____":
                        print("victory")
                        board_matrix[c][move] = f"| {x.color[0:3]} "
                        break
                    elif board_matrix['A'][move] != "|_____":
                        print("Column's full. Next player's turn.")
                        break
                    else:
                        continue

                for c in board_key:
                    print(f"{c} - {''.join(board_matrix[c])}|")

            else:
                print("not a valid input. Next player's turn.")


def main():

    # Defaults here are based off of replicating the classic game Connect Four. Maxes and Mins are just guesses.
    player_count = ask_for_int("How many players?", default=2, accept_min=2, accept_max=12)
    board_size = ask_for_int("How large should the board be?", default=6, accept_min=2, accept_max=12)
    win_run_length = ask_for_int("How many contiguous tokens to win?", default=4, accept_min=2, accept_max=12)

    print_table(play)
    print("\n\n")
    turn_order(play, size)


# Actually run all the things.

main()
