"""

"""

# O(1) time --> as we can only make 256 addresses per byte and IPs consist of 4 bytes:
# Therefore 256*256*256*256 = 2^32, so O(2^32) = O(1) irrespective of the string length.
# O(1) space --> as upperbound we can only have 2^32 addresses which is not literally possible with an input.


def validIPAddresses(string):
    ipAddressesFound = []
    # cant have valid IPs if length < 4

    # starting from index 1 as we cant place '.' on the 0 index
    # also checking for OutofBounds error when len(string) < 4
    for i in range(1, min(len(string), 4)):
        currIPAddrParts = ["", "", "", ""]

        currIPAddrParts[0] = string[:i]
        if not isValidPart(currIPAddrParts[0]):
            continue  # case where this part is not valid

        # 2nd period(.) loop
        # start 1 index ahead as above logic
        for j in range(
            i + 1, min(len(string), i + 4)
        ):  # THE RANGE END LOGIC DIDN'T UNDERSTAND
            currIPAddrParts[1] = string[i:j]
            if not isValidPart(currIPAddrParts[1]):
                continue  # case where this part is not valid

            # 3rd & 4th period(.) loop
            # start 1 index ahead as above logic
            for k in range(j + 1, min(len(string), j + 4)):
                currIPAddrParts[2] = string[j:k]
                currIPAddrParts[3] = string[k:]

                if isValidPart(currIPAddrParts[2]) and isValidPart(currIPAddrParts[3]):
                    ipAddressesFound.append(".".join(currIPAddrParts))

    return ipAddressesFound


def isValidPart(string):
    # removes any 0s that are before a value. eg '01' become 1
    stringInt = int(string)
    if stringInt > 255:
        return False
    # check for leading 0s
    return len(string) == len(str(stringInt))


validIPAddresses("    ")
