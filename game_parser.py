"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: The read_lines() and parse() functions.
         Read_lines() takes a file and returns it as a list of strings
         Parse() takes the output of read_lines() and converts it to a list of cells.
"""


from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells, whose classes are defined in cells.py.
    
    Arguments:
        filename -- a filename in string form"""
    
    string_board = []

    try:
        with open(filename, 'r') as f:
            for line in f:
                string_board.append(line.strip())

    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()

    return string_board


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        rows -- contains list of lists of cells
    """
    X_count = 0
    Y_count = 0
    tele_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    rows = []

    for line in lines:
        line.strip("\n")

        cells = []

        # takes each character of the string and appends the corresponding cell type.
        for cell in line:
            if cell == "*":
                cells.append(Wall())

            if cell == "X":
                cells.append(Start())
                X_count += 1

            if cell == "Y":
                cells.append(End())
                Y_count += 1

            if cell == " ":
                cells.append(Air())

            if cell in "123456789":
                cells.append(Teleport(int(cell)))
                tele_count[int(cell)] += 1

            if cell == "W":
                cells.append(Water())

            if cell == "F":
                cells.append(Fire())

            if cell not in "*XY 123456789WF\n":
                raise ValueError("Bad letter in configuration file: {}.".format(cell))
        
        rows.append(cells)

    if X_count != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(X_count))

    if Y_count != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(Y_count))

    for pad_id,count in list(tele_count.items()):
        if not (count == 0 or count == 2):
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(pad_id))

    return rows
