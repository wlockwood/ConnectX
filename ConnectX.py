

# Get number of players

def get_players():
    try:
        player_num = int(input("How many players are going to play?\n"))
    except:
        print("Please enter a number, not whatever that was.")
        exit()
    players_list = [" "] * player_num

    for index,p in enumerate(players_list):
        num = index + 1
        name = input(f"Player {num}, What is your name/handle?\n")
        players_list[index] = name

    return(players_list)

# Progress through order of players.

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