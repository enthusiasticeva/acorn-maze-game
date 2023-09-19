"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: A script that runs tests on the read_lines() and parse() functions (game_parser.py).
"""

from game_parser import *

def test_readlines():
    # Positive Test Case - inputting a valid file
    assert read_lines("BOARDS/board_basic.txt") == ['*X*****', '*     *', '*     *', '*****Y*'], "Test failed: board not read in correctly"

    # Edge Case - empty file
    assert read_lines("BOARDS/board_empty.txt") == [], "Test failed: incorrect behaviour for empty file"

    # Negative test case - missing file
    # testing of a file not being found will be included in the run.py e2e tests, as it prints directly.

def test_parse():
    # Positive Case - basic file (no teleports, fire, water)
    lines1 = read_lines("BOARDS/board_basic.txt")
    grid1 = parse(lines1)
    assert type(grid1) == list, "Test failed: basic board incorrectly parsed"
    assert type(grid1[0]) == list, "Test failed: basic board incorrectly parsed"
    
    st1 = ""
    for row in grid1:
        for cell in row:
            st1 += cell.display
        st1 += ","
    
    assert st1 == '*X*****,*     *,*     *,*****Y*,', "Test failed: basic board incorrectly parsed"


    # Positive Case - file with teleports
    lines2 = read_lines("BOARDS/board_tele.txt")
    grid2 = parse(lines2)
    assert type(grid2[1][1]) == Teleport and type(grid2[1][3]) == Teleport, "Test failed: board with teleports incorrectly parsed"
    assert grid2[1][1].display == 1 and grid2[1][1].display == 1, "Test failed: board with teleports incorrectly parsed"

    # Positive Case - file with fire and water
    lines3 = read_lines("BOARDS/board_fire_water.txt")
    grid3 = parse(lines3)
    assert type(grid3[1][2]) == Water and type(grid3[3][1]) == Fire, "Test failed: board with fire and water incorrectly parsed"

    # Positive Case - file with all features
    lines4 = read_lines("BOARDS/board_hard.txt")
    grid4 = parse(lines4)
    st4 = ""
    for row in grid4:
        for cell in row:
            st4 += str(cell.display)
        st4 += ","
    
    assert st4 == '*X*************,*       2 *   *,* *** ** **** *,* *  W*   1   *,* ***** ***** *,*  2 *   ** *F*,* ** ***  F   *,* 1********F  *,*************Y*,', "Test failed, board with all features incorrectly parsed"
    
    # Edge Case - empty file, triggers no start position
    try: 
        parse(read_lines("BOARDS/board_empty.txt"))
    except Exception as e:
        assert type(e) == ValueError, "Test failed: incorrect error type"
        assert str(e) == "Expected 1 starting position, got 0.", "Test failed: incorrect error message"

    # Negative Case - no start cell
    try: 
        parse(read_lines("BOARDS/board_no_start.txt"))
    except Exception as e:
        assert type(e) == ValueError, "Test failed: incorrect error type"
        assert str(e) == "Expected 1 starting position, got 0.", "Test failed: incorrect error message"

    # Negative Case - no end cell
    try: 
        parse(read_lines("BOARDS/board_no_end.txt"))
    except Exception as e:
        assert type(e) == ValueError, "Test failed: incorrect error type"
        assert str(e) == "Expected 1 ending position, got 0.", "Test failed: incorrect error message"

    # Negative Case - only 1 of teleport number
    try: 
        parse(read_lines("BOARDS/board_uneven_teleport.txt"))
    except Exception as e:
        assert type(e) == ValueError, "Test failed: incorrect error type"
        assert str(e) == "Teleport pad 1 does not have an exclusively matching pad.", "Test failed: incorrect error message"

    # Negative Case - 4 of same number
    try: 
        parse(read_lines("BOARDS/board_4_teleports.txt"))
    except Exception as e:
        assert type(e) == ValueError, "Test failed: incorrect error type"
        assert str(e) == "Teleport pad 1 does not have an exclusively matching pad.", "Test failed: incorrect error message"

    # Negative Case - invalid symbols in file
    try: 
        parse(read_lines("BOARDS/board_bad_symbols.txt"))
    except Exception as e:
        assert type(e) == ValueError, "Test failed: incorrect error type"
        assert str(e) == "Bad letter in configuration file: L.", "Test failed: incorrect error message"

    # Negative test case - missing file
    # inherited from readlines() - adressed in e2e testing of run.py

def run_tests():
    test_parse()
    test_readlines()

