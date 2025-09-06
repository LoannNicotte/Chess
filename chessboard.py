class Chessboard:
    """
    Represents the state of a chessboard, including piece positions and methods.
    """
    
    def __init__(self):
        """
        Initializes the chessboard with the standard starting position.
        The board is represented as an 8x8 list of lists, where each piece is denoted by a two-character string.
        Example: "wp" for white pawn, "bk" for black king, "--" for an empty square.
        """

        self.board = [
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
        ]


    def get_board(self):
        """
        Returns the current state of the chessboard.
        Returns:
            list: A 2D list representing the chessboard state.
        """

        return self.board   

    def load_board(self, name):
        """
        Loads a chessboard state from a file.
        The file should contain 8 lines, each with 8 space-separated values representing the pieces.
        Example of a line: "br bn bb bq bk bb bn br"
        "--" represents an empty square.
        Args:
            path (str): The file path to load the board state from.
        """

        with open("save/" + name + ".txt", 'r') as f:
            lines = f.readlines()
            for row in range(8):
                self.board[row] = lines[row].strip().split(' ')
            f.close()

    def save_board(self, name):
        """
        Saves the current chessboard state to a file.
        The file will contain 8 lines, each with 8 space-separated values representing the pieces.
        Example of a line: "br bn bb bq bk bb bn br"    
        "--" represents an empty square.
        Args:
            path (str): The file path to save the board state to.
        """

        with open("save/" + name + ".txt", 'w') as f:
            for row in range(8):
                f.write(' '.join(self.board[row]) + '\n')
            f.close()