# acorn-maze-game
A basic maze game built in python!

This is a project I did in my first semester of uni. In the project, I created a basic maze game, played in the command line.

Code was origianlly written in pyhton 3.7, but has been tested and works in 3.11

## Running the Game

To run the game, the command is:
```
$ python3 run.py <filename> [play]
```

For example:
```
$ python3 run.py BOARDS/board_basic.txt True
```

In the `<filename>` spot, the board that you wnt to play must be specified. The boards are available in the `BOARDS/` folder.

The `[play]` boolean flag is optional. 
- If `True` is included after the `<filename>`, the command line will clear on each turn, so that the board essentially 'updates', instead of being reprinted below.
- If the flag is ommited, or set to `False`, then each board update will just print below the previous.


## Basic Mechanics
This game is a WASD game, with the aim of reaching the 'Y' goal. Each turn, you will be promted with 
```
Input a move:
```

These are the possible commands that you can enter. Note that these are case sensistive.

|Command|Function|
|-|-|
|w |Move up|
|a |Move left|
|s |Move down|
|d |Move right|
|e |Wait a turn|
|q |Quit the game|

- note that if a plyer 'waits' on a teleport square, they will be teleported again.

## The Game Board
The game board is made up of 'cells', which can contain any of the following symbols...

|Cell character|Meaning|
|-|-|
|A |Player cell (stands for Acorn)|
|'' |Air cell (space bar)|
|X |Starting cell|
|Y |Ending/Goal cell|
|\* |Wall cells|
|1, 2, 3, 4, 5, 6, 7, 8, 9| Teleport cells. These numbers will come in pairs. On stepping onto the cell, you enter the cell '1', you teleport to the other '1'. Values greater than 9 will not be given. Note: 0 is not a valid teleport pad!|
|W|A water bucket cell. On stepping onto the cell, the player gains a water bucket.
|F |A fire obstacle that you cannot pass unless you have a water bucket.|


## Solver
The solver allows you to run a DFS (depth first search) or BFS (breadth first search) search on a board and get a winning path. To run the solver, use the following command

```
$ python3 solver.py <filename> <mode>
```

For example:

```
$ python3 solver.py BOARDS/board_basic.txt BFS
Path has 7 moves.
Path: s, d, d, d, d, s, s
```

In the `<filename>` spot, the board that you wnt to play must be specified. The boards are available in the `BOARDS/` folder.

The `<mode>` can either be `BFS` or `DFS`

The output will be the number of moves, and the path taken. If there is no possible path, then the response will be `There is no possible path.`

## Tests
To run all tests (unit and e2e), run
```
$ python3 test_all.py
```