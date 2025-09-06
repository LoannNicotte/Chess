import pygame
import assets
import board
import chessboard

class Game():

    def __init__(self):
        """
        Initializes the game, setting up the display, board, and chessboard state.
        """

        self.display = True
        self.running = True
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Chess")
        self.board = board.Board()
        self.chessboard = chessboard.Chessboard()

    def main(self):
        """
        The main game loop, handling events and rendering the board and pieces.
        """

        while self.running:
            self.screen.fill((0, 0, 0))
            self.board.draw(self.screen, self.chessboard)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if event.button == 1:  # Left click
                        if self.board.board_rect.collidepoint(mouse_x, mouse_y):
                            self.board.take_piece(self.chessboard)

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if event.button == 1: # Left click
                        self.board.place_piece((mouse_x, mouse_y), self.chessboard)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.main()