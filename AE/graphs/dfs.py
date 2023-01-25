"""

  You're given a Node class that has a name and an array of optional children nodes.
  When put together, nodes form an acyclic tree-like structure. 
  Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree
  using the Depth-first Search approach (specifically navigating the tree from
  left to right), stores all of the nodes' names in the input array, and returns
  it.

  Input:
    graph = 
             A
          /  |  \ 
         B   C   D
        / \     / \ 
       E   F   G   H
          / \   \ 
         I   J   K

  Output:
    ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

"""

# time - O(v+e) | space - O(v), in worst case where one branch has all the nodes,
# space - O(v) + O(v) for the call stack


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)
        return array
