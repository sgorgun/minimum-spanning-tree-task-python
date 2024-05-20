"""Template for programming assignment: build MST using Prim's algorithm."""
from typing import List, Tuple


def prim_mst(n: int, adj_matrix: List[List[int]]) -> Tuple[List[int], int]:
    """
    Returns the order of adding vertices to the MST according to Prim's algorithm and
    the weight of the MST for an undirected weighted graph.
    The expected algorithm complexity is O(n^2).
    The vertices are enumerated from 0 to n-1, there n is the number of vertices.

    The starting vertex should be 0.
    If several vertices can be chosen at any iteration, the one with the smallest index 
    should be added. If no MST exists, please return (None, None).

    Suppose there is a graph with five vertices from 0 to 4 and an adjacency matrix
    [[0, 2, 0, 6, 0], 
     [2, 0, 3, 8, 5], 
     [0, 3, 0, 0, 7], 
     [6, 8, 0, 0, 9], 
     [0, 5, 7, 9, 0]].

    0 means the absence of an edge, and a positive value means an edge exists and shows its weight.
    The MST is {(0,1), (1,2), (0,3), (1,4)} with a weight of 16.
    The vertices are added to the MST in the following order [0, 1, 2, 4, 3].

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        adj_matrix (List[List[int]): adjacency matrix
    Returns:
        List[int], int: order of adding vertices to MST, weight of the MST
    """
    mst = [0]
    mst_weight = 0

    added_vertices = set([0])

    while len(mst) < n:
        min_weight = float('inf')
        min_vertex = None

        for vertex in added_vertices:
            for neighbor in range(n):
                if neighbor not in added_vertices and adj_matrix[vertex][neighbor] > 0:
                    if adj_matrix[vertex][neighbor] < min_weight:
                        min_weight = adj_matrix[vertex][neighbor]
                        min_vertex = neighbor

        if min_vertex is None:
            return (None, None)

        mst.append(min_vertex)
        mst_weight += min_weight
        added_vertices.add(min_vertex)

    return mst, mst_weight