import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for columns in range(vertices)] for rows in range(vertices)]

    def min_dist(self, dist, spt_set):
        minm = sys.maxsize

        near_vertex = 0
        for k in range(self.V):
            if dist[k] < minm and spt_set[k] is False:
                minm = dist[k]
                near_vertex = k
        return near_vertex

    def dijkstra(self, src):
        inf = sys.maxsize
        dist = [inf] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for temp in range(self.V):
            u = self.min_dist(dist, spt_set)
            spt_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and spt_set[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        print(dist)


def main():
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    g.dijkstra(0)


if __name__ == "__main__":
    main()
