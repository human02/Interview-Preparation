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
