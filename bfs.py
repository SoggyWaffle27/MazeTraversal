from mazetest.py import generate_maze

class Graph():
    def __init__(self, verts, edges):
        self.edges = edges
        self.verts = verts

    def add_vert(self, v):
        self.verts.append(v)

    def add_edge(self, v, w):
        self.verts.append((v, w))

    def adj(self, v):
        out = []
        for i in self.edges:
            if v in i:
                out.append(i)
        return out
    
    def max_degree(self):
        max_e = 0
        for v in self.verts:
            max_e = max(max_e, len(self.adj(v)))
        return max_e
    
    def bfs(G, start):
        queue = []
        visited = set()
        queue.append(start)
        visited.add(start)
        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            for w in G.adj(v):
                if w not in visited:
                    visited.add(w)
                    queue.append(w)

    def path_to(self, v, w):
        queue = [[v]]
        visited = set([w])

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == w:
                return path

            for neighbor in self.adj(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append(new_path)

        return None  # No path found

G = Graph(["A", "B","C", "D","E", "F"], [("A", "B"),("A", "C"),("C", "D")])
print(G.max_degree())

maze = generate_maze(WIDTH, HEIGHT)
display_maze(maze)