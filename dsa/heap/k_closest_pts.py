"""

973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, target and an integer k,
return the k closest points to the target.

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:

    1 <= k <= points.length <= 10^4
    -10^4 <= xi, yi <= 10^4

"""

import heapq, math


class Solution:
    # TC - O(nlogn), SC - O(n)
    def findKclosest_brute(self, points, target, k):
        """
        Idea:
        - Calculate distace from all points to the target and store in a min heap.
        - Pop out k top elements from the heap
        """
        pq = []

        # helper to calculate Euclidean distance
        def calDist(pt):
            x1 = pt[0]
            y1 = pt[1]

            x2 = target[0]
            y2 = target[1]

            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        for point in points:
            pq.append((calDist(point), point))

        # arrange as min-heap
        heapq.heapify(pq)

        result = []
        for _ in range(k):
            dist, curr_pt = heapq.heappop(pq)
            result.append(curr_pt)

        return result

    # # TC - O(nlogk), SC - O(k)
    def findKclosest_better(self, points, target, k):
        """
        Idea:
        - Above, we maintained a min heap of n size, which is wasteful.
        - Instead, use a min heap of k size
        - Push first k distance(putting them in negative) and points in the k max heap
        - Calc distance from remaining points and compare with the top of the max heap.
            - If -top < curr_distance then:
                 - Pop the top element from heap and push this to dist,points to the heap
                 - Else, continue and do nothing in this iteration
        - Reduces complexity as by having a heap of size k, we reduce the log factor from n to k.
        """
        pq = []

        # helper to calculate Euclidean distance
        def calDist(pt):
            x1 = pt[0]
            y1 = pt[1]
            x2 = target[0]
            y2 = target[1]

            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        for i in range(k):
            pq.append((-1 * calDist(points[i]), points[i]))

        heapq.heapify(pq)

        for i in range(k, len(points)):
            curr_dist = calDist(points[i])
            # handling (-)ve value for max-heap
            if -pq[0][0] > curr_dist:
                heapq.heappop(pq)
                heapq.heappush(pq, (-1 * curr_dist, points[i]))

        result = []
        for _ in range(k):
            dist, curr_pt = heapq.heappop(pq)
            result.append(curr_pt)

        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.findKclosest_brute([[1, 3], [-2, 2]], (0, 0), 1))
    print(obj.findKclosest_better([[1, 3], [-2, 2]], (0, 0), 1))
