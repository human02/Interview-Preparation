"""
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
"""


class Solution:
    def encode(self, strs):
        s = ""
        for wrd in strs:
            s += str(len(wrd)) + "#" + wrd
        return s

    def decode(self, s):
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            res.append(s[start : start + length])
            i = start + length
        return res
