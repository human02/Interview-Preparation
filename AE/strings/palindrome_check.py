"""
Difficulty - Easy

Palindrome Check

Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward.
Note that single-character strings are palindromes.

Input - "abcdcba"
Output - true

"""


def isPalindrome(string):
    start = 0
    end = len(string)-1
    while (start < end):
        if (string[start] != string[end]):
            return False
        start += 1
        end -= 1

    return True
