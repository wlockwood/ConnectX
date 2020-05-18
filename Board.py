

class Board:
    default_x_size: int = 7
    default_y_size: int = 6


    def __init__(self, x_size: int = None, y_size: int = None):
        self.x_size = x_size
        self.y_size = y_size

    @classmethod
    def create_board(cls,x_size,y_size):
        print(x_size)
        print(y_size)
        print(cls)
        try:
            if len(x_size) == 0:
                x_size = cls.default_x_size
            if len(y_size) == 0:
                y_size = cls.default_y_size
        except Exception as e:
            print(e)

        x = ['_'] * x_size
        y = ['_'] * y_size

        for num,col in enumerate(x):
            x[num] = y

        return x


    @classmethod
    def print_board(cls,board):
        for r in board:
            print(f"{r}\n")
        return(board)


    def update_board(cls,board,player,column):
        for cell in board:
            if board[column] == '_'
                board[column] = player
        pass
