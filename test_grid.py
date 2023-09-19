"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: A script that runs tests on the grid_to_string() function (grid.py).
"""

from grid import grid_to_string
from player import *
from game_parser import *


def test_grid():
    # Positive Case - 1 water bucket
    p1 = Player()
    p1.num_water_buckets = 1
    g1 =  parse(read_lines("BOARDS/board_basic.txt"))

    s1 = grid_to_string(g1,p1)
    assert s1 == '*X*****\n*     *\n*     *\n*****Y*\n\nYou have 1 water bucket.',"Test failed: grid not properly converted into string"

    # Positive Case - more than one water bucket
    p2 = Player()
    p2.num_water_buckets = 2
    g2 =  parse(read_lines("BOARDS/board_basic.txt"))

    s2 = grid_to_string(g2,p2)
    assert s2 == '*X*****\n*     *\n*     *\n*****Y*\n\nYou have 2 water buckets.',"Test failed: grid not properly converted into string"

    #Positive Case - board with all cell types
    p3 = Player()
    g3 =  parse(read_lines("BOARDS/board_hard.txt"))

    s3 = grid_to_string(g3,p3)
    assert s3 == '*X*************\n*       2 *   *\n* *** ** **** *\n* *  W*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  F   *\n* 1********F  *\n*************Y*\n\nYou have 0 water buckets.',"Test failed: grid not properly converted into string"

    # Negative Case - not a player type
    p4 = "I am not a player"
    g4 =  parse(read_lines("BOARDS/board_basic.txt"))
    try:
        s4 = grid_to_string(g4,p4)
    except Exception as e:
        assert type(e) == TypeError, "Test failed: incorrect error type"
        assert str(e) == "player argument is not of Player type", "Test failed: incorrect error message"

    # Negative Case - Not a list of list of cells
    p5 = Player()
    g5 = [1,2,3,4]
    try:
        s5 = grid_to_string(g5,p5)
    except Exception as e:
        assert type(e) == TypeError, "Test failed: incorrect error type"
        assert str(e) == "grid argument is not a list of list of cells", "Test failed: incorrect error message"




def run_tests():
    test_grid()


