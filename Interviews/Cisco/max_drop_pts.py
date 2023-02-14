"""

A pilot was asked to drop food packets in a terrain.
He must fly over the entire terrain only once but cover a maximum number of drop points.
The points are given as inputs in the form of integer co-ordinates in a two-dimensional field.
The flight path can be horizontal or vertical, but not a mix of the two or diagonal.
Write an algorithm to find the maximum number of drop points that can be covered by flying over the terrain once.

Input:
The first line of input consists of an integer- xCoordinate_size, representing the number of x coordinates (N).
The next line consists of N space-separated integers representing the x coordinates.
The third line consists of an integer yCoordinate_size, representing the number of y coordinates (M).
The next line consists of M space-separated integers representing the y coordinates

Output:
Print an integer representing the number of coordinates in the best path which covers the maximum 
number drop points by flying over the terrain once.

Note:
A path is valid path if, more than one drop points are connected 
(Single coordinate don't create any path, so pilot cannot fly over it).

Constraints:
1 < N, M <= 700 (where N is always equal to M)

Example:

Input:
23242
22658

Output:
3

Explanation:
There are 5 coordinates- (2,2), (3,2), (2,6), (4,5) and (2,8).
The best path is the horizontal one covering (2,2), (2,6) and (2,8).
So, the output is 3.

"""

from collections import defaultdict


def funcDrop(xCoordinate, yCoordinate):
    # We will get the list of x an y coordinates here

    x_points = defaultdict(int)
    y_points = defaultdict(int)

    # count the number of occurrences of each x and y coordinate
    for x in xCoordinate:
        x_points[x] += 1
    for y in yCoordinate:
        y_points[y] += 1

    # get the coordinate with the maximum number of occurrences
    max_x = max(x_points, key=x_points.get)
    max_y = max(y_points, key=y_points.get)

    # get the number of points in the best path
    return max(x_points[max_x], y_points[max_y])


def main():
    # input for Coordinate
    xCoordinate = []
    xCoordinate_size = int(input())
    xCoordinate = list(map(int, input().split()))

    # input for Coordinate
    yCoordinate = []
    yCoordinate_size = int(input())
    yCoordinate = list(map(int, input().split()))

    result = funcDrop(xCoordinate, yCoordinate)
    print(result)


if __name__ == "__main__":
    main()
