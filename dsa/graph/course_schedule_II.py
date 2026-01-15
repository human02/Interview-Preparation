"""

Course Schedule II

There are a total of N tasks, labeled from 0 to N-1. Given an array arr where arr[i] = [a, b] indicates that
you must take course b first if you want to take course a. Find the order of tasks you should pick to finish
all tasks. If no such ordering exists, return an empty array. Since multiple valid answers are possible, the
final output will be 1 if your solution is correct, otherwise 0.

Examples:
Input: N = 4, arr = [[1,0],[2,1],[3,2]]
Output: [0, 1, 2, 3]
Explanation: First,finish task 0, as it has no prerequisites. Then,finish task 1, since it depends only on task 0. After that,finish task 2, since it depends only on task 1. Finally,finish task 3, since it depends only on task 2

Input: N = 4, arr = [[0,1],[3,2],[1,3],[3,0]]
Output: []
Explanation: It is impossible to finish all the tasks. Let’s analyze the pairs:
For pair {0, 1} → we need to finish task 1 first and then task 0 (order: 1 → 0).
For pair {3, 2} → we need to finish task 2 first and then task 3 (order: 2 → 3).
For pair {1, 3} → we need to finish task 3 first and then task 1 (order: 2 → 3 → 1 → 0).
But for pair {3, 0} → we need to finish task 0 first and then task 3, which contradicts the previous order. So, it is not possible to finish all the tasks.

Input: N = 2, arr = [[1,0]]
Output: [0, 1]

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
    def courseOrder(self, n, arr):  # O(V) + O(E) + O(V + E) = O(V + E)

        adj_list = [[] for _ in range(n)]  # O(V)
        for it in arr:  # O(E)
            adj_list[it[1]].append(it[0])

        def topoSort(self, adjL, V):  # TC - O(V+E)
            indeg = [0] * V
            q = deque()

            for i in range(V):  # O(V)
                for it in adjL[i]:  # Total O(E) across all iterations
                    indeg[it] += 1

            for i in range(V):  # O(V)
                if indeg[i] == 0:
                    q.append(i)

            result = []
            while q:  # O(V)
                node = q.popleft()
                result.append(node)

                for nei in adjL[node]:  # Total O(E) across all iterations
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)

            if len(result) == V:
                return result
            else:
                return []

        return topoSort(adj_list, len(adj_list))


if __name__ == "__main__":
    obj = Solution()
    print(obj.courseOrder(4, [[1, 0], [2, 1], [3, 2]]))
    print(obj.courseOrder(4, [[0, 1], [3, 2], [1, 3], [3, 0]]))
    print(obj.courseOrder(2, [[1, 0]]))
