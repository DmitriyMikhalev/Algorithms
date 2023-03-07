"""
Dijkstra's algorithm. Complexity is O(N^2) for adjacency matrix and O(M*logN)
for adjacency list (M is count of edges, N is count of vertices).

Finding the shortest paths from a given vertex to all others:
    1. Create an array of N elements with inf values (paths to vertices).
    2. Create a set of visited vertices.
    3. Create an array of ways (index - to vertex, value - from vertex I came).
    4. The initial vertex in the array is marked 0.
    5. Until all the vertices have been visited:
      * Take the unvisited vertex with the minimum value (for the first time it
        is initial, 0);
      * Search for all possible neighbors of this vertex;
      * For each neighbor that has not been visited yet, put in the array
        minimum value among "current" and "previous minimum + edge to
        the current vertex from the previous one". If value was changed,
        update ways array;
      * Mark the vertex visited.
    6. Return the result-array and ways-array.

To get the optimal way move from end to start and reverse the result.
For example, for 0 vertex:
res:  [0, 3, 1, 3, 8, 5] (it is shortest paths to vertices )
       1  2  3  4  5  6 vertices

ways: [0, 0, 0, 0, 2, 3] (it is indexes of vertices)
       1  2  3  4  5  6 vertices

For way from 0 to 4 vertex:
    * add 4
    * to 4 I came from ways[4] = 2 (index)
    * to 2 I came from ways[2] = 0 (index)

So way is 0 -> 2 -> 4 (indexes) and 1 -> 3 -> 5 by numbers
"""
import sys
from typing import Iterator

INF = sys.maxsize


matrix = [
    [0, 3, 1, 3, 0, 0],
    [3, 0, 4, 0, 0, 0],
    [1, 4, 0, 0, 7, 5],
    [3, 0, 0, 0, 0, 2],
    [0, 0, 7, 0, 0, 4],
    [0, 0, 5, 2, 4, 0]
]


def dijkstra(
    matrix: list[list[int]],
    start: int = 0
) -> tuple[list[int], list[int]]:
    count_verts = len(matrix)
    res = [INF] * count_verts
    shortest_ways = [0] * count_verts
    res[start] = 0
    visited_vert = {start}
    vertex = start

    while vertex != -1:
        for neighbour in get_neighbours(vertex=vertex, matrix=matrix):
            if neighbour not in visited_vert:
                new_val = res[vertex] + matrix[vertex][neighbour]
                if new_val < res[neighbour]:
                    res[neighbour] = new_val
                    shortest_ways[neighbour] = vertex
        vertex = get_min_vertex(res, visited_vert)
        if vertex != -1:
            visited_vert.add(vertex)

    return res, shortest_ways


def get_min_vertex(row: list[int], visited: set[int]) -> int:
    """
    If all vertices are visited returns -1, else returns index of not visited
    vertex with minimum value.
    """
    minimum_ind = -1
    maximum_val = max(row)
    for i, val in enumerate(row):
        if val < maximum_val and i not in visited:
            minimum_ind = i
            maximum_val = val

    return minimum_ind


def get_neighbours(vertex: int, matrix: list[list[int]]) -> Iterator[int]:
    """Generator of neighbours indexes."""
    for i, val in enumerate(matrix[vertex]):
        if val:
            yield i


def get_way(from_ind: int, to_ind: int, ways: list[int]) -> list[int]:
    way = [to_ind]
    while to_ind != from_ind:
        to_ind = ways[way[-1]]
        way.append(to_ind)

    way.reverse()

    return way


def main():
    matrix = [
        [0, 3, 1, 3, 0, 0],
        [3, 0, 4, 0, 0, 0],
        [1, 4, 0, 0, 7, 5],
        [3, 0, 0, 0, 0, 2],
        [0, 0, 7, 0, 0, 4],
        [0, 0, 5, 2, 4, 0]
    ]
    start_ind = int(input("Input index of start vertex: "))
    res, ways = dijkstra(matrix, start_ind)
    assert res == [0, 3, 1, 3, 8, 5]
    assert get_way(0, 4, ways) == [0, 2, 4]


if __name__ == '__main__':
    main()
