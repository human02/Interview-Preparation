"""

Number of Connected Components in an Undirected Graph
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b]
means that there is an edge between node a and node b in the graph.
The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:
Input: n=3, edges=[[0,1], [0,2]]
Output: 1

Example 2:
Input: n=6, edges=[[0,1], [1,2], [2,3], [4,5]]
Output: 2

Constraints:
    1 <= n <= 100
    0 <= edges.length <= n * (n - 1) / 2

"""

from collections import deque


class Solution:
    # TC - O(V+E), SC - O(V+E)
    def connected_components(self, n, edges):
        adjL = [[] for i in range(n)]
        vis = [0] * n
        for u, v in edges:
            adjL[u].append(v)
            adjL[v].append(u)

        def bfs(root):
            q = deque([root])
            while q:
                node = q.popleft()
                vis[node] = 1
                for neighbor in adjL[node]:
                    if not vis[neighbor]:
                        q.append(neighbor)
                        vis[neighbor] = 1

        res = 0
        for i in range(n):
            if not vis[i]:
                bfs(i)
                res += 1
        return res


if __name__ == "__main__":
    obj = Solution()
    assert obj.connected_components(3, [[0, 1], [0, 2]]) == 1
    print(obj.connected_components(3, [[0, 1], [0, 2]]))
