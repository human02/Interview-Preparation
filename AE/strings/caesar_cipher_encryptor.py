"""
Caesar Cipher Encryptor

  Given a non-empty string of lowercase letters and a non-negative integer
  representing a key, write a function that returns a new string obtained by
  shifting every letter in the input string by k positions in the alphabet,
  where k is the key.

  Note that letters should "wrap" around the alphabet; in other words, the
  letter "z" shifted by one returns the letter "a".

  Input:
    string = "xyz"
    key = 2

  Output:
    "zab"
    
"""

# O(n) - time | O(n) - space


def caesarCipherEncryptor(string, key):
    res = ""
    for i in range(len(string)):
        # key%26 is necessary because the key inputs can be > than 26 and there are only 26 alphabets.
        tmp = ord(string[i]) + key % 26
  # if value crosses 122 then it passes lowercase alpha limit of ASCII
        if tmp > 122:
            tmp -= 26
        res += chr(tmp)
    return res


print(caesarCipherEncryptor("yza", 2))
