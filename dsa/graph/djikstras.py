"""
Dijkstra's algorithm

Given a weighted, undirected graph of V vertices, numbered from 0 to V-1, and an adjacency list
adj where adj[i] represents all edges from vertex i. Each entry in adj[i] is of the form [to, weight], where:

to → the neighboring vertex connected to i,
weight → the weight of the edge between i and to.

Given a source node S. Find the shortest distance of all the vertex from the source vertex S.
Return a list of integers denoting shortest distance between each node and source vertex S.
If a vertex is not reachable from source then its distance will be 109.

Examples:
Input: V = 2, adj [] = [[[1, 9]], [[0, 9]]], S=0
Output: [0, 9]
Explanation:
The shortest distance from node 0(source) to node 0 is 0 and the shortest distance from node 0 to node 1 is 9.

Input: V = 3,adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], S=2
Output: [4, 3, 0]
Explanation:
For node 0, the shortest path is 2->1->0 (distance=4)
For node 1, the shortest path is 2->1 (distance=3)

Input: V=4, adj = [[[1, 1], [3, 2]],[[0, 1], [2, 4]],[[1, 4], [3, 3]], [[0, 2], [2, 3]]], S=0
Output:[0, 1, 5, 2]

Constraints:
1 ≤ V ≤ 10000
0 ≤ adj[i][j] ≤ 10000
1 ≤ adj.size() ≤ [ (V*(V - 1)) / 2 ]
0 ≤ S < V

"""

import heapq


class Solution:
    # TC - O((V+E)*logV), SC - O(V)
    def distance_using_djikstra(self, V, adj, src):
        distances = [int(1e9)] * V
        distances[src] = 0
        pq = []
        heapq.heappush(pq, [0, src])
        while pq:
            dist, node = heapq.heappop(pq)
            for neighbor, weight in adj[node]:
                if dist + weight < distances[neighbor]:
                    distances[neighbor] = dist + weight
                    heapq.heappush(pq, [distances[neighbor], neighbor])
        return distances


if __name__ == "__main__":
    obj = Solution()
    print(obj.distance_using_djikstra(4, [[[1, 9]], [[0, 9]]], 0))
    print(
        obj.distance_using_djikstra(
            3, [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], 2
        )
    )
    print(
        obj.distance_using_djikstra(
            4,
            [[[1, 1], [3, 2]], [[0, 1], [2, 4]], [[1, 4], [3, 3]], [[0, 2], [2, 3]]],
            0,
        )
    )
