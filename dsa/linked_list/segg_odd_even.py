"""
Segregate odd and even nodes in LL

Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even
indices and return the reordered list. Consider the 1st node to have index 1 and so on. The relative order of
the elements inside the odd and even group must remain the same as the given input.

Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5
Output: head -> 1 -> 3 -> 5 -> 2 -> 4
Explanation: The nodes with odd indices are 1, 3, 5 and the ones with even indices are 2, 4.

Input: head -> 4 -> 3 -> 2 -> 1
Output: head -> 4 -> 2 -> 3 -> 1
Explanation: The nodes with odd indices are 4, 2 and the ones with even indices are 3, 1.

Input: head -> 1
Output: head -> 1

Constraints:
    0 <= number of nodes in the Linked List <= 105
    0 <= ListNode.val <= 104

"""


class ListNode:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class Solution:
    # TC - O(2*(n/2)) = O(n), SC - O(1)
    def seggOddEven(self, head):
        if head is None or head.next is None:
            return None
        odd = head
        even = head.next
        firstEven = head.next

        # need to reach the 2nd last even only
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        # Now put even list at the end of odd list
        odd.next = firstEven
        return head


# Function to print the linked list
def printLL(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    obj = Solution()

    # Create a linked list with given values
    arr = [1, 3, 4, 2, 5, 6]
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])
    head.next.next.next.next = ListNode(arr[4])
    head.next.next.next.next.next = ListNode(arr[5])

    # Print the original linked list
    print("Original Linked List: ", end="")
    printLL(head)

    # Rearrange the list and print it
    print(obj.seggOddEven(head))
    print("New Linked List: ", end="")
    printLL(head)
