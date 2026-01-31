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
