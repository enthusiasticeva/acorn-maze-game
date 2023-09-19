"""
Author:  Eva Jessurun
Date:    28 May 2020
Purpose: A script that generates paths and tests them using the game class (game.py). 
         The order in which these paths are generated and tested is dictated by the 
         BFS (breadth first search) or DFS (depth first search) system argument.
"""


from game import *
from collections import deque #double ended queue
import sys

def solve(mode, filename):
    if mode == "DFS":
        nodes_ls = []
    elif mode == "BFS":
        nodes_ls = deque()

    moves = ['w','a','s','d','e']

    # Appends the initial possible moves to the queue or stack
    for m in moves:
        game = Game(filename, True)
        if game.path_is_valid(m):
            nodes_ls.append(m)

    # Loops through all paths in the queue or stack
    while nodes_ls:
        path = nodes_ls.pop()
        ga = Game(filename, True)

        #takes the current path and tests what paths off it (wsad) are valid
        for m in moves:
            if ga.path_is_valid(path+m):
                nodes_ls.append(path+m)

        # checks if the current path could win the game.
        g = Game(filename, True)
        won = g.winning_path(path)

        if won:
            return(path)

    return False




if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 solver.py <filename> <mode>")
        sys.exit()

    filename = sys.argv[1]
    mode = sys.argv[2]

    # takes the filename and mode from the system arguments and uses them to run the solve() function
    solution = solve(mode, filename)

    if solution:
        path_list = list(solution)
        print("Path has {} moves.".format(len(solution)))
        print("Path: {}".format(", ".join(path_list)))

    else:
        print("There is no possible path.")
