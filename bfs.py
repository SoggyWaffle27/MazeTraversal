class Graph():
    def __init__(self, verts, edges):
        self.edges = edges
        self.verts = verts

    def add_vert(self, v):
        self.verts.append(w)

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

    def dfs(G, start):
        stack = []
        visited = set()
        stack.append(start)
        visited.add(start)
        while stack:
            v = stack.pop()
            print(v, end=" ")
            for w in G.adj(v):
                if w not in visited:
                    visited.add(w)
                    stack.append(w)
    

G = Graph(["A", "B","C", "D","E", "F"], [("A", "B"),("A", "C"),("C", "D")])
print(G.max_degree())