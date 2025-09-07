"""
A travelling salesperson lives in a country that has road_nodes houses and m roads. The ith road runs from house x[i]
to house y[i] and has length t[i]. The roads are directional, meaning its not possible to travel from y[i] to x[i]
using the same road.

For each house i, determine the length of the shortest cycle that starts and ends at house i. If there is no such
path exists, return 0 for that house.

Notes:
- There are no multiple roads between two houses.
- There can be roads that start and end at the same house.
- All houses may or may not be connected.

Example:
Input: road_nodes = 4, roads_from = [1,2,3,4], roads_to = [2,3,1,3], roads_weight = [14,23,23,30]
Output: [60,60,60,0]
Explanation: The shortest path for each house is:
House 1: 1 -> 2 -> 3 -> 1 with length 60
House 2: 2 -> 3 -> 1 -> 2 with length 60
House 3: 3 -> 1 -> 2 -> 3 with length 60
House 4: No cycle exists, return 0

Constraints:
- 1 <= road_nodes <= 1000
- 1 <= m <= 1000
"""

import heapq

def getMinimumLength(road_nodes, roads_from, roads_to, roads_weight):
    n = road_nodes
    # adjacency list for forward graph: edges of the form (u -> v, w)
    adj = [[] for _ in range(n + 1)]
    # adjacency list for reverse graph: store incoming edges (v <- u, w)
    # This is needed so when we run Dijkstra from s, we can easily check
    # all nodes v that connect back into s by a direct edge (v -> s).
    rev = [[] for _ in range(n + 1)]

    # Build the graph
    for u, v, w in zip(roads_from, roads_to, roads_weight):
        adj[u].append((v, w))   # forward edge (used in Dijkstra relaxations)
        rev[v].append((u, w))   # reverse edge (used to detect cycles ending at v)

    INF = 10**30  # a large number representing infinity

    # Standard Dijkstra’s algorithm (min-heap) to compute shortest paths from src
    def dijkstra(src):
        dist = [INF] * (n + 1)   # initialize distances
        dist[src] = 0
        pq = [(0, src)]          # (distance, node)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:     # skip if this is a stale entry
                continue
            # relax outgoing edges from u
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist

    ans = [0] * n
    # For each house s, compute the shortest cycle starting and ending at s
    for s in range(1, n + 1):
        dist = dijkstra(s)   # shortest paths from s to all other nodes
        best = INF
        # Why check incoming edges via rev[s]?
        # Because any cycle through s must:
        #   (1) leave s by some path s -> ... -> v
        #   (2) then return to s by a direct edge (v -> s, w)
        # So, for every incoming edge (v -> s, w),
        # if dist[v] is finite, we have a cycle:
        #   s -> ... -> v -> s  with length dist[v] + w.
        for v, w in rev[s]:
            if dist[v] < INF:   # there is a path s -> v
                best = min(best, dist[v] + w)
        # If no valid cycle found, answer is 0
        ans[s - 1] = 0 if best == INF else best

    return ans