import random
import pygame
import sys

# Set up the dimensions of the window and colors
WIDTH = int(input("Dimensions: "))  # Width of the maze (in cells)
HEIGHT = WIDTH  # Height of the maze (in cells)
CELL_SIZE = 600 / WIDTH + 1  # Size of each cell (pixels)
WHITE = (255, 255, 255)  # Color for open spaces
BLACK = (0, 0, 0)  # Color for walls
RED = (255, 0, 0)  # Color for the start point

def generate_maze(width, height):
    # Create grid initialized with walls
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    # Starting point
    start_x, start_y = 1, 1
    maze[start_y][start_x] = ' '  # Start position
    
    # Stack for DFS
    stack = [(start_x, start_y)]
    
    # Directions for movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        x, y = stack[-1]
        valid_moves = []
        
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                valid_moves.append((dx, dy, nx, ny))
        
        if valid_moves:
            dx, dy, nx, ny = random.choice(valid_moves)
            maze[ny][nx] = ' '  # Mark as empty space
            maze[y + dy][x + dx] = ' '  # Knock down the wall between
            stack.append((nx, ny))
        else:
            stack.pop()
    
    return maze

def display_maze(maze):
    pygame.init()
    
    # Create the Pygame window
    screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Maze Display")

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the background with white
        screen.fill(WHITE)
        
        # Draw the maze
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if maze[y][x] == '#':  # Wall
                    color = BLACK
                elif maze[y][x] == ' ':  # Empty space
                    color = WHITE
                if (x, y) == (1, 1):  # Start point (for visualization)
                    color = RED
                
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()
    sys.exit()

# Example usage
maze = generate_maze(WIDTH, HEIGHT)
display_maze(maze)
