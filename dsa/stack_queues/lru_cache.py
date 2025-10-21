"""
LRU Cache

Design a data structure that follows the constraints of Least Recently Used (LRU) cache.

Implement the LRUCache class:
LRUCache(int capacity): We need to initialize the LRU cache with positive size capacity.
int get(int key): Returns the value of the key if the key exists, otherwise return -1.
void put(int key,int value): Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Examples:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[ [2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4] ]

Output:
 [null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);  // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);  // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);  // return -1 (not found)
lRUCache.get(3);  // return 3
lRUCache.get(4);  // return 4

Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get"]
[[1], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [3]]

Output:
[null, null, null, -1, null, -1, null, -1]

Explanation:
LRUCache lRUCache = new LRUCache(1);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // evicts key 1, cache is {2=2}
lRUCache.get(1);  // returns -1 (not found)
lRUCache.put(3, 3); // evicts key 2, cache is {3=3}
lRUCache.get(2);  // returns -1 (not found)
lRUCache.put(4, 4); // evicts key 3, cache is {4=4}
lRUCache.get(3);  // returns -1 (not found)

Input:
["LRUCache", "put", "put", "get", "put", "put", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [4, 4], [2], [4]]

Output:
[null, null, null, 1, null, null, -1, 4]

Constraints:
1 <= capacity <= 1000
0 <= key <= 104
0 <= value <= 105
At most 105 calls will be made to get and put.
"""


class Node:

    # DLL Node will have key and val also. -1 is used due to question constraint
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.mpp = {}
        self.head = Node()
        self.tail = Node()
        # Dummy head and tail connected to each other
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insertAtHead(self, node):
        temp = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next = temp
        temp.prev = node

    def get(self, key_):
        if key_ in self.mpp:
            node = self.mpp[key_]
            value = node.val
            self.deleteNode(node)
            self.insertAtHead(node)
            return value
        return -1

    def put(self, key_, value):
        # if key_ is already in Cache
        if key_ in self.mpp:
            node = self.mpp[key_]
            node.val = value
            self.deleteNode(node)
            self.insertAtHead(node)
            return

        # When key_ is not in cache and insert is needed, check cache capacity first
        if self.cap == len(self.mpp):
            # find last node to delete
            node = self.tail.prev
            self.deleteNode(node)
            del self.mpp[node.key]

        # Insert this key_ and val as a node in cache
        newNode = Node(key_, value)
        self.insertAtHead(newNode)
        self.mpp[key_] = newNode


if __name__ == "__main__":
    # Test Case 1
    print("Test Case 1:")
    obj = LRUCache(2)
    operations = [
        "LRUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    results = []
    for op, val in zip(
        operations[1:], values[1:]
    ):  # Skip first operation as it's constructor
        if op == "put":
            results.append(obj.put(val[0], val[1]))
        else:
            results.append(obj.get(val[0]))
    print(f"Expected: [null, null, 1, null, -1, null, -1, 3, 4]")
    print(f"Output: {[None] + results}\n")

    # Test Case 2
    print("Test Case 2:")
    obj = LRUCache(1)
    operations = ["LRUCache", "put", "put", "get"]
    values = [[1], [1, 1], [2, 2], [1]]

    results = []
    for op, val in zip(operations[1:], values[1:]):
        if op == "put":
            results.append(obj.put(val[0], val[1]))
        else:
            results.append(obj.get(val[0]))
    print(f"Expected: [null, null, null, -1]")
    print(f"Output: {[None] + results}\n")

    # Test Case 3
    print("Test Case 3:")
    obj = LRUCache(2)
    operations = ["LRUCache", "put", "put", "get", "put", "put", "get", "get"]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [4, 4], [2], [4]]

    results = []
    for op, val in zip(operations[1:], values[1:]):
        if op == "put":
            results.append(obj.put(val[0], val[1]))
        else:
            results.append(obj.get(val[0]))
    print(f"Expected: [null, null, null, 1, null, null, -1, 4]")
    print(f"Output: {[None] + results}")
