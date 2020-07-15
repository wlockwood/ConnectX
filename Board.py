from Player import Player, PlayerColor
from typing import List, Any
from Cell import Cell

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
            print(f"({column_index},{i}) is: {self.get_cell(column_index, i)}")
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
            print(f"Inserting token into column {column_index}. Found lowest open height of {height}.")  # DEBUG
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
    
    def get_adjacent(self, x: int, y: int) -> List:
        """
        Returns a (...?) containing the values adjacent to a given index.
        """
        print("This would have returned a list of adjacent cells, but isn't yet implemented.")

    def print_board(self):
        """
        Prints a text-based representation of the board's current state.
        """
        board_width = (self.x_size) * 5 - 1
        board_title = "Current board state"
        print()
        print("{title:=^{bw}}".format(title=board_title, bw=board_width))
        print("_" * board_width)
        for row in range(self.y_size - 1, -1, -1):
            print(self.row_to_string(row))
        
    def check_for_win(self, win_num):
        """
        Win check algorithm:
            for each occupied cell:
	        then compare with cell below
	        if friendly, check next down
		        repeat until out
	        if total run length >= than win run length:
		        cake is not a lie / victory
		
            same thing in every other direction
        """

        points = 0
        for origin_x in range(self.x_size):
            for origin_y in range(self.y_size):
                # Skip unoccupied cells
                origin_cell: Player = self.get_cell(origin_x, origin_y)
                if origin_cell is None:
                    continue
                # Compare with lower cells
                if self.check_valid_coord(origin_x +1, origin_y -1):
                    check_cell_y = self.get_cell(origin_x, origin_y - 1)
                else:
                    check_cell_y = None

                # Compare with left cell    
                if self.check_valid_coord(origin_x +1, origin_y):
                    check_cell_x = self.get_cell(origin_x +1 , origin_y)
                else:
                    check_cell_x = None


                # Compare with digonal up left
                if self.check_valid_coord(origin_x +1, origin_y +1):
                    check_cell_diagUp = self.get_cell(origin_x + 1, origin_y + 1)
                else:
                    check_cell_diagUp = None

                # Compare with Diag down
                if self.check_valid_coord(origin_x +1, origin_y - 1):    
                    check_cell_diagDown = self.get_cell(origin_x + 1, origin_y - 1)
                else:
                    check_cell_diagDown = None
                
                # Compare with all
                if origin_cell == (check_cell_y or check_cell_x or check_cell_diagDown or check_cell_diagUp):
                    points += 1
                else:
                    points = 0

                if points >= win_num:
                    print(f"Player {origin_cell} wins!")
                    exit()               

                     

        return False

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
        


if __name__ == "__main__":
    Board.run_tests()
