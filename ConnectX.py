class Player():

    def __init__(self, plid:int, name: str, color: str):
        # Parameters
        self.plid = plid
        self.name = name
        self.color = color

    def list_players(self):
        print("--------------------------------------------")
        print(f"|  {self.plid}  |  {self.name}  |  {self.color}  |")

def get_players():
    """
    Get player 
    """
    debug = 1
    players = {}
    colors = ["red", "blue", "black", "yellow", "green", "orange", "teal", "off-white", "purple", "pinkish"]

    if debug == 1:
        # Debug values
        player_num = 3
        deplay = ["Chrono", "Lucca", "Marle", "Magus", "Robo", "Ayla", "Frog"]

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
        cur_col = colors[play_id]
        if debug == 0:
            cur_player = input(f"Player {play_id+1} , What is your name?\n")
        else:
            cur_player = deplay[play_id] # debug val.
        players.update( {cur_player: Player(play_id,cur_player,cur_col)})
        play_id +=1
        player_num -= 1

    return(players)


def print_table(players):
    print("This is the current list of players.")
    print("    ID     |    Name       |    color ")
    for pl in players:
        Player.list_players(players[pl])

# TODO: create a table display for players
# TODO: look into/set up  __repr__
# TODO: set some debug values
# TODO: Create a method to ask user for a number
# TODO: Create a method to print a sweet colored text representation of the board
# TODO: create a size of board question/logic


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

def table_check(color, move, size):
    #tab = "|_" * size
    #tabl = f"{tab}|\n" *6
    print(tabl)
    print(color,move)
# Progress through order of players.

def turn_order(players_list):
    size = 8 # debug we'll set this up differently later
    board_line = ["|_"] * size
    board_key = ["A","B","C","D","E","F"]
    board_matrix = {'A':board_line.copy(), 'B':board_line.copy(), 'C':board_line.copy(), 'D':board_line.copy(),
                    'E': board_line.copy(), 'F': board_line.copy()}

    while True:
        for p in players_list:
            x = players_list[p]
            move = input(f"{x.name} ({x.color} player), it's your turn. Input the column you'd like to place into (1-{size}) \n")
            try:
                move = int(move)
            except:
                print("not a valid input. Next player's turn.")
                continue

            if move <= size:
                move -= 1
                for c in board_key[::-1]:
                    # print(c)
                    if board_matrix[c][move] == "|_":
                        print("victory")
                        board_matrix[c][move] = f"|{x.color}"

                        break
                    else:
                        continue


                for c in board_key:
                    print(f"{c} - {''.join(board_matrix[c])}|")

                # print(board_matrix)
                # table_check(x.color, move, size)
            else:
                print("not a valid input. Next player's turn.")


            


def main():
    play = get_players()
    print_table(play)
    print("\n\n")
    turn_order(play)

# Actually run all the things.

main()