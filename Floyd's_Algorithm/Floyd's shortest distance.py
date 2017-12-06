INF = 99999


def floyd_warshall(graph, v_number):
    dist = [row[:] for row in graph]

    for k in range(v_number):
        for i in range(v_number):
            for j in range(v_number):
                dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))
    print(dist)


def main():
    v = 4
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]
    floyd_warshall(graph, v)


if __name__ == "__main__":
    main()
