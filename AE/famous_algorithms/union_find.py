"""
Union Find  = Disjoint set Data Structure


"""
# Tree root as the set representative, make parent maps and map accordingly
# Method 1: add parent map and arbitrarily pick one as parent when union
# Method 2: add rank matrix also and union with better rank 0(logn(n))
# Method 3: update mapping at find() by removing the mid parent values (PATH-COMPRESSION)


# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind_1:
    def __init__(self):
        self.parents = {}

    # O(1) time | O(1) space
    def createSet(self, value):
        # self as parent
        self.parents[value] = value

    # O(n) time | O(1) space
    def find(self, value):
        # 1st find if the value even exists
        if value in self.parents:
            currParent = value
            while currParent != self.parents[currParent]:
                currParent = self.parents[currParent]
            return currParent
        else:
            return None

    # O(n) time | O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)

        self.parents[valueTwoRoot] = valueOneRoot


class UnionFind_2:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) time | O(1) space
    def createSet(self, value):
        # self as parent
        self.parents[value] = value
        # initial value set to 0
        self.ranks[value] = 0

    # O(logn(n)) time from balanced tree structure | O(1) space
    def find(self, value):
        # 1st find if the value even exists
        if value in self.parents:
            currParent = value
            while currParent != self.parents[currParent]:
                currParent = self.parents[currParent]
            return currParent
        else:
            return None

    # O(logn(n)) time from balanced tree structure  | O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        # Decide based on rank
        if self.ranks[valueOneRoot] < self.ranks[valueTwoRoot]:
            self.parents[valueOneRoot] = valueTwoRoot
        elif self.ranks[valueOneRoot] > self.ranks[valueTwoRoot]:
            self.parents[valueTwoRoot] = valueOneRoot
        else:
            self.parents[valueTwoRoot] = valueOneRoot
            self.ranks[valueOneRoot] += 1


class UnionFind_3:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) time | O(1) space
    def createSet(self, value):
        # self as parent
        self.parents[value] = value
        # initial value set to 0
        self.ranks[value] = 0

    # O(Ɑ(n)) time inverse accumen function of n,approx O(1) | O(Ɑ(n)) time ,approx O(1) space
    def find(self, value):
        # 1st find if the value even exists
        if value not in self.parents:
            return None
        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]

    # O(logn(n)) time from balanced tree structure  | O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        # Decide based on rank
        if self.ranks[valueOneRoot] < self.ranks[valueTwoRoot]:
            self.parents[valueOneRoot] = valueTwoRoot
        elif self.ranks[valueOneRoot] > self.ranks[valueTwoRoot]:
            self.parents[valueTwoRoot] = valueOneRoot
        else:
            self.parents[valueTwoRoot] = valueOneRoot
            self.ranks[valueOneRoot] += 1
