"""

Sort LL

Given the head of a singly linked list. Sort the values of the linked list in non-decreasing order and
return the head of the modified linked list.


Examples:
Input: head -> 5 -> 6 -> 1 -> 2 -> 1
Output: head -> 1 -> 1 -> 2 -> 5 -> 6
Explanation: 1 <= 1 <= 2 <= 5 <= 6

Input: head -> 6 -> 5 -> -1 -> -2 -> -3
Output: head -> -3 -> -2 -> -1 -> 5 -> 6
Explanation: -3 <= -2 <= -1 <= 5 <= 6

Input: head -> -1 -> -2 -> -3 -> -1
Output: head -> -3 -> -2 -> -1 -> -1

Constraints:
    0 <= number of nodes in the linked list <= 1000
    -104 <= ListNode.val <= 104

"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    # TC - O(nlogn) + O(n) + O(n), SC - O(n) + O(n)
    def sortLL_brute(self, head):
        values = []

        # take out all values from LL
        tmp = head
        while tmp:  # O(n)
            values.append(tmp.val)
            tmp = tmp.next

        values.sort()  # O(nlogn)

        dummyHead = ListNode(-1)
        tmp = dummyHead
        for value in values:  # O(n)
            currNode = ListNode(value)
            tmp.next = currNode
            tmp = tmp.next

        return dummyHead.next


# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp:
        # Print the data of the current node
        print(temp.val, end=" ")
        temp = temp.next
    print()


if __name__ == "__main__":
    obj = Solution()

    # Linked List: 5 6 1 2 1
    head = ListNode(5)
    head.next = ListNode(6)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    print("Original Linked List: ", end="")
    printLinkedList(head)

    head = obj.sortLL_brute(head)

    print("Sorted Linked List: ", end="")
    printLinkedList(head)
