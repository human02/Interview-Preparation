"""

Course Schedule I

There are a total of N tasks, labeled from 0 to N-1. Given an array arr where arr[i] = [a, b]
indicates that you must take course b first if you want to take course a.
Find if it is possible to finish all tasks.

Examples:
Input: N = 4, arr = [[1,0],[2,1],[3,2]]
Output: True
Explanation: It is possible to finish all the tasks in the order : 0 1 2 3.
First, we will finish task 0. Then we will finish task 1, task 2, and task 3.

Input: N = 4, arr = [[0,1],[3,2],[1,3],[3,0]]
Output: False
Explanation: It is impossible to finish all the tasks. Let’s analyze the pairs:
For pair {0, 1} -> we need to finish task 1 first and then task 0. (order : 1 0).
For pair{3, 2} -> we need to finish task 2 first and then task 3. (order: 2 3).
For pair {1, 3} -> we need to finish task 3 first and then task 1. (order: 3 1).
But for pair {3, 0} -> we need to finish task 0 first and then task 3 but task 0 requires task 1 and task 1 requires task 3.
So, it is not possible to finish all the tasks.

Input: N = 2, arr = [[1,0]]
Output: True

Constraints:
  1 <= N <= 2000
  0 <= arr.length <= 5000
  arr[i].length == 2
  0 <= arr[i][0], arr[i][1] < N
  All the pairs arr[i] are unique.

"""

from collections import deque


# TC - O(V+E), SC - O(V+E)
class Solution:
    def isPossible(self, n, arr):
        adj_list = [[] for _ in range(n)]
        for it in arr:
            adj_list[it[1]].append(it[0])

        return self.topoSort(adj_list, len(adj_list))

    def topoSort(self, adjL, V):
        indeg = [0 for _ in range(V)]
        q = deque()

        for i in range(V):
            for it in adjL[i]:
                indeg[it] += 1

        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for nei in adjL[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        if len(result) == V:
            return True
        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPossible(4, [[1, 0], [2, 1], [3, 2]]))
    print(obj.isPossible(4, [[0, 1], [3, 2], [1, 3], [3, 0]]))
    print(obj.isPossible(2, [[1, 0]]))
