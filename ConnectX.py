from Player import Player, PlayerColor
from Board import Board
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
        players.update({cur_player: Player(cur_player, cur_col)})
        play_id += 1
        player_num -= 1

    return (players)

# TODO: Check for wins
# TODO: Figure out colored text output
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


def take_turn(gameboard: Board, p: Player):
    gameboard.print_board()
    
    place_successful = False
    while not place_successful:
        move = ask_for_int(f"Player {p.plid}, ({p.name}) it is your turn. Please choose a column.",accept_min=1,accept_max=gameboard.x_size) - 1
        place_successful = gameboard.insert_token_into_column(move,p)

    

def main():
    # Defaults here are based off of replicating the classic game Connect Four. Maxes and Mins are just guesses.
    
    # Ask for player configuration. TODO: Names and colors
    PlayerColor.build_player_colors()
    player_count = ask_for_int("How many players?", default=2, accept_min=2, accept_max=7)
    players = [Player() for i in range(player_count)]
    print(players)
    
    # Get game configuration from user
    while(True):
        

        # Ask for game options
        board_size_x = ask_for_int("How wide should the board be?", default=7, accept_min=2, accept_max=12)
        board_size_y = ask_for_int("How tall should the board be?", default=6, accept_min=2, accept_max=12)
        win_run_max = max(board_size_x, board_size_y)
        win_run_length = ask_for_int("How many contiguous tokens to win?", default=4, accept_min=2, accept_max=win_run_max)

        print(f"Starting game with {player_count} players on a {board_size_x}x{board_size_y} board and a winning run length of {win_run_length}.")
        response = ask_for_word("Is this correct? y/n")
        if(response.lower()[0] == "y"):
            break
    
    # Initialize board
    gameboard = Board(x_size=board_size_x, y_size=board_size_y)
    
    # Cycling through turns
    while(True):
        for p in players:
            winner = gameboard.determine_winner(win_run_length)
            if winner:
                gameboard.print_board()
                print(f"Yay, {winner} won!")
                exit()

            if not gameboard.can_continue(): 
                gameboard.print_board()
                print(f"Board full - nobody wins. Boo")
                exit()           
            
            
            
            take_turn(gameboard, p)
            

        


   
# Actually run all the things.

main()

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