class Player():

    def __init__(self, id:int, name: str, color: str):
        # Parameters
        self.id = id
        self.name = name
        self.color = color



def get_players():
    """
    Get player 
    """
    # colors
    colors = ["red","blue", "black", "yellow", "green", "orange", "teal", "off-white", "purple", "pinkish"]
    players = {}
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
        # print(cur_col)
        cur_player = input(f"Player {play_id+1} , What is your name?\n")
        players.update( {cur_player: Player(play_id,cur_player,cur_col)})
        play_id +=1
        player_num -= 1

    print(players)
    for pl in players:
        print(pl, players[pl].color)


# create a table display for players
# look into __repr__
# set some debug values




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



# Progress through order of players.
'''
def turn_order(players_list):
    while True:
        turns = len(players_list) -1
        while turns != -1:
            print(f"player {players_list[turns]} (player {turns +1}), it's your turn.")
            turns -=1
            

# Run all the things!

def main():
    turn_order(get_players())


# Actually run all the things.

main()
'''
get_players()