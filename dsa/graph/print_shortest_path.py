"""

Print Shortest Path

Given a weighted undirected graph having n vertices numbered from 1 to n and m edges describing there are edges,
where edges[i]=[ai,bi,wi], representing an edge from vertex ai to bi with weight wi.

Find the shortest path between the vertex 1 and the vertex n and if path does not exist then return a list
consisting of only -1.

If there exists a path, then return a list whose first element is the weight of the path and the remaining
elements represent the shortest path from vertex 1 to vertex n.

Note: On IDE only the total sum of weights will be shown as output. As there might be more than one path
(The path will be validated through driver code and If wrong then output shown will be -2.).

Example 1
Input: n = 5, m= 6, edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
Output: 5 1 4 3 5
Explanation: The source vertex is 1. Hence, the shortest distance path of node 5
from the source will be 1->4->3->5 as this is the path with a minimum sum of edge weights from source to destination.

Example 2
Input: n = 4, m = 4, edges = [[1,2,2], [2,3,4], [1,4,1],[4,3,3]]
Output:1 1 4
Explanation: The source vertex is 1. Hence, the shortest distance path of node 4 from the source will
be 1->4 as this is the path with the minimum sum of edge weights from source to destination.

Example 3
Input: n = 3, m = 1, edges = [[1,2,2]]
Output: -1

Constraints
    2 <= n <= 104
    0 <= m <= 2*104
    1 <= a, b <= n
    1 <= w <= 105

"""

import heapq


class Solution:
    # TC - O((N+M)*logN) for heap operations, SC - O(N)
    def printShortestPath(self, n, m, edges):
        """
        Idea:
        - Make Adjacency List from the edges
        - Also, keep Parent array and initiatize it to each node as parent
        - perform Djiktras algorithm, also make Parent changes in this part
        - Dist[n] will be total weight
        - To find the path:
            - We loop from node=destination until parent[node] is not node itself
            - Keep appending the 'node' to a list
            - In the end, append the source node
            - Reverse this to get out shortest path
        """
        adj = [[] for i in range(n + 1)]
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))

        dist = [float("inf")] * (n + 1)
        dist[1] = 0

        parent = [i for i in range(n + 1)]

        pq = []
        heapq.heappush(pq, (0, 1))

        while pq:
            curr_dist, node = heapq.heappop(pq)

            for nei, wt in adj[node]:
                if dist[node] + wt < dist[nei]:
                    dist[nei] = dist[node] + wt
                    parent[nei] = node
                    heapq.heappush(pq, (dist[nei], nei))

        if dist[n] == float("inf"):
            return [-1]

        # generate path
        node = n  # destination = n here
        path = []
        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(1)  # src = 1 here
        # add shortest path value
        path.append(dist[n])
        path = path[::-1]

        return path


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.printShortestPath(
            5, 6, [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
        )
    )
    print(obj.printShortestPath(4, 4, [[1, 2, 2], [2, 3, 4], [1, 4, 1], [4, 3, 3]]))
    print(obj.printShortestPath(3, 1, [[1, 2, 2]]))
