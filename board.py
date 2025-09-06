import pygame
import assets   


class Board():
    """
    Class to handle drawing the chessboard and pieces.  
    """
    def __init__(self):
        self.board_rect = pygame.Rect(0, 0, 800, 800)

        self.last_moves_pos = []
        self.selected_piece_pos = None

        self.hand = None

    def draw_board(self, display):
        """
        Draws the chessboard on the given display surface.
        Args:
            display (pygame.Surface): The surface to draw the board on.
        """
        display.blit(assets.ASSETS["board"], (0, 0))

    def draw_hand(self, display):
        """
        Draws the piece being moved by the player at the current mouse position.
        Args:
            display (pygame.Surface): The surface to draw the piece on.
        """
        if self.hand:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            display.blit(assets.ASSETS[self.hand], (mouse_x - 50, mouse_y - 50))

    def draw_mooves_captures(self, display, chessboard):
        """
        Draws possible moves and captures for a selected piece.
        Args:
            display (pygame.Surface): The surface to draw the hints on.
            chessboard (list): A 2D list representing the chessboard state.
            pos (tuple): A tuple (row, col) representing the position of the selected piece.
        """
        if self.selected_piece_pos:
            possible_moves, possible_captures = chessboard.get_possible_moves(self.selected_piece_pos, self.hand)

            for move in possible_moves:
                display.blit(assets.ASSETS["moove"], (move[1] * 100, move[0] * 100))
            for capture in possible_captures:
                display.blit(assets.ASSETS["capture"], (capture[1] * 100, capture[0] * 100))

    def draw_highlight(self, display):
        """
        Draws highlights on the board for last moves and selected pieces.
        Args:
            display (pygame.Surface): The surface to draw the highlights on.
        """

        for pos in self.last_moves_pos:
            display.blit(assets.ASSETS["highlight"], (pos[1] * 100, pos[0] * 100))

        if self.selected_piece_pos:
            display.blit(assets.ASSETS["highlight"], (self.selected_piece_pos[1] * 100, self.selected_piece_pos[0] * 100))

    def draw_hover(self, display):
        """
        Draws a hover effect on the tile under the mouse cursor.
        Args:
            display (pygame.Surface): The surface to draw the hover effect on.
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.hand and self.board_rect.collidepoint(mouse_x, mouse_y):
            col = mouse_x // 100
            row = mouse_y // 100
            display.blit(assets.ASSETS["hover"], (col * 100, row * 100))

    def draw_pieces(self, display, chessboard):
        """
        Draws the chess pieces on the board based on the current state.     
        Args:
            display (pygame.Surface): The surface to draw the pieces on.
            chessboard (list): A 2D list representing the chessboard state.
        """ 
        board = chessboard.get_board()
        tile_size = 100
        for row in range(8):
            for col in range(8):
                if board[row][col] != "--":
                    display.blit(assets.ASSETS[board[row][col]], (col * tile_size, row * tile_size))

    def take_piece(self, chessboard):
        """
        Selects a piece at the given position if it exists.
        Args:
            pos (tuple): A tuple (row, col) representing the position of the piece to select.
            chessboard (Chessboard): The chessboard object containing the game state.
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.board_rect.collidepoint((mouse_x, mouse_y)) and not self.hand:
            col = mouse_x // 100
            row = mouse_y // 100
            if chessboard.board[row][col] != "--":
                self.selected_piece_pos = (row, col)
                self.hand = chessboard.board[row][col]
                chessboard.board[row][col] = "--"
    
    def place_piece(self, pos, chessboard):
        """
        Places the selected piece at the current mouse position if valid.
        Args:
            chessboard (Chessboard): The chessboard object containing the game state.
        """
        if self.hand:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.board_rect.collidepoint(mouse_x, mouse_y):
                col = mouse_x // 100
                row = mouse_y // 100
                end_pos = (row, col)
                if chessboard.validate_move(self.selected_piece_pos, end_pos, self.hand):
                    chessboard.move_piece(self.selected_piece_pos, end_pos, self.hand)
                    self.last_moves_pos = [self.selected_piece_pos, end_pos]

                else:
                    # Return piece to original position if move is invalid
                    chessboard.board[self.selected_piece_pos[0]][self.selected_piece_pos[1]] = self.hand

                self.selected_piece_pos = None
                self.hand = None
            else:
                # Return piece to original position if placed outside the board
                chessboard.board[self.selected_piece_pos[0]][self.selected_piece_pos[1]] = self.hand
                self.hand = None

    
    def draw(self, display, chessboard):
        """
        Draws the chessboard and pieces on the given display surface.
        Args:
            display (pygame.Surface): The surface to draw the board and pieces on.
            chessboard (Chessboard): The chessboard object containing the game state.
        """

        self.draw_board(display)
        self.draw_highlight(display)
        self.draw_pieces(display, chessboard)
        self.draw_mooves_captures(display, chessboard)
        self.draw_hover(display)
        self.draw_hand(display)

      