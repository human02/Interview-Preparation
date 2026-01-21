"""

Cheapest flight within K stops

There are n cities and m edges connected by some number of flights.
Given an array of flights where flights[i] = [ fromi, toi, pricei] indicates that there is a flight from city from
i to city toi with cost pricei. Given three integers src, dst, and k, and return the cheapest price from src to dst
with at most k stops. If there is no such route, return -1.

Examples:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation: The optimal path with at most 1 stops from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:The optimal path with at most 1 stops from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Input: n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 0
Output: 500

Constraints:
  1 <= n <= 100
  0 <= flights.length <= (n * (n - 1) / 2)
   flights[i].length == 3
  0 <= fromi, toi < n
  fromi != toi
  1 <= pricei <= 104
  There will not be any multiple flights between the two cities.
  0 <= src, dst, k < n

"""

from collections import deque


class Solution:
    def cheapest_flight_within_k_stop(self, n, flights, src, dst, K):
        adjL = [[] for i in range(n)]

        for flight in flights:
            adjL[flight[0]].append((flight[1], flight[2]))

        distances = [float("inf")] * n
        distances[src] = 0
        q = deque([(0, src, 0)])

        while q:
            stops, node, distance = q.popleft()

            if stops > K:
                continue

            for neighbor, cost in adjL[node]:
                if cost + distance < distances[neighbor] and stops <= K:
                    distances[neighbor] = cost + distance
                    q.append((stops + 1, neighbor, distances[neighbor]))

        if distances[dst] == float("inf"):
            return -1
        return distances[dst]


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.cheapest_flight_within_k_stop(
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
        )
    )
