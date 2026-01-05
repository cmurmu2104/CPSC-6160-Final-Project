# Your game should have a main script that ties everything together and starts the game loop.
# Main game script: Your game should have a main script that ties everything together
# and starts the game loop.
#scp -r <folder>/ cmurmu@access.computing.clemson.edu <folder location>

import pygame
from Stuff import FrameViewer
from Stuff import GameLoop
from Stuff import hero
from Stuff import enemy

#assigning python files to variable for easy future modification
f = FrameViewer

# Initializing the game
pygame.init()

# Draw Game Screen
screen = f.drawDisplay()

# Fetch the Game Screen Background
screenBackground = f.shareBackground()

# Fetch the Game Screen Foreground
screenForeground = f.shareForeground()

# Fetch the Game Screen Sign
screenSign = f.shareSign()

# # Draw Hero
# screenHero = hero.HeroDraw()

# # Fetch the Hero Color
# HeroColor = hero.shareHero()

#calling Game loop from the main
GameLoop.gameLoop(screen, screenBackground, screenForeground, screenSign)



