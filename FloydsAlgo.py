
# The number of vertices
nV = 5  # Change the number of vertices as needed

INF = float('inf')  # Using float('inf') as a representation of infinity

# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)

# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

# Change the graph as needed
G = [
    [0, 3, INF, 5, INF],
    [2, 0, INF, 4, INF],
    [INF, 1, 0, INF, INF],
    [INF, INF, 2, 0, INF],
    [INF, INF, INF, 1, 0]
]

floyd_warshall(G)
