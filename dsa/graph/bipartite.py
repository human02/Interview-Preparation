"""

Bipartite graph

Given an undirected graph with V vertices labeled from 0 to V-1.
The graph is represented using an adjacency list where adj[i] lists all nodes connected to node.
Determine if the graph is bipartite or not.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that
every edge in the graph connects a node in set A and a node in set B.

Example 1
Input: V=4, adj = [[1,3],[0,2],[1,3],[0,2]]
Output: True
Explanation: The given graph is bipartite since, we can partition the nodes into two sets: {0, 2} and {1, 3}.

Example 2
Input: V=4, adj = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: False
Explanation: The graph is not bipartite.
    If we attempt to partition the nodes into two sets, we encounter an edge that connects
    two nodes within the same set, which violates the bipartite property.

Example 3
Input: V=5, adj = [[1,3],[0,2],[1,4],[0,4],[2,3]]
Output: False

Constraints
    E=number of edges
    1 ≤ V, E ≤ 104

"""

from collections import deque


class Solution:
    # TC - O(V+E), SC - O(V)
    def isBipartite(self, V, adj):
        """
        Idea:
        - A graph is bipartite if and only if it is 2-colorable.
        - Any linear graph with no cycle is a bipartite graph
        - A graph with cycle:
            - even length cycle is bipartite
            - Odd length cycle is NEVER bipartite
        - To check if a graph is bipartite, check if:
             - it nodes acan be colored alternatively
             - if alternative coloring is not possible = not bipartite
        - Use 'color' insterad of vis array:
             - -1 means uncolored
             - 0 and 1 are the 2 diff colors
        - We can start the BFS with any node, we start with node1.
        - We color uncolred nei nodes with opp color of node.
        - If we reach a colored node we check if coloring is correct or not.
        """
        color = [-1] * V

        def bfs(src):
            q = deque()

            q.append(src)  # add start node
            color[src] = 0  # update color of start node

            # BFS
            while q:
                node = q.popleft()

                for it in adj[node]:
                    # uncolored
                    if color[it] == -1:
                        color[it] = 1 - (color[node])
                        q.append(it)
                    # if colored, should not be the same as the adjacent color
                    elif color[it] == color[node]:
                        return False
            return True

        # if all node are not connected
        for i in range(V):
            if color[i] == -1:
                result = bfs(i)
                if not result:
                    return False
        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isBipartite(4, [[1, 3], [0, 2], [1, 3], [0, 2]]))
    print(obj.isBipartite(4, [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    print(obj.isBipartite(5, [[1, 3], [0, 2], [1, 4], [0, 4], [2, 3]]))
