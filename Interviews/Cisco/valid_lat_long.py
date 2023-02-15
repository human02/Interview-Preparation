"""
You are given a list of strings that may represent valid latitude/longitude pairs.
Your task is to check if the given latitude/longitude pairs are valid or not.
A string (X.Y) is considered valid if the following criteria are met:
*   The string starts with a bracket, has a comma after X and ends with a bracket.
*   There is no space between the opening parenthesis and the first character of X.
*   There is no space between the comma and the last character of X.
*   There is no space between the comma and the first character of
*   There is no space between Y and the closing parenthesis.
*   X and Y are decimal numbers and may be preceded by a sign.
*   There are no leading zeros.
*   No other characters are allowed in X or Y.
*   -90 <= X <= 90 and - 180 <= Y <= 180

Write an algorithm to identify the valid and invalid latitude/longitude pairs from the given list of strings.

Input
The first line of input consists of an integer- input size, representing the size of the string (N).
The next line consists of N space-separated substrings containing the latitude/longitude pairs.

Output
Print N space separated strings representing the valid and invalid latitude/longitude pairs from the given list of strings. Print Valid" for valid pairs and "Invalid" for invalid pairs.

Constraints
1 ≤ Ns 100

Example

Input:
5
(90,180) (+90,+180) (90.,180) (90.0,180.1) (85S.95W)

Output:
Valid Valid Invalid Invalid Invalid

Explanation:
In the given string, substrings {'(90,180)','(+90,+180)'} are valid as they meet the given criteria but substrings
(90.,180) (90.0,180.1) (85S.95W) are invalid as substring (90.,180) has an extra decimal point after 90,
substring (90.0,180.1) contains 180.1 which is out of bound and substring (855,95W) contains characters in it.
"""

import re


def funcValidPairs(inputStr):
    # Write your code here
    n = int(inputStr.strip())
    res = []
    for i in range(n):
        text = inputStr.strip()
        textToMatch = text[1:-1]
        print(textToMatch)
        coordinates = helper(text[1:-1])
        if coordinates:
            # print (*coordinates)
            res.append("Valid")
        else:
            res.append("Invalid")
    return res


def helper(text):
    pattern = r"^\(((\-?|\+?)?\d+(\.\d+)?),\s*((\-?|\+?)?\d+(\.\d+)?)\)$"
    match = re.search(pattern, text)
    if match:
        latitude = float(match.group(1))
        longitude = float(match.group(2))
    if -90 <= latitude <= 90 and -180 < -longitude <= 180:
        return (latitude, longitude)
    return None


def main():
    # input for inputStr
    inputStr = []
    inputStr_size = int(input())
    inputStr = list(map(str, input().split()))
    result = funcValidPairs(inputStr)
    print(" ".join([str(res) for res in result]))


if __name__ == "__main__":
    main()
