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
        self.parent[key] = key

    def find_set(self, key: int) -> int:
        """Returns a unique set identifier (key) of a given key's set."""
        if self.parent[key] != key:
            self.parent[key] = self.find_set(self.parent[key])
        return self.parent[key]

    def union_sets(self, first_key: int, second_key: int):
        """Joins two given sets into a new one."""
        first_root = self.find_set(first_key)
        second_root = self.find_set(second_key)
        if first_root != second_root:
            self.parent[first_root] = second_root


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
    def get_weight(edge):
        return edge[2]
    edges.sort(key=get_weight)
    minimum_spanning_tree_weight = 0
    disjoint_sets = DisjointSets()

    for vertex in range(n):
        disjoint_sets.make_set(vertex)

    for edge in edges:
        u, v, weight = edge
        if disjoint_sets.find_set(u) != disjoint_sets.find_set(v):
            disjoint_sets.union_sets(u, v)
            minimum_spanning_tree_weight += weight

    root = disjoint_sets.find_set(0)
    for vertex in range(1, n):
        if disjoint_sets.find_set(vertex) != root:
            return None

    return minimum_spanning_tree_weight