from Player import Player, PlayerColor
from typing import List, Any
from Cell import Cell
from LambdaDirections import translate, Coord, get_directions

class Board:
    """
    A two-dimensional rectangular grid that holds Player references.
    Addressed from bottom-left corner for simplicity, starting from 0,0.
    """

    def __init__(self, x_size: int = 6, y_size: int = 7):
        self.x_size = x_size
        self.y_size = y_size

        self.board_grid = [[Cell(x,y) for y in range(y_size)] for x in range(x_size)]
        
        
        print(f"Initialized an empty Board {x_size} wide by {y_size} tall.")

    def get_cell(self, x: int, y:int) -> Cell:
        """
        Returns a reference to the Cell at some coords using 0-indexed coordinates.
        """
        if not self.check_valid_coord(x,y):
            raise Exception(f"Coordinate ({x},{y}) is not on the board!")
            
        return self.board_grid[x][y]

    def check_valid_coord(self, x: int, y: int) -> bool:
        """
        If a coordinate is on the board returns true, else false.
        """
        if 0 <= x < self.x_size and 0 <= y < self.y_size:
            return True
        else:
            return False

    def check_playable_coord(self, x: int, y:int) -> bool:
        """
        If a coordinate is both valid and empty return true, else false.
        """
        if self.check_valid_coord(x,y) and not self.get_cell(x,y).is_occupied():
            return True
        else:
            return False

    def set_cell(self, x: int, y: int, player: Player) -> bool:
        """
        Sets the value of a single cell on the board. (1,1) is bottom-left.
        Board is write-once, so any attempt to set a value that's already been set is exceptional.
        """
        if type(player) != Player:
            raise Exception(
                f"Player reference is the wrong type. Should be a Player class instance, instead was {type(player)}."
            )

        if not self.check_playable_coord(x, y):
            raise Exception(f"Cannot assign player {player} to coordinates ({x},{y}) as it's already filled.")
        
        self.get_cell(x,y).contents = player
        return True

    def get_lowest_open_cell_height(self, column_index: int) -> int:
        """
        Finds the lowest open cell in a column.
        Returns False if the column is already full.
        """
        for i in range(self.y_size):
            #print(f"({column_index},{i}) is: {self.get_cell(column_index, i)}")  # DEBUG
            if not self.get_cell(column_index,i).is_occupied():
                return i
        return -1

    def insert_token_into_column(self, column_index: int, player: Player) -> bool:
        """
        Add a player token to a given column if possible.
        Returns true if insert was successful.
        """
        height = self.get_lowest_open_cell_height(column_index)
        if height >= 0 :
            # print(f"Inserting token into column {column_index}. Found lowest open height of {height}.")  # DEBUG
            self.set_cell(column_index, height, player) 
            return True   
        elif height == -1:
            print(f"column {column_index} is full, cannot insert.")  # DEBUG
            return False
        else:
            raise Exception(f"Unexpected error while finding height to insert attempt. Got '{height}'.")

    def get_row(self, row_index: int) -> List[Player]:
        """
        Returns a row of board cells.
        Row indices are zero-indexed.
        Output is zero-indexed.
        """
        if row_index > self.y_size:
            raise Exception(f"Attempted to retrieve row at row_index {row_index}, but the board only has {y_size} rows.")
        
        output = []
        for i in range(self.x_size):
            output.append(self.get_cell(i, row_index))
        return output

    def row_to_string(self, row_index: int) -> str:
        """
        Creates a string-y version of a row of the board. Intended to assist printing.
        Empty spaces are indicated with an underscore _, while occupied spaces use the Player's token.
        """
        row = self.get_row(row_index)
        list_out = []
        
        for cell in row:
            if cell is None:
                list_out.append("___")
            else:
                list_out.append(cell.get_board_representation())
            
        return "|" + "|".join(list_out) + "|"
    

    def print_board(self):
        """
        Prints a text-based representation of the board's current state.
        """
        board_width = (self.x_size)
        board_title = "Current board state"
        print()
        print("{title:=^{bw}}".format(title=board_title, bw=board_width))
        print(" ___" * board_width)
        for row in range(self.y_size - 1, -1, -1):
            print(self.row_to_string(row))

    def get_all_cells(self) -> List[Cell]:
        return [cell for column in self.board_grid for cell in column]

    def count_most_occupied_cells(self) -> int:

        cells = self.get_all_cells()

        player_token_counter = {}
        for c in cells:
            # Skip empty cells
            if c.contents is None:
                continue

            # Unskip full cells    
            if c.contents not in player_token_counter.keys():
                player_token_counter[c.contents] = 1
            else:
                player_token_counter[c.contents] += 1
        
        for player,tc in player_token_counter.items():
            print(f"Player {player.plid} ({player.name}) has {tc} tokens.")
        
        
        if len(player_token_counter) == 0:
            return 0
        else:
            return max(player_token_counter.values())

    def determine_winner(self, win_num) -> Player:# TODO: Make name more accurate
        """
        Win check algorithm:
            Compare entire board, due to placement being difficult to calculate when 
            winning token placed in between other pieces
        """

        # Check first to see if there are enough pieces on the board for a win. If not, no winners!
        poswin = self.count_most_occupied_cells()
        if poswin < win_num:
            return None

        all_board = self.get_all_cells()
        current_check = ''
     
        # Check each cell, skipping empties
        for c in all_board:
            if c.contents is None:
                continue
            
            # if cell not empty, begin to compare with others
            friendly_player = c.contents
            origin_coord = Coord(c.x_pos,c.y_pos)
            current_check = None 

            for direction in get_directions():
                for distance in range(win_num):
                    check_x, check_y = translate(origin_coord,direction,distance)

                    if not self.check_valid_coord(check_x,check_y):
                        break

                    current_check = self.get_cell(check_x,check_y)

                    if current_check.contents != friendly_player:
                        break                    

                    if distance + 1 >= win_num:
                        return friendly_player
        
        
              

        return None

    @staticmethod
    def run_tests():
        print("Beginning Board.py tests with default parameters...")
        testboard = Board()

        # Initialize two test players
        PlayerColor.build_player_colors()
        Player()
        Player()
        player_list = list(Player.current_players.values())

        print(f"Test player list: {Player.current_players}")

        # Test check_valid_coord
        assert testboard.check_valid_coord(-1,-1) == False, "check_valid_coord gave a false positive: -1,-1 should be outside the board"
        assert testboard.check_valid_coord(0,0) == True, "check_valid_coord gave a false negative: 0,0 should always be on the board"
        assert testboard.check_valid_coord(testboard.x_size - 1,testboard.y_size - 1) == True, "check_valid_coord gave a false negative: upper-right corner should always be on the board"
        assert testboard.check_valid_coord(testboard.x_size,testboard.y_size) == False, "check_valid_coord gave a false positive: UR+1 should always be off the board"
        print("check_valid_coord passed tests.")

        # Test get-cell
        ## Bypass set-cell so that we don't have to rely on set-cell working correctly to confirm that read-cell also work correctly
        testboard.board_grid[0][0].contents = player_list[0]  # The array is zero indexed
        got_player: Player = testboard.get_cell(0,0).contents # The board's interface is one indexed
        testboard.print_board()
        assert got_player == player_list[0], f"get_cell check failed: Expected a reference to {player_list[0]} got {got_player}"
        
        #TODO: Convert this into 
        try:
            got_player = testboard.get_cell(-1,-1)
            assert False, "got_cell check failed: Expected an error, but didn't get one while accessing out-of-board cell reference."
        except:
            pass
        
        try:
            got_player = testboard.get_cell(10000,10000)
            assert False, "got_cell check failed: Expected an error, but didn't get one while accessing out-of-board cell reference."
        except:
            print("get_cell passed tests.")


        # Test set-cell
        ## Confirm cell starts out empty
        test_get_cell = testboard.get_cell(3, 3)
        assert test_get_cell.is_occupied() is False, f"Cell is full but should be empty. Expected False, got True. Contents: {test_get_cell.contents}"
        
        ## Insert a player into a cell and check if it worked. 
        testboard.set_cell(3, 3, player_list[1])
       
        test_get_cell = testboard.get_cell(3, 3)
        assert test_get_cell.contents == player_list[1], f"Cell isn't set properly. Expected {player_list[1]}, got {test_get_cell.contents} which is a {type(test_get_cell)}"

        # Test get_lowest_open_cell_height
        testboard.set_cell(3, 0, player_list[1])
        testboard.set_cell(3, 1, player_list[0])
        testboard.set_cell(3, 2, player_list[1])
        testboard.print_board()
        
        low_height = testboard.get_lowest_open_cell_height(0)
        assert low_height == 1, f"Lowest height given earlier tests should be 1 as column contains something at (0,0). Got {low_height} instead"
        low_height = testboard.get_lowest_open_cell_height(1)
        assert low_height == 0, f"Lowest height given earlier tests should be 0 as column is empty. Got {low_height} instead"
        low_height = testboard.get_lowest_open_cell_height(3)
        assert low_height == 4, f"Lowest height given earlier tests should be 5 as column has four tokens in it. Got {low_height} instead"
        print("get_lowest_open_cell_height passed tests")

        # Test insert_token_into_column
        testboard.print_board()

        ## Test on empty column
        assert testboard.insert_token_into_column(1, player_list[0]), "Couldn't insert into column index 1"
        testboard.print_board()

        # Test insert token into occupied column
        assert testboard.insert_token_into_column(0, player_list[0]), "Couldn't insert into column index 0"
        testboard.print_board()
        
        # Test a full column
        testboard.insert_token_into_column(3, player_list[0])
        testboard.insert_token_into_column(3, player_list[0])
        testboard.insert_token_into_column(3, player_list[0])
        testboard.print_board()

        # this should fail
        test = testboard.insert_token_into_column(3, player_list[0])
        assert test == False, f"This should have failed as column is full. instead got {test}"
        '''
        #check the win
        test = testboard.check_for_win(4)
        assert test == True, f"this should return true. got {test}"
        '''
        
        # Test helper functions
        testboard = Board(5,5)
        all_cells = testboard.get_all_cells()
        
        assert len(all_cells) == 25, f"get_all_cells returned {len(all_cells)} cells instead of 25."
        
        now_token_count = testboard.count_most_occupied_cells()
        assert now_token_count == 0, f"count_most_occupied_cells returned {now_token_count} instead of 0 on an empty board."
        
        testboard.insert_token_into_column(0, player_list[0])
        now_token_count = testboard.count_most_occupied_cells()
        assert now_token_count == 1, f"count_most_occupied_cells returned {now_token_count} instead of 1."

        testboard.insert_token_into_column(3, player_list[0])
        now_token_count = testboard.count_most_occupied_cells()
        assert now_token_count == 2, f"count_most_occupied_cells returned {now_token_count} instead of 2."

        testboard.insert_token_into_column(3, player_list[1])
        testboard.insert_token_into_column(3, player_list[1])
        testboard.insert_token_into_column(3, player_list[1])  
        now_token_count = testboard.count_most_occupied_cells()
        assert now_token_count == 3, f"count_most_occupied_cells returned {now_token_count} instead of 3."
        
        # Check for win is complex and needs lots of tests  
        testboard = Board(5,5)
        assert testboard.determine_winner(3) == None, "Board is empty, but somehow we found a winner."
        testboard.insert_token_into_column(3, player_list[1])
        assert testboard.determine_winner(3) == None, "Board only has one token on it, but we found a winner."
        testboard.insert_token_into_column(3, player_list[1])
        testboard.insert_token_into_column(3, player_list[1])
        assert testboard.determine_winner(3) == player_list[1], "Failed to detect a vertical win."
        testboard.insert_token_into_column(1, player_list[1])
        testboard.insert_token_into_column(2, player_list[1])
        testboard.insert_token_into_column(4, player_list[1])  # Already have a column in 3
        assert testboard.determine_winner(4) == player_list[1], "Failed to detect a horizontal win."
        
        testboard = Board(5,5)
        testboard.insert_token_into_column(1, player_list[1])
        testboard.insert_token_into_column(2, player_list[0])
        testboard.insert_token_into_column(3, player_list[1])
        testboard.insert_token_into_column(4, player_list[0])
        testboard.print_board()
        assert testboard.determine_winner(3) == None, "Detected a false horizontal win"

        testboard = Board(5,5)
        testboard.insert_token_into_column(1, player_list[1])
        testboard.insert_token_into_column(2, player_list[0])
        testboard.insert_token_into_column(2, player_list[1])
        testboard.insert_token_into_column(3, player_list[0])
        testboard.insert_token_into_column(3, player_list[0])
        testboard.insert_token_into_column(3, player_list[1])
        testboard.print_board()
        assert testboard.determine_winner(3) == player_list[1], "Failed to detect a diagonal win."


        testboard = Board(5,5)
        testboard.insert_token_into_column(1, player_list[1])
        testboard.insert_token_into_column(1, player_list[0])
        testboard.insert_token_into_column(1, player_list[1])
        testboard.insert_token_into_column(1, player_list[1])
        testboard.print_board()
        assert testboard.determine_winner(3) == None, f"Winner {testboard.determine_winner(3)} set despite 3 not being in a row."
       
        testboard = Board(2,2)
        testboard.insert_token_into_column(1, player_list[1])
        testboard.insert_token_into_column(1, player_list[0])
        testboard.insert_token_into_column(0, player_list[1])
        testboard.print_board()
        testboard.insert_token_into_column(0, player_list[1])
        testboard.print_board()        
        assert testboard.determine_winner(3) == None, f"Winner {testboard.determine_winner(3)} set board being full."

if __name__ == "__main__":
    Board.run_tests()
