"""Template for programming assignment: build MST using the Prim's algorithm."""
from typing import List, Tuple


def prim_mst(n: int, edges: List[List[int]]) -> Tuple[List[int], int]:
    """
    Returns the order of adding vertices to MST according to the Prim's algorithm and
    the weight of MST for an undirected weighted graph.
    Expected algorithm complexity is O(N^2), N - number of vertices.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    Starting vertex should be 0.
    If there are several possible vertices to choose at any iteration,
    vertex with the smallest index should be added.
    If no MST exists, please, return (None, None).

    E.g. there is a graph with 5 vertices from 0 to 4 and adjacency matrix with weight
    [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]].
    0 means absence of edge, positive value means edge existence and shows its weight.
    MST is {(0,1), (1,2), (0,3), (1,4)} with weight 16.
    Order of adding vertices to MST is [0, 1, 2, 4, 3].

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (List[List[int]): adjacency matrix
    Returns:
        List[int], int: order of adding vertices to MST, the weight of MST
    """
    pass
