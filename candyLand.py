#main file for candy land game

import pygame
from Stuff import FrameViewer
from Stuff import startGame
from Stuff import candyGameLoop

#assigning python files to variable for easy future modification
f = FrameViewer.GameDisplay()

# Initializing the game
pygame.init()

# Draw Game Screen
screen = f.drawDisplay()

# Fetch the Game Screen Background
screenBackground = f.shareBackground()

# # Fetch the Game Screen Foreground
# screenForeground = f.shareForeground()

# # Fetch the Game Screen Sign
# screenSign = f.shareSign()

startGame.start_game(screen, screenBackground)