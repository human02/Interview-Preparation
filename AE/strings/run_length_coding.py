"""
Run-Length Coding

  Write a function that takes in a non-empty string and returns its run-length encoding.

  From Wikipedia, "run-length encoding is a form of lossless data compression in
  which runs of data are stored as a single data value and count, rather than as
  the original run." For this problem, a run of data is any sequence of
  consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".

  To make things more complicated, however, the input string can contain all
  sorts of special characters, including numbers. And since encoded data must be
  decodable, this means that we can't naively run-length-encode long runs. For
  example, the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as "12A" , since this string can be decoded as
  either "AAAAAAAAAAAA" or "1AA". Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the
  aforementioned run should be encoded as "9A3A".

  Input:
    string = "AAAAAAAAAAAAABBCCCCDD"

  Output:
    "9A4A2B4C2D"

"""

# Hashmap wont work as the input can be "aAaAbbbbddd" and hashmap method will give wrong result.


def runLengthEncoding(string):
    # Write your code here.
    # using list as insertion is O(1) while str is o(n) as it immutable.
    encodedStrChars = []
    currRunLen = 1
    # Starting from 2nd index as its mentioned that the string is non-empty
    for i in range(1, len(string)):
        currChar = string[i]
        prevChar = string[i-1]
        if (currChar != prevChar or currRunLen == 9):
            encodedStrChars.append(str(currRunLen))
            encodedStrChars.append(prevChar)
            currRunLen = 0
        currRunLen += 1

    # but we will not print the last part, so handling it here
    encodedStrChars.append(str(currRunLen))
    encodedStrChars.append(string[len(string)-1])

    # converting list to string
    return "".join(encodedStrChars)


print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
