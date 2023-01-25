"""
  Write a function that takes in a list of unique strings and returns a list of
  semordnilap pairs.

  A semordnilap pair is defined as a set of different strings where the reverse
  of one word is the same as the forward version of the other. For example the
  words "diaper" and "repaid" are a semordnilap pair, as are the words
  "palindromes" and "semordnilap".
  
  The order of the returned pairs and the order of the strings within each pair
  does not matter.

  Input:
    words = ["diaper", "abc", "test", "cba", "repaid"]

  Output:
    [["diaper", "repaid"], ["abc", "cba"]]
"""

# O() time | O() space


def semordnilap(words):
    # if duplicates are removed then no change as the pair will be already found
    wordsSet = set(words)
    semordnilapPair = []

    for i in words:
        # python way to reverse a string
        reverseWord = i[::-1]
        # reverseWord != i so as to prevent palindrome word from skewing the result
        if reverseWord in wordsSet and reverseWord != i:
            semordnilapPair.append([i, reverseWord])
            # deleting both to prevent duplicate pair if the reverse of the word is present in the word list.
            wordsSet.remove(i)
            wordsSet.remove(reverseWord)
    return semordnilapPair
