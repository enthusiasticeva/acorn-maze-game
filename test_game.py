"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: A script that runs tests on the Game (game.py) and Player (player.py) classes.
"""

from game import Game
from player import Player


def test_game():
    '''#### set_start_pos() method ####'''
    # the grid used in this method has already been checked for validity in the parse() function, which has been already tested.

    # Positive case - grid with start cell
    # this method is run on initiation
    g = Game("BOARDS/board_basic.txt", True)
    assert g.player.row == 0 and g.player.col == 1 ,"Test failed: start position not correctly set"


    '''#### find_tele_pairs() method ####'''
    # the grid used in this method has already been checked for validity in the parse() function, which has been already tested.
    
    # Positive case - 1 set of teleport pads
    # this method is run on initiation
    g1 = Game("BOARDS/board_tele.txt", True)
    assert g1.tele_pairs == [[(1, 1), (3, 1)], [], [], [], [], [], [], [], []], "Test failed: teleport pads improperly found"

    # Positive case - 9 sets of teleport pads
    g2 = Game("BOARDS/board_many_telepads.txt", True)
    assert g2.tele_pairs == [[(1, 1), (1, 3)], [(2, 1), (2, 3)], [(3, 1), (3, 3)], [(4, 1), (4, 3)], [(5, 1), (5, 3)], [(6, 1), (6, 3)], [(7, 1), (7, 3)], [(8, 1), (8, 3)], [(9, 1),
(9, 3)]], "Test failed: teleport pads improperly found"

    # Edge case - no sets of teleport pads
    g3 = Game("BOARDS/board_basic.txt", True)
    assert g3.tele_pairs == [[], [], [], [], [], [], [], [], []], "Test failed: no teleport pads should have been found"


    '''#### update_board() method ####'''
    # this method is essentially just the grid_to_string() function, which has already been tested.


    '''#### game_move() method ####'''
    # this method is essentially just the player.move() method, which has already been tested.


    '''#### game_move_back() method ####'''
    # this method is essentially just the player.move_back() method, which has already been tested.


    '''#### make_move() method ####'''
    '''#### play() method ####'''
    #these two methods have their functionality demonstrated and thoroughly tested in the e2e tests of run.py


def test_player():
    '''#### move() method ####'''
    p = Player()
    p.row = 5
    p.col = 5

    # Positive case - 'w' argument
    p.move("w")
    assert p.row == 4 and p.col == 5, "Test failed: 'w' move command not working properly"

    # Positive case - 's' argument
    p.move("s")
    assert p.row == 5 and p.col == 5, "Test failed: 's' move command not working properly"

    # Positive case - 'a' argument
    p.move("a")
    assert p.row == 5 and p.col == 4, "Test failed: 'a' move command not working properly"

    # Positive case - 'd' argument
    p.move("d")
    assert p.row == 5 and p.col == 5, "Test failed: 'd' move command not working properly"

    # Positive case - 'e' argument
    p.move("e")
    assert p.row == 5 and p.col == 5, "Test failed: 'e' move command not working properly"

    # Positive case - 'q' argument
    p.move("q")
    assert p.row == 5 and p.col == 5, "Test failed: 'q' move command not working properly"

    # Edge case - capital letter
    p.move("A")
    assert p.row == 5 and p.col == 4, "Test failed: captial letter not properly recognised"

    # Negative case - non string argument
    try:
        p.move(5)
    except Exception as e:
        assert type(e) == ValueError, "Test failed: incorrect error type"
        assert str(e) == "Argument for player.move() was not a string", "Test failed: incorrect error message"

    # Negative case - longer string (with valid letters) 'wsa'
    try:
        p.move("wsa")
    except Exception as e:
        assert type(e) == ValueError, "Test failed: incorrect error type"
        assert str(e) == "Please enter a valid move (w, a, s, d, e, q).", "Test failed: incorrect error message"


    '''#### move_back method ####'''
    # All exception handling for move_back() is inherited from move() and has already been tested.
    p.row = 5
    p.col = 5
    # Positive case - 's' argument
    p.move_back("s")
    assert p.row == 4 and p.col == 5, "Test failed: 'w' move_back command not working properly"

    # Positive case - 'w' argument
    p.move_back("w")
    assert p.row == 5 and p.col == 5, "Test failed: 's' move_back command not working properly"

    # Positive case - 'd' argument
    p.move_back("d")
    assert p.row == 5 and p.col == 4, "Test failed: 'a' move_back command not working properly"

    # Positive case - 'a' argument
    p.move_back("a")
    assert p.row == 5 and p.col == 5, "Test failed: 'd' move_back command not working properly"
    

def run_tests():
    test_player()
    test_game()


