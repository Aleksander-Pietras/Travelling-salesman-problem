''' This program uses the Nearest Neighbour Algorithm to find an approximate solution to the Travelling Salesman Problem'''

from random import randint

# Create a simple 5 x 5 graph

# The adjacency matrix determines how many edges there are between each vertex
# To keep it simple, it will be only one edge between each vertex: a complete graph
adjacency_matrix = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]

# The distance matrix determines the weight of each edge
distance_matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# I will randomise the weight of the graph so that it's easier to test if the algorithm works correctly
for i in range(0, 5):
    for j in range(0, 5):
        if i == j:
            distance_matrix[i][j] = 0
        else:
            distance_matrix[i][j] = randint(10, 100)


copy_distance_matrix = [row[:] for row in distance_matrix]



''' To find the shortest cycle starting at a vertex'''
# Start at vertex A
vertex = 0
order_of_visit = [0]
edge_distances = distance_matrix[0]

for i in range(0, len(distance_matrix)):
# To remove visited vertices
    for j in order_of_visit:
        edge_distances[j] = 0

    shortest_distance = 100_000

# Finds the shortest_distance between any two vertices
    for edge in edge_distances:
        if edge < shortest_distance and edge != 0:
            shortest_distance = edge
    
# To ensure a Hamiltonian cycle
    if shortest_distance == 100_000:
        vertex = 0 # This will force the path to return to the starting vertex

    else:
        vertex = edge_distances.index(shortest_distance)

    order_of_visit.append(vertex)
    edge_distances = distance_matrix[vertex]



''' Now to find the weight of the cycle'''
weight = 0
for i in range(len(order_of_visit) - 1):
    current_vertex = order_of_visit[i]
    next_vertex = order_of_visit[i + 1]
    weight += copy_distance_matrix[current_vertex][next_vertex]

# Add distance back to start (to close the loop)
weight += copy_distance_matrix[order_of_visit[-1]][order_of_visit[0]]

print(weight)

print(order_of_visit)

print(copy_distance_matrix)
