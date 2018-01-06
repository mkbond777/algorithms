class graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, u, v):

    def kruskal_mst(self):
        self.graph = sorted(self.graph, key=lambda items: items[2])
        parent = []

        for node in range(self.V):
            parent = parent[node]

        e = 0
        i = 0
        while e < self.V - 1:
            edge = self.graph[i]
            i += 1
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])

            if x != y:
                result = self.graph[i]
                self.union(parent, x, y)
