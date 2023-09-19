"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: A script using the game class (game.py) to take a board through a system argument and run the game for the user.
"""

from game import Game
import os
import sys


if len(sys.argv) > 1:
    # Retrieves the filename from the system arguments.
    filename = sys.argv[1]

    # Initiates a game
    g = Game(filename, False)

    # Checks if play has been set to True - in which case the screen will be cleared each move
    if len(sys.argv) > 2:
        if sys.argv[2] == "True":
            g.play(True,False)
            
    else:
        g.play(False,False)

else: 
    print("Usage: python3 run.py <filename> [play]")
    sys.exit()
