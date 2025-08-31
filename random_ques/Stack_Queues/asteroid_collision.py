"""
Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

When two asteroids meet, the smaller one will explode. If they are the same size, both will explode. 
Asteroids moving in the same direction will never meet.

Input: asteroids = [2, -2]
Output: []
Explanation: The asteroid with size 2 and the one with size -2 collide, exploding each other.

Input: asteroids = [10, 20, -10]
Output: [10, 20]
Explanation: The asteroid with size 20 and the one with size -10 collide, resulting in the remaining asteroid with size 20. 
The asteroids with sizes 10 and 20 never collide.

Input: asteroids = [10, 2, -5]
Output:
[10]

Constraints:
·  2 <= asteroids.length <= 105
·  -106 <= asteroids[i] <= 106
·  asteroids[i] != 0

"""