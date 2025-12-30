"""

149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:
    1 <= points.length <= 300
    points[i].length == 2
    -104 <= xi, yi <= 104
    All the points are unique.

"""

from collections import defaultdict


class Solution:
    # TC - O(), SC - O()
    def findPts(self, points):
        n = len(points)
        maxPoints = 0

        # If there are 2 or fewer points, all of them are on a line
        if n <= 2:
            return n

        for i in range(n):
            mpp = defaultdict(int)  # Dictionary to store count of slopes
            samePoints = 1  # Count the base point itself
            currMax = 0

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    # Same point, skip as we only care about unique points
                    samePoints += 1
                    continue

                # Reduce the slope to its simplest form
                g = self.gcd(dy, dx)  # Get the greatest common divisor
                if g != 0:
                    dy //= g
                    dx //= g

                # Represent slope as a string (to handle negative signs consistently)
                slope = f"{dy}/{dx}"
                mpp[slope] += 1
                currMax = max(currMax, mpp[slope])

            maxPoints = max(maxPoints, currMax + samePoints)  # Update result

        return maxPoints  # Return the maximum number of points on a line

    # Helper function to calculate the greatest common divisor
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)


if __name__ == "__main__":
    obj = Solution()
    print(obj.findPts([[1, 1], [2, 2], [3, 3]]))
    print(obj.findPts([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
