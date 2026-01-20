"""

Alien Dictionary

Given a sorted dictionary of an alien language having N words and K starting alphabets of a standard dictionary.
Find the order of characters in the alien language. There may be multiple valid orders for a particular test case,
thus you may return any valid order as a string. The output will be True if the order returned by the function is
correct, else False denoting an incorrect order. If the given arrangement of words is inconsistent with any possible
letter ordering, return an empty string "".

Examples:
Input: N = 5, K = 4, dict = ["baa","abcd","abca","cab","cad"]
Output: b d a c
Explanation:
    We will analyze every consecutive pair to find out the order of the characters.
    The pair “baa” and “abcd” suggests 'b' appears before 'a' in the alien dictionary.
    The pair “abcd” and “abca” suggests 'd' appears before 'a' in the alien dictionary.
    The pair “abca” and “cab” suggests 'a' appears before 'c' in the alien dictionary.
    The pair “cab” and “cad” suggests 'b' appears before 'd' in the alien dictionary.
    So, ['b', 'd', 'a', 'c'] is a valid ordering.

Input: N = 3, K = 3, dict = ["caa","aaa","aab"]
Output: c a b
Explanation: Similarly, if we analyze the consecutive pair
    for this example, we will figure out ['c', 'a', 'b'] is a valid ordering.

Input: N = 3, K = 3, dict = ["abc", "bca", "cab"]
Output: a b c

Constraints:
    1 ≤ N, M ≤ 300
    1 ≤ K ≤ 26
    1 ≤ dict[i].length ≤ 50

"""

from collections import deque


class Solution:
    # TC - O(V+E), SC - O(V+E)
    def findOrder(self, n, k, dic):
        adjL = [[] for _ in range(k)]

        # finding which char order, create Adj List
        for i in range(n - 1):
            word1 = dic[i]
            word2 = dic[i + 1]
            char_len = min(len(word1), len(word2))
            j = 0
            while j < char_len:
                if word1[j] != word2[j]:
                    # make sure to use int value as its index
                    u = ord(word1[j]) - ord("a")
                    v = ord(word2[j]) - ord("a")
                    adjL[u].append(v)
                    break
                j += 1

        topo_result = self.topoSort(adjL, k)

        if topo_result:
            return " ".join(topo_result)
        else:
            return []

    # topological sorting - O(V+E), O(V)
    def topoSort(self, adjL, V):
        indeg = [0] * V
        q = deque()

        # calculate indeg
        for i in range(V):
            for it in adjL[i]:
                indeg[it] += 1

        # all with indeg 0 added to q
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for nei in adjL[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        if len(result) == V:
            # converting index values to chars
            for i in range(len(result)):
                result[i] = chr(result[i] + ord("a"))
            return result
        return []


if __name__ == "__main__":
    obj = Solution()
    print(obj.findOrder(5, 4, ["baa", "abcd", "abca", "cab", "cad"]))
    print(obj.findOrder(3, 3, ["caa", "aaa", "aab"]))
    print(obj.findOrder(3, 3, ["abc", "bca", "cab"]))
