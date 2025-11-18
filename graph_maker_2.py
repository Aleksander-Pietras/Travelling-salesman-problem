''' This program will hold a function that will create a graph.
The function will create both: adjecnacy matrix and distance matrix'''
import sys
import numpy as np
from validation_for_inputs import *


def make_graph(size: int = 1):
    """
    Build graph matrices based on the given size.

    Parameters
    ----------
    size : int,
        The number of nodes in the graph (default is 1).

    Returns
    -------
    tuple of (adjacency_matrix, direction_matrix, distance_matrix)
        - adjacency_matrix : 2D list or array
            Represents which nodes are connected.
        - direction_matrix : 2D list or array
            Represents the direction of edges between nodes.
        - distance_matrix : 2D list or array
            Represents the distances/weights between nodes.
    """
    adjacency_matrix = make_adjacency_matrix(size)
    direction_matrix = make_direction_matrix(size, adjacency_matrix)
    distance_matrix = make_distance_matrix(size, adjacency_matrix, direction_matrix)

    return adjacency_matrix, direction_matrix, distance_matrix

def make_adjacency_matrix(size: int) -> list:
    adjacency_matrix = []
    blank_matrix = valid_bool("Would you like a blank adjacency matrix")

    for row in range(size):
        temp_col = []
        for col in range(size):
            if row == col or blank_matrix:
                temp_col.append(0)
            else:
                temp_col.append(1)

        adjacency_matrix.append(temp_col)

    print(adjacency_matrix)

    changes = valid_bool("Would you like to make changes to the matrix")

    if changes:
        adjacency_matrix = make_changes_to_matrix(adjacency_matrix, size)
        return adjacency_matrix
    else:
        return adjacency_matrix

def make_direction_matrix(size: int, adjacency_matrix) -> list:
    raise NotImplementedError

def make_distance_matrix(size: int, adjacency_matrix, direction_matrix) -> list:
    raise NotImplementedError

def make_changes_to_matrix(size: int, matrix: list):
    temp_matrix = matrix.copy()


    




if __name__ == "__main__":
    make_graph(5)
    make_graph(10)