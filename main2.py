def floyd_warshall(graph):
    # Numărul de noduri
    n = len(graph)

    # Inițializarea matricei de distanțe
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
        dist[i][i] = 0

    # Algoritmul Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Exemplu de graf (matrice de adiacență)
graph = [
    [0, 3, 8, -4],
    [float('inf'), 0, 1, 7],
    [4, float('inf'), 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

# Apelarea funcției și afișarea rezultatului
distances = floyd_warshall(graph)
for row in distances:
    print(row)
