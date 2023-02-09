"""
"""

# Division method wont work as the numners can have 0 as well.


# O(n^2) time | O(n) space
def arrayOfProducts_brute(array):
    prods = []

    for i in range(len(array)):
        prod = 1
        for j in range(len(array)):
            if i != j:
                prod *= array[j]
        prods.append(prod)

    print(prods)
    return prods


# O(n) time | O(n) space
def arrayOfProducts(array):
    # cant leave empty as assignment wont work then.
    left = [1 for _ in range(len(array))]
    right = [1 for _ in range(len(array))]
    result = [1 for _ in range(len(array))]

    # calculate prod till left of index
    i = 0
    prod = 1
    while i < len(array):
        left[i] = prod
        prod *= array[i]
        i += 1

    # calculate prod from end till right of index
    i = len(array) - 1
    prod = 1
    while i >= 0:
        right[i] = prod
        prod *= array[i]
        i -= 1

    #  calculate sum of the final
    i = 0
    while i < len(array):
        result[i] = left[i] * right[i]
        i += 1

    print(result)
    return result
    print(left, "\n", right)


# O(n) time | O(n) space
def arrayOfProducts_optimised(array):
    # cant leave empty as assignment wont work then.
    result = [1 for _ in range(len(array))]

    # calculate prod till left of index
    i = 0
    prod = 1
    while i < len(array):
        result[i] = prod
        prod *= array[i]
        i += 1

    # calculate prod from end till right of index
    i = len(array) - 1
    prod = 1
    while i >= 0:
        result[i] *= prod
        prod *= array[i]
        i -= 1

    print(result)
    return result
    print(left, "\n", right)


arrayOfProducts([5, 1, 4, 2])
