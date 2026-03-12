"""

Shortest path in DAG

Given a Directed Acyclic Graph of N vertices from 0 to N-1 and M edges and a 2D Integer array edges,
where there is a directed edge from vertex edge[i][0] to vertex edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from source vertex to all the vertices and if it is impossible to reach any vertex,
then return -1 for that vertex. The source vertex is assumed to be 0.

Example 1
Input: N = 4, M = 2 edge = [[0,1,2],[0,2,1]]
Output: 0 2 1 -1
Explanation:
    Shortest path from 0 to 1 is 0->1 with edge weight 2.
    Shortest path from 0 to 2 is 0->2 with edge weight 1.
    There is no way we can reach 3, so it's -1 for 3.

Example 2
Input: N = 6, M = 7 edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
Output: 0 2 3 6 1 5
Explanation:
    Shortest path from 0 to 1 is 0->1 with edge weight 2.
    Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3.
    Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6.
    Shortest path from 0 to 4 is 0->4 with edge weight 1.
    Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.

Example 3
Input: N = 3, M = 3 edge = [[0, 1, 4], [0, 2, 2], [1, 2, 5]]
Output: 0 4 2

Constraints
    1 ≤ N,M ≤ 5*104
    0 ≤ edge[i][0],edge[i][1] < N-1
    1 ≤ edge[i][2] < 104

"""

from collections import deque


class Solution:
    # TC - O(V+E), SC - O(V+E) due to adj list storage
    def findShortestPath(self, n, m, edge):
        """
        Idea:
        - Its a directed graph w/o unit weighted edges.
        - We cant use BFS here
        - We need to create Adjacency List but diff from normal:
            - We store from -> to,weight like:
                - 6 -> {4,2},{5,3} in pairs
        - Start with toposort on the graph
        - take each node and relax the edges
            - distance array needed, default val = 'inf'
            - Src node distance is set to 0
            - process each node from topo order
        - if a node is unreachable, update distance to -1

        """
        adj = [[] for _ in range(n)]

        # create adjacency list(tweaked)
        for u, v, wt in edge:
            adj[u].append((v, wt))

        def topoSort(V, adj):
            indeg = [0] * V
            q = deque()

            for i in range(V):
                for nei, wei in adj[i]:
                    indeg[nei] += 1

            for i in range(V):
                if indeg[i] == 0:
                    q.append(i)

            result = []
            while q:
                node = q.popleft()
                result.append(node)

                for nei, wt in adj[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
            return result

        topoOrder = topoSort(n, adj)

        dist = [float("inf")] * n
        dist[0] = 0  # As src node = 0

        for node in topoOrder:
            for v, wt in adj[node]:
                # relaxing the edges
                if dist[node] + wt < dist[v]:
                    dist[v] = dist[node] + wt

        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist


if __name__ == "__main__":
    obj = Solution()
    print(obj.findShortestPath(4, 2, [[0, 1, 2], [0, 2, 1]]))
    print(
        obj.findShortestPath(
            6,
            7,
            [
                [0, 1, 2],
                [0, 4, 1],
                [4, 5, 4],
                [4, 2, 2],
                [1, 2, 3],
                [2, 3, 6],
                [5, 3, 1],
            ],
        )
    )
    print(obj.findShortestPath(3, 3, [[0, 1, 4], [0, 2, 2], [1, 2, 5]]))
