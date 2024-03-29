"""
"""


def minimumCharactersForWords(words):
    resultDict = {}
    result = []

    for i in words:
        helperCount(i, resultDict)

    # create list using freq dict - resultDict
    for key, val in resultDict.items():
        for _ in range(val):
            result.append(key)
    return result


def helperCount(str, res):
    currReqDict = {}
    # get current word's char requirement
    for val in str:
        if val in currReqDict.keys():
            currReqDict[val] += 1
        else:
            currReqDict[val] = 1

    # Compare current word reqs and add necessary in result dict
    for key, value in currReqDict.items():
        res[key] = max(res.get(key, 0), value)
        # if key in res:
        #     if value > res[key]:
        #         res[key] = value
        # else:
        #     res[key] = value
