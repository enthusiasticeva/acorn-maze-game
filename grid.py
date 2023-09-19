"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: The grid_to_string() function, which takes a list of list of cells (the output of parse() in game_parser.py)
         and returns a string with the board and the water count, for printing when the game is played.
"""

from cells import Start
from player import Player


def grid_to_string(grid, player):
    """Takes a grid of cells (from the parse() function) and returns a string with the player 
        appropriately placed on the board and the water bucket count.

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        output_string: A string representation of the grid and player. """

    if type(player) != Player:
        raise TypeError("player argument is not of Player type")

    if type(grid) != list or type(grid[0]) != list:
        raise TypeError("grid argument is not a list of list of cells")

    output_string = ""
    col = player.col #x
    row = player.row #y

    # loops through each cell in the grid, using the enumerate function to keep track of the indexes, 
    # which are used like coordiantes to correctly place the player.
    for line_num,line in enumerate(grid):
        for cell_num, cell in enumerate(line):
            if col == cell_num and row == line_num:
                output_string = output_string + "A"
            else:
                output_string = output_string + str(cell.display)

        output_string = output_string + "\n"
    
    if player.num_water_buckets != 1:
        output_string = output_string + "\n" + "You have {} water buckets.".format(player.num_water_buckets)

    else:
        output_string = output_string + "\n" + "You have {} water bucket.".format(player.num_water_buckets)

    return output_string
