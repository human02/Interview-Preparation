"""

Find the intersection point in the two LL

Given the heads of two linked lists A and B, containing positive integers.
Find the node at which the two linked lists intersect. If they do intersect,
return the node at which the intersection begins, otherwise return null.

The Linked List will not contain any cycles. The linked lists must retain their original structure,
given as per the input, after the function returns.

Note: for custom input, the following parameters are required(your program is not provided with these parameters):

intersectVal - The value of the node where the intersection occurs. This is -1 if there is no intersected node.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node(-1 if no intersection).
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node(-1 if no intersection).
listA - The first linked list.
listB - The second linked list.

Examples:
Input: listA: intersectVal = 4, skipA = 3, skipB = 2, head -> 1 -> 2 -> 3 -> 4 -> 5, listB: head -> 7 -> 8 -> 4 -> 5
Output(value at returned node is displayed): 4
Explanation: The two lists have nodes with values 4 and 5 as their tails.

Input: listA: intersectVal = -1, skipA = -1, skipB = -1, head -> 1 -> 2 -> 3, listB: head -> 8 -> 9
Output(value at returned node is displayed): null
Explanation: The two lists do not intersect.

Input: listA: intersectVal = 4, skipA = 0, skipB = 0, head -> 4 -> 5 -> 6, listB: head -> 4 -> 5 -> 6
Output: 4

Constraints:
    m == number of nodes in listA.
    n == number of nodes in listB.
    1 <= m, n <= 5 * 104
    0 <= ListNode.val <= 104
    0 <= skipA < m
    0 <= skipB < n
    intersectVal, skipA, skipB is -1 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

"""
