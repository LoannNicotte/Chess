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
    
    def get_possible_moves(self, position, piece):
        """
        Returns a list of possible moves for a piece at the given position.
        This is a placeholder for actual move generation logic.
        Args:
            position (tuple): A tuple (row, col) representing the position of the piece.
        Returns:
            list: A list of tuples representing possible move positions.
            list: A list of tuples representing possible capture positions.
        """
        row, col = position
        possible_moves = []
        possible_captures = []

        #king moves
        if piece[1] == 'k':
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == "--":
                        possible_moves.append((r, c))
                    elif self.board[r][c][0] != piece[0]:
                        possible_captures.append((r, c))

        #pawn moves
        elif piece[1] == 'p':
            direction = -1 if piece[0] == 'w' else 1
            # Move forward
            if 0 <= row + direction < 8 and self.board[row + direction][col] == "--":
                possible_moves.append((row + direction, col))
                # Double move from starting position
                if (row == 6 and piece[0] == 'w') or (row == 1 and piece[0] == 'b'):
                    if self.board[row + 2 * direction][col] == "--":
                        possible_moves.append((row + 2 * direction, col))
            # Captures
            for dc in [-1, 1]:
                if 0 <= col + dc < 8 and 0 <= row + direction < 8:
                    if self.board[row + direction][col + dc] != "--" and self.board[row + direction][col + dc][0] != piece[0]:
                        possible_captures.append((row + direction, col + dc))   

        #rook moves
        elif piece[1] == 'r':
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == "--":
                        possible_moves.append((r, c))
                    elif self.board[r][c][0] != piece[0]:
                        possible_captures.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc

        #bishop moves
        elif piece[1] == 'b':
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == "--":
                        possible_moves.append((r, c))
                    elif self.board[r][c][0] != piece[0]:
                        possible_captures.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc 
        
        #knight moves 
        elif piece[1] == 'n':
            knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
            for dr, dc in knight_moves:
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == "--":
                        possible_moves.append((r, c))
                    elif self.board[r][c][0] != piece[0]:
                        possible_captures.append((r, c))

        #queen moves
        elif piece[1] == 'q':
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == "--":
                        possible_moves.append((r, c))
                    elif self.board[r][c][0] != piece[0]:
                        possible_captures.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc
                    
        return possible_moves, possible_captures

    def validate_move(self, start_pos, end_pos, piece):
        """
        Validates if a move from start_pos to end_pos is legal.
        Args:
            start_pos (tuple): A tuple (row, col) representing the starting position of the piece.
            end_pos (tuple): A tuple (row, col) representing the ending position of the piece.
        Returns:        
            bool: True if the move is valid, False otherwise.
        """
        possible_moves, possible_captures = self.get_possible_moves(start_pos, piece)
        return end_pos in possible_moves + possible_captures
    
    def move_piece(self, start_pos, end_pos, piece):
        """
        Moves a piece from start_pos to end_pos on the chessboard.
        Args:
            start_pos (tuple): A tuple (row, col) representing the starting position of the piece.
            end_pos (tuple): A tuple (row, col) representing the ending position of the piece.
        """
        self.board[end_pos[0]][end_pos[1]] = piece
        self.board[start_pos[0]][start_pos[1]] = "--"
    
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

    