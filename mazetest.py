from mazelib import Maze
from mazelib.generate import RecursiveBacktracking

maze = Maze()
maze.generator = RecursiveBacktracking()
maze.generate()

# Print the generated maze
maze.display()
