"""Template for programming assignment: build MST using Kruskal's algorithm."""
from typing import List


class DisjointSets:
    """
    Interface for supporting disjoint sets.

    You may use whatever heuristics you desire, but the expected time complexity 
    for the `union_sets` and `find_set` should be no more than O(logN), 
    where N is the number of elements in the disjoint set.
    """

    def __init__(self):
        # Add more class attributes to support the desired heuristics.
        self.parent = {}

    def make_set(self, key: int):
        """Creates a new set that is associated with a given key."""
        pass

    def find_set(self, key: int) -> int:
        """Returns a unique set identifier (key) of a given key's set."""
        pass

    def union_sets(self, first_key: int, second_key: int):
        """Joins two given sets into a new one."""
        pass


def kruskal_mst(n: int, edges: List[List[int]]) -> int:
    """Returns the weight of the MST for an undirected weighted graph.

    The expected algorithm complexity is O(MlogM), where M is the number of edges, M << n^2, 
    and n is the number of vertices.
    
    The vertices are enumerated from `0` to `n-1`.

    If no MST exists, please, return None.

    Suppose there is a graph with five vertices from 0 to 4 and the list of edges
    [[0, 1, 1], [0, 2, 1], [2, 3, 5], [0, 3, 1], [2, 4, 7], [3, 4, 5]].
    Each edge is a combination of its weights and the indexes of the connected vertices.
    The MST is {(0,1), (0,2), (0,3), (3,4)} and has a weight of 8.

    Parameters:
        n (int) : number of vertices in the graph
        edges (List[Tuple[int, int, int]]): contains the indexes of the connected vertices and weight of this edge.
    Returns:
         int: weight of MST
    """
    pass
