import pygame
import assets   

class Board():
    """
    Class to handle drawing the chessboard and pieces.  
    """
    def __init__(self):
        pass   

    def draw_board(self, display):
        """
        Draws the chessboard on the given display surface.
        Args:
            display (pygame.Surface): The surface to draw the board on.
        """
        display.blit(assets.ASSETS["board"], (0, 0))

    def draw_pieces(self, display, echequier):
        """
        Draws the chess pieces on the board based on the current state.     
        Args:
            display (pygame.Surface): The surface to draw the pieces on.
            echequier (list): A 2D list representing the chessboard state.
        """
        tile_size = 100
        for row in range(8):
            for col in range(8):
                if echequier[row][col] != "--":
                    display.blit(assets.ASSETS[echequier[row][col]], (col * tile_size, row * tile_size))
    
    def draw(self, display, echequier):
        self.draw_board(display)
        self.draw_pieces(display, echequier)

      