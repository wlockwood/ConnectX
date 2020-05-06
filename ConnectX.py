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
        player_num = 2
        deplay = ["you", "me"]

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
    print("    ID     |    Name       |    color ")
    for pl in players:
        Player.list_players(players[pl])

# TODO: create a table display for players
# TODO: look into/set up  __repr__
# TODO: set some debug values
# TODO: Create a method to ask user for a number
# TODO: Create a method to print a sweet colored text representation of the board



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



# Progress through order of players. (outdated)

def turn_order(players_list):
    for p in players_list:
        print(f"{players_list[p.name]}")
            


def main():
    play = get_players()
    print(play)
    print_table(play)
    turn_order(play)

# Actually run all the things.

main()