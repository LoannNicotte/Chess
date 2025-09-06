import os
import pygame

"""
Loads and manages game assets.
"""

pygame.init()
pygame.display.set_mode((1, 1))

ASSETS = {}

# Load piece images
for name in os.listdir("assets/pieces"):
    path = os.path.join("assets/pieces/"+ name)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.smoothscale(img, (100, 100))
    ASSETS[name[:2]] = img
        
# Load board image
ASSETS["board"] = pygame.image.load("assets/board/board.png").convert()

# Load highlight, hint, and hover images
ASSETS["highlight"] = pygame.image.load("assets/board/highlight.png").convert_alpha()
ASSETS["moove"] = pygame.image.load("assets/board/moove.png").convert_alpha()
ASSETS["hover"] = pygame.image.load("assets/board/hover.png").convert_alpha()
ASSETS["capture"] = pygame.image.load("assets/board/capture.png").convert_alpha()