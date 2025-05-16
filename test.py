from pyamaze import maze, agent, COLOR

# Create a maze of size 10x10
m = maze(10, 10)
m.CreateMaze()

# Add an agent to the maze
a = agent(m, footprints=True)

# Trace the path using Depth-First Search
m.tracePath({a: m.path})

# Run the maze
m.run()