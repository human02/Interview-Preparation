"""

Disjoint Set

Design a disjoint set (also called union-find) data structure that supports the following operations:

DisjointSet(int n) initializes the disjoint set with n elements.
void unionByRank(int u, int v) merges the sets containing u and v using the rank heuristic.
void unionBySize(int u, int v) merges the sets containing u and v using the size heuristic.
bool areConnected(int u, int v) checks if the elements u and v are in the same set and returns true
if they are, otherwise false.


Example 1
Input:
["DisjointSet", "unionByRank", "unionBySize", "areConnected", "areConnected"]
[[5], [0, 1], [2, 3], [0, 1], [0, 3]]

Output:
[null, null, null, true, false]

Explanation:
DisjointSet ds = new DisjointSet(5); // Initialize a disjoint set with 5 elements
ds.unionByRank(0, 1); // Merge sets containing 0 and 1 using rank
ds.unionBySize(2, 3); // Merge sets containing 2 and 3 using size
ds.areConnected(0, 1); // Returns true as 0 and 1 are in the same set
ds.areConnected(0, 3); // Returns false as 0 and 3 are not in the same set

Example 2
Input:
["DisjointSet", "unionBySize", "unionBySize", "areConnected", "areConnected"]
[[3], [0, 1], [1, 2], [0, 2], [0, 1]]

Output:
[null, null, null, true, true]

Explanation:
DisjointSet ds = new DisjointSet(3); // Initialize a disjoint set with 3 elements
ds.unionBySize(0, 1); // Merge sets containing 0 and 1 using size
ds.unionBySize(1, 2); // Merge sets containing 1 and 2 using rank
ds.areConnected(0, 2); // Returns true as 0 and 2 are in the same set
ds.areConnected(0, 1); // Returns true as 0 and 1 are in the same set

Example 3:
Input:
["DisjointSet", "unionByRank", "unionBySize", "unionByRank", "areConnected", "areConnected"]
[[5], [0, 1], [3, 4], [1, 2], [0, 2], [1, 3]]

Output:
[null, null, null, null, true, false]

Constraints
    1 <= n <= 104
    0 <= u, v < n
    At most 5 * 104 calls will be made to unionByRank, unionBySize, and find

"""


# TC - O(1), SC - O(2N) parent and rank/size arrays
class DisjointSet:
    """
    Idea:
    - BFS/DFS use to find if 2 nodes are connected:
        - will be inefficient - O(V+E)
    - DS is useful for dynamic graphs.
        - Dyn Graph = Graphs that continiously changes its config
    - Connectivity can be checked in O(1) using DS.
    - In Union, we connect:
        - Smaller rank/size to Larger rank/size.
            - as we dont want to increase the length
            - More length = decrease in efficiency
    """

    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]  # [1,2,3,...]
        self.size = [1] * n

    # Finds ULTIMATE parent of a node
    def findUPar(self, node):
        """
        Idea:
        - Finds UltParent and does path compression
        """
        # if node's Ultimate Parent is itself
        if node == self.parent[node]:
            return node

        # path conpression by backtracking
        self.parent[node] = self.findUPar(self.parent[node])

        return self.parent[node]

    def unionByRank(self, u, v) -> None:
        # Find ultimate parents of both nodes
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        # both nodes in the same component
        if ulp_u == ulp_v:
            return False

        # Determines ranks of both parents
        if self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        elif self.rank[ulp_v] > self.rank[ulp_u]:
            self.parent[ulp_u] = ulp_v
        else:  # same rank, add to any of the two Ult Parent
            self.parent[ulp_u] = ulp_v
            self.rank[ulp_v] += 1

        return True

    def unionBySize(self, u, v) -> None:
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            # Update the size
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            # Update the size
            self.size[ulp_u] += self.size[ulp_v]

    # Determines if two nodes are in the same component or not
    def find(self, u, v):
        return self.findUPar(u) == self.findUPar(v)


if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.unionByRank(1, 2)  # Adding edge between 1 and 2
    ds.unionByRank(2, 3)  # Adding edge between 2 and 3
    ds.unionByRank(4, 5)  # Adding edge between 4 and 5
    ds.unionByRank(6, 7)  # Adding edge between 6 and 7
    ds.unionByRank(5, 6)  # Adding edge between 5 and 6
    # Checking if 3 and 7 are in the same component
    print(ds.find(3, 7))

    ds.unionByRank(3, 7)  # Adding edge between 3 and 7
    print(ds.find(3, 7))  # Checking again
