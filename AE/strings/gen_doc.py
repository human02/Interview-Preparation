"""
Generate Document

  You're given a string of available characters and a string representing a
  document that you need to generate. Write a function that determines if you
  can generate the document using the available characters. If you can generate
  the document, your function should return True, otherwise it should return False.


  You're only able to generate the document if the frequency of unique
  characters in the characters string is greater than or equal to the frequency
  of unique characters in the document string. For example, if you're given
  characters = "abcabc" and document = "aabbccc" you can't generate the document because you are missing one 'c'.


  The document that you need to create may contain any characters, including
  special characters, capital letters, numbers, and spaces.

  Note: you can always generate the empty string ("")

  Input:
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"

  Output:
    True

"""
from collections import Counter


def generateDocument(characters, document):
    # Write your code here.
    char_count = Counter(characters)
    doc_count = Counter(document)
    if not (doc_count - char_count):
        return True
    return False


print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
