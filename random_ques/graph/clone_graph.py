"""
Clone Graph

Given a node in a connected undirected graph, return a deep copy of the graph.
Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists,
used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph.
The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.

Example 2:
Input: adjList = [[]]
Output: [[]]
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque


class Solution:
    def cloneGraph(self, node):
        # If the input node is None, return None (empty graph)
        if not node:
            return None

        oldToNew = {}  # Dictionary to map original nodes to their clones
        oldToNew[node] = Node(node.val)  # Clone the root node
        q = deque([node])  # Initialize queue for BFS traversal

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    # If neighbor hasn't been cloned yet, clone and add to queue
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                # Add the cloned neighbor to the current node's clone neighbors list
                oldToNew[cur].neighbors.append(oldToNew[nei])

        # Return the clone of the input node (root of the cloned graph)
        return oldToNew[node]
