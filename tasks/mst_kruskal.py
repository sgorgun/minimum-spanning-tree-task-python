"""Template for programming assignment: build MST using the Kruskal algorithm."""
from typing import List, Tuple


class DisjointSets:
    """
    Interface for supporting disjoint sets.

    Please use any desired heuristics, but expected time complexity for union and finding sets
    should be no more than O(logN), where N - number of elements in the disjoint set.
    """

    def __init__(self):
        # Add more class attributes to support desired heuristics.
        self.parent = {}

    def make_set(self, key: int):
        """Creates a new set that is associated to a given key."""
        pass

    def find_set(self, key: int) -> int:
        """Returns a unique set identifier (key) of a given's key set."""
        pass

    def union_sets(self, first_key: int, second_key: int):
        """Joins two given sets into a new one."""
        pass


def kruskal_mst(n: int, edges: List[List[int]]) -> int:
    """
    Returns the weight of MST for an undirected weighted graph.
    Expected algorithm complexity is O(MlogN), M - number of edges, M << N^2, where N - number of vertices.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    If no MST exists, please, return None.

    E.g. there is a graph with 5 vertices from 0 to 4 and list of edges
    [[0, 1, 1], [0, 2, 1], [2, 3, 5], [0, 3, 1], [2, 4, 7], [3, 4, 5]].
    Each edge is a combination of the indexes of the connected vertices and weight for this edge.
    MST is {(0,1), (0,2), (0,3), (3,4)} with weight 8.

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (List[Tuple[int, int, int]]): contains the indexes of the connected vertices and weight for this edge.
    Returns:
         int: weight of MST
    """
    pass
