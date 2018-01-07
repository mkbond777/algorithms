class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    @staticmethod
    def union_op(parent, rank, u, v):
        if rank[u] > rank[v]:
            parent[v] = u
        if rank[u] < rank[v]:
            parent[u] = v
        else:
            parent[u] = v
            rank[v] += 1

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal_mst(self):
        self.graph = sorted(self.graph, key=lambda items: items[2])
        parent = []
        rank = []
        result = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        e = 0
        i = 0
        while e < self.V - 1:
            edge = self.graph[i]
            i += 1
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])

            if x != y:
                e += 1
                result.append(edge)
                self.union_op(parent, rank, x, y)
        return result


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print(g.kruskal_mst())
