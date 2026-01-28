"""

Floyd Warshall algorithm

Given a graph of V vertices numbered from 0 to V-1. Find the shortest distances between every pair of vertices
in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n x n.
Matrix[i][j] denotes the weight of the edge from i to j. If matrix[i][j] =- 1, it means there is no edge from i to j.

Examples 1:
Input: matrix = [[0, 2, -1, -1],[1, 0, 3, -1],[-1, -1, 0, 1],[3, 5, 4, 0]]
Output: [[0, 2, 5, 6], [1, 0, 3, 4], [4, 6, 0, 1], [3, 5, 4, 0]]
Explanation: matrix[0][0] is storing the distance from vertex 0 to vertex 0,
the distance from vertex 0 to vertex 1 is 2 and so on.

Examples 2:
Input: matrix = [[0,25],[-1,0]]
Output: [[0, 25],[-1, 0]]
Explanation: The matrix already contains the shortest distance.

Examples 3:
Input: matrix = [[0,1,43],[1,0,6],[-1,-1,0]]
Output: [[0, 1, 7], [1, 0, 6], [-1, -1, 0]]

Constraints:
    1 <= n <= 100
    -1 <= matrix[i][j] <= 1000

"""


class Solution:
    """
    Idea:
    - Dijkstra's and Bellman Ford are for single-source shortest path.
    - Floyd Warshall is for multi source shortest path.
    - It works effectively for both directed and undirected graphs.
    - It also handles negative weights.
    - It main idea is "visit VIA each node".
    - It uses Adjacency Matrix - Distance Matrix that:
        - Store weight to reach from i to j as matrix[i][j] value
    """

    # TC - O(n^3), SC - O(n^2)
    def distances_using_floyd(self, matrix):
        n = len(matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # skip k if its not in matrix
                    if matrix[i][k] == -1 or matrix[k][j] == -1:
                        continue

                    if matrix[i][j] == -1:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
                    else:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


if __name__ == "__main__":
    obj = Solution()
    matrix = [[0, 2, -1, -1], [1, 0, 3, -1], [-1, -1, 0, 1], [3, 5, 4, 0]]
    obj.distances_using_floyd(matrix)
    for row in matrix:
        print(row)
    print(f"{"-"*20}\n")
    matrix = [[0, 25], [-1, 0]]
    obj.distances_using_floyd(matrix)
    for row in matrix:
        print(row)
    print(f"{"-"*20}\n")
    matrix = [[0, 1, 43], [1, 0, 6], [-1, -1, 0]]
    obj.distances_using_floyd(matrix)
    for row in matrix:
        print(row)
    print(f"{"-"*20}\n")
