class Player():

    def __init__(self, plid: int, name: str, color: Color):
        # Parameters
        self.plid = plid
        self.name = name
        self.color = color

    def list_players(self):
        print("--------------------------------------------")
        print(f"|  {self.plid}  |  {self.name}  |  {self.color.name}  |")


class Color(): 
    colors = {}

    def __init__(self, full_name: str, abbreviation: str, rgb): 
        self.color_name = full_name
        self.abbreviation = abbreviation  # Should be three letters
        self.rgb = rgb
        Color.colors[color_name] = self

    def __str__(self):
        return self.color_name

    def __repr__(self):
        return "(Color) " + self.color_name

    @staticmethod
    def build_colors():  # TODO: Some way to do a *class* initialization?
        colors = ["red", "blue", "black", "yellow", "green", "orange", "teal", "off-white", "purple", "pinkish"]
        Color("red", "red", ""
        Color("blue", "blu", "")
        Color("black", "blk", "")
        Color("yellow", "ylw", "")
        Color("green", "grn", "")
        # ... add more


class Board():
    
    
    def __init__(self, board_x, board_y):
        self.x_size = board_x
        self.y_size = board_y
        self.columns = []

        # Fill self.columns with empty lists
        for i in range(x_size):
            self.columns.append([])

    def play_chip(self, column_index: int, player: Player):
        # Validate the column index
        if(column_index > self.x_size):
            raise Exception(f"Can't play chip at column {column_index} of {self.x_size}.") # Create a new PlayException or RuleException class?

        this_col = columns[column_index - 1]  # Adjust for zero-indexing

        if len(this_col) >= y_size:
            raise Exception(f"Column {column_index} is full and can't be played into.")
        
        # Add player reference to stand in for their played token
        this_col.append(player)


    def check_for_win(self):
        # Win condition: Any contiguous row or column of the same color of length X
        # Win condition: Any contiguous diagonal of the same color of length X
        return False


    def display(self):
        empty_cell = "|_____"
        
        this_row = []
        row_index = self.y_size
        for col in self.columns:
            if len(col) < self.y_size and not col[row_index]:  # On board and not occupied
                this_row.append(None)
            else:
                this_row.append(col[row_index])
            
            row_index -= 1
            if row_index < 0:
                break
        
        # Print rows



        # print out empty cells for cells which don't exist (based on len of columns vs. board size)
        # print out contents of column, starting from highest value 
        
        # Print out the 

        pass



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
            cur_player = input(f"Player {play_id + 1} , What is your name?\n")
        else:
            cur_player = deplay[play_id]  # debug val.
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

def calculate_longest_possible_run(board_x, board_y):
    print("TEMP: Only allowing orthogonal victories.")
    return max(board_x, board_y)

def main():
    play = get_players()
    size = get_board_size()
    print_table(play)
    print("\n\n")
    turn_order(play, size)  # Game loop


# Actually run all the things.

main()
