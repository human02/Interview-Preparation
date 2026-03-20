"""

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Examples:
Input : str = ["flowers" , "flow" , "fly", "flight"]
Output : "fl"
Explanation :
    All strings given in array contains common prefix "fl".

Input : str = ["dog" , "cat" , "animal", "monkey"]
Output : ""
Explanation :
    There is no common prefix among the given strings in array.

Input : str = ["lady" , "lazy"]
Output: "la"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= str.length <= 200
    1 <= str[i].length <= 200
    str[i] contains only lowercase English letters.

"""

from typing import List


class Solution:
    """
    Idea:
    When a list of strings is sorted lexicographically, 1st str and last str
    in this sorted list will differ the most. The common prefix of these two strs
    is guaranteed to be the longest common prefix across all strings in the array.
    """

    def findLCP(self, strs: List[str]) -> str:
        strs.sort()  # In-Place sorting
        first_str = strs[0]
        last_str = strs[-1]

        n = min(len(first_str), len(last_str))
        i = 0
        while i < n:
            if first_str[i] == last_str[i]:
                i += 1
            else:
                break

        return first_str[:i]


if __name__ == "__main__":
    obj = Solution()
    print(obj.findLCP(["flowers", "flow", "fly", "flight"]))
    print(obj.findLCP(["dog", "cat", "animal", "monkey"]))
    print(obj.findLCP(["lady", "lazy"]))
    print(obj.findLCP(["dog", "racecar", "car"]))
