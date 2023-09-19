"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: The Player class, containing a water count and posisition, and methods to change the position.
"""

class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.col = -1 #x
        self.row = -1 #y


    def move(self, move):
        ''' Takes a move in as a string, checks if it is valid, then moves the player appropriately.
        
        Arguments:
            move - a single character string containing a move (wsade) '''

        if not type(move) == str:
            raise ValueError("Argument for player.move() was not a string")

        if move.lower() == "w":
            self.row -= 1

        if move.lower() == "s":
            self.row += 1

        if move.lower() == "a":
            self.col -= 1

        if move.lower() == "d":
            self.col += 1

        if move.lower() not in ["w","s","a","d","q","e"]:
            raise ValueError("Please enter a valid move (w, a, s, d, e, q).")

    def move_back(self, move):
        ''' Takes a move in a string, and does the reverse of the move. As this function calls move(), the validation of move is already done.

        Arguments:
            move - a single character string containing a move (wsade)'''
        if move.lower() == "w":
            self.move("s")

        if move.lower() == "s":
            self.move("w")

        if move.lower() == "a":
            self.move("d")

        if move.lower() == "d":
            self.move("a")

