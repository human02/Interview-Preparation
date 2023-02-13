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
1 < N, M 5 700 (where N is always equal to M)

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
