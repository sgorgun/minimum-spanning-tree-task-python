# Minimum Spanning Tree (MST)

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* Finding an MST and its weight

## Overview

The coding exercises cover the following practical problems:
* Building an MST using Kruskal's algorithm 
* Building an MST using Prim's algorithm

## Coding exercises

### Exercise 1: Building an MST using Kruskal's algorithm 

Given the number of vertices `n` and graph edges `edges` of an undirected weighted graph, implement the function below to find out the weight of the MST using Kruskal's algorithm. 
The vertices are enumerated from `0` to `n-1`. Each edge in `edges` is a combination of the indexes of the connected vertices and the weight of this edge.

The expected algorithm complexity is O(MlogM), where M is the number of edges, M << N^2, and N is the number of vertices.

If no MST exists, please return None.

```python
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
```

**Example 1:**
```mermaid
graph TD;
    A((0)) -- 1 --- B((1));
    B -- 1 --- C((2));
    C --5--- D((3));
    A --1---D;
    E((4));
    C --7--- E;
    D --5--- E;
```
`n` = 5
`edges` = [[0, 1, 1], [0, 2, 1], [2, 3, 5], [0, 3, 1], [2, 4, 7], [3, 4, 5]]

Expected result: 8.

**Example 2:**
```mermaid
graph TD;
    A((0)) --5--- B((1));
    A --10--- C((2));
    B--6---C;
```
`n` = 3
`edges` = [[1, 0, 5], [2, 0, 10], [1, 2, 6]]

Expected result: 11.

<br/>

Please use the template `tasks/mst_kruskal:kruskal_mst` for the implementation.


### Exercise 2: Building an MST using Prim's algorithm

Given the number of vertices `n` and the graph adjacency weighted matrix `edges` for an undirected weighted graph, implement the function below, which returns the order of adding vertices to the MST according to the Prim's algorithm and its weight. 

The expected algorithm complexity is O(N^2), where N is the number of vertices; M ~ N^2, and M is the number of edges.
The vertices are enumerated from `0` to `n-1`.

The starting vertex should be 0. If several vertices can be chosen at any iteration, the one with the smallest index should be added.  If no MST exists, please return (None, None).

```python
def prim_mst(n: int, edges: List[List[int]]) -> int:
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
```

**Example 1:**
```mermaid
graph TD;
    A((0)) -- 2  --- B((1));
    A --6--- D((3));
    B-- 3 --- C((2));
    B-- 8 --- D;
    B-- 5 --- E((4));
    C --7---E;
    D --9---E;
```
`n = 5`

`edges = [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]`

Expected result: `[0, 1, 2, 4, 3]`, `16`

**Example 2:**
```mermaid
graph TD;
    A((0)) -- 2  --- B((1));
    A --6--- D((3));
    B-- 3 --- C((2));
    B-- 8 --- D;
    E((4));
```

`n = 5`

`edges = [0, 2, 0, 6, 0], [2, 0, 3, 8, 0], [0, 3, 0, 0, 0], [6, 8, 0, 0, 0], [0, 0, 0, 0, 0]]`

Expected result: `None`, `None`


Please use a template for the implementation (`tasks/mst_prim:prim_mst`).
