"""
LeetCode-style Question:

You are given a network of computers represented as a tree with n nodes, numbered from 1 to n. 
The network is described by two lists, network_from and network_to, where each pair (network_from[i], 
network_to[i]) represents a bidirectional connection between computers.

Each computer has a port type denoted by port[i]. Two computers can communicate directly if they share the same port type.
Any two computers that can communicate with each other(i.e same port type) require a bandwidth equal to the distance(number of edges
on the unique path connecting them.

For every port type that appears at least twice in the network, calculate the total bandwidth as follows:
For every pair of computers with the same port type, the bandwidth between them is equal to the number of edges on 
the unique path connecting them. The total bandwidth is the sum of bandwidths for all such pairs and all port types
that appear at least twice.

Return the total bandwidth for the network.

Example:
Input: network_nodes = 5, network_from = [1,2,1,3], network_to = [2,3,4,5], port = [1,2,1,2,1]
Output: 8

Constraints:
- 1 <= network_nodes <= 10^5
- network_from.length == network_to.length == network_nodes - 1
- 1 <= port[i] <= 10^5
"""


from typing import List, Tuple
"""
edge cases:
1. n <= 1 -> no edges, return 0
2. ports with frequency < 2 -> contribute 0, skip them
3. assumes the graph is a tree rooted at 1 (uses parent[1] = -1)
algo:
1. build adjacency list from network_from/network_to variables
2. build parent[] and postorder[] with an explicit stack from root = 1
3. count tot[c] = number of nodes having port value c
4. for each port c with tot[c] >= 2:
a) init sub[u] = 1 if port[u] == c else 0
b) process nodes in postorder:
- for edge (parent[u], u), let s = sub[u]
- add s * (tot[c] - s) to ans
- sub[parent[u]] += s
5. return ans
t.c - O(n + n * used_ports) 
s.c - O(n)
"""


def findTotalBandwidth(network_nodes: int,
                       network_from: List[int],
                       network_to: List[int],
                       port: List[int]) -> int:
    n = network_nodes
    g = [[] for _ in range(n + 1)]
    for u, v in zip(network_from, network_to):
        g[u].append(v)
        g[v].append(u)

    max_port = max(port)
    tot = [0] * (max_port + 1)
    for p in port:
        tot[p] += 1

    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    order.reverse()

    ans = 0

    for c in range(1, max_port + 1):
        if tot[c] < 2:
            continue
        sub = [0] * (n + 1)
        # initialize leaf counts
        for i in range(1, n + 1):
            sub[i] = 1 if port[i - 1] == c else 0

        for u in order:
            p = parent[u]
            if p != -1:
                # contribution of edge (p,u) for this port
                s = sub[u]
                ans += s * (tot[c] - s)
                sub[p] += sub[u]

    return ans