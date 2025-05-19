from mazetest import generate_maze, display_maze
from bfs import Graph


# Set up the dimensions of the window and colors
WIDTH = int(input("Dimensions: "))  # Width of the maze (in cells)
HEIGHT = WIDTH  # Height of the maze (in cells)
CELL_SIZE = (600 / WIDTH) + 0  # Size of each cell (pixels)
WHITE = (255, 255, 255)  # Color for open spaces
BLACK = (0, 0, 0)  # Color for walls
RED = (255, 0, 0)  # Color for the start point
BLUE = (126, 209, 246)

maze = generate_maze(WIDTH, HEIGHT)
display_maze(maze)