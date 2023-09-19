"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: Classes for each of the kinds of cells that can occur on the game board. 
         These include their display in string form and their message when interacted with.
"""

class Start:
    def __init__(self):
        self.display = 'X'


    def print_message(self,water):
        # As the fire message depends on the boolean water, 
        # and when the print_message method is called the type of cell is unknown, 
        # all cells needed water in the method.
        pass



class End:
    def __init__(self):
        self.display = 'Y'

    def print_message(self,water):
        pass


class Air:
    def __init__(self):
        self.display = ' '

    def print_message(self,water):
        pass


class Wall:
    def __init__(self):
        self.display = '*'

    def print_message(self,water):
        print("\nYou walked into a wall. Oof!")


class Fire:
    def __init__(self):
        self.display = 'F'

    def print_message(self,water):
        if water:
            print("\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!")
        else:
            print("\n\nYou step into the fires and watch your dreams disappear :(.")


class Water:
    def __init__(self):
        self.display = 'W'

    def print_message(self,water):
        print("\nThank the Honourable Furious Forest, you've found a bucket of water!")


class Teleport:
    def __init__(self,id):
        self.display = id  # You'll need to change this!

    def print_message(self,water):
        print("\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.")
