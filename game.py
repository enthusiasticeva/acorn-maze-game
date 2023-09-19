"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: The game class that contains methods to set up and play the game, as well as check paths for the solver.
"""

from game_parser import read_lines, parse
from grid import grid_to_string
from player import Player
import os
import sys
from cells import *

class Game:
    def __init__(self, filename,solve):
        self.game_grid = parse(read_lines(filename))
        self.moves_made = []
        self.player = Player()
        self.tele_pairs = [[],[],[],[],[],[],[],[],[]]
        self.win = True
        self.game_state = "game in progress"

        # Sets up the game - finds the start position, configures the teleporters and generates the game display string.
        self.set_start_pos()
        self.find_tele_pairs()
        b = self.update_board()

        # If a game has been initialised for the solver, there is no need to print the board.
        if not solve:
            print(b)



    def set_start_pos(self):
        ''' Searches through the game board and finds the coordinates of the Start cell.
        The existence and exclusivity of these pads has been checked in parse() 
        '''
        for line_num,line in enumerate(self.game_grid):
            for cell_num,cell in enumerate(line):
                if type(cell) == Start:
                    #self.player.position = (cell_num,line_num)
                    self.player.col = cell_num
                    self.player.row = line_num

    def find_tele_pairs(self):
        ''' Goes through each possible teleport pad id and finds the position of both pads. 
        The pads being in exclusive pairs has been checked parse(). '''
        for i in range(1,10):
            for line_num,line in enumerate(self.game_grid):
                for cell_num,cell in enumerate(line):
                    if str(cell.display) == str(i):
                        self.tele_pairs[i-1].append((cell_num,line_num))


    def update_board(self):
        ''' Runs the grid_to_string function with the updated player position and water bucket count.

        Returns:
            string: the game board as a string '''
        return grid_to_string(self.game_grid,self.player)


    def game_move(self, move):
        '''Updates the players position

        Arguments:
            move -- a string '''
        self.player.move(move)


    def game_move_back(self, move):
        '''Does the opposite of the move passed in (used when the player must back from walls.)

        Arguments:
            move -- a string '''
        self.player.move_back(move)


    def make_move(self, play,user_move,solve):
        '''
        Executes a move on the gameboard.

        Arguments:
            play --         a Boolean value of whether the game is in play mode (clears after each move)
            user_move --    a string
            solve --        a boolean value of whether the game object is being used for the solver. '''
        # quits if 'q'
        if user_move.lower() == "q":
            print("\nBye!")
            sys.exit()

        '''Preventing the player from stepping out of bounds.'''
        try:
            self.game_move(user_move)

            water = False # Keeps track of if the player had water when they interacted with fire (so that the correct message can be displayed)
            wall = False # Keeps track of if the user has bumped into a wall on this turn, so the correct message is displayed.

            try:
                cell_type = self.game_grid[self.player.row][self.player.col] #keeps track of the type of the cell, so that the correct message can be displayed (as fire/water turn to air when stepped on)
        
            except IndexError:
                # Bounces the player back if they walk out of bouds on the right or bottom of board.
                self.game_move_back(user_move)
                cell_type = Wall()
                water = False
                wall = True

                # If a game has been initialised for the solver, there is no need to print.
                if not solve:
                    print(self.update_board())
                    cell_type.print_message(water)
                    return

            if self.player.row <0 or self.player.col <0:
                # Bounces the player back if they walk out of bouds on the left or top of board.
                self.game_move_back(user_move)
                cell_type = Wall()
                water = False
                wall = True

                # If a game has been initialised for the solver, there is no need to print.
                if not solve:
                    print(self.update_board())
                    cell_type.print_message(water)
                    return

            
            ''' Checks the kind of cell the player has moved to, and reacts accordingly.'''
            #checks if moving into wall
            if type(self.game_grid[self.player.row][self.player.col]) == Wall:
                pos = self.game_move_back(user_move)
                wall = True
            else:
                self.moves_made.append(user_move.lower())
            self.update_board()

            #checks if moving into fire
            if type(self.game_grid[self.player.row][self.player.col]) == Fire:
                if self.player.num_water_buckets > 0:
                    self.player.num_water_buckets -= 1
                    self.game_grid[self.player.row][self.player.col] = Air()
                    water = True
                    self.game_state = "game in progress"
                    
                else:
                    self.win = False
                    water = False
                    self.game_state = "game lost" #used to check how the game has ended in solver
            else:

                #checks if moving onto water
                if type(self.game_grid[self.player.row][self.player.col]) == Water:
                    self.player.num_water_buckets += 1
                    self.game_grid[self.player.row][self.player.col] = Air()
                    

                #checks if moving onto telepads
                #Uses the tele pairs defined above, checks which one the player is currently on, and swaps them to the other one of the pair.
                if type(self.game_grid[self.player.row][self.player.col]) == Teleport and not wall:

                    current_cell = self.game_grid[self.player.row][self.player.col]
                    tele_index = int(current_cell.display) - 1 #accounts for teleport pair one being at index 0

                    if self.player.col == self.tele_pairs[tele_index][0][0] and self.player.row == self.tele_pairs[tele_index][0][1]:
                        self.player.col = self.tele_pairs[tele_index][1][0]
                        self.player.row = self.tele_pairs[tele_index][1][1]

                    elif self.player.col == self.tele_pairs[tele_index][1][0] and self.player.row == self.tele_pairs[tele_index][1][1]:
                        self.player.col = self.tele_pairs[tele_index][0][0]
                        self.player.row = self.tele_pairs[tele_index][0][1]
                

            # If a game has been initialised for the solver, there is no need to print.
            if not solve:
                print(self.update_board())
                cell_type.print_message(water)

        # Prints an error message if an invalid move is entered
        except ValueError as ve:
            print(self.update_board())
            print("\n{}".format(ve))
            
        # checks if moving to ending cell
        if type(self.game_grid[self.player.row][self.player.col]) == End:
            self.game_state = "game won" #used to check how the game has ended in solver




    def play(self,play,solve):
        ''' Takes user input and passed it into the make_move method. Handles the ending of the game (won/loss)

        Arguments:
            play --     a Boolean value of whether the game is in play mode (clears after each move)
            solve --    a boolean value of whether the game object is being used for the solver.'''
        #takes input
        user_move = input("\nInput a move: ")
        if play:
            os.system("clear")

        self.make_move(play,user_move,solve)

        # Continues to ask for and execute moves until the game has been won/lost
        while self.game_state == "game in progress":
            user_move = input("\nInput a move: ")
            if play:
                os.system("clear")
            self.make_move(play,user_move,solve)

        # Once the game has ended, checks if the game has been won/lost and prints the appropriate message, along with the moves made and count.
        if self.win:
            print("\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
            
            if len(self.moves_made) == 1:
                print("\nYou made {} move.".format(len(self.moves_made)))
                print("Your move: {}".format(", ".join(self.moves_made)))
            
            else:
                print("\nYou made {} moves.".format(len(self.moves_made)))
                print("Your moves: {}".format(", ".join(self.moves_made)))
            print("\n=====================\n====== YOU WIN! =====\n=====================")
        
        
        else:
            print("\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.")
            
            if len(self.moves_made) == 1:
                print("\nYou made {} move.".format(len(self.moves_made)))
                print("Your move: {}".format(", ".join(self.moves_made)))
            
            else:
                print("\nYou made {} moves.".format(len(self.moves_made)))
                print("Your moves: {}".format(", ".join(self.moves_made)))
            print("\n=====================\n===== GAME OVER =====\n=====================")



    """
    Methods used for solver.py
    """
    def path_is_valid(self,moves):
        '''Takes a set of moves and checks if they are valid.

        Arguments: 
            moves -- a string of moves (wsade)

        Returns: 
            boolean -- whether or not the path is valid given the board. '''

        # Creates a grid to keep track of the visited cells
        # The looping is done to make copies of the list in for each row
        # so that they don't all point to the same memory location.
        line = [False]*len(self.game_grid[0])
        visited = []
        for i in range(len(self.game_grid)):
            x = list(line)
            visited.append(x)

        self.set_start_pos()

        # prevents e from appearing more than 3 times in a row
        if "eeee" in moves:
            return False

        # Sets the starting posistion as visited.
        visited[self.player.row][self.player.col] = True


        for move in moves:

            self.game_move(move)

            # resets the visited squares if the block is water, as the player may need to backtrack after picking up water.
            try:
                if type(self.game_grid[self.player.row][self.player.col]) == Water:
                    line = [False]*len(self.game_grid[0])
                    visited = []
                    for i in range(len(self.game_grid)):
                        x = list(line)
                        visited.append(x)
        
                    self.game_grid[self.player.row][self.player.col] = Air
                    
                # checks if the player has left the board to the left or top
                if type(self.game_grid[self.player.row][self.player.col]) == Wall or self.player.row <0 or self.player.col <0: 
                    return False

                # checks if the cell has already been visited
                if visited[self.player.row][self.player.col]:
                    return False


                visited[self.player.row][self.player.col] = True
            
            except IndexError: # checks if the player has left the board to the right or bottom
                return False
        
        return True


    def winning_path(self, moves):
        ''' Takes a valid path (as checked with game.path_is_valid()) and checks if following the path wins the game.

        Arguments: 
            moves -- a string of moves (wsade)

        Returns: 
            boolean -- whether or not the path wins the game given a board. '''
        # ensures the player is at the start (in case the game object has been used for something first)
        self.set_start_pos()

        # follows the path in a game object, checking if the path allows the player to win
        for move in moves:
            self.make_move(False,move, True)
            if self.game_state == "game lost":
                return False

        if type(self.game_grid[self.player.row][self.player.col]) == End:
            return True

        return False
